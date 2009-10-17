'''The class that is called from the ObjServer when creating a new Object'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: oVm.py 188 2009-05-21 00:40:52Z didi $
#
# @author: Hoffmann Geerd-Dietger <geerd.dietger.hoffmann@gmail.com>
# 
#            Final year project for Bournemouth University
#
# @copyright: 
# Copyright (c) 2009, Hoffmann Geerd-Dietger
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     - Neither the name of the copyright owner nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#     - All advertising materials mentioning features or use of this software
#       must display the following acknowledgement:
#         This product includes software developed by Hoffmann Geerd-Dietger
#         and contributors.
#     - The Program and its derivative work will neither be modified or
#       executed to harm any human being nor through inaction permit
#       any human being to be harmed.
#
# THIS SOFTWARE IS PROVIDED BY <copyright holder> ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <copyright holder> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#The antlr libs
#import antlr3

import globalConf

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("Vm")
log.setLevel(globalConf.logLevel)

from random import Random



#My Stuff
from oInt import oInt 
from oString import oString
 
class oVm:
    '''The object virtual machine'''
    
    #Every VM only has one OBJ
    __obj = None
    
    __vmName = "VOID"

    __objtype = "VOID"
    
    def __init__(self, objType, params):
        
        #Create and set the name
        #We assume that 16 is a big enough random number not to be generated 2
        #time
        
        validChars = "abcdefghijklmnopqrstuvwxyz" + \
                     "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                     "0123456789"
        
        self.__vmName = "".join(
                        Random().sample(validChars , 32))
        
        self.__objtype = objType
        
        #Check if it is a built in 
        if objType == "Int":
            #Create new int obj
            self.__obj = oInt(params)
        elif objType == "String":
            self.__obj = oString(params)
        else:
            from Interpreter import Interpreter
            #Must be a user class
            self.__obj = Interpreter()
            self.__obj.setName(self.getName())
            
            
        #Return massive error
        
    
    def call(self, name, params):
        '''Calls a method and returns the result'''
        retval = self.__obj.callFunction(name, params) 
        return retval

    def constructor(self):
        '''The constructor'''
        self.__obj.run(self.__objtype)

    def getName(self):
        '''Returns the name of the VM'''
        return self.__vmName
    
    def __repr__(self):
        return self.call("rep", "VOID")
    

        
    