public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public ListNode MergeKLists(ListNode[] lists)
    {
        List<int> vals = new List<int>();
        Console.WriteLine(lists.Length);
        for (int i = 0; i < lists.Length; i++)
        {
            while (lists[i] != null)
            {
                vals.Add(lists[i].val);
                lists[i] = lists[i].next;
            }
        }
        if (vals.Count == 0)
        {
            return null;
        }
        vals.Sort();
        ListNode returnNode = new ListNode(vals[0]);
        for (int i = 1; i < vals.Count; i++)
        {
            ListNode currentNode = returnNode;
            while (currentNode.next != null)
            {
                currentNode = currentNode.next;
            }
            currentNode.next = new ListNode(vals[i], null);
        }
        return returnNode;
    }
}