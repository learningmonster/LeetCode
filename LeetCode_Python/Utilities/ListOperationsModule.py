class ListOperations(object):
    """description of class"""


    def ListOperations(self):
        print("Initializing ListOperations object...")
        print(f"__name__12 = {__name__}\n")
        
    #@classmethod
    @staticmethod
    def ConvertBracketListToStringArray(bracketListString):

        #print(f"bracketListString = {bracketListString}")
        bracketListString = bracketListString.strip().lstrip('[').rstrip(']').replace('"', '')
        #print(f"bracketListString = {bracketListString}")

        bracketsRemovedStringList = bracketListString.split(',')

        bracketsRemovedStringList = [element.strip() for element in bracketsRemovedStringList]

        #print(f"bracketsRemovedStringList = {bracketsRemovedStringList}")

        return bracketsRemovedStringList


    #public static int[] ConvertBracketListToIntegerArray(string bracketListString)
    #{
    #    string[] bracketsRemovedStringArray = ConvertBracketListToStringArray(bracketListString);
    #    int[] bracketsRemovedIntegerArray = bracketsRemovedStringArray.Select(x => int.Parse(x)).ToArray();
    #    return bracketsRemovedIntegerArray;
    #}

print(f"__name__13 = {__name__}\n")