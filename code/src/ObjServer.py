#!/usr/bin/python

'''The server that is multithreaded and creates vm instances for objects'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: ObjServer.py 188 2009-05-21 00:40:52Z didi $
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

import socket
#import threading
import SocketServer

#The global configuration file
import globalConf


#import threading

import sys

#Some logging
import logging
logging.basicConfig()
log = logging.getLogger("ObjServer")
log.setLevel(globalConf.logLevel)


from oVm import oVm 

#This is the object hash where there are still connections too
objectHash = {} # 'PTGXMV': <oInt> 5

#This is the hash where all the objects are kept to which 
# there are no references too.
oldObjectHash = {} # 'PTGXMV': <oInt> 5

#This is the hash that holds ptr to the request handlers to see if they are 
# still active
vmHash = {}  #'PTGXMV': [RequestHandle1, RequestHandle2]

class globalServer:
    '''This is a global class this how globals can be done in python'''
    server = None
    
    def __init__(self):
        '''Nothing to do right now'''
        pass
    
    def isServerSet(self):
        '''Returns if the server is set'''
        return self.server == None

    def setServer(self, serverToSet):
        '''can set the server'''
        self.server = serverToSet

#class shutMeDown:
#    '''Just a class wrapper'''
#    value = 0
    

def addVm(objHashName, objReference):
    '''Adds another vm to the vmHash'''
    if objHashName in vmHash:
        vmHash[objHashName].append(objReference)
    else:
        vmHash[objHashName] = [ objReference ]
        
def remVm(objHashName, objReference):
    '''Removes a vm when the connection exits'''
    vmHash[objHashName].remove(objReference)
    
    #If there is nothing referencing it anymore move to oldHash
    #This can be optimized as we call new object move this to the old stack
    #and then normally the next call will be connect so we move it to 
    #the used stack again
    try:
        if vmHash.has_key(objHashName):
            if len(vmHash[objHashName]) == 0:
                if objHashName in vmHash:
                    vmHash.pop(objHashName)
                    moveVmtoOld(objHashName)
    except KeyError:
        log.debug("!!! KeyError !!! I have no idea why this is happening")

def moveVmtoOld(objHashName):
    '''Moves an unused VM to the oldVm hash'''
    oldObjectHash[objHashName] = objectHash.pop(objHashName)


def moveVmToUsed(objHashName):
    '''Moves an old Vm to usedVms'''
    if objHashName in oldObjectHash:
        objectHash[objHashName] = oldObjectHash.pop(objHashName)
        return True
    else:
        return False


def printStackInfo():
    '''Prints out some info about the server'''
    log.debug("---------------VM STACK INFO------------------")
    log.debug("Active Obj  :" + str(objectHash))
    log.debug("Inactive Obj: " + str(oldObjectHash))
    log.debug("Connections :" + str(vmHash))
    log.debug("----------------------------------------------")


class RequestHandler(SocketServer.BaseRequestHandler):
    '''A thread for every connection'''
    #The url of the server
    __serverName = globalConf.serverName
    __vm = None
    
    #Init
    def setup(self):
        '''Not really much to do in setup'''
        pass

    #Do it
    def handle(self):
        '''This is called on init'''

        DATASIZE = 65536


        while True: # and shutMeDown.value == 0:
            data = self.request.recv(DATASIZE)
            log.debug("-" + data + "-")
            
            #Remove all those white spaces
            data = data.strip()
            if data == "KILL":
                print "TRYING TO KILL"
                #shutMeDown.value = 1
                self.request.send("Tried to Kill")
                

                
            if data == "END":
                #self.request.send("END")
                break
            
            elif data == "CREATE":
                # Send empty so we can find the type
                self.request.send("what type?")
                
                objectTyp = self.request.recv(DATASIZE).strip()

                #Ask for the string of parameters 
                self.request.send("parameters please?")
                
                objectParameters = self.request.recv(DATASIZE).strip()
                

                #Create new Obj
                self.__vm = oVm(objectTyp, objectParameters)
                
                #Add to the global hash
                objectHash[self.__vm.getName()] = self.__vm
                
                #Add this connection to the connection hash
                addVm(self.__vm.getName(), self)
                
                
                #call the constructot
                if self.__vm.constructor() == "404":
                    self.request.send("404")
                else:
                    log.debug("New object: " + objectTyp + " with " + \
                          objectParameters + " Named: " + \
                          str(self.__vm.getName()))
                
                    self.request.send(self.__serverName +"/"+ self.__vm.getName())
                
                
            elif data.strip() == "CALL":
                # Send empty so we can find the type
                self.request.send("what method?")
                                   
                whatToCall = self.request.recv(DATASIZE).strip()
                
                self.request.send("param str please?")

                params = self.request.recv(DATASIZE).strip()
                
                self.request.send(str(self.__vm.call(whatToCall, params)))
                
            #Connect to Obj
            elif data.strip() == "CONNECT":
                
                 # Send empty so we can find the what obj to connect to
                self.request.send("what object?")
                
                whatObject = self.request.recv(DATASIZE).strip()
                
                #Check if obj is in the current Hash
                if whatObject not in objectHash:
                    #Otherwise try to get it back
                    if moveVmToUsed(whatObject) == False:
                        #If this fails error and the bottom part will to fail
                        log.error("Trying to access an obj that " + \
                                  "doesn't exist: " + str(whatObject))

                
                if whatObject in objectHash:
                    #Assign the VM
                    self.__vm = objectHash[whatObject]
                    
                    #Add this connection to the connection hash
                    addVm(self.__vm.getName(), self)                    
                    
                    self.request.send("connected to object")
                else:
                    self.request.send("404")
                    

                
            elif data == "":
                
                print self.__vm
                try:
                    self.request.send("NO COMMENT")
                except socket.error:
                    #NOTE replace the pass with a break if you want to 
                    #avoid the infinite loop problem 
                    #pass  
                    break
            
            else:

            
                #Del obj
            
                #cur_thread = threading.currentThread()
            
                #response = "%s: %s" % (cur_thread.getName(), data)
                self.request.send("NO COMMENT")
                #pass
        
        if self.__vm == None:
            log.error("Why do we have a none vm?")
        else:
            #Remove from vmHash
            remVm (self.__vm.getName(), self)
        
        
        
        self.cleanUp()
        
    def cleanUp(self):
        '''Closes all the connections, called when server goes downn'''
        
        self.request.close()
        
        self.finish()

    def __repr__(self):
        return str(self.client_address)

class Initializer:
    '''This is the actual server class'''

    globalServer.server = \
        SocketServer.ThreadingTCPServer(('', 8080), RequestHandler)
    
    def __init__(self):
        pass
    
    def getServer(self):
        '''Returns the server instance: for debugging'''
        return globalServer.server
    
    def start_server(self):
        '''Starts and stopps the server'''
#        try:
        globalServer.server.serve_forever()
 #       except:
        #globalServer.server.shutdown() #pylint: disable-msg=E1101 

    def __del__(self):
        pass

if __name__ == "__main__":
    
    #Not nice but it works
    if len(sys.argv) == 1:
        sys.argv.append("VOID")
    
    if str(sys.argv[1]).strip() == "-v":
        print __version__
        sys.exit()

    if str(sys.argv[1]).strip() == "-h":
        print "This is the objic compiler"
        print "All the documentation has moved to the man pages"
        print "Plese use: man ObjServer"
        sys.exit()


    if str(sys.argv[1]).strip() == "-d":
        log.setLevel(logging.DEBUG)
        

    a = Initializer()
    a.start_server()

    
