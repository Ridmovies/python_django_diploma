FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

COPY ./diploma-frontend /code

RUN pip install --upgrade -r /code/requirements.txt -v

COPY . /code

