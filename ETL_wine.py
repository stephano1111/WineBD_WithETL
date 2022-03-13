import numpy as np
import pandas as pd
import csv

wine = pd.read_csv('BaseD/wine.csv')

#-------------------------------------ETL----------------------------------------

#-------Extract:-------
x_bad = np.array(wine[wine.quality == 'bad'].drop(columns='quality'))
x_good = np.array(wine[wine.quality == 'good'].drop(columns='quality'))

#------Transform:------
x_bad_Transformado = x_bad - 0.5
x_good_Transformado = x_good + 1

#--------Load:---------
labels = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol', 'quality']

doct_arr = []

for i in range(744):
    doct_arr.insert(i, 
        {'fixed acidity': x_bad_Transformado[i][0], 'volatile acidity': x_bad_Transformado[i][1], 'citric acid': x_bad_Transformado[i][2], 
        'residual sugar': x_bad_Transformado[i][3], 'chlorides': x_bad_Transformado[i][4], 'free sulfur dioxide': x_bad_Transformado[i][5],
        'total sulfur dioxide': x_bad_Transformado[i][6], 'density': x_bad_Transformado[i][7], 'pH': x_bad_Transformado[i][8],
        'sulphates': x_bad_Transformado[i][9], 'alcohol': x_bad_Transformado[i][10], 'quality': 'bad'}
    )

for i in range(855):
    doct_arr.insert(i+744, 
        {'fixed acidity': x_good_Transformado[i][0], 'volatile acidity': x_good_Transformado[i][1], 'citric acid': x_good_Transformado[i][2], 
        'residual sugar': x_good_Transformado[i][3], 'chlorides': x_good_Transformado[i][4], 'free sulfur dioxide': x_good_Transformado[i][5],
        'total sulfur dioxide': x_good_Transformado[i][6], 'density': x_good_Transformado[i][7], 'pH': x_good_Transformado[i][8],
        'sulphates': x_good_Transformado[i][9], 'alcohol': x_good_Transformado[i][10], 'quality': 'good'}
    ) 

try:
    with open('BaseD/ETL_wine.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in doct_arr:
            writer.writerow(elem)
except IOError:
    print("I/O error")

#------------------------------------Fin:ETL--------------------------------------