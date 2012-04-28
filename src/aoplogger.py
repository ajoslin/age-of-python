import json
from datetime import datetime
import os

num_logs = 5
logs_dir = '../logs/'

# Backup all previous log files, up to num_logs
# eg log0 -> log1, log2 -> log3
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
		# remove the log we just backed up
		os.remove(logs_dir+logs[i])

# set the path for the current log
log_path = logs_dir+'log%d_%s.json' % (0, datetime.today().strftime("%b%d-%H.%M"))
# create empty file for it
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