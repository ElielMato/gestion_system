from app.models import Category

def new_category(id, name, description) -> Category:
    category = Category()
    category.id = id
    category.name = name
    category.description = description
    return category

