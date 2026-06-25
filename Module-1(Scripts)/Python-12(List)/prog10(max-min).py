# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #  Largest  element  of  list  'a'  i.e. 30
print(min(a)) #   Smallest  element  of  list  'a'  i.e.  5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))  #  Largest  string  of  list  'b'  i.e.  Vamsi
print(min(b))  #  Smallest  string  of  list  'b'  i.e.  Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) # Error :  List  can  not  have  complex  number  to  determine  largest  element
d = [25 , '35']
#print(max(d)) # Error :  List  can  not  have  number  and  string  to  determine  largest  element
#print(max([]))  # Error :  List  can  not  be  empty  to  determine  largest  element
#print(min([]))   # Error :  List  can  not  be  empty  to  determine  smallest  element


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''
