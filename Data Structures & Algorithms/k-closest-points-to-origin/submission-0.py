import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestHeap = []
        heapq.heapify(closestHeap)

        for point in points:
            distance = self.calcDistanceFromOrigin(point)
            heapq.heappush(closestHeap, (-distance, point))

            if len(closestHeap) > k:
                heapq.heappop(closestHeap)
        
        return [heapItem[1] for heapItem in closestHeap]


    def calcDistanceFromOrigin(self, point :List[int]) -> float:
        return math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
            