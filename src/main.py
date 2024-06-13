import streamlit as st
from services.usersService import UsersService
from models.usersModel import Base
from utils.connDB import ConnectDB

st.set_page_config(
    layout="wide",
    page_title="Esboço"
)

## TESTES

base = Base()
userService = UsersService()
conn = ConnectDB()

base.metadata.create_all(conn.engine)
userService.createUser("admin", "132567", "admin@teste.com") 


# response = userService.getAllUsers()
# response
# userService.updateUser(4, name="Novo nome", senha="teste132")
# user = userService.getUserById(5)

# userService.deleteUser(3)

# st.title(f"{user.name} - < {user.email} >")
