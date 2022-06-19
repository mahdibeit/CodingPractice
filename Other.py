# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:41:16 2022

@author: Mahdi
"""

def FindPrime(num:int)-> list:
    fac=[]
    for i in range(2, num+1):
        if num%i ==0:
                fac.append(i)
        if len(fac)> 1:
            return 
    return fac

def PrimeFac(num:int)-> list:
    fac=[]
    for i in range(2,num):
        if num%i ==0:
            if FindPrime(i) is not None:
                fac.append(i)
    return list(set(fac))

def primeFactors(n):
 
    c = 2
    while(n > 1):
 
        if(n % c == 0):
            print(c, end=" ")
            n = n / c
        else:
            c = c + 1
            
def reverse( x: int) -> int:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    
    Input: x = 123
    Output: 321
    """
    out = ""
    n = 1
    pos = True if x >= 0 else False
    
    x = abs(x)
    res = x / n
    while res >= 1:
        out += str(int(res % 10))
        n *= 10
        res = x // n
    
    out = int(out) if pos else -1 * int(out)
    return out

def isValidSudoku(board) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:
    
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    """
    
    dic_column = {} # (col, cell): None
    
    for row_n, row in enumerate(board):
        dic_row = {} # cell: None
        if row_n % 3 == 0:
             dic_box = {} # (box, cell): None
                
        for col, cell in enumerate(row):
            if cell != "." and cell in dic_row:
                return False
            else:
                dic_row[cell] = None
            
            box = col // 3
            if cell != "." and (box, cell) in dic_box:
                return False
            else:
                dic_box[(box, cell)] = None
                
            if cell != "." and (col, cell) in dic_column:
                return False
            else:
                dic_column[(col, cell)] = None
    return True

if __name__=="__main__":
    num=8
    print(PrimeFac(num))
    print(primeFactors(num))
    reverse(num)
        
            