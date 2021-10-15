# Сайт риэлторского агентства

Сайт находится в разработке, поэтому доступна только страница со списком квартир и админка для наполнения БД.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — смотри [документацию Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).
- 'STATIC_URL' — [смотри документацию Django, по умолчанию /static/](https://docs.djangoproject.com/en/3.2/ref/settings/#static-url)
- 'STATIC_ROOT' — [смотри документацию Django, по умолчанию None](https://docs.djangoproject.com/en/3.2/ref/settings/#static-root)
- 'MEDIA_URL' — [смотри документацию Django, по умолчанию /media/'](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-MEDIA_URL)
- 'MEDIA_ROOT' — [смотри документацию Django, по умолчанию 'media'](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-MEDIA_ROOT)


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).