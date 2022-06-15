from vk_api import VkDownloaderPhoto


if __name__ == '__main__':
    user_id = int(input('Введите ID пользователя: '))
    vk_token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
    ya_token = input('Введите Токен ЯндексДиска: ')
    quantity = input('Введите количество фото: ')
    if quantity == '':
        quantity = 5

    uploader = VkDownloaderPhoto(vk_token, ya_token)
    result = uploader.vk_download(user_id, int(quantity))
