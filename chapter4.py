
import time
import datetime
from unicodedata import name
import schedule
import sys

def job(username):
    actual_time = datetime.datetime.now()
    print("{} is running at {}:{}:{}".format( name, actual_time.hour, actual_time.minute, actual_time.second))

    schedule.every(5).seconds.do(job,username="Alpha")
    schedule.every(10).seconds.do(job, username = "Beta")

while True:
    try:
      schedule.run_pending()
      time.sleep(2)
    except KeyboardInterrupt:
      sys.exit(0)
