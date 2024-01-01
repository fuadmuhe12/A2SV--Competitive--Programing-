class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        mx = 0
        proc = 0
        tast_start = 0
        task_end = 4
        tasks.sort(reverse = True)
        processorTime.sort()
        while proc < len(processorTime) and tast_start <len(tasks):
            mx =  max(mx,(processorTime[proc] + max(tasks[tast_start:task_end])) )
            proc += 1
            task_end += 4
            tast_start += 4
        return mx
