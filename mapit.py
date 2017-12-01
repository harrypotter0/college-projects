#!/usr/bin/env python3
# mapit.py - launches google map in browser using an address from the
# command line or clipboard.

import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# Get address from clipboard.

else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
