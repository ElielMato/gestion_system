import logging
from flask import Blueprint, request
from app.mapping import MessageMap, CategoryMap
from app.services import MessageBuilder, CategoryService
from app.validators import validate_with

category_bp = Blueprint('category', __name__)
category_map = CategoryMap()
category_service = CategoryService()

result = {}
status_code = 200

@category_bp.route('/category/<int:id>', methods=['GET'])
def get(id: int):
    """Get a category by ID."""
    logging.debug(f"Request to get category with ID: {id}")
    category = category_service.find(id)
    message_map, message_finish = message_create(category_map.dump(category, many=False), "Se encontro la categoria indicada")
    result = message_map.dump(message_finish)
    return result, status_code


@category_bp.route('/category', methods=['GET'])
def get_all():
    """Get all categorys."""
    logging.debug("Request to get all categorys")
    categorys = category_service.find_all()
    message_map, message_finish = message_create({'categorys': category_map.dump(categorys, many=True)}, "Se encontraron todas las categorias")
    result = message_map.dump(message_finish)
    return result, status_code

@category_bp.route('/category', methods=['POST'])
@validate_with(category_map)
def post():
    """Create a new category."""
    logging.debug("Request to create a new category")
    category = category_map.load(request.json)
    category_service.save(category)
    message_map, message_finish = message_create(category_map.dump(category), "Categoria creada con éxito")
    result = message_map.dump(message_finish)
    status_code = 201
    return result, status_code

@category_bp.route('/category/<int:id>', methods=['PUT'])
@validate_with(category_map)
def update(id: int):
    """Update a category by ID."""
    logging.debug(f"Request to update category with ID: {id}")
    category = category_service.find(id)
    if not category:
        message_map, message_finish = message_create({}, "Categoria no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        updated_data = request.json
        for key, value in updated_data.items():
            setattr(category, key, value)
        updated_category = category_service.save(category)
        message_map, message_finish = message_create(category_map.dump(updated_category), "Categoria actualizada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code

@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete(id: int):
    """Delete a category by ID."""
    logging.debug(f"Request to delete category with ID: {id}")
    category = category_service.find(id)
    if not category:
        message_map, message_finish = message_create({}, "Categoria no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        category_service.delete(category)
        message_map, message_finish = message_create({}, "Categoria eliminada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code


def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map, message_finish