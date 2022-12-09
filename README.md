Cards Service
---
Техническое задание
---
Необходимо создать веб-приложение для управления базой данных бонусных карт 
(карт лояльности, кредитный карт и т.д. Я встречал много вариаций).

Описание
---
Cards Service - REST API для управления базой данных бонусных карт

Функционал
---
- вывод списка карт с возможностью фильтрации
- добавление/измение/удаление продуктов
- создание/удаление заказов
- просмотр профиля карты с историей покупок по ней
- активация/деактивация карт
- удаление карт
- генерирование набора новых карт
- автоматическое деактивация карт с истекшим сроком активности

Системные требования
---
- Windows / Linux / MacOS
- Docker
- Docker-compose

Стек 
---
- Python
- Django
- PostgreSQL
- Nginx
- gunicorn
- Docker, docker-compose
- Redis

Зависимости
---
- Django==4.1.3
- djangorestframework==3.14.0  
- psycopg2=2.9.5
- gunicorn==20.1.0
- celery==5.2.7  
- redis==4.3.4
- django-filter==22.1


Запуск проекта
---
1.  Клонировать проект и перейти в его корень:

		git clone https://github.com/Kolobok99/cards_service
		cd cards_service

2. Создать директорию с .env.prod. файлами
		
	    cd backend
		mkdir .env.prod
		cd .env.prod

3. Инициализировать .env.settings со следующими переменными:

	    DEBUG=0
		SECRET_KEY={your_secret_key}
		DJANGO_ALLOWED_HOSTS={your_host_ip}

        POSTGRES_NAME=cards_db
	    POSTGRES_USER=manager
	    POSTGRES_PASSWORD={your_sql_password}
	    POSTGRES_HOST=db
	    POSTGRES_PORT={your_sql_port}
        
		DATABASE=postgres
        
        REDIS_HOST=redis
        REDIS_PORT=6379 

4. Инициализировать .env.prod.db со следующими переменными:

		POSTGRES_DB=stripe_db
		POSTGRES_USER=manager
		POSTGRES_PORT={your_sql_port}
		POSTGRES_PASSWORD={your_sql_password}

5. Инициализировать .env.prod.celery со следующими переменными:

		DB_HOST=db
		DB_NAME=cards_db
		DB_USER=manager
		DB_PASS={your_sql_password}

6. Собрать проект

		cd ../docker-composes
		docker compose -f docker-compose.prod.yml build

6. Запустить проект

		docker compose -f docker-compose.prod.yml up


Документация API:
---
    - GET  api/v1/products/ - получить список всех продуктов
    - POST api/v1/products/ - добавить новый продуктов
    - GET  api/v1/products/{id}/ получить продукт по его id
    - PATCH api/v1/products/{id}/ изменить данные продукта по его id
    - DELETE api/v1/product/{id}/ удалить продукта по его id

	- GET  api/v1/orders/ - получить список всех заказов
    - POST api/v1/orders/ - добавить новый заказ
    - GET  api/v1/orders/{id}/ получить заказ по его id
    - DELETE api/v1/orders/{id}/ удалить заказ по его id

	- GET  api/v1/cards/ - получить список всех карт
	- POST api/v1/cards/generation/ - сгенерировать список карт
	- GET  api/v1/cards/activation/{number}/ - активировать/деактивировать карту по ее number
	- GET api/v1/cards/{number}/ - получить профиль карты с историей покупок по ее number
	- DELETE api/v1/cards/{number}/ удалить карту по ее number

