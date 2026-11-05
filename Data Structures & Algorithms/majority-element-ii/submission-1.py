class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1) Find up to two candidates
        cand1 = cand2 = None
        count1 = count2 = 0

        for x in nums:
            if cand1 == x:
                count1 += 1
            elif cand2 == x:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = x, 1
            elif count2 == 0:
                cand2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1

        # 2) Verify actual counts
        result = []
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > len(nums) // 3 and c not in result:
                result.append(c)

        return result