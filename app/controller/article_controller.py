import logging
from flask import Blueprint, request
from app.services import ArticleService
from app.mapping import ArticleMap
from app.mapping import MessageMap
from app.services import MessageBuilder

article_bp = Blueprint('article', __name__)
article_map = ArticleMap()
article_service = ArticleService()

result = {}
status_code = 200

@article_bp.route('/article/<int:id>', methods=['GET'])
def get(id: int):
    """Get a article by ID."""
    logging.debug(f"Request to get article with ID: {id}")
    article = article_service.find(id)
    message_map, message_finish = message_create(article_map.dump(article, many=False), "Se encontro el articulo indicada")
    result = message_map.dump(message_finish)
    status_code = 200
    return result, status_code


@article_bp.route('/articles', methods=['GET'])
def get_all():
    """Get all articles."""
    logging.debug("Request to get all articles")
    articles = article_service.find_all()
    message_map, message_finish = message_create({'articles': article_map.dump(articles, many=True)}, "Se encontraron todas los articulos")
    result = message_map.dump(message_finish)
    status_code = 200
    return result, status_code

@article_bp.route('/articles', methods=['POST'])
def post():
    """Create a new article."""
    logging.debug("Request to create a new article")
    article = article_map.load(request.json)
    article_service.save(article)
    message_map, message_finish = message_create(article_map.dump(article), "Aticulo creada con éxito")
    result = message_map.dump(message_finish)
    status_code = 201
    return result, status_code


@article_bp.route('/articles/<int:id>', methods=['PUT'])
def update(id: int):
    """Update a article by ID."""
    logging.debug(f"Request to update article with ID: {id}")
    article = article_service.find(id)
    if not article:
        message_map, message_finish = message_create({}, "Articulo no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        updated_data = request.json
        for key, value in updated_data.items():
            setattr(article, key, value)
        updated_article = article_service.save(article)
        message_map, message_finish = message_create(article_map.dump(updated_article), "Articulo actualizada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code

@article_bp.route('/articles/<int:id>', methods=['DELETE'])
def delete(id:int):
    """Delete a article by ID."""
    logging.debug(f"Request to delete article with ID: {id}")
    article = article_service.find(id)
    if not article:
        message_map, message_finish = message_create({}, "Articulo no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        article_service.delete(article)
        message_map, message_finish = message_create({}, "Articulo eliminada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code

def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map, message_finish