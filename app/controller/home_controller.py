from http import client
from flask import Blueprint, jsonify
from app.mapping import MessageMap
from app.services import MessageBuilder, Message

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def get():
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message("Hello World").add_message(", OK").add_code("Green").build()
    return message_map.dump(message_finish), 200