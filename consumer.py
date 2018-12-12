import pika
import json

# @typechecked
def on_message(channel, mframe: pika.spec.Basic.Deliver , hframe, body):
    print(f'delivery_tag={mframe.delivery_tag}')
    print(f'routing_key={mframe.routing_key}')
    print(f'exchange={mframe.exchange}')
    print(body)
    print
    channel.basic_ack(delivery_tag=mframe.delivery_tag)

parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo01')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume(consumer_callback=on_message, queue='fanout01')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()