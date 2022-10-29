namespace LeetCode_CSharp
{
    internal class Palindrome
    {

        public Palindrome()
        {
            string inputFile = "0009_Palindrome.txt";
            string[] lines = FileOperations.ReadLinesInFile(inputFile);

            bool isValidInput = false;
            int testNumber = 0;

            System.Console.WriteLine("Input file has been read.\n");
            Console.WriteLine();

            // Test the file contents by using a foreach loop.
            foreach (string line in lines)
            {
                Console.WriteLine("Testing input '{0}'...\n", line);

                isValidInput = int.TryParse(line, out testNumber);

                if (isValidInput)
                {
                    //Console.WriteLine(Palindrome.IsPalindrome(testNumber));
                    Console.WriteLine(IsPalindrome2(testNumber));
                    Console.WriteLine();
                }
                else
                {
                    Console.WriteLine("{0} is not a valid input.", line);
                    Console.WriteLine();
                }
            }
        }

        // Using string conversion, iterative
        public static bool IsPalindrome(int x)
        {
            if (x < 0) return false;
            if (x < 10) return true;

            string strX = x.ToString();

            while (strX.Length > 1)
            {
                if (strX[0] != strX[strX.Length - 1])
                {
                    return false;
                }

                int newLength = strX.Length - 2;

                if (newLength <= 1)
                {
                    return true;
                }

                strX = strX.Substring(1, newLength);
            }

            return true;
        }

        // Without string conversion, iterative
        public bool IsPalindrome2(int x)
        {
            if (x < 0 || (x % 10 == 0 && x != 0))
            {
                Console.WriteLine("Original x = {0}", x);
                Console.WriteLine("Returning False");
                Console.WriteLine();
                return false;
            }
            else if (x < 10)
            {
                Console.WriteLine("Original x = {0}", x);
                Console.WriteLine("Returning True");
                Console.WriteLine();
                return true;
            }

            int i = 0;
            int reversedNumber = 0;

            Console.WriteLine("Loop cycle #{0}", i);
            Console.WriteLine("reversedNumber = {0}", reversedNumber);
            Console.WriteLine("Original x = {0}", x);
            Console.WriteLine();

            // Loop while the truncated original number is larger than the constructed reversed number
            while (x > reversedNumber)
            {
                i++;
                Console.WriteLine("Loop cycle #{0}", i);

                int lastDigit = x % 10;
                Console.WriteLine("Popped lastDigit = {0}", lastDigit);

                // Construct reversed number by shifting left, and adding the last digit
                reversedNumber = reversedNumber * 10 + lastDigit;

                // Drop last digit from original number
                x /= 10;

                Console.WriteLine("reversedNumber with new LastDigit attached = {0}", reversedNumber);
                Console.WriteLine("Truncated x (minus the popped LastDigit) = {0}", x);
                Console.WriteLine();

                // Repeat until reversedNumber is greater than or equal to the truncated original number.

                // When truncated original number reaches less than or equal to the reversedNumber, 
                // at least half the digits (from the right side) have been truncated out and reversed.
            }

            Console.WriteLine("Loop ended - evaluating result...");

            Console.WriteLine("Truncated x = {0}", x);
            Console.WriteLine("reversedNumber = {0}", reversedNumber);
            Console.WriteLine("reversedNumber / 10 = {0}", reversedNumber / 10);
            Console.WriteLine();

            if (x == reversedNumber)
            {
                Console.WriteLine("Returning True");
                Console.WriteLine();
                return true;
            }
            else if (x == reversedNumber / 10)
            {
                Console.WriteLine("Returning True");
                Console.WriteLine();
                return true;
            }
            else
            {
                Console.WriteLine("Returning False");
                Console.WriteLine();
                return false;
            }
        }

    }
}
