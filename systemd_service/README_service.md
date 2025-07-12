# systemdサービスを使用し、ラズパイが起動後に自動でWatchアプリケーションが起動するための手順

1. 以下のコマンドで、シェルスクリプトに実行権限を与えてください。
```
chmod +x ~/github/RaspiWatch/systemd_service/start_watch_app.sh
```
2. 以下のコマンドを実行し、サービスを有効化し、起動してください。
```
sudo systemctl daemon-reload
sudo systemctl enable raspiwatch.service
sudo systemctl start raspiwatch.service
```