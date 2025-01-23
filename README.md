# pet_sitter_be

## Установка и запуск

Для работы с проектом необходим `Python` версии `3.12` или новее, установленные RabbitMQ и PostgreSQL. 

1) Клонируйте git репозиторий
```commandline
git clone <адрес репозитория>
```
2) Активируйте виртуальное окружение в корне проекта:
```commandline
pip install virtualenv
python -m virtualenv venv 
.\venv\Scripts\activate 
```
3) Установите `poetry` в вашем виртуальном окружении
```commandline
python -m pip install poetry
```
4) Установите зависимости
```commandline
python -m poetry install
```
5) Создайте .env файл, скопировав шаблон из .env_template и пропишите перменные окружения

6) Выполните миграции
```commandline
cd web
python manage.py makemigrations
python manage.py migrate
```
7) Запустите сервер
```commandline
python manage.py runserver
```

## Docker
Для работы с docker необходимо:
1) Установить Docker(если у вас Windows, установите Docker Desktop и WSL): https://docs.docker.com/engine/install/ubuntu/

2) В корне проекта соберите контейнер:
```commandline
docker compose -f docker-compose.yaml build
```

3) Запустите приложение:
```commandline
docker compose -f docker-compose.yaml up -d
```
