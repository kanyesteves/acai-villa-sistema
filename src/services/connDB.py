from sqlalchemy import create_engine
from pathlib import Path

PATH_TO_DB = '/Users/kanydianesteves/projetos/sistema-pedidos/db/db_users.sqlite'

class ConnectDB():
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{PATH_TO_DB}')