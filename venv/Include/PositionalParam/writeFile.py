
# list of built Ins function:
# https://docs.python.org/3/library/functions.html
myList=[1,2,3,4]

myFile=open("firstFile", 'w')
for item in myList:
    # write function only work on string, so cust to string is required
    myFile.write(str(item) + "\n")
# This close action need to be perform to clear the buffer
myFile.close()
