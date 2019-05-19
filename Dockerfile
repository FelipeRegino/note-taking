FROM python:3

MAINTAINER FelipeRegino

WORKDIR /var/www

COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt

CMD flask run --host=0.0.0.0
