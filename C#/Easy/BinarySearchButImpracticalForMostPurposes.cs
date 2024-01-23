public class Solution
{
    public int Search(int[] nums, int target)
    {
        // Yes, I could just use Arrays.IndexOf(). But that would be practical
        // and we're not on Leetcode to be practical.
        int midpoint = nums.Length / 2;
        if(target < nums[midpoint])
        {
            for(int i = 0; i < midpoint; i++)
            {
                if(nums[i] == target) return i;
            }
        }
        else if(target > nums[midpoint])
        {
            for(int i = midpoint; i < nums.Length; i++)
            {
                if(nums[i] == target) return i;
            }
        }
        else if(target == nums[midpoint])
        {
            return midpoint;
        }
        return -1;
    }
}