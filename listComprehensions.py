'''
Python Jupyter - List Comprehensions. Allows us to create quick sets/dictionaries/list/etc 
                 instead of looping or appending.
'''
#%%
# Original way of appending elements to a list
myList = [] 
for char in 'hellooo':
  myList.append(char)

print(myList)

#%%
# List comprehension way.
myList = [char for char in 'hellooo']
myList2 = [num for num in range(0,100)]

print(myList)
print(myList2)

#%%
mylist3 = [num*2 for num in range(0,100)]

print(mylist3)

#%%
myList4 = [num**2 for num in range(0,100)
  if num % 2 == 0]

print(myList4)

#%%
