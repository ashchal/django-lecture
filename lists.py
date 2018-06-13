mylists=['a','b','c','d','e']
mylist=['a','b','c','d','e']

mylists.append('new')
print(mylists)

mylist.reverse()
print(mylist)

num=[1,2,38,4,3]
num.sort()
print(num)

newlist=[1,2,['x','y','z']]
print(newlist[2][2])

#list comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
print(first_col)
