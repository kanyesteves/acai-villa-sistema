from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class FoodBase(DeclarativeBase):
    pass

class FoodModel(FoodBase):
    __tablename__ = 'foods'

    id:             Mapped[int]  = mapped_column(primary_key=True)
    name:           Mapped[str]  = mapped_column(String(50))
    food_type:      Mapped[str]  = mapped_column(String(50))
    description:    Mapped[str]  = mapped_column(String(100))


    def __repr__(self):
        return f"FoodModel(f{self.id=}, {self.name=})"
