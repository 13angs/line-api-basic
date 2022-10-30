from flask import Flask, jsonify
from flask import request
import os, multiprocessing
from dotenv import load_dotenv
from signature import validate_signature
from get_user_data import GetUserData
from pub_sub_client import Publisher

load_dotenv('../.env')
CHANNEL_SECRET=os.environ['CHANNEL_SECRET']
CHANNEL_ID=os.environ['CHANNEL_ID']
RABBITMQ_HOST=os.environ['RABBITMQ_HOST']
EXCHANGE=os.environ['EXCHANGE']
ROUTING_KEY=os.environ['ROUTING_KEY']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def post():
    data = request.json
    str_data = request.data.decode('utf-8')
    x_line_sig = request.headers['x-line-signature']
    val_sig = validate_signature(CHANNEL_SECRET, str_data, x_line_sig)
    if val_sig:
        publisher = Publisher(RABBITMQ_HOST)
        publisher.run(EXCHANGE, ROUTING_KEY, data)
        return jsonify(data), 200
    return jsonify({
            "status_code" : 403,
            "errors": [
                {
                    "message": "Error validating signature",
                    "status_code": 403
                }
            ]
        }), 403

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    flask_proc = multiprocessing.Process(target=app.run, args=('0.0.0.0', 5000, True))
    flask_proc.start()

    gud = GetUserData(RABBITMQ_HOST, EXCHANGE, 'topic', 'get_user_data_queue', ROUTING_KEY, ACCESS_TOKEN)
    gud_proc = multiprocessing.Process(target=gud.run)
    gud_proc.start()