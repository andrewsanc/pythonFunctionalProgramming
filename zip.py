'''
Python Jupyter - Zip function, zip(*args). Takes in unlimited amount of arguments. Returns
                 tuple elements.
'''
#%%
myList = [1,2,3]
yourList = [10,20,30]

print(list(zip(myList, yourList)))

#%%
myList = [1,2,3]
yourList = [10,20,30]
theirList = (100,200,300)

print(list(zip(myList, yourList, theirList)))

#%%
users = ['andrew', 'travis', 'ted']
emails = ['druu@gmail.com', 'tzander@hotmail.com', 'tzanella@commexinc.com']

print(dict(zip(users, emails)))

#%%
