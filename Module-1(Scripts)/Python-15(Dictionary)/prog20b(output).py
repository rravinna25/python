# Find  outputs (Home  work)
a = {'AB' : 'Hyd' ,  'CD' : 'Sec' ,  'EF' : 'Cyb' ,  'GH' : 'Pune'}
for  x , y   in  a . items():  #  x  and  y  are  elements  of  each  tuple  in  the  list  of  dict_items  object
       print(x , y , sep = ' ... ')  #   AB ... Hyd  <next  line>  CD ... Sec  <next  line>  EF ... Cyb <next  line>  GH ... Pune  <next  line>
print()	   
for  x , y   in  a . keys():  #  x  and  y  are  characters  of  each  key  in   the  list  of  dict_keys  object
       print(x , y , sep = ' ... ')  #   A ... B  <next  line>  C ... D  <next  line>  E ... F  <next  line>  G ... H  <next  line>
print()	   
for  x , y   in  a:  #  x  and  y  are  characters  of  each  key  in   the  list  of  dict_keys  object
       print(x , y , sep = ' ... ')	   #   A ... B  <next  line>  C ... D  <next  line>  E ... F  <next  line>  G ... H  <next  line>
print()	   
for  x , y , z   in  a . values():  #  x , y  ,  z   are  characters  of  each  value  in   the  list  of  dict_values  object
       print(x , y , z , sep = ' ... ')   #   H ... y ... d  <next  line>  S ... e ... c  <next  line>  C ... y  ... b  <next  line>  Error :  Pune  has  more  than  3  chars
