'''
Python Jupyter - Map function, map(action, iteratable).
'''
#%%
def multiplyBy2(item):
  return item*2

list(map(multiplyBy2, [1,2,3]))

#%%
myList = [1,2,3]
def multiplyBy2(item):
  return item*2

print(list(map(multiplyBy2, myList))) # Map will return new list
print(myList)

#%%
