import streamlit as st
import requests
import json
import datetime
from ecdsa import SigningKey
from ecdsa import SECP256k1
import binascii

url = "https://f4ykht.deta.dev/transaction_pool"

def main(sender_public_key, sender_private_key, receiver_public_key, amount, description, url):
    time = datetime.datetime.now().isoformat()
    transaction_unsigned = {
        "time": time,
        "sender": sender_public_key,
        "receiver": receiver_public_key,
        "amount": amount,
        "description": description,
    }

    signature_hex =  signature(transaction_unsigned, sender_private_key)
    transaction = {
        "time": time,
        "sender": sender_public_key,
        "receiver": receiver_public_key,
        "amount": amount,
        "description": description,
        "signature": signature_hex
    }
    return requests.post(url, json.dumps(transaction)).json()['message']


def signature(transaction_unsigned, sender_private_key):
    private_key_byte = binascii.unhexlify(sender_private_key)
    private_key = SigningKey.from_string(private_key_byte, curve=SECP256k1)
    transaction_unsigned_json = json.dumps(transaction_unsigned)
    transaction_unsigned_bytes = bytes(transaction_unsigned_json, encoding = 'utf-8')
    signature_bytes = private_key.sign(transaction_unsigned_bytes)
    signature_hex = signature_bytes.hex()
    return signature_hex


st.title('コインの送信')
if st.session_state:
    sender_public_key = st.text_input(label='public key', value=st.session_state["public_key"])
    sender_private_key = st.text_input(label='private key', value=st.session_state["private_key"])
else:
    sender_public_key = st.text_input(label='public key', value='')
    sender_private_key = st.text_input(label='private key', value='')
receiver_public_key = st.text_input(label='receiver public key', value='')
amount = st.text_input(label='amount', value='')
description = st.text_input(label='description', value='')
button = st.button('送信')

if st.session_state:
    st.sidebar.write('public key')
    st.sidebar.info(st.session_state["public_key"])
    st.sidebar.write('private key')
    st.sidebar.info(st.session_state["private_key"])

if button:
    if sender_public_key and sender_private_key and receiver_public_key and amount and description and url:
        st.info(main(sender_public_key, sender_private_key, receiver_public_key, amount, description, url))
    else:
        st.info('入力欄に誤りがあります。')