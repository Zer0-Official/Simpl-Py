# Variables + Imports
# ------------------------------
# CHANGE THE DATE AND VERSION!!!
# ------------------------------

try:
    import wmi, os
    from termcolor import cprint
    from pathlib import Path
    import importlib
    import sys, time
    import src.Handlers
    version, updated = '0.8.0-beta', '12/14/2022'
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

def moduleHandler(code):   # do not change for testing purposes
    if '@' in code:
        cStart = time.time()
        modN = ('SPY_' + code.replace('@', ''))
        sys.path.append('mod')
        cImp = __import__(modN)
        #modin = input('What Function?  ')
        modin = 'inside'
        func = getattr(cImp, 'init')
        out = func(modin)
        cEnd = time.time()
        cTotal = cEnd - cStart
        cMS = cTotal * 1000
        print(out)
        return ('Clock Time:  ' + str(cMS) + 'ms')

def inputHandler(code):
    if '@' in code:
        modH = moduleHandler(code)
        return modH
    else:
        pH = printH.printHandler(code)
        if pH != None: return pH
        else:
            vH = varH.varHandler(code)
            if vH != None: return vH
            else:
                tH = txtH.txtHandler(code)
                if tH != None: return tH
                else:
                    sH = slashH.slashHandler(code)
                    if sH != None: return sH
                    else: return ''

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
        with open("src/BaseFunc/copyright.txt", "r") as file:
            for CopyrightContents in file:
                print(CopyrightContents)
    elif code == 'credits':
        print('---CREDITS---\n')
        with open("src/BaseFunc/credits.txt", "r") as file:
            for CreditsContents in file:
                print(CreditsContents)
    else:
        out = inputHandler(code)  # Direct to sections based on contents of input
        print(out)

systemInfoDisp()
welcomeDisp()
while True:
    main()
