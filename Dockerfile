FROM python:3

WORKDIR /app

RUN pip3 install flask

RUN pip3 install Pillow

RUN pip3 install numpy

RUN pip3 install requests

RUN pip3 install gunicorn

RUN pip3 install gevent

RUN apt-get -y update

COPY . /app

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "3", "--timeout=360", "-k", "gevent"]
