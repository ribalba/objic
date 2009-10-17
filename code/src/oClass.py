'''The class that represents an object in memory'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: oClass.py 188 2009-05-21 00:40:52Z didi $
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


#This is the runtime representative of a class
#All classes on objic are mapped into this class

from ObjManager import ObjManager

import globalConf

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("oClass")
log.setLevel(globalConf.logLevel)

class oClass:
    '''The class that represents an object in memory'''
    
    __name = "VOID"
    __stack = [{}]
    __objManager = ""
    __methods = {}
    
    def __init__ (self):
        self.__objManager = ObjManager()
    
    def getStack(self):
        '''Returns the stack'''
        return self.__stack
    
    def setStack(self, stackToSet):
        '''Sets the stack '''
        self.__stack = stackToSet
    
    #This should ONLY be called at creation
    def setName(self, name):
        '''Sets the name of the object'''
        if self.__name != "VOID":
            log.debug("DEV DEBUG: Tried to rename class")

        self.__name = name

    
    def getName(self):
        '''Gets the name of the object'''
        return self.__name
    
    
    def raiseStack(self):
        '''Adds one level to the stack normally when block starts'''
        self.__stack.append({})
        
    def popStack(self):
        '''Pops the stack noramlly when block ends'''
        if len(self.__stack) == 0:
            log.error("VM ERRRO: Error pop from null stack ")
        
        #Close all the open connections
        self.cleanStackLevel()
        
        #And pop the stack. Nothing should be in it anyway
        self.__stack.pop()
        
        log.debug("STACK popped")
        
    
    def dump_stack(self):
        '''Returns a nice string of the satck'''
        returnVal = ""
        for i in xrange(0, len(self.__stack) ):
            returnVal = returnVal + "stack level " + str(i)
            returnVal = returnVal + str(self.__stack[i])
        
        return returnVal
    
    def addMethod(self, methodName, start, end):
        '''Adds a method to the object'''
        startStop = (start, end)
        self.__methods[methodName] = startStop
        
    def getMethod(self, methodName):
        '''Returns a method by the name'''
        if methodName in self.__methods:
            return self.__methods[methodName]
        else:
            log.error("Can not find requested method:" + str(methodName))
            print self.__methods
            return None
    
    def addVar(self, varName, objectToPointTo ):
        '''Adds a variable to the stack'''
        
        #Check if the var is already in the stack
        if self.priGetVar(varName) != None:
            #So the var is in the stack replace it

            #If we already have a connection we should close it 
            for i in range((len(self.__stack) -1), -1, -1 ):
                if varName in self.__stack[i]:
                    self.__stack[i][varName].close()
                    self.__stack[i][varName] = None
                    self.__stack[i][varName] = objectToPointTo
                    log.debug("Modified variable " + str(varName) + \
                              " to point to " + str(objectToPointTo)) 
        
        else: #Var is not in the stack so add it
            #Add the new connection Object
            self.__stack[(len(self.__stack) - 1)][varName] = objectToPointTo
            log.debug("Added new variable " + str(varName) + \
                      " pointing to " + str(objectToPointTo) + " in level " + \
                      str(len(self.__stack) - 1))
            
            log.debug( "====================================")
            log.debug( self.dump_stack())
            log.debug( "====================================")
            log.debug( self.getVar(varName))
            log.debug( "====================================")
            
            
    def priGetVar(self, varName):
        '''This method does not return an error string'''
        returnObj = None
        
        
        for i in range((len(self.__stack)-1), -1, -1 ):
            if varName in self.__stack[i]:
                returnObj = self.__stack[i][varName]
                return returnObj
            
        return returnObj
    
                    
    def getVar(self, varName):
        '''Gets the variable from the stack or errors'''
        returnVal = self.priGetVar(varName)
        
        if returnVal == None:
            #So we have not found the name in the var stack
            log.error("Var name not found in stack: " + str(varName))
            log.error( "====================================")
            log.error( self.dump_stack())
            log.error( "====================================")
        
        
        return returnVal
        
        
        
    def __del__(self):
        for i in xrange(0, len(self.__stack)):
            for j in self.__stack[i]:
                self.__stack[i][j].close()
            
        #Close all remaining connections
    
    def cleanStackLevel(self):
        '''Cleans up all the connections'''
        if len(self.__stack) == 0:
            return
        
        for k, v in self.__stack[ len(self.__stack) -1].iteritems():
            #log.debug(str(k) + " still open")
            v.close()

    def deepCleanStack(self):
        '''Cleans the hole stack'''
        while (len(self.__stack) - 1) > 0:
            self.popStack()
        
    
    def __str__(self):
        
        #log.debug("======STACK=======")
        #log.debug(self.dump_stack())
        #log.debug("==================")
        return "CLASS: " + str(self.__name)


