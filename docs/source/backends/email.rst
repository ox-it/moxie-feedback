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
 * ``send_to``: (mandatory) list of email address where the feedback should be send
 * ``email_subject``: (optionnal) subject of the email (defaults to "Feedback")

Dummy backend
-------------

Used for debug purpose, ``moxie_feedback.backends.dummy.DummyBackend`` prints the message on the console.

Example of configuration
------------------------

.. code-block:: yaml

    feedback:
        FeedbackService:
            backends:
              moxie_feedback.backends.dummy.DummyBackend: {}
              moxie_feedback.backends.mail.EmailBackend:
                smtp_server: 'smtp.server'
                sender_email: 'noreply@moxie.com'
                send_to: ['employee1@my.company.com', 'employee2@my.company.com']
