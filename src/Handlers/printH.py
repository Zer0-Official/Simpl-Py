from termcolor import cprint
cMathInts, cMathSub, cMathMult, cMathDiv = [], 0, 0, 0

def printHandler(code): ### PUT BETA ON ECHO PRINT
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