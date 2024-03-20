class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sep(left, right):
            if left -right == 0:
                return (left, right)
            else:
                mid = (left + right)//2
                leftArr = sep(left, mid)
                rightArr = sep(mid+1, right)
                up = merge(nums[leftArr[0]: leftArr[1]+1], nums[rightArr[0]:rightArr[1]+1])
                nums[left: right+1] = up
                return (left, right)

        def merge(arr1, arr2):
            new = []
            ind = 0
            p2 = 0
            while ind < len(arr1) and p2 < len(arr2):
                if  arr1[ind] <= arr2[p2]:
                    new.append(arr1[ind])
                    ind += 1
                else:
                    new.append(arr2[p2])
                    p2 += 1
            new.extend(arr2[p2:])
            new.extend(arr1[ind:])
            return new           
        sep(0, len(nums)-1)
        return nums

