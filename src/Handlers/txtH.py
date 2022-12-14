from termcolor import cprint
from pathlib import Path

def txtHandler(code):
    if code == 'txt.read':
        try:
            cReadName = input('File Name? (no extension)  ')
            cFile = open('../MyDocuments/' + (cReadName + '.txt'), "r")
            return cFile.readlines()
        except:
            return cprint('Read TXT Error: {S-013x}', 'red')                # format like this for all cprint
    elif code == 'txt.write':
        try:
            cWriteName = input('File Name? (no extension)  ')
            cWrite = input('Write What?  ')
            cFile = open("./MyDocuments/" + (cWriteName + '.txt'), "a")
            cFile.write(cWrite)
            return ('Written to ' + cWriteName + '.')
        except:
            cprint('Write TXT Error: {S-014x}', 'red')
    elif code == 'txt.write_var':
        try:
            cWriteVarName = input('File Name? (no extension)  ')
            cFile = open('./MyDocuments/' + (cWriteVarName + '.txt'), 'a')
            cWriteVar = input('Variable to Write?  ')
            if cWriteVar in varName:
                cWriteVarIdx = varName.index(cWriteVar)
                cWriteVarVal = varVal[cWriteVarIdx]
                cFile.write(cWriteVarVal)
                return ('Variable ' + cWriteVar + ' written to ' + cWriteVarName + '.')
            else:
                return 'Variable not found.'
        except:
            cprint('Write Var TXT Error: {S-015x}', 'red')
    elif code == 'txt.new':
        try:
            cNewName = input('New File Name? (no extension)  ')
            cFile = open("./MyDocuments/" + (cNewName + '.txt'), "w+")
            return 'File Created.'
        except:
            cprint('New TXT Error: {S-016x}', 'red')
    elif code == 'txt.delete':
        try:
            cFileRemove = input('Delete File Name? (no extension)  ')
            os.remove("./MyDocuments/" + cFileRemove + ".txt")
            return 'File Deleted.'
        except:
            cprint('Delete TXT Error: {S-017x}', 'red')
