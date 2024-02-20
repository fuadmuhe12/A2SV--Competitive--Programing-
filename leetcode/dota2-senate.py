class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rlst = []
        dlst = []
        ind = 0
        for i in senate:
            if i == "R":
                rlst.append(ind)
            else:
                dlst.append(ind)
            ind += 1
        while len(rlst) >0 and len(dlst) >0:
            r = rlst.pop(0)
            d = dlst.pop(0)
            if r < d:
                rlst.append(len(senate)  + r)
            else:
                dlst.append(len(senate)  + d)
        if len(rlst) >0:
            return "Radiant"
        else:
            return "Dire"
