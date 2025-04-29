from typing import List
from app.models import Stock
from app.repositories import StockRepository

class StockService:

    @staticmethod
    def save(stock: Stock) -> 'Stock':
        StockRepository.save(stock)
        return stock

    @staticmethod
    def find(id: int) -> 'Stock':
        return StockRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Stock']:
        return StockRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Stock']:
        return StockRepository.find_by(**kwargs)
    
    @staticmethod
    def register(stock: Stock) -> 'Stock':
        StockRepository.save(stock)
        return stock