from app.models import Brand

def new_brand(id, name, description):
    brand = Brand()
    brand.id = id
    brand.name = name
    brand.description = description
    return brand
