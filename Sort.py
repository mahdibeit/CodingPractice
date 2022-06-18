# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:51:01 2022

@author: Mahdi
"""

def RadixSort(array:list) -> list:
    
    max_len_pos=array.index(max(array))
    array=list(map(str, array))
    max_len=len(array[max_len_pos])
    
    for i in range(max_len):
        h_map={}
        for number in array:
            digit= int(number[-i-1]) if i< len(number) else 0
            h_map[digit]=h_map[digit]+[number] if digit in h_map else [number]
    
        temp=0
        for i in range(10):
            if i in h_map:
                for number in h_map[i]:
                    array[temp]=number
                    temp+=1
        
    return list(map(int,array))

if __name__=='__main__':
    array=[100,2244,32,4,15,6]

    sorted_array=RadixSort(array[:])
    print(sorted_array)
    
        
        