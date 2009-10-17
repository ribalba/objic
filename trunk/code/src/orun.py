#!/usr/bin/python

'''The class that runs an object'''

__version__ = "$Revision: 78 $"

# ObjiC $Id: oObject.py 78 2009-04-14 21:41:46Z didi $
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
if len(sys.argv) == 1:
    print ("Please specify a file to compile")
    sys.exit()

if str(sys.argv[1]).strip() == "-v":
    print __version__
    sys.exit()

nomain = 0
if str(sys.argv[1]).strip() == "-nm":
    nomain = 1
    sys.argv.remove("-nm")


if str(sys.argv[1]).strip() == "-h":
    print "This is the objic runner"
    print "All the documentation has moved to the man pages"
    print "Plese use: man orun"
    sys.exit()



if str(sys.argv[1]).strip() == "-d":
    logLevel = globalConf.logging.DEBUG

if len(sys.argv) == 1:
    print ("Please specify a file to compile")
    sys.exit()



from ObjManager import ObjManager

params = "VOID"

if len(sys.argv) == 3:
    params = sys.argv[2]
    
if len(sys.argv) == 1 :
    print ("Please specify a class to run")
    sys.exit()

objman = ObjManager()

objptr = objman.newObj(sys.argv[1], "VOID", globalConf.serverName )

if objptr == "404":
    print("Class not found")
    sys.exit()

obcon = objman.connectToObj(objptr)

retval = ""
if nomain == 0:
    retval = obcon.callMethod("main", params)

if retval[:3] == "404":
    print("Main not found")
    sys.exit()

if len(retval.split(":")) >=2: 
    objretval = objman.connectToObj(retval.split(":")[1])

    retValreal = objretval.callMethod("value", "VOID")

    print retValreal

    objretval.close()

obcon.close()


