from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.services import ArticleService, CategoryService, BrandService, BatchService
from utils import new_article, new_brand, new_category, new_batch, new_receipt, new_receipt_header, new_receipt_items, new_receipt_footer, new_receipt_type
brand = new_brand(id=1, name='Marca', description='Una Marca')
category = new_category(id=1, name='Category', description='Una Categoria')
batch = new_batch(id=1, code='001', expiration_date=datetime.now())
article = article = new_article(id=1, name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')

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
        header = new_receipt_header(id=1, submission_date=datetime.now())
        footer = new_receipt_footer(id=1, total=100)
        receipt_type = new_receipt_type(id=1, name='Entrada', description='Entrada a Almacén', entry=1)
        receipt = new_receipt(id=1, receipt_type_id=receipt_type.id, header_id=header.id, footer_id=footer.id)
        items = new_receipt_items(id=1, quantity=10, article_id=article.id, batch_id=batch.id, receipt_id=receipt.id)
        self.assertEqual(header.id, 1)
        self.assertEqual(footer.id, 1)
        self.assertEqual(receipt_type.id, 1)
        self.assertEqual(receipt.id, 1)
        self.assertEqual(items.article_id, article.id)

    def test_save(self):
        header = new_receipt_header(id=1, submission_date=datetime.now())
        footer = new_receipt_footer(id=1, total=100)
        receipt_type = new_receipt_type(id=1, name='Entrada', description='Entrada a Almacén', entry=1)
        receipt = new_receipt(id=1, receipt_type_id=receipt_type.id, header_id=header.id, footer_id=footer.id)
        items = new_receipt_items(id=1, quantity=10, article_id=article.id, batch_id=batch.id, receipt_id=receipt.id)

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