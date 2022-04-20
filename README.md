# kvartirka_test_task
REST API для системы комментариев блога.
Позволяет создавать статьи и древовидные комментарии. 
Стек: Python 3.10, Django 4.0, DRF, django-mptt, PostgreSQL, pipenv
## Начало работы

Установите pipenv, если не сделали этого раньше

```sh
pip install --user pipenv
```

Скопируйте репозиторий

```sh
git clone https://github.com/menyanet73/kvartirka_test_task.git
```

Перейдите в репозиторий

```sh
cd kvartirka_test_task
```

Установите зависимости

```sh
pipenv sync --dev
```

Примените миграции:

```sh
cd kvartirka_test_task
```

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
