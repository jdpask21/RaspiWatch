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
3. 以下のコマンドを実行し、サービスを有効化し、起動してください。
GUIアプリケーションなので、--userが必須になります。システム用のサービスで起動しても、どのユーザーにもGUIが紐づいていないので、何も表示されていません。（このあたりはXサーバーと呼ばれる仕組みで紐づけが実現されているようです。）  
```
systemctl --user daemon-reload
systemctl --user enable raspiwatch.service
systemctl --user start raspiwatch.service
```
また、`systemctl --user start raspiwatch.service`を`~/.bashrc`などに記述しておくことで、起動時に自動的にGUIアプリケーションを起動することができます。  
サービスを削除するには以下のコマンドを実行します。（参考用）
```
sudo systemctl disable raspiwatch.service
sudo systemctl stop raspiwatch.service
sudo rm /etc/systemd/system/raspiwatch.service
sudo systemctl daemon-reload
```