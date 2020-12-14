name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
words=list()
counts=dict()
bigvalue=0
bigkey=None
handle = open(name)
for line in handle:
    line=line.rstrip()
    if not line.startswith("From:"):
        continue
#    line=line[2:]
    line=line.split()
    words=line[1:]
#    print(words)
    for word in words:
        counts[word]=counts.get(word,0) + 1
#print("Dict looks like ",counts.items())

for key,value in counts.items() :
    if value is None or value > bigvalue:
        bigvalue=value
        bigkey=key
print(bigkey,bigvalue)
