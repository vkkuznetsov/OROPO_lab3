from copy import deepcopy
import json
import requests

TOKEN_sec = ""
USER_ID_sec = "368564385"


def get_friends(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/friends.get"
    params["fields"] = "contacts"
    response = requests.get(url, params=params)
    return response.json()


def process_friend_list(friend_list):
    return [friend['first_name'] + " " + friend['last_name'] for friend in friend_list]


def get_groups(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/groups.get"
    params['extended'] = 1
    response = requests.get(url, params=params)
    return response.json()


def process_group_list(group_list):
    return [group['name'] for group in group_list]


def get_followers(params):
    params = deepcopy(params)
    url = f"https://api.vk.com/method/users.getFollowers"
    params['fields'] = "screen_name"
    response = requests.get(url, params=params)
    return response.json()


if __name__ == "__main__":

    TOKEN = input("Enter TOKEN = ")
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
    answer = dict()

    result = get_friends(params)
    answer['friends'] = process_friend_list(result['response']['items'])

    result = get_groups(params)
    answer['groups'] = process_group_list(result['response']['items'])

    result = get_followers(params)
    answer['followers'] = process_friend_list(result['response']['items'])
    with open('user.json', 'w', encoding='UTF-8') as f:
        json.dump(answer, f, ensure_ascii=False, indent=4)
