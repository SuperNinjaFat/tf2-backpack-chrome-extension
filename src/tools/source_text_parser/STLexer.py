# $ANTLR 3.1.1 ST.g 2010-07-15 11:11:20

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LT=12
WS=10
T__15=15
T__14=14
LETTER=6
UnicodeEscape=7
CHAR=5
LINECOMMENT=13
COMMENT=11
EOF=-1
HexDigit=9
EscapeSequence=8
STRING=4


class STLexer(Lexer):

    grammarFileName = "ST.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "T__14"
    def mT__14(self, ):

        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # ST.g:7:7: ( '{' )
            # ST.g:7:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):

        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # ST.g:8:7: ( '}' )
            # ST.g:8:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__15"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):

        try:
            # ST.g:25:14: (~ ( '\"' | '\\\\' ) )
            # ST.g:25:16: ~ ( '\"' | '\\\\' )
            pass 
            if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # ST.g:27:5: ( '\\u0024' | '\\u0041' .. '\\u005a' | '\\u005f' | '\\u0061' .. '\\u007a' | '\\u00c0' .. '\\u00d6' | '\\u00d8' .. '\\u00f6' | '\\u00f8' .. '\\u00ff' | '\\u0100' .. '\\u1fff' | '\\u3040' .. '\\u318f' | '\\u3300' .. '\\u337f' | '\\u3400' .. '\\u3d2d' | '\\u4e00' .. '\\u9fff' | '\\uf900' .. '\\ufaff' | '\\u0030' .. '\\u0039' | '\\u0660' .. '\\u0669' | '\\u06f0' .. '\\u06f9' | '\\u0966' .. '\\u096f' | '\\u09e6' .. '\\u09ef' | '\\u0a66' .. '\\u0a6f' | '\\u0ae6' .. '\\u0aef' | '\\u0b66' .. '\\u0b6f' | '\\u0be7' .. '\\u0bef' | '\\u0c66' .. '\\u0c6f' | '\\u0ce6' .. '\\u0cef' | '\\u0d66' .. '\\u0d6f' | '\\u0e50' .. '\\u0e59' | '\\u0ed0' .. '\\u0ed9' | '\\u1040' .. '\\u1049' )
            # ST.g:
            pass 
            if self.input.LA(1) == 36 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 8191) or (12352 <= self.input.LA(1) <= 12687) or (13056 <= self.input.LA(1) <= 13183) or (13312 <= self.input.LA(1) <= 15661) or (19968 <= self.input.LA(1) <= 40959) or (63744 <= self.input.LA(1) <= 64255):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "EscapeSequence"
    def mEscapeSequence(self, ):

        try:
            # ST.g:59:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UnicodeEscape )
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 92) :
                LA1_1 = self.input.LA(2)

                if (LA1_1 == 34 or LA1_1 == 39 or LA1_1 == 92 or LA1_1 == 98 or LA1_1 == 102 or LA1_1 == 110 or LA1_1 == 114 or LA1_1 == 116) :
                    alt1 = 1
                elif (LA1_1 == 117) :
                    alt1 = 2
                else:
                    nvae = NoViableAltException("", 1, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # ST.g:59:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt1 == 2:
                # ST.g:60:9: UnicodeEscape
                pass 
                self.mUnicodeEscape()



        finally:

            pass

    # $ANTLR end "EscapeSequence"



    # $ANTLR start "UnicodeEscape"
    def mUnicodeEscape(self, ):

        try:
            # ST.g:64:5: ( '\\\\' 'u' HexDigit HexDigit HexDigit HexDigit )
            # ST.g:64:9: '\\\\' 'u' HexDigit HexDigit HexDigit HexDigit
            pass 
            self.match(92)
            self.match(117)
            self.mHexDigit()
            self.mHexDigit()
            self.mHexDigit()
            self.mHexDigit()




        finally:

            pass

    # $ANTLR end "UnicodeEscape"



    # $ANTLR start "HexDigit"
    def mHexDigit(self, ):

        try:
            # ST.g:68:5: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # ST.g:68:7: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HexDigit"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # ST.g:73:3: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # ST.g:73:5: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # ST.g:75:5: ( '\"' ( EscapeSequence | ~ ( '\\\\' | '\"' ) )* '\"' )
            # ST.g:75:7: '\"' ( EscapeSequence | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # ST.g:75:11: ( EscapeSequence | ~ ( '\\\\' | '\"' ) )*
            while True: #loop2
                alt2 = 3
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 92) :
                    alt2 = 1
                elif ((0 <= LA2_0 <= 33) or (35 <= LA2_0 <= 91) or (93 <= LA2_0 <= 65535)) :
                    alt2 = 2


                if alt2 == 1:
                    # ST.g:75:12: EscapeSequence
                    pass 
                    self.mEscapeSequence()


                elif alt2 == 2:
                    # ST.g:75:29: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # ST.g:81:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # ST.g:81:7: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")
            # ST.g:81:12: ( options {greedy=false; } : . )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 42) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 47) :
                        alt3 = 2
                    elif ((0 <= LA3_1 <= 46) or (48 <= LA3_1 <= 65535)) :
                        alt3 = 1


                elif ((0 <= LA3_0 <= 41) or (43 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # ST.g:81:39: .
                    pass 
                    self.matchAny()


                else:
                    break #loop3


            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINECOMMENT"
    def mLINECOMMENT(self, ):

        try:
            _type = LINECOMMENT
            _channel = DEFAULT_CHANNEL

            # ST.g:85:5: ( '//' (~ ( LT ) )* | '[$' ( CHAR )* )
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 47) :
                alt6 = 1
            elif (LA6_0 == 91) :
                alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # ST.g:85:7: '//' (~ ( LT ) )*
                pass 
                self.match("//")
                # ST.g:85:12: (~ ( LT ) )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((0 <= LA4_0 <= 9) or (11 <= LA4_0 <= 12) or (14 <= LA4_0 <= 8231) or (8234 <= LA4_0 <= 65535)) :
                        alt4 = 1


                    if alt4 == 1:
                        # ST.g:85:12: ~ ( LT )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 8231) or (8234 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop4


                #action start
                _channel=HIDDEN;
                #action end


            elif alt6 == 2:
                # ST.g:86:7: '[$' ( CHAR )*
                pass 
                self.match("[$")
                # ST.g:86:12: ( CHAR )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((0 <= LA5_0 <= 33) or (35 <= LA5_0 <= 91) or (93 <= LA5_0 <= 65535)) :
                        alt5 = 1


                    if alt5 == 1:
                        # ST.g:86:12: CHAR
                        pass 
                        self.mCHAR()


                    else:
                        break #loop5


                #action start
                _channel=HIDDEN;
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINECOMMENT"



    # $ANTLR start "LT"
    def mLT(self, ):

        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # ST.g:90:5: ( '\\n' | '\\r' | '\\u2028' | '\\u2029' )
            # ST.g:
            pass 
            if self.input.LA(1) == 10 or self.input.LA(1) == 13 or (8232 <= self.input.LA(1) <= 8233):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LT"



    def mTokens(self):
        # ST.g:1:8: ( T__14 | T__15 | WS | STRING | COMMENT | LINECOMMENT | LT )
        alt7 = 7
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # ST.g:1:10: T__14
            pass 
            self.mT__14()


        elif alt7 == 2:
            # ST.g:1:16: T__15
            pass 
            self.mT__15()


        elif alt7 == 3:
            # ST.g:1:22: WS
            pass 
            self.mWS()


        elif alt7 == 4:
            # ST.g:1:25: STRING
            pass 
            self.mSTRING()


        elif alt7 == 5:
            # ST.g:1:32: COMMENT
            pass 
            self.mCOMMENT()


        elif alt7 == 6:
            # ST.g:1:40: LINECOMMENT
            pass 
            self.mLINECOMMENT()


        elif alt7 == 7:
            # ST.g:1:52: LT
            pass 
            self.mLT()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\4\uffff\1\52\4\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\u2029\4\uffff\1\57\4\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\uffff\1\6\1\3\1\7\1\5"
        )

    DFA7_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\7\1\3\1\uffff\1\7\1\3\22\uffff\1\7\1\uffff\1\4\14"
        u"\uffff\1\5\53\uffff\1\6\37\uffff\1\1\1\uffff\1\2\u1faa\uffff\2"
        u"\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\4\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(STLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
