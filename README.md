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

## 🧠 NLP Techniques Used

- Text preprocessing (lowercasing, punctuation removal, stopword removal)
- Bag of Words representation
- TF-IDF (Term Frequency – Inverse Document Frequency)
- Supervised Text Classification using Support Vector Machine

---

## 📊 Dataset

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

## 🎯 Model Accuracy

Accuracy: **YOUR_ACCURACY%**

---

## 🌐 Live Demo

🔗 **Live App:**  
https://YOUR_APP_LINK.streamlit.app

---

## 📸 Application Preview

### ✅ Positive Review Prediction

(Add your positive screenshot file name below)

![Positive Prediction](positive_review.png)

---

### ❌ Negative Review Prediction

(Add your negative screenshot file name below)

![Negative Prediction](negative_review.png)

---

## 🚀 Deployment

This application is deployed using Streamlit Community Cloud.

### Deployment Process:

1. Uploaded project to GitHub
2. Connected GitHub repository to Streamlit Cloud
3. Selected `app.py` as entry point
4. Deployed publicly

The app automatically redeploys when changes are pushed to GitHub.

---

## 💻 How to Run Locally

```bash
# Clone repository
git clone https://github.com/YOUR_GITHUB_USERNAME/restaurant-sentiment-analysis.git
cd restaurant-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
