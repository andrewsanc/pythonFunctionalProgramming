'''
Python Jupyter - Filter function, filter(action, iteratable). Returns value from iterable based
                 on true.
'''
#%%
myList = [1,2,3]
def onlyOdd(item):
  return item % 2 != 0

print(list(filter(onlyOdd, myList)))
print(myList)

#%%
names = ['luci', 'alcazar', 'sam', 'duncan', 'drew']
def charSort(item):
  return item[0] == 'd'

print(list(filter(charSort, names)))

#%%
