class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-stone for stone in stones]
        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            y = -heapq.heappop(stoneHeap)
            x = -heapq.heappop(stoneHeap)
            if y != x:
                heapq.heappush(stoneHeap, -(y - x))
        
        return -stoneHeap[0] if len(stoneHeap) == 1 else 0
        