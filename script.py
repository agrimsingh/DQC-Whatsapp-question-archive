# -*- coding: utf-8 -*-
import re
f = open("1.txt", "r")
g = open("questions.txt", "w")
pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")  #check if line starts with date
templine = ''
count = 0
for line in f:
    if pattern.match(line):
        if line.count(":") == 1: #check for edge cases
            continue
        print templine
        if (len(re.findall("(\S+)", templine)) > 15): #arbitrary limit to distinguish questions from conversations
            g.write(templine)
            count += 1
        str_split = line.split(":") #split at second colon

        templine = str_split[2] #test if line is accurate
    else:
        templine += line

print "Done"
print count

# string2 = "02/04/2016, 22:32 - ‪+91 97118 46794‬: Last name can be derived from a famously terrible food item made by stuffing meat into a sheep's stomach"
#string = "02/04/2016, 22:36 - ‪+91 97118 46794‬: Who was the oldest of Louis the Pious three children, who inherited the middle kingdom after his father's death in 843? One of France's regions is named after him."
