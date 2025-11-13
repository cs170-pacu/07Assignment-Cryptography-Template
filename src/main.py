################################################################################
# File name:    main.py
# Author:       YOUR NAME HERE
# Date:         11/13/2025
# Class:        CS 170
# Assignment:   07Cryptography
# Purpose:      Demonstrate Codespaces & Python
# Hours:        1.5
################################################################################

# HELPER FUNCTIONS
################################################################################
def printHeading(sHeading):
    '''Displays a passed in heading with a line of 75 asterisks above 
       and below it
    Parameter: 
        sHeading (string): Heading to print
    Returns:
        Nothing
    '''
    pass

def getKeys():
    '''Asks for the keys. Valid keys are between 2 and 25 characters.
       Will convert all keys to upper case.
    Parameters:
        None
    returns:
        string: the keys
    '''
    pass

def readFile(sType):
    '''Prompts for a filename, opens a file for reading,
       and stores contents in a list.
    Parameters:
        sType (string): either plaintext or ciphertext
    Returns:
        list: empty if file was not opened correctly
    '''
    pass

def encodeStrings(lText, lMappingTable):
    '''Encode list of strings using the passed in mapping table
    Parameters:
        lText (list): a list of strings to be encoded
        lMappingTable (list): the mapping table
    Returns:
        list: a list of strings, which is the encoded input list 
    '''
    pass

def decodeStrings(lText, lMappingTable):
    '''Decode list of strings using the passed in mapping table
    Parameters:
        lText (list): a list of strings to be decoded
        lMappingTable (list): the mapping table
    Returns:
        list: a list of strings, which is the decoded input list
    '''
    pass

def writeFile(sType, lOutput, sWord):
    '''Open the output file, then write the contents of the list to the file
    Parameters:
        sType (string): either the word plaintext or ciphertext
        lOutput (list): contents to be output to the file
        sWord (string): either the word encrypted or decrypted
    Returns:
        None
    '''
    pass
################################################################################


# FUNCTIONS TO CREATE MAPPING TABLE
################################################################################
def incrementCharacter(sLetter):
    '''Advance the passed-in letter to the next letter in the alphabet. 
       For example, 'A' becomes 'B', 'G' becomes 'H'
       If the letter is 'Z' then advance to 'A'
    Parameters:
        sLetter (string): the character to advance
    Returns:
        string: the next letter in the alphabet
    '''
    if sLetter is not None and 1 == len(sLetter):
        if 'Z' == sLetter:
            sNextLetter = 'A'
        else:
            sAsciiValue = ord(sLetter)
            sNextLetter = chr(sAsciiValue+1)
        return sNextLetter

def constructOneMapping(sLetter):
    '''Construct one mapping dictionary beginning with the passed in letter
    If sLetter is X, mapping dictionary will be:
    {'A':'X', 'B':'Y', 'C':'Z', 'D':'A'.....}
    Parameters:
        sLetter (character): the starting character for the mapping
    Returns:
        dictionary: that represents the mapping
    '''
    pass

def constructMappingTable(sKeys):
    '''Create a list of mappings based on the passed-in keys
    If sKeys is: 'COX',
    the list will be:
    [
     {'A':'C', 'B':'D', 'C':'E', 'D':'F'.....}
     {'A':'O', 'B':'P', 'C':'Q', 'D':'R'.....}
     {'A':'X', 'B':'Y', 'C':'Z', 'D':'A'.....}
    ]
    Parameters:
        sKeys (string): the keys (2-25 uppercase letters)
    Returns:
        list: the list of mappings based on the passed in keys
    '''
    pass
################################################################################



# FUNCTIONS TO ENCODE AND DECODE A CHARACTER
################################################################################
def encode(sPlainLetter, lMappingTable):
    '''Encodes one plain letter to the encoded letter using the 
       passed in mapping table
    Parameters:
        sPlainLetter (string): the plain letter
        lMappingTable (list): the mapping table
    Returns:
        string: the encoded letter
    '''
    pass

def decode(sEncodedLetter, lMappingTable):
    '''Decodes one encoded letter to the plain letter using the 
       passed in mapping table
    Parameters:
        sEncodedLetter (string): the encoded letter
        lMappingTable (list): the mapping table
    Returns:
        string: the plain letter
    '''
    pass
################################################################################



# MAIN CODE
################################################################################
TITLE = 'Cryptography - Enigma Machine'
ENCRYPT = 'E'
DECRYPT = 'D'
QUIT = 'Q'
dConstants = {ENCRYPT:['plaintext', 'ciphertext', 'encrypted'], 
              DECRYPT:['ciphertext', 'plaintext', 'decrypted']}
printHeading(TITLE)

sInput = input('Enter E) for encryption, D) for decryption, or Q) for quit: ').upper()
while QUIT != sInput:
    if ENCRYPT == sInput or DECRYPT == sInput:
        sKeys = getKeys()
        lMappingTable = constructMappingTable(sKeys)
        
        # Uncomment next two lines for part 1!!!!!
        #for dMap in lMappingTable:
        #    print(dMap)
        
        lInput = readFile(dConstants[sInput][0])
        if ENCRYPT == sInput:
            lOutput = encodeStrings(lInput, lMappingTable)
        else:
            lOutput = decodeStrings(lInput, lMappingTable)
        
        # Remove next line for part 2        
        print(lOutput)

        writeFile(dConstants[sInput][1], lOutput, dConstants[sInput][2])
    sInput = input('Enter E) for encryption, D) for decryption, or Q) for quit: ').upper()
