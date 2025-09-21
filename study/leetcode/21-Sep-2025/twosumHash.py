# Leet code two sum problem = https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contheap={}

        for index,value in enumerate (nums):
            middlevalue = target - value 
            
            if middlevalue in contheap:

                return [contheap[middlevalue],index]

            contheap[value] = index
        return[]
    

solver = Solution()


input_nums = [2, 7, 11, 15]
input_target = 9

result = solver.twoSum(input_nums, input_target)


print(result)