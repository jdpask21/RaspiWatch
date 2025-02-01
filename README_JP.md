# RaspiWatch

Fletフレームワークでビルドされたデスクトップクロックアプリケーションです。時刻、温度、湿度、天気情報を表示します。このアプリケーションはRaspberry PiとDHT22温湿度センサーで動作するように設計されています。

[English version here](README.md)

## 特徴

- リアルタイムの時計表示
- 大阪の現在の天気状況
- 温度と湿度のモニタリング（DHT22センサーが必要）
- 6時間ごとの天気更新
- フルスクリーン表示対応

## 必要条件

- Raspberry Pi
- Python 3.7以上
- DHT22温湿度センサー
- Raspberry PiのGPIOピンD18が利用可能であること

## ハードウェアのセットアップ

1. DHT22センサーをRaspberry Piに接続します：
   - センサーのデータピンをGPIO18（ピンD18）に接続
   - VCCを3.3Vまたは5V電源に接続
   - GNDをグラウンドに接続
   - データピンとVCCピンの間に10KΩ抵抗を接続

## インストール

1. リポジトリをクローンします：
```bash
git clone https://github.com/yourusername/RaspiWatch.git
```

2. 必要なパッケージをインストールします：
```bash
pip install -r requirements.txt
```

## 使用方法

アプリケーションを起動するには、以下のコマンドを実行します：
```bash
cd RaspiWatch
flet run watch_app
```

## ライセンス

このプロジェクトはApache License 2.0の下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。
