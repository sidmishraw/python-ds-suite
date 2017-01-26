# linkedlist_examples.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-17 16:01:06
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-17 17:46:14

# importing my custom built LinkedList ADT
from lists.lists import LinkedList

# using python's debugger
import pdb


# if __name__ == '__main__':


#   l1 = LinkedList()

#   l1.insert(1)
#   l1.insert(2)
#   l1.insert(3)
#   l1.insert(4)
#   l1.insert(5)

#   l2 = LinkedList()

#   l2.insert(6)
#   l2.insert(7)

#   currentl1node = l1.start_node

#   for _ in range(0,3,1):
#     currentl1node = currentl1node.next_node
  
#   node = l2.start_node

#   while node.next_node != None:
#     node = node.next_node

#   # This makes the intersection of the linkedlists
#   node.next_node = currentl1node

#   print(l1)
#   print(l2)

#   # now that the setup is done, I can begin implementing the
#   # algorithm

#   # step 1 - find the longer linkedlist and prune the extra nodes
#   currentl1 = l1.start_node
#   currentl2 = l2.start_node
#   len_l1 = 0
#   len_l2 = 0

#   while currentl1 != None:
#     len_l1 += 1
#     currentl1 = currentl1.next_node

#   while currentl2 != None:
#     len_l2 += 1
#     currentl2 = currentl2.next_node

#   if len_l1 > len_l2:
    
#     # prune l1's extra nodes from the beginning, since
#     # the nbr of nodes after intersection is same for both
#     # the lists

#     currentl1 = l1.start_node

#     for _ in range(0, len_l1 - len_l2, 1):
#       currentl1 = currentl1.next_node

#     # we have skipped the extra nodes

#     currentl2 = l2.start_node

#     while currentl1 != None:

#       if currentl1 == currentl2:
#         print(currentl1.node_data)
#         break

#       currentl1 = currentl1.next_node
#       currentl2 = currentl2.next_node

#   elif len_l1 < len_l2:
    
#     # prune l2's extra nodes from the beginning, since
#     # the nbr of nodes after intersection is same for both
#     # the lists

#     currentl2 = l2.start_node

#     for _ in range(0, len_l2 - len_l1, 1):
#       currentl2 = currentl2.next_node

#     # we have skipped the extra nodes

#     currentl1 = l1.start_node

#     while currentl1 != None:

#       if currentl1 == currentl2:
#         print(currentl1.node_data)
#         break

#       currentl1 = currentl1.next_node
#       currentl2 = currentl2.next_node
#   else:
    
#     currentl1 = l1.start_node
#     currentl2 = l2.start_node

#     while currentl1 != None:

#       if currentl1 == currentl2:
#         print(currentl1.node_data)
#         break

#       currentl1 = currentl1.next_node
#       currentl2 = currentl2.next_node


if __name__ == '__main__':

  l1 = LinkedList()

  l1.insert(2)
  l1.insert(9)
  l1.insert(5)
  

  l2 = LinkedList()

  l2.insert(6)
  l2.insert(6)
  l2.insert(6)
  l2.insert(1)
  l2.insert(7)
  

  # the digits of the nbr are stored backwards
  # start from one's place

  node1 = l1.start_node
  node2 = l2.start_node

  # I didn't plan on using the linkedlist as this
  # but since I need a customized operation on the linkedlist
  # I'll have to deal with Python's namewrangling.

  new_node = LinkedList._LinkedList__Node(0, None)

  start_new_node = new_node

  pdb.set_trace()

  while node1 != None and node2 != None:

    sum_initial = (node1.node_data + node2.node_data + new_node.node_data)
    ones_digit =  sum_initial % 10
    carry_digit = sum_initial // 10

    new_node.node_data = ones_digit

    new_node.next_node = LinkedList._LinkedList__Node(carry_digit \
      if carry_digit else None, None) \
      if node1.next_node != None and node2.next_node != None else None

    node1 = node1.next_node
    node2 = node2.next_node
    new_node = new_node.next_node

  if node1 == None and node2 != None:

    while node2 != None:

      new_node.node_data = node2.node_data
      new_node.next_node = LinkedList._LinkedList__Node(None, None) \
        if node2.next_node != None else None

      new_node = new_node.next_node
      node2 = node2.next_node
  elif node1 != None and node2 == None:

    while node1 != None:

      new_node.node_data = node1.node_data
      new_node.next_node = LinkedList._LinkedList__Node(None, None)

      new_node = new_node.next_node
      node1 = node1.next_node











