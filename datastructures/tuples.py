#Tuples
'''Tuples are very similar to list, except that they are immutable.
mweans that they cant be changed at all anyway whatsoever. As such, they are fater
to deal with for computers as they are STATIC.
Also, they are created using parentheses, rather than square bracket,
Slicing is just a means of retrieving values, so just chill, it's not at all there to
MODIFY values at all.
'''

words=("spam", "egg", "sausage",)
print(words[0])

words[1]="cheese"
#TypeError:'tuple' objest does not support item assignment

#tuple can incluse num str list, and the list in tuple is mutable.

t=(1,"hungry",["x","y"])
t[2][0]='abc'
print(t)

#Tuple can also be "packed" and "Unpacked" which can be very useful for creating variables

fruits=("apple","orange","melon")
f1,f2,f3=fruits
print(f1)
print(f2)
print(f3)

#list
list=["one",2]
#dictionary
dic={1:"one","two":2,3:[1,2,3]}
#Tuple
tup=(1,"two",[1,2,3])
#tuple can be created without parentheses() by just separating with commas,
tuple="one",2,[1,2,3]

'''Tuple is simple for PC, because tuple is static and immutable. So tuples 
are faster than lists.'''

tuple=(1,(1,2,3))
print(tuple[1])
print(tuple[1][0])
print(tuple[1][1])
print(tuple[1][2])
#we almost got the same results
list=[1,[1,2,3]]
print(list[1])
print(tuple[1][0])
print(tuple[1][1])
print(tuple[1][2])



'''
this list slicing reversese the list numbers
[::-1] cause it's [index1:index2:step], where index 1 is default to 0
index is default to last in the list.
'''
nums = (55, 44, 33, 22, 11)
print(max(min([:2]),abs(-42)))

