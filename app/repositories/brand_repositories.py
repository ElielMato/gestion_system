from typing import List
from app.models import Brand
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class BrandRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):

    @staticmethod
    def save(brand:Brand) -> Brand:
        db.session.add(brand)
        db.session.commit()
        return brand
    
    @staticmethod
    def delete(brand:Brand) -> None:
        db.session.delete(brand)
        db.session.commit()
    
    @staticmethod
    def find(id: int) -> 'Brand':
        return Brand.query.get(id)

    @staticmethod
    def find_all() -> List['Brand']:
        return Brand.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Brand']:
        return Brand.query.filter_by(**kwargs).all()
    