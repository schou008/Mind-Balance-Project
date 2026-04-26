import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# SYNTHETIC DATA GENERATION
data = pd.DataFrame({
    "sleep": np.random.randint(2, 10, 600),
    "screen": np.random.randint(0, 12, 600),
    "exercise": np.random.randint(0, 8, 600),
    "social": np.random.randint(0, 8, 600),
})

# LABEL FUNCTION
def label(row):
    score = 0

    if row["sleep"] <= 4:
        score += 4
    elif row["sleep"] <= 6:
        score += 2

    if row["screen"] >= 8:
        score += 3
    elif row["screen"] >= 5:
        score += 2

    if row["exercise"] <= 2:
        score += 3
    elif row["exercise"] <= 4:
        score += 1

    if row["social"] <= 2:
        score += 3
    elif row["social"] <= 4:
        score += 1

    if score <= 4:
        return "Low"
    elif score <= 8:
        return "Moderate"
    else:
        return "High"

# Apply the labelling function to generate target variable
data["risk"] = data.apply(label, axis=1)

# FEATURE / TARGET SPLIT
# Separate input features (X) and target labels (y)
X = data.drop("risk", axis=1)
y = data["risk"]

# MODEL TRAINING
model = RandomForestClassifier(n_estimators=120, random_state=42)
model.fit(X, y)

# MODEL EXPORT
joblib.dump(model, "model.pkl")

print("Model trained")