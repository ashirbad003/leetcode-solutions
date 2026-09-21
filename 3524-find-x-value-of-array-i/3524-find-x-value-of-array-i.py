class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        cnt = [0] * k
        for a in nums:
            new = [0] * k
            for r in range(k):
                if cnt[r]:
                    new[(r * a) % k] += cnt[r]
            new[a % k] += 1
            cnt = new
            for r in range(k):
                res[r] += cnt[r]
        return res