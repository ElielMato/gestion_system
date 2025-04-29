
from typing import List
from app.models import Brand
from app.repositories import BrandRepository

class BrandService():

    @staticmethod
    def save(brand:Brand) -> Brand:
        BrandRepository.save(brand)
        return brand
    
    @staticmethod
    def delete(brand:Brand) -> None:
        BrandRepository.delete(brand)

    @staticmethod
    def find(id: int) -> 'Brand':
        return BrandRepository.find(id)

    @staticmethod
    def find_all() -> List['Brand']:
        return BrandRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Brand']:
        return BrandRepository.find_by(**kwargs)