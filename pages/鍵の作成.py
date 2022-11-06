import streamlit as st
import requests
URL = "https://f4ykht.deta.dev/create_key"

st.title('鍵の作成')

res = requests.get(URL)
st.write('public key')
st.info(res.json()["public_key_str"])
st.write('private key')
st.info(res.json()["private_key_str"])

st.sidebar.write('public key')
st.sidebar.info(res.json()["public_key_str"])
st.sidebar.write('private key')
st.sidebar.info(res.json()["private_key_str"])

st.session_state['public_key'] = res.json()["public_key_str"]
st.session_state['private_key'] = res.json()["private_key_str"]