from typing import List
from app.models import Category
from app.repositories import CategoryRepositories
category_repositories = CategoryRepositories()

class CategoryService:

    def save(self, category: Category) -> 'Category':
        category_repositories.save(category)
        return category
    
    def delete(self, category: 'Category') -> None:
        category_repositories.delete(category)

    def find(self, id: int) -> 'Category':
        return category_repositories.find(id)
    
    def find_all(self) -> List['Category']:
        return category_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['Category']:
        return category_repositories.find_by(**kwargs)