try:
    inf=open("a2.txt")
    lines=inf.readlines()
    inf.close()
    outf=open("aa2.txt","w")
    for i in lines:
        if not(i.startswith("#")):
            outf.write(i)

    outf.close()
except IOError as io:
    print(io)
