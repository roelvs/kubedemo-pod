
import logging
from flask import Flask, render_template


logging.info("starting the engines...")

# first open connection to database

application = Flask(__name__)


@application.route('/', methods=['GET'])
def welcome():
    """
    endpoint for check availability
    :return: http response 200/"data collector online"
    """
    logging.debug("default pagina opgevraagd...")
    return render_template('index.html')


if __name__ == '__main__':
    try:
        application.run(host='0.0.0.0', port=5000)
    except Exception as ex:
        logging.error("exception while running influx-api worker: " + str(ex))
