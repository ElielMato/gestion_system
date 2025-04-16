from typing import List
from app.models import Article
from app import db
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class ArticleRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):
    
    @staticmethod
    def save(article: Article) -> 'Article':
        db.session.add(article)
        db.session.commit()
        return article
    
    @staticmethod
    def delete(article: Article) -> None:
        db.session.delete(article)
        db.session.commit()

    @staticmethod
    def find(id: int) -> 'Article':
        return Article.query.get(id)
    
    @staticmethod
    def find_all() -> List[Article]:
        return Article.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List[Article]:
        return Article.query.filter_by(**kwargs).all()