# Cyrillic_to_Latin_Bot

Телеграм-бот, преобразующий ФИО с кириллицы в латиницу.


КАК СОБРАТЬ И ЗАПУСТИТЬ В Docker

1. Убедитесь, что установлен Docker и он запущен https://docs.docker.com/get-started/get-docker/

2. В корне проекта (там же, где dockerfile) соберите образ:
    
    docker build -t my-telegram-bot .

3. Запустите контейнер, изменив расширение .env.example на .env(добавьте в этот файл ваш ТОКЕН):
    
    docker run --env-file .env my-telegram-bot

4. Проверьте, что бот запустился, просмотрев логи:
    docker logs <НАЗВАНИЕ_КОНТЕЙНЕРА>



КАК ЗАПУСТИТЬ БОТА только через код!

1. Склонируйте репозиторий и перейдите в папку проекта:

    git clone https://github.com/fuckuritic/Cyrillic_to_Latin_Bot.git
    cd Cyrillic_to_Latin_Bot


2. Создайте и активируйте виртуальное окружение:

    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux

3. Установите зависимости(необходимые библиотеки):

    pip install -r requirements.txt

4. Запустите бота, изменив расширение .env.example на .env(добавьте в этот файл ваш ТОКЕН):

    python bot.py




