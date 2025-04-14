from typing import List
from app.models import Article
from app import db


class ArticleRepositories():
    
    def save(self, article: Article) -> 'Article':
        db.session.add(article)
        db.session.commit()
        return article
    
    def delete(self, article: Article) -> None:
        db.session.delete(article)
        db.session.commit()

    def find(self, id: int) -> 'Article':
        return Article.query.get(id)
    
    def find_all(self) -> List[Article]:
        return Article.query.all()
    
    def find_by(self, **kwargs) -> List[Article]:
        return Article.query.filter_by(**kwargs).all()