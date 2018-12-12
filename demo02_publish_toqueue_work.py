import pika

parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo02')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# if enabled, you will get an error if publishing to a non-existent exchange or the cluster errored during receiving the message
channel.confirm_delivery()

props = pika.BasicProperties(content_type='text/plain', delivery_mode=1)

result01 = channel.basic_publish(exchange='sys_activity', routing_key='email_notify', body=b'message to email_notify', properties=props)
if result01:
    print('email_notify delivered')
else:
    print('email_notify error')

result02 = channel.basic_publish(exchange='sys_activity', routing_key='gen_thumbnails', body=b'message to gen_thumbnails', properties=props)
if result02:
    print('gen_thumbnails delivered')
else:
    print('gen_thumbnails error')

result03 = channel.basic_publish(exchange='sys_activity', routing_key='update_file_system', body=b'message to update_file_system', properties=props)
if result03:
    print('update_file_system delivered')
else:
    print('update_file_system error')

connection.close()