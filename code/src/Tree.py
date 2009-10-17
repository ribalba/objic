# $ANTLR 3.1.2 /home/didi/fyp/code/LexParse/Tree.g 2009-03-15 17:10:20

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
CLASS=10
T__26=26
T__25=25
LINE_COMMENT=15
T__24=24
T__23=23
T__22=22
T__21=21
T__20=20
NEWOBJ=7
INT=13
EOF=-1
T__19=19
NAME=11
WS=16
NEWLINE=12
T__18=18
T__17=17
IFTEST=9
BLOCK=4
CALL=8
EQ=5
COMMENT=14
PARAMS=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "BLOCK", "EQ", "PARAMS", "NEWOBJ", "CALL", "IFTEST", "CLASS", "NAME", 
    "NEWLINE", "INT", "COMMENT", "LINE_COMMENT", "WS", "'{'", "'}'", "'if'", 
    "'('", "')'", "'else'", "'='", "'new'", "'.'", "','"
]




class Tree(TreeParser):
    grammarFileName = "/home/didi/fyp/code/LexParse/Tree.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)




        self.memory = {}



                


        



    # $ANTLR start "prog"
    # /home/didi/fyp/code/LexParse/Tree.g:12:1: prog : ( block )+ ;
    def prog(self, ):

        try:
            try:
                # /home/didi/fyp/code/LexParse/Tree.g:12:5: ( ( block )+ )
                # /home/didi/fyp/code/LexParse/Tree.g:12:9: ( block )+
                pass 
                # /home/didi/fyp/code/LexParse/Tree.g:12:9: ( block )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/didi/fyp/code/LexParse/Tree.g:12:9: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_prog52)
                        self.block()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                #action start
                print 'lol'
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "prog"


    # $ANTLR start "block"
    # /home/didi/fyp/code/LexParse/Tree.g:15:1: block : ^( BLOCK ( . )+ ) ;
    def block(self, ):

        try:
            try:
                # /home/didi/fyp/code/LexParse/Tree.g:16:2: ( ^( BLOCK ( . )+ ) )
                # /home/didi/fyp/code/LexParse/Tree.g:16:5: ^( BLOCK ( . )+ )
                pass 
                self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block68)

                self.match(self.input, DOWN, None)
                # /home/didi/fyp/code/LexParse/Tree.g:16:13: ( . )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((BLOCK <= LA2_0 <= 26)) :
                        alt2 = 1
                    elif (LA2_0 == 3) :
                        alt2 = 2


                    if alt2 == 1:
                        # /home/didi/fyp/code/LexParse/Tree.g:16:13: .
                        pass 
                        self.matchAny(self.input)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1



                self.match(self.input, UP, None)
                #action start
                print 'classdef'
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "block"


    # Delegated rules


 

    FOLLOW_block_in_prog52 = frozenset([1, 4])
    FOLLOW_BLOCK_in_block68 = frozenset([2])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Tree)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
