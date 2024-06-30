import streamlit as st
from backend.services.userService import UserService

st.set_page_config(
    layout="wide",
    page_title="Usuários"
)

userService = UserService()

@st.experimental_dialog("Adicionar um Usuário")
def addUser():
    with st.form("Adicionar"):
        name = st.text_input("Nome")
        senha = st.text_input("Senha", type="password")
        office = st.text_input("Cargo")
        if st.form_submit_button("Adicionar"):
            userService.createUser(name=name, senha=senha, office=office)
            st.success("Adicionado com sucesso !")
            st.switch_page("pages/1_Usuarios.py")

@st.experimental_dialog("Atualizar um usuário")
def updateUser():
    with st.form("Atualizar"):
        id = st.text_input("ID")
        name = st.text_input("Nome")
        senha = st.text_input("Senha", type="password")
        office = st.text_input("Cargo")
        if st.form_submit_button("Atualizar"):
            userService.updateUser(id, name=name, senha=senha, office=office)
            st.success("Atualizado com sucesso !")
            st.switch_page("pages/1_Usuarios.py")

@st.experimental_dialog("Remover um usuário")
def removeUser():
    with st.form("Remover"):
        id = st.text_input("ID")
        if st.form_submit_button("Remover"):
            userService.deleteUser(id)
            st.success("Removido com sucesso !")
            st.switch_page("pages/1_Usuarios.py")


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

    col1, col2, col3 = st.columns([1, 1, 1])    
    if col1.button("Adicionar", type="primary"):
        addUser()
        all_users = userService.getAllUsers()
    if col2.button("Atualizar", type="primary"):
        updateUser()
        all_users = userService.getAllUsers()
    if col3.button("Remover", type="primary"):
        removeUser()
        all_users = userService.getAllUsers()

    with st.expander("Tabela de Usuários"):
        all_users = all_users.drop("senha", axis='columns')
        st.table(all_users)



if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()