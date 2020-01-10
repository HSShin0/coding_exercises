"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Constraints:
-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# without using copy.deepcopy

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ''' O(n)/O(n) where n : the length of the input linked list '''
        if not head:
            return None
        
        ori2cp = {}
        node = head
        ori2cp[node] = Node(node.val)
        # Construct a dictionary ori2cp={node: copy_of_node}
        while node.next:
            next_node = node.next
            ori2cp[next_node] = Node(next_node.val)
            # copy the pointer for the next node
            ori2cp[node].next = ori2cp[next_node]
            node = next_node
        # Copy the pointer for the random node
        node = head
        if node.random:
            ori2cp[node].random = ori2cp[node.random]
        while node.next:
            node = node.next
            if node.random:
                ori2cp[node].random = ori2cp[node.random]
            
        return ori2cp[head]
