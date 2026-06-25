# Formats  demo  program
a = 25.68
print('%d'  %a)  #  Converts  object  'a'  to   string  integer  due  to  '%d'  i.e.  '25'
print('%s'  %a)  #  Converts  object  'a'  to   string  due  to  '%s'  i.e.  '25.68'
print('%f'  %a)  #  Converts  object  'a'  to   string  float   due  to  '%f'  i.e.  '25.680000'
print('%g'  %a)   #  Converts  object  'a'  to   string  float   due  to  '%g'  i.e.  '25.68'
#print('%f' ,  %a)  #  Error  due  to  comma
print('a : ' ,  a)  #  a :  <space> 25.68
print('%f' ,  a) #   %f  <space>  25.68
#print('%f'  a)  #   Error  :  %  is  missing  for  object  'a'
#print('a  :  '  %a)  #  Error  :  Format is  missing


'''
Formats
-----------
1) What  is  the  format  for  integer ?  --->  '%d'  (or)  '%i'
    What  is  the  format  for  float ?  --->  '%f'  (or)  '%g'
    What  is  the  format  for  string ?  --->  '%s'
    What  is  the  format  for  list , tuple , set  and  dict ?  --->  No  format

2) What  is  '%d'  (or)  '%i'  called  ?  --->  String  integer
    What  is  '%f'  (or)  '%g'  called  ?  --->  String  float
    What  is  '%s'  called  ?  --->  String  
	
3) What  does  '%d'   %object  do ?  --->  Converts   object  to  string  integer  
     What  does  '%f'   %object  do ?  ---> Converts   object  to  string  float 
     What  does  '%s'   %object  do ?  --->  Converts   object  to  string  
	 
4) How  many  digits  after  decimal  point  for  %f ?  ---> 6
     How  many  digits  after  decimal  point  for  %g ?  ---> Variable  number  of  digits

5) What  is  a  better  format  between  '%f'  and  '%g' ?  --->   %g'  becoz  unnecessary  zeroes  are  not  printed

6) What  does  'g'  stand  for  in  '%g' ?  --->  general

7) What  is  %  in  '%s'  called  ?  ---> Format  specifier

8) What  are  the  two  ways  to  convert  object  to  string ?  --->  str(object)  and  '%s'   %object
'''
