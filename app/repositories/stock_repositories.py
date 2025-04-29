from app import db
from app.models import Stock
from app.repositories import CreateAbstractRepository, ReadAbstractRepository

class StockRepository(CreateAbstractRepository, ReadAbstractRepository):

    @staticmethod
    def save(stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock

    @staticmethod
    def find(stock_id: int) -> Stock:
        return Stock.query.get(stock_id)

    @staticmethod
    def find_all() -> list:
        return Stock.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> Stock:
        return Stock.query.filter_by(**kwargs).first()