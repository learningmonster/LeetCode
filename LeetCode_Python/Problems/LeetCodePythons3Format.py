class LeetCodePythons3Format(object):
    """description of class"""


class Solution:
    #def longestCommonPrefix(self, strs: List[str]) -> str:
        
    def __init__(self):
        print("Initializing class...\n")
        print(f"__name__4 = {__name__}")

    #def longestCommonPrefix(self, strs):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """

        print(f"stringArray2 = {strs}\n")

        shortestStringLength = 201
        numStrings = len(strs)

        for stringIndex in range(numStrings):
            if (len(strs[stringIndex]) < shortestStringLength):
                shortestStringLength = len(strs[stringIndex])

        LongestMatchingPrefix = ''
        currentLetterMatches = True

        for index in range(shortestStringLength):
            print(f"currentLetterMatches0 = {currentLetterMatches}")
            currentLetter = strs[0][index]

            for substring in strs:
                print(f"currentLetterMatches1 = {currentLetterMatches}")
                if not substring[index] == currentLetter:
                    currentLetterMatches = False
                    print(f"currentLetterMatches2 = {currentLetterMatches}")
                    break

            if currentLetterMatches:
                LongestMatchingPrefix += currentLetter
                print(f"LongestMatchingPrefix1 = {LongestMatchingPrefix}")
                print(f"currentLetterMatches3 = {currentLetterMatches}")
            else:
                print("In the else clause!")
                print(f"currentLetterMatches4 = {currentLetterMatches}")
                break

        print(f"LongestMatchingPrefix2={LongestMatchingPrefix}")
        print(f"currentLetterMatches5 = {currentLetterMatches}")
        return LongestMatchingPrefix

print(f"__name__5 = {__name__}")