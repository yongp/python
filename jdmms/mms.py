#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys, httplib

def SendRtx(target,title,content):
    SENDTPL = \
            '''<?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://ws.oa.com/common/message">
        <SOAP-ENV:Body>
            <ns1:SendRTX>
                <ns1:sender>dantezhu</ns1:sender>
                <ns1:receiver>%s</ns1:receiver>
                <ns1:title>%s</ns1:title>
                <ns1:msgInfo>%s</ns1:msgInfo>
                <ns1:messageType>0</ns1:messageType>
            </ns1:SendRTX>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>'''

    SoapMessage = SENDTPL % (target,title,content)

    webservice = httplib.HTTP("ws.oa.com")
    webservice.putrequest("POST", "/messageservice.asmx")
    webservice.putheader("Host", "ws.oa.com")
    webservice.putheader("User-Agent", "Python Post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(SoapMessage))
    webservice.putheader("SOAPAction", "\"http://ws.oa.com/common/message/SendRTX\"")
    webservice.endheaders()
    webservice.send(SoapMessage)

    # get the response

    statuscode, statusmessage, header = webservice.getreply()
    print "Response: ", statuscode, statusmessage
    print "headers: ", header
    print webservice.getfile().read()

SendRtx('dantezhu',"素材管理系统","您的单")
