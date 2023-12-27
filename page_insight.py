import streamlit as st

def show_insight():
    st.title('Insight from Twitter Sentiment Analysis')

    st.markdown('### **Apa kata-kata yang sering muncul pada sentimen positif?**')
    st.image('images/positive_wordcloud.png')
    st.write('Tampak wordcloud yang menampilkan kata-kata yang paling sering muncul pada sentimen positif.')
    st.write('Kita bisa lihat bahwa kata-katanya memiliki vibes positif, seperti thank, love, lol, well, fun, haha, dan sebagainya.')

    st.markdown('### **Apa kata-kata yang sering muncul pada sentimen negatif?**')
    st.image('images/negative_wordcloud.png')
    st.write('Wordcloud tersebut menunjukkan kata-kata yang paling sering muncul pada sentimen positif.')
    st.write('Tampak kata-katanya memiliki vibes negatif, seperti hate, miss, bad, sad, dan suck.')

    st.markdown('### **Apa saja gabungan 2 kata yang paling sering muncul pada sentimen positif?**')
    st.image('images/positive_bigrams.png')
    st.write('Kita bisa melihat dengan jelas bahwa semua kata-kata tersebut memiliki nuansa positif.')
    st.write('Jika kita lihat, mayoritas berupa sapaan dan ucapan, seperti good morning, good night, dan happy birthday..')
    
    
    st.markdown('### **Apa saja gabungan 2 kata yang paling sering muncul pada sentimen negatif?**')
    st.image('images/negative_bigrams.png')
    st.write('Tampak bahwa kata-kata tersebut memiliki nuansa negatif.')
    st.write('Mayoritas kata-katanya berupa ungkapan perasaan sedih, bersalah, dan kata-kata yang diawali dengan "tidak".')


    st.markdown('## **Thank You 😀**')