import pika
import sys

def exchange_does_not_exist(props, channel):
    try:
        result = channel.basic_publish(exchange='does_not_exist', routing_key='file_upload', body=b'message body value', properties=props)
        if result:
            print('confirmed')
        else:
            print('not confirmed')
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        
        print(e)
        print(v)

def exchange_with_no_bindings(props, channel):
    try:
        channel.exchange_declare('work.exchange')
        result = channel.basic_publish(exchange='work.exchange', routing_key='file_upload', body=b'message body value', properties=props)
        if result:
            print('confirmed')
        else:
            print('not confirmed')
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        
        print(e)
        print(v)

def exchange_with_queue_and_binding(props, channel: pika.BlockingConnection):
    try:
        channel.exchange_declare('work.exchange')
        channel.queue_declare('add.to.newsletter')
        channel.queue_bind(exchange='work.exchange', queue='add.to.newsletter', routing_key='new_user_registration')

        result = channel.basic_publish(exchange='work.exchange', routing_key='new_user_registration', body=b'message body value', properties=props)
        if result:
            print('confirmed')
        else:
            print('not confirmed')
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        
        print(e)
        print(v)

def exchange_with_queue_and_invalid_binding(props, channel: pika.BlockingConnection):
    try:
        channel.exchange_declare('work.exchange')
        channel.queue_declare('add.to.newsletter')
        channel.queue_bind(exchange='work.exchange', queue='add.to.newsletter', routing_key='new_user_registration')

        result = channel.basic_publish(exchange='work.exchange', routing_key='i_am_invalid', body=b'message body value', properties=props)
        if result:
            print('confirmed')
        else:
            print('not confirmed')
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        
        print(e)
        print(v)


if __name__ == '__main__':
    parameters = pika.URLParameters('amqp://DemoMqUser:DemoMqUser@localhost:5672/demo04')

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    # if enabled, you will get an error if publishing to a non-existent exchange or the cluster errored during receiving the message
    channel.confirm_delivery()

    props = pika.BasicProperties(content_type='text/plain', delivery_mode=1)

    exchange_with_queue_and_binding(props, channel)

    connection.close()