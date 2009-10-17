'''The class that handles all the low level object connection'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: ObjConnection.py 188 2009-05-21 00:40:52Z didi $
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
log = logging.getLogger("ObjConnection")
log.setLevel(globalConf.logLevel)

import socket

class ObjConnection:
    '''The class that handles all the low level object connection'''

    __sock  = ""
    __ptr   = ""

    def __init__(self, whereTo):
        self.connect(socket.gethostbyname(whereTo), 8080)
      
      
    def connect(self, ip, port):
        '''Connects to an ip'''
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((ip, port))

    def sendMsg(self, message):
        '''Sends a message to the connection'''
        self.__sock.send(message)
        response = self.__sock.recv(1024)
        return response
        
        
    def close(self):
        '''Closes the socket'''
        if  self.__sock != "" :
            #Do some error catching
            try:
                self.__sock.send("END")
                self.__sock.close()
            except socket.error :#, (value, message):
                pass
                #log.info("Tried to close an  closed socket: " + str(message))

        
    def ptr(self):
        '''Returns the ptr'''
        return self.__ptr
    
    def setPtr(self, name):
        '''Sets the ptr'''
        if self.__ptr != "":
            log.error("Someone is trying to reset the ptr")
            
        self.__ptr = name
        
        
    def callMethod(self, name, params):
        '''Calls a method'''
        log.debug("Calling " + name + " on " + self.__ptr + " with " + params)
        
        if self.sendMsg("CALL") != "what method?":
            log.error("Server is funny, doesn't want to know the method")
        
        if self.sendMsg(name) != "param str please?":
            log.error("Server is funny, doesn't want to know the parameters")
            
        return self.sendMsg(params)
        

    
    def __repr__(self):
        '''A nice representation'''
        return "ObjConnection:" + str (self.__ptr)
    
    def __del__(self):
        pass
        # self.close()
