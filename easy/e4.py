#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:56:00 2018

@author: duh17
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_only = False
        count = {}
        for i in nums:
            if count.get(i) is None:
                count[i] = 1
            else :
                is_only = True
        return is_only
    

nums = [1, 2, 3, 4]
do = Solution()
print(do.containsDuplicate(nums))