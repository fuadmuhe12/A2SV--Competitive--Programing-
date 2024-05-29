# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/


class UnionFind:
    def __init__(self, num):
        self.parent = list(range(num))
        self.rank = [0 for _ in range(num)]
    
    def find_set(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find_set(self.parent[u])
        return self.parent[u]

    def union(self, set1, set2):
        if set1 == set2:
            return
        rank1, rank2 = self.rank[set1], self.rank[set2]
        if rank1 > rank2:
            self.parent[set2] = set1
        else:
            self.parent[set1] = set2
            if rank1 == rank2:
                self.rank[set2] += 1
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        sets = set()
        for acc in accounts:
            for address in acc[1:]:
                sets.add(address)
                
        N, M = len(accounts), len(sets)
        addresses = sorted(list(sets))
        ind_ad_dic = {(idx + N) : address for idx, address in enumerate(addresses)}
        adre_ind_dic = {address : (idx + N) for idx, address in enumerate(addresses)}
        
        uf = UnionFind(N + M)
        
        for i, acc in enumerate(accounts):
            for address in acc[1:]:
                address_idx = adre_ind_dic[address]
                uf.union(uf.find_set(i), uf.find_set(address_idx))
        
        parent_dict = collections.defaultdict(list)
        for i in range(N + M):
            parent = uf.find_set(i)
            parent_dict[parent].append(i)
        
        res = []
        for group in parent_dict.values():
            person_idx = group[0]
            person = accounts[person_idx][0]
            data = [person]
            for address_idx in group[1:]:
                if address_idx >= N:
                    data.append(ind_ad_dic[address_idx])
            res.append(data)
        
        return res