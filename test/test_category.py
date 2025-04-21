import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.services import CategoryService
from utils import new_category
category = new_category(id=1, name='Categoría', description='Una Categoría')

class CategoryTestCase(unittest.TestCase):
    """
    Test Category Model
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
    
    def test_category(self):
        self.assertIsNotNone(category)
        self.assertEqual(category.name, "Categoría")
        self.assertEqual(category.description, "Una Categoría")

    def test_save(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        
    def test_find(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_find = CategoryService.find(category_save.id)
        self.assertIsNotNone(category_find)

    def test_find_all(self):
        category1 = new_category(id=2, name='Categoría 1', description='Una Categoría 1')
        category_save = CategoryService.save(category)
        CategoryService.save(category1)
        self.check_data(category_save)
        categories = CategoryService.find_all()
        self.assertIsNotNone(categories)
        self.assertEqual(len(categories), 2)

    def test_find_by_id(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_find_by = CategoryService.find_by(id=1)
        self.assertIsNotNone(category_find_by)

    def test_update(self):
        category_save = CategoryService.save(category)
        category_save.name = "Categoría Actualizada"
        category_update_save = CategoryService.save(category_save)
        self.assertEqual(category_update_save.name, "Categoría Actualizada")
        self.assertEqual(category_save.name, category_update_save.name)
        self.assertEqual(category.name, category_update_save.name)
        
    def test_delete(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_delete = CategoryService.delete(category_save)
        self.assertIsNone(category_delete)
    
    def check_data(self, save):
        self.assertIsNotNone(save)
        self.assertIsNotNone(save.id)
        self.assertGreater(save.id, 0)