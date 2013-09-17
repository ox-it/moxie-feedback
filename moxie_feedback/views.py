from datetime import datetime

from flask import request, jsonify
from moxie.core.exceptions import BadRequest

from moxie.core.views import ServiceView, accepts
from moxie.core.representations import HAL_JSON, JSON


from .services import FeedbackService
from .domain import Message


class Feedback(ServiceView):

    methods = ['OPTIONS', 'POST']
    cors_allow_headers = ['Content-Type']

    def handle_request(self):
        service = FeedbackService.from_context()
        message_json = request.get_json(force=True, silent=True, cache=True)
        user_agent = request.headers.get('User-Agent', '')
        if not message_json:
            raise BadRequest("You must pass a JSON document")
        message = self.json_to_message(message_json, user_agent)
        return service.send_feedback(message)

    @accepts(JSON, HAL_JSON)
    def as_json(self, response):
        if response:
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'error'}), 500

    def json_to_message(self, json, ua):
        """JSON object to Message object (domain)
        :param json: JSON document
        :param ua: User-Agent from the request
        :return: Message object
        """
        if 'message' not in json:
            raise BadRequest("You must provide a 'message' property")
        message = Message(json['message'], ua, datetime.now())
        if 'email' in json:
            message.email = json['email']
        if 'referer' in json:
            message.referer = json['referer']
        if 'device' in json:
            message.device = json['device']
        return message