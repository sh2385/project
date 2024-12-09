from flask import Flask, request, jsonify
import pandas as pd
import joblib
import numpy as np

# Инициализация Flask приложения
app = Flask(__name__)

# Загрузка обученной модели
clf = joblib.load('crime_predictor.pkl')

# Загрузка исходных данных для подготовки признаков
df = pd.read_csv('crime.csv')

# Удаляем лишние колонки для обучения
initial = df.drop(['communityname', 'ViolentCrimesPerPop', 'fold', 'state'], axis=1)

# Главная страница
@app.route('/')
def home():
    return "Crime Prediction API"

# API для предсказания
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получение данных из запроса (JSON)
        data = request.get_json()

        # Преобразование данных в DataFrame
        new_data = pd.DataFrame(data)

        # Удаляем лишние столбцы
        new_data = new_data.drop(['communityname', 'ViolentCrimesPerPop', 'fold', 'state'], axis=1, errors='ignore')

        # Проверка на совпадение с обучающими признаками
        missing_cols = list(set(initial.columns) - set(new_data.columns))
        if missing_cols:
            return jsonify({"error": f"Missing columns: {', '.join(missing_cols)}"}), 400

        # Предсказание
        predictions = clf.predict(new_data)

        # Возвращаем результат предсказания
        return jsonify({"predictions": predictions.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
