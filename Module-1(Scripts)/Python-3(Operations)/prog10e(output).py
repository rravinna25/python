#  Find   outputs (Home work)
i = 10
i = not  i > 14 # not  10 > 14  --->  not  False   --->   True
print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))# True


'''
1) i = not  i >  14
   Why  is  >  operator  evaluated  before  not  operator ?  --->
                                                     Since  relational  operator  '>'  has  got  higher  priority  over  logical  operator  not

2) ! (6 < 4  ||  9 >= 5  &&  6 != 6)
    = !(false  ||  true  &&  false)
    = !(false  ||  false)
    = !false
    = true
'''
