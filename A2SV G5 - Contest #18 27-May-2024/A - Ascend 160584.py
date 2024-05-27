# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

t= int(input())
lis = list(map(int, input().split()))

cur  = 0
mx = 0
start = 0
for i in range(t):
    if lis[i] <= cur:
        
        start = i
    cur = lis[i]
    mx =  max(mx, i - start +1)
print(mx)
