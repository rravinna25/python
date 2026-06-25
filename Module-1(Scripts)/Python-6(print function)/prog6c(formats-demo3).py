# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <5 spaces> 10.9
print('%10.3f'  %a) # <4 spaces> 10.927
print('%.2f'  %a)  #10.93
print('%.6f'  %a)  #  10.927400
print('%f'  %a) # 10.927400
print('%g'  %a) # 10.9274


'''
1) What  is  the  difference  between  8  and  2   in  %8.2f ?  --->  8  is  total  width  of  the  string 
																													and
																										2  is  number  of  digits  after  decimal  point  which
																										is  called  precision

2) What  is  the  suitable  format  for  currency ?  ---> %.2f  becoz  paise  is  a  2-digit  number   (or)   %g

3) What  is  the  default  precision  for  %f  ?  ---> 6  i.e.  6  digits  after  decimal  point
'''
