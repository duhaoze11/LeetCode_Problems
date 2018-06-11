#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:06:13 2018

@author: duh17
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x.bit_length() > 31 : return 0
        temp = -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        return 0 if temp.bit_length() > 31 else temp
        
x = 1534236469        
do = Solution()
print(do.reverse(x))