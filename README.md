# api_final
Учебный проект по созданию API с помощью Django REST framework.
Имитирует работу блога с возможностью создавать посты, объединять посты в
группы, комментировать и подписываться на других авторов.
API позволяет производить CRUD операции над вышеупомянутыми объектами.
В качестве стандарта передачи данных используется json.

Основной задачей при создании проекта было добавление необходимых моделей,
создание адресов и представлений для обработки запросов в соответсвии с
документацией (см. http://127.0.0.1:8000/redoc/ после запуска сервера).

## Как запустить проект
Клонировать репозиторий:

`git@github.com:Resistor-git/api_final_yatube.git`

Перейти в репозиторий в командной строке:

`cd api_final_yatube`

Создать и активировать виртуальное окружение:

Linux `python3 -m venv venv`

Windows `py -m venv venv`

Установить зависимости из requirements.txt:

Linux

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Windows
```
py -m pip install --upgrade pip
pip install -r requirements.txt
```

В папке с файлом manage.py выполнить миграции и запустить проект:
Lunix
```
python3 manage.py migrate
python3 manage.py runserver
```
Windows
```
py manage.py migrate
py manage.py runserver
```
## Примеры основных запросов
### Получение списка постов:
GET `/api/v1/posts/`
Опциональные параметры пагинации:
* limit - количество публикаций на страницу
* offset - номер страницы после которой начинать выдачу
Пример удачного ответа без пагинации (статус 200):
```
[
    {
        "id": 1,
        "pub_date": "2023-04-23T16:55:10.711684Z",
        "text": "firstpost",
        "author": "first",
        "group": null,
        "image": null
    }
]
```
Пример удачного ответа с пагинацией (статус 200):
```
{
    "count": 4,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 3,
            "pub_date": "2023-04-24T15:11:55.029638Z",
            "text": "secondpost",
            "author": "first",
            "group": null,
            "image": null
        },
        {
            "id": 4,
            "pub_date": "2023-04-24T15:12:05.693600Z",
            "text": "3rdpost",
            "author": "first",
            "group": null,
            "image": null
        }
    ]
}
```
### Получение отдельного поста:
GET `/api/v1/posts/1/`
### Публикация нового поста (требуется аутентификация через JWT токен):
PUT `/api/v1/posts/`
Тело запроса должно содержать поля:
* text - string (обязательно)
* image - byte string (опционально)
* group - integer (опционально)

Пример тела запроса для создания поста:
```
    "text": "some text",
    "image": "some bytestring",
    "group": 0
```
### Получение JWT токена:
POST `/api/v1/jwt/create/`
Тело запроса должно содержать поля:
* username - string
* password - string

Ответ на успешный запрос содержит два поля:
* refresh - string 
* access - string

"access" - сам токен, "refesh" используется для обновления токена.
Тип токена: Bearer.

## Стек
Бэкенд:

[Django==3.2.16](https://docs.djangoproject.com/en/3.2/)

[djangorestframework==3.12.4](https://www.django-rest-framework.org/)

Авторизация:

[djangorestframework-simplejwt==4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)

[PyJWT==2.1.0](https://pyjwt.readthedocs.io/en/stable/)

Тестирование:

[pytest==6.2.4](https://docs.pytest.org/en/6.2.x/)

[pytest-pythonpath==0.7.3](https://pypi.org/project/pytest-pythonpath/)

[pytest-django==4.4.0](https://pytest-django.readthedocs.io/en/latest/)

Работа с изображениями:

[Pillow==9.3.0](https://pillow.readthedocs.io/en/stable/)

Прочее:

[requests==2.26.0](https://pypi.org/project/requests/2.26.0/)

## Автор
Resistor ([GitHub](https://github.com/Resistor-git/))