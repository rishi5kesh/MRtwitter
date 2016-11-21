#/usr/bin/python -O 
import sys
sys.path.append('.')
import io
import codecs
import re
import difflib

#use difference library (difflib) to compare two tweets

current_word = None
current_count = 0
word1 = None
word2 = None
count = 0

#set stdin encoding to utf8
UTF8Reader = codecs.getreader('utf8')
sys.stdin = UTF8Reader(sys.stdin)

#set stdout encoding to utf8
UTF8Writer2 = codecs.getwriter('utf8')
sys.stdout = UTF8Writer2(sys.stdout)


# input comes from STDIN from the mapper
for line in sys.stdin:
   
    if '\t' in line:
        
        word1 = re.split(r'\t+',line)
       
    #compare the tweets for 90% match
    if difflib.SequenceMatcher(None,word1[1],word1[2]).ratio() >= .9:
        print 'Good--Match--\n'
        print 'First => %s \n Second => %s' % (word1[1],word1[2])
    