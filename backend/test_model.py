import joblib
import os
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.dummy import DummyClassifier

# Carregar dados
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'
df = pd.read_csv(url)
df = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'species']].dropna()

X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']]
y = df['species']

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modelo_pinguins.joblib')
model = joblib.load(MODEL_PATH)

LE_PATH = os.path.join(os.path.dirname(__file__), 'label_encoder.joblib')
le = joblib.load(LE_PATH)

ACCEPTABLE_ACCURACY = 0.8

def test_model_accuracy_aceitavel():
    y_test_decoded = le.inverse_transform(y_test)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test_decoded, y_pred)
    print(f"A acurácia do modelo é: {acc:.2f}")
    assert acc >= ACCEPTABLE_ACCURACY, f"A acurácia está abaixo do aceitável: {acc:.2f}"

def test_model_accuracy_inaceitavel_simulada():
    dummy_model = DummyClassifier(strategy='most_frequent')
    dummy_model.fit(X_train, y_train)

    y_pred = dummy_model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    assert acc < ACCEPTABLE_ACCURACY, f"A acurácia está acima do limiar definido: {acc:.2f}"
