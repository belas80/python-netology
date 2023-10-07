import os.path
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        file_for_upload = os.path.split(file_path)[1]
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + file_for_upload, 'overwrite': 'true'}
        resp_geturl = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params=params,
            headers=headers
        )
        # resp_geturl.raise_for_status()
        if resp_geturl.status_code != requests.codes.ok:
            return f'При получении ссылки для загрузки произошла ошибка (код: {resp_geturl.status_code})'
        href = resp_geturl.json()['href']
        with open(file_path, 'rb') as f:
            response = requests.put(href, files={"file": f})
        if response.status_code not in (requests.codes.created, requests.codes.accepted):
            return f'При загрузке файла произошла ошибка (код: {response.status_code})'
        return f'Файл {file_for_upload} успешно загружен на Яндекс.Диск'


if __name__ == '__main__':
    with open('token', 'r') as t:
        my_token = t.read()
    uploader = YaUploader(my_token)
    result = uploader.upload('file_for_upload.png')
    print(result)
