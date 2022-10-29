import json
from pub_sub_client import Subscriber

class GetUserData(Subscriber):
    def __init__(self, host, exchange, exchange_type, queue_name, routing_key):
        Subscriber.__init__(self, host)
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.host = host

    def on_message_callback(self, ch, method, properties, body) -> None:
        message = json.loads(body)
        print(f'message received: {message}')


        # assign/update value
        # publish the message


    def run(self):
        super().setup(exchange=self.exchange, exchange_type=self.exchange_type,
                        queue_name=self.queue_name, routing_key=self.routing_key)
        print('Waiting for message. To exit press Ctrl+C')
        self.channel.start_consuming()