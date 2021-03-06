# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:23:09 2022

@author: Mahdi
"""

def DuplicateNumber(num_list: list) -> list:
    
    hMap={} #value:repeat
    dupList=[]
    
    for num in num_list:
        if num in hMap:
            hMap[num]+=1
            if hMap[num] == 2:
                dupList.append(num)
        else:
            hMap[num]=1
    
    return dupList

def RemoveDuplicate(num_list: list)-> list:
    h_map={} #value:None
    non_dup=[]
    
    for num in num_list:
        if num not in h_map:
            non_dup.append(num)
            h_map[num]=None
    return non_dup

def BalanceIntList(int_lst:list)-> dict:
    """Given a list of ints, balance the list so that each int appears equally in the list.
    Return a dictionary where the key is the int and the value is the count needed to balance the list.
    [1, 1, 2] => {2: 1}
    [1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}
    
    """
    h_map={} #digit:repeat
    max_repeat=0
    for num in int_lst:
        h_map.setdefault(num, 0)
        h_map[num]+= 1 
        if h_map[num]> max_repeat:
            max_repeat=h_map[num]
    
    h_map_out={}
    for num in h_map:
        if h_map[num]< max_repeat:
            h_map_out[num]=max_repeat-h_map[num]
    return h_map_out


def are_they_equal(array_a, array_b):
  # Write your code here
  """Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing
      any subarrays from array B any number of times."""
  a_map={}
  b_map={}

  for a, b in zip(array_a, array_b):
    a_map.setdefault(a, 0)
    a_map[a]+=1
    
    b_map.setdefault(b, 0)
    b_map[b]+=1
  
  if b_map != a_map:
    return False
  else:
    return True




def findSignatureCounts(arr):
    """
    You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
    Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
    
    n = 2
    arr = [2, 1]
    output = [2, 2]
    
    """   
    output=[1]*len(arr)

    counter=0
    while counter!=len(arr):
      new_arr=arr[:]
      counter=0
      for idx, i in enumerate(arr):
        if i!=arr[i-1]:
          new_arr[idx]=arr[i-1]
          output[idx]+=1
        else:
          counter+=1
      arr=new_arr[:]
    return output
        

def count_subarrays(arr):
  """
  Cound subarrays such that each index i is the maximum of the subarray and the subarray starts or ends at index i
  
  
  """
  
  output=[0]*len(arr)
  
  for idx, num in enumerate(arr):
    
    if idx<len(arr):
      right_idx=idx+1
      while num>= max(arr[idx:right_idx]):
        output[idx]+=1
        right_idx+=1
        if right_idx> len(arr):
          break
      
    if idx>0:  
      left_idx=idx-1
      while num>= max(arr[left_idx:idx]):
        output[idx]+=1
        left_idx-=1
        if left_idx< 0:
          break
  return output

def maxArea( height) -> int:
    """
    Container With Most Water
    
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
    
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    
    """
    maxArea = 0
    l, r = 0, len(height) - 1
    
    while r > l:
        newArea = min(height[r], height[l]) * (r - l)
        if newArea > maxArea:
            maxArea = newArea
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
        
    return maxArea

def threeSum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    
    """
    output = []
    nums.sort(reverse = True)
    
    for idx, num in enumerate(nums):
        if idx > 0 and num == nums[idx-1]:
            continue

        l, r = idx + 1, len(nums) - 1     
        while (l < r):
            threeSum = nums[l] + nums[r] + num
            if threeSum == 0:
                output.append([num, nums[l], nums[r]])
                l += 1
                while nums[l-1] == nums[l] and l < r:
                    l +=1
            elif threeSum > 0:
                l += 1
            else:
                r -= 1
    return output

def generateParenthesis(n: int):
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:
    
    Input: n = 1
    Output: ["()"]
    """
    output = []
    
    def AddP(subString: str, numO: int, numC: int):
        
        if numO > 0:
            AddP(subString + "(", numO - 1, numC)
        
        if numC > 0 and numO < numC:
            AddP(subString + ")", numO, numC - 1)
            
        if numO == 0 and numC == 0:
            output.append(subString)
    
    AddP("(", n-1, n)
    return output

def nextPermutation( nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

        For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
        The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
        
        For example, the next permutation of arr = [1,2,3] is [1,3,2].
        Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
        While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
        """
        i = j = len(nums) - 1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        i -= 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

def search(nums, target: int) -> int:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    
    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    
    You must write an algorithm with O(log n) runtime complexity.
    
    """
        
    if not nums:
        return -1
    
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1           
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1

def searchRange(nums, target: int):
    """
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    
    You must write an algorithm with O(log n) runtime complexity.
    
    Example 1:
    
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
    """
    if not nums:
        return [-1, -1]
    
    l, r = 0, len(nums) - 1
    while (l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            i = j = mid 
            while i >= 1 and nums[i - 1] == target:
                i -= 1
            while j <= len(nums)-2 and nums[j + 1] == target:
                j += 1
            return [i, j]
        
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return [-1, -1]

def combinationSum(self, candidates, target: int):
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
    
    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

    Example 1:
    
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    
    """
    out = []
    
    def Remainder(canList, target, subOut):
        for can in canList:
            if can == target:
                out.append(subOut + [can])
            else:
                newCanList = [i for i in canList if i <= target - can and i >= can]
                if newCanList:
                    Remainder(newCanList, target - can, subOut + [can])
                
    Remainder([i for i in candidates if i <= target], target, [])
    
    return out

def combinationSum2(self, candidates, target: int):
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.
    
    Note: The solution set must not contain duplicate combinations.
    
    Example 1:
    
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]
    
    """
    out = []
    dup = {} # can: duplicate
    for can in candidates: 
        dup.setdefault(can, 0)
        dup[can] += 1
    
    candidates = list(set(candidates))
    def Remainder(canList, target, subOut, dup):
        for can in canList:
            if can == target:
                out.append(subOut + [can])
            else:
                
                if dup[can] != 1:
                    newCanList = [i for i in canList if i <= target - can and i >= can]
                    dup[can] -= 1
                else:
                    newCanList = [i for i in canList if i <= target - can and i >= can and i != can]
                if newCanList:
                    Remainder(newCanList, target - can, subOut + [can], dup.copy())
            
    Remainder([i for i in candidates if i <= target], target, [], dup.copy())

    return out


def jump(nums) -> int:
    """
    Given an array of non-negative integers nums, you are initially positioned
    at the first index of the array.
    Each element in the array represents your maximum jump length at that
    position.
    Your goal is to reach the last index in the minimum number of jumps.
    You can assume that you can always reach the last index.

    Example 1:

    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
    """
    totalJumps = 0
    idx = 0
    while (idx < len(nums) - 1):
        if idx + nums[idx] >= len(nums) - 1:
            totalJumps += 1
            break
        max_idx = 0
        for step, next_j in enumerate(nums[idx+1: idx + nums[idx] + 1]):
            if step + next_j > max_idx:
                max_idx = step + next_j
                next_idx = idx + step + 1
        idx = next_idx
        totalJumps += 1

    return totalJumps


def permute(nums):
    """
    Given an array nums of distinct integers, return all the possible
    permutations. You can return the answer in any order.

    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    out = []

    def perm(subList):
        if len(subList) != len(nums):
            for digit in nums:
                if digit not in subList:
                    perm(subList + [digit])
        else:
            out.append(subList)

    perm([])
    return out
                
                

if __name__=="__main__":
    sample=[1,2,9, 3,3,4,5,6,6,7,8,9,1,3,3]
    
    print(DuplicateNumber(sample))
    print(RemoveDuplicate(sample))  
    print(BalanceIntList(sample))
    print(count_subarrays(sample))