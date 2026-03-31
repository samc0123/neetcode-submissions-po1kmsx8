class Solution:
    def do_binary_search(self,nums:list[int],target:int):
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = int((l+r)/2)
            if nums[m] == target:
                break
            elif nums[m] > target:
                r = m - 1 # search left side 
            elif nums[m] < target: 
                l = m+1 # search right side
        return m
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p_top_col = 0
        p_bot_col = len(matrix) - 1

        while p_top_col <= p_bot_col:
            # Get the middle column 
            p_mid_col = int((p_top_col+p_bot_col)/2)
            v_mid_col_first = matrix[p_mid_col][0]
            if  v_mid_col_first == target:
                return True
            elif v_mid_col_first > target:
                # Move bottom col pointer below mid col
                p_bot_col = p_mid_col - 1
            elif v_mid_col_first < target:
                row_to_search = matrix[p_mid_col]
                found_index = self.do_binary_search(row_to_search,target)
                if row_to_search[found_index] == target:
                    return True
                p_top_col = p_mid_col + 1
        return False



