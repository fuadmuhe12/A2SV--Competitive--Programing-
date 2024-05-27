# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import math
t=int(input())
for q in range(t):
	m=int(input())
	p=input().split()
	p=[int(z) for z in p]
	n=int(math.log(m,2))
	k=0
	for x in range(n-1,-1,-1):
		l=2**x
		i=0
		j=l
		while j<m:
			if p[i:j]>p[i+l:j+l]:
				k+=1
				p[i:j],p[i+l:j+l]=p[i+l:j+l],p[i:j]
			i+=l*2
			j+=l*2
	u=[]
	u+=p
	p.sort()
	if u!=p:
		k=-1
	print(k)