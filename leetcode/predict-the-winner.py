class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        num_elements = len(nums)
        dp_table = [[0] * num_elements for _ in range(num_elements)]
      
        for i in range(num_elements):
            dp_table[i][i] = nums[i]
      
        for i in range(num_elements - 2, -1, -1):  # Start from second to last and go to start of the list
            for j in range(i + 1, num_elements):  # Start from just after i and move to the end of the list
                dp_table[i][j] = max(nums[i] - dp_table[i + 1][j],  # If choosing the start
                                     nums[j] - dp_table[i][j - 1])  # If choosing the end
      
        return dp_table[0][num_elements - 1] >= 0
