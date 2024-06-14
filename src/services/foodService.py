import pandas as pd
from utils.libs import Libs
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session
from models.foodModel import FoodModel

class FoodService():
    def __init__(self):
        self.conn = ConnectDB()
        self.lib = Libs()


    def getFoodById(self, id):
        with Session(bind=self.conn.engine) as session:
            select_query = select(FoodModel).filter_by(id=id)
            food = session.execute(select_query).fetchall()
            return food[0][0]


    def getAllFoods(self):
        with Session(bind=self.conn.engine) as session:
            select_query = select(FoodModel)
            all_foods = session.execute(select_query).fetchall()
            all_foods = [food[0] for food in all_foods]
            foods = [
                {
                    "id": food.id,
                    "name": food.name,
                    "food_type": food.food_type,
                    "description": food.description
                }
                for food in all_foods
            ]
            df = pd.DataFrame(foods)
            return df


    def createFood(self, name, food_type, description):
        with Session(bind=self.conn.engine) as session:
            food = FoodModel(name=name, food_type=food_type, description=description)
            session.add(food)
            session.commit()


    def updateFood(self, id, **kwargs):
        with Session(bind=self.conn.engine) as session:
            select_query = select(FoodModel).filter_by(id=id)
            foods = session.execute(select_query).fetchall()
            for food in foods:
                for key, value in kwargs.items():
                    setattr(food[0], key, value)

            session.commit()


    def deleteFood(self, id):
        with Session(bind=self.conn.engine) as session:
            select_query = select(FoodModel).filter_by(id=id)
            foods = session.execute(select_query).fetchall()
            for food in foods:
                session.delete(food[0])

            session.commit()