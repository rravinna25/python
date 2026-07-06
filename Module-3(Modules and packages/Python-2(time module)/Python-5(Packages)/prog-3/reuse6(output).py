# Save  in  any  file  of  cwd
import   p1 #  Imports  package  p1  and  automatically  executes  p1 . __init__  module
import  p1 . mod1  #  Imports  p1 . mod1  but  does not  execute  p1 . __init__  module  as  it  is  already  executed
from  p1  import  mod1  #   Imports  mod1  of  package  p1  but  does not  execute  p1 . __init__  module  as  it  is  already  executed
from   p1 . mod1  import   * #   Imports  all  the  members  of  p1 . mod1  but  does  not  execute  p1 . __init__  module  as  it  is  already  executed
import  p1 . __init__   #   Imports  p1 . __init__  module  but  does not  execute  p1 . __init__  module  as  it  is  already  executed


'''
__init__   module  is  executed
__name__  :   p1
__init__   module  is  executed
__name__  :   p1.__init__
'''
