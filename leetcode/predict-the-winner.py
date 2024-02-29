class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def maxscore(left, right, turn ):
            if left > right:
                return 0
          
            if turn: 
                return  max((nums[left] + maxscore(left +1, right, not turn), nums[right] + maxscore(left, right-1, not turn)))
            else:
                return min(  maxscore(left +1, right, not turn) - nums[left], maxscore(left, right-1, not turn) - nums[right])
           
        val =  maxscore(0, len(nums)-1, True)
        return val >= 0


