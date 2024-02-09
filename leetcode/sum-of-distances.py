class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        {key : [old_val, rep, last_ind]}
        [1, 3, 1, 1, 2, 1, 1]
        {1:3, 3:1,
         }
        [0, 0, 2, 4, 0, 0, 0]
                ___
        ___________

        th5

        ________________
                ________
                  ______ 
        """
        dic =  defaultdict(list)
        arr = [0]*len(nums)
        for ind, val in enumerate(nums):
            if val in dic:
                old, rep, lind  = dic[val]
                old =  old + rep*(ind -lind)
                arr[ind] += old
                dic[val] = [old, rep +1, ind]
            else:
                dic[val] = [0, 1, ind]
        arr = arr[::-1]
        new  = defaultdict(list)
        for ind, val in enumerate(nums[::-1]):
            if val in new:
                old, rep, lind  = new[val]
                old =  old + rep*(ind -lind)
                arr[ind] += old
                new[val] = [old, rep +1, ind]
            else:
                new[val] = [0, 1, ind]
        return arr[::-1]




