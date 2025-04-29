from typing import List
from app import  db  
from app.models import Receipt, ReceiptItem, Stock
from app.repositories import ReceiptRepository
from app.dto import ReceiptDTO

class ReceiptService():
    
    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':
        ReceiptRepository.save(receipt)
        return receipt

    @staticmethod
    def find(id: int) -> 'Receipt':
        return ReceiptRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Receipt']:
        return ReceiptRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Receipt']:
        return ReceiptRepository.find_by(**kwargs)
    
    @staticmethod
    def register(receipt_dto: ReceiptDTO) -> 'ReceiptDTO':
        try:
            db.session.begin()
            if not receipt_dto.header:
                raise ValueError("ReceiptDTO.header must be a valid.")
            if not receipt_dto.Footer:
                raise ValueError("ReceiptDTO.Footer must be a valid.")
            
            
            from app.services import ReceiptTypeService, ArticleService, BatchService, StockService
            
            #TODO: Cambiar metodos find por un metodo que devuelva verdadero o falso si existe el objeto.
            ReceiptTypeService.find(receipt_dto.id_receipt_type)
           
            receipt = Receipt(
                id_header=receipt_dto.header.id,
                id_footer=receipt_dto.footer.id,
                id_receipt_type=receipt_dto.id_receipt_type
            )

            ReceiptRepository.save(receipt)

            for item_dto in receipt_dto.items:
            
                article = ArticleService.find(item_dto.id_article)
                batch = BatchService.find(item_dto.id_batch)
                receipt_item = ReceiptItem(
                    article=article,
                    quantity=item_dto.quantity,
                    batch=batch,
                    receipt=receipt
                )
                db.session.add(receipt_item)

                stock = Stock(
                    id_article=article.id,
                    quantity=item_dto.quantity,
                    id_batch=batch,
                    receipt=receipt
                )
                StockService.register(stock)

            db.session.commit()

            return receipt_dto

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error registering receipt: {str(e)}")


        #TODO: Buscar el tipo de comprobante por id
        #TODO: Buscar el articulo por id de items
        #TODO: Crear un objeto receipt a partir de receipt_dto
        #TODO: Guardar el objeto receipt en la base de datos
        #TODO: Actualizar el stock de los articulos
        #TODO: El guardar y el actualizar deben ser transaccional