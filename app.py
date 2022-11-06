import streamlit as st
import requests

st.title('walletへようこそ')

if st.session_state:
    if not requests.get("https://f4ykht.deta.dev/utxo/" + st.session_state["public_key"]).json()["amount"]:
        st.write('鍵が作成できたようですね！')
        st.write('それでは送信を。。。コインを持っていないようです。')
        st.write('コインは、持っている人に送ってもらうか、マイニングをしてみてくださいね！')
    else:
        st.write('コインを手に入れたようですね！おめでとうございます！')
        st.write('コインを送るときは送信先の鍵もしっかりと確認してくださいね。')
        st.write('バグがありましたら報告お願いします。それでは！')
else:
    st.write('まずは、鍵を作成してみましょう。')

if st.session_state:
    st.sidebar.write('public key')
    st.sidebar.info(st.session_state["public_key"])
    st.sidebar.write('private key')
    st.sidebar.info(st.session_state["private_key"])