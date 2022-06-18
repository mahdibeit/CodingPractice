# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:54:47 2022

@author: Mahdi
"""


def IsDuplicate(sentence: str ) -> bool:
    """O(n)"""
    hashMap={} #char: none
    
    for char in sentence:
        if char in hashMap:
            return True
        else: 
            hashMap[char]=None
    else:

        return False
    

def IsDuplicateForce(sentence:str) -> bool:
    
    for indx, char in enumerate (sentence):
        for otherChar in sentence[indx+1:]:
            if char==otherChar:
                return True
    else:
        return False
            
def FirstNonRepeatChar(sentence:str) -> str:
    
    hMap={} #value:(index,repeat)
    for index, char in enumerate(sentence):
        hMap.setdefault(char, (index,0))
        hMap[char]=(hMap[char][0],hMap[char][1]+1)

    
    for char in hMap:
        if hMap[char][1]==1:
            return char
        


def rotationalCipher(input, rotation_factor):

  """  One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
  For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
  Given a string and a rotation factor, return an encrypted string.
  """
  
  
  AZ="abcdefghijklmnopqrstuvwxyz"
  numeric_char ="0123456789"
  
  output=""
  for char in input:
    if char.casefold() in AZ:
      position=(AZ.index(char.casefold())+rotation_factor)%len(AZ)
      if char.isupper():
          output+=AZ[position].upper()
      else:
          
          output+=AZ[position]
      
    elif char in numeric_char:
      position=(numeric_char.index(char)+rotation_factor)%len(numeric_char)
      output+=numeric_char[position]
    
    else:
      output+=char
      
  return output

def lengthOfLongestSubstring( s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """
    
    best_str=""
    local_str=""
    
    for char in s:
        if char in local_str:
            local_str=local_str.split(char)[1]
            
        local_str+= char

        if len(local_str)> len(best_str):
            best_str=local_str
            
    return len(best_str)
    
def longestPalindrome(self, s: str) -> str:
    best_l = 0
    best_r = 0
    length = len(s)
    
    if length <= 1:
        return s
    
    for idx in range(length):
        # for odd palindrome
        l, r = idx, idx 
        while l >= 0 and r < length and s[l] == s[r]:
            if r - l + 1 > best_r - best_l + 1:
                best_r = r
                best_l = l

            l -= 1
            r += 1
            
        # for even 
        l, r = idx, idx + 1
        while l >= 0 and r < length and s[l] == s[r]:
            if r - l + 1 > best_r - best_l + 1:
                best_r = r
                best_l = l
            l -= 1
            r += 1
    
    return s[best_l: best_r+1]

def convert(self, s: str, numRows: int) -> str:
    """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
        
        P   A   H   N
        A P L S I I G
        Y   I   R
        
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
    
    """


    zig = ""
    
    if numRows == 1:
        return s
    
    for n in range (numRows):
        if n < len(s):
            zig += s[n]
            idx=n
            while True:
                shift = 2 * (numRows - (n + 1))
                idx += shift
                if  shift != 0 and idx < len(s):
                    zig += s[idx]

                shift = 2 * n
                idx += shift
                if  shift != 0 and idx < len(s):
                    zig += s[idx]

                if idx >= len(s):
                    break
                
    return zig

def convert2(self, s: str, numRows: int) -> str:
    arr = ["" for _ in range(numRows)]
    zig = ""
    row = 0
    down = True 
    
    if numRows == 1:
        return s
    
    for idx, char in enumerate(s):
        arr[row] += char
        
        if row == numRows -1:
            row -= 1
            down = not down
            
        elif row == 0:
            row += 1
            down = not down
            
        elif down:
            row -= 1
            
        else:
            row += 1
    
    for i in range(numRows):
        zig += arr[i]

    return zig
                
def letterCombinations(digits: str):
    """
    17. Letter Combinations of a Phone Number
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    """



    dic_map = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"],
        '5': ['j', 'k' , 'l'], '6': ['m', "n", "o"], '7': ["p", "q", "r", "s"], 
        '8': ['t', 'u' , 'v'], '9': ['w', 'x', 'y', 'z']}
    output = []

    def addDigit(tempStr, digits):
        for num in dic_map[digits[0]]:
            if len(digits) >= 2:
                addDigit(tempStr + num, digits[1:])
            else:
                output.append(tempStr + num)
                
    if digits !=     "":
        addDigit("", digits)

    return output

    
if __name__=="__main__":
    sample="My Name Is Mahdi"
    print(IsDuplicate(sample))
    print(IsDuplicateForce(sample))
    print(FirstNonRepeatChar(sample))
    print(rotationalCipher(sample,5))
    


    