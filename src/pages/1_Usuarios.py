import streamlit as st
from backend.services.userService import UserService

st.set_page_config(
    layout="wide"
)

userService = UserService()

@st.experimental_dialog("Adicionar um usuário")
def addUser():
    st.write("cadastrar")

@st.experimental_dialog("Atualizar um usuário")
def updateUser():
    st.write("atualizar")

@st.experimental_dialog("Remover um usuário")
def removeUser():
    st.write("remover")


def main():
    st.sidebar.subheader(f"Usuário logado: {st.session_state.user['name']}")

    col1, col2 = st.columns([2, 0.5])
    col1.title("Usuários")
    st.divider()
    if col2.button("Logout"):
        st.session_state.user = {}
        st.session_state.login = False
        st.switch_page("login.py")

    
    col1, col2, col3 = st.columns(3)
    if col1.button("Adicionar usuário"):
        addUser()
    if col2.button("Atualizar usuário"):
        updateUser()
    if col3.button("Remover usuário"):
        removeUser()

    all_users = userService.getAllUsers()
    all_users









if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()