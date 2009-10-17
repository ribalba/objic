'''The class that manages all the calls to other object servers'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: ObjManager.py 188 2009-05-21 00:40:52Z didi $
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
import antlr3

#The global configuration file
import globalConf

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("ObjManager")
log.setLevel(globalConf.logLevel)

from ObjConnection import ObjConnection

#Module specific
from ObjlocLexer import ObjlocLexer
from ObjlocParser import ObjlocParser

#Tokens
from ObjlocLexer import NEWDEF

class ObjManager:
    '''Object management methods like create and connect'''
    
    __objectLoc = {}

    
    def __init__(self):
        #TODO: Change this to be inculded in the Bin ary file
        char_stream = antlr3.ANTLRFileStream("../../../../objic/ObjLocFile")

        lexer = ObjlocLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = ObjlocParser(tokens)
        r = parser.file()

        root = r.tree

        nodes = antlr3.tree.CommonTreeNodeStream(root)
        nodes.setTokenStream(tokens)

        for i in range(0, nodes.size()):
            if nodes.get(i).getType() == NEWDEF:
                i = i + 2 #Skip the DOWN
                self.__objectLoc[nodes.get(i).getText()] = \
                nodes.get(i = i + 1).getText()
                
        log.debug(str(self.__objectLoc))

    def newObj(self, typeOfObj, params, serverRequest= ""):
        '''Create a new Object and return ptr'''

        createWhere = ""
        #See if we know where to initialize it

        if serverRequest != "":
            createWhere = serverRequest
        elif self.__objectLoc.has_key(typeOfObj):
            createWhere = self.__objectLoc[typeOfObj]
        else: #we assume localhost
            createWhere = "localhost"

        # Create new connection Object
        newObj = ObjConnection(createWhere)
        
        # Send "NEW type"
        if newObj.sendMsg("CREATE") != "what type?" :
            log.error("Server error, doesn't want to know which type")
     
            
        # Send type
        if newObj.sendMsg(typeOfObj) != "parameters please?":
            log.error("Server error, doesn't want to know the parameters")

        
        #Send paramters
        objPtr = newObj.sendMsg(str(params))
        
        if objPtr == "404":
            newObj.close()
            return objPtr
        
        newObj.setPtr(objPtr)

        #Close the connection
        newObj.close()

        #Return the New connection object 
        return newObj.ptr()
 
    
    def connectToObj(self, oUrl):
        '''Connect to an object'''
        
        #split up url
        hostName , objHash = oUrl.split("/")
        log.debug ("CONNECTING TO:" + hostName + " " + objHash)
        
        # Create new connection Object
        newObjC = ObjConnection(hostName)
        
        if newObjC.sendMsg("CONNECT") != "what object?":
            log.error("Server doesn't want hash")
            
        # send Hash and hope we are connected with the obj
        if newObjC.sendMsg(objHash) != "connected to object":
            log.error("Server doesn't allow connect")
        
        newObjC.setPtr(oUrl)
        
        return newObjC
        
        