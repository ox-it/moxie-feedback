from moxie.core.service import Service


class FeedbackService(Service):

    def __init__(self, backends={}):
        self.backends = map(self._import_provider, backends.items())

    def send_feedback(self, message):
        for backend in self.backends:
            backend.feedback(message)