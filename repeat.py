t=(1,2,3,4,5,5,'rani','rani')
element=input()
k=-1
c=t.count(element)
print('number of element',c)
for i in range(c):
	k=t.index(element,k+1)
	print('position',k)
