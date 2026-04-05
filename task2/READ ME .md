# 🧠 Task 2: Deep Learning Model (Image Classification)

## 📌 Objective
Implement a deep learning model for image classification using TensorFlow and visualize the results.

---

## 📊 Dataset
- MNIST Dataset (handwritten digits 0–9)
- Loaded directly from TensorFlow

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading
- Loaded MNIST dataset using TensorFlow
- Dataset contains 60,000 training and 10,000 testing images

### 2️⃣ Data Preprocessing
- Normalized pixel values (0–255 → 0–1)
- Reshaped images to (28 × 28 × 1) for CNN

### 3️⃣ Model Architecture
- Convolutional Neural Network (CNN)
  - Conv2D (32 filters)
  - MaxPooling
  - Conv2D (64 filters)
  - MaxPooling
  - Flatten
  - Dense (128 neurons)
  - Output layer (10 classes)

### 4️⃣ Model Training
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy
- Epochs: 5

### 5️⃣ Model Evaluation
- Evaluated on test dataset
- Achieved high accuracy (~98%)

---

## 📈 Visualizations

### 🔹 Accuracy Graph
- Shows training vs validation accuracy across epochs

### 🔹 Loss Graph
- Shows training vs validation loss decreasing

### 🔹 Prediction Outputs
- Displays predicted vs actual digits

---

## 📦 Output Files

All outputs are stored in the `outputs/` folder:

- `accuracy.png` → Accuracy graph  
- `loss.png` → Loss graph  
- `prediction_0.png` to `prediction_4.png` → Sample predictions  
- `cnn_model.h5` → Trained deep learning model  

---

## 🛠️ Technologies Used

- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  

---

## 🚀 How to Run the Project

```bash
pip install tensorflow matplotlib numpy
python cnn_model.py
