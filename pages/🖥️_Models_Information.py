import streamlit as st

st.set_page_config(
    page_title="Models Information",
    page_icon="🖥️"
)

def show_model_information():
    st.title('🖥️ Models Information')

    st.markdown('### **1️⃣ Case Pertama**')
    st.write('Pada case 1, saya menggunakan seluruh baris pada data, yaitu sebanyak 1.6 juta baris.')
    st.write('Dengan menggunakan seluruh data tersebut, maka tidak semua model dapat dilatih karena beberapa model membutuhkan waktu yang sangat lama untuk memproses 1.6 juta baris data tersebut.')
    st.write('Oleh karena itu, hanya 3 model yang dilatih pada case ini:')
    st.write('1. Logistic Regression (Best)')
    st.write('2. Bernoulli Naive Bayes')
    st.write('3. XGBoost Classifier')

    st.image('images/case1.png')

    st.markdown('### **🔍 Analisis Case 1**')
    st.write('Metrik yang saya gunakan untuk mengevaluasi performa model adalah F1 Score.')
    st.write('Hal tersebut karena precision dan recall sama-sama penting pada kasus sentimen analysis ini. Skor F1 dapat memberikan gambaran yang lebih baik tentang keseimbangan performa antara precision dan recall. Hal itu yang menyebabkan skor F1 digunakan sebagai metrik utama untuk mengevaluasi performa model pada kasus ini.')
    st.markdown('Saya berhasil mendapatkan skor F1 yang **lebih tinggi** dibandingkan submisi peserta lainnya pada Kaggle dengan dataset sama. Skor F1 tertinggi diraih oleh model Logistic Regression, yaitu berhasil mencapai 82.1%.')
    st.write('Tampak bahwa model Logistic Regression lebih unggul dibandingkan Bernoulli Naive Bayes. Hal tersebut karena BNB hanya menghitung probabilitas kata-kata pada setiap kelas sentimen, sedangkan Logistic Regression langsung bekerja dengan mencari pemisah antara kedua kelas berdasarkan bobot dari setiap katanya sehingga memberikan performa yang lebih baik pada kasus sentiment analysis seperti ini.')
    st.write('Model XGBoost juga memiliki skor F1 yang lebih rendah dibandingkan Logistic Regression. Hal tersebut dapat terjadi karena XGBoost dapat overfitting jika terdapat noise pada data. Data teks memiliki banyak fitur dan noise tidak bisa dihilangkan sepenuhnya sehingga XGBoost justru dapat terlalu fokus membuat cabang pohon yang merupakan noise sehingga performa pada data test menjadi lebih buruk. Selain itu, XGBoost juga membuat pohon baru dengan mengurangi kesalahan dari pohon sebelumnya sehingga jika kesalahan pada pohon sebelumnya ditimbulkan oleh noise, maka pohon baru tersebut justru mengurangi kesalahan yang tidak perlu karena dihasilkan oleh noise tersebut. Hal itu yang menyebabkan performa XGBoost lebih rendah pada kasus ini.')

    st.markdown('### **2️⃣ Case Kedua**')
    st.write('Pada case 2, saya melakukan sampling dengan mengambil 30 ribu baris dari keseluruhan data yang meliputi 15 ribu baris sentimen positif dan 15 ribu baris sentimen negatif.')
    st.write('Dengan mengurangi jumlah data, maka lebih banyak model yang dapat dicoba.')
    st.write('Model yang dicoba pada case ini adalah:')
    st.write('1. Logistic Regression (Best)')
    st.write('2. Support Vector Machine')
    st.write('3. Bernoulli Naive Bayes')
    st.write('4. Decision Tree Classifier')
    st.write('5. Random Forest Classifier')
    st.write('6. XGBoost Classifier')
    st.write('7. CatBoost Classifier')
    st.write('8. Convolutional Neural Network (CNN)')

    st.image('images/case2.png')

    st.markdown('### **🔍 Analisis Case 2**')
    st.write('Tampak bahwa model Logistic Regression lagi-lagi menghasilkan skor F1 tertinggi, yaitu 77.5%.')
    st.write('Angka tersebut masih lebih rendah 5% dari case pertama karena data yang digunakan pada case kedua hanya merupakan sampling dari case pertama sehingga ada beberapa informasi yang hilang. Hal tersebut menyebabkan performa model pada case kedua tidak sebaik pada case pertama.')
    st.write('Pada case ini, tampak bahwa performa model Logistic Regression, SVM, dan CNN cenderung mirip. CNN yang merupakan model deep learning belum mampu mengungguli model Logistic Regression dan SVM pada case ini. Bahkan, saya juga sudah mencoba menggunakan BERT dan hasilnya juga serupa dengan CNN tersebut.')
    st.write('Hal ini terjadi karena sentimen analysis merupakan task yang lebih cocok untuk model yang berbasis pada frekuensi kata, seperti Logistic Regression dan SVM. Model deep learning kontekstual seperti BERT lebih cocok untuk task yang membutuhkan pemahaman konteks mendalam, seperti text generation atau chatbot sehingga tidak memiliki keunggulan khusus pada kasus ini, padahal waktu trainingnya jauh lebih lama dibandingkan model Logistic Regression dan SVM.')
    st.write('Model SVM juga memiliki performa yang baik karena SVM bukan hanya mencari hyperplane pemisah saja, tetapi juga mencari hyperplane yang memiliki margin maksimal. Selain itu, SVM hanya menggunakan support vector untuk mencari hyperplane sehingga cocok digunakan pada data berdimensi tinggi, seperti data teks ini.')
    st.write('Model Catboost memiliki performa yang lebih baik dibandingkan model berbasis tree lainnya. Hal tersebut terjadi karena Catboost membuat pohon dengan mengurangi kesalahan dari pohon sebelumnya dan hal tersebut tidak dilakukan oleh Random Forest. Selain itu, Catboost menggunakan teknik ordered boosting sehingga dapat mengurangi kebocoran informasi di masa depan sehingga overfittingnya (dapat dilihat pada notebook) lebih rendah dibandingkan XGBoost.')
    st.write('Tampak hal menarik lainnya bahwa model decision tree memiliki skor F1 terendah. Hal tersebut terjadi karena DT dapat membuat pohon yang terlalu spesifik pada data train. Akibatnya, model menjadi sulit digeneralisasi pada data test sehingga melakukan banyak kesalahan saat memprediksi data yang belum pernah dilihat sebelumnya. Hal itu yang menyebabkan model DT cenderung overfitting (akurasi train dan test memiliki selisih mencapai 30% yang dapat dilihat pada notebook) dan memiliki performa terendah dibandingkan model lainnya.')


    # st.image('images/model_accuracy.png')
    # st.write('Semua model tidak ada yang overfitting karena akurasi data train dan data test tidak jauh berbeda. Semua model tidak ada yang underfitting, serta akurasinya pun cukup baik.')
    # st.write('Tampak bahwa model Logistic Regression menghasilkan akurasi yang paling tinggi, yaitu 83% untuk data train dan 82% untuk data test.')
    # st.write('Hal ini masuk akal karena logistic regression cukup efisien untuk data dengan dimensi yang tinggi, seperti data teks ini.')
    # st.write('Model ini juga lebih cepat dalam waktu training dibandingkan model yang lain, seperti XGBoost.')
    # st.write('Oleh karena itu, saya menggunakan Logistic Regression untuk memprediksi sentimen dari teks yang dimasukkan user.')


    st.markdown('## **Thank You 😀**')

show_model_information()