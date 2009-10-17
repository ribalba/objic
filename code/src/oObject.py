'''The class that represents an Object, Everything inherits from here'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: oObject.py 188 2009-05-21 00:40:52Z didi $
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

#The global configuration file
import globalConf

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("oObject")
log.setLevel(globalConf.logLevel)


#Every VM has it's own objManager
from ObjManager import ObjManager

class oObject:
    '''The base object definition, every object has to extend this'''
    
    __objman = ObjManager()
    
    def __init__(self):
        '''The initializer'''
        #Not much a base object can do
        pass
    
    def cheanVal(self, strVal):
        '''Cleans the string of all the transimition stuff'''
        if str(strVal).startswith("\"") or str(strVal).endswith("\""):
            #Ok we have the " strip them
            return strVal.strip("\"")
        else:
            return strVal
    
    def run(self, objType):
        '''The first constructor'''
        pass
    
    
    def createNewObj(self, typeOfObj, params):
        '''A wrapper to create new Objects'''
        return self.__objman.newObj(typeOfObj, params)
    
    
    def frep(self, params):
        '''Returns a string of the object name'''
         
        if params != "VOID":
            log.error("Why are you giving me parameters" + str(params))       
        
        return "<oObject> " + str(self)
    
    
    def callFunction(self, name, params):
        '''A interpreter local call to call int methods'''
        
        nameToCall = "f" + str(name)
        
        if hasattr(self, nameToCall):
            func = getattr(self, nameToCall)
            return func(params)
        else:
            log.error("Method " + str(name) + " does not exist")
            return "404 METHOD " + str(name) + " in " + str(self.frep("VOID"))
            