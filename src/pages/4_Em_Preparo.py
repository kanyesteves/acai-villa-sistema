import streamlit as st


def main():
    st.sidebar.subheader(f"Usuário logado: {st.session_state.user['name']}")

    col1, col2 = st.columns([2, 0.5])
    col1.title("Em Preparo")
    if col2.button("Logout"):
        st.session_state.user = {}
        st.session_state.login = False
        st.switch_page("login.py")

    st.divider()






if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()