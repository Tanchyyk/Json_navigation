import json
from collections.abc import Iterable


def check_type(data):
    """
    Check type of an object. Return False if it is dictionary or list, True - otherwise.
    """
    if isinstance(data, str):
        return True
    elif isinstance(data, Iterable):
        return False
    return True


def get_value_from_json(path):
    """
    Function helps you to navigate in json object.
    """
    with open(path, "r") as file:
        data = json.load(file)

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
