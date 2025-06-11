import streamlit as st
import pickle
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
import joblib

st.set_page_config(
    page_title="Twitter Sentiment Analyzer",
    page_icon="🤓"
)

@st.cache_data
def load_model():
    with open('models/logistic_regression_model_base.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

@st.cache_data
def load_vectorizer():
    tfidf_vectorizer = joblib.load('models/tfidf_vectorizer_base.pkl')
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
    
    nltk.download('wordnet')
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


def show_predict():
    st.title('🤓 Sentiment Analyzer')

    # with st.form("user_input"):
    st.info('📢 Tip: Silakan klik tombol "Generate Random Text" untuk mengisi inputan dengan teks random agar lebih mudah untuk mencoba-coba sistem prediksi ini.')

    text_list = [
        "I hate when I have to call and wake people up",
        "I'm really sad today",
        "I love the new design of Toyota Innova",
        "This is the best day of my life",
        "I am so excited about the new project",
        "I feel so depressed and hopeless",
        "The weather is terrible today",
        "I am so grateful for all the support I have received",
        "I am so angry at my friend for canceling our plans",
        "I am so proud of my team for finishing the project on time",
        "I am so frustrated with the traffic today",
        "The movie was amazing, I loved it!",
        "He is such a kind person, always helping others",
        "I am so nervous about the upcoming exam",
        "I hate when that happen.",
        "Just woke up and can't sleep. This sucks",
        "Love my new sweater, it's so warm and cozy",
        "This product is awesome, I highly recommend it!",
        "I am so disappointed with the service I received",
        "I'm really tired today, I need a break",
        "Happy to be here with you all",
    ]

    # Inisialisasi session_state jika belum ada
    if "input_text" not in st.session_state:
        st.session_state.input_text = "I am so happy to see my family again"

    # Tombol untuk generate random text
    if st.button('🔄 Generate Random Text', help='Klik untuk menghasilkan teks acak'):
        rand_idx = np.random.randint(0, len(text_list))
        st.session_state.input_text = text_list[rand_idx]

    # Input teks
    text = st.text_input("📋 Masukkan teks yang ingin diprediksi sentimennya:", 
                        value=st.session_state.input_text, 
                        key="input_text", 
                        help='Masukkan teks yang ingin Anda analisis sentimennya')

    # Tombol prediksi
    if st.button("🔍 Predict"):
        if text == '':
            st.warning('⚠️ Silakan masukkan teks terlebih dahulu.')
            return
        else:
            hasil_sentimen = predict_sentiment(text)
            # st.write('Teks yang dimasukkan:', text)
            if hasil_sentimen[0] == 0:
                font_color = 'red'
                st.markdown(f"<h3>Sentimen: <span style='color: {font_color}'>Negatif</span></h3>", unsafe_allow_html=True)
            elif hasil_sentimen[0] == 1:
                font_color = 'green'
                st.markdown(f"<h3>Sentimen: <span style='color: {font_color}'>Positif</span></h3>", unsafe_allow_html=True)
        st.info('🕵️ Silakan klik tombol "Generate Random Text" untuk mencoba teks lainnya.')


show_predict()