from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
import asyncio

from app.config import BOT_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Простой хэндлер для команды /start
@dp.message()
async def start(message: Message):
    await message.answer("👋 Привет! Я бот-планировщик задач.")


# Основная функция для запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
