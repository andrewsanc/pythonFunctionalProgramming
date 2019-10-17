'''
Python Jupyter - Exercise: Lambda expressions.
'''
# Using Lambda, return squared numbers.
#%%
nums = [5,4,3]

print(list(map(lambda num: num**2, nums)))

# List sorting. Sort by the second element.
#%%
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)
#%%
