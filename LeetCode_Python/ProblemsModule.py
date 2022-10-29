import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'Problems' )
sys.path.append( mymodule_dir )

#for p in sys.path:
#    print( p )

from LongestCommonPrefix_0014 import *

#class class1(object):
#    """description of class"""


print(f"__name__3 = {__name__}")