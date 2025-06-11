import streamlit as st

st.set_page_config(
    page_title="Insights Analysis",
    page_icon="📈"
)

def show_insight():
    st.title('📈 Insights from Twitter Sentiment Analysis')

    st.markdown('### **Apa kata-kata yang sering muncul pada sentimen positif?**')
    st.image('images/wc_positif.png')
    with st.expander('📋 Analisis insights', expanded=True):
        st.info('Word cloud tersebut menampilkan kata-kata yang paling sering muncul pada sentimen positif.')
        st.info("Tampak kata-katanya memiliki vibes positif, seperti love, thank, lol, great, nice, fun, well, yay, dan sebagainya. Kata 'love' yang sangat besar menunjukkan bahwa tweet bersentimen positif didominasi oleh kata-kata yang menunjukkan rasa suka dan kepuasaan terhadap suatu hal. Adanya dominasi kata 'thank' juga menunjukkan bahwa tweet dengan sentimen positif sering berisi ungkapan terima kasih dan rasa syukur. Kata-kata lainnya pada word cloud tersebut juga menunjukkan ekspresi kebahagiaan, cinta, antuisiasme, dan kegembiraan dari pengguna Twitter terhadap suatu hal.")

    st.markdown('### **Apa kata-kata yang sering muncul pada sentimen negatif?**')
    st.image('images/wc_negatif.png')
    with st.expander('📋 Analisis insights', expanded=True):
        st.info('Word cloud tersebut menampilkan kata-kata yang paling sering muncul pada sentimen negatif.')
        st.info("Tampak kata-katanya memiliki vibes negatif, seperti hate, miss, bad, sad, sorry, sick, dan suck. Berbagai kata tersebut menunjukkan ekspresi kekecewaan, kebencian, penyesalan, dan kemarahan dari para pengguna Twitter. Banyak ungkapan yang menunjukkan rasa tidak suka terhadap suatu hal, seperti barang dan seseorang. Banyaknya kata 'work' pada sentimen negatif juga menunjukkan perasaan stress dan kekesalan pengguna terhadap pekerjaan mereka.")

    st.markdown('### **Apa saja gabungan 2 kata yang paling sering muncul pada sentimen positif?**')
    st.image('images/bigrams_positif.png')
    with st.expander('📋 Analisis insights', expanded=True):
        st.info('Bigrams tersebut menunjukkan gabungan dari 2 kata yang sering muncul bersama-sama pada sentimen positif.')
        st.info('Tampak hal menarik bahwa tweet yang memiliki sentimen positif sering disertai dengan ucapan, seperti good morning, good luck, good night, dan sebagainya. Terlihat pula bahwa tweet sentimen positif didominasi oleh ucapan ulang tahun dan ucapan hari ibu. Kata looking forward juga sering muncul pada sentimen positif sehingga menunjukkan bahwa sentimen positif didominasi dengan harapan dan kebahagiaan pengguna terhadap suatu hal.')
    
    st.markdown('### **Apa saja gabungan 2 kata yang paling sering muncul pada sentimen negatif?**')
    st.image('images/bigrams_negatif.png')
    with st.expander('📋 Analisis insights', expanded=True):
        st.info('Tampak insight menarik pada gabungan 2 kata yang sering muncul pada sentimen negatif.')
        st.info("Terlihat jelas bahwa bigrams sentimen negatif didominasi oleh kata-kata negasi, seperti don't want, don't think, don't like, don't wanna, dan sebagainya sehingga memunculkan kesan negatif. Kata 'feel like' juga menunjukkan bahwa sentimen negatif didominasi oleh curhatan tentang perasaan seseorang. Dominasi kata 'look like' menunjukkan bahwa tweet yang memiliki sentimen negatif berisi tentang penilaian atau kekhawatiran seseorang terhadap sesuatu. Ungkapan 'don't like' juga menunjukkan bahwa tweet bersentimen negatif sering berisi tentang ketidaksukaan atau ketidakpuasan terhadap suatu hal, seperti orang, produk, atau situasi. Maka, tampak jelas bahwa kata-kata yang mendominasi sentimen negatif berbeda dengan sentimen positif sehingga keduanya terpisahkan dengan jelas dan membantu model untuk mengklasifikasikan sentimen suatu tweet.")


    # st.markdown('## **Thank You 😀**')

show_insight()