Backends
========

The ``FeedbackService`` takes a list of ``backends`` where the feedback message should be send to.

Email backend
-------------

To add the email backend, include ``moxie_feedback.backends.mail.EmailBackend`` in the list of ``backends``
of the ``FeedbackService``.

The following parameters should be defined in the configuration:

 * ``smtp_server``: (mandatory) domain of the SMTP server
 * ``sender_email``: (mandatory) email address of the sender
 * ``send_to``: (mandatory) email address where the feedback should be send
 * ``email_subject``: (optionnal) subject of the email (defaults to "Feedback")
