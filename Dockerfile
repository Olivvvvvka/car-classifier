# Используем минимальный образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только нужные файлы
COPY app.py requirements.txt ./

# Устанавливаем зависимости ОДНИМ вызовом
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 5000

# Запуск
CMD ["python", "app.py"]
