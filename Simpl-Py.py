# Variables + Imports
# ------------------------------
# CHANGE THE DATE AND VERSION!!!
# ------------------------------

# todo 0.7.0: add modules folder in extras
try:
    import wmi
    import os
    from termcolor import colored, cprint
    from pathlib import Path
    import importlib
    import sys
    version, updated = '0.6.9', '12/8/2022'
    varName, varVal, varType = [], [], []
    cMathInts, cMathSub, cMathMult, cMathDiv = [], 0, 0, 0
    mods = []
    cBeta = 0
except:
    print('ROOT ERROR: VARIABLES/IMPORTS COULD NOT BE LOADED')

# Functions
def systemInfoDisp():
    try:
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]
        print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")
    except:
        cprint('System Info Error: {S-001x}', 'red')
        exit()

def welcomeDisp():
    try:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
        print('Type "help", "copyright", or "credits" for more information.')
        print('Type "/Simpl-Py" and "beta" to try the current beta features.')
    except:
        cprint('Welcome Display Error: {S-002x}', 'red')

def moduleHandler(code):
    if '@' in code:
        modN = ('SPY_' + code.replace('@', ''))
        cImp = __import__(modN)
        modin = input('What Function?  ')
        func = getattr(cImp, 'init')
        return func(modin)

def inputHandler(code):
    if '@' in code:
        modH = moduleHandler(code)
        return modH
    else:
        pH = printHandler(code)
        if pH != None: return pH
        else:
            vH = varHandler(code)
            if vH != None: return vH
            else:
                txtH = txtHandler(code)
                if txtH != None: return txtH
                else:
                    slashH = slashHandler(code)
                    if slashH != None: return slashH
                    else: return ''

def printHandler(code):
    # Print Functions  ### PUT BETA ON ECHO PRINT
    if code == 'print':
        try:
            cPrint = input('Print What?  ')
            return cPrint
        except:
            cprint('Print Error: {S-004x}', 'red')
    elif code == 'print.echo':
        try:
            cEcho = input('Echo What?  ')
            cEchoSpace = int(input('Echo Space?  '))
            cEcho = cEcho + (' ' * cEchoSpace)
            cEchoAmount = int(input('Echo Amount?  '))
            cEchoOut = cEcho * cEchoAmount
            return cEchoOut
        except:
            cprint('Print Echo Error: {S-005x}', 'red')
    elif code == 'print_math':
        try:
            cMathInts.clear()
            cMathIntCount = int(input('Number of Integers: '))
            for i in range(0, cMathIntCount):
                cMathInts.append(int(input('Integer:  ')))
            cMathOp = input('Operator (+, -, *, /):  ')
            if cMathOp == '+':
                return sum(cMathInts)
            elif cMathOp == '-':
                cMathSub = cMathInts[0]
                for i in range(1, len(cMathInts)):
                    cMathSub -= cMathInts[i]
                return cMathSub
            elif cMathOp == '*':
                cMathMult = cMathInts[0]
                for i in range(1, len(cMathInts)):
                    cMathMult *= cMathInts[i]
                return cMathMult
            elif cMathOp == '/':
                cMathDiv = cMathInts[0]
                for i in range(1, len(cMathInts)):
                    cMathDiv /= cMathInts[i]
                return cMathDiv
            else:
                return 'Invalid operator.'
        except:
            cprint('Print Math Error: {S-006x}', 'red')
    elif code == 'print.correct':
        try:
            cCorrect = input('Correct What?  ')
            return cCorrect.capitalize()
        except:
            cprint('Print Correct Error: {S-007x}', 'red')
    elif code == 'print.lower':
        try:
            cLower = input('Lower What?  ')
            return cLower.lower()
        except:
            cprint('Print Lower Error: {S-008x}', 'red')
    elif code == 'print.upper':
        try:
            cUpper = input('Upper What?  ')
            return cUpper.upper()
        except:
            cprint('Print Upper Error: {S-009x}', 'red')
    elif code == 'print.backwards':
        try:
            cBackwards = input('Backwards What?  ')
            return (cBackwards [::-1])
        except:
            cprint('Print Backwards Error: {S-010x}', 'red')

def varHandler(code):
    # Variables
    if code == 'var.new':
        try:
            cVarName = input('New Var Name:  ')
            varName.append(cVarName)
            cVarVal = input('Enter Value:  ')
            varVal.append(cVarVal)
            try:
                cIntStore = int(cVarVal)
                varType.append(type(cIntStore))
            except:
                varType.append(type(cVarVal))
            print(varType)
            return ('Created ' + cVarName + ' with value ' + cVarVal)
        except:
            cprint('New Var Error: {S-011x}', 'red')

    elif code == 'print_var':
        try:
            cPrintVar = input('What Variable?  ')
            if cPrintVar in varName:
                cVarFindIndex = varName.index(str(cPrintVar))
                cVarFindVal = varVal[cVarFindIndex]
                return cVarFindVal
            else:
                return 'Variable not found.'
        except:
            cprint('Print Var Error: {S-012x}', 'red')

def txtHandler(code):
    # TXT Files
    if code == 'txt.read':
        try:
            cReadName = input('File Name? (no extension)  ')
            cFile = open('Extras/MyDocuments/' + (cReadName + '.txt'), "r")
            return cFile.readlines()
        except:
            cprint('Read TXT Error: {S-013x}', 'red')
    elif code == 'txt.write':
        try:
            cWriteName = input('File Name? (no extension)  ')
            cWrite = input('Write What?  ')
            cFile = open("Extras/MyDocuments/" + (cWriteName + '.txt'), "a")
            cFile.write(cWrite)
            return ('Written to ' + cWriteName + '.')
        except:
            cprint('Write TXT Error: {S-014x}', 'red')
    elif code == 'txt.write_var':
        try:
            cWriteVarName = input('File Name? (no extension)  ')
            cFile = open('Extras/MyDocuments/' + (cWriteVarName + '.txt'), 'a')
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
            cFile = open("Extras/MyDocuments/" + (cNewName + '.txt'), "w+")
            return 'File Created.'
        except:
            cprint('New TXT Error: {S-016x}', 'red')
    elif code == 'txt.delete':
        try:
            cFileRemove = input('Delete File Name? (no extension)  ')
            os.remove("Extras/MyDocuments/" + cFileRemove + ".txt")
            return 'File Deleted.'
        except:
            cprint('Delete TXT Error: {S-017x}', 'red')

def slashHandler(code):
    # Slash Commands
    if code == '/get':
        try:
            cGet = input('Get What?  ')
            if cGet == 'system_info':
                return systemInfoDisp()
            else:
                return 'Invalid /get Command'
        except:
            cprint('/get Error: {S-018}', 'red')
    elif code == '/Simpl-Py':
        try:
            cSP = input('What Simpl-Py Command?  ')
            if cSP == 'last_updated':
                return ('Simpl-Py Last Updated: ' + updated)
            elif cSP == 'version':
                return ('Simpl-Py Version: ' + version)
            elif cSP == 'docs':
                return 'Simpl-Py Docs: sites.google.com/view/simpl-py'
            elif cSP == 'web_link':
                return 'Simpl-Py Website: sites.google.com/view/simpl-py'
            elif cSP == 'change_log':
                return 'No change log currently. Wait for 1.0.0.'  # Open change log.txt when prompted
            elif cSP == 'i_care':
                return 'Thank you for caring about Simpl-Py!'
            elif cSP == 'create_date':
                return 'Simpl-Py Created: 7/12/2021'
            elif cSP == 'beta':
                cBeta = 1
                return 'Beta Mode Activated! Find the Docs to see the Current Beta Features.'
            else:
                return 'Invalid /Simpl-Py Command'
        except:
            cprint('/Simpl-Py Error: {S-019x}', 'red')
    elif code == '/stop':
        exit()

# def betaHandler(code):
    # Beta Features (activated by '/Simpl-Py' and 'beta')

def main():
    code = input('\n>>> ')

    # Base Functions
    if code == 'help':
        print('---HELP---\n')
        print('Report any bugs, flaws, or errors: github.com/Zer0-Official/Simpl-Py/issues')
        print('To discuss Simpl-Py or get help with this program: github.com/Zer0-Official/Simpl-Py/discussions')
    elif code == 'copyright':
        print('---COPYRIGHT---\n')
        with open("Extras/copyright.txt", "r") as file:
            for CopyrightContents in file:
                print(CopyrightContents)
    elif code == 'credits':
        print('---CREDITS---\n')
        with open("Extras/credits.txt", "r") as file:
            for CreditsContents in file:
                print(CreditsContents)
    else:
        out = inputHandler(code)  # Direct to sections based on contents of input
        print(out)

systemInfoDisp()
welcomeDisp()
while True:
    main()
