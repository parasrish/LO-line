# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

mail_dict = dict()
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail=''
for line in handle:
    if line.startswith('From '):
        words = line.split()
        #print words
    else:
        continue
    mail = words[1]
    mail_dict[mail] = mail_dict.get(mail,0)+1

#through dict now, biggest
mail_count = mail_dict.values()
mail_count.sort()
max_count = mail_count[len(mail_count)-1]
for key,val in mail_dict.items():
    if val == max_count:
        print key, val
#print 'max wrd'
#print 'max count', mail_count[len(mail_count)-1]
