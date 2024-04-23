# Exercise 1
### Add the folling methods to the `LinkedList` class implementation:
- ```python
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
```
- ```python
def remove_by_value(self, data):
    # Remove first node that contains data
```

# Exercise 2
### Implement a doubly linked list, with the following node strcuture and methods:
- ```python
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
```

- ```python
def print_forward(self):
    # This method prints list in forward direction using node.next
```

- ```python
def print_backward(self):
    # Print linked list in reverse direction using node.prev
```
**N.B:** The exercises in this directory are a build on from the Linked list class built in the course of the YouTube tutorial and the original file can be found here -> [Linked list tutorial -  Codebasic](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py)

