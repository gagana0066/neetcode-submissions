class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashset = set(nums)
        return len(Hashset) != len(nums)
        