"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
   # print(type(reader))
    #print(next(reader))
    texts = list(reader)

    #print(texts[0])



 # reader - it made a list with each line/row being a list
 # the whole is a reader object
 # reader is an iterator and you need to index it, hence you convert it to a list
 # ['90197 24124', '99612 41256', '30-09-2016 22:51:07']  
 #  list(reader)

# reader function, reads line by line and slots them into a list

# reaches end when run    
# f is a file handler
# "with" is not a function, hence the variables stay after file is closed
#print (texts[0])
#print ("First record of texts," + " " + texts[0][0] + " " + "texts" + " " + texts[0][1] + " " + "at time" + " " + texts[0][2])

# this will not work as after the reader is run, the pointer reaches end of file
# at this point, for x in f is pointing to end of file


       
with open('calls.csv', 'r') as f: 
    reader = csv.reader(f)
    calls = list(reader)
   # print ("Last record of calls," + " " + calls[-1][0] + " " + "calls" + " " + calls[-1][1] + " " + "at time" + " " + calls[-1][2] + ", "  + "lasting " + calls[-1][3] + " seconds")



"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

