using algorithm_exercises;

namespace algorithm_exercises_test_csharp
{
    public class MinCostClimbingStairsTest
    {
        public readonly ClimbingStairs service = new();

        [Fact]
        public void Test1()
        {
            int[] cost = { 10, 15, 20 };

            int result = service.MinCostClimbingStairs(cost);

            Assert.Equal(15, result);
        }

        [Fact]
        public void Test2()
        {
            int[] cost = { 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 };

            int result = service.MinCostClimbingStairs(cost);

            Assert.Equal(6, result);
        }
    }
}
