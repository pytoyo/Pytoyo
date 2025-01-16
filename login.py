import streamlit as st

def login():
    # Criação da interface de login
    st.title("Tela de Login")

    # Campos de input para usuário e senha
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    # Validação do login
    if st.button("Entrar"):
        if username == "admin" and password == "senha123":  # Validação simples
            st.session_state.logged_in = True
            st.session_state.page = "home"  # Definindo a página após o login
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos!")

def show_home():
    # Apenas exibe o conteúdo da home se o usuário estiver logado
    st.title("Bem-vindo à página inicial!")
    st.write("Você está logado e acessando a página principal.")
    # Aqui você pode colocar o conteúdo da home, como o menu

def show_menu():
    # Exibe o menu na barra lateral
    st.sidebar.title("Menu")
    st.sidebar.write("Aqui fica o menu, apenas visível após o login.")
    # Exemplo de menu
    st.sidebar.write("Item 1")
    st.sidebar.write("Item 2")

if __name__ == "__main__":
    # Verificando se o usuário está logado e qual página deve ser carregada
    if "logged_in" in st.session_state and st.session_state.logged_in:
        # Exibe o menu e a página inicial apenas se o usuário estiver logado
        show_menu()  # Só exibe o menu se o usuário estiver logado
        show_home()  # Página inicial após o login
    else:
        # Quando não estiver logado, exibe apenas a tela de login
        login()
