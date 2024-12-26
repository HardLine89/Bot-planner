import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from app.config import BOT_TOKEN
from app.handlers import planner
from app.utils.commands import set_commands
from app.utils.database import init_db

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


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
    dp.message.register(planner.add_task, Command(commands=["add_task"]))
    dp.message.register(planner.list_tasks, Command(commands=["tasks"]))
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
