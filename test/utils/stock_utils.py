from app.models import Stock, Article, Batch, Receipt

def new_stock(article: Article, quantity: float, batch: Batch, receipt: Receipt) -> Stock:
    stock = Stock()
    stock.article = article
    stock.quantity = quantity
    stock.batch = batch
    stock.receipt = receipt
    return stock