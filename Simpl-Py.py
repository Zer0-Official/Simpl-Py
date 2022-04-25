# Variables + Imports
try:
    import wmi
    import os
    from termcolor import colored
    version, updated = '0.4.0', '4/22/2022'
    varName, varVal, varType = [], [], []
    cMathInts, cMathSub, cMathMult, cMathDiv = [], 0, 0, 0
except:
    print('ROOT ERROR: VARIABLES/IMPORTS COULD NOT BE LOADED')

# Functions
def systemInfoDisp():
    try:
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]
        print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")
    except:
        print(colored('System Info Error: {S-001x}', 'red'))
        exit()

def welcomeDisp():
    try:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
        print('Type "help", "copyright", or "credits" for more information.')
    except:
        print(colored('Welcome Display Error: {S-002x}', 'red'))

def inputHandler(code):
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
    # Print Functions
    if code == 'print':
        try:
            cPrint = input('Print What?  ')
            return cPrint
        except:
            print(colored('Print Error: {S-004x}', 'red'))
    elif code == 'print.echo':
        try:
            cEcho = input('Echo What?  ')
            cEchoSpace = int(input('Echo Space?  '))
            cEcho = cEcho + (' ' * cEchoSpace)
            cEchoAmount = int(input('Echo Amount?  '))
            cEchoOut = cEcho * cEchoAmount
            return cEchoOut
        except:
            print(colored('Print Echo Error: {S-005x}', 'red'))
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
            print(colored('Print Math Error: {S-006x}', 'red'))
    elif code == 'print.correct':
        try:
            cCorrect = input('Correct What?  ')
            return cCorrect.capitalize()
        except:
            print(colored('Print Correct Error: {S-007x}', 'red'))
    elif code == 'print.lower':
        try:
            cLower = input('Lower What?  ')
            return cLower.lower()
        except:
            print(colored('Print Lower Error: {S-008x}', 'red'))
    elif code == 'print.upper':
        try:
            cUpper = input('Upper What?  ')
            return cUpper.upper()
        except:
            print(colored('Print Upper Error: {S-009x}', 'red'))
    elif code == 'print.backwards':
        try:
            cBackwards = input('Backwards What?  ')
            return (cBackwards [::-1])
        except:
            print(colored('Print Backwards Error: {S-010x}', 'red'))

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
            print(colored('New Var Error: {S-011x}', 'red'))

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
            print(colored('Print Var Error: {S-012x}', 'red'))

def txtHandler(code):
    # TXT Files
    if code == 'txt.read':
        try:
            cReadName = input('File Name? (no extension)  ')
            cFile = open('Extras/MyDocuments/' + (cReadName + '.txt'), "r")
            return cFile.readlines()
        except:
            print(colored('Read TXT Error: {S-013x}', 'red'))
    elif code == 'txt.write':
        try:
            cWriteName = input('File Name? (no extension)  ')
            cWrite = input('Write What?  ')
            cFile = open("Extras/MyDocuments/" + (cWriteName + '.txt'), "a")
            cFile.write(cWrite)
            return ('Written to ' + cWriteName + '.')
        except:
            print(colored('Write TXT Error: {S-014x}', 'red'))
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
            print(colored('Write Var TXT Error: {S-015x}', 'red'))
    elif code == 'txt.new':
        try:
            cNewName = input('New File Name? (no extension)  ')
            cFile = open("Extras/MyDocuments/" + (cNewName + '.txt'), "w+")
            return 'File Created.'
        except:
            print(colored('New TXT Error: {S-016x}', 'red'))
    elif code == 'txt.delete':
        try:
            cFileRemove = input('Delete File Name? (no extension)  ')
            os.remove("Extras/MyDocuments/" + cFileRemove + ".txt")
            return 'File Deleted.'
        except:
            print(colored('Delete TXT Error: {S-017x}', 'red'))

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
            print(colored('/get Error: {S-018}', 'red'))
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
            else:
                return 'Invalid /Simpl-Py Command'
        except:
            print(colored('/Simpl-Py Error: {S-019x}', 'red'))
    elif code == '/stop':
        exit()

# def otherHandler(code):
    # Miscellaneous Functions
    # blank

def main():
    try:
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
    except:
        print(colored('Main Error: {S-020x}', 'red'))

systemInfoDisp()
welcomeDisp()
while True:
    main()
