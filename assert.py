mylist = ['item']
assert len(mylist) >= 1 # AssertionError не будет
mylist.pop()
print(mylist)
assert len(mylist) >= 1 # AssertionError есть
