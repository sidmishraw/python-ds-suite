# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-08 19:59:41
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-08 23:16:27


__author__ = 'sidmishraw'

from trees.trees import BinarySearchTree

def main():
  b = BinarySearchTree()
  b.insert(10)
  b.insert(8)
  b.insert(11)
  b.insert(9)
  b.insert(7)
  print(b.in_order_traverse())
  print(b.pre_order_traverse())
  print(b.post_order_traverse())



if __name__ == '__main__':
  main()