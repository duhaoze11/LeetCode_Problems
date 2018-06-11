#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:48:25 2018

@author: duh17
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
do = Solution()
do.rotate(matrix)
print(matrix)