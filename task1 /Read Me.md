# Task 1: Data Pipeline Development

## 📌 Objective
Build an ETL pipeline using Pandas and Scikit-learn and train a machine learning model.

---

## ⚙️ Steps Performed

### 1. Data Extraction
- Loaded Titanic dataset from GitHub

### 2. Data Transformation
- Removed unnecessary columns (Name, Ticket, Cabin)
- Handled missing values
- Encoded categorical variables

### 3. Data Processing
- Feature scaling using StandardScaler

### 4. Model Building
- Logistic Regression model
- Used Pipeline for automation

### 5. Evaluation
- Accuracy Score
- Classification Report

### 6. Output
- Processed dataset (`processed_data.csv`)
- Trained model (`model.pkl`)
- Visualization (`data_distribution.png`)

---

## 🛠️ Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 📊 Result
The model successfully predicts survival with good accuracy.

---

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib scikit-learn joblib
python data_pipeline.py
