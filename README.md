# DjangoAPI

## Prerequisites

- python 3.6+
- SQliteStudio (for managing the database)

## install requirements

First install all requirements including Django, Django Rest Framework and Django CORS Headers

```python
pip install -r requirements.txt
```

## start DjangoAPI server

```python
python manage.py runserver
```

## Updating Database

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

## Testing API calls

I did not get around to writing tests within the Django framework so all API tests were made using [Postman](https://www.postman.com/downloads/).
