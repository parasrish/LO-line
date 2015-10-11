# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

# method 1 : whole file read
#fcontent = fh.read()
#fcontentupper = fcontent.upper()
#print fcontentupper

# method 2 : line by line read
for fline in fh:
    trimfline = fline.rstrip()
    uppertrimfline = trimfline.upper()
    print uppertrimfline
    
