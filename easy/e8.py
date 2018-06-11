#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:04:45 2018

@author: duh17
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        temp = nums.copy()
        for i in temp:
            if i == 0:
                count = count + 1
                nums.remove(0)
        for i in range(count):
            nums.append(0)

nums = [0, 0, 1]
do = Solution()
do.moveZeroes(nums)
print(nums)