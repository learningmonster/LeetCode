using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode_CSharp
{
    internal class FileOperations
    {
        internal FileOperations()
        {

        }

        public static string[] ReadLinesInFile(string inputFile)
        {
            // D:\Projects\ProgrammingChallenges\LeetCode\LeetCode\TestCases\0009_Palindrome.txt

            // Read each line of the file into a string array. Each element
            // of the array is one line of the file.
            string[] lines = System.IO.File.ReadAllLines(inputFile);

            return lines;
        }


    }
}
