import streamlit as st
import requests
import pandas as pd

URL01 = "https://dbc2ah.deta.dev"
URL02 = "https://f4ykht.deta.dev"
URL03 = "https://0ek14b.deta.dev"

server = st.sidebar.radio("サーバー", ("サーバー01 (deta.sh)", "サーバー02 (deta.sh)", "サーバー03 (deta.sh)"))
if st.session_state:
    st.sidebar.write('public key')
    st.sidebar.info(st.session_state["public_key"])
    st.sidebar.write('private key')
    st.sidebar.info(st.session_state["private_key"])


st.title('ブロック')
if server == "サーバー01 (deta.sh)":
    res01 = requests.get(URL01 + '/chain').json()['blocks']
    res01_pd = pd.DataFrame([res.values() for res in res01], columns= ['hash', 'nonce', 'time', 'transaction'])
    st.table(res01_pd)
elif server == "サーバー02 (deta.sh)":
    res02 = requests.get(URL02 + '/chain').json()['blocks']
    res02_pd = pd.DataFrame([res.values() for res in res02], columns= ['hash', 'nonce', 'time', 'transaction'])
    st.table(res02_pd)
elif server == "サーバー03 (deta.sh)":
    res03 = requests.get(URL03 + '/chain').json()['blocks']
    res03_pd = pd.DataFrame([res.values() for res in res03], columns= ['hash', 'nonce', 'time', 'transaction'])
    st.table(res03_pd)


st.title('マイニング')
if st.session_state:
    public_key = st.text_input(label='public key', value=st.session_state["public_key"])
else:
    public_key = st.text_input(label='public key', value='')
button = st.button('ブロック作成')

if button:
    if public_key:
        if server == "サーバー01 (deta.sh)":
            requests.get(URL01 + '/create_block/' + public_key)
        elif server == "サーバー02 (deta.sh)":
            requests.get(URL02 + '/create_block/' + public_key) 
        elif server == "サーバー03 (deta.sh)":
            requests.get(URL03 + '/create_block/' + public_key)
    else:
        st.info('入力に誤りがあります。')