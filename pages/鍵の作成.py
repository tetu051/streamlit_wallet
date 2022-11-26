import streamlit as st
import requests
from ecdsa import SigningKey
from ecdsa import SECP256k1

private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.verifying_key
private_key_hex = private_key.to_string().hex()
public_key_hex = public_key.to_string().hex()

st.title('鍵の作成')

st.write('public key')
st.info(public_key_hex)
st.write('private key')
st.info(private_key_hex)

st.sidebar.write('public key')
st.sidebar.info(public_key_hex)
st.sidebar.write('private key')
st.sidebar.info(private_key_hex)

st.session_state['public_key'] = public_key_hex
st.session_state['private_key'] = private_key_hex