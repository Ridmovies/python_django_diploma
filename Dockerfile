FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

COPY ./diploma-frontend /code

RUN pip install --upgrade -r /code/requirements.txt -v

COPY . /code

#EXPOSE 5000
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]


# docker-compose build
# docker build . -t django-megano
# docker run -d -p 5000:5000 django-megano


# docker rm my_fastapi
# docker rmi final2-web
# docker logs
# docker volume ls
# docker volume prune
# docker system prune --all --volumes

