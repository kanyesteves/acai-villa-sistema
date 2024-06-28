import streamlit as st
from backend.services.userService import UserService

st.set_page_config(
    layout="wide",
    page_title="Usuários"
)

userService = UserService()

@st.experimental_dialog("Adicionar um Usuário")
def addUser():
    with st.form("adicionar"):
        name = st.text_input("Nome")
        senha = st.text_input("Senha", type="password")
        office = st.text_input("Cargo")
        if st.form_submit_button("Adicionar"):
            userService.createUser(name=name, senha=senha, office=office)
            st.success("Adicionado com sucesso !")

@st.experimental_dialog("Atualizar um usuário")
def updateUser():
    st.write("atualizar")

@st.experimental_dialog("Remover um usuário")
def removeUser():
    st.write("remover")


def main():
    all_users = userService.getAllUsers()
    st.sidebar.subheader(f"Usuário logado: {st.session_state.user['name']}")

    col1, col2 = st.columns([2, 0.5])
    col1.title("Usuários")
    if col2.button("Logout"):
        st.session_state.user = {}
        st.session_state.login = False
        st.switch_page("login.py")

    st.divider()

    container = st.container(border=True)
    col1, col2 = container.columns([0.5, 2.5])
    if col1.button("Adicionar usuário", type="primary"):
        addUser()
    if col1.button("Atualizar usuário", type="primary"):
        updateUser()
    if col1.button("Remover usuário", type="primary"):
        removeUser()
    if col1.button("Atualizar tabela", type="primary"):
        all_users = userService.getAllUsers()

    with col2.expander("Tabela de Usuários"):
        all_users



if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()