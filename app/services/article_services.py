from typing import List
from app.models import Article
from app.repositories import ArticleRepositories
article_repositories = ArticleRepositories()


class ArticleService():
    
    def save(self, article: Article) -> 'Article':
        article_repositories.save(article)
        return article
    
    def delete(self, article: 'Article') -> None:
        article_repositories.delete(article)

    def find(self, id: int) -> 'Article':
        return article_repositories.find(id)
    
    def find_all(self) -> List['Article']:
        return article_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['Article']:
        return article_repositories.find_by(**kwargs)