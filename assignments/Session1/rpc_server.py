# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : Script for the rpc server


# Imports of libraries
import pika
import os
import msgpack 
import msgpack_numpy as m 
import numpy as np #if Numpy is required. 

# Configure a connexion to a remote RabbitMQ instance
amqp_url='amqp://mywwnzeu:ADR6er2GN0RetPcGDP1X4P8N_GZQinGc@lark.rmq.cloudamqp.com/mywwnzeu'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def on_request(ch, method, props, body):
   

    print(" [.] Client %r" % body)
    response = "Fine and you ?"

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()