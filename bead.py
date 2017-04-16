import os.path

class Ford:
    def __init__(self, szotar):
        self.data = szotar
    def fordit(self, f1, f2):
        if (not os.path.isfile(f1)):
            print "Nincs input file!"
        else:
            r = file(f1, "r")
            w = file(f2, "w")
            for line in r:
                for k in self.data:
                    line = line.replace(k, self.data[k])
                w.write(line)
    def visszafordit(self, f1, f2):
        if (not os.path.isfile(f1)):
            print "Nincs input file!"
        else:
            r = file(f1, "r")
            w = file(f2, "w")
            for line in r:
                for k in self.data:
                    line = line.replace(self.data[k], k)
                w.write(line)