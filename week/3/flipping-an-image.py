class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        '''
        1. start = 0
        end = len(image)-1
        
        '''
        # ans = []
        for i in image:
            start = 0
            end = len(i)-1
            while end >= start:
                if i[end] == 1:
                    i[end] = 0
                else:
                    i[end] =1
                if len(image)%2 == 0 or start != end:
                    if i[start] == 1:
                        i[start] = 0
                    else:
                        i[start] =1
                i[start] , i[end] = i[end], i[start]
                start +=1
                end -= 1
            
            # ans.append(i)
        return image
