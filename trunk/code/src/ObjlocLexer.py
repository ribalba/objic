# $ANTLR 3.1.2 /home/didi/fyp/code/LexParse/Objloc.g 2009-04-15 15:11:42

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class ObjlocLexer(Lexer):

    grammarFileName = "/home/didi/fyp/code/LexParse/Objloc.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "T__11"
    def mT__11(self, ):

        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Objloc.g:7:7: ( '@' )
            # /home/didi/fyp/code/LexParse/Objloc.g:7:9: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__11"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Objloc.g:25:5: ( ( '0' .. '9' )+ )
            # /home/didi/fyp/code/LexParse/Objloc.g:25:7: ( '0' .. '9' )+
            pass 
            # /home/didi/fyp/code/LexParse/Objloc.g:25:7: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:25:7: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1





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

            # /home/didi/fyp/code/LexParse/Objloc.g:27:6: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '.' | INT )+ )
            # /home/didi/fyp/code/LexParse/Objloc.g:27:8: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '.' | INT )+
            pass 
            # /home/didi/fyp/code/LexParse/Objloc.g:27:8: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '.' | INT )+
            cnt2 = 0
            while True: #loop2
                alt2 = 6
                LA2 = self.input.LA(1)
                if LA2 == 97 or LA2 == 98 or LA2 == 99 or LA2 == 100 or LA2 == 101 or LA2 == 102 or LA2 == 103 or LA2 == 104 or LA2 == 105 or LA2 == 106 or LA2 == 107 or LA2 == 108 or LA2 == 109 or LA2 == 110 or LA2 == 111 or LA2 == 112 or LA2 == 113 or LA2 == 114 or LA2 == 115 or LA2 == 116 or LA2 == 117 or LA2 == 118 or LA2 == 119 or LA2 == 120 or LA2 == 121 or LA2 == 122:
                    alt2 = 1
                elif LA2 == 65 or LA2 == 66 or LA2 == 67 or LA2 == 68 or LA2 == 69 or LA2 == 70 or LA2 == 71 or LA2 == 72 or LA2 == 73 or LA2 == 74 or LA2 == 75 or LA2 == 76 or LA2 == 77 or LA2 == 78 or LA2 == 79 or LA2 == 80 or LA2 == 81 or LA2 == 82 or LA2 == 83 or LA2 == 84 or LA2 == 85 or LA2 == 86 or LA2 == 87 or LA2 == 88 or LA2 == 89 or LA2 == 90:
                    alt2 = 2
                elif LA2 == 95:
                    alt2 = 3
                elif LA2 == 46:
                    alt2 = 4
                elif LA2 == 48 or LA2 == 49 or LA2 == 50 or LA2 == 51 or LA2 == 52 or LA2 == 53 or LA2 == 54 or LA2 == 55 or LA2 == 56 or LA2 == 57:
                    alt2 = 5

                if alt2 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:27:9: 'a' .. 'z'
                    pass 
                    self.matchRange(97, 122)


                elif alt2 == 2:
                    # /home/didi/fyp/code/LexParse/Objloc.g:27:18: 'A' .. 'Z'
                    pass 
                    self.matchRange(65, 90)


                elif alt2 == 3:
                    # /home/didi/fyp/code/LexParse/Objloc.g:27:27: '_'
                    pass 
                    self.match(95)


                elif alt2 == 4:
                    # /home/didi/fyp/code/LexParse/Objloc.g:27:31: '.'
                    pass 
                    self.match(46)


                elif alt2 == 5:
                    # /home/didi/fyp/code/LexParse/Objloc.g:27:35: INT
                    pass 
                    self.mINT()


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

    # $ANTLR end "NAME"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /home/didi/fyp/code/LexParse/Objloc.g:29:9: ( ( '\\r' )? '\\n' )
            # /home/didi/fyp/code/LexParse/Objloc.g:29:11: ( '\\r' )? '\\n'
            pass 
            # /home/didi/fyp/code/LexParse/Objloc.g:29:11: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # /home/didi/fyp/code/LexParse/Objloc.g:29:11: '\\r'
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

            # /home/didi/fyp/code/LexParse/Objloc.g:33:5: ( '\\*' ( options {greedy=false; } : . )* '*/' )
            # /home/didi/fyp/code/LexParse/Objloc.g:33:9: '\\*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match(42)
            # /home/didi/fyp/code/LexParse/Objloc.g:33:14: ( options {greedy=false; } : . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 42) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 47) :
                        alt4 = 2
                    elif ((0 <= LA4_1 <= 46) or (48 <= LA4_1 <= 65535)) :
                        alt4 = 1


                elif ((0 <= LA4_0 <= 41) or (43 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:33:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop4


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

            # /home/didi/fyp/code/LexParse/Objloc.g:37:5: ( '\\\\' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/didi/fyp/code/LexParse/Objloc.g:37:7: '\\\\' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(92)
            # /home/didi/fyp/code/LexParse/Objloc.g:37:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:37:12: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5


            # /home/didi/fyp/code/LexParse/Objloc.g:37:26: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # /home/didi/fyp/code/LexParse/Objloc.g:37:26: '\\r'
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

            # /home/didi/fyp/code/LexParse/Objloc.g:40:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # /home/didi/fyp/code/LexParse/Objloc.g:40:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # /home/didi/fyp/code/LexParse/Objloc.g:40:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((9 <= LA7_0 <= 10) or LA7_0 == 13 or LA7_0 == 32) :
                    alt7 = 1


                if alt7 == 1:
                    # /home/didi/fyp/code/LexParse/Objloc.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1


            #action start
            self.skip()
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # /home/didi/fyp/code/LexParse/Objloc.g:1:8: ( T__11 | INT | NAME | NEWLINE | COMMENT | LINE_COMMENT | WS )
        alt8 = 7
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:10: T__11
            pass 
            self.mT__11()


        elif alt8 == 2:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:16: INT
            pass 
            self.mINT()


        elif alt8 == 3:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:20: NAME
            pass 
            self.mNAME()


        elif alt8 == 4:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:25: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt8 == 5:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:33: COMMENT
            pass 
            self.mCOMMENT()


        elif alt8 == 6:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:41: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt8 == 7:
            # /home/didi/fyp/code/LexParse/Objloc.g:1:54: WS
            pass 
            self.mWS()







    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\2\uffff\1\11\1\uffff\1\10\1\12\5\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\11\1\uffff\1\56\1\uffff\1\12\1\11\5\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\172\1\uffff\1\172\1\uffff\1\12\1\40\5\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\2\uffff\1\5\1\6\1\7\1\2\1\4"
        )

    DFA8_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\1\10\1\5\2\uffff\1\4\22\uffff\1\10\11\uffff\1\6\3\uffff"
        u"\1\3\1\uffff\12\2\6\uffff\1\1\32\3\1\uffff\1\7\2\uffff\1\3\1\uffff"
        u"\32\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\2\7\uffff\32\3\4\uffff\1\3\1\uffff"
        u"\32\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\2\10\2\uffff\1\10\22\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    DFA8 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ObjlocLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
