import smtplib
from email.mime.text import MIMEText


class EmailBackend(object):

    def __init__(self, smtp_server, sender_email, send_to, email_subject='Feedback'):
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.send_to = send_to
        self.email_subject = email_subject

    def feedback(self, message):
        msg = MIMEText(message.text)

        msg['Subject'] = self.email_subject
        msg['From'] = self.sender_email
        msg['To'] = self.send_to

        s = smtplib.SMTP(self.smtp_server)
        s.sendmail(self.sender_email, [self.send_to], msg.as_string())
        s.quit()