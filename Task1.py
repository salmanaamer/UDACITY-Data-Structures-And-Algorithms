"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    mylist = []
    for row in calls:
        mylist.append(row[0])
        mylist.append(row[1])
    counter = 0
    mydict = dict.fromkeys(mylist,0)
    mylist = list(mydict) # why does this work as have keys and values, and not using dict.keys

print (texts[0]) # why does this work as texts is a local variable ?



