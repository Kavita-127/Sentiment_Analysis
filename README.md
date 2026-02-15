# 🍽 Restaurant Review Sentiment Analysis

## 📌 Project Overview

This project is a Natural Language Processing (NLP) based Machine Learning application that classifies restaurant reviews as **Positive** or **Negative**.

The model is trained using TF-IDF vectorization and a Linear Support Vector Machine (SVM) classifier, and deployed as an interactive web application using Streamlit.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- LinearSVC (SVM)
- Streamlit (for deployment)

---

##  NLP Techniques Used

- Text preprocessing (lowercasing, punctuation removal, stopword removal)
- Bag of Words representation
- TF-IDF (Term Frequency – Inverse Document Frequency)
- Supervised Text Classification using Support Vector Machine

---

##  Dataset

- **Restaurant_Reviews.tsv**
- 1000 labeled restaurant reviews
- Target:
  - 1 → Positive Review
  - 0 → Negative Review

---

## ⚙️ Model Workflow

1. Load dataset
2. Text preprocessing
3. Train-test split (80-20)
4. TF-IDF vectorization
5. Model training using LinearSVC
6. Model evaluation
7. Save trained model (`.pkl`)
8. Deploy using Streamlit

---

##  Model Accuracy

Accuracy: **81%**

---

## 🌐 Live Demo

🔗 **Live App:**  
[http://localhost:8503/](http://localhost:8503/)

---

##  Application Preview

### ✅ Positive Review Prediction

![Positive Prediction](Positive_Review.png)

---

### ❌ Negative Review Prediction

![Negative Prediction](Negative_Review.png)

---

### Deployment Process:

1. Uploaded project to GitHub
2. Connected GitHub repository to Streamlit Cloud
3. Selected `app.py` as entry point
4. Deployed publicly

---

## 💻 Running the Application Locally

1. Clone the repository:
   git clone https://github.com/your-username/restaurant-sentiment-analysis.git

2. Navigate to the project folder:
   cd restaurant-sentiment-analysis

3. Install required packages:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run app.py
