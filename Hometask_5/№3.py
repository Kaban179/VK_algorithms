import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        i = 0

        while len(heap) < k:
            heapq.heappush(heap, nums[i])
            i += 1

        while i < len(nums):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])

            i += 1

        return heap[0]

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
    
        while len(heap) < k:
            heapq.heappush(heap, -nums[i])
            i += 1
    
        while i < len(nums):
            if nums[i] < -heap[0]:
                heapq.heapreplace(heap, -nums[i])
            i += 1
    
        return -heap[0]

# Для K-го наибольшего используем min-heap размером K.
# Храним K самых больших элементов, заменяя минимум при необходимости.
# В конце минимальный элемент кучи является K-м наибольшим.
# Аналогично для к наименьших
