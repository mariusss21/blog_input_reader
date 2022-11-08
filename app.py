import streamlit as st
import json
import pandas as pd

from google.cloud import firestore
from google.oauth2 import service_account


# page config
st.set_page_config(
     page_title="Blog",
)

m = st.markdown("""
<style>
div.stButton > button:first-child{
    width: 100%;
    font-size: 18px;
}
label.css-qrbaxs{
    font-size: 18px;
}
p{
    font-size: 18px;
}
h1{
    text-align: center;
}
div.block-container{
    padding-top: 1rem;
}
div.streamlit-expanderHeader{
    width: 100%;
    font-size: 18px;
    background-color: rgb(240,242,246);
    color: black;
}
</style>""", unsafe_allow_html=True)

# database config
# key_dict = json.loads(st.secrets['firebase_info'])
# creds = service_account.Credentials.from_service_account_info(key_dict)
creds = service_account.Credentials.from_service_account_info(st.secrets["firebase_info"])
db = firestore.Client(credentials=creds, project='portfolio-blog')

# teste banco de dados

botao = st.button('teste db')
if botao:
    dados = {'cu': 'bilola'}
    doc_ref = db.collection('bobinas').document('bobinas')
    try:
        doc_ref.set(dados)
        st.success('teste ok')
    except Exception as e:
        st.error(e)



