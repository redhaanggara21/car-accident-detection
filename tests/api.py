# handlers/api.py
# Import the Flask Framework
from flask import Flask, jsonify

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/api/v1.0/ping', methods = ['GET'])
def ping():
    return jsonify({
        'ping': 'pong'
    })

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500