### kvartirka_test_task
# REST API для системы комментариев блога.
Позволяет создавать статьи и древовидные комментарии. 

## Возможности:
- Методы **POST, GET** - добавление статьи, и получение списка статей
```
/articles/ - 
```
/articles/ - 
Стек: Python 3.10, Django 4.0, DRF, django-mptt, PostgreSQL, pipenv
## Начало работы:
#### Необходимо наличие установненной версии Python 3.10.4

Установите pipenv, если не сделали этого раньше

```sh
pip install pipenv
```

Скопируйте репозиторий

```sh
git clone https://github.com/menyanet73/kvartirka_test_task.git
```

Перейдите в репозиторий

```sh
cd kvartirka_test_task
```

Включите виртуальную среду

```sh
pipenv shell
```

Установите зависимости

```sh
pipenv sync --dev
```

#### Для выполнения следующих манипуляций необходимо наличие установленной PostgreSQL.
Создайте нового пользователя PostgreSQL с полными полномочиями и со следующими данными:
  USER = DBUser
  PASSWORD = netuser
Создайте новую базу данных с названием BlogDB.
Либо измените соответствующие настройки в поле DATABASES, в файле kvartirka_test_task/blog/settings.py

Примените миграции:

```sh
python3 manage.py migrate
```

Запустите сервер:

```sh
python3 manage.py runserver
```

### Документация для API доступна по ссылке:
```sh
127.0.0.1:8000/swagger/
```
