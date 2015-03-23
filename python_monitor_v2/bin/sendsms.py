#!/usr/bin/python
#coding=utf-8

import urllib2
import urllib


def sendsms(content):
	url = 'http://sendsms.pp.jd.com/cgi-bin/jd_sendsms'

	smsid = {'smsid':'com.paipai.backService.alert'}
	phone = {'phone':'18688950910'}
	#phone = {'jiangpengxian':'18664907029', 'yinmiao':'18676697051', 'pengyong':'18688950910'}
	#phone = {'jiangpengxian':'18664907029'}
	#phone = {'yinmiao':'18676697051'}
	content = {'content':'%s' %(content)}

	smsid_info = urllib.urlencode(smsid)
	phone_info = urllib.urlencode(phone)
	content_info = urllib.urlencode(content)

	#post
	#req = urllib2.Request(url,data)

	#get
	req = url + '?' + smsid_info + '&' + phone_info + '&' + content_info
	print req

	try:
		s = urllib2.urlopen(req).read()
		print s
	except urllib2.HTTPErrror,e:
		print e.code
	except urllib2.URLErrror,e:
		print str(e)

