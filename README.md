# irkit_flask
IRkitを用いて家電操作を行う。Flaskで構築。

## to build & run
```
docker-compose up -d
```

## Usage
`http://<server-ip>:8000`にブラウザから接続するとリモコンが表示される。

## Setting change
家電機器の変更、追加により赤外線信号の修正が必要な際は`app.py` `const.py` `index.html` を修正する。

## 課題
2021年現在、apiサーバ側がTLS1.2以降に対応していないっぽい。<br>
なのでブラウザからアクセスした際にブラウザ側で接続拒否を起こしている。
⇒自分でサーバ立てるか。。。
