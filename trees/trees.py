# trees.py
'This module contains the implementations of all the tree Data structures'


__author__ = 'sidmishraw'




class BinarySearchTree(object):
  'Implementation of the binary search tree'

  class __Node(object):
    'Node of the binary tree'

    def __init__(self, node_data = None, left_child = None, \
      right_child = None):
      'initialize the node with None values by default'
      self.__data = node_data
      self.__left_child = left_child
      self.__right_child = right_child

    @property
    def node_data(self):
      'The data at the node of the tree'
      return self.__data

    @node_data.setter
    def node_data(self, new_data):
      'setter for the data of the node'
      self.__data = new_data

    @property
    def left_child(self):
      'gets the left child of the node'
      return self.__left_child

    @left_child.setter
    def left_child(self, new_left_child):
      'sets the left child of the node'
      self.__left_child = new_left_child

    @property
    def right_child(self):
      'gets the right child of the node'
      return self.__right_child

    @right_child.setter
    def right_child(self, new_right_child):
      'sets the right child of the node'
      self.__right_child = new_right_child

  def __init__(self):
    'initializes the binary tree'
    self.__root = None
    self.__length = 0

  # Insertion into the Binary Tree
  def insert(self, new_value):
    'inserts the new value into the Binary Tree'
    if self.__length == 0:
      new_node = self.__Node(node_data = new_value, left_child = None,\
        right_child = None)
      self.__root = new_node
      return
    else:
      # TODO - implement the insertion at the required node satisfying
      # BST property.
      pass

  # Search value in the tree
  def search(self, value):
    'searches for the value in the tree, returns None if not found'
    pass

  # TODO - In - order Traversal
  # TODO - Post - order Traversal
  # TODO - Pre - order Traversal

  
  @property
  def length(self):
    'The length of the BST'
    return self.__length

  def __repr__(self):
    'String representation of the binary tree'
    pass


