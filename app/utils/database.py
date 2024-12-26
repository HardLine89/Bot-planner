from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.config import DATABASE_URL
from app.models.models import Base, User, Task

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Настраиваем сессию
async_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Функция для получения сессии
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


# Функция для получения или создания пользователя
async def get_or_create_user(
    session: AsyncSession, telegram_id: str, username: str = None
):
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalars().first()

    if not user:
        user = User(telegram_id=telegram_id, username=username)
        session.add(user)
        await session.commit()

    return user


# Функция для создания новой задачи
async def create_task(
    session: AsyncSession, user_id: int, description: str, due_date=None
):
    task = Task(user_id=user_id, description=description, due_date=due_date)
    session.add(task)
    await session.commit()
    return task


# Функция для получения задач пользователя
async def get_tasks(session: AsyncSession, user_id: int):
    result = await session.execute(select(Task).where(Task.user_id == user_id))
    return result.scalars().all()
