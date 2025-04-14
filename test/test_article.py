import os
import unittest
from app import create_app
from app import db
from app.models import Article
from app.services import ArticleService
service = ArticleService()

class ArticleTestCase(unittest.TestCase):
    """
    Test Article Model
    We apply principle such as DRY, KISS, YAGNI and, SOLID
    """

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_article(self):
        article = self.__new_article()
        self.assertIsNotNone(article)
        self.assertEqual(article.name, 'Articulo 1')
        self.assertEqual(article.description, 'Descripcion 1')
        self.assertEqual(article.category, 'Categoria 1')
        self.assertEqual(article.brand, 'Marca 1')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article = self.__new_article()
        article_save = service.save(article)
        self.check_data(article_save)

    def test_find(self):
        article = self.__new_article()
        article_save = service.save(article)
        self.check_data(article_save)
        article_find = service.find(article_save.id)
        self.check_data(article_find)

    def test_find_all(self):
        article = self.__new_article()
        article2 = self.__new_article()
        article2.id = 2
        article_save = service.save(article)
        article2_save = service.save(article2)
        self.check_data(article_save)
        self.assertIsNotNone(article2_save)
        articles = service.find_all()
        self.assertIsNotNone(articles)
        self.assertGreater(len(articles), 1)

    def test_find_by(self):
        article = self.__new_article()
        article_save = service.save(article)
        self.check_data(article_save)
        article = service.find_by(description = 'Descripcion 1')
        self.assertIsNotNone(article)
        self.assertGreater(len(article), 0)

    def test_update(self):
        article = self.__new_article()
        article_save = service.save(article)
        article_save.description = 'Nueva Descripcion'
        article_save_update = service.save(article_save)
        self.assertEqual(article_save_update.description, 'Nueva Descripcion')
        self.assertEqual(article_save.description, article_save_update.description)
        self.assertEqual(article.description, article_save_update.description)

    def __new_article(self):
        article = Article()
        article.name = 'Articulo 1'
        article.description = 'Descripcion 1'
        article.category = 'Categoria 1'
        article.brand = 'Marca 1'
        article.minimun_stock = 1
        article.code_ean13 = 'abc'
        return article
    
    def check_data(self, article_save):
        self.assertIsNotNone(article_save)
        self.assertIsNotNone(article_save.id)
        self.assertGreater(article_save.id, 0)