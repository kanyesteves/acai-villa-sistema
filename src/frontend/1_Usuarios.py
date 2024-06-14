import streamlit as st
# from backend.services.userService import UserService

st.set_page_config(
    layout="wide",
    page_title="Cadastro de Usuários"
)

# userService = UserService()

def login():
    with st.container(border=True):
        st.title("Login")


def main():
    login()


if __name__ == '__main__':
    main()