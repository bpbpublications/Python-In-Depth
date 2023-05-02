############################################################################################
#    Python in-depth
#
#    Chapter 4
#
#        Useful Modules and Libraries
#
#    Example of scheduler
#
#    Author: Ahidjo Ayeva
###########################################################################################

import sys
import time
import datetime
import schedule


def job(name):
	actual_time = datetime.datetime.now()
	print("{} is running at {}:{}:{}".format(name, actual_time.hour,
											actual_time.minute,
											actual_time.second))


schedule.every(5).seconds.do(job, "Alpha", )
schedule.every(10).seconds.do(job, "Beta")

while 1:
	try:
		schedule.run_pending()
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(0)
