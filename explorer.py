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
        visited_directions = {} # room_id -> set(visited exits for this room_id)
        map = {} # direction goes to
        traversal_path = []
        backtracking = Stack()
        response = api.init()
        available_exits, cooldown = response["exits"], response["cooldown"]

        # We're only done after we've visited all rooms.
        while len(visited_directions) < num_rooms:
            print(f"Waiting {cooldown} second(s).")
            time.sleep(cooldown)

            if map.get(response["room_id"]) is None:
                map[response["room_id"]] = {}

            if visited_directions.get(response["room_id"]) is None:
                visited_directions[response["room_id"]] = set()

            unvisited_exits = [ex for ex in available_exits if ex not in visited_directions[response["room_id"]]]

            if len(unvisited_exits) > 0: # we can keep exploring.
                direction = random.choice(unvisited_exits)
                new_response = api.move(direction)
                map[response["room_id"]][direction] = new_response["room_id"]
                available_exits, cooldown = new_response["exits"], new_response["cooldown"]
                visited_directions[response["room_id"]].add(direction)
                traversal_path.append(direction)

                # Save the opposite direction of the one we just traveled.
                # If we run into a dead end at some point, we'll need to move backwards.
                backtracking.push((opposite_direction_mapping[direction], response["room_id"]))
            else: # we've reached a dead end and must move backwards.
                backtracking_direction, backtracking_room_id = backtracking.pop()
                new_response = api.move(backtracking_direction, backtracking_room_id)
                available_exits, cooldown = new_response["exits"], new_response["cooldown"]
                traversal_path.append(backtracking_direction)

explorer = Explorer()
explorer.explore(500)