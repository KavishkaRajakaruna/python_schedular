import pika



class queue_broker():
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()

    def send_message(self, queue, message):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)
        print(" [x] Sent %r" % message)