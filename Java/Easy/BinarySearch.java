class Solution
{
    public int search(int[] nums, int target)
    {
        // worst java one-liner ever seen!
        return IntStream.of(nums).boxed().collect(Collectors.toList()).indexOf(target);
    }
}