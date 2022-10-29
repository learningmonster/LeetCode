from UtilitiesModule import *

#import inspect

#for name, obj in inspect.getmembers(FileOperations):
#    #print(f"type(obj) = {type(obj)}")
#    if inspect.isclass(obj):
#        print("TRUE -")
#        print ('obj = ' + str(obj))
#    else:
#        print("FALSE -")
#        print ('obj = ' + str(obj))

class LongestCommonPrefix(object):

    def __init__(self):
        print("Initializing LongestCommonPrefix object...\n")
        print(f"__name__4 = {__name__}\n")

        #FileOperationsObject = FileOperations()

        inputFile = "0014_LongestCommonPrefix.txt";
        #lines = FileOperations.ReadLinesInFile(inputFile)
        #lines = ReadLinesInFile(self, inputFile)
        lines = FileOperations.ReadLinesInFile(inputFile)

        isValidInput = False
        testNumber = 0

        #print("Input file has been read.\n");
        #print()

        # Test the file contents by using a foreach loop.
        for line in lines:
            #print(f"Testing input, line = {line}...\n");

            lineArray = ListOperations.ConvertBracketListToStringArray(line);

            print(f"Testing input, lineArray = {lineArray}...\n");

            print(f"self.longestCommonPrefix(line) = {self.longestCommonPrefix(lineArray)}\n\n")

    #def longestCommonPrefix(self, strs):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """

        #print(f"stringArray2 = {strs}\n")

        shortestStringLength = 201
        numStrings = len(strs)

        for stringIndex in range(numStrings):
            if (len(strs[stringIndex]) < shortestStringLength):
                shortestStringLength = len(strs[stringIndex])

        LongestMatchingPrefix = ''
        currentLetterMatches = True
        #print(f"currentLetterMatches0 (default starting value) = {currentLetterMatches}\n")

        for charPositionIndex in range(shortestStringLength):
            #print(f"currentLetterMatches0 (value at loop start) = {currentLetterMatches}\n")
            #print(f"charPositionIndex = {charPositionIndex}\n")
            currentLetter = strs[0][charPositionIndex]
            #print(f"currentLetter = {currentLetter}\n")

            for memberString in strs:
                #print(f"currentLetter2 at position {charPositionIndex} = {currentLetter}\n")
                #print(f"currentLetterMatches1 = {currentLetterMatches}\n")
                #print(f"memberString = {memberString}\n")

                if not memberString[charPositionIndex] == currentLetter:
                    currentLetterMatches = False
                    #print(f"currentLetterMatches2 = {currentLetterMatches}")
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