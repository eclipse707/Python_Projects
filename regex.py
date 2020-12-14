import re
count=0
num=[]
name = input("Enter file:")
if len(name) < 1 : name = "sum.txt"
handle = open(name)
words=list()
#hour=list()
for line in handle :
    line=handle.read()
    y=re.findall('[0-9]+',line)
    print(len(y))

list_of_floats = []
for item in y:
    list_of_floats.append(float(item))
print(sum(list_of_floats))


#y=re.findall('[0-9]+',X)
