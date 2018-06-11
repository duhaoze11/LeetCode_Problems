#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:41:23 2018

@author: duh17
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        temp2 = nums[:n-k].copy()
        temp1 = nums[n-k:].copy()
        temp1.extend(temp2)
        nums.clear()
        nums.extend(temp1)
        return
    
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

do = Solution()
do.rotate(nums, k)
print(nums)