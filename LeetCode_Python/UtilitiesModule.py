import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'Utilities' )
sys.path.append( mymodule_dir )

#for p in sys.path:
#    print( p )

from FileOperationsModule import *
from ListOperationsModule import *

#class class1(object):
#    """description of class"""


print(f"__name__15 = {__name__}")