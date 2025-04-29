import os
import unittest
from app import create_app
from app import db
from app.services import ArticleService
from utils import new_article, new_brand, new_category

class ArticleTestCase(unittest.TestCase):
    """
    Test Article model
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
        article = self.__create_article()
        self.assertIsNotNone(article)
        self.assertEqual(article.name, 'Tupu')
        self.assertEqual(article.description, 'description')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article = self.__create_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)

    def test_find(self):
        article = self.__create_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_find = ArticleService.find(article_save.id)
        self.check_data(article_find)

    def test_find_all(self):
        article = self.__create_article()
        article2 = self.__create_article2()
        article_save = ArticleService.save(article)
        ArticleService.save(article2)
        self.check_data(article_save)
        articles = ArticleService.find_all()
        self.assertIsNotNone(articles)
        self.assertEqual(len(articles), 2)

    def test_find_by(self):
        article = self.__create_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_find = ArticleService.find_by(description = 'description')
        self.assertIsNotNone(article_find)

    def test_update(self):
        article = self.__create_article()
        article_save = ArticleService.save(article)
        article_save.name = 'Tupu Update'
        article_save.description = 'description Update'
        article_update_save = ArticleService.save(article_save)
        self.assertEqual(article_update_save.name, 'Tupu Update')
        self.assertEqual(article_save.description, 'description Update')

    def test_delete(self):
        article = self.__create_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_delete = ArticleService.delete(article_save)
        self.assertIsNone(article_delete)
        
    def check_data(self, save):
        self.assertIsNotNone(save)
        self.assertIsNotNone(save.id)
        self.assertGreater(save.id, 0)

    def __create_article(self):
        brand = new_brand(name='Marca', description='Una Marca')
        category = new_category(name='Category', description='Una Categoria')
        article = new_article(category=category, brand=brand, name='Tupu', description='description', minimun_stock=1, code_ean13='abc')
        return article
    
    def __create_article2(self):
        brand = new_brand(name='Marca', description='Una Marca')
        category = new_category(name='Category', description='Una Categoria')
        article = new_article(category=category, brand=brand, name='Tupu2', description='description2', minimun_stock=2, code_ean13='abc')
        return article
                

if __name__ == '__main__':
    unittest.main()