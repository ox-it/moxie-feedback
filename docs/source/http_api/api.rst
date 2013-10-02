HTTP API
========

POST /feedback
--------------

You must pass a JSON document containing the following properties:

 * ``message`` (mandatory): the text message (feedback)
 * ``email`` (optional): an email address to eventually get an answer
 * ``referer`` (optional): referer

Example of request made with curl:
``curl -X POST -H "Content-Type: application/json" -d '{"message":"My great feedback",}' http://localhost:5000/feedback/``

Returns HTTP 200, or HTTP 429 (TOO MANY REQUESTS) if more than 5 requests are sent in less than 60 seconds for one IP address.
