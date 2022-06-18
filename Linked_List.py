# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:53:14 2022

@author: Mahdi
"""

class Linked_list:
    def __init__(self, head):
        self.head=head
        

class Node():
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
        
def PrintVal(l_Link: Linked_list) -> None:
    head=l_Link.head
    
    def Traverse(node: Node):
        if node==None:
            return
        else:
            print(node.data)
            Traverse(node.next)
    Traverse(head)
    
def PrintVal2(l_Link: Linked_list) -> None:
    node= l_Link.head
    
    while node is not None:
        print(node.data)
        node=node.next
    
def ReverseLink(l_link: Linked_list) -> None:
    node=l_link.head
    
    previous_node=None
    while node is not None:
        true_next=node.next
        node.next=previous_node
        previous_node=node
        node=true_next

    l_link.head=previous_node
    return

def removeNthFromEnd(head, n: int):
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """
    right_pointer = head
    left_pointer = head
    
    for _ in range(n):
        right_pointer = right_pointer.next
        
    if not right_pointer:
        return head.next
    
    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    left_pointer.next = left_pointer.next.next
    return head
    
def swapPairs(head):
    """
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
    Example 2:
    
    Input: head = []
    Output: []
    Example 3:
    
    Input: head = [1]
    Output: [1]
    """
    
    if not head or not head.next: return head
    dummy = Node(0)
    dummy.next = head
    cur = dummy
    
    while cur.next and cur.next.next:
        a=cur.next
        b=cur.next.next
        c=cur.next.next.next 
        cur.next=b
        b.next=a
        a.next=c
        
        cur=a
    return dummy.next 
        
if __name__=="__main__":
    
    head_node=Node('Mon')
    linked_list=Linked_list(head_node)
    n1=Node('Tue')
    n2=Node('We')
    n3=Node('Th')
    head_node.next=n1
    n1.next=n2
    n2.next=n3
    
    PrintVal(linked_list)
    # PrintVal2(linked_list)
    # ReverseLink(linked_list)
    # PrintVal2(linked_list)
    swapPairs(head_node)
    PrintVal2(linked_list)
    
    