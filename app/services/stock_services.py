from typing import List
from app.models import Stock
from app.repositories import StockRepositories
stock_repositories = StockRepositories()

class StockService:

    def save(stock: Stock) -> 'Stock':
        stock_repositories.save(stock)
        return stock
    
    def delete(stock: 'Stock') -> None:
        stock_repositories.delete(stock)

    def find(id: int) -> 'Stock':
        return stock_repositories.find(id)
    
    def find_all() -> List['Stock']:
        return stock_repositories.find_all()
    
    def find_by(**kwargs) -> List['Stock']:
        return stock_repositories.find_by(**kwargs)