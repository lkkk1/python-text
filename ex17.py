#coding = utf-8
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s"%(from_file,to_file))

#we could do this two or one line too,how?
#In = open (from_file)
#indata = In.read()
#indata = open(from_file).read()

'''
print("The input file is %d bytes long"%len(indata))
print("Does the output file exist? %r"%exists(to_file))
print("Ready,hit RETURN to continue,CTRL-C to abort")
input()

output = open (to_file,'w')
output.write(indata)
'''

open(to_file,'w').truncate()
open(to_file,'w').write(open(from_file).read())
print("Alright,all done")

open(to_file).close()
open(from_file).close()