"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


def maxvalue (dict):
    current_tele = 0
    current_max = 0
    for x in dict:
        if dict[x] > current_max:
            current_max = dict[x]
            current_tele = x
    current_max = str(current_max)
    print (current_tele + " spent the longest time, " + current_max + " seconds, on the phone during September 2016.")
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
mylist = []
for row in calls:
    mylist.append(row[0])
    mylist.append(row[1])
mydict = dict.fromkeys(mylist,0)
for row in calls:
    mydict[row[0]] = int(mydict[row[0]]) + int(row[3]) 
    mydict[row[1]] = int(mydict[row[1]]) + int(row[3])
maxvalue(mydict)
    

#sorted function, 
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.

 if mydict[row[0]] == None:
                mydict[row[0]] = 0
if mydict[row[1]] == None:
                mydict[row[1]] = 0


Answering the phone ???


Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

