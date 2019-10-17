'''
Python Jupyter - Exercise: Comprehensions.
'''
#%%
chars = ['a','b','c','b','d','m','n','n']

duplicates = list(set([char for char in chars
  if chars.count(char)>1]))

print(duplicates)

#%%
