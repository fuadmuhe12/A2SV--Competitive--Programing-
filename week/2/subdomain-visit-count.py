class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic =  defaultdict(int)
        for cur in cpdomains:
            val , dom = cur.split()
            val = int(val)
            dom =list(dom.split("."))
            for i in range(len(dom)):
                dic[".".join(dom[i:])] += val
        return [f'{value} {key}' for key, value in dic.items()]


