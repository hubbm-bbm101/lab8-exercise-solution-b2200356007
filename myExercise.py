import sys

file=open(sys.argv[1],"r")
dict={}
for line in file:
    name, info=line.split(":")
    dict[name]=info[:-1]
file.close()

for i in sys.argv[2].split(","):
    try:
        uni=dict[i]
        print("Name:",i)
        print("University:",uni)
    except:
        print("No record of '{}' was found!".format(i))