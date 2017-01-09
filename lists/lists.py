# lists.py
# Python_DS_Suite
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-08 23:34:40
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-08 23:34:48


'All list related DS implementations will go in here'

__author__ = 'sidmishraw'

# lists.py
class LinkedList(object):
  'Linked list implementation'

  class __Node(object):
    'Node of the linked list'

    def __init__(self, nodeData, nextNode = None):
      'initializes the node'
      self.__node_data = nodeData
      self.__next_node = nextNode

    @property
    def node_data(self):
      'fetches the data of the current node'
      return self.__node_data

    # Self note -- @property decorator makes a method to behave as 
    # an attribute rather than a method for the user.
    # @<property-name>.setter
    # @<property-name>.deleter are used to set and delete the values
    # respectively.
    @node_data.setter
    def node_data(self, nodeData):
      'setter for node_data property'
      self.__node_data = nodeData

    @node_data.deleter
    def node_data(self):
      'deletes the node, no data => no node:)'
      del self

    @property
    def next_node(self):
      'get the next node'
      return self.__next_node

    @next_node.setter
    def next_node(self, nextNode):
      'sets the next node'
      self.__next_node = nextNode

  def __init__(self):
    'initialize the linked list'
    self.__start_node = None
    self.__length = 0

  @property
  def start_node(self):
    'access the start node of the list'
    return self.__start_node

  @start_node.setter
  def start_node(self, new_node):
    'set the start node of the list to point to the new node'
    self.__start_node = new_node

  # INSERTION INTO THE LINKED LIST
  def insert(self, node_data, position = 1):
    'inserts the node at the beginning of the list by default'
    if position < 1:
      raise Exception('The list begins from 1 index position.')
    if self.__start_node == None and position == 1:
      # Access inner classes using self or cls, since they are
      # parts of the object/class as well.
      new_node = self.__Node(node_data, None)
      self.__start_node = new_node
      self.__length += 1
      return
    elif self.__start_node == None and position != 1:
      # last node(inserting at the end)
      self.__start_node = self.__Node(node_data, None)
      self.__length += 1
      return
    else:
      positonCounter = 1
      prev = None
      current = self.__start_node
      while current != None:
        if position == positonCounter:
          break
        prev = current
        current = current.next_node
        positonCounter += 1
      else:
        # last node(inserting at the end)
        prev.next_node = self.__Node(node_data, None)
        self.__length += 1
        return
      if positonCounter == 1:
        # insert at the beginning of the list
        self.__start_node = self.__Node(node_data, current)
        self.__length += 1
        return
      if None != current:
        prev.next_node = self.__Node(node_data, current)
        self.__length += 1
        return
      else:
        raise Exception('The list is too small to insert at the \
        required location: List Underflow')


  # NODE DELETION FROM THE LINKED LIST
  def delete_node(self, position):
    'deletes the node at the specified position'
    positonCounter = 1
    prev = None
    current = self.__start_node
    if position == 1:
      # deleting the first node
      self.__start_node = current.next_node
      del current
      self.__length -= 1
      return
    elif position == self.__length:
      # deleting the last node
      while current.next_node != None:
        prev = current
        current = current.next_node
      prev.next_node = None
      del current
      self.__length -= 1
      return
    else:
      # handle deletion in between
      while current.next_node != None:
        if positonCounter == position:
          prev.next_node = current.next_node
          del current
          self.__length -= 1
          return
        prev = current
        current = current.next_node
        positonCounter += 1

  # UPDATE NODE OF THE LINKED LIST
  def update_node(self, position, new_value):
    'updates the node at the specified position with the new value'
    positonCounter = 1
    current = self.__start_node
    while current != None:
      if positonCounter == position:
        current.node_data = new_value
        return
      current = current.next_node
      positonCounter += 1

  # READ NODE VALUE
  def read_node(self, position):
    'reads the value of the node at the particular position'
    positonCounter = 1
    current = self.__start_node
    while current != None:
      if positonCounter == position:
        return current.node_data
      current = current.next_node
      positonCounter += 1
    else:
      return None

  def __repr__(self):
    'str representation of LinkedList'
    current = self.__start_node
    repr_str = 'START ---> '
    while None != current:
      repr_str += '%s ---> ' % current.node_data
      current = current.next_node
    repr_str += 'END\n'
    return repr_str

  def __len__(self):
    'returns the length of the linked list'
    return self.__length

  def __iter__(self):
    'to conform to the iter protocol'
    return self

  def __next__(self):
    'generator for using the linked list in iterators'
    current = self.__start_node
    while current != None:
      yield current
      current = current.next_node


# Doubly linked list
class DoublyLinkedList(object):
  'Doubly linked list implementation'

  class __Node(object):
    'Node of the doubly linked list'

    def __init__(self, node_data, prev_node, next_node):
      'initializes the node of the doubly linked list'
      self.__node_data = node_data
      self.__prev_node = prev_node
      self.__next_node = next_node

    @property
    def node_data(self):
      'data at the node'
      return self.__node_data

    @node_data.setter
    def node_data(self, new_data):
      'setter for data of the node'
      self.__node_data = new_data

    @property
    def prev_node(self):
      'gets the previous node of this node'
      return self.__prev_node

    @prev_node.setter
    def prev_node(self, new_prev_node):
      'setter of the prev_node'
      self.__prev_node = new_prev_node

    @property
    def next_node(self):
      'gets the next node to this node'
      return self.__next_node

    @next_node.setter
    def next_node(self, new_next_node):
      'setter for the next_node'
      self.__next_node = new_next_node

  def __init__(self):
    'initializer for the doubly linked list'
    self.__start_node = None
    self.__length = 0

  @property
  def start_node(self):
    'getter for the start node of the doubly linked list'
    return self.__start_node

  @start_node.setter
  def start_node(self, new_start_node):
    'setter for the start node of the doubly linked list'
    self.__start_node = new_start_node


  def __len__(self):
    'returns the length of the doubly linked list'
    return self.__length

  @property
  def length(self):
    'gets the current length of the doubly linked list'
    return self.__length

  # CRUD operations on the doubly linked list
  # INSERTION (Create)
  def insert(self, node_data, position = 1):
    'inserts the data into the position specified (1 by default)'
    positonCounter = 1
    current = self.__start_node
    if position == 1 and self.__start_node == None:
      new_node = self.__Node(node_data, prev_node=None, next_node=None)
      self.__start_node = new_node
      self.__length += 1
      return
    elif position == 1 and self.__start_node != None:
      new_node = self.__Node(node_data, prev_node = None, \
        next_node = self.__start_node)
      current.prev_node = new_node
      self.__start_node = new_node
      self.__length += 1
      return
    else:
      prev = current
      while current != None:
        # loop will stop at the penultimate node of the doubly linked list
        if positonCounter == position:
          new_node = self.__Node(node_data, prev_node = current.prev_node,\
            next_node=current)
          if current.prev_node != None:
            current.prev_node.next_node = new_node
          current.prev_node = new_node
          current = new_node
          self.__length += 1
          return
        prev = current
        current = current.next_node
        positonCounter += 1
      else:
        # loop breaks to give the last node of the doubly linked list
        new_node = self.__Node(node_data, prev_node = prev, \
          next_node = None)
        prev.next_node = new_node
        current = new_node
        self.__length += 1
        return

  # UPDATE
  def update(self, new_data, position):
    'updates the node data at the specified position'
    positonCounter = 1
    current = self.__start_node
    while current.next_node != None:
      if positonCounter == position:
        current.node_data = new_data
        return
      current = current.next_node
      positonCounter += 1
    else:
      if position == self.__length:
        current.node_data = new_data
        return
      else:
        print('Nothing to update')

  # READ
  def read_node(self, position):
    'reads the data at the specified position of the doubly linked list'
    positonCounter = 1
    current = self.__start_node
    while current.next_node != None:
      if positonCounter == position:
        return current.node_data
      current = current.next_node
      positonCounter += 1
    else:
      if position == self.__length:
        return current.node_data

  # DELETE
  def delete_node(self, position):
    'deletes the node at the specified position of the doubly linked list'
    positionCounter = 1
    current = self.__start_node
    if position == 1:
      self.__start_node = current.next_node
      del current
      self.__length -= 1
      return
    while current.next_node != None:
      if positionCounter == position:
        prev_node = current.prev_node
        next_node = current.next_node
        if prev_node != None and next_node != None:
          prev_node.next_node = next_node
          next_node.prev_node = prev_node
          del current
          self.__length -= 1
          return
        elif next_node != None:
          next_node.prev_node = None
          del current
          self.__length -= 1
          return
      current = current.next_node
      positionCounter += 1
    else:
      if position == self.__length:
        prev_node = current.prev_node
        prev_node.next_node = None
        self.__length -= 1
        del current
        return

  def __repr__(self):
    'string representation of the doubly linked list'
    s = 'START ---> '
    current = self.__start_node
    while None != current:
      s += '%s <---> ' % current.node_data
      current = current.next_node
    s += 'END\n'
    return s





