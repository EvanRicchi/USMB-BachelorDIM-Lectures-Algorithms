# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : Script able to reade all the messages available into the queue 
# ’presentation’

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

def read():
    ##
    # Function able to read all messages avaible into the queue 'presentation'
    channel.queue_declare(queue='presentation')
    
    def callback(ch, method, properties, body):
        
        print(" [x] Received %r " % body)
        read_message = method.delivery_tag
        # Printing the number of read messages
        print("Number of read messages : %i" % read_message)
        
    channel.basic_consume(callback,
                          queue='presentation',
                          no_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()