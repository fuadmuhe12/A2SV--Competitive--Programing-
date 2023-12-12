class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1.  create a dictionary with index inlist as value 
        2. for each val in the nums find if target -nums  in  dictionary 
        3.  if the vlaue have the same as prev val check the lenth of ind > 1 if so return ([0][1])
        else search for other iteration


        '''
        ind_dic = defaultdict(list)
        for key, val  in enumerate(nums):
            ind_dic[val].append(key)
        for values in nums:
            if target - values in ind_dic:
                if (target - values == values and len(ind_dic[(target - values)]) > 1) :
                    return ind_dic[(target - values)]
                if target - values != values:
                    return [ind_dic[values][0], ind_dic[target - values][0]]



