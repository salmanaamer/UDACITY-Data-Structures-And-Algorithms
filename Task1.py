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
mydict = dict.fromkeys(mylist)
   # print (mydict)
mylist = list(mydict.keys()) # why does this work as have keys and values, and not using dict.keys
print (mylist[0])
print (mylist[1])
print (mylist[2])
#print (texts[0]) # why does this work as texts is a local variable ? resolved


# add all of the ones in the text file as well

# by default only takes the key values when converting to list 
# use mydict.keys() or the value method
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


