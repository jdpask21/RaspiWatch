# RaspiWatch

Fletでビルドされたデスクトップクロックアプリケーションです。時刻、温度、湿度、天気情報を表示します。このアプリケーションは、DHT22温湿度センサーを搭載したRaspberry Piでの実行を想定しており、SwitchBotデバイスの制御もサポートしています。

[English version here](README.md)

## 機能

- リアルタイムの時計表示
- 大阪の現在の天気状況
- 温度と湿度のモニタリング（DHT22センサーが必要）
- 6時間ごとの天気更新
- フルスクリーン表示対応
- SwitchBotデバイス制御機能
  - 現在はAM312人感センサーを使用したライト制御に対応
  - 今後のアップデートで複数のデバイスタイプをサポート予定
  - 人の存在検知に基づく自動ライト制御

## 必要条件

- Raspberry Pi
- Python 3.7以上
- DHT22温湿度センサー
- Raspberry PiのGPIOピンD18が利用可能であること
- AM312人感センサー
- SwitchBotアカウントと対応デバイス

## ハードウェアのセットアップ

1. DHT22センサーをRaspberry Piに接続:
   - センサーのデータピンをGPIO18（ピンD18）に接続
   - VCCを3.3Vまたは5V電源に接続
   - GNDをグラウンドに接続

2. AM312人感センサーの接続:
   - VCCをGPIOピン2（5V電源）に接続
   - GNDをGPIOピン9（グラウンド）に接続
   - OUTをGPIOピン37（GPIO26）に接続

## インストール

1. リポジトリのクローン:
```bash
git clone https://github.com/yourusername/RaspiWatch.git
```

2. デバイスIDの取得（不明な場合）:
```bash
python watch_app/src/get_device_id.py
```
このスクリプトを実行すると、利用可能なSwitchBotデバイスとそのIDの一覧が表示されます。

3. SwitchBotの認証情報の設定:
```bash
python setup.py
```
SwitchBot APIトークン、シークレット Token、デバイスIDの入力を求められます。これらの認証情報の取得方法については、[SwitchBot APIドキュメント](https://github.com/OpenWonderLabs/SwitchBotAPI)を参照してください。

4. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

アプリケーションを起動するには、以下を実行します:
```bash
cd RaspiWatch
flet run watch_app
```

## ライセンス

このプロジェクトはApache License 2.0の下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。