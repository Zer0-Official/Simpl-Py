from termcolor import cprint
varName, varVal, varType = [], [], []

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
