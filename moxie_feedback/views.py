from datetime import datetime

from flask import request

from moxie.core.views import ServiceView, accepts
from moxie.core.representations import HAL_JSON, JSON

from .services import FeedbackService
from .domain import Message


class Feedback(ServiceView):

    def handle_request(self):
        service = FeedbackService.from_context()
        pass

    @accepts(JSON, HAL_JSON)
    def as_json(self, response):
        pass