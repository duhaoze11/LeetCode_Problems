#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:04:45 2018

@author: duh17
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = True
        n = len(board)
        # process row
        for i in board :
            temp = {}
            for j in i :
                if j != '.' :
                    if temp.get(j) == None :
                        temp[j] = 1
                    else :
                        res = False
        
        # process column
        for j in range(n) :
            temp = {}
            for i in range(n) :
                cur = board[i][j]
                if cur != '.' :
                    if temp.get(cur) == None :
                        temp[cur] = 1
                    else :
                        res = False
                        
        # process each 3 * 3
        # i = 3 * x + ii
        # j = 3 * y + jj
        for x in range(3):
            for y in range(3):
                temp = {}
                for ii in range(3):
                    for jj in range(3):
                        i = 3*x + ii
                        j = 3*y + jj
                        cur = board[i][j]
                        if cur != '.' :
                            if temp.get(cur) == None :
                                temp[cur] = 1
                            else :
                                res = False
#                                print(x, y, cur, temp)
        
        return res
    
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

do = Solution()
print(do.isValidSudoku(board))
