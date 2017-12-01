#! python3
# Reads text file and ask user to insert an adjective, noun, adverb and verb
# which appeared in the text file.
# python3 mad_lib.py

import os

f = open('./desktop/a.txt','r+')
lines = f.readlines()
k=1

f.close()
f=open('./desktop/a.txt','w')

while (k==1):
    k=0
    for i in range(len(lines)):

        a, n, v, adv ='ADJECTIVE', 'NOUN' , 'VERB', 'ADVERB';
        if (a in lines[i]) == True:
            lines[i] = lines[i].replace(a,input('Enter an adjective : '),1)
            k=1
        if (n in lines[i]) == True:
            lines[i] = lines[i].replace(n,input('Enter a noun : '),1)
            k=1
        if (v in lines[i]) == True:
            lines[i] = lines[i].replace(v,input('Enter a verb : '),1)
            k=1
        if (adv in lines[i]) == True:
            lines[i] = lines[i].replace(adv,input('Enter an adverb : '),1)
            k=1


for i in range(len(lines)):
    f.write(lines[i])



f.close()
