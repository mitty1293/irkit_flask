# irkit_flask
IRkitを用いて家電操作を行う。Flaskで構築。

## to build & run
```
docker-compose up -d
```

## Usage
`http://ip or host:9000`にブラウザから接続するとリモコンが表示される。

## Setting change
家電機器の変更、追加により赤外線信号の修正が必要な際は`app.py` `const.py` `index.html` を修正する。
