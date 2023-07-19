# ドローンエンジニア養成塾15期アプリケーションコース修了課題
SITLで動作する、Pymavlinkスクリプトです。<br>
*実機では絶対に実行しないで下さい！！*

前提条件<br>
・pymavlinkをインストールする<br>
・python3が実行できること<br>
・シミュレータ起動時は、"-L Kawachi"オプションを付けて下さい。<br>
・python実行にあたり、追加で必要なパッケージはありません

実行方法
WSL(Ubuntu)のターミナルを2つ開き、それぞれでSITL実行とpymavlinkスクリプトの実行をして下さい<br>
$ sim_vehicle.py -v Copter --console -L Kawachi<br>
$ python task.py


