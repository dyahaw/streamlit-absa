import streamlit as st
# import pickle

# load save model

# judul halaman
st.title("Aspect Based Sentimen Analysis Suatu Ulasan")

text_input = st.text_input("Masukkan Kalimat Ulasan")
# aspect_classification = ''
prediksi = st.button("Hasil Prediksi")

if prediksi:
    # aspek = model.predict(loaded_vec.fit_transfor([text_input]))
    # sentimen =
    # if (sentimen == -1):
    #     kelas_sentimen = 'Negatif'
    # else:
    #     kelas_sentimen = 'Positif'
    # st.success(f"Kelas Aspek {aspek}, Sentimen {sentimen}")
    aspek = ('responsiveness')
    sentimen = ('positif')
    st.success(f"Kelas Aspek {aspek}, Sentimen {sentimen}")
