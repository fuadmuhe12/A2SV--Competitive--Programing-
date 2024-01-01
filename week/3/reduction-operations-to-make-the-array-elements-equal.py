class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        1. we will have a counter the store it on cur_dif
        2. the goal is to make the len cur_dif 1
        3. we gonna sort the keys in deceasing order store it in cur_keys
        4. we goona hava pointer Itering over the keys let be pon
            also a op = 0
        iterate over the keys and add ot the op and also second elem , oly iterate over 0 -len(key)-2
        5. we gonna take the number of the key and add to op and also the second key of the elem 
        6. iterarte 
        """

        cur_dif = Counter(nums)  
        keys = sorted(cur_dif.keys(), reverse=True)
        op = 0
        for i in range(1, len(keys)):
            op += cur_dif[keys[i-1]]
            cur_dif[keys[i]] += cur_dif[keys[i-1]]
        
        return op


