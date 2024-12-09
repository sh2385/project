import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

# Загрузка данных
df = pd.read_csv('crime.csv')

# Создание целевой переменной 'highCrime'
df['highCrime'] = np.where(df['ViolentCrimesPerPop'] > 0.1, 1, 0)

# Удаление лишних столбцов
initial = df.drop(['communityname', 'ViolentCrimesPerPop', 'fold', 'state'], axis=1)

# Целевая переменная
Y = df['highCrime']

# Обучение модели
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(initial, Y)

# Сохранение модели в файл
joblib.dump(clf, 'crime_predictor.pkl')

print("Модель сохранена в crime_predictor.pkl")
