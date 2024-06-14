from backend.utils.connDB import ConnectDB
from backend.models.userModel import UserBase
from backend.models.foodModel import FoodBase



connect = ConnectDB()
user_base = UserBase()
food_base = FoodBase()

# Criando tabelas do banco de dados
user_base.metadata.create_all(bind=connect.engine)
food_base.metadata.create_all(bind=connect.engine)