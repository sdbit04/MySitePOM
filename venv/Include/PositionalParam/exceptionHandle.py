def handleException():
    try:
        a=30
        b=20
        c=0
        d=(a+b)/c
        print (d)
    except:
        print("this will be printed while Excepion occure")
        raise Exception 
    else:
        print("this will be printed while no excepion")
    finally:
        print("this will Always be printed, this finally block is used to close network connection, database conneciton to avoid memory leakage")



handleException()