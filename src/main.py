import streamlit as st
from services.usersService import UsersService

st.set_page_config(
    layout="wide",
    page_title="Esboço"
)

## TESTES

userService = UsersService()


response = userService.allUsers()
response
user = userService.getUserById(2)

st.title(f"{user.name} - < {user.email} >")
