import json
from datetime import datetime
import os
import shutil

num_logs = 5
logs_dir = os.getcwd()+'/../logs/'

def log_file(n): return logs_dir+("log%d.json" % n)

def backup_log_file(n):
	try:
		shutil.copyfile(log_file(n), log_file(n+1))
	except IOError:
		do_something_so_python_doesnt_error = True

for i in range(num_logs):
	backup_log_file(i)

# Backup all previous log files, up to num_logs
# eg log0 turns into log1
for i in range(num_logs):
	backup_log_file(i)

# make sure log0 (current log) is empty
open(log_file(0),'w').close()

class Logger(object):
	def __init__(self, name):
		self.name = name

	def log(self, msg, *args):
		f = open(log_file(0), 'a')
		if len(args)>0:
			msg = msg % args
		f.write(json.dumps({
			'time': datetime.now().strftime("%H:%M:%S"),
			'text': msg,
			'origin': self.name,
		})+'\n');
		f.close()