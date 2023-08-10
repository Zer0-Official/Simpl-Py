# Simpl-Py by Zer0 2023

try:
    import wmi
    import os
    from termcolor import cprint
    from pathlib import Path
    import importlib
    import sys
    import time
    import re
except:
    exit('ROOT ERROR: IMPORTS COULD NOT BE LOADED')

version, updated = '0.8.1-beta', '8/9/2023'
var_name, var_val, var_type = [], [], []
dev_mode, beta_mode, zer0_mode = 0, False, 0

##########################
# # # # # TOKENS # # # # #
##########################

# # # BASES
t_print = 'print'
t_var = 'var'
t_txt = 'txt'
t_mod = '@'
t_slash = '/'
t_dial = '#'

# # # OPERATORS
t_dot = '.'
t_under = '_'

# # # SUBS
st_echo = 'echo'
st_math = 'math'
st_correct = 'correct'
st_lower = 'lower'
st_upper = 'upper'
st_reverse = 'reverse'
st_read = 'read'
st_write = 'write'
st_writevar = 'write-var'
st_new = 'new'
st_delete = 'delete'
st_var = 'var'

# # # SLASH SUBS
st_systeminfo = 'system-info'
st_lastupdated = 'last-updated'
st_version = 'version'
st_docs = 'docs'
st_icare = 'i-care'
st_createdate = 'create-date'
st_stop = 'stop'

# # # DIAL SUBS
st_dev = '779'  # 4
st_emer_stop = '7867'
st_reset = '73738'
st_clear = '25327'
st_beta = '2382'
st_zer0 = '0'


def tokenizer(cmd):
    tokens = []
    if t_dot in cmd and t_under not in cmd:  # GooglyTank was here
        tokens = re.split(r'(\.)', cmd)
        cmd_type = 'dot'
    elif t_under in cmd and t_dot not in cmd:
        tokens = re.split(r'(_)', cmd)
        cmd_type = 'under'
    elif t_under in cmd and t_dot in cmd:
        tokens = re.split(r'(_)|(.)', cmd)
        cmd_type = 'double'
    else:
        tokens.append(cmd)
        cmd_type = 'base'
    while '' in tokens:
        tokens.remove('')

    return tokens, cmd_type


def find_handler(cmd):
    tokens, cmd_type = tokenizer(cmd)
    test_token = tokens[0]

    if test_token == t_print:
        print_handler(tokens, cmd_type)
    elif test_token == t_var:
        var_handler(tokens, cmd_type)
    elif test_token == t_txt:
        txt_handler(tokens, cmd_type)
    elif t_mod in test_token:
        mod_handler(tokens, cmd_type)
    elif t_slash in test_token:
        slash_handler(tokens, cmd_type)
    elif t_dial in test_token:
        call_handler(tokens, cmd_type)
    elif test_token == t_dot:
        error('001x', tokens, cmd_type)
    elif test_token == t_under:
        error('002x', tokens, cmd_type)


##########################
# # # # # ERRORS # # # # #
##########################

docs = 'See the Simpl-Py docs for information on this error.'

errors = [
    # code |   name                 | details                            | debug
    ['001x', 'Dot Operator Error', 'Started command with . (dot) operator.', 'Use . operator between two tokens.'],
    ['002x', 'Underscore Operator Error', 'Started command with _ (underscore) operator.', 'Use _ operator between '
                                                                                           'two tokens.'],
    ['003x', 'System Info Display Error', 'Could not display system info correctly.', 'Report this error. (internal)'],
    ['004x', 'Welcome Display Error', 'Could not display welcome info correctly.', 'Report this error. (internal)'],
    ['005x', 'Module DNE Error', 'Module does not exist.', 'Likely spelled wrong or in wrong directory.'],
    ['006x', 'Module Import/Function Error', 'Module found, but could not be imported or function could not be '
                                             'accessed.', 'Check your spelling or read docs for imported module.'],
    ['007x', 'Module Handler Error', 'Command could not be found within the module handler.', docs],
    ['008x', 'print Base Error', 'Base print function failed.', 'Likely inserted special character.'],
    ['009x', 'print.echo Error', 'print.echo function failed.', 'Likely inserted string when integer was expected.'],
    ['010x', 'print_math Error', 'print_math function failed.', 'Likely inserted string when integer was expected.'],
    ['011x', 'print.correct Error', 'print.correct function failed.', docs],
    ['012x', 'print.lower Error', 'print.lower function failed.', docs],
    ['013x', 'print.upper Error', 'print.upper function failed.', docs],
    ['014x', 'print.reverse Error', 'print.reverse function failed.', docs],
    ['015x', 'print_var Error', 'print_var function failed.', docs],
    ['016x', 'Print Handler Error', 'Command could not be found within the print handler.', docs],
    ['017x', 'Slash Handler Error', 'Command could not be found within the slash handler.', docs],
    ['018x', 'txt.read Error', '.txt file could not be read.', 'Check your spelling or file may not exist.'],
    ['019x', 'txt.write Error', 'Contents could not be written to the .txt file.', docs],
    ['020x', 'txt.write-var Error', 'Variable could not be written to the .txt file.', docs],
    ['021x', 'txt.new Error', 'New .txt file could not be created.', docs],
    ['022x', 'txt.delete Error', '.txt file could not be deleted.', 'Check your spelling or the file may not exist.'],
    ['023x', 'TXT Handler Error', 'Command could not be found within the txt handler.', docs],
    ['024x', 'var.new Error', 'New variable could not be created.', docs],
    ['025x', 'Var Handler Error', 'Command could not be found within the var handler.', docs],
    ['026x', 'Call Handler Error', 'Number dialed could not be found within the call handler.', docs]
]


def error(code, tokens, cmd_type):
    error_subject = None
    for i in range(len(errors)):
        if errors[i][0] == code:
            error_subject = errors[i]
            break
    if error_subject is None:
        print('Internal Error Error :(   Report this bug!')
    else:
        error_subject_test = errors.index(error_subject)
        e_code = errors[error_subject_test][0]
        e_name = errors[error_subject_test][1]
        e_desc = errors[error_subject_test][2]
        e_dbg = errors[error_subject_test][3]

        cprint('{S-' + e_code + '}  -  ' + e_name, 'red')
        cprint(e_desc, 'red')

        if dev_mode:
            cprint('Info: ' + e_dbg, 'yellow')
            cprint("Tokens: '" + ("', '".join(tokens)) + "'", 'yellow')
            cprint('Type: ' + cmd_type, 'yellow')


############################
# # # # # START-UP # # # # #
############################

def system_info_disp():
    try:
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]
        print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system.Model} - {my_system.SystemType}")
    except:
        error('003x', None, None)
        exit()


def welcome_disp():
    try:
        print('~' * 80)
        print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
        print('Type "help", "copyright", or "credits" for more information.')
    except:
        error('004x', None, None)


############################
# # # # # HANDLERS # # # # #
############################


def mod_handler(temp, cmd_type):
    tt = t_mod
    tkns = re.split(r'(@)', temp[0])
    while '' in tkns:
        tkns.remove('')
    if tkns == [tt]:
        print('- - - Module Settings - - -')
        print('- [A]dd auto-import')
        print('- [C]lear auto-imports')
        print('- [E]xit')
        setting = (input('\n Type a letter:  ')).lower()
        if setting == 'a':
            # add = input('Module Name:  ')
            cprint('Sorry, module auto-imports are not available right now.', 'yellow')           # add this
            cprint('Do not report this bug.', 'grey')
        elif setting == 'c':
            cprint('Sorry, module auto-imports are not available right now.', 'yellow')           # add this
            cprint('Do not report this bug.', 'grey')
    elif tt in tkns:
        try:
            mod_name = ('SPY_' + tkns[1])
            sys.path.append('src/mod')
            imp_mod = __import__(mod_name)
            modin = input('What Function?  ')
            func = getattr(imp_mod, 'init')
            out = func(modin)
            print(out)
        except ModuleNotFoundError:
            error('005x', tkns, cmd_type)
        except:
            error('006x', tkns, cmd_type)
    else:
        error('007x', tkns, cmd_type)                                                    # doesn't go here


def print_handler(tkns, cmd_type):
    tt = t_print
    if tkns == [tt]:
        try:
            print_in = input('Print What?  ')
            print(print_in)
        except:
            error('008x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_echo]:
        try:
            echo_in = input('Echo What?  ')
            echo_space = int(input('Echo Space?  '))
            echo_in += (' ' * echo_space)
            echo_amount = int(input('Echo Amount?  '))
            echo_out = echo_in * echo_amount
            print(echo_out)
        except:
            error('009x', tkns, cmd_type)
    elif tkns == [tt, t_under, st_math]:
        try:
            math_ints = []
            math_int_count = int(input('Number of Integers: '))
            for i in range(math_int_count):
                math_ints.append(int(input('Integer:  ')))
            math_op = input('Operator (+, -, *, /):  ')
            if math_op == '+':
                print(sum(math_ints))
            elif math_op == '-':
                math_sub = math_ints[0]
                for i in range(1, len(math_ints)):
                    math_sub -= math_ints[i]
                print(math_sub)
            elif math_op == '*':
                math_mult = math_ints[0]
                for i in range(1, len(math_ints)):
                    math_mult *= math_ints[i]
                print(math_mult)
            elif math_op == '/':
                math_div = math_ints[0]
                for i in range(1, len(math_ints)):
                    math_div /= math_ints[i]
                print(math_div)
            else:
                print('Invalid operator.')
        except:
            error('010x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_correct]:
        try:
            correct = input('Correct What?  ')
            print(correct.capitalize())
        except:
            error('011x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_lower]:
        try:
            c_lower = input('Lower What?  ')
            print(c_lower.lower())
        except:
            error('012x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_upper]:
        try:
            c_upper = input('Upper What?  ')
            print(c_upper.upper())
        except:
            error('013x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_reverse]:
        try:
            c_backwards = input('Reverse What?  ')
            print(c_backwards[::-1])
        except:
            error('014x', tkns, cmd_type)
    elif tkns == [tt, t_under, st_var]:
        try:
            print_var = input('What Variable?  ')
            if print_var in var_name:
                var_find_idx = var_name.index(str(print_var))
                print(var_val[var_find_idx])
            else:
                print('Variable not found.')
        except:
            error('015x', tkns, cmd_type)
    else:
        error('016x', tkns, cmd_type)


def slash_handler(temp, cmd_type):
    tt = t_slash
    tkns = re.split(r'(/)', temp[0])
    tkns.remove('')
    if tkns == [tt, st_systeminfo]:
        system_info_disp()
    elif tkns == [tt, st_lastupdated]:
        print('Simpl-Py Last Updated: ' + updated)
    elif tkns == [tt, st_version]:
        print('Simpl-Py Version: ' + version)
    elif tkns == [tt, st_docs]:
        print('Simpl-Py Docs: sites.google.com/view/simpl-py')
    elif tkns == [tt, st_icare]:
        print('Thank you for caring about Simpl-Py!')
    elif tkns == [tt, st_createdate]:
        print('Simpl-Py Created: 7/12/2021')
    elif tkns == [tt, st_stop]:
        cprint('Report any bugs on the official GitHub repo.', 'grey')
        print('Thanks for using Simpl-Py!')
        exit()
    else:
        error('017x', tkns, cmd_type)


def txt_handler(tkns, cmd_type):
    tt = t_txt
    fldr = './src/MyDocuments/'

    if tkns == [tt, t_dot, st_read]:
        try:
            read_name = input('File Name? (no extension)  ')
            file_open = open(fldr + (read_name + '.txt'), "r")
            print(file_open.readlines())
        except:
            error('018x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_write]:
        try:
            write_name = input('File Name? (no extension)  ')
            write = input('Write What?  ')
            file_open = open(fldr + (write_name + '.txt'), "a")
            file_open.write(write)
            print('Written to ' + write_name + '.')
        except:
            error('019x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_writevar]:
        try:
            write_var_name = input('File Name? (no extension)  ')
            file_open = open(fldr + (write_var_name + '.txt'), 'a')
            write_var = input('Variable to Write?  ')
            if write_var in var_name:
                write_var_idx = var_name.index(write_var)
                write_var_val = var_val[write_var_idx]
                file_open.write(write_var_val)
                print('Variable ' + write_var + ' written to ' + write_var_name + '.')
            else:
                print('Variable not found.')
        except:
            error('020x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_new]:
        try:
            new_name = input('New File Name? (no extension)  ')
            open(fldr + (new_name + '.txt'), "w+")
            print('File Created.')
        except:
            error('021x', tkns, cmd_type)
    elif tkns == [tt, t_dot, st_delete]:
        try:
            file_remove = input('Delete File Name? (no extension)  ')
            os.remove(fldr + file_remove + ".txt")
            print('File Deleted.')
        except:
            error('022x', tkns, cmd_type)
    else:
        error('023x', tkns, cmd_type)


def var_handler(tkns, cmd_type):
    tt = t_var
    if tkns == [tt, t_dot, st_new]:
        try:
            new_var_name = input('New Var Name:  ')
            var_name.append(new_var_name)
            new_var_val = input('Enter Value:  ')
            var_val.append(new_var_val)
            try:
                int_store = int(new_var_val)
                var_type.append(type(int_store))
            except:
                var_type.append(type(new_var_val))
            print('Created ' + new_var_name + ' with value ' + new_var_val)
        except:
            error('024x', tkns, cmd_type)
    else:
        error('025x', tkns, cmd_type)


def call_handler(temp, cmd_type):
    global dev_mode, beta_mode, zer0_mode
    tt = t_dial
    tkns = re.split(r'(#)', temp[0])
    tkns.remove('')
    if tkns == [tt, st_dev]:
        if dev_mode is True:
            print('SPY DEV mode already activated.')
            deactivate = input('Would you like to disable it? (y, n)  ')
            if deactivate == 'y' or deactivate == 'Y':
                dev_mode = 0
                print('SPY DEV mode deactivated.')
        elif dev_mode == 2:
            dev_mode = True
            cprint('Simpl-Py Developer Mode Activated!', 'green')
            cprint('Read the docs for more info.', 'grey')
        else:
            dev_mode += 1
            cprint('You are ' + str(3 - dev_mode) + ' step(s) away from entering SPY DEV mode.', 'grey')
    elif tkns == [tt, st_emer_stop]:
        exit('SPY - Emergency Stop Process Complete.')
    elif tkns == [tt, st_reset]:
        global var_name, var_val, var_type
        var_name, var_val, var_type = [], [], []
        dbg, dev_mode, beta_mode, zer0_mode = False, 0, False, 0
        cprint('Data Reset.', 'grey')
    elif tkns == [tt, st_clear]:
        os.system('cls')
        system_info_disp()
        welcome_disp()
    elif tkns == [tt, st_beta]:
        if beta_mode is True:
            print('SPY BETA mode already activated.')
            deactivate = input('Would you like to disable it? (y, n)  ')
            if deactivate == 'y' or deactivate == 'Y':
                beta_mode = 0
                print('SPY BETA mode deactivated.')
        else:
            beta_mode = True
            cprint('Simpl-Py Beta Mode Activated!', 'green')
            cprint('See docs for more info.', 'grey')
    elif tkns == [tt, st_zer0]:
        if zer0_mode is True:
            print('Zer0 M0de already activated.')
            deactivate = input('Would you like to disable it? (y, n)  ')
            if deactivate == 'y' or deactivate == 'Y':
                zer0_mode = 0
                print('Zer0 M0de deactivated.')
        elif zer0_mode < 23:
            cprint('...', 'grey')
            zer0_mode += 1
        else:
            zer0_mode = True
            cprint('Zer0 M0de Activated!', 'green')
    else:
        error('026x', tkns, cmd_type)


def main():
    while True:
        cmd_in = input('\n>>> ')

        if cmd_in == '':
            pass
        elif cmd_in == 'help':
            print('- - - HELP - - -\n')
            print('Report any bugs, flaws, or errors: github.com/Zer0-Official/Simpl-Py/issues')
            print('To get help with this language, read the README or the docs.')
        elif cmd_in == 'copyright':
            print('- - - COPYRIGHT - - -\n')
            with open("src/BaseFunc/copyright.txt", "r") as file:
                for copyright_contents in file:
                    print(copyright_contents)
        elif cmd_in == 'credits':
            print('- - - CREDITS - - -\n')
            with open("src/BaseFunc/credits.txt", "r") as file:
                for credits_content in file:
                    print(credits_content)
        else:
            find_handler(cmd_in)


if __name__ == '__main__':
    system_info_disp()
    welcome_disp()
    main()
