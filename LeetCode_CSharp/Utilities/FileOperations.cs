using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode_CSharp
{
    internal class FileOperations
    {
        // TODO: Set folder location as a configurable setting
        static string TestCasesFolder = @"D:\Projects\ProgrammingChallenges\LeetCode\TestCases\";

        // TestCases location under Linux:
        // static string TestCasesFolder = "~/Learning/LeetCode/LeetCode/TestCases/";

        // TestCases location under Windows:
        // static string TestCasesFolder = @"D:\Projects\ProgrammingChallenges\LeetCode\TestCases\";

        internal FileOperations()
        {

        }

        public static string[] ReadLinesInFile(string inputFile)
        {
            string FullFilePath = TestCasesFolder + inputFile;
            // Read each line of the file into a string array. Each element
            // of the array is one line of the file.
            string[] lines = System.IO.File.ReadAllLines(FullFilePath);

            return lines;
        }


    }
}
