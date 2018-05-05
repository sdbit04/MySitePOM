var=10

def parentM():
    global var
    print("parentM local value of var = " +  str(var))
    var = 6
    if 5 == 5:
        var=2
        print("It takes value of var from enclosed block = " + str(var))

print ("value of global var before method execution = " + str(var))
parentM()
print ("value of global var after method execution = " + str(var))

