public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        for (int i = 2; i < cost.Length; i++)
        {
            cost[i] += Math.Min(cost[i - 1], cost[i - 2]);
        }

        return Math.Min(cost[cost.Length - 1], cost[cost.Length - 2]);
    }
}
