__author__ = 'Monil'

from flask import Flask
from flask import jsonify
import time
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
start = time.time()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_description():
    return 'This is WallClock service for Startbucks simulation'


@app.route('/wallclock', methods=['GET'])
def get_wallclock_time():
    return jsonify({'time': round(time.time() - start, 2)}), 200


if __name__ == '__main__':
    app.run(port=10001)
