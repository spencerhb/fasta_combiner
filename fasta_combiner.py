import sys
import os

if len(sys.argv) <2:
    print("Usage: python %s requires outfile (not extension)" % sys.argv[0])
    sys.exit()


outfile= sys.argv[1]
OFH=open(outfile,"w")


for f in os.listdir("C:\Users\Godjira\Desktop\Tester"):
    if f.endswith(".faa"):
        #print(f)
        INFH = open(f)

        print >> OFH, INFH.read(), "\n ************************************************************************** \n"



print "Output file=", outfile


INFH.close()
