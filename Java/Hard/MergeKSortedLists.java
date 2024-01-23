public class ListNode
{
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

class Solution
{
    public ListNode mergeKLists(ListNode[] lists)
    {
        List<Integer> vals = new ArrayList<Integer>();
        for (int i = 0; i < lists.length; i++)
        {
            while (lists[i] != null)
            {
                vals.add(lists[i].val);
                lists[i] = lists[i].next;
            }
        }
        if (vals.size() == 0)
        {
            return null;
        }
        Collections.sort(vals);
        ListNode returnNode = new ListNode(vals.get(0));
        for (int i = 1; i < vals.size(); i++)
        {
            ListNode currentNode = returnNode;
            while (currentNode.next != null)
            {
                currentNode = currentNode.next;
            }
            currentNode.next = new ListNode(vals.get(i));
        }
        return returnNode;
    }
}