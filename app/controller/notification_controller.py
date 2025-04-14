import logging
from flask import Blueprint, request
from app.mapping import MessageMap, NotificationMap
from app.services import MessageBuilder, NotificationService

notification_bp = Blueprint('notification', __name__)
notification_map = NotificationMap()
notification_service = NotificationService()

result = {}
status_code = 200

@notification_bp.route('/notification/<int:id>', methods=['GET'])
def get(id: int):
    """Get a notification by ID."""
    logging.debug(f"Request to get notification with ID: {id}")
    notification = notification_service.find(id)
    message_map, message_finish = message_create(notification_map.dump(notification, many=False), "Se encontro la notificacion indicada")
    result = message_map.dump(message_finish)
    return result, status_code

@notification_bp.route('/notification', methods=['GET'])
def get_all():
    """Get all notifications."""
    logging.debug("Request to get all notifications")
    notifications = notification_service.find_all()
    message_map, message_finish = message_create({'notifications': notification_map.dump(notifications, many=True)}, "Se encontraron todas las notificaciones")
    result = message_map.dump(message_finish)
    return result, status_code


@notification_bp.route('/notification', methods=['POST'])
def post():
    """Create a new notification."""
    logging.debug("Request to create a new notification")
    notification = notification_map.load(request.json)
    notification_service.save(notification)
    message_map, message_finish = message_create(notification_map.dump(notification), "Notificacion creada correctamente")
    result = message_map.dump(message_finish)
    return result, 201

@notification_bp.route('/notification/<int:id>', methods=['PUT'])
def update(id: int):
    """Update a notification by ID."""
    logging.debug(f"Request to update notification with ID: {id}")
    notification = notification_service.find(id)
    if not notification:
        message_map, message_finish = message_create({}, "Notificacion no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        updated_data = request.json
        for key, value in updated_data.items():
            setattr(notification, key, value)
        updated_notification = notification_service.save(notification)
        message_map, message_finish = message_create(notification_map.dump(updated_notification, many=False), "Notificacion actualizada correctamente")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code
    
@notification_bp.route('/notification/<int:id>', methods=['DELETE'])
def delete(id: int):
    """Delete a notification by ID."""
    logging.debug(f"Request to delete notification with ID: {id}")
    notification = notification_service.find(id)
    if not notification:
        message_map, message_finish = message_create({}, "Notificacion no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        notification_service.delete(notification)
        message_map, message_finish = message_create({}, "Notificacion eliminada correctamente")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code


def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map, message_finish