import os
pid = os.fork()
# fork and exec together
print ("second test")
if pid == 0: # This is the child
 print ("this is the child")
 print ("I'm going to exec another program now")
 os.execl('program.sh', 'cmd') # insert the new program here
else:
 print ("the child is pid %d" % pid)
 os.wait()


