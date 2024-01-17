namespace algorithm_exercises
{
    public class ClimbingStairs
    {
        public int MinCostClimbingStairs(int[] cost)
        {
            for (int i = 2; i < cost.Length; i++)
            {
                cost[i] += Math.Min(cost[i - 1], cost[i - 2]);
            }

            return Math.Min(cost[^1], cost[^2]);
        }
    }
}

