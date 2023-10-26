input()
a=[*map(int,input().split())]
if any((x-a[0])%2for x in a):a.sort()
print(*a)
