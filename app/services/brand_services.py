
from typing import List
from app.models import Brand
from app.repositories import BrandRepositories
brand_repositories = BrandRepositories()

class BrandService():

    def save(brand:Brand) -> Brand:
        brand_repositories.save(brand)
        return brand
    
    def delete(brand:Brand) -> None:
        brand_repositories.delete(brand)

    def find(id: int) -> 'Brand':
        return brand_repositories.find(id)

    def find_all() -> List['Brand']:
        return brand_repositories.find_all()
    
    def find_by(**kwargs) -> List['Brand']:
        return brand_repositories.find_by(**kwargs)