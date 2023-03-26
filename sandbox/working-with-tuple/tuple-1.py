"""
This module is tuple playground and
it demonstrates how tuples work
"""

tupleA = () #An empty tuple
print(type(tupleA))

tupleB = (1,) #A tuple with one element, it is necessary to have trailing comma
notTupleB = (1)
print(type(tupleB)) # Output: tuple
print(type(notTupleB)) # Output: int

tupleC = (1,2,3,4,5,6)
print(tupleC)
print(tupleC + (7,8))# Operations on tuple (+)
print(tupleC * 7)# Operations on tuple (*)

print(5 in tupleC) # in operator
print(7 not in tupleC) # not in operator