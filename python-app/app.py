import os
import logging
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def query_sentiment():
    try:
        req_json = request.get_json()

        if req_json is None:
            return jsonify(error='testing')

    except Exception as ex:
        app.log.error(type(ex))
        app.log.error(ex.args)
        app.log.error(ex)
        return jsonify(error=str(ex))

if __name__ == '__main__':
    LOG_FORMAT = "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    app.log = logging.getLogger(__name__)
    port = os.environ['FLASK_PORT']
    app.run(host='0.0.0.0', port=int(port), debug=False)
