class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        def is_rotation(block, seg):
            # seg ko block+block mein dhundhte hain, comma ke saath taaki alignment sahi rahe
            hay = "," + ",".join(map(str, block + block)) + ","
            needle = "," + ",".join(map(str, seg)) + ","
            return needle in hay

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            for start in range(0, n, k):
                block = nums[start:start + k]
                seg = sorted_nums[start:start + k]
                if not is_rotation(block, seg):
                    ok = False
                    break
            if ok:
                total += k

        return total