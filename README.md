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

## Note
* 2021年現在、apiサーバ側がTLS1.2以降に対応していないため、`IRKit Internet HTTP API`を用いるとブラウザ側で接続が拒否されてしまい、APIに接続できない。
* 現在はIRkitと同じnetwork内のサーバ（LatitudeE6400 TL-WN725N）にコンテナを立て `IRKit Device HTTP API` を用いて稼働中。
* 上記のAPIの違いにより、`const.py`, `post_irkit.py`において差異がある。
