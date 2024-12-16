import asyncio
import logging
import sys
import openpyxl
import http.client
import exel_def as ex

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

from cfg import TOKEN

#global Admins, Name_ADM, Ktoto, Name_K, Number, Kogda, Number_text, IP, Name, CHEY_IP, Name_Chey, Gotov

file_path = 'data.xlsx'
P = True
My_ID = 1711818456


(P and print("Start"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")
@dp.message(Command("help"))
async def handle_start(message: types.Message):
    await message.answer(text=f"I am a simple bot.\nSend me any message")
@dp.message(Command("reboot"))
async def handle_start(message: types.Message):
    await message.answer(text=f"-_-")
    exit()
    

@dp.message()
async def echo_message(message: types.Message):
    if message.chat.id not in Admins and message.chat.id not in Ktoto:
        await message.send_copy(chat_id=message.chat.id)
    else:
        await message.reply(text="Sorry you are ADM")
    # await bot.send_message(chat_id=message.chat.id, text="send_message with no id")
    # await bot.send_message(chat_id=message.chat.id, text="Reply_with_id", reply_to_message_id=message.message_id)
    # await message.reply(text="reply_without_id(last)")
    # if message.text:
    #     await message.answer(text=message.text)
    # elif message.sticker:
    #     await message.reply_sticker(sticker=message.sticker.file_id)
    # else:
    #     await message.reply(text="Its not a text")


async def main():

    await bot.send_message(chat_id=My_ID, text="Bot start")
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    Admins = ex.read_column_to_list(file_path, 1)
    Name_ADM = ex.read_column_to_list(file_path, 2)
    Ktoto = ex.read_column_to_list(file_path, 3)
    Name_K = ex.read_column_to_list(file_path, 4)
    Number = ex.read_column_to_list(file_path, 5)
    Kogda = ex.read_column_to_list(file_path, 6)
    Number_text = ex.read_column_to_list(file_path, 7)
    IP = ex.read_column_to_list(file_path, 8)
    Name = ex.read_column_to_list(file_path, 9)
    CHEY_IP = ex.read_column_to_list(file_path, 10)
    Name_Chey = ex.read_column_to_list(file_path, 11)
    Gotov = ex.read_column_to_list(file_path, 12)

    asyncio.run(main())


(P and print("End"))