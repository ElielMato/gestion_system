from datetime import datetime, timezone
import unittest
import os
from app import create_app
from app import db
from app.models import Stock
from app.services import StockService
from utils import new_article, new_brand, new_category, new_batch
brand = new_brand(name='Marca', description='Una Marca')
category = new_category(name='Category', description='Una Categoria')
article = new_article(category=category, brand=brand, name='Tupu', description='description', minimun_stock=1, code_ean13='abc')
batch = new_batch(code="Batch001", expiration_date=datetime.now(timezone.utc))

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
        stock.id_article = article.id
        stock.id_batch = batch.id
        stock.quantity = 10

    def test_save(self):
        db.session.add(category)
        db.session.add(brand)
        db.session.add(article)
        db.session.add(batch)
        db.session.commit()

        stock = Stock(id_article=article.id, id_batch=batch.id, quantity=10)
        saved_stock = StockService.save(stock)

        self.assertIsNotNone(saved_stock.id)
        self.assertEqual(saved_stock.id_article, article.id)
        self.assertEqual(saved_stock.id_batch, batch.id)
        self.assertEqual(saved_stock.quantity, 10)
       
    
if __name__ == '__main__':
    unittest.main()
