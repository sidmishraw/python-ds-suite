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

    # The insert should be called on the node
    # the node takes the responsibility of inserting the incoming
    # data value into the appropriate place
    def insert(self, incoming_new_value):
      'inserts the incoming value at the appropriate position or delegates\
      to it\'s children'
      if incoming_new_value <= self.__data:
        # incoming value belongs to the left subtree
        if self.__left_child == None:
          # if the node doesn't have a left child, the incoming value
          # becomes that child
          self.__left_child = self.__class__(node_data = incoming_new_value, \
            left_child = None, right_child = None)
          return
        else:
          # delegate to the existing left child
          return self.__left_child.insert(incoming_new_value)
      else:
        # incoming value belongs to the right subtree
        if self.__right_child == None:
          # didn't have a right child, so make a right child
          self.__right_child = self.__class__(node_data = incoming_new_value, \
            left_child = None, right_child = None)
          return
        else:
          # delegate it to the right subchild
          return self.__right_child.insert(incoming_new_value)

    # searches for the value checks if the node has that value, if not
    # delegates the task to it's children
    def search(self, value):
      'searches for the value, returns true if the value is found at the node\
      else delegates the search to the children(sub-tree)'
      # print('current node data = %s' % self.__data)
      if self.__data == value:
        return True
      elif self.__data > value:
        if self.__left_child == None:
          return False
        else:
          return self.__left_child.search(value)
      elif self.__data < value:
        if self.__right_child == None:
          return False
        else:
          return self.__right_child.search(value)

    # Traverse the tree inorder
    # left-child first, then the node itself and then the right-child
    def in_order_traverse(self, tree_nodes):
      'traverses the nodes of the binary search tree - delegated tasks'
      # delegate to traverse left subtree it it exists
      if self.__left_child != None:
        self.__left_child.in_order_traverse(tree_nodes)
      # the node it self, root
      tree_nodes.append(self.__data)
      # delegate to traverse right subtree it it exists
      if self.__right_child != None:
        self.__right_child.in_order_traverse(tree_nodes)

    # Traverse the tree pre-order
    # root first and then delegate the stuff to left and then right subtrees
    # (children)
    def pre_order_traverse(self, tree_nodes):
      'traverses the nodes of the binary search tree - delegated tasks'
      # first the root itself
      # root
      tree_nodes.append(self.__data)
      # delegate the traversal to left child if it exists
      # left subtree
      if self.__left_child != None:
        self.left_child.pre_order_traverse(tree_nodes)
      # delegate the traversal to right child if it exists
      # right subtree
      if self.__right_child != None:
        self.__right_child.pre_order_traverse(tree_nodes)

    # Traverse the tree post_order
    # left, right and then the root at the end
    def post_order_traverse(self, tree_nodes):
      'traverses the nodes of the binary search tree - delegated tasks'
      # first the left subtree
      # delegate to child to traverse the left subtree, if it exists
      if self.__left_child != None:
        self.__left_child.post_order_traverse(tree_nodes)
      # delegate to child to traverse the right subtree, if it exists
      if self.__right_child != None:
        self.__right_child.post_order_traverse(tree_nodes)
      # finally the root (node itself)
      tree_nodes.append(self.__data)

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
      self.__length += 1
      return
    else:
      '''
      delegate the responsibility to insert at the appropriate location to
      the node itself. That way it will traverse down to it's appropriate 
      location on it's own.
      '''
      self.__root.insert(new_value)
      self.__length += 1
      return

  # Search value in the tree
  def search(self, value):
    'searches for the value in the tree, returns None if not found'
    # if value found at the root, return with true
    # else delegate it to the children based on it's comparision
    # less - left subtree
    # more - right subtree
    return self.__root.search(value)

  # TODO - In - order Traversal
  # first left subtree, then root and then the right subtree
  def in_order_traverse(self):
    'traverses the tree in IN_ORDER and generates the parsed tree string'
    tree_nodes = []
    self.__root.in_order_traverse(tree_nodes)
    tree_string = ' '.join(list(map(str, tree_nodes)))
    return tree_string

  # TODO - Post - order Traversal
  def post_order_traverse(self):
    'traverses the tree in PRE_ORDER and generates the parsed tree string'
    tree_nodes = []
    self.__root.post_order_traverse(tree_nodes)
    tree_string = ' '.join(list(map(str, tree_nodes)))
    return tree_string

  # TODO - Pre - order Traversal
  # first the root, then the left subtree and then the right subtree
  def pre_order_traverse(self):
    'traverses the tree in PRE_ORDER and generates the parsed tree string'
    tree_nodes = []
    self.__root.pre_order_traverse(tree_nodes)
    tree_string = ' '.join(list(map(str, tree_nodes)))
    return tree_string

  
  @property
  def length(self):
    'The length of the BST'
    return self.__length


