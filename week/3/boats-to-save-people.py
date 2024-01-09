class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) -1
        bot = 0
        while end >= start:
            if people[end] + people[start] <= limit:
                bot += 1
                end -= 1
                start += 1
            else:
                bot +=1
                end -= 1
        return bot


