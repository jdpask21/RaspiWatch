import pprint

import requests


def get_device_id(token):
    """Get device id from SwitchBot Cloud API."""
    url = "https://api.switch-bot.com/v1.0/devices"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception("Failed to get device id from SwitchBot Cloud API.")
    return res.json()

if __name__ == "__main__":
    token = input("Enter your token: ")
    pprint.pprint(get_device_id(token))