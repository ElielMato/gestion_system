
from typing import List
from app.models import Brand
from app.repositories import BrandRepositories
brand_repositories = BrandRepositories()

class BrandService():

    def save(self, brand:Brand) -> Brand:
        brand_repositories.save(brand)
        return brand
    
    def delete(self, brand:Brand) -> None:
        brand_repositories.delete(brand)

    def find(self, id: int) -> 'Brand':
        return brand_repositories.find(id)

    def find_all(self) -> List['Brand']:
        return brand_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['Brand']:
        return brand_repositories.find_by(**kwargs)