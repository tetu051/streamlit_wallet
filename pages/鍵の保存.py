import streamlit as st
import requests

st.title('鍵の保存')

st.write('※ページを離れた際に削除されます。')

public_key = st.text_input(label='public key', value='')
private_key = st.text_input(label='private_key', value='')
button = st.button('保存')

if button:
    if public_key and  private_key:
        st.session_state['public_key'] = public_key 
        st.session_state['private_key'] = private_key
        st.info('保存しました！残高は' + str(requests.get("https://f4ykht.deta.dev/utxo/" + st.session_state["public_key"]).json()["amount"]) + 'です。')
    else:
        st.info('入力欄に誤りがあります。')


if st.session_state:
    st.sidebar.write('public key')
    st.sidebar.info(st.session_state["public_key"])
    st.sidebar.write('private key')
    st.sidebar.info(st.session_state["private_key"])