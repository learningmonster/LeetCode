#class _0014_LongestCommonPrefix(object):
#    """description of class"""



# class Solution(object):
class LongestCommonPrefix(object):

    def __init__(self):
        print("Initializing class...")

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        shortestStringLength = 201
        numStrings = strs.length

        for stringIndex in range(numStrings):
            if (strs[stringIndex].length < shortestStringLength):
                shortestStringLength = strs[stringIndex].length

        LongestMatchingPrefix = ''

        for index in range(shortestStringLength):
            currentLetterMatches = True
            currentLetter = strs[0][index]

            for substring in strs:
                if not substring[index] == currentLetter:
                    currentLetterMatches = False
                    break

            if currentLetterMatches:
                LongestMatchingPrefix += currentLetter
            
        return LongestMatchingPrefix





            



        



