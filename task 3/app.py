# ==========================================
# FLASK WEB APP
# ==========================================

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form

    features = [
        float(data['Pclass']),
        float(data['Sex']),
        float(data['Age']),
        float(data['SibSp']),
        float(data['Parch']),
        float(data['Fare']),
        float(data['Embarked'])
    ]

    prediction = model.predict([features])[0]

    result = "Survived ✅" if prediction == 1 else "Not Survived ❌"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
