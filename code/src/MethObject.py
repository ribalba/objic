'''The class that extends the connection and provides a connection 
to a method'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: MethObject.py 188 2009-05-21 00:40:52Z didi $
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


from ObjConnection import ObjConnection

class MethObject(ObjConnection):
    '''This is the object that wraps a method call to a connection'''
    
    methodToCall = None
    parameters = "VOID"
    
    def __init__(self, conString, methodToCall, parameters):

        #split up url
        hostName , objHash = conString.split("/")
        log.debug ("CONNECTING TO:" + hostName + " " + objHash)
        
        # Create new connection Object
        ObjConnection.__init__(self, hostName)
        
        if self.sendMsg("CONNECT") != "what object?":
            log.error("Server doesn't want hash")
            
        # send Hash and hope we are connected with the obj
        if self.sendMsg(objHash) != "connected to object":
            log.error("Server doesn't allow connect")
        
        #Set the obj prt
        self.setPtr(conString)

        #Assign all the local vars
        self.methodToCall = methodToCall
        self.parameters = parameters
        
    def call(self):
        '''Calls the method specified at creation from its self'''
        #print "----------"
        #print "Calling " + self.methodToCall
        #print str(self.callMethod(self.methodToCall, self.parameters))
        #print "----------"
        return self.callMethod(self.methodToCall, self.parameters)
        
    
    def __repr__(self):
        return "MethObject:" + \
            str(self.ptr())+":"+self.methodToCall+"(" + self.parameters + ")"