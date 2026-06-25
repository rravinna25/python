# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #  ['Hyd\nis', 'green\tcity']  i.e. splits  on  ' '   
print(a . split()) #  ['Hyd', 'is', 'green', 'city']  i.e. splits  on   white  space   
print(a . split('green'))  #  ['Hyd\nis ', '\tcity']  i.e.  splits  on  'green'  
print(a . split(''))  #  Error :  Delim  can  not  be  empty  string
