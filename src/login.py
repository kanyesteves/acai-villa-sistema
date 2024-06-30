import streamlit as st
from time import sleep
from backend.services.userService import UserService
from backend.utils.libs import Libs

st.set_page_config(
    layout="wide",
    page_title="Cadastro de Usuários"
)

userService = UserService()
lib = Libs()

def login():
    with st.container(border=True):

        st.subheader("Login Açaí da Villa")
        users = userService.getAllUsers()
        all_users = userService.all_users
        user_selected = st.selectbox("Usuário", users["name"])
        passwd = st.text_input("Senha", type="password")
        for user_name in all_users:
            if user_name["name"] == user_selected:
                user = user_name

        if st.button("Entrar"):
            if lib.check_password(user["senha"], passwd):
                st.success("Login efetuado com sucesso!!")
                st.session_state.user = user
                st.session_state.login = True
                sleep(1)
                st.rerun()
            else:
                st.error(f"Senha do {user["name"]} incorreta")

def main():
    if not 'login' in st.session_state:
        st.session_state.login = False

    if not st.session_state.get("login"):
        login()
    else:
        st.switch_page("pages/1_Usuarios.py")


if __name__ == '__main__':
    main()