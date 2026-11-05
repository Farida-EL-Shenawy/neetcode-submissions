class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(heap_size: int, i: int) -> None:
            # sift-down from index i within [0, heap_size)
            while True:
                largest = i
                left = 2*i + 1
                right = 2*i + 2

                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        # 1) Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # 2) Extract max to the end, shrink heap, and fix
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]  # move current max to correct spot
            heapify(end, 0)

        return nums
