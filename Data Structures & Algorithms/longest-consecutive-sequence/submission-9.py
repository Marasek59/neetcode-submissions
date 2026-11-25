class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        l = len(nums)
        o = 1
        m=1
        if l > 0:
            for i in range(l-1):
                t = (True if nums[i]+1 == nums[i+1] else False)
                if t:
                    m+=1
                else:
                    if m > o:
                        o = m
                    m=1
            if m > o:
                o = m
            return o

        else:
            return 0

