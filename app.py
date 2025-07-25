import streamlit as st
import os
import openai
openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
API_KEY = st.secrets.get("API_KEY", os.getenv("API_KEY"))
API_SECRET_KEY = st.secrets.get("API_SECRET_KEY", os.getenv("API_SECRET_KEY"))
SUPPLIER_ID = st.secrets.get("SUPPLIER_ID", os.getenv("SUPPLIER_ID"))
import json
import kalemSoru17temmuz
from kalemSoru17temmuz import process_order_response, barcode_model_lookup

st.title("Kalem Soru Analiz Uygulaması")

soru_metni = st.text_area("Lütfen JSON formatında sipariş bilgisini girin:")

adet = st.number_input("Adet:", min_value=1, step=1, value=1)

if st.button("Analiz Et"):
    if soru_metni.strip() == "":
        st.warning("Lütfen soru metni girin.")
    else:
        try:
            json_data = json.loads(soru_metni)
            sonuc = process_order_response(json_data, barcode_model_lookup, adet)
            st.success("İşlem Sonucu:")
            st.json(sonuc)
        except Exception as e:
            st.error(f"Hata: {str(e)}")