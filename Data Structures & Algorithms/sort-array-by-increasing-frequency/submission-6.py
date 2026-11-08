class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count: 
                count[num] += 1 
            else:
                count[num] = 1 
        result = []
        for freq in range(1,len(nums) + 1):
            group = []
            for num in count:
                if count[num] == freq:
                    group.append(num)
            group.sort(reverse=True)
            for num in group:
                for j in range(freq):
                    result.append(num)
        return result
