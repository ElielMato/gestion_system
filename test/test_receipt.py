# from datetime import datetime
# import os
# import unittest
# from app import create_app
# from app import db
# from app.models import Receipt, ReceiptFooter, ReceiptHeader, ReceiptItem
# from app.services import ReceiptService
# from utils import new_article, new_brand, new_category, new_batch
# brand = new_brand(id=1, name='Marca', description='Una Marca')
# category = new_category(id=1, name='Category', description='Una Categoria')
# batch = new_batch(id=1, code='001', expiration_date=datetime.now())

# class ReceiptTestCase(unittest.TestCase):
#     """
#     Receipt Mode
#     Necesitamos aplicar principios como DRY( Don't repeat yourself) y KISS (Keep it Simple, Stupid).
#     YAGNI (You aren't gonna need it) y SOLID (Single responsability principle).
#     """

#     def setUp(self):
#         os.environ['FLASK_CONTEXT'] = 'testing'
#         self.app = create_app()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()

#     def test_receipt_save(self):
#         receipt = Receipt()
#         header = self.__get_header()
#         items = self.__get_items()
#         footer = self.__get_footer()
#         receipt.header = header
#         receipt.items = items
#         receipt.footer = footer
#         db.session.add(header)
#         db.session.add(items)
#         db.session.add(footer)
#         db.session.add(receipt)
#         db.session.commit()
        
#     def __get_header(self) -> ReceiptHeader:
#         header = ReceiptHeader() 
#         header.id = 1
#         header.submission_date = datetime.now()
#         return header

#     def __get_items(self) -> list[ReceiptItem]:
#         article1 = new_article(id=1, name='Articulo 1', description='Un Articulo', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
#         article2 = new_article(id=2, name='Articulo 2', description='Otro Articulo', category=category.id, brand=brand.id, minimun_stock=2, code_ean13='def')
#         article3 = new_article(id=3, name='Articulo 3', description='Tercer Articulo', category=category.id, brand=brand.id, minimun_stock=3, code_ean13='ghi')
#         items = []
#         items.append(ReceiptItem(article_id=article1.id, quantity=2.0, batch_id=batch.id)) 
#         items.append(ReceiptItem(article_id=article2.id, quantity=3.0, batch_id=batch.id))
#         items.append(ReceiptItem(article_id=article3.id, quantity=4.0, batch_id=batch.id))
#         return items
    
#     def __get_footer(self) -> ReceiptFooter:
#         footer = ReceiptFooter()
#         footer.id = 1
#         footer.total = 100.0
#         return footer
    