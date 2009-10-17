'''The class that represents a String'''

__version__ = "$Revision: 75 $"

# ObjiC $Id: oInt.py 75 2009-04-14 15:47:55Z didi $
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
log = logging.getLogger("oString")
log.setLevel(globalConf.logLevel)


#My Stuff
from oObject import oObject


#CHANGE to string

class oString(oObject):
    '''The class that represents an string'''
    
    __val = ""
    

            
    
    def __init__(self, params):
        
        #Initialize the base
        oObject.__init__(self)
        
        if str(params).strip().upper() == "VOID":
            self.__val = ""
        else:
            #If the first two fail try extreme methods
            #This will be run by -INT : Maybe optimize a little ;)
            try:
                self.__val = str(self.cheanVal(params))
            except (ValueError, IndexError):
                log.error("Invalid parameter in create")
                self.__val = 0
        
    def fadd(self, params):
        '''Creates a new obj with the value plus params and retuns a new ptr'''
        
        #Check if the parameter is valid
        return "NEWOBJ:" + \
            oObject.createNewObj(self, "String", "\"" + \
                        (str(self.__val) + str(self.cheanVal(params))) + "\"")
        
    
    def fvalue(self, params):
        '''Returns the value'''
        
        if params != "VOID":
            log.error("Why are you giving value me parameters:" + str(params))
        
        return "\"" + str(self.__val) + "\"" 
    
    def frep(self, params):
        '''Returns a string represtenation'''
     
        if params != "VOID":
            log.error("Why are you giving rep me parameters:" + str(params))

        return "<oString> " + str(self.callFunction("value", "VOID")) 
        
