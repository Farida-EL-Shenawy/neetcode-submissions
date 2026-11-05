class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:       # duplicate found
                return True
            seen.add(x)         # first time seeing x
        return False