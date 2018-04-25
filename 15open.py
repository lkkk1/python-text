#'r'读模式   'w'写模式  'a'追加模式  'b'二进制模式   '+'读写模式
filename = input("Type the filename:\n >>>")
X=open(filename)
print(X.read())
X.close()
#不在同一文件夹文件的读取
print("Type the file >>>")
Y = open(r'f:\Python text3\ex15b.txt')
print(Y.read())
Y.close()