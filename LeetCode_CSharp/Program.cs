using System;

namespace LeetCode_CSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool forever = true;

            while (forever)
            {
                Console.WriteLine("Welcome to the Leetcode solutions using C#.");
                Console.WriteLine();

                Console.WriteLine("Solved Problems - ");
                Console.WriteLine();
                Console.WriteLine("0. Quit");
                Console.WriteLine("1. Two Sum");
                Console.WriteLine("9. Palindrome");
                Console.WriteLine();

                bool isValidInput = false;
                int problemNumber = 0;

                while (!isValidInput)
                {
                    Console.WriteLine("Enter a problem number from the list above:");
                    string userChoice = Console.ReadLine();
                    isValidInput = int.TryParse(userChoice, out problemNumber);

                    if (!isValidInput)
                    {
                        Console.WriteLine("Invalid input!\n");
                    }
                }

                switch (problemNumber)
                {
                    case 1:
                        {
                            Console.WriteLine("You chose # 1. Two Sum\n");
                            TwoSumSolution twoSum = new TwoSumSolution();
                            break;
                        }
                    case 9:
                        {
                            Console.WriteLine("You chose # 9. Palindrome\n");
                            Palindrome palindrome = new Palindrome();
                            break;
                        }
                    default:
                        {
                            Console.WriteLine();
                            break;
                        }
                        
                }

                if (problemNumber == 0)
                {
                    break;
                }

            }
        }
    }
}