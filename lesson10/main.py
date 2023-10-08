import requests
from pprint import pprint


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.headers = {
            'Authorization': 'Bearer ' + self.token
        }
        self.params = {
            'v': self.version
        }
        self.owner_id = requests.get(
            self.url + 'users.get',
            headers=self.headers,
            params=self.params
        ).json()['response'][0]['id']

    def get_vk_users(self, ids=None):
        if ids is None:
            ids = self.owner_id
        user_params = {
            'user_ids': ids,
            'fields': 'followers_count, friend_status'
        }
        result = requests.get(self.url + 'users.get', headers=self.headers, params={**self.params, **user_params})
        return result.json()

    def search_vk_users(self, name, birth_year, hometown):
        search_params = {
            'q': name,
            'birth_year': birth_year,
            'hometown': hometown,
            'fields': 'bdate'
        }
        result = requests.get(self.url + 'users.search', headers=self.headers, params={**self.params, **search_params})
        return result.json()

    def get_vk_followers(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        followers_params = {
            'user_id': user_id,
            'count': 1000,
            # 'fields': 'maiden_name'
        }
        result = requests.get(self.url + 'users.getFollowers',
                              headers=self.headers,
                              params={**self.params, **followers_params})
        return result.json()['response']['items']


if __name__ == '__main__':
    with open('token', 'r') as t:
        my_token = t.read()
    user1_id = '1'
    user2_id = '556711874'
    vk_user = VkUser(token=my_token, version='5.131')
    vk_user1 = vk_user.get_vk_followers(user_id=user1_id)
    vk_user2 = vk_user.get_vk_followers(user_id=user2_id)
    friends = list(set(vk_user1) & set(vk_user2))
    print(friends)
