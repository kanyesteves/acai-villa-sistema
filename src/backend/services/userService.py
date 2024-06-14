import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.utils.libs import Libs
from backend.utils.connDB import ConnectDB
from backend.models.userModel import UserModel

class UserService():
    def __init__(self):
        self.conn = ConnectDB()
        self.lib = Libs()


    def getUserById(self, id):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UserModel).filter_by(id=id)
            user = session.execute(select_query).fetchall()
            return user[0][0]

     
    def getAllUsers(self):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UserModel)
            all_users = session.execute(select_query).fetchall()
            all_users = [user[0] for user in all_users]
            users = [
                {
                    "id": user.id,
                    "name": user.name,
                    "senha": user.senha,
                    "office": user.office,
                    "acess_gestor": user.acess_gestor
                }
                for user in all_users
            ]
            df = pd.DataFrame(users)
            return df


    def createUser(self, name, senha, office, **kwargs):
        with Session(bind=self.conn.engine) as session:
            user = UserModel(name=name, senha=self.lib.set_password(senha), office=office, **kwargs)
            session.add(user)
            session.commit()


    def updateUser(self, id, **kwargs):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UserModel).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                for key, value in kwargs.items():
                    if key == 'senha':
                        user[0].senha = self.lib.set_password(value)
                    else:
                        setattr(user[0], key, value)

            session.commit()


    def deleteUser(self, id):
        with Session(bind=self.conn.engine) as session:
            select_query = select(UserModel).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                session.delete(user[0])

            session.commit()
    
