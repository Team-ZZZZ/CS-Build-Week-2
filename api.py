import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
bc_base_url = "https://lambda-treasure-hunt.herokuapp.com/api/bc/"

headers = {
    "Authorization": f"Token {os.getenv('API_KEY')}"
}


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
        f"{base_url}sell/", headers=headers,json={"name": item_name, "confirm": "yes"})
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


def status():
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
        f"{base_url}carry/", headers=headers, json= {"name": name})
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