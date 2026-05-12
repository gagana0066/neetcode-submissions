class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            number = target - n

            if number in hashMap:
                return [hashMap[number], i]

            hashMap[n] = i