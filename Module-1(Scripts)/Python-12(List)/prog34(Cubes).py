# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [x ** 3 for x in range(2, 11, 2)]  #   Appends  x ^ 3  to  list  'a'  where  'x'  varies  from  2  to  10  in  steps  of  '2'
print(a)  #  [8 , 64 , 216 , 512 , 1000]
