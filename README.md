概要
===========
websocketとRedisのpubsubを利用し、お知らせをリアルタイムで通知するサンプルソース

前提条件(ざっくり)
===========
・Python3  
・websockets https://pypi.org/project/websockets/
・Redis(ミドルウェア)
・Flask
・redis(Pythonのライブラリ) https://pypi.org/project/redis/

※以下のコマンドはMac基準    

インストール
===========
※Redisはローカルホストで動いていると想定(インストール必要)。リモートサーバーのRedisを使う場合はソースコードからホスト情報を書き換えてください。
```
% git clone https://gitlab.efactoryguys.com/JEONG/python-websocket-pubsub.git
% cd python-websocket-pubsub
% python3 -m venv venv
% . venv/bin/activate
(venv) % pip install websockets
(venv) % pip install Flask
(venv) % pip install redis
```

動作確認
===========
※ローカルのRedisを使う場合は事前に起動しておいてください。(redis-server)

1. ターミナルでソケットサーバーを起動
```
(venv) % python3 socket-server.py
```
2. ターミナルでAPIサーバーを起動
```
(venv) % python3 api-server.py
```
3. Windowsエクスプローラー or MacFinder等でmypage.htmlを実行
```
例えば
file:///Users/jeong/dev/python-websocket-pubsub/mypage.html
```
4. 別のブラウザでお知らせ送信前画面を表示
```
http://127.0.0.1:5000/pushpage/
```
5. 送信ボタンを押下すると、mypage.htmlの表示が変わる(お知らせを受信)