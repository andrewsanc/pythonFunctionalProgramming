'''
Python Jupyter - List Comprehensions. Allows us to create quick sets/dictionaries/list/etc 
                 instead of looping or appending.
'''
#%%
mySet = {char for char in 'hellooo'}
mySet2 = {num for num in range(0,100)}

print(mySet)
print(mySet2)

#%%
simpleDict = {
  'a': 1,
  'b': 2
}

myDict = {key:value**2 for key,value in simpleDict.items()}

print(myDict)

#%%
myDict = {num:num*2 for num in [1,2,3]}
print(myDict)

#%%
