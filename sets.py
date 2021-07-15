
#sets
'''
sets are data structures, similar to lists or dictionaries.
They are created using curly braces, or the set function.
They shares some functionality with lists, such as the use if in to check whether they contain a particulat item.
'''
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "egg", "sausage"])
print(3 in num_set)  #True
print("spam" not in word_set)  #False
'''
to create an empty set, ypu must use set(), as{} creates an empty dictionary.
Dictionry are also built with {}, but contain a pairs:
dict ={"a":1, "b":2}

lists:[], mutable, indexed, 
          use lists if you have a collection of data that does not need random access.
          try to choose lists when you need a simple, iterable collection that is modified frequently         
tuples:(), unmutable, indexed
           use tuples when your data cannot change
dictionary:{pairs}, mutable, a pair of key and value. 
           When you need a logical association between a key:value pair
           When your data is being constantly modified 
           A basically lists made up of keys each associated  with a value.
sets:{}, not indexed
         use a set if you need uniqueness for the elements
         sets are like lists, with the difference that its elements can't be repeatef(duplicated)

sets are like lists, except they don't assign indices to their element. Because
of this, sets use less memory than lists do, which is a big deal for large sets or lists.
'''

#set also gives you unique elements
elem = 1,2,3,4,4,5
print(set(elem))   #{1,2,3,4,5} #去除重複數


elem = 8,1,6,2,3,4,4,5
print(set(elem))  #自動排序

'''
unordered and unique collection of things is a set: example a set of cards considering the
symbol n number together whereas ordered collection which can contain duplicate things is a list:
example
'''

#An easy way to check whether a list contains duplicates:
list1 = [1, 2, 3, 4]
list2 = [1, 2, 2, 3]
list1 == list(set(list1))  #True
list2 == list(set(list2) ) #Flase
'''
This is because creating a set removes all duplicate elements from the argument.
'''

'''
Sets differ from lists in several ways, but share several list operations such as
"len". Instead of using append to add to a set, use "add".
The method remove removes a specific element from a set; POP removes an arbitrary element.
'''
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)  #{1, 2, 4, 5, 6, -7}

nums = {1, 2, 1, 3, 1, 4, 5, 6}
while len(nums) > 0:
    nums.pop()
    print(nums)
'''
{2, 3, 4, 5, 6}
{3, 4, 5, 6}
{4, 5, 6}
{5, 6}
{6}
set()
'''    
'''
it's arbitrary, because the way Python implements sets, there is not guarantee that
the elements will be returned in the same order,in which they were added 
in some cases it may, but not always,
'''

#pop works good only with string, not int 
a = [1, 2.0, True, '5', 7]
print(a)
for i in range(5):
    b = a.pop()
    print(a,b)
'''
[1, 2.0, True, '5', 7]
[1, 2.0, True, '5'] 7
[1, 2.0, True] 5
[1, 2.0] True
[1] 2.0
[] 1
''' 

nums = {1, 2, 1, 3, 1, 4, 5, 6, 4, 7, 3, 9}    
while len(nums)>0:
    nums.pop()
    print(nums)
'''output
{2, 3, 4, 5, 6, 7, 9}
{3, 4, 5, 6, 7, 9}
{4, 5, 6, 7, 9}
{5, 6, 7, 9}
{6, 7, 9}
{7, 9}
{9}
set()
  
# it removes all instances of the same numer in a ascending order, one by one
,except the last one in the order
'''

#using .pop with a list of integers
nums = {1, 2, 1, 3, 1, 4, 5, 6}
while len(nums)>0:
    nums.pop();
    print(nums)

print("\n")

#using pop with a string (converting from integers)
nums = {1, 2, 1, 3, 1, 4, 5, 6}
str1 = ''.join(str(e) for e in nums)
print(str1)
while len(nums)>0:
    nums.pop();
    print(nums)
print("\n")

#using pop with a string (backup incase the above code didn't work)
nums = {'1', '2', '1', '3', '1', '4', '5', '6'}
while len(nums)>0:
    nums.pop();
    print(nums)
'''output
{2, 3, 4, 5, 6}
{3, 4, 5, 6}
{4, 5, 6}
{5, 6}
{6}
set()


123456
{2, 3, 4, 5, 6}
{3, 4, 5, 6}
{4, 5, 6}
{5, 6}
{6}
set()


{'4', '5', '3', '6', '1'}
{'5', '3', '6', '1'}
{'3', '6', '1'}
{'6', '1'}
{'1'}
set()
'''

#converting nums from a set of integers to a set of strings using the set() function
nums = {3,14,15,9,26,53}
str1 = set(str(i) for i in nums)
msg = "\nThis is str1: {}\n".format(str1)
print(msg)
while len(str1) > 0:
    str1.pop()
    print(str1)

#converting nums from a set of integers to a set of strings using curly brace notation
nums ={3,14,15,9,26,53}
str2 = {str(i) for i in nums}
msg = "\nThis is str2: {}\n".format(str2)
print(msg)
while len(str2) > 0:
    str2.pop()
    print(str2)

#converting nums from a set of integers to a set of string characters using the map function and a traditionally-defined function
nums = {3,14,15,9,26,53}
def stringify(x):
    return str(x)
str3 = set(map(stringify,nums))
msg = "\nThis is str3: {}\n".format(str3)
print(msg)
while len(str3) > 0:
    str3.pop()
    print(str3)

#converting nums from a set of integers to a set of string characters using the map function and lambda syntax
nums = {3,14,15,9,26,53}
str4 = set(map(lambda x: str(x),nums))
msg = "\nThis is str4: {}\n".format(str4)
print(msg)
while len(str4) > 0:
    str4.pop()
    print(str4)
    
'''output
This is str4: {'9', '53', '3', '26', '14', '15'}

{'53', '3', '26', '14', '15'}
{'3', '26', '14', '15'}
{'26', '14', '15'}
{'14', '15'}
{'15'}
set()
'''



#sets can be combined using mathematical operations

first ={1, 2, 3, 4, 5, 6}
second ={4, 5, 6, 7, 8, 9}

print(first | second)   #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second)   #{4, 5, 6}
print(first - second)   #{1, 2, 3}
print(second - first)   #{8, 9, 7}
print(first ^ second)   #{1, 2, 3, 7, 8, 9} 
'''
|  the union operator | combines two sets to form a new one cointaining items in either.
& the intersection operator gets items only in both
- the difference operator gets items in the first set but not in the second
^ the symmetric difference operator gets items in either set, but not both.
'''
