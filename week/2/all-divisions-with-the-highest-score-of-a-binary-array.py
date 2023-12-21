class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        '''
        dic {1:[0], 2:[1], 3:[2], }
        [0 0 1 0]  l(zero) =3 r[one] = 0 tot = 3
                1 
                i = 4
        l-zero = 2
        r-one = 0
        count_one = 1
        count_zero = 3l

        '''
        store = defaultdict(list)
        left_zero = 0
        right_one = nums.count(1)
        store[left_zero+right_one].append(0)
        for ind in range(1, len(nums)+1):
            if nums[ind-1] == 0:
                left_zero += 1
            else:
                right_one -= 1
            store[left_zero+right_one].append(ind)
        return store[max(store.keys())]




        