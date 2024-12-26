import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from app.config import BOT_TOKEN
from app.utils.database import init_db

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Простой хэндлер для команды /start
@dp.message()
async def start(message: Message):
    await message.answer("👋 Привет! Я бот-планировщик задач.")


# Основная функция для запуска бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    print("Инициализация базы данных...")
    await init_db()
    print("База данных готова!")
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
