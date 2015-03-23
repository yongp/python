#!/usr/bin/python
#coding=utf-8

import os,time,re
from cpu import cpu_collect
from disk import disk_collect
from mem import mem_collect
from load import load_collect
from network import network_collect
from ping import ping_collect
from process_port import process_port
from sendsms import sendsms 
from write_mysql import mysql_reported
from multiprocessing import cpu_count

#timestamp
now = int(time.time())

#configuration file processing
def alarm_Threshold_conf():
	type_threshold = {}

	for line in open('../etc/alarm_Threshold.conf'):
		if not line.startswith('#'):
			if re.findall('^\w+\s+\d+',line):
				lines = line.split()
				type_threshold[lines[0]] = int(lines[1])

	return type_threshold

#funtion
def get_ip():
	command_idc_ip = "'{ print $2 }' | awk '{ print $1 }' | sed -n '/^172/p'"
	get_idc_ip = os.popen('netstat -ie  | grep "inet addr:" | awk -F ":" %s' % (command_idc_ip)).read().split('\n')[:-1]

	if len(get_idc_ip) != 0:
		local_ip = ''.join(get_idc_ip)

	return local_ip

def cpu_Alarm():
	#cpu alarm
	for k,v in cpu_collect().items():
		if k == 'id':
			pass
		else:
			for type,threshold in alarm_Threshold_conf().items():
				if type == 'cpu' and v >= threshold:
					cpu_alarm_info = """服务器IP: %s, cpu %s 使用率为: %s, 大于阀值 %s, 请尽快处理！""" %(get_ip(),k,v,threshold)
					sendsms(cpu_alarm_info)
				else:
					pass
	#mysql
	data = cpu_collect()
	command = "insert into cpu_status_history(serverip,wa,ni,sy,id,us,writetime)values('%s','%s','%s','%s','%s','%s','%s')" %(get_ip(),data['wa'],data['ni'],data['sy'],data['id'],data['us'],now)
	
	if mysql_reported(command) == False:
		cpu_info_reported = "服务器IP: %s, cpu数据写入mysql失败" %(get_ip())
		sendsms(cpu_info_reported)

def disk_Alarm():
	for k,v in disk_collect().items():
		#mysql
		command = "insert into partition_status_history(serverip,partname,usepercent,writetime)values('%s','%s','%s','%s')" %(get_ip(),k,v,now)
		if mysql_reported(command) == False:
			disk_info_reported = "服务器IP: %s, 磁盘分区数据写入mysql失败" %(get_ip())
			sendsms(disk_info_reported)
		
		#disk alarm
		for type,threshold in alarm_Threshold_conf().items():
			if type == 'disk' and v >= threshold:
				disk_alarm_info = """服务器IP: %s, 磁盘分区 %s 使用率为: %s, 大于阀值 %s, 请尽快处理！""" %(get_ip(),k,v,threshold)
				sendsms(disk_alarm_info)
			else:
				pass

def mem_Alarm():
	for k,v in mem_collect().items():
		for type,threshold in alarm_Threshold_conf().items():
			if k == 'Mem_Used' and type == 'Mem_Used' and v >= threshold:
				mem_alarm_info = """服务器IP: %s, %s 使用: %s, 大于阀值 %s, 请尽快处理!""" %(get_ip(),k,v,threshold)
				sendsms(mem_alarm_info)
             		elif k == 'Swap_Used' and type == 'Swap_Used' and v >= threshold:
                            	mem_alarm_info = """服务器IP: %s, %s 使用: %s, 大于阀值 %s, 请尽快处理!""" %(get_ip(),k,v,threshold)
                            	sendsms(mem_alarm_info)
			else:	
                          	pass
	#mysql
	data = mem_collect()
	command = "insert into mem_status_history(serverip,Mem_Used,Swap_Used,writetime)values('%s','%s','%s','%s')" %(get_ip(),data['Mem_Used'],data['Swap_Used'],now)
	
	if mysql_reported(command) == False:
		mem_info_reported = "服务器IP: %s, 内存数据写入mysql失败" %(get_ip())
		sendsms(mem_info_reported)

				
def load_Alarm():
	#Threshold = '%s' % cpu_count()
	Threshold = cpu_count()
	for k,v in load_collect().items():
		if v >= Threshold:
			load_alarm_info = """服务器IP: %s 负载过高，大于cpu %s个核心数，请尽快处理!""" %(get_ip(),threshold)
			sendsms(load_alarm_info)
		else:
			pass

	#mysql
	data = load_collect()
	command = "insert into load_status_history(serverip,load1,load5,load15,writetime)values('%s','%s','%s','%s','%s')" %(get_ip(),data['load(1min)'],data['load(5min)'],data['load(15min)'],now)
	
	if mysql_reported(command) == False:
		load_info_reported = "服务器IP: %s 负载数据写入mysql失败" %(get_ip())
		sendsms(load_info_reported)

def network_Alarm():
	#mysql
	In = network_collect()[0]
	Out = network_collect()[1]
	
	for k,v in In.items():
		command = "insert into network_status_history(serverip,networktype,input,output,writetime)values('%s','%s','%s','%s','%s')" %(get_ip(),k,v,Out[k],now)
		if mysql_reported(command) == False:
			network_info_reported = "服务器IP: %s 网卡流量数据写入mysql失败" %(get_ip())
			sendsms(network_info_reported)

	#print network_collect()[0]
	#print network_collect()[1]

def ping_Alarm():
	for k,v in ping_collect().items():
		#mysql
		command = "insert into ping_status_history(serverip,pingip,pingstatus,writetime)values('%s','%s','%s','%s')" %(get_ip(),k,v,now)
		print command
		if mysql_reported(command) == False:
			ping_info_reported = "服务器IP: %s ping数据写入mysql失败" %(get_ip())
			sendsms(ping_info_reported)

		#alarm
		if v == 'timeout':
			ping_alarm_info = """服务器IP: %s ping无法到达 %s, 请检查网络!""" %(get_ip(),k)
			sendsms(ping_alarm_info)

def process_port_Alarm():
	for k,v in process_port().items():
		for a,b in v[0].items():
			port = a
			portstatus = b
		
		for x,y in v[1].items():
			processname = x
			procestatus = y

		if portstatus == 'down' or  procestatus == 'stop':
			pro_port_alarm_info = """服务器IP: %s 端口号: %s 进程: %s 不存在，请尽快处理!""" %(get_ip(),port,processname)
			sendsms(pro_port_alarm_info)

		
		command = "insert into process_status_history(serverip,port,portstatus,processname,procestatus,writetime)values('%s','%s','%s','%s','%s','%s')" %(get_ip(),port,portstatus,processname,procestatus,now)

		if mysql_reported(command) == False:
			process_port_info_reported = "服务器IP: %s 进程端口数据上报mysql失败" %(get_ip())
			sendsms(process_port_info_reported)
	
if __name__ == '__main__':
	#cpu_Alarm()
	#disk_Alarm()
	#mem_Alarm()
	#load_Alarm()
	#network_Alarm()
	#ping_Alarm()
	process_port_Alarm()
	#print cpu_collect()
	#print disk_collect()
	#print mem_collect()
	#print load_collect()
	#print network_collect()
	#print ping_collect()
	#print process_port()
	#print alarm_Threshold_conf()
	#for k,v in load_collect().items():
		#print v
		#print type(v)
