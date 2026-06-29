#  Find  outputs
import  time
from  importlib  import  reload
import   module1  #  imports  module1  and  also  executes  statements  of  module1
print('Program   sleeps  for  30  sec')
time . sleep(30) #  Modify  module1  in   30  sec
reload(module1)  #  Executes  modified   module  i.e.  module1
print('End')


'''
Hyd
Sec
Cyb
Program  sleeps   for  30  sec
Hyd
Sec
Cyb
India
Usa
End


Modify  module1  within  30  sec  after  execution  of  current  module
i.e.  Add  two  more  print  statements  to  module1.py
'''
