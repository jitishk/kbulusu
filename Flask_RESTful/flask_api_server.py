"""
File: chapter03/flask_api_server.py

A HTTP RESTFul API server to control an LED built using Flask-RESTful.

Dependencies:
  pip3 install gpiozero pigpio flask-restful

Built and tested with Python 3.7 on Raspberry Pi 4 Model B
"""
import logging
from flask import Flask, request, render_template                                    # (1)
from flask_restful import Resource, Api, reqparse, inputs                            # (2)

# Initialize Logging
logging.basicConfig(level=logging.WARNING)  # Global logging configuration
logger = logging.getLogger('main')  # Logger for this module
logger.setLevel(logging.INFO) # Debugging for this file.


# Flask & Flask-RESTful instance variables
app = Flask(__name__) # Core Flask app.                                              # (4)
api = Api(app) # Flask-RESTful extension wrapper                                     # (5)

"""
Flask & Flask-Restful Related Functions
"""

# @app.route applies to the core Flask instance (app).
# Here we are serving a simple web page.
@app.route('/', methods=['GET'])                                                     # (8)
def index():
    """Make sure inde.html is in the templates folder
    relative to this Python file."""
    return render_template('index_api_client.html') #, pin=LED_GPIO_PIN)                # (9)

if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", debug=True)                                              # (20)
