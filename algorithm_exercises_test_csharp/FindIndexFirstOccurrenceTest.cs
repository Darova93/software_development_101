using algorithm_exercises;

namespace algorithm_exercises_test_csharp
{
    public class FindIndexFirstOccurrenceTest
    {
        public readonly FindIndexFirstOccurrence service = new();

        [Fact]
        public void Test1()
        {
            var haystack = "sadbutsad";
            var needle = "sad";

            int result = service.StrStr(haystack, needle);

            Assert.Equal(0, result);
        }

        [Fact]
        public void Test2()
        {
            var haystack = "leetcode";
            var needle = "leeto";

            int result = service.StrStr(haystack, needle);

            Assert.Equal(-1, result);
        }
    }
}