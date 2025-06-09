from flask import Flask, request, render_template_string
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
import os

app = Flask(__name__)

# Глобальные переменные
model = None
scaler = None
class_encoder = None
feature_columns = None

# HTML-шаблоны
form_html = '''
<!DOCTYPE html>
<html>
<head><title>Оценка автомобиля</title></head>
<body>
  <h2>Введите параметры автомобиля</h2>
  <form action="/predict" method="post">
    Buying: <input type="number" name="buying"><br>
    Maint: <input type="number" name="maint"><br>
    Doors: <input type="number" name="doors"><br>
    Persons: <input type="number" name="persons"><br>
    Lug_boot: <input type="number" name="lug_boot"><br>
    Safety: <input type="number" name="safety"><br><br>
    <input type="submit" value="Предсказать">
  </form>
</body>
</html>
'''

result_html = '''
<!DOCTYPE html>
<html>
<head><title>Результат</title></head>
<body>
  <h2>Класс автомобиля: {{ prediction }}</h2>
  <a href="/">Назад</a>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(form_html)

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        int(request.form['buying']),
        int(request.form['maint']),
        int(request.form['doors']),
        int(request.form['persons']),
        int(request.form['lug_boot']),
        int(request.form['safety'])
    ]
    features_scaled = scaler.transform(np.array(features).reshape(1, -1))
    prediction = model.predict(features_scaled)
    predicted_class = np.argmax(prediction)
    class_name = class_encoder.inverse_transform([predicted_class])[0]
    return render_template_string(result_html, prediction=class_name)

if __name__ == '__main__':
    # Загружаем модель и утилиты ТОЛЬКО при запуске
    model = tf.keras.models.load_model("models/car_classification_model.h5")
    scaler = joblib.load("models/scaler.pkl")
    class_encoder = joblib.load("models/class_encoder.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    app.run(host='0.0.0.0', port=5000)
