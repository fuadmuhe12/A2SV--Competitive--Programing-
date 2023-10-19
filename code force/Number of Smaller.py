n, m = list(map(int, input().split()))
l1 =list(map(int, input().split()))
l2 =list(map(int, input().split()))
p1 = 0
p2 = 0
final = []
k = False
while p2 < m:
    if k:
        final.append(n)
        p2 += 1
        continue
    if l2[p2] > l1[p1]:
        p1 += 1
        if p1 == n:
            k = True
    else:
        final.append(len(l1[0:p1]))
        p2 += 1
 
for i in final:
    print(i, end=" ")
