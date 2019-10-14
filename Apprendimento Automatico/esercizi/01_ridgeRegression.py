import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

dataset = load_boston()
houses = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
display(houses.head())


houses['PRICE'] = dataset.target
X_rooms = houses['RM']
y_price = houses['PRICE']

X_rooms = np.array(X_rooms).reshape(-1,1)
y_price = np.array(y_price).reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(X_rooms, y_price, test_size = 0.2, random_state=5)


alphas= [0.0, 0.01, 0.1, 1.0, 100.0]

plt.figure(figsize=(16,8))
plt.title("Distribuzione dei valori")
plt.ylabel("Prezzo (1000$)")
plt.xlabel("Numero stanze")
plt.scatter(X_test, Y_test,  color='black', linewidth=0.5)


for val in alphas:
    ridgeRegression = Ridge(alpha=val)
    ridgeRegression.fit(X_train, Y_train) #"Istruisco l'algoritmo"
    prediction = ridgeRegression.predict(X_test)  # predico i nuovi valori di Y a partire da X di test dopo aver istruito l'algoritmo
    plt.figure(figsize=(16,8))
    plt.title("Ridge Regression con alpha = " + str(val))
    plt.ylabel("Prezzo (1000$)")
    plt.xlabel("Numero stanze")
    plt.scatter(X_test, Y_test,  color='black', linewidth=0.5) #Stampo i valori reali
    plt.plot(X_test, prediction, color='red', linewidth=1) # Stampo la funzione calcolata con X di test e le Y predette
    plt.show()
