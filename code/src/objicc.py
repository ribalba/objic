#!/usr/bin/python

'''The Compiler'''

__version__ = "$Revision: 188 $"

# ObjiC $Id: objicc.py 188 2009-05-21 00:40:52Z didi $
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

#For the serial output
import cPickle

#For the command line options
import sys

#For buiilding the AST
import antlr3

#From antlr
from ExprLexer import ExprLexer
from ExprParser import ExprParser

if str(sys.argv[1]).strip() == "-v":
    print __version__
    sys.exit()

if str(sys.argv[1]).strip() == "-h":
    print "This is the objic compiler"
    print "All the documentation has moved to the man pages"
    print "Plese use: man objicc"
    sys.exit()


debug = 0

if str(sys.argv[1]).strip() == "-d":
    debug = 1
    sys.argv.remove(sys.argv[1])

if len(sys.argv) == 1:
    print ("Please specify a file to compile")
    sys.exit()

char_stream = antlr3.ANTLRFileStream(sys.argv[1])

lexer = ExprLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = ExprParser(tokens)
r = parser.prog()

root = r.tree
nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)

#We know the 3rd token is the class name
output = open("./uclasses/" +(str(nodes.get(2).getText()) + ".rti") , 'wb', -1)

#dunp it
cPickle.dump(nodes, output)

#Close the file
output.close()


if debug == 1:
    
    tab = ""
    
    for i in range(0, nodes.size()):
        if nodes.get(i).getText() == "DOWN":
            tab = tab + "   "
        if nodes.get(i).getText() == "UP":
            tab = tab[0:(len(tab) - 3)]
        
        print tab + str(nodes.get(i).getText())
