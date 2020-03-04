import random
import api
import time
import json
from util import Stack

opposite_direction_mapping = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e",
}

class Explorer:
    def explore(self, num_rooms):
        map = {}

        with open("map.json", "r") as f:
            try:
                map = json.loads(f.read())
            except:
                pass

        traversal_path = []
        backtracking = Stack()

        with open("backtracking.txt", "r") as f:
            backtracking.stack = f.read().splitlines()

        response = api.init()
        available_exits, cooldown = response["exits"], response["cooldown"]
        num_visited_rooms = 0

        for room in map.values():
            for available_exit in room["available_exits"]:
                if available_exit in room["visited_exits"]:
                    num_visited_rooms += 1
                    break

        # We're only done after we've visited all rooms.
        while num_visited_rooms < num_rooms:
            print(f"Waiting {cooldown} second(s).")
            time.sleep(cooldown)

            for item_name in response["items"]:
                if item_name == "tiny treasure" or item_name == "small treasure":
                    continue

                item_response = api.take_item(item_name)
                print(f"Waiting {item_response['cooldown']} second(s).")
                time.sleep(item_response["cooldown"])

            if map.get(str(response["room_id"])) is None:
                map[str(response["room_id"])] = {
                    "visited_exits": [],
                    "exits": {},
                    "available_exits": response["exits"],
                    "title": response["title"],
                    "description": response["description"],
                    "coordinates": response["coordinates"],
                }

            unvisited_exits = [ex for ex in available_exits if ex not in map[str(response["room_id"])]["visited_exits"]]

            if len(unvisited_exits) > 0: # we can keep exploring.
                direction = random.choice(unvisited_exits)
                new_response = api.move(direction)
                map[str(response["room_id"])]["exits"][direction] = new_response["room_id"]
                available_exits, cooldown = new_response["exits"], new_response["cooldown"]
                map[str(response["room_id"])]["visited_exits"].append(direction)
                traversal_path.append(direction)

                if map.get(str(new_response["room_id"])) is None:
                    map[str(new_response["room_id"])] = {
                        "visited_exits": [],
                        "exits": {},
                        "available_exits": new_response["exits"],
                        "title": new_response["title"],
                        "description": new_response["description"],
                        "coordinates": new_response["coordinates"],
                    }

                # Save the opposite direction of the one we just traveled.
                # If we run into a dead end at some point, we'll need to move backwards.
                opposite_direction = opposite_direction_mapping[direction]
                map[str(new_response["room_id"])]["exits"][opposite_direction] = response["room_id"]
                map[str(new_response["room_id"])]["visited_exits"].append(opposite_direction)
                backtracking.push(opposite_direction)

                response = new_response
            else: # we've reached a dead end and must move backwards.
                num_visited_rooms += 1
                backtracking_direction = backtracking.pop()
                new_response = api.move(backtracking_direction, map[str(response["room_id"])]["exits"][backtracking_direction])
                available_exits, cooldown = new_response["exits"], new_response["cooldown"]
                traversal_path.append(backtracking_direction)

                response = new_response

            with open("map.json", "w") as f:
                f.write(json.dumps(map))
            
            with open("backtracking.txt", "w") as f:
                f.writelines(s + "\n" for s in backtracking.stack)
        
        print("Success!")

explorer = Explorer()
explorer.explore(500)