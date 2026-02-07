# Используем slim Python 3.11
FROM python:3.11-slim

# Устанавливаем рабочую директорию — корень проекта
WORKDIR /edvardkuryla

# Копируем только зависимости сначала, чтобы кэшировать pip
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Запуск FastAPI через uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

