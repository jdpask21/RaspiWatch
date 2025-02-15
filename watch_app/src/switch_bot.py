import os
import json
import requests
import hashlib
import hmac
from datetime import datetime, timezone
from typing import Dict, Any

SWITCHBOT_API_TOKEN = ''   #your api token
SWITCHBOT_API_SECRET = ''   # your secret api token
SWITCHBOT_DEVICE_ID = ''   # your device ID
#TODO: add feature to operate N-device in this application

class SwitchBotController:
    """SwitchBotデバイスを制御するクラス"""

    def __init__(self, token: str, secret: str, device_id: str):
        """
        SwitchBotコントローラーの初期化

        Args:
            token (str): SwitchBot APIトークン
            secret (str): SwitchBot APIシークレット
            device_id (str): 制御するデバイスのID
        """
        self.base_url = "https://api.switch-bot.com/v1.0"
        self.token = token
        self.secret = secret
        self.device_id = device_id

    def _generate_headers(self) -> Dict[str, str]:
        """
        認証ヘッダーを生成する

        Args:

        Returns:
            Dict[str, str]: 認証ヘッダー
        """
        return {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

    def _make_api_request(self, method: str = "GET", payload: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        SwitchBot APIにリクエストを送信する

        Args:
            endpoint (str): APIエンドポイント
            method (str): HTTPメソッド
            payload (dict): リクエストペイロード

        Returns:
            Dict[str, Any]: APIレスポンス
        """
        try:
            headers = self._generate_headers()
            devices = "/devices/"
            commands = "/commands"
            full_url = f"{self.base_url}{devices}{SWITCHBOT_DEVICE_ID}{commands}"

            if method == "GET":
                response = requests.get(full_url, headers=headers)
            elif method == "POST":
                response = requests.post(full_url, headers=headers, data=json.dumps(payload))
            else:
                raise ValueError(f"サポートされていないメソッド: {method}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"APIリクエストエラー: {e}")
            print(f"レスポンス内容: {e.response.text if hasattr(e, 'response') else 'なし'}")
            return {}

    def turn_on_light(self) -> bool:
        """デバイスのライトをONにする"""
        payload = {
            "command": "turnOn",
        }
        response = self._make_api_request(method="POST", payload=payload)
        return response.get("statusCode") == 100

    def turn_off_light(self) -> bool:
        """デバイスのライトをOFFにする"""
        payload = {
            "command": "turnOff",
            "parameter": "default",
            "deviceId": self.device_id
        }
        response = self._make_api_request(method="POST", payload=payload)
        return response.get("statusCode") == 100

def main():
    """
    メイン関数: SwitchBotライトの操作デモ
    環境変数からAPIトークン、シークレット、デバイスIDを取得
    """
    # 環境変数からAPIトークン、シークレット、デバイスIDを取得
    token = SWITCHBOT_API_TOKEN
    secret = SWITCHBOT_API_SECRET
    device_id = SWITCHBOT_DEVICE_ID

    if not token or not secret or not device_id:
        print("環境変数 SWITCHBOT_API_TOKEN、SWITCHBOT_API_SECRET、または SWITCHBOT_DEVICE_ID が設定されていません。")
        return

    # SwitchBotコントローラーの初期化
    controller = SwitchBotController(token, secret, device_id)

    # ライトをONにする
    if controller.turn_on_light():
        print("ライトをONにしました。")
    else:
        print("ライトのON操作に失敗しました。")

if __name__ == "__main__":
    main()