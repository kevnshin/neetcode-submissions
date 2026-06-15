class Solution:
    def isValid(self, s: str) -> bool:
        parens:list = []
        for char in s:
            if isOpenParen(char):
                parens.append(char)
            elif isCloseParen(char):
                if len(parens) is 0:
                    return False
                open:str = parens[len(parens) - 1]
                if isMatchingClose(open = open, close = char):
                    parens.pop()
                else:
                    return False
        return len(parens) is 0


def isOpenParen(s: str) -> bool:
    return s is '(' or s is '{' or s is '['

def isCloseParen(s: str) -> bool:
    return s is ')' or s is '}' or s is ']'

def isMatchingClose(open: str, close: str) -> bool:
    if open is '{':
        return close is '}'
    elif open is '(':
        return close is ')'
    elif open is '[':
        return close is ']'
        