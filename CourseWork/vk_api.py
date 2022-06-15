import requests
from datetime import date
import time
from progress.bar import IncrementalBar
from ya_api import YaUploader


class VkDownloaderPhoto:
    def __init__(self, vk_token: str, ya_token: str):
        self.vk_token = vk_token
        self.ya_token = ya_token

    def get_largest(self, size_dict):
        if size_dict['width'] >= size_dict['height']:
            return size_dict['width']
        else:
            return size_dict['height']

    def vk_download(self, user_id, quantity):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': user_id,
            'access_token': self.vk_token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': True,
            'photo_sizes': True
        }

        names = []
        res = requests.get(URL, params=params)
        photos = res.json()

        bar = IncrementalBar('Загрузка', max=quantity)
        index = 0

        for photo in photos['response']['items']:
            bar.next()
            time.sleep(1)

            likes = photo['likes']['count']
            sizes = photo['sizes']
            max_sizes = max(sizes, key=self.get_largest)
            type_size = max_sizes['type']
            file = max_sizes['url']

            if likes in names:
                likes = f'{likes}_{date.today()}'
            names.append(likes)

            uploader = YaUploader(self.ya_token)
            result = uploader.ya_upload(file, likes, type_size)

            index += 1
            if index == quantity:
                bar.finish()
                break
