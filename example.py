'''
    Test suite for using my DS implementations suite
'''

__author__ = 'sidmishraw'

def build_linked_list(list_of_items):
  'tests for linked lists'
  from lists.lists import LinkedList
  print('building linked list %s' % list_of_items)
  l = LinkedList()
  for item in list_of_items:
    l.insert(item)
  print('linked list built = %s' % l)
  return l

def main():
  'point of entry of the program'
  pass

if __name__ == '__main__':
  main()