"""
Read and write a file using With As statement
This way doesnt required to close the file every operation is complete
"""

print("Write a file")
with open("secondFile", 'w') as My2ndFileW:
    My2ndFileW.write("Try to write this line and dont explicite close")

print("Read the file")
with open("secondFile", 'r') as My2ndFileR:
    print(str(My2ndFileR.read()))
