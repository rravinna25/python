# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if  __name__  ==  '__main__':
	print('Four')
	print('Five')
	print('Six')
print('Seven')
print('Eight')
print('Nine')


'''
1) py  mod1.py
   What  is  the  value  of  __name__ ?  --->  '__main__'
   What  are  the  outputs ?  ---> One , Two , Three , Four , Five , Six , Seven , Eight , Nine

2) import  mod1
    What  is  the  value  of  __name__ ?  --->  'mod1'
    What  are  the  outputs ?  ---> One , Two , Three , Seven , Eight , Nine
'''
