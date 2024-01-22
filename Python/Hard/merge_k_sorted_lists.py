from typing import List
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    vals = []
    for list in lists:
        while list is not None:
            vals.append(list.val)
            list = list.next
    vals.sort()
    try:
        retn_node = ListNode(val=vals[0])
        for i in range(1, len(vals)):
            current_node = retn_node
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = ListNode(vals[i], None)
        return retn_node
    except IndexError:
        pass