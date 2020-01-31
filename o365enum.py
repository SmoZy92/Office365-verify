#!/usr/bin/env python
import string, sys, os ,json
import threading 
from queue import Queue 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
   
print_lock = threading.Lock()

def validate(email):
    cmd = './o365 {}'.format(email)
    out = os.popen(cmd).read()
    try:
        data = json.loads(out)
    except ValueError:
        return
    ValidAddress = data[0]["ValidAddress"]
    DomainIsO365 = data[0]["DomainIsO365"]
    if str(ValidAddress) == "True" and str(DomainIsO365) == "True":
        with print_lock:
            print(bcolors.OKGREEN + "[-]" + bcolors.ENDC + " {} is a valid O365 address email".format(email))
    else:
        with print_lock:
            print(bcolors.FAIL + "[-]" + bcolors.ENDC + " {} is not a valid O365 address email".format(email))
 

if __name__ == "__main__":
    if len (sys.argv) != 3 :
            print "Usage: ./" + sys.argv[0] + " [Email list] [Threads] "
            sys.exit (1)
            
email_list = [line.rstrip('\n') for line in open(sys.argv[1])]
threads = sys.argv[2]

def threader():
   while True:
      worker = q.get()
      validate(worker)
      q.task_done()

q = Queue()
 
for x in range(int(threads)):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()

for worker in email_list:
   q.put(worker)
 
q.join()
