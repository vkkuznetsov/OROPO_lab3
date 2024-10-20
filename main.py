import requests

TOKEN_sec = "vk1.a.MvU3sowe64m9tGqa7G7NIYPfn9eFMMfG3K2XzAmf_e_NGsF2BuJcgkQn4kPFAx3db-95Y3ipmcwZof8Eu76MQ3XNm41ff_eVSz6QrilkO3CAZJMVZtKNlAPnwJS_efHarPCI3OLxTK8XQDUFmWWNz7UVkbYDGsUQ_9bPPTEtTmvEw-0NpCHhG2jURXJGNFgS"
USER_ID_sec = "368564385"


def get_friends(user_id, token):
    url = f"https://api.vk.com/method/friends.get"
    params = {
        "user_id": user_id,
        "v": "5.199",
        "access_token": token,
        "fields": "contacts"
    }
    response = requests.get(url, params=params)
    return response.json()


def process_friend_list(friend_list):
    for friend in friend_list:
        formatted_friend = friend['first_name'] + " " + friend['last_name']
        print(formatted_friend)

if __name__ == "__main__":
    TOKEN = input("Enter TOKEN (enter to use mine) = ")
    if not TOKEN:
        TOKEN = TOKEN_sec
    USER_ID = input("Enter USER_ID (enter to use 368564385) = ")
    if not USER_ID:
        USER_ID = USER_ID_sec

    result = get_friends(USER_ID, TOKEN)
    process_friend_list(result['response']['items'])
