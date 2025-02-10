# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY . /app/

# Открываем порт
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
