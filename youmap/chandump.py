import sqlite3
import json
import codecs

with open('channel.json') as f:
    vids = json.loads(f.read())
    f.close()
    print('Loaded video list from file')
    retrieved = True

fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for video in vids :
    idval = video['id']
    snippet = video['snippet']
    where = snippet['title']
    # print snippet
    try:
        rd = video['recordingDetails']
        loc = rd['location']
        lat = loc['latitude']
        lng = loc['longitude']
        if lat == 0 or lng == 0 : continue
    except:
        print('No location',idval,where)
        continue
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"','"+idval+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
fhand.close()
print(count, "records written to where.js")
print("Open index.html to view the data in a browser - you may need to clear the cache")

