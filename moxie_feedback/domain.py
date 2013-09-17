class Message(object):
    def __init__(self, text, message_date, email=None):
        """Event
        :param uid: unique identifier of the event
        """
        self.text = text
        self.message_date = message_date
        self.email = email

    text = None

    message_date = None

    email = None
