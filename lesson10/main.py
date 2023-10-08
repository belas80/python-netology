import requests


def get_vk_user(ids, token):
    url = 'https://api.vk.com/method/users.get'

    headers = {
        'Authorization': 'Bearer ' + token
    }

    params = {
        # 'user_ids': ids,
        'v': '5.131'
    }

    result = requests.get(url, headers=headers, params=params)
    return result.json()


if __name__ == '__main__':
    with open('token', 'r') as t:
        my_token = t.read()
    print(get_vk_user(1, my_token))
