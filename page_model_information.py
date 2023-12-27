import streamlit as st
import pandas as pd

def show_model_information():
    st.title('Model Information')

    st.write('Model yang dicoba:')
    st.write('1. Logistic Regression (Best)')
    st.write('2. Bernoulli Naive Bayes')
    st.write('3. XGBoost Classifier')

    st.markdown('### **Akurasi Setiap Model**')
    st.image('images/model_accuracy.png')
    st.write('Semua model tidak ada yang overfitting karena akurasi data train dan data test tidak jauh berbeda. Semua model tidak ada yang underfitting, serta akurasinya pun cukup baik.')
    st.write('Tampak bahwa model Logistic Regression menghasilkan akurasi yang paling tinggi, yaitu 83% untuk data train dan 82% untuk data test.')
    st.write('Hal ini masuk akal karena logistic regression cukup efisien untuk data dengan dimensi yang tinggi, seperti data teks ini.')
    st.write('Model ini juga lebih cepat dalam waktu training dibandingkan model yang lain, seperti XGBoost.')
    st.write('Oleh karena itu, saya menggunakan Logistic Regression untuk memprediksi sentimen dari teks yang dimasukkan user.')


    st.markdown('## **Thank You 😀**')