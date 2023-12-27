import streamlit as st
import pickle
import re
from nltk.stem import WordNetLemmatizer
import joblib

def load_model():
    with open('sentiment_model.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

def load_vectorizer():
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    return tfidf_vectorizer

def cleanText(text):
    cleanedText = []

    links = r'http\S+|www\S+|https\S+'
    userPattern = '@[^\s]+'
    apostrophe = r"'"
    nonWord = r'\W'
    singleCharacter = r'\s+[a-zA-Z]\s+'
    caretSymbol = r'\^[a-zA-Z]\s+'
    alphabet = "[^a-zA-Z0-9]"
    sequencePattern = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    multiSpace = r'\s+'

    text = text.lower()

    text = re.sub(links, ' ', text, flags=re.MULTILINE)

    text = re.sub(userPattern,' ', text)
    text = re.sub(apostrophe, '', text)
    text = re.sub(nonWord, ' ', text)
    text = re.sub(singleCharacter, ' ', text)
    text = re.sub(caretSymbol, ' ', text) 
    text = re.sub(alphabet, " ", text)
    text = re.sub(sequencePattern, seqReplacePattern, text)
    
    text = re.sub(multiSpace, ' ', text, flags=re.I)
    
    wordLemm = WordNetLemmatizer()

    words = ''
    for word in text.split():
        if len(word)>1:
            if word != 'was':
                word = wordLemm.lemmatize(word)
            words += (word+' ')

    cleanedText.append(words)

    return " ".join(cleanedText)

def predict_sentiment(text):
    cleaned_text = cleanText(text)

    text_vectorized = tfidf_vectorizer.transform([cleaned_text])

    sentiment_prediction = model.predict(text_vectorized)

    return sentiment_prediction

model = load_model()
tfidf_vectorizer = load_vectorizer()

def show_predict_sentiment():

    st.title('Sentiment Prediction')

    text = st.text_input('Masukkan teks yang ingin diprediksi sentimennya: (gunakan Bahasa Inggris)')
    analyze = st.button('Predict Sentiment')

    if analyze:
        if text == '':
            st.write('Silakan masukkan teks terlebih dahulu.')
            return
        else:
            hasil_sentimen = predict_sentiment(text)
            if hasil_sentimen[0] == 0:
                st.subheader('Sentimen: Negatif')
            elif hasil_sentimen[0] == 1:
                st.subheader('Sentimen: Positif')
                