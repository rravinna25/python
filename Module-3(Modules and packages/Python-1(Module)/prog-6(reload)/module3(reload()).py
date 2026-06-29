# reload()  function  demo  program
import    importlib
import  module1   #  imports  module1  and  also  statements  of  module1
print()
importlib . reload(module1)  #  Executes  module1  after  loading  into  memory
print()
importlib . reload(module1)  #  Executes  module1  again  after  loading  into  memory
#importlib . reload('module1')  #  Error :  reload()  function  expects  module  but  string  is  passed
#reload(module1)  #  Error :  current  module  does  not  have  reload()  function  

'''
Hyd
Sec
Cyb

Hyd
Sec
Cyb

Hyd
Sec
Cyb
'''
