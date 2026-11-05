class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for val, f in freq.items():
            buckets[f].append(val)

        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for v in buckets[f]:
                res.append(v)
                if len(res) == k:
                    return res
        return res