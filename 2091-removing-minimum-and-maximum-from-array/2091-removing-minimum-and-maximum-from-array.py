class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))   # index of minimum
        j = nums.index(max(nums))   # index of maximum
        
        if i > j:
            i, j = j, i  # ensure i < j
        
        # option 1: remove both from front
        from_front = j + 1
        # option 2: remove both from back
        from_back = n - i
        # option 3: remove one from front, one from back
        both_sides = (i + 1) + (n - j)
        
        return min(from_front, from_back, both_sides)