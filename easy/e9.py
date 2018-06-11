#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:04:45 2018

@author: duh17
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j = j + 1

nums = [2, 7, 11, 15]
target = 18
do = Solution()
print(do.twoSum(nums, target))
