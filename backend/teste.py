import joblib
import numpy as np

model = joblib.load('modelo_pinguins.joblib')
# Tente prever um exemplo arbitrário
exemplo = np.array([[50, 15, 200], [39.1, 18.7, 181]])  # valores arbitrários
print(model.predict(exemplo))