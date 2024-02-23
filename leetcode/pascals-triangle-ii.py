class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def rec(target, stack , ind = 0):
            if ind == target:
                return stack
            else:
                stack.append(1)
                if len(stack) > 2:
                    demo =  stack[:]
                    for ind  in range(1, len(stack)-1):
                        stack[ind] = demo[ind-1] + demo[ind]
            return rec(target, stack, ind+1  )
        return rec(rowIndex, [1])



