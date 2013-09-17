import smtplib
import logging
from smtplib import SMTPException
from email.mime.text import MIMEText

logger = logging.getLogger(__file__)


class EmailBackend(object):

    def __init__(self, smtp_server, sender_email, send_to, email_subject='Feedback'):
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.send_to = send_to
        self.email_subject = email_subject

    def feedback(self, message):
        msg = self._get_email(message)

        try:
            s = smtplib.SMTP(self.smtp_server)
            s.sendmail(self.sender_email, [self.send_to], msg.as_string())
            s.quit()
        except:
            logger.error("Error when sending email", exc_info=True)
            return False
        else:
            return True

    def _get_email(self, message):
        msg_text = self._get_email_text(message)
        msg = MIMEText(msg_text)

        msg['Subject'] = self.email_subject
        msg['From'] = self.sender_email
        msg['To'] = self.send_to
        return msg

    def _get_email_text(self, message):
        """
        Prepare the text of the email message
        :param message: Message domain object
        :return: string with message
        """
        return """Date:        {date}
E-mail:      {email}
User-agent:  {ua}
Referer:     {referer}

{text}
        """.format(text=message.text, date=str(message.message_date),
                   email=message.email, ua=message.user_agent,
                   referer=message.referer)