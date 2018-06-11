#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:15:20 2018

@author: duh17
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        diff = [prices[i + 1] - prices[i] for i in range(len(prices)-1)]
        return sum([d if d > 0 else 0 for d in diff])

prices = [7, 1, 5, 3, 6, 4]
do = Solution()
print(do.maxProfit(prices))
#print(a)

        