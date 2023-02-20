import requests

from config import url_backend


def get_key(telegram_id):
    response = requests.get(url_backend, params={'user_id': telegram_id})

    if response.status_code == 404:
        return False
    else:
        return response


def send_username_and_id(username, telegram_id):
    response = requests.post(url_backend, json={
        'telegram_id': telegram_id,
        'username': username
    })

    if response.status_code == 201:
        return False
    else:
        return True
