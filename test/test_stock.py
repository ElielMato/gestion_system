from datetime import datetime, timezone
import unittest
import os
from app import create_app
from app import db
from app.models import Stock
from app.services import StockService
from utils import new_article, new_brand, new_category, new_batch
brand = new_brand(id=1, name='Marca', description='Una Marca')
category = new_category(id=1, name='Category', description='Una Categoria')
article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
batch = new_batch(id=1, code="Batch001", expiration_date=datetime.now(timezone.utc))

class TestStock(unittest.TestCase):
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

    def test_stock_creation(self):
        stock = Stock()
        stock.article_id = article.id
        stock.batch_id = batch.id
        stock.quantity = 10

    def test_save(self):
        db.session.add(category)
        db.session.add(brand)
        db.session.add(article)
        db.session.add(batch)
        db.session.commit()

        stock = Stock(article_id=article.id, batch_id=batch.id, quantity=10)
        saved_stock = StockService.save(stock)

        self.assertIsNotNone(saved_stock.id)
        self.assertEqual(saved_stock.article_id, article.id)
        self.assertEqual(saved_stock.batch_id, batch.id)
        self.assertEqual(saved_stock.quantity, 10)
       
    
if __name__ == '__main__':
    unittest.main()
