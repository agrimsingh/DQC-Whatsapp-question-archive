# -*- coding: utf-8 -*-
import re
import time

today = time.strftime("%d/%m/%Y") #string rep of today's date
word = "#DQC"

f = open("1.txt", "r") #replace with your log
g = open("test.txt", "w") #question log generated
pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")  #check if line starts with date
templine = ''
fcount = 0

def doThingsToCompletedLine (line):
    if (word in line):
    #if (len(re.findall("(\S+)", templine)) > 15): #arbitrary limit to distinguish questions from conversations
        g.write(line)
        print line
        #fcount += 1

for line in f:
    if pattern.match(line):
        if line.count(":") == 1: #check for edge cases
            continue
        doThingsToCompletedLine(templine)

        str_split = line.split(":") #split at second colon
        templine = str_split[2] #test if line is accurate
    else:
        templine += line
doThingsToCompletedLine(templine)
print "Done"
# print fcount
print today
print type(today)
print type(pattern)

# string2 = "02/04/2016, 22:32 - ‪+91 97118 46794‬: Last name can be derived from a famously terrible food item made by stuffing meat into a sheep's stomach"
#string = "02/04/2016, 22:36 - ‪+91 97118 46794‬: Who was the oldest of Louis the Pious three children, who inherited the middle kingdom after his father's death in 843? One of France's regions is named after him."
