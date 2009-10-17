# $ANTLR 3.1.2 /home/didi/fyp/code/LexParse/Objloc.g 2009-04-15 15:11:41

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NAME=5
WS=10
NEWLINE=6
LINE_COMMENT=9
T__11=11
INT=7
COMMENT=8
EOF=-1
NEWDEF=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NEWDEF", "NAME", "NEWLINE", "INT", "COMMENT", "LINE_COMMENT", "WS", 
    "'@'"
]




class ObjlocParser(Parser):
    grammarFileName = "/home/didi/fyp/code/LexParse/Objloc.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class file_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "file"
    # /home/didi/fyp/code/LexParse/Objloc.g:13:1: file : ( defin )+ ;
    def file(self, ):

        retval = self.file_return()
        retval.start = self.input.LT(1)

        root_0 = None

        defin1 = None



        try:
            try:
                # /home/didi/fyp/code/LexParse/Objloc.g:14:2: ( ( defin )+ )
                # /home/didi/fyp/code/LexParse/Objloc.g:14:4: ( defin )+
                pass 
                root_0 = self._adaptor.nil()

                # /home/didi/fyp/code/LexParse/Objloc.g:14:4: ( defin )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NAME) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/didi/fyp/code/LexParse/Objloc.g:14:4: defin
                        pass 
                        self._state.following.append(self.FOLLOW_defin_in_file44)
                        defin1 = self.defin()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, defin1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "file"

    class defin_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "defin"
    # /home/didi/fyp/code/LexParse/Objloc.g:17:1: defin : a= NAME '@' b= NAME ( NEWLINE )? -> ^( NEWDEF $a $b) ;
    def defin(self, ):

        retval = self.defin_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        char_literal2 = None
        NEWLINE3 = None

        a_tree = None
        b_tree = None
        char_literal2_tree = None
        NEWLINE3_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_11 = RewriteRuleTokenStream(self._adaptor, "token 11")

        try:
            try:
                # /home/didi/fyp/code/LexParse/Objloc.g:18:2: (a= NAME '@' b= NAME ( NEWLINE )? -> ^( NEWDEF $a $b) )
                # /home/didi/fyp/code/LexParse/Objloc.g:18:4: a= NAME '@' b= NAME ( NEWLINE )?
                pass 
                a=self.match(self.input, NAME, self.FOLLOW_NAME_in_defin60) 
                stream_NAME.add(a)
                char_literal2=self.match(self.input, 11, self.FOLLOW_11_in_defin62) 
                stream_11.add(char_literal2)
                b=self.match(self.input, NAME, self.FOLLOW_NAME_in_defin66) 
                stream_NAME.add(b)
                # /home/didi/fyp/code/LexParse/Objloc.g:18:22: ( NEWLINE )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == NEWLINE) :
                    alt2 = 1
                if alt2 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:18:22: NEWLINE
                    pass 
                    NEWLINE3=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_defin68) 
                    stream_NEWLINE.add(NEWLINE3)




                # AST Rewrite
                # elements: b, a
                # token labels: b, a
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_b = RewriteRuleTokenStream(self._adaptor, "token b", b)
                stream_a = RewriteRuleTokenStream(self._adaptor, "token a", a)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 18:30: -> ^( NEWDEF $a $b)
                # /home/didi/fyp/code/LexParse/Objloc.g:18:33: ^( NEWDEF $a $b)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEWDEF, "NEWDEF"), root_1)

                self._adaptor.addChild(root_1, stream_a.nextNode())
                self._adaptor.addChild(root_1, stream_b.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "defin"


    # Delegated rules


 

    FOLLOW_defin_in_file44 = frozenset([1, 5])
    FOLLOW_NAME_in_defin60 = frozenset([11])
    FOLLOW_11_in_defin62 = frozenset([5])
    FOLLOW_NAME_in_defin66 = frozenset([1, 6])
    FOLLOW_NEWLINE_in_defin68 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ObjlocLexer", ObjlocParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
