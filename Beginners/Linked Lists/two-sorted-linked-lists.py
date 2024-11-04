#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    head = SinglyLinkedListNode(-1)
    curr = head
    i, j = head1, head2
    
    while i and j:
        if i.data < j.data:
            curr.next = SinglyLinkedListNode(i.data)
            i = i.next
        else:
            curr.next = SinglyLinkedListNode(j.data)
            j = j.next
        curr = curr.next
        
    while i:
        curr.next = SinglyLinkedListNode(i.data)
        i = i.next
        curr = curr.next
    while j:
        curr.next = SinglyLinkedListNode(j.data)
        j = j.next
        curr = curr.next        
        
    return head.next
