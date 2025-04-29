from app.models import Brand

def new_brand(name: str, description: str) -> Brand:
    brand = Brand()
    brand.name = name
    brand.description = description
    return brand
