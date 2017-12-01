#! python3
# pw.py - An insecure password locker program

PASSWORDS ={'SBI' : 'asfjafjk',
            'BOB' : 'adfjandf',
            'SWD' : 'dghbgbgd'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named '+ account)
