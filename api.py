import requests
import os
import json
import time
from dotenv import load_dotenv
from util import Queue

load_dotenv()
base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
bc_base_url = "https://lambda-treasure-hunt.herokuapp.com/api/bc/"

headers = {
    "Authorization": f"Token {os.getenv('API_KEY')}"
}

map = {}

with open("map.json", "r") as f:
    map = {}

    with open("map.json", "r") as f:
        try:
            map = json.loads(f.read())
        except:
            pass


def init():
    response = requests.get(f"{base_url}init/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def move(direction, next_room_id=None):
    dictionary = {"direction": direction}

    if next_room_id:
        dictionary["next_room_id"] = str(next_room_id)

    response = requests.post(
        f"{base_url}move/", headers=headers, json=dictionary)
    print(response.text)
    json = response.json()
    return json


def take_item(item_name):
    response = requests.post(
        f"{base_url}take/", headers=headers, json={"name": item_name})
    print(response.text)
    json = response.json()
    return json


def drop_item(item_name):
    response = requests.post(
        f"{base_url}drop/", headers=headers, json={"name": item_name})
    print(response.text)
    json = response.json()
    return json


def sell_item(item_name):
    response = requests.post(
        f"{base_url}sell/", headers=headers, json={"name": item_name, "confirm": "yes"})
    print(response.text)
    json = response.json()
    return json


def status():
    response = requests.post(
        f"{base_url}status/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def examine(name):
    response = requests.post(
        f"{base_url}examine/", headers=headers, json={"name": name})
    print(response.text)
    json = response.json()
    return json


def wear_item(item_name):
    response = requests.post(
        f"{base_url}wear/", headers=headers, json={"name": item_name})
    print(response.text)
    json = response.json()
    return json


def undress_item(item_name):
    response = requests.post(
        f"{base_url}undress/", headers=headers, json={"name": item_name})
    print(response.text)
    json = response.json()
    return json


def change_name(name):
    response = requests.post(
        f"{base_url}change_name/", headers=headers, json={"name": name, "confirm": "aye"})
    print(response.text)
    json = response, json()
    return json


def pray():
    response = request.post(
        f"{base_url}pray/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def fly(direction):
    response = request.post(
        f"{base_url}fly/", headers=headers, json={"direction": direction})
    print(response.text)
    json = response.json()
    return json


def dash(direction, num_rooms=None, next_room_ids=None):
    dictionary = {"direction": direction}

    if num_rooms > 1:
        if next_room_ids:
            dictionary["next_room_ids"] = next_room_ids

    response = requests.post(
        f"{base_url}dash/", headers=headers, json=dictionary)
    print(response.text)
    json = response.json()
    return json


def carry(name):
    response = request.post(
        f"{base_url}carry/", headers=headers, json={"name": name})
    print(response.text)
    json = response.json()
    return json


def receive():
    response = request.post(
        f"{base_url}receive/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def warp():
    response = request.post(
        f"{base_url}warp/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def recall():
    response = request.post(
        f"{base_url}recall/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def mine_proof(new_proof):
    response = request.post(
        f"{bc_base_url}mine/", headers=headers, json={"proof": new_proof})
    print(response.text)
    json = response.json()
    return json


def last_proof():
    response = request.get(
        f"{bc_base_url}last_proof/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def get_balance():
    response = request.get(
        f"{bc_base_url}get_balance/", headers=headers)
    print(response.text)
    json = response.json()
    return json


def transmogrify(item_name):
    response = request.post(
        f"{base_url}transmogrify/", headers=headers, json={"name": item_name})
    print(response.text)
    json = response.json()
    return json

def navigate_to(target_room_id):
    init_response = init()
    print(f"Waiting {init_response['cooldown']} second(s).")
    time.sleep(init_response["cooldown"])

    current_room_id = str(init_response["room_id"])
    target_room_id = str(target_room_id)

    visited = {}
    queue = Queue()
    queue.enqueue([current_room_id])

    while queue.size() > 0:
        path = queue.dequeue()
        last_room_id = str(path[-1])
        exits = map[last_room_id]["available_exits"]

        if last_room_id not in visited:
            visited[last_room_id] = path

            for exit in exits:
                queue.enqueue(path.copy() + [str(map[last_room_id]["exits"][exit])])

    room_id_path = visited[target_room_id][1:]
    traversal_path = []

    current_room_exits = map[current_room_id]["exits"]

    for room_id in room_id_path:
        direction = list(current_room_exits.keys())[list(current_room_exits.values()).index(int(room_id))]
        traversal_path.append((direction, room_id))
        current_room_exits = map[str(room_id)]["exits"]

    for path in traversal_path:
        response = move(path[0], path[1])
        print(f"Waiting {response['cooldown']} second(s).")
        time.sleep(response["cooldown"])

def navigate_to_shop():
    navigate_to(1)

def navigate_to_pirate():
    navigate_to(467)

def navigate_to_holloway_shrine():
    navigate_to(22)

def navigate_to_fully_shrine():
    navigate_to(22)

def navigate_to_linh_shrine():
    navigate_to(461)

def navigate_to_donut_shop():
    navigate_to(15)

def navigate_to_wishing_well():
    navigate_to(55)

if __name__ == "__main__":
    navigate_to_wishing_well()