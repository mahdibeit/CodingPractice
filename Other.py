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

if __name__=="__main__":
    num=8
    print(PrimeFac(num))
    print(primeFactors(num))
    reverse(num)
        
            