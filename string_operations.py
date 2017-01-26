# string_operations.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-18 11:00:10
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-19 00:09:45


def permute(arr, l, r):
  if l >= r:
    print(''.join(arr))

  for i in range(l, r, 1):
    # fix a[i] as the a[l] and permute l+1 to r
    arr[l], arr[i] = arr[i], arr[l]
    # permute
    permute(arr, l+1, r)
    # backtrack to original configuration
    arr[l], arr[i] = arr[i], arr[l]

def permute_string(string):
  permute(list(string), 0, len(string))






  # kid is hopping 1, 2 or 3 steps at a time
  # total steps - n in stairs
  # how many ways can be done?
  # similar to problem asking sum of lenghts of rods etc

  # a.1 + b.2 + c.3 = n
  # n = 10
  # 1.1 + 0.2 + 3.3 = 10
  # 2.1 + 1.2 + 2.3 = 10
  # 3.1 + 2.2 + 1.3 = 10
  # 4.1 + 3.2 + 0.3 = 10
  # 0.1 + 2.2 + 2.3 = 10
  # 10.1 + 0.2 + 0.3 = 10

  # n = 5
  # 0.1 + 1.2 + 1.3 = 5
  # 1.1 + 2.2 + 0.3 = 5
  # 2.1 + 0.2 + 1.3 = 5
  # 3.1 + 1.2 + 0.3 = 5
  # 5.1 + 0.2 + 0.3 = 5

def count_ways(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

# using memoization for count_ways
# memory is initialized to [-1] * (n + 1) array
def count_ways_m(n, memory):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif (memory[n] > -1):
    return memory[n]
  else:
    memory[n] = count_ways_m(n - 1, memory) + \
    count_ways_m(n - 2, memory) + count_ways_m(n - 3, memory)
    return memory[n]


# Generic row and col, can be from any coordinate to any other coordinate
# sr - start row index
# sc - start col index
# dr - destination row index
# dc - destination col index
# We generally backtrack from dr,dc to sr,sc in this problem
# this will give us a nice recursion since if we know how to get to
# dr - 1, dc or dr, dc - 1, we basically know how to reach dr, dc
# cache is used for memoization
def robo_path(maze, sr, sc, dr, dc, path, cache):

  if len(maze) == 0 or maze == None or \
  sr > dr or sc > dc or not maze[dr][dc] or (dr, dc) in cache:
    return False

  if (dr == sr and sc == dc) or \
  robo_path(maze, sr, sc, dr - 1, dc, path, cache) or \
  robo_path(maze, sr, sc, dr, dc - 1, path, cache):
    path.append((dr, dc))
    return True
  else:
    # point that failed needs to be added into a cache so
    # that we can prevent repetition and use the memoization
    cache.append((dr, dc))
    return False

# string reversal using stack O(N)
# space is O(N) since it uses a stack for storage
def reverse_string_stack(string):
  stack = []
  for c in string:
    stack.append(c)
  for _ in range(0, len(stack), 1):
    print(stack.pop(), end= '')
  print()



# Building a trie for storing contact information
# trie is a very cool Data structure for storing information
# in which the key shows the path to the data
# for example 'Sid' has nbrs '5104498203' and '8080842228' stored
# so, each character in sid shows the path in the n-ary tree branches
# key part - d
# key part - i
# key part - s
# ['5104498203']
# key part - s
# key part - i
# key part - d
# ['5104498203', '8080842228']

class TrieNode:

  def __init__(self):

    # since same key can have different data, I maintain the
    # duplicate data instead of overwriting it
    self.data = []

    # since trie is a n-ary tree, each node can have atmost
    # n children, hence this list
    # since I'm storing names as keys, there has to be
    # 26 characters (given I'm following only ASCII - lowercase Eng)
    # will need more if need to follow if unicode is needed
    # this array can also be a hashmap(dict) that maps the child to
    # the identifying character/key part
    self.children = [ None for i in range(0, 26, 1) ]


def insert(root, key, data):

  current = root

  if len(key) == 0:
    current.data.append(data)
    return

  # decompose the key
  key_char_int = ord(key[0].lower())

  if current.children[key_char_int - 97] == None:
    current.children[key_char_int - 97] = TrieNode()

  current = current.children[key_char_int - 97]
  insert(current, key[1:], data)


def print_trie(root):
  current = root
  if current.children == [None] * 26:
    print(current.data)
  for i in range(0, 26, 1):
    if current.children[i] != None:
      print('key part - {}'.format(chr(i + 97)))
      print_trie(current.children[i])

def search_trie(root, value):

  current = root

  if len(value) == 0:
    return current.data

  value_char_int = ord(value[0].lower())

  if current.children[value_char_int - 97] != None:
    return search_trie(current.children[value_char_int - 97], value[1:])
  else:
    return None



def build_trie():

  # root the trie
  trie_root = TrieNode()

  insert(trie_root, 'Sid', '5104498203')
  insert(trie_root, 'Dis', '5104498203')
  insert(trie_root, 'Sid', '8080842228')

  return trie_root


# magic index
# array is sorted with distinct intergers
def magic_index(arr, l, h):

  mid = (l + h) // 2

  if arr[mid] == mid:
    return mid
  elif arr[mid] < mid:
    l = mid + 1
  else:
    h = mid - 1

  return magic_index(arr, l, h)

# if not distinct, then we cannot narrow down to the left or right
# of middle element, so we need to run the case for both of them
def magic_index_nd(arr, l, h):

  if h < l:
    return -1

  mid = (l + h) // 2

  if arr[mid] == mid:
    return mid

  # take the one that is smaller for left side
  left_index  = min(mid - 1, arr[mid])
  left_val = magic_index_nd(arr, l, left_index)
  if left_val >= 0:
    return left_val

  right_index = max(arr[mid], mid + 1)
  return magic_index_nd(arr, right_index, h)










if __name__ == '__main__':

  string = 'abc'
  permute_string(string)

  path = []
  maze = [[True, False, True, True],\
  [True, True, False, True],\
  [False, True, True, True],
  [True, True, False, True]]

  x = magic_index_nd([-10, 1, 1, 3, 5, 6], 0, 5)

  # robo_path([[True, False], [True, True]], 0, 0, 1, 1, path, [])
  








