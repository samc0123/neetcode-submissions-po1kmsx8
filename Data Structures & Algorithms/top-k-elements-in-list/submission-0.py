from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        res = count.most_common(k)
        res_arr = []
        for pair in res:
            res_arr.append(pair[0])
        
        return res_arr

        