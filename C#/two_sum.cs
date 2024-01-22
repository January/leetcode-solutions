public class Solution
{
    public static int[] TwoSum(int[] nums, int target)
    {
        for(int i = 0; i < nums.Length; i++)
        {
            for(int j = 1; j < nums.Length; j++)
            {
                if (nums[i] + nums[j] == target && i != j)
                {
                    return [i, j];
                }
            }
        };
        return [0];
    }

    static public void Main(String[] args)
    {
        int[] soln = TwoSum([2, 7, 11, 15], 9);
        Console.Write("[ ");
        for(int i = 0; i < soln.Length; i++)
        {
            Console.Write(soln[i] + " ");
        }
        Console.Write("]");
    }
}