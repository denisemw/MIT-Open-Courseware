def rev(s):
	assert type(s) == list
	for i in range(len(s)/2):
		tmp = s[i]
		s[i] = s[-(i+1)]
		s[-(i+1)] = tmp
s =	[1,2,3]
rev(s)
print s
