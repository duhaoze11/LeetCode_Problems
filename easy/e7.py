#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 12:24:47 2018

@author: duh17
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits[-1] + 1
        digits[-1] = res % 10
        pos = -2
        while res > 9 :
            if pos < -len(digits) :
                break
            res = digits[pos]
            res = res + 1
            digits[pos] = res % 10
            pos = pos - 1
            
        if res == 10 :
            digits.insert(0, 1)
        return digits
    
digits = [9, 9, 9]    
do = Solution()
print(do.plusOne(digits))