import streamlit as st
from services.createTableUsers import CreateTableUsers, Base
from services.connDB import ConnectDB

base = Base()
connection = ConnectDB()
engine = connection.engine

st.set_page_config(
    layout="wide",
    page_title="Esboço"
)

base.metadata.create_all(bind=engine)
st.title("Pedido")

col1, col2 = st.columns(2)
lanche = col1.selectbox("Lanche", ["Cachorro Quente", "Porção"])
if "Cachorro Quente" in lanche:
    col2.selectbox("Adicional", ["Milho verde", "Cheedar", "Catupiry", "Mussarela", "Bacon", "Calabresa"])
else: 
    col2.selectbox("Adicional", ["Bacon", "Calabresa"])