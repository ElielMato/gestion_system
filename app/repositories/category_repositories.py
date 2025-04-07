from app import db
from app.models import Category
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class CategoryRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):
    def save(self, category: Category) -> Category:
        db.session.add(category)
        db.session.commit()
        return category

    def find(self, category_id: int) -> Category:
        return Category.query.get(category_id)

    def find_all(self) -> list:
        return Category.query.all()

    def delete(self, category: Category) -> None:
        db.session.delete(category)
        db.session.commit()

    def find_by(self, **kwargs) -> Category:
        return Category.query.filter_by(**kwargs).first()