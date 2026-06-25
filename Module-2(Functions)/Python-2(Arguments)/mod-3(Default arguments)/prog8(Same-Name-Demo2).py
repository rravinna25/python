# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument function :   <space> 10 <space> 20 <space> 30
#disp(40 , 50 , 60 , 70) # Error :  70  is  excess  argument 
disp(80 , 90) # 3-argument fucntion :  <space> 80 <space> 90 <space> 25
