import streamlit as st
from utils.predictor import predict_news_veracity

st.set_page_config(page_title="TruthLens", layout="centered")

st.title("📰 TruthLens – AI News Veracity Detector")

news_input = st.text_area("Paste the news content or headline:")

if st.button("Analyze"):
    if news_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        label, confidence = predict_news_veracity(news_input)
        st.success(f"Prediction: **{label}**")
        st.info(f"Confidence Score: {confidence:.2f}")
