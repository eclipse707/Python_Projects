fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
count=0
fh = open(fname)
for line in fh :
    line=line.rstrip()
    if line.startswith("From:"):
        count = count + 1
        line.split()
        print(line[6:])

print("There were", count, "lines in the file with From as the first word")
