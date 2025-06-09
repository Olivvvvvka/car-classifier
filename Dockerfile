# Используем минимальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения (кроме модели!)
COPY app.py requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 5000

# Запускаем Flask
CMD ["python", "app.py"]
RUN pip install --no-cache-dir \
    flask \
    tensorflow \
    numpy \
    pandas \
    joblib \
    scikit-learn
