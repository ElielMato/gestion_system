import os
import unittest
from app import create_app
from app import db
from app.services import ArticleService
from utils import new_article, new_brand, new_category
brand = new_brand(id=1, name='Marca', description='Una Marca')
category = new_category(id=1, name='Category', description='Una Categoria')

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
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        self.assertIsNotNone(article)
        self.assertEqual(article.name, 'Tupu')
        self.assertEqual(article.description, 'description')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        self.check_data(article_save)

    def test_find(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_find = ArticleService.find(article_save.id)
        self.check_data(article_find)

    def test_find_all(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article2 = new_article(id=2, name='Tupu2', description='description2', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        ArticleService.save(article2)
        self.check_data(article_save)
        articles = ArticleService.find_all()
        self.assertIsNotNone(articles)
        self.assertEqual(len(articles), 2)

    def test_find_by(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_find = ArticleService.find_by(description = 'description')
        self.assertIsNotNone(article_find)

    def test_update(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        article_save.name = 'Tupu Update'
        article_save.description = 'description Update'
        article_update_save = ArticleService.save(article_save)
        self.assertEqual(article_update_save.name, 'Tupu Update')
        self.assertEqual(article_save.description, 'description Update')

    def test_delete(self):
        article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_delete = ArticleService.delete(article_save)
        self.assertIsNone(article_delete)
        
    def check_data(self, save):
        self.assertIsNotNone(save)
        self.assertIsNotNone(save.id)
        self.assertGreater(save.id, 0)

if __name__ == '__main__':
    unittest.main()