#!/usr/bin/python
#coding=utf-8

import MySQLdb
 
def mysql_reported(command):
	try:
		conn=MySQLdb.connect(host='*****',user='***',passwd='***',db='***',port=3306,charset='utf8')
		cur=conn.cursor()
		cur.execute(command)
		#cur.execute('select * from cpu_status_history')
		
		conn.commit()
		cur.close()
		conn.close()

		return True

	except MySQLdb.Error,e:
		#print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return False
	
#if __name__ == '__main__':
#	command = "insert into cpu_status_history(serverip,wa,ni,sy,id,us,writetime)values('172.22.213.59','0','0','1','96','2','1427100348')"
#	if mysql_reported(command) == True:
#		print 'sucess'
#	else:
#		print 'fail'
