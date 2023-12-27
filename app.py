import streamlit as st
from page_predict_sentiment import show_predict_sentiment
from page_insight import show_insight
from page_model_information import show_model_information
import nltk

nltk.download('wordnet')

page = st.sidebar.radio("Choose Option", ("Predict Sentiment", "Insight", "Model Information"))

if page == 'Predict Sentiment':
    show_predict_sentiment()
elif page == 'Insight':
    show_insight()
elif page == 'Model Information':
    show_model_information()