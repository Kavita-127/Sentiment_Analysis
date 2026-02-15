import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("sentiment_model.pkl")

st.set_page_config(page_title="Sentiment Analysis", layout="centered")

st.title("🍽 Restaurant Review Sentiment Analysis")
st.write("This model predicts whether a restaurant review is Positive or Negative.")

# User input
user_input = st.text_area("Enter your review here:")

if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter a review first.")
    else:
        prediction = model.predict([user_input])

        if prediction[0] == 1:
            st.success("✅ Positive Review 😊")
        else:
            st.error("❌ Negative Review 😠")

# Dataset Preview
if st.checkbox("Show Sample Dataset"):
    df = pd.read_csv("Restaurant_Reviews.tsv", sep="\t")
    st.dataframe(df.head())
