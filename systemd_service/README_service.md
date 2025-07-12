# systemdサービスを使用し、ラズパイが起動後に自動でWatchアプリケーションが起動するための手順

1. 以下のコマンドで、シェルスクリプトに実行権限を与えてください。
```
chmod +x ~/github/RaspiWatch/systemd_service/start_watch_app.sh
```
2. 以下のコマンドを実行し、serivceファイルをsystemd/userフォルダに移動させてください。(serviceファイルのorkingDirectoryについては、ユーザー名を自身のものに変更してください。)
```
mkdir -p ~/.config/systemd/user
cp ~/github/raspi_smartwatch/RaspiWatch/raspiwatch.service ~/.config/systemd/user/
```
2. 以下のコマンドを実行し、サービスを有効化し、起動してください。
```
sudo systemctl daemon-reload
sudo systemctl enable raspiwatch.service
sudo systemctl start raspiwatch.service
```