import pandas as pd
from models.usersModel import UsersModel, Base
from utils.connDB import ConnectDB
from sqlalchemy import select
from sqlalchemy.orm import Session

class UsersService():
    def __init__(self):
        self.base = Base()
        self.conn = ConnectDB()

    def getUserById(self, id):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UsersModel).filter_by(id=id)
            user = session.execute(select_query).fetchall()
            return user[0][0]

    def createUser(self, name, senha, email, **kwargs):
        with Session(bind=self.conn.engine) as session:
            user = UsersModel(name=name, senha=senha, email=email, **kwargs)
            session.add(user)
            session.commit()

    def allUsers(self):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UsersModel)
            all_users = session.execute(select_query).fetchall()
            all_users = [user[0] for user in all_users]
            users = [
                {
                    "id": user.id,
                    "name": user.name,
                    "senha": user.senha,
                    "email": user.email,
                    "acess_gestor": user.acess_gestor
                }
                for user in all_users
            ]
            df = pd.DataFrame(users)
            return df

    
