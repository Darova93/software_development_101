namespace algorithm_exercises
{
    public class FindIndexFirstOccurrence
    {
        public int StrStr(string haystack, string needle)
        {
            if (haystack.Length <= needle.Length)
            {
                return -1;
            }

            for (int i = 0; i < haystack.Length - needle.Length + 1; i++)
            {
                if (haystack.Substring(i, needle.Length) == needle)
                {
                    return i;
                }

            }

            return -1;
        }
    }
}
