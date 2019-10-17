'''
Python Jupyter - Lambda. Lambda expressions are one time anonymous functions. 
                 lambda param: action(param)
'''
#%%
myList = [1,2,3,4]

print(list(map(lambda item: item*2, myList)))
print(myList)

#%%
words = ['alcazar', 'luci', 'duncan', 'sam']

print(list(map(lambda name: name.title(), words)))

#%%
from functools import reduce
myList = [1,2,3,4]

print(reduce(lambda acc, item: acc+item, myList))

#%%
