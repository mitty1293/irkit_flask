# ベースイメージ
FROM python:3

# 必要パッケージインストール
# apache2-devはmod_wsgiのインストールに必要
RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    apache2-dev

COPY requirements.txt /tmp

RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt

COPY config/flask.conf /etc/apache2/sites-available/

RUN a2ensite flask

EXPOSE 80

CMD [ "/usr/sbin/apachectl", "-D", "FOREGROUND"]