# 🍽 Restaurant Review Sentiment Analysis

## 📌 Project Overview

This project is a **Natural Language Processing (NLP)** based Machine Learning application that classifies restaurant reviews as **Positive** or **Negative**.

The model is trained using **TF-IDF vectorization** and a **Linear Support Vector Machine (SVM)** classifier, and presented as an interactive web application using Streamlit.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- TF-IDF Vectorizer  
- LinearSVC (SVM)  
- Streamlit (for interactive interface)

---

## NLP Techniques Used

- Text preprocessing (lowercasing, punctuation removal, stopword removal)  
- Stopword removal  
- Bag of Words representation  
- TF-IDF (Term Frequency – Inverse Document Frequency)  
- Supervised Text Classification using Support Vector Machine  

---

## Dataset

- **Restaurant_Reviews.tsv**  
- 1000 labeled restaurant reviews  

Target labels:
- `1` → Positive Review  
- `0` → Negative Review  

---

## Model Workflow

1. Load dataset  
2. Perform text preprocessing  
3. Split data into training and testing sets (80-20)  
4. Apply TF-IDF vectorization  
5. Train model using LinearSVC  
6. Evaluate model performance  
7. Save trained model (`.pkl` file)  
8. Build interactive UI using Streamlit  

---

## Model Performance

Accuracy: **81%**

---

## Application Preview

### ✅ Positive Review Prediction
![Positive Prediction](Positive_Review.png)

---

### ❌ Negative Review Prediction
![Negative Prediction](Negative_Review.png)

---

## Running the Application Locally

Follow these steps to run the project :

### 1️. Clone the repository

```bash
git clone https://github.com/Kavita-127/Sentiment_Analysis.git
cd Sentiment_Analysis
```

### 2️. Install required dependencies

```bash
pip install -r requirements.txt
```

### 3️. Run the Streamlit application

```bash
streamlit run app.py
```
