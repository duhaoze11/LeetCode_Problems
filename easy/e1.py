#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:35:04 2018

@author: duh17
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = []
        cnt = nums.copy()
        old = cnt[0]
        nums.clear()
        nums.append(old)
        for i in cnt :
            if i == old :
                continue
            else :
                old = i
                nums.append(old)
        
        
        return len(nums)
        
        
#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
do = Solution()
print(do.removeDuplicates(nums))
print(nums)