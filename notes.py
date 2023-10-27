from decimal import Decimal
import requests

Decimal("1.973282738")
Decimal(1.92798372) #becomes a float point which is WRONG 

r = requests.get("http://website.com")
r.content # shows me the content 
# r.text or r.json()

# Key is the lookup and value is value 

# Variable.keys()
x = [1,2,3]
while x: 
	x.pop()
# Pop as in pop off not populate 

# Everything goes into ram for memory 
# —> can do gpu 

def foo(x):
	print(x.pop())

x.append(1)
foo(x)#     MUST CALL FUNCTIONS 

#Ctrl L —> clears ur page 

#Global = bad 

#Lists, dictionaries, and objects —> get affected by foo while variables do not 

#Type hinting
from typing import List, Any
def foo(x: int, y: List[int]) -> int: 
    return y[x]
foo(1, [1,2,3])

#class is a collection of data and functions 
class foobar:
    arr: List[Any]
    def foo(self, x):
          """
          foo returns the xth element of arr
          """
          return self.arr[x]
    def bar(self, x):
        """
        bar will append x to arr
        """
        return self.arr.append(x)
    def __init__(self, *elems) -> None:
          self.arr = list(elems)
x = foobar(1,2,3)
#bar in this instance adds "asdf" to the end 
# """ will create a hover text message that you can see on docstring 

#after an index error appears
try:
    x.foo(300)
except IndexError as e:
    print(f"oh no we have an issue here: {e}")
except KeyError as e:
    print(f"key error")
else:
     print("yayyyyy")
finally:
     print("well, we done")

class baz(foobar):
#class is indicating an object type 
# the foobar in parenthesis means that baz inherits attributes and functions
    def baz(self, x):
         print(type(x))
x = baz(1,2,3,4)