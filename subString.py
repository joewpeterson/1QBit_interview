#!/bin/python

def divide_symbols(string):
    '''
    Input: a string
    Output: an array of strings, each a substring of string with a 
    condition that each entry in the array must be comparsed of characters
    belong to no other entry.
    '''
    
    ## Define output list
    substrings = []

    ## Begin lookinf for substrings starting at the fisrt char
    wordStart = 0

    ## run over all char positions in the string
    while wordStart < len(string):

        ## Set the end of this word to the chars last occuance
        wordEnd = string.rfind(string[wordStart], wordStart)

        ## Check if any char between wordStart and wordEnd
        ## extend beyond wordEnd. If, yes, redefine wordEnd
        wordSearch = wordStart + 1
        while wordSearch < wordEnd:
            testEnd = string.rfind(string[wordSearch], wordEnd + 1)
            if testEnd >wordEnd:
                wordEnd = testEnd

            wordSearch += 1

        ## Append the word to the substring list
        substrings.append(string[wordStart:wordEnd + 1])

        ## start the next word after the one just found
        wordStart = wordEnd +1

        
    return substrings

one = divide_symbols("abcdefghijklamnopqrstuvwxyz")
print(one)
