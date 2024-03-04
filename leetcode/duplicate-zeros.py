class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        space = []
        for i in arr:
            if i == 0:
                space.extend([0, 0])
            else:
                space.append(i)
            if len(space) > len(arr):
                break
        arr[:] = space[:len(arr)]
        