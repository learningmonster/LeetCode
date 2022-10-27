using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode_CSharp
{
    internal class ArrayOperations
    {
        internal ArrayOperations()
        {
        }

        public static string[] ConvertBracketListToStringArray(string bracketListString)
        {
            string[] bracketsRemovedStringArray = bracketListString.Trim().TrimStart('[').TrimEnd(']').Split(',');
            return bracketsRemovedStringArray;
        }

        public static int[] ConvertBracketListToIntegerArray(string bracketListString)
        {
            string[] bracketsRemovedStringArray = ConvertBracketListToStringArray(bracketListString);
            int[] bracketsRemovedIntegerArray = bracketsRemovedStringArray.Select(x => int.Parse(x)).ToArray();
            return bracketsRemovedIntegerArray;
        }

    }
}
