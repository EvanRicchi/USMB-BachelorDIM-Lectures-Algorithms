# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : Script for the rpc client


# Imports of libraries
import pika
import uuid
import os
import msgpack 
import msgpack_numpy as m 
import numpy as np #if Numpy is required. 

#class for the rpc client
class RpcClient(object):
    def __init__(self):
        # Configure a connexion to a remote RabbitMQ instance
        amqp_url='amqp://mywwnzeu:ADR6er2GN0RetPcGDP1X4P8N_GZQinGc@lark.rmq.cloudamqp.com/mywwnzeu'
        url = os.environ.get('CLOUDAMQP_URL',amqp_url)
        params = pika.URLParameters(url)
        params.socket_timeout = 5
        self.connection = pika.BlockingConnection(params)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
                    
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

rpc = RpcClient()

print(" [x] Requesting message")
response = rpc.call('Hi, how ﬁne ?')
print(" [.] Got %r" % response)