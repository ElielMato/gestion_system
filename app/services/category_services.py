from app.models import Category
from app.repositories import CategoryRepositories
category_repository = CategoryRepositories()

class CategoryService:

    def save(self, category: Category) -> Category:
        return self.repository.save(category)

    def find(self, category_id: int) -> Category:
        return self.repository.find(category_id)

    def find_all(self) -> list:
        return self.repository.find_all()

    def delete(self, category: Category) -> None:
        self.repository.delete(category)

    def find_by(self, **kwargs) -> Category:
        return self.repository.find_by(**kwargs)