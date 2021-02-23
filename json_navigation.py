from collections.abc import Iterable
import requests


def get_json_object():
    """
    Return a json object from Twitter Api, using bearer token.
    """
    base_url = "https://api.twitter.com/1.1/friends/list.json"

    # input here your bearer token:
    bearer_token = ""

    search_headers = {
        "Authorization": f'Bearer {bearer_token}'
    }
    search_params = {
        "screen_name": "@BarackObama",  # input here a username
        "count": 4
    }

    response = requests.get(base_url, headers=search_headers, params=search_params)
    return response.json()


def check_type(data):
    """
    Check type of an object. Return False if it is dictionary or list, True - otherwise.
    """
    if isinstance(data, str):
        return True
    elif isinstance(data, Iterable):
        return False
    return True


def get_value_from_json(data):
    """
    Function helps you to navigate in json object.
    Return a value of the key, you have input.
    """

    while True:
        print(data.keys())
        print("Choose and type a key: ")
        user_key = input()

        if check_type(data[user_key]):
            return data[user_key]

        if isinstance(data[user_key], list):
            if len(data[user_key]) == 0:
                print("This list is empty!")
                return data[user_key]

            print("The value for this key is a list!")
            print(f'"Enter an index from 0 to {len(data[user_key]) - 1}: ')
            index = int(input())

            if isinstance(data[user_key][index], dict):
                data = data[user_key][index]
                print("The value for this key is a dictionary!")

        elif isinstance(data[user_key], dict):
            print("The value for this key is a dictionary!")
            data = data[user_key]

# Print: get_value_from_json(get_json_object()) to test a program
# Do not forget to inpet a bearer token in line 12
