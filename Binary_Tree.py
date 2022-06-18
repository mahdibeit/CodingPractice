# -*- coding: utf-8 -*-
"""
Created on Thu May 12 23:31:53 2022

@author: Mahdi
"""

class Node():
    def __init__(self, data, left, right):
        self.data=data
        self.left=left
        self.right=right 
        


def FindHeight(node):
    
    if node is not None:
        return 1+max(FindHeight(node.left), FindHeight(node.right))
    else:
        return 0
    
def TraverseWithoutRecursion_PreOrder(Tree):
    node=Tree
    node_list=[] 
    while node is not None:
        print(node.data, end=' ')
        if node.right is not None:
            node_list.append(node.right)
        if node.left is not None:
            node=node.left
        else:
            if node_list:   
                node=node_list[-1]
                node_list.remove(node)
            else:
                node=None
                
def TraverseWithoutRecursion_PreOrder_better(Tree):
    node_stack=[]
    node_stack.append(Tree)
    
    while node_stack:
        node=node_stack.pop()
        print(node.data, end=' ')
        
        if node.right is not None:
            node_stack.append(node.right)
        
        if node.left is not None:
            node_stack.append(node.left)
                    
def TraverseInOrder_NoRecursion(node):

    node_stack=[]
    
    while True:
        if node is not None:
                node_stack.append(node)
                node=node.left
        elif(node_stack):
            node=node_stack.pop()
            print(node.data, end=' ')
            node=node.right
        else:
            break
        
def BreadthSearch(node):
    
    stack=[]
    stack.append(node)
    
    while stack:
        node=stack.pop()
        print(node.data, end=" ")
        
        if node.right is not None:
            stack.append(node.right)
        
        if node.left is not None:
            stack.append(node.left)


if __name__=="__main__":
    Tree= Node(2,Node(3, Node(1, None, None), None),Node(4, None, None))
     
    print(FindHeight(Tree))
    TraverseWithoutRecursion_PreOrder(Tree)
    print()
    TraverseWithoutRecursion_PreOrder_better(Tree)
    
    print()
    TraverseInOrder_NoRecursion(Tree)
    
    print()
    print('Breadth Search')
    BreadthSearch(Tree)
        
    