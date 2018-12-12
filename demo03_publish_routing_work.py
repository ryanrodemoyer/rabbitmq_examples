import pika

parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo03')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# if enabled, you will get an error if publishing to a non-existent exchange or the cluster errored during receiving the message
channel.confirm_delivery()

props = pika.BasicProperties(content_type='text/plain', delivery_mode=1)
result = channel.basic_publish(exchange='sys_activity', routing_key='file_upload', body=b'message body value', properties=props)
if result:
    print('confirmed')
else:
    print('not confirmed')

connection.close()