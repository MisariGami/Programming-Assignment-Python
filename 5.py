# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Programming-Assignment-Python

# Exception ArithmeticError
try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")


# Exception LookupError
try: 
    a = [1, 2, 3] 
    print (a[3]) 
except LookupError: 
    print ("Index out of bound error.")


# Exception AttributeError
class Attributes(object):
    pass
  
object = Attributes()
print (object.attribute)


# Exception FloatingPointError
import math
print (math.exp(1000))


# Exception IndexError
array = [ 0, 1, 2 ]
print (array[3])



