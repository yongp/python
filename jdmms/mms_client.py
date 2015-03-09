#!/usr/bin/python

from suds.client import Client
#client = Client('http://localhost:7789/?wsdl')
#client = Client('http://mms.360buy.com/services/NewMessageServer')
client = Client('http://mms.360buy.com/services/NewMessageServer?wsdl=NewMessageSender.wsdl')

mobileNum = '18688950910' 
msgContent = 'hello world'
senderNum = 'Tms.Tms.ZiTi'
orderId = '1000'

#userid = 'Jack'
#password = '123456'
#mobiles = '13812345678'
#msg = 'hello world!'
#time = '2011-03-01'

#result = client.service.sendSms(userid, password, mobiles, msg, time)
result = client.service.sendUmMsg.sendSMS(mobileNum, msgContent, senderNum, orderId)

print result
