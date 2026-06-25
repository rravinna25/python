# Find outputs  (Home  work)
a = {'AB' : 20 , 'CD' : 40 ,  'EF' : 60}
for  x , y  in   a . items():  #  dict_items([('AB' , 20) , ('CD' , 40) , ('EF' , 60)])
	print(x , y , sep = '...')  #   AB ...  20  <next  line>  CD  ... 40    <next  line>  EF  ...  60   <next  line>
for  x ,  y  in   a:    #  dict_keys(['AB' , 'CD' , 'EF'])
	print(x , y , sep = '...')  #   A ... B    <next  line>   C  ...  D   <next  line>  E  ... F   <next  line>
for  x , y  in  {'AB' : 20 ,  'CDE' : 40 ,  'FGHI' : 60}:  #  dict_keys(['AB' , 'CDE' , 'FGHI'])   
	print(x , y , sep = '...')  #   A ... B    <next  line>   Error  in  2nd  iteration
			
