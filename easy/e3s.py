#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:24:31 2018

@author: duh17
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = -1
        count = {}
        for i in s:
            if count.get(i) == None:
                count[i] = 1
            else :
                count[i] = count[i] + 1
        
        for i in range(n):
            if count[s[i]] == 1 :
                res = i
                break
        
        return res
        
        
        
x = 'leetcode'
do = Solution()
print(do.firstUniqChar(x))