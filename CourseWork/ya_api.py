import requests
import json


class YaUploader:
    def __init__(self, ya_token: str):
        self.ya_token = ya_token

    def ya_upload(self, file_url, file_name, size_photo):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': f'OAuth {self.ya_token}'}
        params = {'path': f'Netology/{file_name}', 'url': file_url}
        response = requests.post(upload_url, headers=headers, params=params)
        response.raise_for_status()

        f_name = f'{file_name}.jpg'
        data = [{"file_name": f_name, "size": size_photo}]

        if response.status_code == 202:
            with open('upload_files.json', 'a') as outfile:
                json.dump(data, outfile)
        else:
            print(f"Файл не загружен. Ошибка {response.status_code}")
