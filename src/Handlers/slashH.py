from termcolor import cprint

def slashHandler(code):
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