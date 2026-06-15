import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countsMap = defaultdict(int)
        for num in nums:
            countsMap[num] += 1
        
        heap = []
        
        for key, value in countsMap.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
            

        return [heapItem[1] for heapItem in heap]



        