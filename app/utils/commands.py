from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        # BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="add_task", description="Добавить задачу"),
        BotCommand(command="tasks", description="Список задач"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
