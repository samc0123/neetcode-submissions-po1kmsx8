class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums: 
            count[num] = count.get(num,0) + 1 
        # Sort by keys
        sorted_count = sorted(count.items(), key = lambda items: items[1])
        print(sorted_count)
        res = []

        while k > 0:
            res.append(sorted_count.pop()[0])
            k-=1
        return res