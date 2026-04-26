import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import shap

# DATA
def create_dataset():
    np.random.seed(42)
    data = []

    for _ in range(600):
        sleep = np.random.randint(4, 10)
        screen = np.random.randint(1, 12)
        exercise = np.random.randint(0, 10)
        social = np.random.randint(0, 10)

        score = sleep*8 - screen*3 + exercise*5 + social*4

        if score > 55:
            risk = 0
        elif score > 35:
            risk = 1
        else:
            risk = 2

        data.append([sleep, screen, exercise, social, risk])

    return pd.DataFrame(data, columns=["sleep", "screen", "exercise", "social", "risk"])

df = create_dataset()

X = df.drop("risk", axis=1)
y = df["risk"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=120, random_state=42)
model.fit(X_train, y_train)
explainer = shap.TreeExplainer(model)

# PREDICTION
def predict_risk(data):
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]

    labels = ["Low", "Moderate", "High"]
    return labels[pred]

# HEALTH SCORE
def compute_score(data):
    score = 100
    score -= max(0, 6 - data["sleep"]) * 8
    score -= data["screen"] * 3
    score -= max(0, 3 - data["exercise"]) * 10
    score -= max(0, 3 - data["social"]) * 8

    return max(0, min(100, int(score)))

# SHAP
def get_shap_values(data):
    df = pd.DataFrame([data])

    shap_values = explainer.shap_values(df)

    # HANDLE SHAP OUTPUT
    # Multiclass (list of arrays)
    if isinstance(shap_values, list):
        class_index = int(model.predict(df)[0])
        class_index = min(class_index, len(shap_values) - 1)
        values = shap_values[class_index][0]

    # Binary/Single Output Array
    else:
        values = shap_values[0]

    values = np.array(values).flatten()
    features = ["sleep", "screen", "exercise", "social"]

    values = values[:len(features)]
    if len(values) < len(features):
        values = np.pad(values, (0, len(features) - len(values)))

    # SCALE FOR UI
    scaled = np.abs(values)

    if scaled.max() > 0:
        scaled = (scaled / scaled.max()) * 4

    return {
        features[i]: int(round(scaled[i]))
        for i in range(len(features))
    }