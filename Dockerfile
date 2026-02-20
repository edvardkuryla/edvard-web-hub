# Используем легкий образ Python
FROM python:3.11-slim

# Запрещаем Python писать файлы .pyc и включаем буферизацию логов
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости (нужны для сборки некоторых библиотек, например, psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Команда для запуска (через uvicorn)
# Указываем путь к main:app внутри папки src
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]