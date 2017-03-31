class Theorem201(Theorem):
    def __init__(self):
        super(Theorem201, self).__init__(201, "if nodes >= 6.0 and connected and nodes >= 3.0*edgeInd-(1.0) then \n{\n    nodeCover <= 2.0*edgeInd-(mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","connected","edgeInd","nodeCover","mindeg"]
    def run(self):
        if minb("nodes") >= 6.0 and get("connected") == True  and minb("nodes") >= 3.0*maxb("edgeInd")-(1.0):
            try:
                set("nodeCover",  2.0*maxb("edgeInd")-(minb("mindeg")), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("mindeg")/2.0+minb("nodeCover")/2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0*maxb("edgeInd")-(minb("nodeCover")), ind='Max')
            except:
                pass
        
        return

class Theorem202(Theorem):
    def __init__(self):
        super(Theorem202, self).__init__(202, "if regular then \n{\n    nodeCover >= nodes/2.0+(maxClique-(1.0))*(maxClique-(2.0))/(2.0*mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeCover","nodes","maxClique","mindeg"]
    def run(self):
        if get("regular") == True :
            try:
                set("nodeCover",  minb("nodes")/2.0+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/(2.0*maxb("mindeg")), ind='Min')
            except:
                pass
            try:
                set("nodes",  (-(minb("maxClique")**2.0)+3.0*minb("maxClique")+2.0*maxb("mindeg")*maxb("nodeCover")-(2.0))/maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("maxClique",  sqrt(8.0*maxb("mindeg")*maxb("nodeCover")-(4.0*maxb("mindeg")*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  (minb("maxClique")**2.0-(3.0*minb("maxClique"))+2.0)/(2.0*maxb("nodeCover")-(minb("nodes"))), ind='Min')
            except:
                pass
        
        return

class Theorem203(Theorem):
    def __init__(self):
        super(Theorem203, self).__init__(203, "if maxClique == 2.0 then \n{\n    nodeCover <= (1.0/2.0)*(2.0*nodes+3.0-(sqrt(8.0*nodes+9.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCover","nodes"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("nodeCover",  (1.0/2.0)*(2.0*maxb("nodes")+3.0-(sqrt(8.0*maxb("nodes")+9.0))), ind='Max')
            except:
                pass
            try:
                set("nodes",  1.0*minb("nodeCover")+0.5*sqrt(8.0*minb("nodeCover")+1.0)-(0.5), ind='Min')
            except:
                pass
        
        return

class Theorem204(Theorem):
    def __init__(self):
        super(Theorem204, self).__init__(204, "if maxClique == 2.0 and nodes < 2.0*nodeCover and nodeCover <= 3.0*nodes/5.0 then \n{\n    nodeCover <= (2.0*nodes-(sqrt(5.0*edges-(nodes**2.0))))/5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","nodeCover","edges"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and maxb("nodes") < 2.0*minb("nodeCover") and maxb("nodeCover") <= 3.0*minb("nodes")/5.0:
            try:
                set("nodeCover",  (2.0*maxb("nodes")-(sqrt(5.0*minb("edges")-(maxb("nodes")**2.0))))/5.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeCover")+sqrt(minb("edges")-(minb("nodeCover")**2.0)), ind='Min')
            except:
                pass
            try:
                set("edges",  0.2*minb("nodes")**2.0+0.2*(5.0*maxb("nodeCover")-(2.0*minb("nodes")))**2.0, ind='Max')
            except:
                pass
        
        return

class Theorem205(Theorem):
    def __init__(self):
        super(Theorem205, self).__init__(205, "if mindeg == 2.0 then \n{\n    edgeCover <= nodes*max(4.0, maxdeg)/(2.0+max(4.0, maxdeg))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeCover","nodes","maxdeg"]
    def run(self):
        if minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0:
            try:
                set("edgeCover",  maxb("nodes")*max(4.0, maxb("maxdeg"))/(2.0+max(4.0, maxb("maxdeg"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edgeCover")*(max(4.0, minb("maxdeg"))+2.0)/max(4.0, minb("maxdeg")), ind='Min')
            except:
                pass
        
        return

class Theorem206(Theorem):
    def __init__(self):
        super(Theorem206, self).__init__(206, "nodeCover <= (nodes*maxdeg+1.0)/(maxdeg+1.0)-(1.0/(mindeg+1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","mindeg"]
    def run(self):
        try:
            set("nodeCover",  (maxb("nodes")*maxb("maxdeg")+1.0)/(maxb("maxdeg")+1.0)-(1.0/(maxb("mindeg")+1.0)), ind='Max')
        except:
            pass
        try:
            set("nodes",  (minb("maxdeg")*minb("mindeg")*minb("nodeCover")+minb("maxdeg")*minb("nodeCover")+minb("maxdeg")+minb("mindeg")*minb("nodeCover")-(minb("mindeg"))+minb("nodeCover"))/(minb("maxdeg")*(minb("mindeg")+1.0)), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (-(minb("mindeg")*maxb("nodeCover"))+minb("mindeg")-(maxb("nodeCover")))/(minb("mindeg")*maxb("nodeCover")-(minb("mindeg")*minb("nodes"))+maxb("nodeCover")-(minb("nodes"))+1.0), ind='Min')
        except:
            pass
        try:
            set("mindeg",  (-(minb("maxdeg")*maxb("nodeCover"))+minb("maxdeg")*minb("nodes")-(minb("maxdeg"))-(maxb("nodeCover")))/(minb("maxdeg")*maxb("nodeCover")-(minb("maxdeg")*minb("nodes"))+maxb("nodeCover")-(1.0)), ind='Min')
        except:
            pass
        return

class Theorem207(Theorem):
    def __init__(self):
        super(Theorem207, self).__init__(207, "if maxClique == 2.0 and maxdeg >= 3.0 then \n{\n    nodeCover <= nodes*(maxdeg-((6.0/5.0)/(maxdeg-((1.0/5.0)))))\n\n} else if nodes >= 3.0 and connected and not complete and not cycle or (cycle and isset nodes and even nodes) then \n{\n    nodeCover <= nodes*(maxdeg-(1.0))/maxdeg+1.0/(maxdeg+1.0)-(1.0/(mindeg+1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","nodeCover","nodes","connected","complete","cycle","mindeg"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and minb("maxdeg") >= 3.0:
            try:
                set("nodeCover",  maxb("nodes")*(maxb("maxdeg")-((6.0/5.0)/(maxb("maxdeg")-((1.0/5.0))))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("nodeCover")*(-(5.0*minb("maxdeg"))+1.0)/(-(5.0*minb("maxdeg")**2.0)+minb("maxdeg")+6.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (5.0*minb("nodeCover")+minb("nodes")+sqrt(25.0*minb("nodeCover")**2.0-(10.0*minb("nodeCover")*minb("nodes"))+121.0*minb("nodes")**2.0))/(10.0*minb("nodes")), ind='Min')
            except:
                pass
        
        elif minb("nodes") >= 3.0 and get("connected") == True  and get("complete") == False  and get("cycle") == False  or (get("cycle") == True  and maxb("nodes") != 'undt'  and minb("nodes") == maxb("nodes") and evenInvar("nodes")):
            try:
                set("nodeCover",  maxb("nodes")*(maxb("maxdeg")-(1.0))/maxb("maxdeg")+1.0/(maxb("maxdeg")+1.0)-(1.0/(maxb("mindeg")+1.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  maxb("maxdeg")*(maxb("maxdeg")*minb("mindeg")*minb("nodeCover")+maxb("maxdeg")*minb("nodeCover")+maxb("maxdeg")+minb("mindeg")*minb("nodeCover")-(minb("mindeg"))+minb("nodeCover"))/(maxb("maxdeg")**2.0*minb("mindeg")+maxb("maxdeg")**2.0-(minb("mindeg"))-(1.0)), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(minb("mindeg")*minb("nodeCover"))+minb("mindeg")-(minb("nodeCover"))+sqrt(minb("mindeg")**2.0*minb("nodeCover")**2.0-(4.0*minb("mindeg")**2.0*minb("nodeCover")*minb("nodes"))-(2.0*minb("mindeg")**2.0*minb("nodeCover"))+4.0*minb("mindeg")**2.0*minb("nodes")**2.0+minb("mindeg")**2.0+2.0*minb("mindeg")*minb("nodeCover")**2.0-(8.0*minb("mindeg")*minb("nodeCover")*minb("nodes"))-(2.0*minb("mindeg")*minb("nodeCover"))+8.0*minb("mindeg")*minb("nodes")**2.0-(4.0*minb("mindeg")*minb("nodes"))+minb("nodeCover")**2.0-(4.0*minb("nodeCover")*minb("nodes"))+4.0*minb("nodes")**2.0-(4.0*minb("nodes"))))/(2.0*(minb("mindeg")*minb("nodeCover")-(minb("mindeg")*minb("nodes"))+minb("nodeCover")-(minb("nodes"))+1.0)), ind='Min')
            except:
                pass
            try:
                set("mindeg",  (-(maxb("maxdeg")**2.0*maxb("nodeCover"))+maxb("maxdeg")**2.0*minb("nodes")-(maxb("maxdeg")**2.0)-(maxb("maxdeg")*maxb("nodeCover"))-(minb("nodes")))/(maxb("maxdeg")**2.0*maxb("nodeCover")-(maxb("maxdeg")**2.0*minb("nodes"))+maxb("maxdeg")*maxb("nodeCover")-(maxb("maxdeg"))+minb("nodes")), ind='Min')
            except:
                pass
        
        return

class Theorem208(Theorem):
    def __init__(self):
        super(Theorem208, self).__init__(208, "if connected and not complete then \n{\n    nodeCover <= (2.0*edges*nodes*nodes-(3.0*nodes)-(1.0))/(2.0*edges*nodes+nodes*nodes)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","complete","nodeCover","edges","nodes"]
    def run(self):
        if get("connected") == True  and get("complete") == False :
            try:
                set("nodeCover",  (2.0*maxb("edges")*minb("nodes")*minb("nodes")-(3.0*minb("nodes"))-(1.0))/(2.0*maxb("edges")*minb("nodes")+minb("nodes")*minb("nodes")), ind='Max')
            except:
                pass
            try:
                set("edges",  -((maxb("nodeCover")*maxb("nodes")**2.0+3.0*maxb("nodes")+1.0)/(2.0*maxb("nodes")*(maxb("nodeCover")-(maxb("nodes"))))), ind='Min')
            except:
                pass
            try:
                set("nodes",  (2.0*maxb("edges")*maxb("nodeCover")+sqrt(4.0*maxb("edges")**2.0*maxb("nodeCover")**2.0+12.0*maxb("edges")*maxb("nodeCover")+8.0*maxb("edges")-(4.0*maxb("nodeCover"))+9.0)+3.0)/(2.0*(2.0*maxb("edges")-(maxb("nodeCover")))), ind='Max')
            except:
                pass
        
        return

class Theorem209(Theorem):
    def __init__(self):
        super(Theorem209, self).__init__(209, "nodeCover <= nodes*(1.0-(2.0/(maxdeg+maxClique+1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","maxClique"]
    def run(self):
        try:
            set("nodeCover",  maxb("nodes")*(1.0-(2.0/(maxb("maxdeg")+maxb("maxClique")+1.0))), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("nodeCover")*(minb("maxClique")+minb("maxdeg")+1.0)/(minb("maxClique")+minb("maxdeg")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (-(minb("maxClique")*maxb("nodeCover"))+minb("maxClique")*minb("nodes")-(maxb("nodeCover"))-(minb("nodes")))/(maxb("nodeCover")-(minb("nodes"))), ind='Min')
        except:
            pass
        try:
            set("maxClique",  (-(minb("maxdeg")*maxb("nodeCover"))+minb("maxdeg")*minb("nodes")-(maxb("nodeCover"))-(minb("nodes")))/(maxb("nodeCover")-(minb("nodes"))), ind='Min')
        except:
            pass
        return

class Theorem210(Theorem):
    def __init__(self):
        super(Theorem210, self).__init__(210, "nodeCover <= ((nodes-(2.0))*maxdeg+maxClique+mindeg-(1.0))/(maxdeg+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","maxClique","mindeg"]
    def run(self):
        try:
            set("nodeCover",  ((maxb("nodes")-(2.0))*maxb("maxdeg")+maxb("maxClique")+maxb("mindeg")-(1.0))/(maxb("maxdeg")+1.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  (-(maxb("maxClique"))+minb("maxdeg")*(minb("nodeCover")+2.0)-(maxb("mindeg"))+minb("nodeCover")+1.0)/minb("maxdeg"), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (minb("maxClique")+minb("mindeg")-(maxb("nodeCover"))-(1.0))/(maxb("nodeCover")-(minb("nodes"))+2.0), ind='Min')
        except:
            pass
        try:
            set("maxClique",  minb("maxdeg")*minb("nodeCover")-(minb("maxdeg")*maxb("nodes"))+2.0*minb("maxdeg")-(maxb("mindeg"))+minb("nodeCover")+1.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  -(maxb("maxClique"))+minb("maxdeg")*minb("nodeCover")-(minb("maxdeg")*maxb("nodes"))+2.0*minb("maxdeg")+minb("nodeCover")+1.0, ind='Min')
        except:
            pass
        return

class Theorem211(Theorem):
    def __init__(self):
        super(Theorem211, self).__init__(211, "if nodeCover > nodes-(nodeCliqueCover) then \n{\n    nodeCover <= nodes*maxdeg/(maxdeg+1.0)-((1.0/3.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","nodeCliqueCover","maxdeg"]
    def run(self):
        if minb("nodeCover") > maxb("nodes")-(minb("nodeCliqueCover")):
            try:
                set("nodeCover",  maxb("nodes")*maxb("maxdeg")/(maxb("maxdeg")+1.0)-((1.0/3.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("nodeCover")+1.0/3.0+minb("nodeCover")/maxb("maxdeg")+1.0/(3.0*maxb("maxdeg")), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  -((3.0*maxb("nodeCover")+1.0)/(3.0*maxb("nodeCover")-(3.0*maxb("nodes"))+1.0)), ind='Min')
            except:
                pass
        
        return

class Theorem212(Theorem):
    def __init__(self):
        super(Theorem212, self).__init__(212, "nodeCliqueCover <= edgeCover;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","edgeCover"]
    def run(self):
        try:
            set("nodeCliqueCover",  maxb("edgeCover"), ind='Max')
        except:
            pass
        try:
            set("edgeCover",  minb("nodeCliqueCover"), ind='Min')
        except:
            pass
        return

class Theorem213(Theorem):
    def __init__(self):
        super(Theorem213, self).__init__(213, "domination <= nodeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodeInd"]
    def run(self):
        try:
            set("domination",  maxb("nodeInd"), ind='Max')
        except:
            pass
        try:
            set("nodeInd",  minb("domination"), ind='Min')
        except:
            pass
        return

class Theorem214(Theorem):
    def __init__(self):
        super(Theorem214, self).__init__(214, "domination <= edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["domination","edgeInd"]
    def run(self):
        try:
            set("domination",  maxb("edgeInd"), ind='Max')
        except:
            pass
        try:
            set("edgeInd",  minb("domination"), ind='Min')
        except:
            pass
        return

class Theorem215(Theorem):
    def __init__(self):
        super(Theorem215, self).__init__(215, "numOfComponents <= domination;", "")
    def involves(self, str_invar):
        return str_invar in ["numOfComponents","domination"]
    def run(self):
        try:
            set("numOfComponents",  maxb("domination"), ind='Max')
        except:
            pass
        try:
            set("domination",  minb("numOfComponents"), ind='Min')
        except:
            pass
        return

class Theorem216(Theorem):
    def __init__(self):
        super(Theorem216, self).__init__(216, "maxdeg <= edgeChromatic;", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","edgeChromatic"]
    def run(self):
        try:
            set("maxdeg",  maxb("edgeChromatic"), ind='Max')
        except:
            pass
        try:
            set("edgeChromatic",  minb("maxdeg"), ind='Min')
        except:
            pass
        return

class Theorem217(Theorem):
    def __init__(self):
        super(Theorem217, self).__init__(217, "edgeChromatic <= maxdeg+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","maxdeg"]
    def run(self):
        try:
            set("edgeChromatic",  maxb("maxdeg")+1.0, ind='Max')
        except:
            pass
        try:
            set("maxdeg",  minb("edgeChromatic")-(1.0), ind='Min')
        except:
            pass
        return

class Theorem218(Theorem):
    def __init__(self):
        super(Theorem218, self).__init__(218, "mindeg <= nodeCover;", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodeCover"]
    def run(self):
        try:
            set("mindeg",  maxb("nodeCover"), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  minb("mindeg"), ind='Min')
        except:
            pass
        return

class Theorem219(Theorem):
    def __init__(self):
        super(Theorem219, self).__init__(219, "edgeConnec <= mindeg;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg"]
    def run(self):
        try:
            set("edgeConnec",  maxb("mindeg"), ind='Max')
        except:
            pass
        try:
            set("mindeg",  minb("edgeConnec"), ind='Min')
        except:
            pass
        return

class Theorem220(Theorem):
    def __init__(self):
        super(Theorem220, self).__init__(220, "maxClique <= chromaticNum;", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum"]
    def run(self):
        try:
            set("maxClique",  maxb("chromaticNum"), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  minb("maxClique"), ind='Min')
        except:
            pass
        return

