FROM python:3.7

ENV FLASK_HOST='localhost'

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python","-u","requester.py" ]
