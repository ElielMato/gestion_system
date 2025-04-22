from app import db
from app.models import Category
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class CategoryRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):

    @staticmethod
    def save(category: Category) -> Category:
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def delete(category: Category) -> None:
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def find(category: int) -> Category:
        return Category.query.get(category)

    @staticmethod
    def find_all() -> list:
        return Category.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> Category:
        return Category.query.filter_by(**kwargs).first()