# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : Script able to connect to the queue named ’presentation’ and publish a 
# string message containing the user name. 

# Imports of libraries
import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://mywwnzeu:ADR6er2GN0RetPcGDP1X4P8N_GZQinGc@lark.rmq.cloudamqp.com/mywwnzeu'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()

def write():
    ##
    # Function able to publish a string message containing the user name in 
    # queue named 'presentation'

    channel.queue_declare(queue='presentation')
    
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Username : ricchie')
    print(" [x] Sent 'Username : ricchie'")
    connection.close()

write()