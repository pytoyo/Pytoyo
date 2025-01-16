import streamlit as st
import pandas as pd
st.title('Sistema contas a pagar a receber')

def home():
    st.title("Bem-vindo à página inicial!")
    st.write("Você está logado e acessando a página principal.")

if __name__ == "__main__":
    if "logged_in" in st.session_state and st.session_state.logged_in:
        home()
    else:
        st.error("Você não está logado. Por favor, faça o login.")
