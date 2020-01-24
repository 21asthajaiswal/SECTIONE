a = input()
k = ''
for i in a:
	b = a.count(i)
	if i not in k:
		print(i)
		k+=i
		
