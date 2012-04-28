import json
from datetime import datetime
import os

num_logs = 5
logs_dir = '../logs/'
log_path = logs_dir+'log%d_%s.json' % (0, datetime.today().strftime("%b%d@%H:%M"))

# Write all the old logs to new files.
# eg log0 -> log1, log8 -> log9, up to log9.
logs = os.listdir(logs_dir)
for i in range(num_logs):
	if i<len(logs):
		# write log1 to log2.
		 # open old log
		old_log = open(logs_dir+logs[i], 'r')
		 #open new log
		new_log = open(logs_dir+logs[i].replace(str(i), str(i+1), 1), 'w')
		 #write data from old to new
		new_log.write(old_log.read())
		new_log.close()
		old_log.close()
		os.remove(logs_dir+logs[i])
	else:
		print "not doing %d" % i


# create empty file
open(log_path,'w').close()


class logger(object):
	def __init__(self, name):
		self.name = name

	def log(self, msg, *args):
		f = open(log_path, 'a')
		f.write(json.dumps({
			'time': datetime.now().strftime("%H:%M:%S"),
			'text': msg % args,
			'origin': self.name,
		})+'\n');
		f.close()