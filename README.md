# ドローンエンジニア養成塾15期アプリケーションコース修了課題
SITLで動作する、Pymavlinkスクリプトです。<br>
*実機では絶対に実行しないで下さい！！*

## 前提条件<br>
・pymavlinkをインストールする。<br>
・python3が実行できること。<br>
・シミュレータ起動時は、"-L Kawachi"オプションを付けて下さい。<br>
・python実行にあたり、追加で必要なパッケージはありません。

## 実行方法<br>
WSL(Ubuntu)のターミナルを2つ開き、それぞれでSITL実行とpymavlinkスクリプトの実行をして下さい。<br>
なお、SITL起動直後にpymavlinkスクリプトを実行するとフライトモード変更出来ない事があります。<br>
30秒ほど待ってからpymavlinkスクリプトを実行してください。<br>
$ sim_vehicle.py -v Copter --console -L Kawachi<br>
$ python task.py


