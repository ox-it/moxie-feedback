HTTP API
========

POST /feedback
--------------

You must pass a JSON document containing the following properties:

 * ``message`` (mandatory): the text message (feedback)
 * ``email`` (optional): an email address to eventually get an answer
 * ``referer`` (optional): referer
 * ``device`` (optional): information on the device sending feedback

Example of request made with curl:
``curl -X POST -H "Content-Type: application/json" -d '{"message":"My great feedback",}' http://localhost:5000/feedback/``
