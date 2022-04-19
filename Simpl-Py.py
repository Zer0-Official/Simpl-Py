# Variables + Imports
import wmi
version = '0.3.0'
updated = '3/28/2022'
var1 = 0
var2 = 0
var3 = 0

# Functions
def systemInfoDisp():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")

def welcomeDisp():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
    print('Type "help", "copyright", or "credits" for more information.')

def inputHandler(code):
    pH = printHandler(code)
    if pH != None:
        return pH
    else:
        vH = varHandler(code)
        if vH != None:
            return vH
        else:
            txtH = txtHandler(code)
            if txtH != None:
                return txtH
            else:
                slashH = slashHandler(code)
                if slashH != None:
                    return slashH
                else:
                    return ''


def printHandler(code):
    # Print Functions
    if code == 'print':
        cPrint = input('Print What?  ')
        return cPrint
    elif code == 'echo.print':
        cEcho = input('Echo What?  ')
        cEchoSpace = int(input('Echo Space?  '))
        cEcho = cEcho + (' ' * cEchoSpace)
        cEchoAmount = int(input('Echo Amount?  '))
        cEchoOut = cEcho * cEchoAmount
        return cEchoOut
    elif code == 'print_math':
        cMathInt1 = int(input('First Integer:  '))
        cMathOp = input('Operator (+, -, *, /):  ')
        cMathInt2 = int(input('Second Integer:  '))
        if cMathOp == '+':
            print('{} + {} = '.format(cMathInt1, cMathInt2))
            return (cMathInt1 + cMathInt2)
        elif cMathOp == '-':
            print('{} - {} = '.format(cMathInt1, cMathInt2))
            return (cMathInt1 - cMathInt2)
        elif cMathOp == '*':
            print('{} * {} = '.format(cMathInt1, cMathInt2))
            return (cMathInt1 * cMathInt2)
        elif cMathOp == '/':
            print('{} / {} = '.format(cMathInt1, cMathInt2))
            return (cMathInt1 / cMathInt2)
        else:
            return 'Invalid operator.'
    elif code == 'correct.print':
        cCorrect = input('Correct What?  ')
        return cCorrect.capitalize()
    elif code == 'lower.print':
        cLower = input('Lower What?  ')
        return cLower.lower()
    elif code == 'upper.print':
        cUpper = input('Upper What?  ')
        return cUpper.upper()
    elif code == 'backwards.print':
        cBackwards = input('Backwards What?  ')
        return (cBackwards [::-1])

def varHandler(code):
    # Variables
    global var1,var2,var3
    if code == 'var1':
        var1 = input('Set var1:  ')
        return ('Set var1 to ' + var1)
    elif code == 'var2':
        var2 = input('Set var2:  ')
        return ('Set var2 to ' + var2)
    elif code == 'var3':
        var3 = input('Set var3:  ')
        return ('Set var3 to ' + var3)

    elif code == 'print_var':
        cPrintVar = input('What Variable?  ')
        if cPrintVar == 'var1':
            return var1
        elif cPrintVar == 'var2':
            return var2
        elif cPrintVar == 'var3':
            return var3
        else:
            return 'Variable not found.'

def txtHandler(code):
    # TXT Files
    if code == 'txt.read':
        cReadName = input('Name? (no extension)  ')
        cFile = open('Extras/MyDocuments/' + (cReadName + '.txt'), "r")
        return cFile.readlines()
    elif code == 'txt.write':
        cWriteName = input('Name? (no extension)  ')
        cWrite = input('Write What?  ')
        cFile = open("Extras/MyDocuments/" + (cWriteName + '.txt'), "a")
        cFile.write(cWrite)
        return ('Written to ' + cWriteName)
    elif code == 'txt.new':
        cNewName = input('New File Name? (no extension)  ')
        cFile = open("Extras/MyDocuments/" + (cNewName + '.txt'), "w+")
        return 'File Created.'

def slashHandler(code):
    # Slash Commands
    if code == '/get':
        cGet = input('Get What?  ')
        if cGet == 'system_info':
            return systemInfoDisp()
        else:
            return 'Invalid /get Command'
    elif code == '/Simpl-Py':
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
    elif code == '/stop':
        exit()

#def otherHandler(code):
    # Miscellaneous Functions
    # blank

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