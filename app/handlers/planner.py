from aiogram.types import Message
from app.utils.database import get_session, get_or_create_user, create_task, get_tasks


async def add_task(message: Message):
    async with get_session() as session:

        user = await get_or_create_user(
            session,
            telegram_id=str(message.from_user.id),
            username=message.from_user.username,
        )

        # Получаем описание задачи от пользователя
        command_args = message.text.split(maxsplit=1)  # Разделяем текст команды
        if len(command_args) > 1:
            task_description = command_args[1]
        else:
            task_description = None
        if not task_description:
            await message.answer(
                "❗️ Пожалуйста, укажите описание задачи после команды /add_task."
            )
            return

        await create_task(session, user_id=user.id, description=task_description)
        await message.answer("✅ Задача добавлена!")


async def list_tasks(message: Message):
    async with get_session() as session:
        user = await get_or_create_user(
            session,
            telegram_id=str(message.from_user.id),
            username=message.from_user.username,
        )

        tasks = await get_tasks(session, user_id=user.id)
        if not tasks:
            await message.answer("ℹ️ У вас пока нет задач.")
            return

        tasks_list = "\n".join(
            [f"{i + 1}. {task.description}" for i, task in enumerate(tasks)]
        )
        await message.answer(f"📋 Ваши задачи:\n{tasks_list}")
