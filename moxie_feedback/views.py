from datetime import datetime

from flask import request, jsonify
from moxie.core.exceptions import BadRequest

from moxie.core.views import ServiceView, accepts
from moxie.core.representations import HAL_JSON, JSON


from .services import FeedbackService
from .domain import Message


class Feedback(ServiceView):

    methods = ['POST']

    def handle_request(self):
        service = FeedbackService.from_context()
        message_json = request.get_json(force=True, silent=True, cache=True)
        if not message_json:
            raise BadRequest("You must pass a JSON document")
        message = self.json_to_message(message_json)
        service.send_feedback(message)
        return True

    @accepts(JSON, HAL_JSON)
    def as_json(self, response):
        if response:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error'})

    def json_to_message(self, json):
        """JSON object to Message object (domain)
        :param json: JSON document
        :return: Message object
        """
        if 'message' not in json:
            raise BadRequest("You must provide a 'message' property")
        message = Message(json['message'], datetime.now())
        if 'email' in json:
            message.email = json['email']
        return message