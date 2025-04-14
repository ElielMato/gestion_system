from app import db
from dataclasses import dataclass

@dataclass(init=True, eq=False)
class Category(db.Model):
    """
    Model Category with is attribute
    """
    __tablename__ = "categories"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column("name", db.String(100), nullable=False)
    description: str = db.Column("description", db.String(250), nullable=False)
    
    def __eq__(self, category: object) -> bool:
        return (self.id == category.id)