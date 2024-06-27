class VM:
    def __init__(self,file):
        initseg = initfile.readline()
        initpage = initfile.readline()
        seg = initseg.split(" ")
        page = initpage.split(" ")
        self.pm = []
        x=0
        while(x<524288):
            self.pm.append(0)
            x+=1
        i = 0
        while i != (len(seg)):
            si = int(seg[i])
            zi = int(seg[i+1])
            fi = int(seg[i+2])
            i=i+3
            self.pm[2*si] = zi
            self.pm[2*si+1] = fi
        i = 0
        while i !=(len(page)):
            si = int(page[i])
            pi = int(page[i+1])
            fi = int(page[i+2])
            i= i+3
            self.pm[self.pm[2*si+1]*512+pi] = fi

    def VAtoPA(self,VA):
        VAline = VA.readline()
        Vasplit = VAline.split(" ")
        PAcomplete = ""
        for i in Vasplit:
            Vaint = int(i)
            s = Vaint >> 18
            w = Vaint & 0x1FF
            p = (Vaint>>9) & 0x1FF
            pw = Vaint & 0x3FFFF
            
            if(pw>=self.pm[2*s]):
                PAcomplete = PAcomplete+"-1 "
            elif(self.pm[(2*s)+1]==0):
                PAcomplete = PAcomplete+"-1 "
            elif(self.pm[(self.pm[(2*s)+1]*512)+p]==0):
                PAcomplete = PAcomplete+"-1 "
            else:
                PAcomplete = PAcomplete+str((self.pm[(self.pm[(2*s)+1]*512)+p]*512)+w)+ " "
        return(PAcomplete)


initfile = open("init-no-dp.txt", "r")
test = VM(initfile)
infile = open("input-no-dp.txt", "r")
out_file = open("output-no-dp.txt","w")
out_file.write(test.VAtoPA(infile))

initfile.close()
infile.close()
out_file.close()
