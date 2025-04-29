from typing import List
from app.models import Category
from app.repositories import CategoryRepository

class CategoryService:

    @staticmethod
    def save(category: Category) -> 'Category':
        CategoryRepository.save(category)
        return category
    
    @staticmethod
    def delete(category: 'Category') -> None:
        CategoryRepository.delete(category)

    @staticmethod
    def find(id: int) -> 'Category':
        return CategoryRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Category']:
        return CategoryRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Category']:
        return CategoryRepository.find_by(**kwargs)