############################################################################################
#    Python in-depth
#
#    Chapter 4
#
#        Useful Modules and Libraries
#
#    Example of scheduler with job execution in parallel.
#
#    Author: Ahidjo Ayeva
###########################################################################################

import sys
import time
import datetime
import schedule
import threading

def job(name):
	actual_time = datetime.datetime.now()
	print("{} is running at {}:{}:{}".format(name, actual_time.hour,
											actual_time.minute,
											actual_time.second))

def run(func, args):
	thread = threading.Thread(target=func, args=args)
	thread.start()

schedule.every(5).seconds.do(run, job, args=("Alpha",))
schedule.every(5).seconds.do(run, job, args=("Beta",))
schedule.every(5).seconds.do(run, job, args=("Teta",))

while 1:
	try:
		schedule.run_pending()
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(0)
