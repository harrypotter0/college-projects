import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# put api key and playlist id  in config.py - see config-dist.py
import config

api_key = config.keys()['api_key']
playlistId = config.keys()['playlistId']

serviceurl = 'https://www.googleapis.com/youtube/v3/playlistItems?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
parms['part'] = 'id,snippet'
parms['maxResults'] = '50'
parms['playlistId'] = playlistId
parms['key'] = api_key

vids = list()
count = 0
nextPageToken = None
while True:
    if nextPageToken is not None: 
        parms['pageToken'] = nextPageToken

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    # print(data)
    items = js['items']
    print('Found',len(items),'videos');
    vids.extend(items)
    if 'nextPageToken' in js :
        nextPageToken = js['nextPageToken']
        x = input(nextPageToken+' Continue?')
        continue
    break

with open('channel.json', 'w') as outfile:
    json.dump(vids, outfile, indent=4)
    outfile.close()

print('Video count:',len(vids))

# https://content.googleapis.com/youtube/v3/videos?id=%207ScIlzEcKMg&part=snippet%2CrecordingDetails%2Cstatistics&key=AIzaSyAloitai2JJNpWcLpMW3Pa5aY8tM1vbdHw

parms = dict()
parms['part'] = 'id,snippet,recordingDetails,statistics'
parms['key'] = api_key

serviceurl = 'https://content.googleapis.com/youtube/v3/videos?'

newvids = list()
for video in vids: 
    try:
        idval = video['snippet']['resourceId']['videoId']
    except:
        print('Unable to find video id')
        print(video)
        quit()

    print('Idval',idval)
    if 'recordingDetails' in video : 
        print('recordingDetails already retrieved');
        newvids.append(video)
        continue

    parms['id'] = idval
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    item = js['items'][0];
    newvids.append(item)
  
with open('channel.json', 'w') as outfile:
    json.dump(newvids, outfile, indent=4)
    outfile.close()

print('')
print('Now run:')
print('python3 chandump.py')
