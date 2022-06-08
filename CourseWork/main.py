import requests
from pprint import pprint
from datetime import date

class VkToYaUploader:
    def __init__(self, vk_token: str, ya_token: str):
        self.vk_token = vk_token
        self.ya_token = ya_token

    def ya_upload(self, file_url, file_name):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'Netology/{file_name}', 'url': file_url}
        response = requests.post(upload_url, headers=headers, params=params)

        response.raise_for_status()
        if response.status_code == 202:
            print("Файл загружен")
        else:
            print(f"Файл не загружен. Ошибка {response.status_code}")

    def get_largest(self, size_dict):
        if size_dict['width'] >= size_dict['height']:
            return size_dict['width']
        else:
            return size_dict['height']

    def vk_download(self, id):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': id,
            'access_token': vk_token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': True,
            'photo_sizes': True
        }

        names = []
        res = requests.get(URL, params=params)
        photos = res.json()
        for photo in photos['response']['items']:
            likes = photo['likes']['count']
            sizes = photo['sizes']
            max_sizes = max(sizes, key=self.get_largest)
            file = max_sizes['url']
            if likes in names:
                likes = f'{likes}_{date.today()}'
            names.append(likes)
            self.ya_upload(file, likes)


if __name__ == '__main__':
    u_id = 552934290
    vk_token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
    ya_token = ' '
    uploader = VkToYaUploader(vk_token, ya_token)
    result = uploader.vk_download(u_id)

