'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' O(n^2) / O(?) '''
        def twoSum(subnums: List[int], k: int) -> List[List[int]]:
            '''
            Find all tuples in subnums which gives the sum of k
            subnums is sorted by ascending order
            '''
            answer = []
            idx1 = 0
            idx2 = len(subnums) - 1
            while idx1 < idx2:
                x = subnums[idx1]
                y = subnums[idx2]  # x <= y
                if x + y > k:
                    idx2 -= 1   # "decrease" y
                elif x + y == k:
                    if idx1 + 1 < idx2:
                        if subnums[idx1 + 1] == x:  # move to the "last" x in subnums
                            idx1 += 1
                        elif subnums[idx2 - 1] == y:    # move to the "first" y in subnums
                            idx2 -= 1                  
                        else:
                            answer.append([x, y])
                            idx1 += 1
                            idx2 -= 1
                    else: # idx1 + 1 == idx2
                        answer.append([x, y])
                        break
                else:   # if x + y < k, "increase" x
                    idx1 += 1
            return answer
        
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            x = nums[i]
            if i > 0 and nums[i-1] == x:
                continue
            sum_neg_x = twoSum(nums[i+1: ], -x)
            for t in sum_neg_x:
                triplets.append([x]+t)         
        return triplets
