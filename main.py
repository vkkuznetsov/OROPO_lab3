from copy import deepcopy

import requests

TOKEN_sec = "vk1.a.iD8A2g4QA6gAe0x0QmqlmwFy8rz0QjMUHltAnTLkFqIUPfLWO8uz56n1gSIvyL02YnyhBrTGHGkFjhjvTp38UbtVamIhzHeeYg5lSxHpzblCnQv1XMZIiwjq7Pz79rQ5mSkpBaDkkPP8W8n41ve_vpwE28R7X2rtPUW8rtmlGoJfJU1poVPSSi9bY7xkjUzh"
USER_ID_sec = "287263552"


def get_friends(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/friends.get"
    params["fields"] = "contacts"
    response = requests.get(url, params=params)
    return response.json()


def process_friend_list(friend_list):
    for friend in friend_list:
        formatted_friend = friend['first_name'] + " " + friend['last_name']
        print(formatted_friend)


def get_groups(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/groups.get"
    params['extended'] = 1
    response = requests.get(url, params=params)
    return response.json()


def process_group_list(group_list):
    for group in group_list:
        formatted_friend = group['name'] + " "
        print(formatted_friend)


def get_followers(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/users.getFollowers"
    params['fields'] = "screen_name"
    response = requests.get(url, params=params)
    return response.json()


if __name__ == "__main__":

    TOKEN = input("Enter TOKEN (enter to use mine) = ")
    print(TOKEN_sec)
    if not TOKEN:
        TOKEN = TOKEN_sec

    USER_ID = input("Enter USER_ID (enter to use 368564385) = ")
    if not USER_ID:
        USER_ID = USER_ID_sec

    params = {
        "user_id": USER_ID,
        "v": "5.199",
        "access_token": TOKEN,
    }

    result = get_friends(params)
    print(result)
    process_friend_list(result['response']['items'])

    result = get_groups(params)
    process_group_list(result['response']['items'])

    result = get_followers(params)
    process_friend_list(result['response']['items'])
