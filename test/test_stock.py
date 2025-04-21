# import unittest
# from flask import current_app
# from app import create_app
# import os
# from app import db
# from app.models import Stock
# from app.services import StockService

# class StockTestCase(unittest.TestCase):
#     """
#     Test Stock Model
#     We apply principle such as DRY, KISS, YAGNI and, SOLID
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
    
#     def test_stock(self):
#         stock = self.__new_stock()
#         self.assertIsNotNone(stock)
#         self.assertEqual(stock.article_id, 1)
#         self.assertEqual(stock.quantity, 10.0)
#         self.assertEqual(stock.batch_id, 1)
#         self.assertEqual(stock.entry, 1)
#         self.assertEqual(stock.receipt_number, 12345)
        

#     def __new_stock(self):
#         stock = Stock()
#         stock.article_id=1,
#         stock.quantity=10.0,
#         stock.batch_id=1,
#         stock.entry=1,
#         stock.receipt_number=12345

#         return stock
    
#     def check_data(self, save):
#         self.assertIsNotNone(save)
#         self.assertIsNotNone(save.id)
#         self.assertGreater(save.id, 0)