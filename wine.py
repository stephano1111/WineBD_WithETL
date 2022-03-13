from re import X
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

wine = pd.read_csv('BaseD/wine.csv')
ETLwine = pd.read_csv('BaseD/ETL_wine.csv')
#print(wine.head())

#-------------------------------------Datos Normales----------------------------------

fig = wine[wine.quality == 'bad'].plot(kind='scatter', x='fixed acidity', y='volatile acidity', color='red', label='Bad wine')
wine[wine.quality == 'good'].plot(kind='scatter', x='fixed acidity', y='volatile acidity', color='green', label='Good wine', ax=fig)

fig = wine[wine.quality == 'bad'].plot(kind='scatter', x='fixed acidity', y='citric acid', color='red', label='Bad wine')
wine[wine.quality == 'good'].plot(kind='scatter', x='fixed acidity', y='citric acid', color='green', label='Good wine', ax=fig)

#-------------------------------------Datos Con ETL-----------------------------------
fig = ETLwine[ETLwine.quality == 'bad'].plot(kind='scatter', x='fixed acidity', y='volatile acidity', color='red', label='Bad wine')
ETLwine[ETLwine.quality == 'good'].plot(kind='scatter', x='fixed acidity', y='volatile acidity', color='green', label='Good wine', ax=fig)

fig = ETLwine[ETLwine.quality == 'bad'].plot(kind='scatter', x='fixed acidity', y='citric acid', color='red', label='Bad wine')
ETLwine[ETLwine.quality == 'good'].plot(kind='scatter', x='fixed acidity', y='citric acid', color='green', label='Good wine', ax=fig)

#-------Modelo: Bad-Wine/Good-Wine------
x = np.array(ETLwine.drop(columns='quality'))
y = np.array(ETLwine['quality'])

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
print(f'{x_train.shape[0]}: datos para el entrenamiento y {x_test.shape[0]} datos para la prueba')

#Regresión logística
log_model = LogisticRegression()
log_model.fit(x_train,y_train)
prediction = log_model.predict(x_test)
print(f'Precisión del modelo Regresión logística es {log_model.score(x_train, y_train)*100}')

#SVC
svc_model = SVC()
svc_model.fit(x_train, y_train)
prediction = svc_model.predict(x_test)
print(f'Precisión de SVC es: {svc_model.score(x_train, y_train)*100}')

#KNN
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(x_train, y_train)
prediction = knn_model.predict(x_test)
print(f'Precisión de KNN es: {knn_model.score(x_train, y_train)*100}')

#DecisionTreeClassifier
dtc_model = DecisionTreeClassifier()
dtc_model.fit(x_train, y_train)
prediction = dtc_model.predict(x_test)
print(f'Precisión de DTC es: {dtc_model.score(x_train, y_train)*100}')

#plt.show()