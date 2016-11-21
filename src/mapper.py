#/usr/bin/python -O 
import sys
sys.path.append('.')
import codecs

#open the input file
f = codecs.open("filtertext.txt", encoding='utf-8', mode='r')
#readlines from the file
lines = f.readlines()
count = 0;

#set stdout encoding to UTF
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

#iterate through the lines and emit key, value pairs
#key is the count of the outer loop and values are the tweet text to be compared
for first in range(0, len(lines)):
        count=count+1
        for second in range(count, len(lines)):
                lines[first] = lines[first].strip('\n')
                lines[second] = lines[second].strip('\n')
                print '%s\t%s\t%s' % (count,lines[first],lines[second])
f.close()




