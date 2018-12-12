import pika

parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo03')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# delete existing config
channel.queue_delete('email_notify')
channel.queue_delete('gen_thumbnails')
channel.queue_delete('update_file_system')
channel.exchange_delete('sys_activity')
# end delete

# declare the exchange
channel.exchange_declare('sys_activity', exchange_type='direct')

# declare the queues
channel.queue_declare('email_notify')
channel.queue_declare('gen_thumbnails')
channel.queue_declare('update_file_system')

# bind the queues to the exchange
# in effect, publishing a single message to the 'sys_activty' exchange with the routing_key 'file_upload' 
# will put a message in each queue email_notify/gen_thumbnails/update_file_system
channel.queue_bind(queue='email_notify', exchange='sys_activity', routing_key='file_upload')
channel.queue_bind(queue='gen_thumbnails', exchange='sys_activity', routing_key='file_upload')
channel.queue_bind(queue='update_file_system', exchange='sys_activity', routing_key='file_upload')

connection.close()