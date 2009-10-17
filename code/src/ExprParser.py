# $ANTLR 3.1.2 /home/didi/fyp/code/LexParse/Expr.g 2009-04-30 15:44:22

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
CLASS=10
METHDEF=20
WHILE=13
DEBUGFLAG=21
NEWOBJ=7
EOF=-1
BREAK=14
NAME=23
T__51=51
T__52=52
T__53=53
T__54=54
IFTEST=9
EQ=5
COMMENT=27
RETURNSTM=22
T__50=50
PARAMS=6
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=28
T__48=48
T__49=49
ELSE=16
BOOL=12
INT=26
STRINGTPL=25
T__30=30
T__31=31
T__32=32
WS=29
T__33=33
T__34=34
NEWLINE=24
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
BLOCK=4
PRINTSTM=17
SERVERNAME=19
CALL=8
PTRASS=11
OSTRING=18
DOWHILE=15

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "BLOCK", "EQ", "PARAMS", "NEWOBJ", "CALL", "IFTEST", "CLASS", "PTRASS", 
    "BOOL", "WHILE", "BREAK", "DOWHILE", "ELSE", "PRINTSTM", "OSTRING", 
    "SERVERNAME", "METHDEF", "DEBUGFLAG", "RETURNSTM", "NAME", "NEWLINE", 
    "STRINGTPL", "INT", "COMMENT", "LINE_COMMENT", "WS", "'class'", "'{'", 
    "'}'", "'return'", "'('", "')'", "'def'", "'.'", "'print'", "'while'", 
    "'break'", "'if'", "'else'", "'='", "'new'", "'@'", "'for'", "';'", 
    "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "','"
]




class ExprParser(Parser):
    grammarFileName = "/home/didi/fyp/code/LexParse/Expr.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prog"
    # /home/didi/fyp/code/LexParse/Expr.g:34:1: prog : classdef ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        classdef1 = None



        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:34:6: ( classdef )
                # /home/didi/fyp/code/LexParse/Expr.g:34:8: classdef
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_classdef_in_prog117)
                classdef1 = self.classdef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, classdef1.tree)



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

    # $ANTLR end "prog"

    class classdef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classdef"
    # /home/didi/fyp/code/LexParse/Expr.g:38:1: classdef : 'class' NAME block -> ^( CLASS NAME block ) ;
    def classdef(self, ):

        retval = self.classdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal2 = None
        NAME3 = None
        block4 = None


        string_literal2_tree = None
        NAME3_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_30 = RewriteRuleTokenStream(self._adaptor, "token 30")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:39:2: ( 'class' NAME block -> ^( CLASS NAME block ) )
                # /home/didi/fyp/code/LexParse/Expr.g:39:5: 'class' NAME block
                pass 
                string_literal2=self.match(self.input, 30, self.FOLLOW_30_in_classdef131) 
                stream_30.add(string_literal2)
                NAME3=self.match(self.input, NAME, self.FOLLOW_NAME_in_classdef133) 
                stream_NAME.add(NAME3)
                self._state.following.append(self.FOLLOW_block_in_classdef136)
                block4 = self.block()

                self._state.following.pop()
                stream_block.add(block4.tree)

                # AST Rewrite
                # elements: NAME, block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 39:28: -> ^( CLASS NAME block )
                # /home/didi/fyp/code/LexParse/Expr.g:39:31: ^( CLASS NAME block )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CLASS, "CLASS"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())
                self._adaptor.addChild(root_1, stream_block.nextTree())

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

    # $ANTLR end "classdef"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "block"
    # /home/didi/fyp/code/LexParse/Expr.g:43:1: block : '{' ( stat )* '}' -> ^( BLOCK ( stat )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal5 = None
        char_literal7 = None
        stat6 = None


        char_literal5_tree = None
        char_literal7_tree = None
        stream_32 = RewriteRuleTokenStream(self._adaptor, "token 32")
        stream_31 = RewriteRuleTokenStream(self._adaptor, "token 31")
        stream_stat = RewriteRuleSubtreeStream(self._adaptor, "rule stat")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:44:2: ( '{' ( stat )* '}' -> ^( BLOCK ( stat )* ) )
                # /home/didi/fyp/code/LexParse/Expr.g:44:4: '{' ( stat )* '}'
                pass 
                char_literal5=self.match(self.input, 31, self.FOLLOW_31_in_block163) 
                stream_31.add(char_literal5)
                # /home/didi/fyp/code/LexParse/Expr.g:44:9: ( stat )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((NAME <= LA1_0 <= NEWLINE) or LA1_0 == 31 or LA1_0 == 33 or LA1_0 == 36 or (38 <= LA1_0 <= 41) or LA1_0 == 46) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/didi/fyp/code/LexParse/Expr.g:44:13: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_block170)
                        stat6 = self.stat()

                        self._state.following.pop()
                        stream_stat.add(stat6.tree)


                    else:
                        break #loop1


                char_literal7=self.match(self.input, 32, self.FOLLOW_32_in_block177) 
                stream_32.add(char_literal7)

                # AST Rewrite
                # elements: stat
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 44:27: -> ^( BLOCK ( stat )* )
                # /home/didi/fyp/code/LexParse/Expr.g:44:30: ^( BLOCK ( stat )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                # /home/didi/fyp/code/LexParse/Expr.g:44:38: ( stat )*
                while stream_stat.hasNext():
                    self._adaptor.addChild(root_1, stream_stat.nextTree())


                stream_stat.reset();

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

    # $ANTLR end "block"

    class stat_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "stat"
    # /home/didi/fyp/code/LexParse/Expr.g:48:1: stat : ( iftest | methdef | forloop | newvar | call | block | whileloop | loopbreak | printstm | returnstm | NEWLINE );
    def stat(self, ):

        retval = self.stat_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE18 = None
        iftest8 = None

        methdef9 = None

        forloop10 = None

        newvar11 = None

        call12 = None

        block13 = None

        whileloop14 = None

        loopbreak15 = None

        printstm16 = None

        returnstm17 = None


        NEWLINE18_tree = None

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:49:2: ( iftest | methdef | forloop | newvar | call | block | whileloop | loopbreak | printstm | returnstm | NEWLINE )
                alt2 = 11
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:49:4: iftest
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_iftest_in_stat200)
                    iftest8 = self.iftest()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, iftest8.tree)


                elif alt2 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:50:4: methdef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_methdef_in_stat207)
                    methdef9 = self.methdef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, methdef9.tree)


                elif alt2 == 3:
                    # /home/didi/fyp/code/LexParse/Expr.g:51:4: forloop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_forloop_in_stat212)
                    forloop10 = self.forloop()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, forloop10.tree)


                elif alt2 == 4:
                    # /home/didi/fyp/code/LexParse/Expr.g:52:5: newvar
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_newvar_in_stat218)
                    newvar11 = self.newvar()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, newvar11.tree)


                elif alt2 == 5:
                    # /home/didi/fyp/code/LexParse/Expr.g:53:4: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_stat223)
                    call12 = self.call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, call12.tree)


                elif alt2 == 6:
                    # /home/didi/fyp/code/LexParse/Expr.g:54:5: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_stat229)
                    block13 = self.block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, block13.tree)


                elif alt2 == 7:
                    # /home/didi/fyp/code/LexParse/Expr.g:55:4: whileloop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_whileloop_in_stat234)
                    whileloop14 = self.whileloop()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, whileloop14.tree)


                elif alt2 == 8:
                    # /home/didi/fyp/code/LexParse/Expr.g:56:4: loopbreak
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_loopbreak_in_stat239)
                    loopbreak15 = self.loopbreak()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, loopbreak15.tree)


                elif alt2 == 9:
                    # /home/didi/fyp/code/LexParse/Expr.g:57:4: printstm
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_printstm_in_stat244)
                    printstm16 = self.printstm()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, printstm16.tree)


                elif alt2 == 10:
                    # /home/didi/fyp/code/LexParse/Expr.g:58:4: returnstm
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_returnstm_in_stat249)
                    returnstm17 = self.returnstm()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, returnstm17.tree)


                elif alt2 == 11:
                    # /home/didi/fyp/code/LexParse/Expr.g:59:4: NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()

                    NEWLINE18=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat254)

                    NEWLINE18_tree = self._adaptor.createWithPayload(NEWLINE18)
                    self._adaptor.addChild(root_0, NEWLINE18_tree)



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

    # $ANTLR end "stat"

    class returnstm_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "returnstm"
    # /home/didi/fyp/code/LexParse/Expr.g:64:1: returnstm : 'return' '(' NAME ')' -> ^( RETURNSTM NAME ) ;
    def returnstm(self, ):

        retval = self.returnstm_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal19 = None
        char_literal20 = None
        NAME21 = None
        char_literal22 = None

        string_literal19_tree = None
        char_literal20_tree = None
        NAME21_tree = None
        char_literal22_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_33 = RewriteRuleTokenStream(self._adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:65:2: ( 'return' '(' NAME ')' -> ^( RETURNSTM NAME ) )
                # /home/didi/fyp/code/LexParse/Expr.g:65:5: 'return' '(' NAME ')'
                pass 
                string_literal19=self.match(self.input, 33, self.FOLLOW_33_in_returnstm268) 
                stream_33.add(string_literal19)
                char_literal20=self.match(self.input, 34, self.FOLLOW_34_in_returnstm270) 
                stream_34.add(char_literal20)
                NAME21=self.match(self.input, NAME, self.FOLLOW_NAME_in_returnstm272) 
                stream_NAME.add(NAME21)
                char_literal22=self.match(self.input, 35, self.FOLLOW_35_in_returnstm274) 
                stream_35.add(char_literal22)

                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 65:27: -> ^( RETURNSTM NAME )
                # /home/didi/fyp/code/LexParse/Expr.g:65:30: ^( RETURNSTM NAME )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURNSTM, "RETURNSTM"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())

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

    # $ANTLR end "returnstm"

    class methdef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "methdef"
    # /home/didi/fyp/code/LexParse/Expr.g:70:1: methdef : 'def' NAME block -> ^( METHDEF NAME block ) ;
    def methdef(self, ):

        retval = self.methdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal23 = None
        NAME24 = None
        block25 = None


        string_literal23_tree = None
        NAME24_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:71:2: ( 'def' NAME block -> ^( METHDEF NAME block ) )
                # /home/didi/fyp/code/LexParse/Expr.g:71:4: 'def' NAME block
                pass 
                string_literal23=self.match(self.input, 36, self.FOLLOW_36_in_methdef296) 
                stream_36.add(string_literal23)
                NAME24=self.match(self.input, NAME, self.FOLLOW_NAME_in_methdef298) 
                stream_NAME.add(NAME24)
                self._state.following.append(self.FOLLOW_block_in_methdef300)
                block25 = self.block()

                self._state.following.pop()
                stream_block.add(block25.tree)

                # AST Rewrite
                # elements: block, NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 71:21: -> ^( METHDEF NAME block )
                # /home/didi/fyp/code/LexParse/Expr.g:71:24: ^( METHDEF NAME block )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHDEF, "METHDEF"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())
                self._adaptor.addChild(root_1, stream_block.nextTree())

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

    # $ANTLR end "methdef"

    class call_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "call"
    # /home/didi/fyp/code/LexParse/Expr.g:76:1: call : a= NAME '.' b= NAME paramlist -> ^( CALL $a $b paramlist ) ;
    def call(self, ):

        retval = self.call_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        char_literal26 = None
        paramlist27 = None


        a_tree = None
        b_tree = None
        char_literal26_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_37 = RewriteRuleTokenStream(self._adaptor, "token 37")
        stream_paramlist = RewriteRuleSubtreeStream(self._adaptor, "rule paramlist")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:77:2: (a= NAME '.' b= NAME paramlist -> ^( CALL $a $b paramlist ) )
                # /home/didi/fyp/code/LexParse/Expr.g:77:4: a= NAME '.' b= NAME paramlist
                pass 
                a=self.match(self.input, NAME, self.FOLLOW_NAME_in_call326) 
                stream_NAME.add(a)
                char_literal26=self.match(self.input, 37, self.FOLLOW_37_in_call328) 
                stream_37.add(char_literal26)
                b=self.match(self.input, NAME, self.FOLLOW_NAME_in_call332) 
                stream_NAME.add(b)
                self._state.following.append(self.FOLLOW_paramlist_in_call334)
                paramlist27 = self.paramlist()

                self._state.following.pop()
                stream_paramlist.add(paramlist27.tree)

                # AST Rewrite
                # elements: a, b, paramlist
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
                # 77:32: -> ^( CALL $a $b paramlist )
                # /home/didi/fyp/code/LexParse/Expr.g:77:35: ^( CALL $a $b paramlist )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                self._adaptor.addChild(root_1, stream_a.nextNode())
                self._adaptor.addChild(root_1, stream_b.nextNode())
                self._adaptor.addChild(root_1, stream_paramlist.nextTree())

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

    # $ANTLR end "call"

    class printstm_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "printstm"
    # /home/didi/fyp/code/LexParse/Expr.g:82:1: printstm : 'print' '(' printparams ')' -> ^( PRINTSTM printparams ) ;
    def printstm(self, ):

        retval = self.printstm_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal28 = None
        char_literal29 = None
        char_literal31 = None
        printparams30 = None


        string_literal28_tree = None
        char_literal29_tree = None
        char_literal31_tree = None
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_printparams = RewriteRuleSubtreeStream(self._adaptor, "rule printparams")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:83:2: ( 'print' '(' printparams ')' -> ^( PRINTSTM printparams ) )
                # /home/didi/fyp/code/LexParse/Expr.g:83:4: 'print' '(' printparams ')'
                pass 
                string_literal28=self.match(self.input, 38, self.FOLLOW_38_in_printstm361) 
                stream_38.add(string_literal28)
                char_literal29=self.match(self.input, 34, self.FOLLOW_34_in_printstm363) 
                stream_34.add(char_literal29)
                self._state.following.append(self.FOLLOW_printparams_in_printstm365)
                printparams30 = self.printparams()

                self._state.following.pop()
                stream_printparams.add(printparams30.tree)
                char_literal31=self.match(self.input, 35, self.FOLLOW_35_in_printstm367) 
                stream_35.add(char_literal31)

                # AST Rewrite
                # elements: printparams
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 83:32: -> ^( PRINTSTM printparams )
                # /home/didi/fyp/code/LexParse/Expr.g:83:35: ^( PRINTSTM printparams )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PRINTSTM, "PRINTSTM"), root_1)

                self._adaptor.addChild(root_1, stream_printparams.nextTree())

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

    # $ANTLR end "printstm"

    class printparams_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "printparams"
    # /home/didi/fyp/code/LexParse/Expr.g:87:1: printparams : ( call | NAME | STRINGTPL -> ^( OSTRING STRINGTPL ) );
    def printparams(self, ):

        retval = self.printparams_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME33 = None
        STRINGTPL34 = None
        call32 = None


        NAME33_tree = None
        STRINGTPL34_tree = None
        stream_STRINGTPL = RewriteRuleTokenStream(self._adaptor, "token STRINGTPL")

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:88:2: ( call | NAME | STRINGTPL -> ^( OSTRING STRINGTPL ) )
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == NAME) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 37) :
                        alt3 = 1
                    elif (LA3_1 == 35) :
                        alt3 = 2
                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae

                elif (LA3_0 == STRINGTPL) :
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:88:4: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_printparams387)
                    call32 = self.call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, call32.tree)


                elif alt3 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:89:4: NAME
                    pass 
                    root_0 = self._adaptor.nil()

                    NAME33=self.match(self.input, NAME, self.FOLLOW_NAME_in_printparams392)

                    NAME33_tree = self._adaptor.createWithPayload(NAME33)
                    self._adaptor.addChild(root_0, NAME33_tree)



                elif alt3 == 3:
                    # /home/didi/fyp/code/LexParse/Expr.g:90:4: STRINGTPL
                    pass 
                    STRINGTPL34=self.match(self.input, STRINGTPL, self.FOLLOW_STRINGTPL_in_printparams397) 
                    stream_STRINGTPL.add(STRINGTPL34)

                    # AST Rewrite
                    # elements: STRINGTPL
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 90:14: -> ^( OSTRING STRINGTPL )
                    # /home/didi/fyp/code/LexParse/Expr.g:90:17: ^( OSTRING STRINGTPL )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OSTRING, "OSTRING"), root_1)

                    self._adaptor.addChild(root_1, stream_STRINGTPL.nextNode())

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

    # $ANTLR end "printparams"

    class whileloop_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "whileloop"
    # /home/didi/fyp/code/LexParse/Expr.g:95:1: whileloop : 'while' '(' boolexp ')' a= block -> ^( WHILE boolexp $a) ;
    def whileloop(self, ):

        retval = self.whileloop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal35 = None
        char_literal36 = None
        char_literal38 = None
        a = None

        boolexp37 = None


        string_literal35_tree = None
        char_literal36_tree = None
        char_literal38_tree = None
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_boolexp = RewriteRuleSubtreeStream(self._adaptor, "rule boolexp")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:96:2: ( 'while' '(' boolexp ')' a= block -> ^( WHILE boolexp $a) )
                # /home/didi/fyp/code/LexParse/Expr.g:96:4: 'while' '(' boolexp ')' a= block
                pass 
                string_literal35=self.match(self.input, 39, self.FOLLOW_39_in_whileloop418) 
                stream_39.add(string_literal35)
                char_literal36=self.match(self.input, 34, self.FOLLOW_34_in_whileloop420) 
                stream_34.add(char_literal36)
                self._state.following.append(self.FOLLOW_boolexp_in_whileloop422)
                boolexp37 = self.boolexp()

                self._state.following.pop()
                stream_boolexp.add(boolexp37.tree)
                char_literal38=self.match(self.input, 35, self.FOLLOW_35_in_whileloop424) 
                stream_35.add(char_literal38)
                self._state.following.append(self.FOLLOW_block_in_whileloop428)
                a = self.block()

                self._state.following.pop()
                stream_block.add(a.tree)

                # AST Rewrite
                # elements: a, boolexp
                # token labels: 
                # rule labels: retval, a
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if a is not None:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                else:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                root_0 = self._adaptor.nil()
                # 96:36: -> ^( WHILE boolexp $a)
                # /home/didi/fyp/code/LexParse/Expr.g:96:39: ^( WHILE boolexp $a)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(WHILE, "WHILE"), root_1)

                self._adaptor.addChild(root_1, stream_boolexp.nextTree())
                self._adaptor.addChild(root_1, stream_a.nextTree())

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

    # $ANTLR end "whileloop"

    class loopbreak_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "loopbreak"
    # /home/didi/fyp/code/LexParse/Expr.g:100:1: loopbreak : 'break' -> ^( BREAK ) ;
    def loopbreak(self, ):

        retval = self.loopbreak_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal39 = None

        string_literal39_tree = None
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:101:2: ( 'break' -> ^( BREAK ) )
                # /home/didi/fyp/code/LexParse/Expr.g:101:4: 'break'
                pass 
                string_literal39=self.match(self.input, 40, self.FOLLOW_40_in_loopbreak452) 
                stream_40.add(string_literal39)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 101:12: -> ^( BREAK )
                # /home/didi/fyp/code/LexParse/Expr.g:101:15: ^( BREAK )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BREAK, "BREAK"), root_1)

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

    # $ANTLR end "loopbreak"

    class iftest_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "iftest"
    # /home/didi/fyp/code/LexParse/Expr.g:109:1: iftest : 'if' '(' boolexp ')' a= block ( 'else' b= block )? -> ^( IFTEST boolexp $a ( ELSE $b)? ) ;
    def iftest(self, ):

        retval = self.iftest_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal40 = None
        char_literal41 = None
        char_literal43 = None
        string_literal44 = None
        a = None

        b = None

        boolexp42 = None


        string_literal40_tree = None
        char_literal41_tree = None
        char_literal43_tree = None
        string_literal44_tree = None
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_boolexp = RewriteRuleSubtreeStream(self._adaptor, "rule boolexp")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:109:9: ( 'if' '(' boolexp ')' a= block ( 'else' b= block )? -> ^( IFTEST boolexp $a ( ELSE $b)? ) )
                # /home/didi/fyp/code/LexParse/Expr.g:109:11: 'if' '(' boolexp ')' a= block ( 'else' b= block )?
                pass 
                string_literal40=self.match(self.input, 41, self.FOLLOW_41_in_iftest474) 
                stream_41.add(string_literal40)
                char_literal41=self.match(self.input, 34, self.FOLLOW_34_in_iftest476) 
                stream_34.add(char_literal41)
                self._state.following.append(self.FOLLOW_boolexp_in_iftest478)
                boolexp42 = self.boolexp()

                self._state.following.pop()
                stream_boolexp.add(boolexp42.tree)
                char_literal43=self.match(self.input, 35, self.FOLLOW_35_in_iftest480) 
                stream_35.add(char_literal43)
                self._state.following.append(self.FOLLOW_block_in_iftest484)
                a = self.block()

                self._state.following.pop()
                stream_block.add(a.tree)
                # /home/didi/fyp/code/LexParse/Expr.g:109:40: ( 'else' b= block )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 42) :
                    alt4 = 1
                if alt4 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:109:41: 'else' b= block
                    pass 
                    string_literal44=self.match(self.input, 42, self.FOLLOW_42_in_iftest487) 
                    stream_42.add(string_literal44)
                    self._state.following.append(self.FOLLOW_block_in_iftest491)
                    b = self.block()

                    self._state.following.pop()
                    stream_block.add(b.tree)




                # AST Rewrite
                # elements: a, boolexp, b
                # token labels: 
                # rule labels: retval, b, a
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if b is not None:
                    stream_b = RewriteRuleSubtreeStream(self._adaptor, "rule b", b.tree)
                else:
                    stream_b = RewriteRuleSubtreeStream(self._adaptor, "token b", None)


                if a is not None:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                else:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                root_0 = self._adaptor.nil()
                # 109:58: -> ^( IFTEST boolexp $a ( ELSE $b)? )
                # /home/didi/fyp/code/LexParse/Expr.g:110:5: ^( IFTEST boolexp $a ( ELSE $b)? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IFTEST, "IFTEST"), root_1)

                self._adaptor.addChild(root_1, stream_boolexp.nextTree())
                self._adaptor.addChild(root_1, stream_a.nextTree())
                # /home/didi/fyp/code/LexParse/Expr.g:110:25: ( ELSE $b)?
                if stream_b.hasNext():
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(ELSE, "ELSE"))
                    self._adaptor.addChild(root_1, stream_b.nextTree())


                stream_b.reset();

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

    # $ANTLR end "iftest"

    class newvar_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "newvar"
    # /home/didi/fyp/code/LexParse/Expr.g:115:1: newvar : (a= NAME '=' 'new' b= NAME paramlist ( '@' servername )? -> ^( EQ $a NEWOBJ ( servername )? $b paramlist ) | a= NAME '=' b= NAME -> ^( EQ $a PTRASS $b) | NAME '=' call -> ^( EQ NAME call ) );
    def newvar(self, ):

        retval = self.newvar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        char_literal45 = None
        string_literal46 = None
        char_literal48 = None
        char_literal50 = None
        NAME51 = None
        char_literal52 = None
        paramlist47 = None

        servername49 = None

        call53 = None


        a_tree = None
        b_tree = None
        char_literal45_tree = None
        string_literal46_tree = None
        char_literal48_tree = None
        char_literal50_tree = None
        NAME51_tree = None
        char_literal52_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_45 = RewriteRuleTokenStream(self._adaptor, "token 45")
        stream_43 = RewriteRuleTokenStream(self._adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_call = RewriteRuleSubtreeStream(self._adaptor, "rule call")
        stream_paramlist = RewriteRuleSubtreeStream(self._adaptor, "rule paramlist")
        stream_servername = RewriteRuleSubtreeStream(self._adaptor, "rule servername")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:116:2: (a= NAME '=' 'new' b= NAME paramlist ( '@' servername )? -> ^( EQ $a NEWOBJ ( servername )? $b paramlist ) | a= NAME '=' b= NAME -> ^( EQ $a PTRASS $b) | NAME '=' call -> ^( EQ NAME call ) )
                alt6 = 3
                LA6_0 = self.input.LA(1)

                if (LA6_0 == NAME) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 43) :
                        LA6_2 = self.input.LA(3)

                        if (LA6_2 == 44) :
                            alt6 = 1
                        elif (LA6_2 == NAME) :
                            LA6_4 = self.input.LA(4)

                            if (LA6_4 == 37) :
                                alt6 = 3
                            elif ((NAME <= LA6_4 <= NEWLINE) or (31 <= LA6_4 <= 33) or (35 <= LA6_4 <= 36) or (38 <= LA6_4 <= 41) or (46 <= LA6_4 <= 47)) :
                                alt6 = 2
                            else:
                                nvae = NoViableAltException("", 6, 4, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 6, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:116:4: a= NAME '=' 'new' b= NAME paramlist ( '@' servername )?
                    pass 
                    a=self.match(self.input, NAME, self.FOLLOW_NAME_in_newvar533) 
                    stream_NAME.add(a)
                    char_literal45=self.match(self.input, 43, self.FOLLOW_43_in_newvar535) 
                    stream_43.add(char_literal45)
                    string_literal46=self.match(self.input, 44, self.FOLLOW_44_in_newvar537) 
                    stream_44.add(string_literal46)
                    b=self.match(self.input, NAME, self.FOLLOW_NAME_in_newvar541) 
                    stream_NAME.add(b)
                    self._state.following.append(self.FOLLOW_paramlist_in_newvar543)
                    paramlist47 = self.paramlist()

                    self._state.following.pop()
                    stream_paramlist.add(paramlist47.tree)
                    # /home/didi/fyp/code/LexParse/Expr.g:116:38: ( '@' servername )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 45) :
                        alt5 = 1
                    if alt5 == 1:
                        # /home/didi/fyp/code/LexParse/Expr.g:116:39: '@' servername
                        pass 
                        char_literal48=self.match(self.input, 45, self.FOLLOW_45_in_newvar546) 
                        stream_45.add(char_literal48)
                        self._state.following.append(self.FOLLOW_servername_in_newvar548)
                        servername49 = self.servername()

                        self._state.following.pop()
                        stream_servername.add(servername49.tree)




                    # AST Rewrite
                    # elements: paramlist, b, servername, a
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
                    # 116:56: -> ^( EQ $a NEWOBJ ( servername )? $b paramlist )
                    # /home/didi/fyp/code/LexParse/Expr.g:117:5: ^( EQ $a NEWOBJ ( servername )? $b paramlist )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EQ, "EQ"), root_1)

                    self._adaptor.addChild(root_1, stream_a.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(NEWOBJ, "NEWOBJ"))
                    # /home/didi/fyp/code/LexParse/Expr.g:117:21: ( servername )?
                    if stream_servername.hasNext():
                        self._adaptor.addChild(root_1, stream_servername.nextTree())


                    stream_servername.reset();
                    self._adaptor.addChild(root_1, stream_b.nextNode())
                    self._adaptor.addChild(root_1, stream_paramlist.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt6 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:118:4: a= NAME '=' b= NAME
                    pass 
                    a=self.match(self.input, NAME, self.FOLLOW_NAME_in_newvar584) 
                    stream_NAME.add(a)
                    char_literal50=self.match(self.input, 43, self.FOLLOW_43_in_newvar586) 
                    stream_43.add(char_literal50)
                    b=self.match(self.input, NAME, self.FOLLOW_NAME_in_newvar590) 
                    stream_NAME.add(b)

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
                    # 118:22: -> ^( EQ $a PTRASS $b)
                    # /home/didi/fyp/code/LexParse/Expr.g:118:25: ^( EQ $a PTRASS $b)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EQ, "EQ"), root_1)

                    self._adaptor.addChild(root_1, stream_a.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(PTRASS, "PTRASS"))
                    self._adaptor.addChild(root_1, stream_b.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt6 == 3:
                    # /home/didi/fyp/code/LexParse/Expr.g:119:4: NAME '=' call
                    pass 
                    NAME51=self.match(self.input, NAME, self.FOLLOW_NAME_in_newvar611) 
                    stream_NAME.add(NAME51)
                    char_literal52=self.match(self.input, 43, self.FOLLOW_43_in_newvar613) 
                    stream_43.add(char_literal52)
                    self._state.following.append(self.FOLLOW_call_in_newvar615)
                    call53 = self.call()

                    self._state.following.pop()
                    stream_call.add(call53.tree)

                    # AST Rewrite
                    # elements: call, NAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 119:18: -> ^( EQ NAME call )
                    # /home/didi/fyp/code/LexParse/Expr.g:119:21: ^( EQ NAME call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EQ, "EQ"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())
                    self._adaptor.addChild(root_1, stream_call.nextTree())

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

    # $ANTLR end "newvar"

    class forloop_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "forloop"
    # /home/didi/fyp/code/LexParse/Expr.g:124:1: forloop : 'for' '(' a= newvar ';' boolexp ';' b= newvar ')' block -> ^( BLOCK $a ^( WHILE boolexp ^( BLOCK block $b) ) ) ;
    def forloop(self, ):

        retval = self.forloop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal54 = None
        char_literal55 = None
        char_literal56 = None
        char_literal58 = None
        char_literal59 = None
        a = None

        b = None

        boolexp57 = None

        block60 = None


        string_literal54_tree = None
        char_literal55_tree = None
        char_literal56_tree = None
        char_literal58_tree = None
        char_literal59_tree = None
        stream_47 = RewriteRuleTokenStream(self._adaptor, "token 47")
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_newvar = RewriteRuleSubtreeStream(self._adaptor, "rule newvar")
        stream_boolexp = RewriteRuleSubtreeStream(self._adaptor, "rule boolexp")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:125:2: ( 'for' '(' a= newvar ';' boolexp ';' b= newvar ')' block -> ^( BLOCK $a ^( WHILE boolexp ^( BLOCK block $b) ) ) )
                # /home/didi/fyp/code/LexParse/Expr.g:125:4: 'for' '(' a= newvar ';' boolexp ';' b= newvar ')' block
                pass 
                string_literal54=self.match(self.input, 46, self.FOLLOW_46_in_forloop641) 
                stream_46.add(string_literal54)
                char_literal55=self.match(self.input, 34, self.FOLLOW_34_in_forloop643) 
                stream_34.add(char_literal55)
                self._state.following.append(self.FOLLOW_newvar_in_forloop648)
                a = self.newvar()

                self._state.following.pop()
                stream_newvar.add(a.tree)
                char_literal56=self.match(self.input, 47, self.FOLLOW_47_in_forloop650) 
                stream_47.add(char_literal56)
                self._state.following.append(self.FOLLOW_boolexp_in_forloop652)
                boolexp57 = self.boolexp()

                self._state.following.pop()
                stream_boolexp.add(boolexp57.tree)
                char_literal58=self.match(self.input, 47, self.FOLLOW_47_in_forloop654) 
                stream_47.add(char_literal58)
                self._state.following.append(self.FOLLOW_newvar_in_forloop659)
                b = self.newvar()

                self._state.following.pop()
                stream_newvar.add(b.tree)
                char_literal59=self.match(self.input, 35, self.FOLLOW_35_in_forloop661) 
                stream_35.add(char_literal59)
                self._state.following.append(self.FOLLOW_block_in_forloop663)
                block60 = self.block()

                self._state.following.pop()
                stream_block.add(block60.tree)

                # AST Rewrite
                # elements: boolexp, block, b, a
                # token labels: 
                # rule labels: retval, b, a
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if b is not None:
                    stream_b = RewriteRuleSubtreeStream(self._adaptor, "rule b", b.tree)
                else:
                    stream_b = RewriteRuleSubtreeStream(self._adaptor, "token b", None)


                if a is not None:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                else:
                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                root_0 = self._adaptor.nil()
                # 125:60: -> ^( BLOCK $a ^( WHILE boolexp ^( BLOCK block $b) ) )
                # /home/didi/fyp/code/LexParse/Expr.g:126:5: ^( BLOCK $a ^( WHILE boolexp ^( BLOCK block $b) ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                self._adaptor.addChild(root_1, stream_a.nextTree())
                # /home/didi/fyp/code/LexParse/Expr.g:126:16: ^( WHILE boolexp ^( BLOCK block $b) )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(WHILE, "WHILE"), root_2)

                self._adaptor.addChild(root_2, stream_boolexp.nextTree())
                # /home/didi/fyp/code/LexParse/Expr.g:126:33: ^( BLOCK block $b)
                root_3 = self._adaptor.nil()
                root_3 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_3)

                self._adaptor.addChild(root_3, stream_block.nextTree())
                self._adaptor.addChild(root_3, stream_b.nextTree())

                self._adaptor.addChild(root_2, root_3)

                self._adaptor.addChild(root_1, root_2)

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

    # $ANTLR end "forloop"

    class boolexp_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "boolexp"
    # /home/didi/fyp/code/LexParse/Expr.g:130:1: boolexp : ( | a= booltype cmp_operator b= booltype -> ^( BOOL cmp_operator $a $b) );
    def boolexp(self, ):

        retval = self.boolexp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None

        b = None

        cmp_operator61 = None


        stream_booltype = RewriteRuleSubtreeStream(self._adaptor, "rule booltype")
        stream_cmp_operator = RewriteRuleSubtreeStream(self._adaptor, "rule cmp_operator")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:131:2: ( | a= booltype cmp_operator b= booltype -> ^( BOOL cmp_operator $a $b) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 35 or LA7_0 == 47) :
                    alt7 = 1
                elif (LA7_0 == NAME) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:132:2: 
                    pass 
                    root_0 = self._adaptor.nil()


                elif alt7 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:132:4: a= booltype cmp_operator b= booltype
                    pass 
                    self._state.following.append(self.FOLLOW_booltype_in_boolexp710)
                    a = self.booltype()

                    self._state.following.pop()
                    stream_booltype.add(a.tree)
                    self._state.following.append(self.FOLLOW_cmp_operator_in_boolexp712)
                    cmp_operator61 = self.cmp_operator()

                    self._state.following.pop()
                    stream_cmp_operator.add(cmp_operator61.tree)
                    self._state.following.append(self.FOLLOW_booltype_in_boolexp716)
                    b = self.booltype()

                    self._state.following.pop()
                    stream_booltype.add(b.tree)

                    # AST Rewrite
                    # elements: a, cmp_operator, b
                    # token labels: 
                    # rule labels: retval, b, a
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if b is not None:
                        stream_b = RewriteRuleSubtreeStream(self._adaptor, "rule b", b.tree)
                    else:
                        stream_b = RewriteRuleSubtreeStream(self._adaptor, "token b", None)


                    if a is not None:
                        stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                    else:
                        stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                    root_0 = self._adaptor.nil()
                    # 132:39: -> ^( BOOL cmp_operator $a $b)
                    # /home/didi/fyp/code/LexParse/Expr.g:133:5: ^( BOOL cmp_operator $a $b)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BOOL, "BOOL"), root_1)

                    self._adaptor.addChild(root_1, stream_cmp_operator.nextTree())
                    self._adaptor.addChild(root_1, stream_a.nextTree())
                    self._adaptor.addChild(root_1, stream_b.nextTree())

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

    # $ANTLR end "boolexp"

    class cmp_operator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "cmp_operator"
    # /home/didi/fyp/code/LexParse/Expr.g:137:1: cmp_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def cmp_operator(self, ):

        retval = self.cmp_operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set62 = None

        set62_tree = None

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:138:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # /home/didi/fyp/code/LexParse/Expr.g:
                pass 
                root_0 = self._adaptor.nil()

                set62 = self.input.LT(1)
                if (48 <= self.input.LA(1) <= 53):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set62))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





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

    # $ANTLR end "cmp_operator"

    class booltype_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "booltype"
    # /home/didi/fyp/code/LexParse/Expr.g:147:1: booltype : ( call | NAME );
    def booltype(self, ):

        retval = self.booltype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME64 = None
        call63 = None


        NAME64_tree = None

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:148:2: ( call | NAME )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == NAME) :
                    LA8_1 = self.input.LA(2)

                    if (LA8_1 == 37) :
                        alt8 = 1
                    elif (LA8_1 == 35 or (47 <= LA8_1 <= 53)) :
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:148:4: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_booltype783)
                    call63 = self.call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, call63.tree)


                elif alt8 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:149:4: NAME
                    pass 
                    root_0 = self._adaptor.nil()

                    NAME64=self.match(self.input, NAME, self.FOLLOW_NAME_in_booltype788)

                    NAME64_tree = self._adaptor.createWithPayload(NAME64)
                    self._adaptor.addChild(root_0, NAME64_tree)



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

    # $ANTLR end "booltype"

    class paramlist_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "paramlist"
    # /home/didi/fyp/code/LexParse/Expr.g:153:1: paramlist : '(' ( atom ( ',' atom )* )? ')' -> ^( PARAMS ( atom )* ) ;
    def paramlist(self, ):

        retval = self.paramlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal65 = None
        char_literal67 = None
        char_literal69 = None
        atom66 = None

        atom68 = None


        char_literal65_tree = None
        char_literal67_tree = None
        char_literal69_tree = None
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:154:2: ( '(' ( atom ( ',' atom )* )? ')' -> ^( PARAMS ( atom )* ) )
                # /home/didi/fyp/code/LexParse/Expr.g:154:4: '(' ( atom ( ',' atom )* )? ')'
                pass 
                char_literal65=self.match(self.input, 34, self.FOLLOW_34_in_paramlist801) 
                stream_34.add(char_literal65)
                # /home/didi/fyp/code/LexParse/Expr.g:154:8: ( atom ( ',' atom )* )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == NAME or (STRINGTPL <= LA10_0 <= INT)) :
                    alt10 = 1
                if alt10 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:154:10: atom ( ',' atom )*
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_paramlist805)
                    atom66 = self.atom()

                    self._state.following.pop()
                    stream_atom.add(atom66.tree)
                    # /home/didi/fyp/code/LexParse/Expr.g:154:16: ( ',' atom )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == 54) :
                            alt9 = 1


                        if alt9 == 1:
                            # /home/didi/fyp/code/LexParse/Expr.g:154:17: ',' atom
                            pass 
                            char_literal67=self.match(self.input, 54, self.FOLLOW_54_in_paramlist809) 
                            stream_54.add(char_literal67)
                            self._state.following.append(self.FOLLOW_atom_in_paramlist811)
                            atom68 = self.atom()

                            self._state.following.pop()
                            stream_atom.add(atom68.tree)


                        else:
                            break #loop9





                char_literal69=self.match(self.input, 35, self.FOLLOW_35_in_paramlist819) 
                stream_35.add(char_literal69)

                # AST Rewrite
                # elements: atom
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 154:36: -> ^( PARAMS ( atom )* )
                # /home/didi/fyp/code/LexParse/Expr.g:154:39: ^( PARAMS ( atom )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMS, "PARAMS"), root_1)

                # /home/didi/fyp/code/LexParse/Expr.g:154:48: ( atom )*
                while stream_atom.hasNext():
                    self._adaptor.addChild(root_1, stream_atom.nextTree())


                stream_atom.reset();

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

    # $ANTLR end "paramlist"

    class servername_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "servername"
    # /home/didi/fyp/code/LexParse/Expr.g:159:1: servername : a= NAME '.' b= NAME -> ^( SERVERNAME $a '.' $b) ;
    def servername(self, ):

        retval = self.servername_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        char_literal70 = None

        a_tree = None
        b_tree = None
        char_literal70_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_37 = RewriteRuleTokenStream(self._adaptor, "token 37")

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:160:2: (a= NAME '.' b= NAME -> ^( SERVERNAME $a '.' $b) )
                # /home/didi/fyp/code/LexParse/Expr.g:160:4: a= NAME '.' b= NAME
                pass 
                a=self.match(self.input, NAME, self.FOLLOW_NAME_in_servername845) 
                stream_NAME.add(a)
                char_literal70=self.match(self.input, 37, self.FOLLOW_37_in_servername847) 
                stream_37.add(char_literal70)
                b=self.match(self.input, NAME, self.FOLLOW_NAME_in_servername851) 
                stream_NAME.add(b)

                # AST Rewrite
                # elements: b, 37, a
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
                # 160:22: -> ^( SERVERNAME $a '.' $b)
                # /home/didi/fyp/code/LexParse/Expr.g:160:25: ^( SERVERNAME $a '.' $b)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SERVERNAME, "SERVERNAME"), root_1)

                self._adaptor.addChild(root_1, stream_a.nextNode())
                self._adaptor.addChild(root_1, stream_37.nextNode())
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

    # $ANTLR end "servername"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "atom"
    # /home/didi/fyp/code/LexParse/Expr.g:164:1: atom : ( INT | NAME | STRINGTPL );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set71 = None

        set71_tree = None

        try:
            try:
                # /home/didi/fyp/code/LexParse/Expr.g:165:2: ( INT | NAME | STRINGTPL )
                # /home/didi/fyp/code/LexParse/Expr.g:
                pass 
                root_0 = self._adaptor.nil()

                set71 = self.input.LT(1)
                if self.input.LA(1) == NAME or (STRINGTPL <= self.input.LA(1) <= INT):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set71))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





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

    # $ANTLR end "atom"


    # Delegated rules


    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\27\3\uffff\1\45\10\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\56\3\uffff\1\53\10\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\6\1\7\1\10\1\11\1\12\1\13\1\4\1"
        u"\5"
        )

    DFA2_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\4\1\12\6\uffff\1\5\1\uffff\1\11\2\uffff\1\2\1\uffff"
        u"\1\10\1\6\1\7\1\1\4\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14\5\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    DFA2 = DFA
 

    FOLLOW_classdef_in_prog117 = frozenset([1])
    FOLLOW_30_in_classdef131 = frozenset([23])
    FOLLOW_NAME_in_classdef133 = frozenset([31])
    FOLLOW_block_in_classdef136 = frozenset([1])
    FOLLOW_31_in_block163 = frozenset([23, 24, 31, 32, 33, 36, 38, 39, 40, 41, 46])
    FOLLOW_stat_in_block170 = frozenset([23, 24, 31, 32, 33, 36, 38, 39, 40, 41, 46])
    FOLLOW_32_in_block177 = frozenset([1])
    FOLLOW_iftest_in_stat200 = frozenset([1])
    FOLLOW_methdef_in_stat207 = frozenset([1])
    FOLLOW_forloop_in_stat212 = frozenset([1])
    FOLLOW_newvar_in_stat218 = frozenset([1])
    FOLLOW_call_in_stat223 = frozenset([1])
    FOLLOW_block_in_stat229 = frozenset([1])
    FOLLOW_whileloop_in_stat234 = frozenset([1])
    FOLLOW_loopbreak_in_stat239 = frozenset([1])
    FOLLOW_printstm_in_stat244 = frozenset([1])
    FOLLOW_returnstm_in_stat249 = frozenset([1])
    FOLLOW_NEWLINE_in_stat254 = frozenset([1])
    FOLLOW_33_in_returnstm268 = frozenset([34])
    FOLLOW_34_in_returnstm270 = frozenset([23])
    FOLLOW_NAME_in_returnstm272 = frozenset([35])
    FOLLOW_35_in_returnstm274 = frozenset([1])
    FOLLOW_36_in_methdef296 = frozenset([23])
    FOLLOW_NAME_in_methdef298 = frozenset([31])
    FOLLOW_block_in_methdef300 = frozenset([1])
    FOLLOW_NAME_in_call326 = frozenset([37])
    FOLLOW_37_in_call328 = frozenset([23])
    FOLLOW_NAME_in_call332 = frozenset([34])
    FOLLOW_paramlist_in_call334 = frozenset([1])
    FOLLOW_38_in_printstm361 = frozenset([34])
    FOLLOW_34_in_printstm363 = frozenset([23, 25])
    FOLLOW_printparams_in_printstm365 = frozenset([35])
    FOLLOW_35_in_printstm367 = frozenset([1])
    FOLLOW_call_in_printparams387 = frozenset([1])
    FOLLOW_NAME_in_printparams392 = frozenset([1])
    FOLLOW_STRINGTPL_in_printparams397 = frozenset([1])
    FOLLOW_39_in_whileloop418 = frozenset([34])
    FOLLOW_34_in_whileloop420 = frozenset([23, 35])
    FOLLOW_boolexp_in_whileloop422 = frozenset([35])
    FOLLOW_35_in_whileloop424 = frozenset([31])
    FOLLOW_block_in_whileloop428 = frozenset([1])
    FOLLOW_40_in_loopbreak452 = frozenset([1])
    FOLLOW_41_in_iftest474 = frozenset([34])
    FOLLOW_34_in_iftest476 = frozenset([23, 35])
    FOLLOW_boolexp_in_iftest478 = frozenset([35])
    FOLLOW_35_in_iftest480 = frozenset([31])
    FOLLOW_block_in_iftest484 = frozenset([1, 42])
    FOLLOW_42_in_iftest487 = frozenset([31])
    FOLLOW_block_in_iftest491 = frozenset([1])
    FOLLOW_NAME_in_newvar533 = frozenset([43])
    FOLLOW_43_in_newvar535 = frozenset([44])
    FOLLOW_44_in_newvar537 = frozenset([23])
    FOLLOW_NAME_in_newvar541 = frozenset([34])
    FOLLOW_paramlist_in_newvar543 = frozenset([1, 45])
    FOLLOW_45_in_newvar546 = frozenset([23])
    FOLLOW_servername_in_newvar548 = frozenset([1])
    FOLLOW_NAME_in_newvar584 = frozenset([43])
    FOLLOW_43_in_newvar586 = frozenset([23])
    FOLLOW_NAME_in_newvar590 = frozenset([1])
    FOLLOW_NAME_in_newvar611 = frozenset([43])
    FOLLOW_43_in_newvar613 = frozenset([23])
    FOLLOW_call_in_newvar615 = frozenset([1])
    FOLLOW_46_in_forloop641 = frozenset([34])
    FOLLOW_34_in_forloop643 = frozenset([23])
    FOLLOW_newvar_in_forloop648 = frozenset([47])
    FOLLOW_47_in_forloop650 = frozenset([23, 47])
    FOLLOW_boolexp_in_forloop652 = frozenset([47])
    FOLLOW_47_in_forloop654 = frozenset([23])
    FOLLOW_newvar_in_forloop659 = frozenset([35])
    FOLLOW_35_in_forloop661 = frozenset([31])
    FOLLOW_block_in_forloop663 = frozenset([1])
    FOLLOW_booltype_in_boolexp710 = frozenset([48, 49, 50, 51, 52, 53])
    FOLLOW_cmp_operator_in_boolexp712 = frozenset([23])
    FOLLOW_booltype_in_boolexp716 = frozenset([1])
    FOLLOW_set_in_cmp_operator0 = frozenset([1])
    FOLLOW_call_in_booltype783 = frozenset([1])
    FOLLOW_NAME_in_booltype788 = frozenset([1])
    FOLLOW_34_in_paramlist801 = frozenset([23, 25, 26, 35])
    FOLLOW_atom_in_paramlist805 = frozenset([35, 54])
    FOLLOW_54_in_paramlist809 = frozenset([23, 25, 26])
    FOLLOW_atom_in_paramlist811 = frozenset([35, 54])
    FOLLOW_35_in_paramlist819 = frozenset([1])
    FOLLOW_NAME_in_servername845 = frozenset([37])
    FOLLOW_37_in_servername847 = frozenset([23])
    FOLLOW_NAME_in_servername851 = frozenset([1])
    FOLLOW_set_in_atom0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ExprLexer", ExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
