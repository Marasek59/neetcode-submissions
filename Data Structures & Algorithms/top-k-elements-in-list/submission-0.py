class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in nums:
            group.setdefault(i, []).append(i)
        r = list(group.values())
        nejdelsi = sorted(r, key=len, reverse=True)[:k]
        result = []
        for a in nejdelsi:
            result.append(a[0])
        return result