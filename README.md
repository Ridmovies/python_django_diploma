
# Megano

## Description
This project is a backend for an online store, developed using Django, Django REST framework and Redis. 
It includes a system of authorization, registration, user credentials management, 
as well as the functionality of a product catalog, a review system, a shopping cart and checkout.


## Fast install with Docker and sqlite
```bash
docker-compose -f sqlite-docker-compose.yaml up --build
```



## Installation with Docker
1. Clone the repo
   ```bash
   git clone https://gitlab.skillbox.ru/riddler_rid/python_django_diploma.git
   ```
   
2. Install Docker Engine
* https://docs.docker.com/engine/install/
* https://docs.docker.com/engine/install/ubuntu/

3. Enter the application root folder:
``` 
cd python_advanced_diploma 
```

4. Run docker-compose 
   ```bash
    docker-compose up 
   ```
   
### Creating a superuser
```bash
docker exec -it megano python manage.py createsuperuser
```

### Импорт всех данных:

```bash
python manage.py loaddata fixtures/all_data.json
```



## Installation with Virtual Environment
1. Clone the repo
   ```bash
   git clone https://gitlab.skillbox.ru/riddler_rid/python_django_diploma.git
   ```

2. Create a virtual environment in the project's root folder:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash 
   source venv/bin/activate 
   ```

4. Install dependencies for the production environment:
   ```bash
    pip install -r requirements.txt
   ```
   
5. Change .env file
* Create postgres database or launch postgres docker 
* Rename '.env.template' to '.env'
* Replace the settings with your own
   
6. Perform a database migration:
   ```bash
   python manage.py migrate
   ```

### Запустить Redis на локальной машине

8. Start your application:   
   ```bash
    python manage.py runserver
   ```
   
<!-- USAGE EXAMPLES -->
## Usage

### Creating a superuser
```bash
python manage.py createsuperuser --username=root --email=root@example.com
```

* ### Start page application
        http://127.0.0.1:8000/

* ### Admin Panel
        http://127.0.0.1:8000/admin

* ### Swagger UI (API)
        http://127.0.0.1:8000/api/schema/swagger-ui/


   ```bash

```

# Develop

## Работа с fixtures
### Экспорт всех данных:
   ```bash
python manage.py dumpdata > fixtures/all_data.json --format=json 
```


### Экспорт данных конкретной модели:

```bash
python manage.py loaddata product_app.Product >fixtures/products-fixtures.json --format=json
```

### Импорт всех данных:

```bash
python manage.py loaddata fixtures/all_data.json
```


## Команды для работы с Docker Compose
Эти команды помогут управлять контейнерами и образами в вашем проекте, обеспечивая удобный процесс разработки и тестирования.

## Для запуска консоли внутри работающего Docker-контейнера используется команда docker exec
```bash
docker exec -it megano bash 
```


### Остановка и удаление всех сервисов и образов

```bash
docker-compose down --rmi all
```
Эта команда останавливает и удаляет все сервисы, созданные с помощью `docker-compose`, а также удаляет образы, использованные этими сервисами.

### Сборка нового образа

```bash
docker-compose build
```
Эта команда собирает новый образ на основе инструкций в `docker-compose.yml`.

### Запуск сервисов

```bash
docker-compose up 
```
Запускает сервисы, определенные в `docker-compose.yml`.



### Просмотр активных контейнеров

```bash
docker ps
```
Отображает список запущенных контейнеров.

### Принудительная остановка всех контейнеров

```bash
docker stop $(docker ps -aq)
```
Останавливает все активные контейнеры.

### Удаление всех остановленных контейнеров

```bash
docker rm $(docker ps -aq)
```
Удаляет все остановленные контейнеры.



## Команды для работы с Redis
### Запустить Redis на локальной машине
```bash
sudo service redis-server start
```

### Запустить Redis в Docker
```bash
docker build -f Dockerfile-redis -t my-redis-image .
docker run -p 6379:6379 my-redis-image
```

### Запустить Redis и Celery в Docker
```bash
docker-compose -f docker-compose-dev.yml up
```



## Линтеры:
```bash
black --check --diff .\product_app\views.py

isort --check-only --diff --profile black .\product_app\views.py

mypy --incremental ./product_app/views.py 
```


## Тестирование
```bash
python manage.py test
```
