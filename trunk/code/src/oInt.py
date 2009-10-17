'''The class that represents an Integer'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: oInt.py 188 2009-05-21 00:40:52Z didi $
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

import sys

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("oInt")
log.setLevel(globalConf.logLevel)


#My Stuff
from oObject import oObject



class oInt(oObject):
    '''The class that represents an integer'''
    
    __val = 0
    
    def __init__(self, params):
        
        params = self.cheanVal(params)
        
        #Initialize the base
        oObject.__init__(self)
        if str(params).isdigit():
            self.__val = int(params)
        elif str(params).strip() == "VOID":
            self.__val = 0
        else:
            #If the first two fail try extreme methods
            #This will be run by -INT : Maybe optimize a little ;)
            try:
                self.__val = int(params.strip())
            except (ValueError, IndexError):
                log.error("Invalid parameter in create: " + str(params))
                self.__val = 0
        
    def fadd(self, params):
        '''Creates a new obj with the value plus params and retuns a new ptr'''
        
        params = self.cheanVal(params)
        
        #Check if the parameter is valid
        if str(params).strip().isdigit():
            return "NEWOBJ:" + \
                oObject.createNewObj(self, "Int", (self.__val + int(params)))
        else:
            log.error("Invalid parameter in add" + str(params))
            return "Invalid parameter in add" + str(params)

    def fmul(self, params):
        '''Creates a new obj with the value multiplied by params'''
        
        params = self.cheanVal(params)
        
        #Check if the parameter is valid
        if str(params).strip().isdigit():
            return "NEWOBJ:" + \
                oObject.createNewObj(self, "Int", (self.__val * int(params)))
        else:
            log.error("Invalid parameter in mul" + str(params) )
            return "Invalid parameter in mul" + str(params)

    def fdev(self, params):
        '''Creates a new obj with the value devided by params'''
        
        params = self.cheanVal(params)
        
        #Check if the parameter is valid
        if str(params).strip().isdigit():
            return "NEWOBJ:" + \
                oObject.createNewObj(self, "Int", (self.__val / int(params)))
        else:
            log.error("Invalid parameter in mul" + str(params) )
            return "Invalid parameter in mul" + str(params)

    
    def fmin(self, params):
        '''Creates a new obj with the value min params and retuns a new ptr'''
        
        params = self.cheanVal(params)
        
        #Check if the parameter is valid
        if str(params).strip().isdigit():
            return "NEWOBJ:" + \
                oObject.createNewObj(self, "Int", (self.__val - int(params)))
        else:
            log.error("Invalid parameter in min"+ str(params) )
            return "Invalid parameter in add" + str(params)   
        

    def fvalue(self, params):
        '''Returns the value of the int'''
        
        if params != "VOID":
            log.error("Why are you giving value me parameters:" + str(params))
        
        return str(self.__val)
    
    def frep(self, params):
        '''Returns a string represtenation of the int'''
     
        if params != "VOID":
            log.error("Why are you giving rep me parameters:" + str(params))

        return "<oInt> " + str(self.callFunction("value", "VOID"))
        
        
if __name__ == '__main__':

    testObj = oInt("0")
    if testObj.fvalue("VOID") != "0":
        print("Error in fvalue")

    if testObj.frep("VOID") != "<oInt> 0":
        print("Error in frep")
    
    if testObj.fmin("1").split("/")[0] != "NEWOBJ:bigi":
        print ("Error in min")
        
    if testObj.fadd("1").split("/")[0] != "NEWOBJ:bigi":
        print ("Error in add")
        
    if testObj.fmul("1").split("/")[0] != "NEWOBJ:bigi":
        print ("Error in mul")
        
    if testObj.fdev("1").split("/")[0] != "NEWOBJ:bigi":
        print ("Error in dev")    