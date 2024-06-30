import streamlit as st
from backend.services.foodService import FoodService

st.set_page_config(
    layout="wide",
    page_title="Lanches"
)

foodService = FoodService()

@st.experimental_dialog("Adicionar um lanche")
def addFood():
    with st.form("Adicionar"):
        name_food = st.text_input("Nome do lanche")
        type_food = st.text_input("Tipo do lanche")
        description = st.text_input("Descrição")
        if st.form_submit_button("Adicionar"):
            foodService.createFood(name=name_food, food_type=type_food, description=description)
            st.success("Adicionado com sucesso !")
            st.switch_page("pages/2_Lanches.py")

@st.experimental_dialog("Atualizar um lanche")
def updateFood():
    with st.form("Atualizar"):
        id = st.text_input("ID")
        name_food = st.text_input("Nome do lanche")
        type_food = st.text_input("Tipo do lanche")
        description = st.text_input("Descrição")
        if st.form_submit_button("Atualizara"):
            foodService.updateFood(id, name=name_food, food_type=type_food, description=description)
            st.success("Adicionado com sucesso !")
            st.switch_page("pages/2_Lanches.py")

@st.experimental_dialog("Remover um lanche")
def removeFood():
    with st.form("Remover"):
        id = st.text_input("ID")
        if st.form_submit_button("Remover"):
            foodService.deleteFood(id)
            st.success("Removido com sucesso !")
            st.switch_page("pages/2_Lanches.py")


def main():
    all_foods = foodService.getAllFoods()
    st.sidebar.subheader(f"Usuário logado: {st.session_state.user['name']}")

    col1, col2 = st.columns([2, 0.5])
    col1.title("Lanches")
    if col2.button("Logout"):
        st.session_state.user = {}
        st.session_state.login = False
        st.switch_page("login.py")

    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])
    if col1.button("Adicionar", type="primary"):
        addFood()
        all_foods = foodService.getAllFoods()
    if col2.button("Atualizar", type="primary"):
        updateFood()
        all_foods = foodService.getAllFoods()
    if col3.button("Remover", type="primary"):
        removeFood()
        all_foods = foodService.getAllFoods()

    with st.expander("Tabela de Lanches"):
        all_foods


if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()