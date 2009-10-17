''' The class that parses the AST and calls the appropriate methods. Normally
 one interpreter is called for one object '''

__version__ = "$Revision: 188 $"

#ObjiC $Id: Interpreter.py 188 2009-05-21 00:40:52Z didi $
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

import cPickle

#import antlr3

import sys
#from types import *

#Import all the Tokens
from ExprLexer import CLASS, DOWN, UP, BLOCK, EQ, NEWOBJ, \
                      CALL, PTRASS, PARAMS, IFTEST,BOOL, \
                      WHILE, BREAK, ELSE, NEWLINE, PRINTSTM, \
                      OSTRING, NAME, SERVERNAME, METHDEF, RETURNSTM
                      
from oClass import oClass
from ObjManager import ObjManager
from MethObject import MethObject

#The global configuration file
import globalConf

#Some os stuff
import os


#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("Interpreter")
log.setLevel(globalConf.logLevel)


class Interpreter:
    ''' The class that deals with interpreting the AST'''

    #The tree we interpreter 
    __parseTree = ""
    
    #Where we are in that tree
    __posInTree = 0
    
    #The object manager that is used for connections and suck
    __objman = ObjManager()
    
    #The object that represents the interpreter
    myClass = None
    
    #So stuff can be passed down the stack like a break call
    stackMessage = ""
    
    vmName = "VOID"

    #The old way
    #def __init__(self, nodesToAdd):
        #self.__parseTree = nodesToAdd

    def __init__(self):
        pass
    
    def setName(self, vmDesc):
        '''Sets the name of the base Vm'''
        self.vmName = vmDesc
    
    def getName(self):
        '''Returns the name of the base Vm'''
        return self.vmName
    
    def pathToMe (self):
        '''Returns the object pointer to itself'''
        return globalConf.serverName + "/" + self.vmName 
    
    
    def getNode(self):
        '''Gets the current node'''
        return self.__parseTree.get(self.__posInTree)
        
    def getNextNode(self):
        '''Returns the next node and progresses one in the tree'''
        self.__posInTree = self.__posInTree + 1
        return self.getNode()
        
    def hasNextNode(self):
        '''Checks if there is another node'''
        return (self.__parseTree.size() >= self.__posInTree + 2 )
    
    def printTree(self):
        '''Prints a nice indented version of the AST'''
        tab = ""
        for i in range(0, self.__parseTree.size()):
            if self.__parseTree.get(i).getText() == "DOWN":
                tab = tab + "   "
            if self.__parseTree.get(i).getText() == "UP":
                tab = tab[0:(len(tab) - 3)]

            #print tab + str( nodes.get(i).getType()  ),
            print tab + str(self.__parseTree.get(i).getText())
            
    def checkIfNextIsDown(self):
        '''A wrapper to see if the next node is pf type DOWN'''
        if self.getNextNode().getType() != DOWN:
            log.error("Tree struckture not ok, Down Token : " \
                      + str(self.getNode()))
    
    def checkIfNextIsUp(self):
        '''A wrapper to see if the next node is pf type UP'''
        if self.getNextNode().getType() != UP:
            log.error("Tree struckture not ok, Up Token : " \
                      + str(self.getNode()))
     
    def findBlockbounds(self):
        '''Finds the position in the tree when to stop for the block'''
        scount = 0
        
        #Catch if we are not positioned at a BLOCK
        if self.getNode().getType() != BLOCK \
            and self.getNode().getType() != BOOL:
            log.error("Trying to find a block but not passed in a block :" + \
                      str(self.getNode()) )
        
        i = self.__posInTree + 1
        while True: 
            if self.__parseTree.get(i).getText() == "DOWN":
                scount = scount + 1 
            elif self.__parseTree.get(i).getText() == "UP":
                scount = scount - 1
            
            #We have a block
            if scount == 0:
                return i
            
            #otherwise we keep on searching
            i = i + 1
     
    def getParameters(self):
        '''Creates a string representation from the params tokens'''
        
        #Next should be the token PARAMS
        if self.getNextNode().getType() != PARAMS:
            log.error( "No paramters given something funky, VOID assumed ")
                       
        paramStr = ""
         #We have some parameters
        if self.getNextNode().getType() == DOWN:
            while self.getNextNode().getType() != UP:
                #check if it is a variable
                varCheck = self.myClass.priGetVar(self.getNode().getText())
                if varCheck != None:
                    #It seams like we have a var
                    #Check if it is a method obj
                    if isinstance(varCheck, MethObject):
                        paramStr = paramStr + varCheck.call()
                    else:
                        log.error("Trying to get value from non Methob :" + \
                                  str (varCheck))
                else:
                    paramStr = paramStr + self.getNode().getText() + " "
        else:
            paramStr = "VOID"
            
        return paramStr
     
     
    def resovelCallTree(self):
        '''A wrapper for the CALL token and the following parameters'''
        if self.getNextNode().getType() == CALL:
            self.checkIfNextIsDown()
            
            varNameToCall = self.getNextNode().getText()
            methodToCall = self.getNextNode().getText()
            parameters = self.getParameters()
            
            return self.callMethodWrapper(varNameToCall, \
                                          methodToCall, parameters)
        else:
            log.error("The CALL didn't seam to work")    

     
    def checkBool(self, startpos, endpos):
        '''Check the BOOL token'''
        
        self.__posInTree = startpos
        
        self.checkIfNextIsDown()
        
        #This can be '==', '!=', '<', '>', and so on
        typeOfCompare = self.getNextNode().getText()
        
        firstVal = self.resovelCallTree()
        
        secondVal = self.resovelCallTree()
        
        self.checkIfNextIsUp()
        #self.checkIfNextIsUp()
        
        if self.__posInTree > endpos:
            log.error("Somehow the checkBool went over the end position")
        
        log.debug(str(firstVal) + typeOfCompare  + str(secondVal))
        
        #This might be a performance hit ?!?
        return eval(str(firstVal) + typeOfCompare  + str(secondVal))

         
    def callMethodWrapper(self, varName, method, parameterStr):
        '''calls a methos on a specific varibale on the stack'''
        log.debug( "New call " + str(varName) + " method " + str(method)  )

        #self.checkIfNextIsDown()
                    
        #check if the object is in myCalss var
        # get the connection obj is existent
        conObj = self.myClass.getVar(varName)
                    
        #Some error checking
        if conObj == None:
            log.error("Could not get the correct obj from the stack. Token: " \
                      + str(varName))

                    
        methodToCall = method
                    
                    
        log.debug( "CALLING METHOD: " + methodToCall + " with " + parameterStr)
        
        # call the call Funct on the ob with the params
        conreply =  conObj.callMethod(methodToCall, parameterStr)
              
        return conreply    
  
    def printRange(self, a, b):
        '''Prints the range of the AST defined by a and b'''
        log.debug("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        buff = ""
        for i in range(a, b):
            buff = str(self.__parseTree.get(i)) + " "
        log.debug(buff)
        log.debug( "\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    
    def handleCall(self):
        '''Is called as soon as we encounter the CALL token'''
        
        if not self.getNode().getType() == CALL:
            log.error("Called handleCall without a call, Token:" \
                      + str(self.getNode()))
            return None
        
        self.checkIfNextIsDown()
        
        varNameToCall = self.getNextNode().getText()
        methodToCall = self.getNextNode().getText()
        parameters = self.getParameters()
                    
        conn_obj = self.myClass.getVar(varNameToCall)
        
        if(conn_obj == None):
            return None
        
        methodObj = MethObject(conn_obj.ptr(), methodToCall, parameters)
                    
        #Call the dam thing
        return methodObj    
        
        
    def parseBlock(self, startposition, stopposition, isMethod=False):
        '''This is so we can parse blocks independentelly'''
        
        #self.printRange(startposition, stopposition)
        
        #Set the ptr to the startPos
        self.__posInTree = startposition
        
        #First thing we raise the stack
        self.myClass.raiseStack()
        
        #And get rid of the first BLOCK token
        if self.getNode().getType() != BLOCK:
            log.error("No block; Token given:" + str(self.getNode().getText()))
         
        self.getNextNode()
        
        #And start parsing till we hit end of file or the stop position
        while self.hasNextNode() and (self.__posInTree < stopposition-1) :
            if self.getNode().getType() == BLOCK:
                self.parseBlock(self.__posInTree, self.findBlockbounds())
###EQ#######  
            elif self.getNode().getType() == EQ:
                self.checkIfNextIsDown()
                
                #Once we have construced everything we add the var to myClass
                varname = self.getNextNode().getText()
                
                wtd = self.getNextNode().getType()
                
                if wtd == NEWOBJ:
                    serverName = ""
                    
                    isServer = self.getNextNode()
                    
                    if isServer.getType() == SERVERNAME:

                        #Server specified with @NAME
                        self.checkIfNextIsDown()
                        serverName = self.getNextNode().getText() +\
                                    self.getNextNode().getText() + \
                                    self.getNextNode().getText() 
                        self.checkIfNextIsUp()
                        isServer = self.getNextNode()
                    
                    conn_obj = self.__objman.connectToObj( \
                        self.__objman.newObj(isServer.getText(), \
                                             self.getParameters(), serverName))
                    
                    self.myClass.addVar(varname, conn_obj)
                    
                if wtd == CALL:
                    
                    conMethObj = self.handleCall()
                    
                    conreply = conMethObj.call()
                    
                    if conreply.split(":")[0] == "NEWOBJ":
                        #we have to add a new object to the stack
                        
                        log.debug("NEWOBJ in rpl: " + str(conreply))
                        #connect
                        #connObj2 = self.__objman.connectToObj(\
                        #                             conreply.split(":")[1])
                        
                        connObj2 = MethObject(conreply.split(":")[1], \
                                              "value", "VOID")
                        #And add it to the stack
                        self.myClass.addVar(varname, connObj2)

                        conMethObj.close()
                        
                    else:
                        
                        self.myClass.addVar(varname, conMethObj)
                        
                        #print "CALLRPL: " + str(conreply)   
                
                
                if wtd == PTRASS:
                    log.debug( "New ptrassign")
                    
                    #check if the object is in myCalss var
                    # get the connection obj is existent
                    conObjlol = self.myClass.getVar(\
                                                self.getNextNode().getText())
                    
                    #Some error checking
                    if conObjlol == None:
                        log.error("Could not get the obj fromstack. Token: " \
                                  + str(self.getNode()))
                        break
                     
                    self.myClass.addVar(varname, conObjlol)   
                    
###IF#######
            elif self.getNode().getType() ==  IFTEST :
                log.debug( "If call")
                
                haseElse = False
                
                self.checkIfNextIsDown()
                    
                if self.getNextNode().getType() != BOOL:
                    log.error("An if statement always needs a boolean")
                        
                #Check the boolean
                boolToF = self.checkBool(\
                                    self.__posInTree, self.findBlockbounds())
                
                #Add one so we are on the block
                self.__posInTree += 1 

                
                trueBlockStart = self.__posInTree
                trueBlockEnd = self.findBlockbounds()
                
                self.__posInTree =  trueBlockEnd + 1             
                

                if self.getNode().getType == ELSE:
                    self.__posInTree = self.__posInTree + 1
                    #It seams like we have a else block
                    falseBlockStart = self.__posInTree
                    falseBlockEnd = self.findBlockbounds()
                    haseElse = True
                
                    #Set the current pointer past all this
                    self.__posInTree = falseBlockEnd + 1              

                
                if boolToF == True:
                        
                    #We execute the true block
                    self.parseBlock(trueBlockStart, trueBlockEnd)
                    
                else:
                    if haseElse == True:
                        #We execute the false block
                        self.parseBlock(falseBlockStart, falseBlockEnd)
                    
                
                #Set the pointer to the end of all this
                if haseElse == True:
                    self.__posInTree = falseBlockEnd
                else:
                    self.__posInTree = trueBlockEnd
            
###WHILE#### 
            elif self.getNode().getType() ==   WHILE:
                log.debug( "While loop")
                
                self.checkIfNextIsDown()

                if self.getNextNode().getType() != BOOL:
                    log.error("An while loop needs a boolean as parameter")
                        
                #Find out where the bool block is so we can test it
                startBool = self.__posInTree
                endBool = self.findBlockbounds()
                
                #Add one so we are on the block
                self.__posInTree =  endBool + 1

                #The block to execute
                startBlock = self.__posInTree
                endBlock = self.findBlockbounds()
                
                #Lucky we are an interpreter and can just do a while loop too
                while self.checkBool(startBool, endBool):
                    self.parseBlock(startBlock, endBlock)
                    if self.stackMessage == "BREAK":
                        break

            
                #Move the ptr to the end of so we don't parse it once too much
                self.__posInTree = endBlock + 1


###BREAK####             
            elif self.getNode().getType() == BREAK:
                log.debug("break statement")
                #pass
                #Exit from stack
                self.stackMessage = self.getNode().getText()
                self.__posInTree = stopposition  
                self.myClass.popStack()
                return

###NEWLINE##                         
            elif self.getNode().getType() == NEWLINE:
                #We don't really care about new lines
                pass

###DOWNUP##            
            elif self.getNode().getType() == DOWN \
                or self.getNode().getType() == UP:
                #We don't really care about the tree
                pass


###METHDEF##            
            elif self.getNode().getType() == METHDEF:
                log.debug("Method defined")
            
                self.checkIfNextIsDown()
                
                methodName = self.getNextNode().getText()
                
                #Move one to the BLOCK token
                self.getNextNode()
                
                startMeth = self.__posInTree
                endOfMeth = self.findBlockbounds()
                
                self.__posInTree = endOfMeth
                
                self.myClass.addMethod(methodName, startMeth, endOfMeth)


###CALL#####            
            elif self.getNode().getType() == CALL:
                selfCallObj = self.handleCall()
                return selfCallObj.call()


###RETUNR###                
            elif self.getNode().getType() ==  RETURNSTM:
                log.debug("Return stm")

                self.checkIfNextIsDown()
               
                whatToRet = self.getNextNode()
                
                if whatToRet.getType() == NAME: 
                    #We can assume that this has to be a ptr to a MethObject
                    methPtr = self.myClass.getVar(whatToRet.getText())
                    
                    #But we check
                    if not isinstance(methPtr, MethObject):
                        log.error("Type is not MethodObject")
                    else:
                        rtVal = methPtr.call()
                        objretptr = self.__objman.newObj("String", str(rtVal))
                        self.stackMessage = "BREAK:" + str(objretptr)
                        #self.myClass.popStack()
                        #return "NEWOBJ:" + str(objretptr)
                        break
                else:
                    log.error("return has to have a methobj")
                    return "VOID"
            
            
###PRINT####            
            elif self.getNode().getType() == PRINTSTM:
                log.debug("Print stm")            
                
                self.checkIfNextIsDown()
                
                whatPrint = self.getNextNode()
                
                toPrint = ""
                
                #3 cases call, NAME, String
                if whatPrint.getType() ==  OSTRING:
                    self.checkIfNextIsDown()
                    theStringToPrint = self.getNextNode()
                    
                    toPrint = theStringToPrint.getText().strip("\"")
                    
                elif whatPrint.getType() == NAME:
                    
                    #We can assume that this has to be a ptr to a MethObject
                    methPtr = self.myClass.getVar(whatPrint.getText())
                    
                    #But we check
                    if not isinstance(methPtr, MethObject):
                        log.error("Type is not MethodObject")
                    else:
                        toPrint = methPtr.call()
                    
                elif whatPrint.getType() == CALL:

                    #self.checkIfNextIsDown()
                    #print "AHHHH CALL" 
                    callPtr =  self.handleCall()
                    #print "LOLOL: " + str(callPtr) 
                    toPrintPointer = callPtr.call()
                    
                    if len(str(toPrintPointer).split(":")) > 1:
                        objretptr = self.__objman.connectToObj( \
                                            toPrintPointer.split(":")[1])
                        toPrint = objretptr.callMethod("value","VOID")
                    
                        objretptr.close()
                    else:
                        toPrint = toPrintPointer
                    #print "TOPRINT: " + str(toPrint)
                    
                    callPtr.close()
                
                else:
                    log.error("Not known print parameter")
                
                print str(toPrint)

            
            #And if we don't know what to do with it shout
            else:
                print "Can't handle: " + \
                    str(self.getNode().getText()) \
                    + "(" + str(self.getNode().getType()) \
                    + ")" + " : " + str(self.getNode().getLine())
                
            
            if self.stackMessage.split(":")[0] == "BREAK":
                #self.stackMessage = self.stackMessage.split(":")[1]
                break
            
            self.getNextNode()
            
        #Pop the stack, pretty much the last thing we do
        self.myClass.popStack()
        
        #print "STACK MESSAGE: " + self.stackMessage
        
        if self.stackMessage == "VOID" :
            return "VOID"
        
        if self.stackMessage != "" :
            if self.stackMessage.split(":")[0] == "BREAK":
                log.debug("We seam to have a return")

            #We are in a mathod so stop recursion
            if isMethod == True:
                
                retStackRet = str(self.stackMessage.split(":")[1])
            
                #And reset for reuse :)
                self.stackMessage = ""

                return "NEWOBJ:" + retStackRet
        
        elif self.stackMessage == "":
            self.stackMessage = "VOID"
        
        else:
            log.error("Cannot understand stack message: "+  self.stackMessage)
                  
        return self.stackMessage
        
    def  callFunction(self, name, params):
        '''A interpreter local call to call int methods'''
        retval = "VOID"
      
        if self.myClass == None:
            return "404"        
        
        #Check if it is a built in
        if name == "rep":
            return "<Instance>: " + str(self.myClass.getName())
        
        currPos = self.__posInTree
        

        
        retVal = self.myClass.getMethod(name)

        #save the stack
        #bufferStack =  self.myClass.getStack()
        
        #reset the stack
        #self.myClass.setStack([{}])
        
        if retVal == None:
            log.error("Method not found: " + name)
            return "404 Method not found"
        
        conn_obj = self.__objman.connectToObj( \
                        self.__objman.newObj("String",str(params),"localhost"))
                    
        self.myClass.addVar("ARGS", conn_obj)
        
        
        
        startBock, stopBlock = self.myClass.getMethod(name)
        
        
        retval = self.parseBlock(startBock, stopBlock, True)

        #print "AHHH callFunction:" + str(retval)
        
        if retval == None:
            retval = "VOID"
            
        self.__posInTree = currPos
        
        return retval
        

    def run(self, className):
        '''Start the interpretation'''
        if not os.path.exists("./uclasses/" + str(className) + ".rti"):
            log.debug("Tried calling a non existing class")
            return("404")
        
        #Load the binary file
        pkl_file = open("./uclasses/" + str(className) + ".rti", 'rb')

        nodes = cPickle.load(pkl_file)
        
        self.__parseTree = nodes
        
        pkl_file.close()

        #self.printTree()
        #print "++++++++++++++++++++++++++++++++++++++++"
        
        #
        #Here we go and handle all the stuff
        #
        while self.hasNextNode():
            if self.getNode().getType() == CLASS :
                self.myClass = oClass()
                
                self.checkIfNextIsDown()
                
                self.myClass.setName(self.getNextNode().getText())
        
            elif self.getNode().getType() == BLOCK :
                #Setup some global variables for the class                
                conn_obj = self.__objman.connectToObj( \
                        self.__objman.newObj("String","VOID","localhost"))
                    
                self.myClass.addVar("STDOUT", conn_obj)
                
                meObj = self.__objman.connectToObj(self.pathToMe())
                
                self.myClass.addVar("ME", meObj)           
                
                self.parseBlock(self.__posInTree, self.findBlockbounds(), True)
                
            self.getNextNode()
                
        
        
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print ("Please specify a class to run")
        sys.exit()
    
    #Create a new instance and run
    runner = Interpreter()
    runner.run(sys.argv[1])