n=int(input())
t=n
for i in range(1,n+1):
	r=n%10
	n=n/10
	sum=s+r*r*r
	s=s+1
if(t==sum):
	print('pallandrome')
else:
	print('not pallandrome')

