import os.path
import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        file_for_upload = os.path.split(file_path)[1]
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + file_for_upload, 'overwrite': 'true'}
        resp_geturl = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params=params,
            headers=headers
        )
        resp_geturl.raise_for_status()
        href = resp_geturl.json()['href']
        with open(file_path, 'rb') as f:
            response = requests.put(href, files={"file": f})
            response.raise_for_status()
        return response


if __name__ == '__main__':
    with open('token', 'r') as t:
        my_token = t.read()
    uploader = YaUploader(my_token)
    result = uploader.upload('file_for_upload.png')
