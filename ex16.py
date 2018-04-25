#coding = utf-8
from sys import argv

script,filename = argv

prompt = ">>>"
#erase 抹去
print("We're going to erase %r."%filename)
print("If you don't want that,hit Ctrl C.\nIf you do want that,hit ENTER. ")
#print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")

target = open(filename,'w')
print("Truncating the file. Goodbye!")
target.truncate()

#print("Now I'm going to ask you for three lines.")

line1 = input("Now I'm going to ask you for three lines.\nline1:")
line2 = input("line2:")
line3 = input("line3:")

#print("I'm going to write these to the file.")

target.write("I'm going to write these to the file.\n%r\n%s\n%s\n"%(line1,line2,line3))
'''
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
print("And finally,we close it.")
target.close()

print ("Now let's read the new file:")
F=open(filename,'r')
print(prompt,end = '')
print(F.read())