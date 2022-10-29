#import sys

#for p in sys.path:
#    print( p )

from ProblemsModule import *

#import inspect

#for name, obj in inspect.getmembers(ProblemsModule):
#    if inspect.isclass(obj):
#        print ('obj = ' + str(obj))



def Main():
    #print(f"__name__1 = {__name__}")
    forever = True

    while forever:
        print("\nWelcome to the Leetcode solutions using Python.")
        print()

        print("Solved Problems - ")
        print()
        print("0. Quit")
        print("14. Longest Common Prefix")
        print()

        isValidInput = False
        problemNumber = 0

        while not isValidInput:
            # Get user input from keyboard
            userChoice = input("Enter a problem number from the list above: ")

            try:
                problemNumber = int(userChoice)
                isValidInput = True
            except ValueError:
                print(f"{userChoice} is invalid input! Please enter an integer value only.\n")

        match problemNumber:
            case 14:
                print("You chose # 14. Longest Common Prefix\n")
                prefixFinder = LongestCommonPrefix()
                #stringArray = ["substring", "substance", "substandard", "subs"]
                #print(f"Typeof(stringArray) = {type(stringArray)}")
                #print(f"stringArray1 = {stringArray}\n")
                #result = prefixFinder.longestCommonPrefix(stringArray)
                #print(f"LongestMatchingPrefix={result}\n")

            case 0:
                forever = False
                print("Ending program...\n")
            case _:
                print(f"{problemNumber} is not a valid option. Please choose only one of the listed options.\n")

    print("Thank you for your participation.\n")


if __name__ == '__main__':
    print(f"__name__2 = {__name__}")
    Main()