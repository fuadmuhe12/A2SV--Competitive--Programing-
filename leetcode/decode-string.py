class Solution:
    def decodeString(self, s: str) -> str:
        lst = [i for i in s]
        answer = []
        indx = 0
        def number (val):
            try:
                val = int(val)
                return True
            except:
                return False
        k = ''
        def rec(k, indx):
            val = []
            ks = ''
            while len(lst) > indx and lst[indx] != ']':

                if number(lst[indx]):
                    ks += lst[indx]
                    indx += 1
                    continue

                if lst[indx] == '[':
                    # val.append(rec(int(lst[indx-1]), indx + 1 ))
                    #
                    cur = rec(int(ks), indx + 1)
                    ks = ''
                    for i in cur:
                        val.append(i)
                    indx = val.pop()
                    #
                if lst[indx] != ']': val.append(lst[indx])
                indx += 1
            val = val*k
            val.append(indx)
            return val

        ks = ''
        while len(lst) > indx:

            if number(lst[indx]):
                ks += lst[indx]
                indx += 1
                continue
            if lst[indx] == '[':
                cur = rec(int(ks), indx + 1)
                ks = ''
                for i in cur:
                    answer.append(i)
                indx = answer.pop()
            else:
                if lst[indx] != ']':
                    answer.append(lst[indx])
            indx += 1
        last = ''
        for i in answer:
            last += i
        return last