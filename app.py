import streamlit as st
import json
import kalemSoru17temmuz as ks17
import openai

# Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]
API_KEY = st.secrets["API_KEY"]
API_SECRET_KEY = st.secrets["API_SECRET_KEY"]
SUPPLIER_ID = st.secrets["SUPPLIER_ID"]

st.title("Kalem Soru Analiz Uygulaması")


# Soru metni
soru_metni = st.text_area("Müşteri mesajını girin", height=150)

# Adet belirleme
adet = st.number_input("Adet:", min_value=1, step=1, value=1)

if st.button("Analiz Et"):
    if not soru_metni.strip():
        st.warning("Lütfen müşteri mesajını girin.")
    else:
        try:
            st.info("Analiz ediliyor...")
            json_cevap = ks17.analiz_fonksiyonu(soru_metni, "DESC", False, adet)
            st.json(json_cevap)

            # Onaylama
            onay = st.radio("Bu yanıtı onaylıyor musunuz?", ("Evet", "Hayır", "Düzenle"))
            if onay == "Evet":
                st.success("Yanıt onaylandı.")
            elif onay == "Hayır":
                st.warning("Yanıt reddedildi.")
            else:
                st.info("Lütfen düzenleme yapınız.")
        except Exception as e:
            st.error(f"Hata: {str(e)}")