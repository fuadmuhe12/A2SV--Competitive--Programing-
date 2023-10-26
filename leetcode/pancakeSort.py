class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        track = len(arr) - 1
        cur = len(arr)
        answer = []
        while track > 0:
            x = arr.index(cur)
            if x == track:
                track -= 1
                cur -= 1
            else:
                arr[:x+1] = arr[:x + 1][::-1]
                answer.append(x +1)
                arr[:track + 1] = arr[:track + 1][::-1]
                answer.append(track +1)
                track -= 1
                cur -= 1
        return answer

            
