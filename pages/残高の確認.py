import streamlit as st
import requests
URL = "https://f4ykht.deta.dev/utxo/"

st.title('残高の確認')
if st.session_state:
    public_key = st.text_input(label='public key', value=st.session_state["public_key"])
else:
    public_key = st.text_input(label='public key', value='')
button = st.button('確認')
if st.session_state:
    st.sidebar.write('public key')
    st.sidebar.info(st.session_state["public_key"])
    st.sidebar.write('private key')
    st.sidebar.info(st.session_state["private_key"])

if button:
    if public_key:
        url = URL + public_key
        res = requests.get(url)
        st.info(str(res.json()["amount"]))
    else:
        st.info('入力欄が空です。')