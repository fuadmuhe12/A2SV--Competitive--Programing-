class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        1.  set for deleted
        start m at 0
        2. while loop when set < n-1 
        3. start if val not in visted and not m not equl to k m++
        4. 
        '''
        visited = set()
        m  = 0
        a  =list(range(1,n+1))
        ind = 0
        while len(visited) < n-1:
            if a[ind % n] not in visited and m != k:
                m +=1 
            if a[ind % n] not in visited and m == k:
                m = 0
                visited.add( a[ind % n])
            ind += 1
        for i in a :
            if i not in visited :
                return i
         



