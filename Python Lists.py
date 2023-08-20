st = []
for i in range(n):
    x = input()
    if x[0] == "i":
        lst = list(x.split())
        ind = int(lst[1])
        val = int(lst[2])
        st.insert(ind, val)
    elif x[0:2] == 'pr':
        print(st)
    elif x[0:3] == "rem":
        lst = list(x.split())
        if int(lst[1]) in st:
            st.remove(int(lst[1]))
    elif x[0] == 'a':
        lst = list(x.split())
        st.append(int(lst[1]))
    elif x[0] == 's':
        st = sorted(st) 
    elif x[0:2] == 'po':
        st.pop()
    else:
        st = st[::-1]
