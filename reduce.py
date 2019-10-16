'''
Python Jupyter - Reduce function. reduce(func, sequence). Reduces values from an iterable to
                 a accumulator.
'''
#%%
from functools import reduce

myList = [1,2,3]

def accumulator(acc, item):
  return acc + item

print(reduce(accumulator, myList, 0))
#%%
