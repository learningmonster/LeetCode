# import statements

def Main():
    forever = True

    while forever:
        print("Welcome to the Leetcode solutions using Python.")
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
            case 15:
                print("You chose # 14. Longest Common Prefix\n")
                #TwoSumSolution twoSum = new TwoSumSolution()
                prefixFinder = LongestCommonPrefix()

            case 0:
                forever = False
                print("Ending program...\n")
            case _:
                print(f"{problemNumber} is not a valid option. Please choose only one of the listed options.\n")

    print("Thank you for your participation.\n")


if __name__ == '__main__':
    Main()