using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode_CSharp
{
    internal class TwoSumSolution
    {
        public TwoSumSolution()
        {
            string inputFile = @"D:\Projects\ProgrammingChallenges\LeetCode\LeetCode\TestCases\0001_TwoSum.txt";
            string[] lines = FileOperations.ReadLinesInFile(inputFile);

            int i = 0;
            int[] nums = new int[] { };
            int target = 0;

            System.Console.WriteLine("Input file has been read.\n");
            Console.WriteLine();

            // Test the file contents by using a foreach loop.
            foreach (string line in lines)
            {
                i++;

                if (i%2 == 1)
                {
                    Console.WriteLine("Testing input {0}...", line);
                    nums = ArrayOperations.ConvertBracketListToIntegerArray(line);
                }
                else
                {
                    Console.WriteLine("For a TwoSum of {0}...\n", line);
                    bool isValidInput = int.TryParse(line, out target);

                    int[] result = TwoSum(nums, target);

                    Console.WriteLine("The result is: [{0},{1}]", result[0], result[1]);
                    Console.WriteLine();
                }

            }
        }

        public int[] TwoSum(int[] nums, int target)
        {
            int low = 0;
            int high = nums.Length - 1;
            int[] sortedNums = (int[])nums.Clone();
            Array.Sort(sortedNums);
            for (int i = 0; i < sortedNums.Length; i++)
            {
                int currentSum = sortedNums[low] + sortedNums[high];
                if (currentSum == target)
                {
                    break;
                }
                else if (currentSum < target)
                {
                    low += 1;
                }
                else if (currentSum > target)
                {
                    high -= 1;
                }
            }

            int lowPosition = Array.IndexOf(nums, sortedNums[low]);
            
            // temporarily remember the value at the low position
            int valueAtLowPosition = nums[lowPosition];

            //temporarily change the value at low position to an out of bounds value
            nums[lowPosition] = int.MinValue;

            int highPosition = Array.IndexOf(nums, sortedNums[high]);

            //restore the original value at low position.
            nums[lowPosition] = valueAtLowPosition;

            int[] result = { lowPosition, highPosition };
            return result;
        }


    }
}
