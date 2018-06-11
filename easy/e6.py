#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 12:18:51 2018

@author: duh17
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        res = []
        for i in nums1:
            if count.get(i) == None:
                count[i] = 1
            else:
                count[i] = count[i] + 1
        
        for i in nums2:
            if count.get(i) == None:
                continue
            elif count[i] > 0:
                count[i] = count[i] - 1
                res.append(i)
            
        return res

do = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(do.intersect(nums1, nums2))