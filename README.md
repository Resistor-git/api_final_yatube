# api_final
Учебный проект по созданию API.
Имитирует работу блога с возможностью создавать посты, объединять посты в
группы, комментировать и подписываться на других авторов.
API позволяет производить CRUD операции над вышеупомянутыми объектами.
В качестве стандарта передачи данных используется json.
## Как запустить проект.
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
## Примеры основных запросов.
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