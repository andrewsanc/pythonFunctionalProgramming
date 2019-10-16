'''
Python Jupyter - Pure functions. 2 rules. 1) Given the same input it will always return
                 the same output. 2) A function should not produce any side effects. Side
                 effects are elements that affect the outside scope of the function.
'''
#%%
def multiplyBy2(li):
  newList = []
  for item in li:
    newList.append(item*2)
  return newList

multiplyBy2([1,2,3]) # Takes an input. returns same output. doesnt affect the outside scope

#%%
newList = []
def multiplyBy2(li): # Isn't a pure function due to it effecting code outside the scope of the function
  for item in li:
    newList.append(item*2)
  return newList

multiplyBy2([1,2,3])