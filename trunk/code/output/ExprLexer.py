# $ANTLR 3.1.2 /home/didi/fyp/code/LexParse/Expr.g 2009-05-02 15:02:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
OSTRING=18
PTRASS=11
CALL=8
DOWHILE=15


class ExprLexer(Lexer):

    grammarFileName = "/home/didi/fyp/code/LexParse/Expr.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )






    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:7:7: ( 'class' )
            # /home/didi/fyp/code/LexParse/Expr.g:7:9: 'class'
            pass 
            self.match("class")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:8:7: ( '{' )
            # /home/didi/fyp/code/LexParse/Expr.g:8:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:9:7: ( '}' )
            # /home/didi/fyp/code/LexParse/Expr.g:9:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:10:7: ( 'return' )
            # /home/didi/fyp/code/LexParse/Expr.g:10:9: 'return'
            pass 
            self.match("return")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:11:7: ( '(' )
            # /home/didi/fyp/code/LexParse/Expr.g:11:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:12:7: ( ')' )
            # /home/didi/fyp/code/LexParse/Expr.g:12:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:13:7: ( 'def' )
            # /home/didi/fyp/code/LexParse/Expr.g:13:9: 'def'
            pass 
            self.match("def")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:14:7: ( '.' )
            # /home/didi/fyp/code/LexParse/Expr.g:14:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:15:7: ( 'print' )
            # /home/didi/fyp/code/LexParse/Expr.g:15:9: 'print'
            pass 
            self.match("print")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:16:7: ( 'while' )
            # /home/didi/fyp/code/LexParse/Expr.g:16:9: 'while'
            pass 
            self.match("while")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:17:7: ( 'break' )
            # /home/didi/fyp/code/LexParse/Expr.g:17:9: 'break'
            pass 
            self.match("break")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:18:7: ( 'if' )
            # /home/didi/fyp/code/LexParse/Expr.g:18:9: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:19:7: ( 'else' )
            # /home/didi/fyp/code/LexParse/Expr.g:19:9: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:20:7: ( '=' )
            # /home/didi/fyp/code/LexParse/Expr.g:20:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:21:7: ( 'new' )
            # /home/didi/fyp/code/LexParse/Expr.g:21:9: 'new'
            pass 
            self.match("new")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:22:7: ( '@' )
            # /home/didi/fyp/code/LexParse/Expr.g:22:9: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:23:7: ( 'for' )
            # /home/didi/fyp/code/LexParse/Expr.g:23:9: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:24:7: ( ';' )
            # /home/didi/fyp/code/LexParse/Expr.g:24:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:25:7: ( '==' )
            # /home/didi/fyp/code/LexParse/Expr.g:25:9: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "T__49"
    def mT__49(self, ):

        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:26:7: ( '!=' )
            # /home/didi/fyp/code/LexParse/Expr.g:26:9: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__49"



    # $ANTLR start "T__50"
    def mT__50(self, ):

        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:27:7: ( '<=' )
            # /home/didi/fyp/code/LexParse/Expr.g:27:9: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):

        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:28:7: ( '>=' )
            # /home/didi/fyp/code/LexParse/Expr.g:28:9: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):

        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:29:7: ( '<' )
            # /home/didi/fyp/code/LexParse/Expr.g:29:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):

        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:30:7: ( '>' )
            # /home/didi/fyp/code/LexParse/Expr.g:30:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:31:7: ( ',' )
            # /home/didi/fyp/code/LexParse/Expr.g:31:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__54"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:173:5: ( ( '+' | '-' )? ( '0' .. '9' )+ )
            # /home/didi/fyp/code/LexParse/Expr.g:173:7: ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            # /home/didi/fyp/code/LexParse/Expr.g:173:7: ( '+' | '-' )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 43 or LA1_0 == 45) :
                alt1 = 1
            if alt1 == 1:
                # /home/didi/fyp/code/LexParse/Expr.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # /home/didi/fyp/code/LexParse/Expr.g:173:20: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:173:20: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:177:6: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | INT )+ )
            # /home/didi/fyp/code/LexParse/Expr.g:177:8: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | INT )+
            pass 
            # /home/didi/fyp/code/LexParse/Expr.g:177:8: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | INT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 5
                LA3 = self.input.LA(1)
                if LA3 == 97 or LA3 == 98 or LA3 == 99 or LA3 == 100 or LA3 == 101 or LA3 == 102 or LA3 == 103 or LA3 == 104 or LA3 == 105 or LA3 == 106 or LA3 == 107 or LA3 == 108 or LA3 == 109 or LA3 == 110 or LA3 == 111 or LA3 == 112 or LA3 == 113 or LA3 == 114 or LA3 == 115 or LA3 == 116 or LA3 == 117 or LA3 == 118 or LA3 == 119 or LA3 == 120 or LA3 == 121 or LA3 == 122:
                    alt3 = 1
                elif LA3 == 65 or LA3 == 66 or LA3 == 67 or LA3 == 68 or LA3 == 69 or LA3 == 70 or LA3 == 71 or LA3 == 72 or LA3 == 73 or LA3 == 74 or LA3 == 75 or LA3 == 76 or LA3 == 77 or LA3 == 78 or LA3 == 79 or LA3 == 80 or LA3 == 81 or LA3 == 82 or LA3 == 83 or LA3 == 84 or LA3 == 85 or LA3 == 86 or LA3 == 87 or LA3 == 88 or LA3 == 89 or LA3 == 90:
                    alt3 = 2
                elif LA3 == 95:
                    alt3 = 3
                elif LA3 == 43 or LA3 == 45 or LA3 == 48 or LA3 == 49 or LA3 == 50 or LA3 == 51 or LA3 == 52 or LA3 == 53 or LA3 == 54 or LA3 == 55 or LA3 == 56 or LA3 == 57:
                    alt3 = 4

                if alt3 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:177:9: 'a' .. 'z'
                    pass 
                    self.matchRange(97, 122)


                elif alt3 == 2:
                    # /home/didi/fyp/code/LexParse/Expr.g:177:18: 'A' .. 'Z'
                    pass 
                    self.matchRange(65, 90)


                elif alt3 == 3:
                    # /home/didi/fyp/code/LexParse/Expr.g:177:27: '_'
                    pass 
                    self.match(95)


                elif alt3 == 4:
                    # /home/didi/fyp/code/LexParse/Expr.g:177:31: INT
                    pass 
                    self.mINT()


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "STRINGTPL"
    def mSTRINGTPL(self, ):

        try:
            _type = STRINGTPL
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:181:2: ( ( '\"' (~ '\"' )* '\"' ) )
            # /home/didi/fyp/code/LexParse/Expr.g:181:4: ( '\"' (~ '\"' )* '\"' )
            pass 
            # /home/didi/fyp/code/LexParse/Expr.g:181:4: ( '\"' (~ '\"' )* '\"' )
            # /home/didi/fyp/code/LexParse/Expr.g:181:5: '\"' (~ '\"' )* '\"'
            pass 
            self.match(34)
            # /home/didi/fyp/code/LexParse/Expr.g:181:9: (~ '\"' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((0 <= LA4_0 <= 33) or (35 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:181:10: ~ '\"'
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop4


            self.match(34)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRINGTPL"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:184:9: ( ( '\\r' )? '\\n' )
            # /home/didi/fyp/code/LexParse/Expr.g:184:11: ( '\\r' )? '\\n'
            pass 
            # /home/didi/fyp/code/LexParse/Expr.g:184:11: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # /home/didi/fyp/code/LexParse/Expr.g:184:11: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:188:5: ( '\\*' ( options {greedy=false; } : . )* '*/' )
            # /home/didi/fyp/code/LexParse/Expr.g:188:9: '\\*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match(42)
            # /home/didi/fyp/code/LexParse/Expr.g:188:14: ( options {greedy=false; } : . )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 42) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 47) :
                        alt6 = 2
                    elif ((0 <= LA6_1 <= 46) or (48 <= LA6_1 <= 65535)) :
                        alt6 = 1


                elif ((0 <= LA6_0 <= 41) or (43 <= LA6_0 <= 65535)) :
                    alt6 = 1


                if alt6 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:188:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop6


            self.match("*/")
            #action start
            self.skip();
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:192:5: ( '\\\\' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/didi/fyp/code/LexParse/Expr.g:192:7: '\\\\' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(92)
            # /home/didi/fyp/code/LexParse/Expr.g:192:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 12) or (14 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:192:12: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7


            # /home/didi/fyp/code/LexParse/Expr.g:192:26: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # /home/didi/fyp/code/LexParse/Expr.g:192:26: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            self.skip();
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Expr.g:195:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # /home/didi/fyp/code/LexParse/Expr.g:195:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # /home/didi/fyp/code/LexParse/Expr.g:195:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((9 <= LA9_0 <= 10) or LA9_0 == 13 or LA9_0 == 32) :
                    alt9 = 1


                if alt9 == 1:
                    # /home/didi/fyp/code/LexParse/Expr.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1


            #action start
            self.skip();
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # /home/didi/fyp/code/LexParse/Expr.g:1:8: ( T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | INT | NAME | STRINGTPL | NEWLINE | COMMENT | LINE_COMMENT | WS )
        alt10 = 32
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # /home/didi/fyp/code/LexParse/Expr.g:1:10: T__30
            pass 
            self.mT__30()


        elif alt10 == 2:
            # /home/didi/fyp/code/LexParse/Expr.g:1:16: T__31
            pass 
            self.mT__31()


        elif alt10 == 3:
            # /home/didi/fyp/code/LexParse/Expr.g:1:22: T__32
            pass 
            self.mT__32()


        elif alt10 == 4:
            # /home/didi/fyp/code/LexParse/Expr.g:1:28: T__33
            pass 
            self.mT__33()


        elif alt10 == 5:
            # /home/didi/fyp/code/LexParse/Expr.g:1:34: T__34
            pass 
            self.mT__34()


        elif alt10 == 6:
            # /home/didi/fyp/code/LexParse/Expr.g:1:40: T__35
            pass 
            self.mT__35()


        elif alt10 == 7:
            # /home/didi/fyp/code/LexParse/Expr.g:1:46: T__36
            pass 
            self.mT__36()


        elif alt10 == 8:
            # /home/didi/fyp/code/LexParse/Expr.g:1:52: T__37
            pass 
            self.mT__37()


        elif alt10 == 9:
            # /home/didi/fyp/code/LexParse/Expr.g:1:58: T__38
            pass 
            self.mT__38()


        elif alt10 == 10:
            # /home/didi/fyp/code/LexParse/Expr.g:1:64: T__39
            pass 
            self.mT__39()


        elif alt10 == 11:
            # /home/didi/fyp/code/LexParse/Expr.g:1:70: T__40
            pass 
            self.mT__40()


        elif alt10 == 12:
            # /home/didi/fyp/code/LexParse/Expr.g:1:76: T__41
            pass 
            self.mT__41()


        elif alt10 == 13:
            # /home/didi/fyp/code/LexParse/Expr.g:1:82: T__42
            pass 
            self.mT__42()


        elif alt10 == 14:
            # /home/didi/fyp/code/LexParse/Expr.g:1:88: T__43
            pass 
            self.mT__43()


        elif alt10 == 15:
            # /home/didi/fyp/code/LexParse/Expr.g:1:94: T__44
            pass 
            self.mT__44()


        elif alt10 == 16:
            # /home/didi/fyp/code/LexParse/Expr.g:1:100: T__45
            pass 
            self.mT__45()


        elif alt10 == 17:
            # /home/didi/fyp/code/LexParse/Expr.g:1:106: T__46
            pass 
            self.mT__46()


        elif alt10 == 18:
            # /home/didi/fyp/code/LexParse/Expr.g:1:112: T__47
            pass 
            self.mT__47()


        elif alt10 == 19:
            # /home/didi/fyp/code/LexParse/Expr.g:1:118: T__48
            pass 
            self.mT__48()


        elif alt10 == 20:
            # /home/didi/fyp/code/LexParse/Expr.g:1:124: T__49
            pass 
            self.mT__49()


        elif alt10 == 21:
            # /home/didi/fyp/code/LexParse/Expr.g:1:130: T__50
            pass 
            self.mT__50()


        elif alt10 == 22:
            # /home/didi/fyp/code/LexParse/Expr.g:1:136: T__51
            pass 
            self.mT__51()


        elif alt10 == 23:
            # /home/didi/fyp/code/LexParse/Expr.g:1:142: T__52
            pass 
            self.mT__52()


        elif alt10 == 24:
            # /home/didi/fyp/code/LexParse/Expr.g:1:148: T__53
            pass 
            self.mT__53()


        elif alt10 == 25:
            # /home/didi/fyp/code/LexParse/Expr.g:1:154: T__54
            pass 
            self.mT__54()


        elif alt10 == 26:
            # /home/didi/fyp/code/LexParse/Expr.g:1:160: INT
            pass 
            self.mINT()


        elif alt10 == 27:
            # /home/didi/fyp/code/LexParse/Expr.g:1:164: NAME
            pass 
            self.mNAME()


        elif alt10 == 28:
            # /home/didi/fyp/code/LexParse/Expr.g:1:169: STRINGTPL
            pass 
            self.mSTRINGTPL()


        elif alt10 == 29:
            # /home/didi/fyp/code/LexParse/Expr.g:1:179: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt10 == 30:
            # /home/didi/fyp/code/LexParse/Expr.g:1:187: COMMENT
            pass 
            self.mCOMMENT()


        elif alt10 == 31:
            # /home/didi/fyp/code/LexParse/Expr.g:1:195: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt10 == 32:
            # /home/didi/fyp/code/LexParse/Expr.g:1:208: WS
            pass 
            self.mWS()







    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\1\uffff\1\31\2\uffff\1\31\2\uffff\1\31\1\uffff\5\31\1\51\1\31"
        u"\1\uffff\1\31\2\uffff\1\55\1\57\2\uffff\1\60\2\uffff\1\37\1\61"
        u"\3\uffff\6\31\1\70\1\31\2\uffff\2\31\6\uffff\2\31\1\76\3\31\1\uffff"
        u"\1\31\1\103\1\104\2\31\1\uffff\3\31\1\112\2\uffff\1\113\1\31\1"
        u"\115\1\116\1\117\2\uffff\1\120\4\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\121\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\11\1\154\2\uffff\1\145\2\uffff\1\145\1\uffff\1\162\1\150\1\162"
        u"\1\146\1\154\1\75\1\145\1\uffff\1\157\2\uffff\2\75\1\uffff\1\60"
        u"\1\53\2\uffff\1\12\1\11\3\uffff\1\141\1\164\1\146\2\151\1\145\1"
        u"\53\1\163\2\uffff\1\167\1\162\6\uffff\1\163\1\165\1\53\1\156\1"
        u"\154\1\141\1\uffff\1\145\2\53\1\163\1\162\1\uffff\1\164\1\145\1"
        u"\153\1\53\2\uffff\1\53\1\156\3\53\2\uffff\1\53\4\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\175\1\154\2\uffff\1\145\2\uffff\1\145\1\uffff\1\162\1\150\1"
        u"\162\1\146\1\154\1\75\1\145\1\uffff\1\157\2\uffff\2\75\1\uffff"
        u"\1\71\1\172\2\uffff\1\12\1\40\3\uffff\1\141\1\164\1\146\2\151\1"
        u"\145\1\172\1\163\2\uffff\1\167\1\162\6\uffff\1\163\1\165\1\172"
        u"\1\156\1\154\1\141\1\uffff\1\145\2\172\1\163\1\162\1\uffff\1\164"
        u"\1\145\1\153\1\172\2\uffff\1\172\1\156\3\172\2\uffff\1\172\4\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\uffff\1\5\1\6\1\uffff\1\10\7\uffff\1\20\1\uffff"
        u"\1\22\1\24\2\uffff\1\31\2\uffff\1\33\1\34\2\uffff\1\36\1\37\1\40"
        u"\10\uffff\1\23\1\16\2\uffff\1\25\1\27\1\26\1\30\1\32\1\35\6\uffff"
        u"\1\14\5\uffff\1\7\4\uffff\1\17\1\21\5\uffff\1\15\1\1\1\uffff\1"
        u"\11\1\12\1\13\1\4"
        )

    DFA10_special = DFA.unpack(
        u"\121\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\37\1\34\2\uffff\1\33\22\uffff\1\37\1\23\1\32\5\uffff"
        u"\1\5\1\6\1\35\1\27\1\26\1\27\1\10\1\uffff\12\30\1\uffff\1\22\1"
        u"\24\1\16\1\25\1\uffff\1\20\32\31\1\uffff\1\36\2\uffff\1\31\1\uffff"
        u"\1\31\1\13\1\1\1\7\1\15\1\21\2\31\1\14\4\31\1\17\1\31\1\11\1\31"
        u"\1\4\4\31\1\12\3\31\1\2\1\uffff\1\3"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\30"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\30\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\2\37\2\uffff\1\37\22\uffff\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff"
        u"\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    DFA10 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ExprLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
