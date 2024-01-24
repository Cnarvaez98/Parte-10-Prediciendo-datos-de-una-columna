import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Supongamos que tienes un DataFrame llamado df con tus datos
# Elimina las columnas DEATH_EVENT, age y categoria_edad
X = df.drop(['DEATH_EVENT', 'age', 'categoria_edad'], axis=1)

# Utiliza la columna age como el vector y
y = df['age']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializa el modelo de regresión lineal
modelo_regresion = LinearRegression()

# Ajusta el modelo a los datos de entrenamiento
modelo_regresion.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = modelo_regresion.predict(X_test)

# Calcula el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)

print(f"Error cuadrático medio: {mse}")
