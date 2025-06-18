import logging
import sys
import os
# import asyncio


from aiogram import Bot, Dispatcher
from aiogram.types import Message  # ловим все обновления этого типа
from aiogram.filters.command import Command  # обрабатываем команды /start, /help и другие


translit_table = {
    # строчные
    "а": "A",
    "б": "B",
    "в": "V",
    "г": "G",
    "д": "D",
    "е": "E",
    "ё": "E",
    "ж": "ZH",
    "з": "Z",
    "и": "I",
    "й": "I",
    "к": "K",
    "л": "L",
    "м": "M",
    "н": "N",
    "о": "O",
    "п": "P",
    "р": "R",
    "с": "S",
    "т": "T",
    "у": "U",
    "ф": "F",
    "х": "KH",
    "ц": "TS",
    "ч": "CH",
    "ш": "SH",
    "щ": "SHCH",
    "ы": "Y",
    "ъ": "IE",
    "э": "E",
    "ю": "IU",
    "я": "IA",
    " ": " ",
    # заглавные
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TS",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Ъ": "IE",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
}


# 2. Инициализация обьектов

# 7349526718 - это id нашего бота, уникальный ключ,
# по которому можно идентифицировать нашего бота
# AAGdPhPRvAZuSEt78Ru5XPnM3dnTU9P5ss0 - это ключ подключения к серверам ТГ
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(
    level=logging.INFO,
    format="[ %(levelname)s ] %(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", mode='w', encoding='utf-8'),  # файл
        logging.StreamHandler(sys.stdout),  # вывод в консоль (docker logs)
    ]
)


# Делаем транслитирацию
def transliterate(text: str) -> str:
    result = ""
    for char in text:
        result += translit_table.get(char, char.upper())
    return result


# 3. Обработка команды start
@dp.message(Command(commands=["start"]))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Привет, {user_name}!"
    logging.info(f"{user_name} {user_id} запустил бота")
    await bot.send_message(chat_id=user_id, text=text)


# 4. Обработка всех сообщений
@dp.message()
async def send_translit_fio(message: Message):
    text = message.text.strip()
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    if not text:
        await message.answer("Отправь мне ФИО на кириллице.")
        logging.info(
            f"{user_name} ({user_id}) отправил пустое сообщение или только пробелы"
        )
        return
    latin = transliterate(text)
    logging.info(f"{user_name} {user_id} отправил: {text} -> {latin}")
    await message.answer(latin)


# 5. Запуск процесса поллинга
if __name__ == "__main__":
    dp.run_polling(bot)


# async def main():
#     """
#     Запуск бота.
#     """
#     logging.info("Бот запускается")
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())
