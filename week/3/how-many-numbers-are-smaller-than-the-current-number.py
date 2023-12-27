from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        val = nums[:]
        val.sort()

        # Iterate through each element in nums
        for i in range(len(nums)):
            # Check if the element is not already in the dictionary
            if val[i] not in dic:
                # Store the count of elements smaller than the current element
                dic[val[i]] = i

        # Create a list of counts for each element in nums
        result = [dic[num] for num in nums]

        return result
