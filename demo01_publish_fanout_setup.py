import pika

parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo01')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
# channel.confirm_delivery()

# # delete existing config
channel.queue_delete('fanout01')
channel.queue_delete('fanout02')
channel.queue_delete('fanout03')
channel.exchange_delete('myfanout')
# # end delete

# declare the exchange
channel.exchange_declare('myfanout', exchange_type='fanout')

# declare the queues
channel.queue_declare('fanout01')
channel.queue_declare('fanout02')
channel.queue_declare('fanout03')

# bind the queues to the exchange
# in effect, publishing a single message to the 'myfanout' exchange will put a message in each queue fanout01/fanout02/fanout03
channel.queue_bind(queue='fanout01', exchange='myfanout')
channel.queue_bind(queue='fanout02', exchange='myfanout')
channel.queue_bind(queue='fanout03', exchange='myfanout')

connection.close()