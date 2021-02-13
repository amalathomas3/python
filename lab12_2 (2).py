try:
    a=open("aa.txt","a")
    x=input("enter the text")
    while x:
        a.write(x+"\n")
        x=input("enter the text")
    a.close()
except IOError as io:
    print(io)
