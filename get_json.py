import requests


def get_json():
    """
    Return a json object from Twitter Api, using bearer token.
    """
    base_url = "https://api.twitter.com/1.1/friends/list.json"

    # input here youe bearer token:
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAFx4MwEAAAAA%2FZcsDE86L0w2He8EjBi1JbfDiMc%3DKysXA5FGeaV53qiLXXdmmXl62pa43vwhpFbpioTgromw6asmqZ"

    search_headers = {
        "Authorization": f'Bearer {bearer_token}'
    }
    search_params = {
        "screen_name": "@BarackObama",  # input here a username
        "count": 4
    }

    response = requests.get(base_url, headers=search_headers, params=search_params)
    return response.json()
