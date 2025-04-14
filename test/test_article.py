import os
import unittest
from app import create_app
from app import db
from app.models import Article
from app.services import ArticleService
service = ArticleService()

class ArticleTestCase(unittest.TestCase):
    """
    Test Article model
    Aplicamos principios como DRY, KISS, YAGNI y SOLID.
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
        self.assertEqual(article.name, 'Tupu')
        self.assertEqual(article.description, 'description')
        self.assertEqual(article.category, 'coso')
        self.assertEqual(article.brand, 'cosito')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article = self.__new_article()
        article_save = service.save(article)
        self.check_data(article_save)
        article_delete = service.delete(article)
        self.assertIsNone(article_delete)

    def test_find(self):
        article = self.__new_article()
        article_save = service.save(article)
        self.check_data(article_save)
        article = service.find(1)
        self.check_data(article_save)

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
        article = service.find_by(description = 'description')
        self.assertIsNotNone(article)
        self.assertGreater(len(article), 0)

    def test_update(self):
        article = self.__new_article()
        article_save = service.save(article)
        article_save.description = 'new description'
        article_save_update = service.save(article_save)
        self.assertEqual(article_save_update.description, 'new description')
        self.assertEqual(article_save.description, article_save_update.description)
        self.assertEqual(article.description, article_save_update.description)

    def __new_article(self):
        article = Article()
        article.name = 'Tupu'
        article.description = 'description'
        article.category = 'coso'
        article.brand = 'cosito'
        article.minimun_stock = 1
        article.code_ean13 = 'abc'
        return article
    
    def check_data(self, article_save):
        self.assertIsNotNone(article_save)
        self.assertIsNotNone(article_save.id)
        self.assertGreater(article_save.id, 0)


if __name__ == '__main__':
    unittest.main()