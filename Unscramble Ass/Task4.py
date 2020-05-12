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
    mylist1 = []
    mylist2 = []
    for row in calls:
        mylist1.append(row[0])
        mylist2.append(row[1])
    # remove duplicates in list of outgoing and incoming calls and obtain 2 different lists
    mydict_outgoing = dict.fromkeys(mylist1,0)
    mydict_incoming = dict.fromkeys(mylist2,0)
    mylist_outgoing = list(mydict_outgoing)
    mylist_incoming = list(mydict_incoming)
    # check if number made call but did not receive a call and if so, delete it from outgoing call list
    for outcall in mylist_outgoing:
        if outcall in mylist_incoming:
            mylist_outgoing.remove(outcall)
    print (mylist_outgoing)

# check if the number ever made a text    
def check_text (call_list)





"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

