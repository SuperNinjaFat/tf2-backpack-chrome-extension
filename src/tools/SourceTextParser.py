# $ANTLR 3.1.1 SourceText.g 2010-03-18 17:48:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LT=12
WS=10
T__15=15
LETTER=6
T__14=14
UnicodeEscape=7
CHAR=5
LINECOMMENT=13
COMMENT=11
EOF=-1
HexDigit=9
EscapeSequence=8
STRING=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "STRING", "CHAR", "LETTER", "UnicodeEscape", "EscapeSequence", "HexDigit", 
    "WS", "COMMENT", "LT", "LINECOMMENT", "'{'", "'}'"
]




class SourceTextParser(Parser):
    grammarFileName = "SourceText.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
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


    class source_mapping_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "source_mapping"
    # SourceText.g:15:1: source_mapping[value] : ( element[value] )* ;
    def source_mapping(self, value):

        retval = self.source_mapping_return()
        retval.start = self.input.LT(1)

        root_0 = None

        element1 = None



        try:
            try:
                # SourceText.g:16:5: ( ( element[value] )* )
                # SourceText.g:16:7: ( element[value] )*
                pass 
                root_0 = self._adaptor.nil()

                # SourceText.g:16:7: ( element[value] )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == STRING) :
                        alt1 = 1


                    if alt1 == 1:
                        # SourceText.g:16:8: element[value]
                        pass 
                        self._state.following.append(self.FOLLOW_element_in_source_mapping45)
                        element1 = self.element(value)

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, element1.tree)


                    else:
                        break #loop1





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

    # $ANTLR end "source_mapping"

    class element_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "element"
    # SourceText.g:20:1: element[mapping] : ( item '{' ( element[n] )* '}' | i0= item i1= item );
    def element(self, mapping):

        retval = self.element_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal3 = None
        char_literal5 = None
        i0 = None

        i1 = None

        item2 = None

        element4 = None


        char_literal3_tree = None
        char_literal5_tree = None

        try:
            try:
                # SourceText.g:21:5: ( item '{' ( element[n] )* '}' | i0= item i1= item )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == STRING) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == STRING) :
                        alt3 = 2
                    elif (LA3_1 == 14) :
                        alt3 = 1
                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # SourceText.g:21:9: item '{' ( element[n] )* '}'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_item_in_element69)
                    item2 = self.item()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, item2.tree)
                    #action start
                    n = mapping[((item2 is not None) and [item2.value] or [None])[0]] = {} 
                    #action end
                    char_literal3=self.match(self.input, 14, self.FOLLOW_14_in_element89)

                    char_literal3_tree = self._adaptor.createWithPayload(char_literal3)
                    self._adaptor.addChild(root_0, char_literal3_tree)

                    # SourceText.g:23:13: ( element[n] )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == STRING) :
                            alt2 = 1


                        if alt2 == 1:
                            # SourceText.g:23:14: element[n]
                            pass 
                            self._state.following.append(self.FOLLOW_element_in_element92)
                            element4 = self.element(n)

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, element4.tree)


                        else:
                            break #loop2


                    char_literal5=self.match(self.input, 15, self.FOLLOW_15_in_element97)

                    char_literal5_tree = self._adaptor.createWithPayload(char_literal5)
                    self._adaptor.addChild(root_0, char_literal5_tree)



                elif alt3 == 2:
                    # SourceText.g:25:9: i0= item i1= item
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_item_in_element110)
                    i0 = self.item()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, i0.tree)
                    self._state.following.append(self.FOLLOW_item_in_element114)
                    i1 = self.item()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, i1.tree)
                    #action start
                    mapping[i0.value] = unicode(i1.value) 
                    #action end


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

    # $ANTLR end "element"

    class item_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.value = None
            self.tree = None




    # $ANTLR start "item"
    # SourceText.g:30:1: item returns [value] : s0= STRING ;
    def item(self, ):

        retval = self.item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        s0 = None

        s0_tree = None

        try:
            try:
                # SourceText.g:31:5: (s0= STRING )
                # SourceText.g:31:9: s0= STRING
                pass 
                root_0 = self._adaptor.nil()

                s0=self.match(self.input, STRING, self.FOLLOW_STRING_in_item150)

                s0_tree = self._adaptor.createWithPayload(s0)
                self._adaptor.addChild(root_0, s0_tree)

                #action start
                retval.value = s0.text[1:-1] 
                #action end



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

    # $ANTLR end "item"


    # Delegated rules


 

    FOLLOW_element_in_source_mapping45 = frozenset([1, 4])
    FOLLOW_item_in_element69 = frozenset([14])
    FOLLOW_14_in_element89 = frozenset([4, 15])
    FOLLOW_element_in_element92 = frozenset([4, 15])
    FOLLOW_15_in_element97 = frozenset([1])
    FOLLOW_item_in_element110 = frozenset([4])
    FOLLOW_item_in_element114 = frozenset([1])
    FOLLOW_STRING_in_item150 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SourceTextLexer", SourceTextParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)