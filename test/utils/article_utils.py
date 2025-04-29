from app.models import Article, Category, Brand

def new_article(category: Category, brand: Brand, name: str, description: str, minimun_stock: float, code_ean13: str) -> Article:
    article = Article()
    article.category = category
    article.brand = brand
    article.name = name
    article.description = description
    article.minimun_stock = minimun_stock
    article.code_ean13 = code_ean13
    return article
