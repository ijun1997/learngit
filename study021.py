import time ,sys,queue
from multiprocessing.managers import BaseManager

class QueueMannager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='10.14.242.141'
print('Connect to sever %s...' % server_addr)
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()
for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d*%d...' % (n,n))
		r='%d*%d=%d' % (n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
	
print('worker exit.')		
