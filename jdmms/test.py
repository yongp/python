#! /usr/bin/python
from suds.client import Client 

client = Client('http://mms.360buy.com/services/NewMessageServer?wsdl=NewMessageSender.wsdl')
print client

result =  client.service.getMobileCodeInfo(18688950910)
print result
print client.last_received()
