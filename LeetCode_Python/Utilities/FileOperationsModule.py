import os.path

class FileOperations(object):
    """description of class"""
    
    # Under Linux
    TestCasesFolder = "../TestCases/"
    # TestCases/0014_LongestCommonPrefix.txt
    
    # Under Windows
    # TestCasesFolder = "D:\\Projects\\ProgrammingChallenges\\LeetCode\\TestCases\\"

    def __init__(self):
        print("Initializing FileOperations object...\n")
        print(f"__name__11 = {__name__}\n")

    #// TODO: Set folder location as a configurable setting
        #static string TestCasesFolder = @"D:\Projects\ProgrammingChallenges\LeetCode\TestCases\";
        #self.TestCasesFolder = "D:\\Projects\\ProgrammingChallenges\\LeetCode\\TestCases\\"

        #TestCasesFolder = "D:\\Projects\\ProgrammingChallenges\\LeetCode\\TestCases\\"

        #// TestCases location under Linux:
        #// static string TestCasesFolder = "~/Learning/LeetCode/LeetCode/TestCases/";

        #// TestCases location under Windows:
        #// static string TestCasesFolder = @"D:\Projects\ProgrammingChallenges\LeetCode\TestCases\";

        #internal FileOperations()
        #{

        #}

        #public static string[] ReadLinesInFile(string inputFile)
        #{
        #    string FullFilePath = TestCasesFolder + inputFile;
        #    // Read each line of the file into a string array. Each element
        #    // of the array is one line of the file.
        #    string[] lines = System.IO.File.ReadAllLines(FullFilePath);

        #    return lines;
        #}

    #def ReadLinesInFile(self, inputFile):
    #@staticmethod
    #def ReadLinesInFile(inputFile):
    @classmethod
    def ReadLinesInFile(cls, inputFile):

        print(f"cls = {cls}")
        print(f"inputFile = {inputFile}")

        # Define a filename
        #FullFilePath = self.TestCasesFolder + inputFile;
        FullFilePath = FileOperations.TestCasesFolder + inputFile;
        print(f"FullFilePath = {FullFilePath}")
            
        if not os.path.isfile(FullFilePath):
            print('File does not exist.')
            lines = None
        else:
            #Read each line of the file into a string array. Each element
            #of the array is one line of the file.
            with open(FullFilePath, 'r', encoding='utf8') as FileReader:
                lines = FileReader.readlines()

        return lines

print(f"__name__14 = {__name__}\n")



