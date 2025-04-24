from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.models import Receipt, ReceiptFooter, ReceiptHeader, ReceiptItem
from app.services import ReceiptService
from utils import new_article, new_brand, new_category, new_batch
brand = new_brand(id=1, name='Marca', description='Una Marca')
category = new_category(id=1, name='Category', description='Una Categoria')
batch = new_batch(id=1, code='001', expiration_date=datetime.now())

class ReceiptTestCase(unittest.TestCase):
    """
    Receipt Mode
    Necesitamos aplicar principios como DRY( Don't repeat yourself) y KISS (Keep it Simple, Stupid).
    YAGNI (You aren't gonna need it) y SOLID (Single responsability principle).
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
    
    def test_brand(self):
        # header
        # self.assertIsNotNone(brand)
        # self.assertEqual(brand.name, "Marca")
        # self.assertEqual(brand.description, "Una Marca")

    # def test_save(self):
    #     brand = new_brand(id=1, name='Marca', description='Una Marca')
    #     brand_save = BrandService.save(brand)
    #     self.check_data(brand_save)
