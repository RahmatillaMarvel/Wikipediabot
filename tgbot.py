
import logging
import wikipedia
 
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum. Bizning wikipedia botimizga xush kelibsiz!")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        wikipedia.set_lang("uz")
        await message.answer(wikipedia.summary(message.text))
    except:
        await message.reply("Bunday maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
