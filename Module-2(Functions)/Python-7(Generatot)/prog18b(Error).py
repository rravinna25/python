# Find  outputs (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1() #  Error  :   Excess  elements  in  generator  object
#p , q , r , s , m = f1()  #  Error  :  Few   elements  in  generator  object
m , n , o , p = f1()  #   Unpacks  generator  object  to  4  elements
print(m , n , o , p)    #  10  <space>  20  <space>  30  <space>  40 
