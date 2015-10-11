# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
word_dict = dict()
handle = open(name)
for line in handle:
    if line.startswith('From '):
        words = line.split()
        #print words
        subwords = words[5].split(':')
        #print subwords
        hr = subwords[0]
        word_dict[hr] = word_dict.get(hr, 0) + 1;
#print word_dict
#sort now
lst = word_dict.items()
lst.sort()
#print lst
for tup in lst:
    (k,v) = tup
    print k,v

