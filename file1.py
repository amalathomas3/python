try:
    word=input("Enter the word");
    inf=open("a1.txt")
    lines=inf.readlines()
    inf.close()
    outf=open("output.txt","w")
    for line in lines:
        if word not in line.strip("\n"):
            outf.write(line)

    outf.close()
except IOError as io:
    print(io)
    
