from itertools import*
for s in[*open(0)][2::2]:print(sum(max(map(int,v))for _,v in groupby(s.split(),str.isdigit)))
