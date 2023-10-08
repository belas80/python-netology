import requests

API_BASE_URL = 'https://api.vk.com/method/'
VERSION = '5.131'
with open('token', 'r') as t:
    TOKEN = t.read()


class VkUser:

    def __init__(self, user_id=None):
        self.headers = {
            'Authorization': 'Bearer ' + TOKEN
        }
        self.params = {
            'v': VERSION
        }
        self.user_id = user_id
        if self.user_id is None:
            self.user_id = requests.get(
                API_BASE_URL + 'users.get',
                headers=self.headers,
                params=self.params
            ).json()['response'][0]['id']

    def get_vk_users(self):
        user_params = {
            'user_ids': self.user_id,
            'fields': 'followers_count, friend_status'
        }
        result = requests.get(API_BASE_URL + 'users.get', headers=self.headers, params={**self.params, **user_params})
        return result.json()

    def search_vk_users(self, name, birth_year, hometown):
        search_params = {
            'q': name,
            'birth_year': birth_year,
            'hometown': hometown,
            'fields': 'bdate'
        }
        result = requests.get(
            API_BASE_URL + 'users.search',
            headers=self.headers,
            params={**self.params, **search_params})
        return result.json()

    def get_vk_followers(self):
        followers_params = {
            'user_id': self.user_id,
            'count': 1000,
            # 'fields': 'maiden_name'
        }
        result = requests.get(API_BASE_URL + 'users.getFollowers',
                              headers=self.headers,
                              params={**self.params, **followers_params})
        return result.json()['response']['items']

    def get_vk_friends(self):
        friends_params = {'user_id': self.user_id}
        result = requests.get(API_BASE_URL + 'friends.get',
                              headers=self.headers,
                              params={**self.params, **friends_params})
        if 'error' in result.json():
            print(f'Ошибка. Не могу получить список друзей user_id {self.user_id}: '
                  f'{result.json()["error"]["error_msg"]}')
            exit(1)
        return result.json()['response']['items']

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

    def __and__(self, other):
        return [VkUser(friend_id) for friend_id in set(self.get_vk_friends()) & set(other.get_vk_friends())]


def get_common_friends():
    user1_id = input('Введите пользователя 1: ')
    user1 = VkUser(user1_id)
    print(user1)
    user2_id = input('Введите пользователя 2: ')
    user2 = VkUser(user2_id)
    print(user2)
    print('Общие друзья:')
    common_friends = user1 & user2
    for f in common_friends:
        print(f)


if __name__ == '__main__':
    get_common_friends()
    # print(VkUser().get_vk_users())
