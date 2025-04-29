from dataclasses import dataclass
from app.models import Brand, Category
from app import db

@dataclass(init=True, eq=True)
class Article(db.Model):
    """
    Model Article with is attribute
    """
    __tablename__ = 'articles'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_category: str = db.Column('id_category', db.Integer, db.ForeignKey('categories.id'), nullable=False)
    id_brand: str = db.Column('id_brand', db.Integer, db.ForeignKey('brands.id'), nullable=False)
    name: str = db.Column('name', db.String[100], nullable=False)
    description: str = db.Column('description', db.String[150], nullable=False)
    minimun_stock: float = db.Column('minimun_stock', db.Float, nullable=False)
    code_ean13: str = db.Column('code_ean13', db.String[150], nullable=False)

    brand = db.relationship('Brand', lazy=True)
    category = db.relationship('Category', lazy=True)