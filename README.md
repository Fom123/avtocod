<p align="center">
    <a href="https://github.com/Fom123/avtocod">
        <img src="https://profi.avtocod.ru/img/icons/apple-touch-icon-152x152.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Avtocod - неофициальная Python библиотека</b>
    <br>
    
[![PyPI version](https://img.shields.io/pypi/v/avtocod.svg)](https://pypi.org/project/avtocod/)
[![Code Quality Score](https://api.codiga.io/project/30917/score/svg)](https://frontend.code-inspector.com/public/project/30917/avtocod/dashboard) 
![Downloads](https://img.shields.io/pypi/dm/avtocod)
![codecov](https://codecov.io/gh/Fom123/avtocod/branch/develop/graph/badge.svg)
![mypy](https://img.shields.io/badge/type_checker-mypy-style=flat)
</p>

**Avtocod** - неофициальный, элегантный, асинхронный враппер [автокода](https://profi.avtocod.ru/).
Позволяет взаимодействовать с апи автокода используя лишь данные от учетной записи.

### Ключевые особенности
- **Быстрый**
- **Поддержка тайпхинтов**
- **Асинхронный код**


### Требования

- Python 3.8 или выше.
- [Аккаунт Автокода](https://profi.avtocod.ru/auth).


### Установка

``` bash
pip3 install -U avtocod
```


### Документация

Временно, вместо документации, вы можете использовать [примеры](examples)

### Предупреждение
Очень рекомендуется сменить ```User-Agent``` при работе с библиотекой.
Это можно сделать так:
``` python 
from avtocod import AvtoCod
from avtocod.session.aiohttp import AiohttpSession

async def main():
    avtocod = AvtoCod(
        session=AiohttpSession(
            headers={"User-Agent": "your-user-agent-here"}
        )
    )
```
Или если вы используете конструктор:
``` python
from avtocod import AvtoCod
from avtocod.session.aiohttp import AiohttpSession

async def main():
    avtocod = AvtoCod.from_credentials(
        email="myuser@example.com",
        password="mypassword",
        session=AiohttpSession(
            headers={"User-Agent": "your-user-agent-here"}
        )
    )
```


### Внесение своего вклада в проект

Любой вклад в проект приветствуется.
### Благодарности

- [@JrooTJunior](https://github.com/JrooTJunior) за [Aiogram](https://github.com/aiogram/aiogram). Выбрал вас в качестве примера
