import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.models import Category
from app.services import CategoryService
service = CategoryService()

class CategoryTestCase(unittest.TestCase):
    """
    Test Category model
    Aplicamos principios como DRY, KISS, YAGNI y SOLID.
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
        category = self.__new_category()
        self.assertIsNotNone(category)
        self.assertEqual(category.name, "Categoría")
        self.assertEqual(category.description, "Una Categoría")

    def test_save(self):
        category = self.__new_category()
        category_save = service.save(category)
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertGreater(category_save.id, 0)
        
    def test_find(self):
        category = self.__new_category()
        category_save = service.save(category)
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertEqual(category_save.id, 1)
        category_find = service.find(category_save.id)
        self.assertIsNotNone(category_find)

    def test_find_all(self):
        category = self.__new_category()
        category1 = self.__new_category()
        category1.name = "Categoría 1"
        category1.description = "Una Categoría 1"
        category_save = service.save(category)
        service.save(category1)
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertEqual(category_save.id, 1)
        categories = service.find_all()
        self.assertIsNotNone(categories)
        self.assertEqual(len(categories), 2)

    def test_find_by_id(self):
        category = self.__new_category()
        category_save = service.save(category)
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertGreater(category_save.id, 0)
        category_find_by = service.find_by(id=1)
        self.assertIsNotNone(category_find_by)

    def test_update(self):
        category = self.__new_category()
        category_save = service.save(category)
        category_save.name = "Categoría Actualizada"
        category_update_save = service.save(category_save)
        self.assertEqual(category_update_save.name, "Categoría Actualizada")
        self.assertEqual(category_save.name, category_update_save.name)
        self.assertEqual(category.name, category_update_save.name)
        
    def test_delete(self):
        category = self.__new_category()
        category_save = service.save(category)
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertGreater(category_save.id, 0)
        category_delete = service.delete(category_save)
        self.assertIsNone(category_delete)

    def __new_category(self):
        category = Category()
        category.name = "Categoría"
        category.description = "Una Categoría"
        return category