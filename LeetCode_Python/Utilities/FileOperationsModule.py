import os.path

class FileOperations(object):
    """description of class"""
    
    # Under Linux
    # When running WITHOUT debugging
    # TestCasesFolder = "../TestCases/"
    # When running WITH debugging
    TestCasesFolder = "TestCases/"
    
    # Under Windows
    # TestCasesFolder = "D:\\Projects\\ProgrammingChallenges\\LeetCode\\TestCases\\"

    def __init__(self):
        print("Initializing FileOperations object...\n")
        print(f"__name__11 = {__name__}\n")

    #// TODO: Set folder location as a configurable setting


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
        
        cwd = os.getcwd()
        print(f"cwd = {cwd}")
        
        
        if not os.path.isfile(FullFilePath):
            print('File does not exist.')
            with open(FullFilePath, 'r', encoding='utf8') as FileReader:
                lines = FileReader.readlines()
            # lines = None
        else:
            #Read each line of the file into a string array. Each element
            #of the array is one line of the file.
            with open(FullFilePath, 'r', encoding='utf8') as FileReader:
                lines = FileReader.readlines()

        return lines

print(f"__name__14 = {__name__}\n")



