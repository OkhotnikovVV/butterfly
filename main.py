import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from dotenv import load_dotenv

from util_butterfly import get_predict
from data import data


# Подгружаем переменные окружения
load_dotenv()

# Включаем логирование
logging.basicConfig(level=logging.INFO)


bot = Bot(token=os.environ.get("TOKEN"))

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Здравствуйте! Отправьте мне фото бабочки")


# Хэндлер, срабатывающий на входящие фотографии
@dp.message(F.photo)
async def send_to_admin(message: types.Message, bot: Bot) -> None:
    file = await bot.download(message.photo[-1])
    ans = await get_predict(file)
    await message.reply(f"{data[ans[0]][1]}")


async def main() -> None:
    """ Точка входа. """
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(dp.start_polling(bot, skip_updates=True))
    except* TypeError as te:
        for errors in te.exceptions:
            print(errors)
    except* Exception as ex:
        print(ex.exceptions)


if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print('Bot stopped')
