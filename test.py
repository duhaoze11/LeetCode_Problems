#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:30:38 2018

@author: duh17
"""
import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '' : return 0
        if str.split() == [] : return 0
        
        intmax = 2147483647
        intmin = -2147483648
        
        ch = re.search('\S', str).group()
        if ch != '-' or ch.isdigit : return 0
        nums = re.search('(-)?(\d)+', str).group()
        n = int(nums)
        if n > intmax : return intmax
        if n < intmin : return intmin
        return n
        
        
s = "   -42"
do = Solution()
print(do.myAtoi(s))