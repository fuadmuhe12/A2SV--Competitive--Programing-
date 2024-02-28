t = int(input())
for i in range(t):
    n = int(input())
    ls = list(map(int, list(input())))
    from collections import defaultdict
    dic = defaultdict(int)
    dic[0] = 1
    acc = 0
    ans = 0
    for ind, val in enumerate(ls):
        acc += val
        if acc - (ind +1) in dic:
            ans += dic[acc - (ind +1)]
        dic[acc - (ind +1)] += 1
    print(ans)



        




