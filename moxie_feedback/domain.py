class Message(object):
    def __init__(self, text, user_agent, message_date, email=None, referer=None, device=None):
        """Message
        :param text: text of the message
        :param user_agent: User-Agent from the query
        :param message_date: date of the message
        :param email: email address of the sender
        :param referer: optional referer
        """
        self.text = text
        self.user_agent = user_agent
        self.message_date = message_date
        self.email = email
        self.referer = referer
        self.device = device

    text = None

    user_agent = None

    message_date = None

    email = None

    referer = None

    device = None