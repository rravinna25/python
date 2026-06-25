# complex()  function  demo  program
print(complex(3 , 4)) # (3+4j)
print(complex(0 , 4)) #  4j
print(complex(3)) # (3+0j)
print(complex(3.8 , 4.6)) # (3.8 + 4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3 + 4.5j)
print(complex(True , False)) # (1+0j)
print(complex(True)) #  (1+0j)
print(complex(False)) #  0j
print(complex(True , 4)) # (1+ 4j)
print(complex('3')) #  (3+0j)
print(complex('3.8')) # (3.8+0j)
#print(complex(3 , '4')) #  Error :  2nd  argument  can  not  be  a  string
#print(complex('3' , 4)) #  Error :  2nd  argument  is   not  permitted  as  first argument is  a  string
#print(complex('3' , '4'))  #  Error :  2nd  argument  is   not  permitted  as  first argument is  a  string
#print(complex('Ten')) #  Error  :  'Ten'  can  not  be converted  to  complex
