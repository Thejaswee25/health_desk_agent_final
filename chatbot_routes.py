from flask import Blueprint, request, jsonify
from ai.chatbot import get_chatbot_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get('message','')
    reply = get_chatbot_response(msg)
    return jsonify({'reply': reply})
