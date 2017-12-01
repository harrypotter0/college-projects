#! /usr/bin/env/ python3
# Amazon.py - Open several item searched results

import requests, bs4, webbrowser, sys

res=request.get("https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results links
soup = bs4.BeautifulSoup(res.txt, "html.parser")

# Open new tab for each results
