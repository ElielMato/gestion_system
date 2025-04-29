from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.services import ArticleService, CategoryService, BrandService, BatchService
from utils import new_article, new_brand, new_category, new_batch, new_receipt, new_receipt_header, new_receipt_items, new_receipt_footer, new_receipt_type
brand = new_brand(name='Marca', description='Una Marca')
category = new_category(name='Category', description='Una Categoria')
batch = new_batch(code='001', expiration_date=datetime.now())
article = new_article(category=category, brand=brand, name='Tupu', description='description', minimun_stock=1, code_ean13='abc')

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
    
    def test_receipt(self):
        header = new_receipt_header(submission_date=datetime.now())
        footer = new_receipt_footer(total=100)
        receipt_type = new_receipt_type(name='Entrada', description='Entrada a Almacén', entry=1)
        receipt = new_receipt(id_header=header.id, id_footer=footer.id, receipt_type=receipt_type)
        items = new_receipt_items(quantity=10, id_article=article.id, id_batch=batch.id, id_receipt=receipt.id)
        self.assertEqual(header.id, 1)
        self.assertEqual(footer.id, 1)
        self.assertEqual(receipt_type.id, 1)
        self.assertEqual(receipt.id, 1)
        self.assertEqual(items.id_article, article.id)

    def test_save(self):
        header = new_receipt_header(submission_date=datetime.now())
        footer = new_receipt_footer(total=100)
        receipt_type = new_receipt_type(name='Entrada', description='Entrada a Almacén', entry=1)
        receipt = new_receipt(id_receipt_type=receipt_type.id, id_header=header.id, id_footer=footer.id)
        items = new_receipt_items(quantity=10, id_article=article.id, id_batch=batch.id, id_receipt=receipt.id)

        db.session.add(header)
        db.session.add(footer)
        db.session.add(receipt_type)
        db.session.commit()

        CategoryService.save(category)
        BrandService.save(brand)
        BatchService.save(batch)
        ArticleService.save(article)

        db.session.add(receipt)
        db.session.add(items)
        db.session.commit()