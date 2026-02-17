import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
from config.database.database import Base
import src.models.models

target_metadata = Base.metadata

# 1. Загружаем переменные из .env
load_dotenv()

# Объект конфигурации Alembic
config = context.config

# 2. Подставляем URL из .env в конфигурацию Alembic программно
# Это заменяет необходимость писать URL в alembic.ini
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 3. Импортируем твои модели и Base
# Без этого autogenerate не увидит твои таблицы!
from config.database.database import Base
import src.models.models  # Импорт важен, чтобы Base "узнал" о существовании таблиц
target_metadata = Base.metadata

# Оставляем функции миграций как есть, они теперь будут использовать
# обновленный url из config.set_main_option

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    # Здесь Alembic создаст движок, используя URL, который мы подставили выше
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()