FROM python:3.11-slim

WORKDIR /
#app

# Установка системных зависимостей
#RUN apt-get update && apt-get install -y \
#    gcc \
#    postgresql-client \
#    netcat-openbsd \
#    && rm -rf /var/lib/apt/lists/*

# Копирование requirements и установка Python пакетов
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование приложения и скриптов
COPY app/ /app/
# Создаем директории для логов и сессий
RUN mkdir -p /app/logs /app/sessions

# Переменные окружения для Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Добавляем /app в PYTHONPATH
ENV PYTHONPATH=/app

# Команда для запуска приложения
CMD ["python", "-m", "app.main"]