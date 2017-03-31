class Theorem401(Theorem):
    def __init__(self):
        super(Theorem401, self).__init__(401, "if planar and edges == 3.0*nodes-(6.0) and maxdeg <= mindeg+1.0 then \n{\n    mindeg == nodeConnec\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","edges","nodes","maxdeg","mindeg","nodeConnec"]
    def run(self):
        if get("planar") == True  and minb("edges") >= 3.0*maxb("nodes")-(6.0) and maxb("edges") <= 3.0*minb("nodes")-(6.0) and maxb("maxdeg") <= minb("mindeg")+1.0:
            try:
                set("mindeg",  minb("nodeConnec"), ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  maxb("nodeConnec"), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  minb("mindeg"), ind='Min')
            except:
                pass
        
        return

class Theorem402(Theorem):
    def __init__(self):
        super(Theorem402, self).__init__(402, "bandwidth <= nodes-((mindeg+1.0)*(numOfComponents-(1.0)))-(1.0)-((nodeInd-(numOfComponents)+1.0)/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","mindeg","numOfComponents","nodeInd"]
    def run(self):
        try:
            set("bandwidth",  maxb("nodes")-((minb("mindeg")+1.0)*(maxb("numOfComponents")-(1.0)))-(1.0)-((minb("nodeInd")-(maxb("numOfComponents"))+1.0)/2.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("bandwidth")+minb("mindeg")*minb("numOfComponents")-(minb("mindeg"))+minb("nodeInd")/2.0+minb("numOfComponents")/2.0+1.0/2.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  (-(2.0*minb("bandwidth"))-(minb("nodeInd"))+2.0*maxb("nodes")-(minb("numOfComponents"))-(1.0))/(2.0*(minb("numOfComponents")-(1.0))), ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  (-(2.0*maxb("bandwidth"))+2.0*minb("mindeg")-(maxb("nodeInd"))+2.0*minb("nodes")-(1.0))/(2.0*minb("mindeg")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  -(2.0*minb("bandwidth"))-(2.0*maxb("mindeg")*minb("numOfComponents"))+2.0*maxb("mindeg")+2.0*maxb("nodes")-(minb("numOfComponents"))-(1.0), ind='Max')
        except:
            pass
        return

class Theorem403(Theorem):
    def __init__(self):
        super(Theorem403, self).__init__(403, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem404(Theorem):
    def __init__(self):
        super(Theorem404, self).__init__(404, "if mindeg > edgeConnec and edgeConnec == nodeConnec then \n{\n    nodes >= mindeg+maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeConnec","nodeConnec","nodes","maxdeg"]
    def run(self):
        if minb("mindeg") > maxb("edgeConnec") and minb("edgeConnec") >= maxb("nodeConnec") and maxb("edgeConnec") <= minb("nodeConnec"):
            try:
                set("nodes",  minb("mindeg")+minb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("mindeg",  -(minb("maxdeg"))+maxb("nodes"), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(minb("mindeg"))+maxb("nodes"), ind='Max')
            except:
                pass
        
        return

class Theorem405(Theorem):
    def __init__(self):
        super(Theorem405, self).__init__(405, "if mindeg > edgeConnec and edgeConnec == nodeConnec and nodeConnec > 0.0 and diam == 3.0 then \n{\n    domination <= edgeConnec+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeConnec","nodeConnec","diam","domination"]
    def run(self):
        if minb("mindeg") > maxb("edgeConnec") and minb("edgeConnec") >= maxb("nodeConnec") and maxb("edgeConnec") <= minb("nodeConnec") and minb("nodeConnec") > 0.0 and minb("diam") >= 3.0 and maxb("diam") <= 3.0:
            try:
                set("domination",  maxb("edgeConnec")+1.0, ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  minb("domination")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem406(Theorem):
    def __init__(self):
        super(Theorem406, self).__init__(406, "if edges > (nodes-(1.0))**2.0/4.0 and edges <= (nodes-(1.0))*(nodes-(2.0))/2.0 then \n{\n    mindeg <= edgeConnec-(1.0)+(nodes-(sqrt(4.0*edges+2.0*nodes-(nodes**2.0))))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","mindeg","edgeConnec"]
    def run(self):
        if minb("edges") > (maxb("nodes")-(1.0))**2.0/4.0 and maxb("edges") <= (minb("nodes")-(1.0))*(minb("nodes")-(2.0))/2.0:
            try:
                set("mindeg",  maxb("edgeConnec")-(1.0)+(maxb("nodes")-(sqrt(4.0*minb("edges")+2.0*maxb("nodes")-(maxb("nodes")**2.0))))/2.0, ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  minb("mindeg")-(0.5*maxb("nodes"))+0.5*sqrt(4.0*minb("edges")+2.0*maxb("nodes")-(maxb("nodes")**2.0))+1.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  -(maxb("edgeConnec"))+minb("mindeg")+sqrt(-(4.0*maxb("edgeConnec")**2.0)+8.0*maxb("edgeConnec")*minb("mindeg")+4.0*maxb("edgeConnec")+8.0*minb("edges")-(4.0*minb("mindeg")**2.0)-(4.0*minb("mindeg"))+1.0)/2.0+3.0/2.0, ind='Min')
            except:
                pass
            try:
                set("edges",  -(0.5*maxb("nodes"))+0.25*maxb("nodes")**2.0+0.25*(2.0*maxb("edgeConnec")-(2.0*minb("mindeg"))+1.0*maxb("nodes")-(2.0))**2.0, ind='Max')
            except:
                pass
        
        return

class Theorem407(Theorem):
    def __init__(self):
        super(Theorem407, self).__init__(407, "domination <= (nodes-(maxdeg)-(1.0))*(nodes-(mindeg)-(2.0))/(nodes-(1.0))+2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","maxdeg","mindeg"]
    def run(self):
        try:
            set("domination",  (maxb("nodes")-(minb("maxdeg"))-(1.0))*(maxb("nodes")-(minb("mindeg"))-(2.0))/(maxb("nodes")-(1.0))+2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("domination")/2.0+minb("maxdeg")/2.0+minb("mindeg")/2.0+sqrt(minb("domination")**2.0+2.0*minb("domination")*minb("maxdeg")+2.0*minb("domination")*minb("mindeg")-(2.0*minb("domination"))+minb("maxdeg")**2.0-(2.0*minb("maxdeg")*minb("mindeg"))-(6.0*minb("maxdeg"))+minb("mindeg")**2.0-(2.0*minb("mindeg"))+1.0)/2.0+1.0/2.0, ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (maxb("domination")*minb("nodes")-(maxb("domination"))+maxb("mindeg")*minb("nodes")-(maxb("mindeg"))-(minb("nodes")**2.0)+minb("nodes"))/(maxb("mindeg")-(minb("nodes"))+2.0), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (maxb("domination")*minb("nodes")-(maxb("domination"))+maxb("maxdeg")*minb("nodes")-(2.0*maxb("maxdeg"))-(minb("nodes")**2.0)+minb("nodes"))/(maxb("maxdeg")-(minb("nodes"))+1.0), ind='Max')
        except:
            pass
        return

class Theorem408(Theorem):
    def __init__(self):
        super(Theorem408, self).__init__(408, "let s = floor((maxdeg+2.0-(sqrt((maxdeg+2.0)**2.0-(4.0*nodes))))/2.0);if diameter == 3.0 and s <= floor((nodes/2.0)**(1.0/3.0)) then \n{\n    edges >= nodes+s*(s-(1.0))/2.0-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","edges"]
    def run(self):
        if minb("diameter") >= 3.0 and maxb("diameter") <= 3.0 and maxb(floor(("maxdeg"+2.0-(sqrt(("maxdeg"+2.0)**2.0-(4.0*"nodes"))))/2.0)) <= floor((minb("nodes")/2.0)**(1.0/3.0)):
            try:
                set("edges",  minb("nodes")+floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)*(floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)-(1.0))/2.0-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  -(floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)**2.0/2.0)+floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)/2.0+maxb("edges")+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem409(Theorem):
    def __init__(self):
        super(Theorem409, self).__init__(409, "if nodes >= 4.0 and maxClique == 2.0 and hamiltonian then \n{\n    edges <= (nodes-(4.0))*nodes/4.0+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxClique","hamiltonian","edges"]
    def run(self):
        if minb("nodes") >= 4.0 and minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and get("hamiltonian") == True :
            try:
                set("edges",  (maxb("nodes")-(4.0))*maxb("nodes")/4.0+2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*sqrt(minb("edges")-(1.0))+2.0, ind='Min')
            except:
                pass
        
        return

class Theorem410(Theorem):
    def __init__(self):
        super(Theorem410, self).__init__(410, "spectralRadius >= mindeg;", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","mindeg"]
    def run(self):
        try:
            set("spectralRadius",  minb("mindeg"), ind='Min')
        except:
            pass
        try:
            set("mindeg",  maxb("spectralRadius"), ind='Max')
        except:
            pass
        return

class Theorem411(Theorem):
    def __init__(self):
        super(Theorem411, self).__init__(411, "if connected and nodes >= 2.0*mindeg+2.0 and istrue congruent(nodes, mindeg+1.0, 0.0) then \n{\n    diameter <= 3.0*nodes/(mindeg+1.0)-(3.0)\n\n} else if connected and nodes >= 2.0*mindeg+2.0 and istrue congruent(nodes, mindeg+1.0, 1.0) then \n{\n    diam <= 3.0*nodes/(mindeg+1.0)+2.0\n\n} else if connected and nodes >= 2.0*mindeg+2.0 then \n{\n    diam <= 3.0*nodes/(mindeg+1.0)-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodes","mindeg","diameter","diam"]
    def run(self):
        if get("connected") == True  and minb("nodes") >= 2.0*maxb("mindeg")+2.0 and congruent("nodes", "mindeg"+1.0, 0.0):
            try:
                set("diameter",  3.0*maxb("nodes")/(minb("mindeg")+1.0)-(3.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("diameter")*minb("mindeg")/3.0+minb("diameter")/3.0+minb("mindeg")+1.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  (-(minb("diameter"))+3.0*maxb("nodes")-(3.0))/(minb("diameter")+3.0), ind='Max')
            except:
                pass
        
        elif get("connected") == True  and minb("nodes") >= 2.0*maxb("mindeg")+2.0 and congruent("nodes", "mindeg"+1.0, 1.0):
            try:
                set("diam",  3.0*maxb("nodes")/(minb("mindeg")+1.0)+2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("diam")*minb("mindeg")/3.0+minb("diam")/3.0-(2.0*minb("mindeg")/3.0)-(2.0/3.0), ind='Min')
            except:
                pass
            try:
                set("mindeg",  (-(minb("diam"))+3.0*maxb("nodes")+2.0)/(minb("diam")-(2.0)), ind='Max')
            except:
                pass
        
        elif get("connected") == True  and minb("nodes") >= 2.0*maxb("mindeg")+2.0:
            try:
                set("diam",  3.0*maxb("nodes")/(minb("mindeg")+1.0)-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("diam")*minb("mindeg")/3.0+minb("diam")/3.0+minb("mindeg")/3.0+1.0/3.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  (-(minb("diam"))+3.0*maxb("nodes")-(1.0))/(minb("diam")+1.0), ind='Max')
            except:
                pass
        
        return

class Theorem412(Theorem):
    def __init__(self):
        super(Theorem412, self).__init__(412, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem413(Theorem):
    def __init__(self):
        super(Theorem413, self).__init__(413, "edges >= (nodes-(chromaticNum))**2.0/(nodeInd-(1.0))+chromaticNum*(chromaticNum-(1.0))/2.0-((nodeInd-(1.0))*((nodes-(chromaticNum))/(nodeInd-(1.0)))*((nodes-(chromaticNum))/(nodeInd-(1.0)))/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","chromaticNum","nodeInd"]
    def run(self):
        try:
            set("edges",  (maxb("nodes")-(maxb("chromaticNum")))**2.0/(maxb("nodeInd")-(1.0))+maxb("chromaticNum")*(maxb("chromaticNum")-(1.0))/2.0-((maxb("nodeInd")-(1.0))*((maxb("nodes")-(maxb("chromaticNum")))/(maxb("nodeInd")-(1.0)))*((maxb("nodes")-(maxb("chromaticNum")))/(maxb("nodeInd")-(1.0)))/2.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  minb("chromaticNum")+sqrt((minb("nodeInd")-(1.0))*(-(minb("chromaticNum")**2.0)+minb("chromaticNum")+2.0*minb("edges"))), ind='Min')
        except:
            pass
        try:
            set("chromaticNum",  (minb("nodeInd")+2.0*minb("nodes")+sqrt((minb("nodeInd")-(1.0))*(8.0*minb("edges")*minb("nodeInd")+minb("nodeInd")-(4.0*minb("nodes")**2.0)+4.0*minb("nodes")-(1.0)))-(1.0))/(2.0*minb("nodeInd")), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  (-(maxb("chromaticNum")**2.0)+maxb("chromaticNum")+2.0*minb("edges")+(maxb("chromaticNum")-(maxb("nodes")))**2.0)/(-(maxb("chromaticNum")**2.0)+maxb("chromaticNum")+2.0*minb("edges")), ind='Min')
        except:
            pass
        return

class Theorem414(Theorem):
    def __init__(self):
        super(Theorem414, self).__init__(414, "if diam <= 4.0 then \n{\n    edges <= ((nodes-(2.0))*(nodes-(3.0))-(2.0*(nodes-(2.0))*(diam-(4.0))*nodeConnec)-(4.0*nodeConnec*(nodeConnec+1.0))+nodeConnec**2.0*(diam-(2.0))*(diam-(3.0)))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diam","edges","nodes","nodeConnec"]
    def run(self):
        if maxb("diam") <= 4.0:
            try:
                set("edges",  ((maxb("nodes")-(2.0))*(maxb("nodes")-(3.0))-(2.0*(maxb("nodes")-(2.0))*(maxb("diam")-(4.0))*minb("nodeConnec"))-(4.0*minb("nodeConnec")*(minb("nodeConnec")+1.0))+minb("nodeConnec")**2.0*(maxb("diam")-(2.0))*(maxb("diam")-(3.0)))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("diam")*minb("nodeConnec")-(4.0*minb("nodeConnec"))+sqrt(-(12.0*minb("diam")*minb("nodeConnec")**2.0)+4.0*minb("diam")*minb("nodeConnec")+8.0*minb("edges")+56.0*minb("nodeConnec")**2.0+1.0)/2.0+5.0/2.0, ind='Min')
            except:
                pass
            try:
                set("diam",  (5.0*minb("nodeConnec")+2.0*minb("nodes")+sqrt(8.0*minb("edges")+17.0*minb("nodeConnec")**2.0-(12.0*minb("nodeConnec")*minb("nodes"))+40.0*minb("nodeConnec")+4.0*minb("nodes")-(8.0))-(4.0))/(2.0*minb("nodeConnec")), ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  (minb("diam")*maxb("nodes")-(2.0*minb("diam"))-(4.0*maxb("nodes"))+sqrt(2.0*minb("diam")**2.0*maxb("edges")+minb("diam")**2.0*maxb("nodes")-(2.0*minb("diam")**2.0)-(10.0*minb("diam")*maxb("edges"))-(3.0*minb("diam")*maxb("nodes")**2.0)+11.0*minb("diam")*maxb("nodes")-(10.0*minb("diam"))+4.0*maxb("edges")+14.0*maxb("nodes")**2.0-(70.0*maxb("nodes"))+88.0)+10.0)/(minb("diam")**2.0-(5.0*minb("diam"))+2.0), ind='Max')
            except:
                pass
        
        return

class Theorem415(Theorem):
    def __init__(self):
        super(Theorem415, self).__init__(415, "domination <= (nodes+2.0-(mindeg))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","mindeg"]
    def run(self):
        try:
            set("domination",  (maxb("nodes")+2.0-(minb("mindeg")))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*minb("domination")+minb("mindeg")-(2.0), ind='Min')
        except:
            pass
        try:
            set("mindeg",  -(2.0*minb("domination"))+maxb("nodes")+2.0, ind='Max')
        except:
            pass
        return

class Theorem416(Theorem):
    def __init__(self):
        super(Theorem416, self).__init__(416, "if even nodes and maxdeg == nodes-(2.0) and edgeChromatic == maxdeg+1.0 then \n{\n    edges >= (nodes-(2.0))**2.0/2.0+1.0+mindeg\n\n};if even nodes and maxdeg == nodes-(2.0) and edges >= (nodes-(2.0))**2.0/2.0+1.0+mindeg then \n{\n    maxdeg == nodes-(2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxdeg","edgeChromatic","edges","mindeg"]
    def run(self):
        if evenInvar("nodes") and minb("maxdeg") >= maxb("nodes")-(2.0) and maxb("maxdeg") <= minb("nodes")-(2.0) and minb("edgeChromatic") >= maxb("maxdeg")+1.0 and maxb("edgeChromatic") <= minb("maxdeg")+1.0:
            try:
                set("edges",  (minb("nodes")-(2.0))**2.0/2.0+1.0+minb("mindeg"), ind='Min')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*maxb("edges")-(2.0*minb("mindeg"))-(2.0))+2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  maxb("edges")-((minb("nodes")-(2.0))**2.0/2.0)-(1.0), ind='Max')
            except:
                pass
        
        if evenInvar("nodes") and minb("maxdeg") >= maxb("nodes")-(2.0) and maxb("maxdeg") <= minb("nodes")-(2.0) and minb("edges") >= (maxb("nodes")-(2.0))**2.0/2.0+1.0+maxb("mindeg"):
            try:
                set("maxdeg",  minb("nodes")-(2.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("maxdeg")+2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodes")-(2.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("maxdeg")+2.0, ind='Min')
            except:
                pass
        
        return

class Theorem417(Theorem):
    def __init__(self):
        super(Theorem417, self).__init__(417, "if maxClique <= 2.0 and maxdeg <= 3.0 then \n{\n    edges >= 13.0*nodes/2.0-(14.0*nodeInd)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 3.0:
            try:
                set("edges",  13.0*minb("nodes")/2.0-(14.0*maxb("nodeInd")), ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edges")/13.0+28.0*maxb("nodeInd")/13.0, ind='Max')
            except:
                pass
            try:
                set("nodeInd",  -(maxb("edges")/14.0)+13.0*minb("nodes")/28.0, ind='Min')
            except:
                pass
        
        return

class Theorem418(Theorem):
    def __init__(self):
        super(Theorem418, self).__init__(418, "if maxClique <= 2.0 and maxdeg <= 2.0 then \n{\n    edges >= 7.0*nodes-(15.0*nodeInd)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 2.0:
            try:
                set("edges",  7.0*minb("nodes")-(15.0*maxb("nodeInd")), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/7.0+15.0*maxb("nodeInd")/7.0, ind='Max')
            except:
                pass
            try:
                set("nodeInd",  -(maxb("edges")/15.0)+7.0*minb("nodes")/15.0, ind='Min')
            except:
                pass
        
        return

class Theorem419(Theorem):
    def __init__(self):
        super(Theorem419, self).__init__(419, "if maxClique <= 2.0 and nodeCover <= 3.0*nodes/5.0 then \n{\n    nodeCover <= (3.0*nodes-(sqrt(5.0*edges-(nodes**2.0))))/5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCover","nodes","edges"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("nodeCover") <= 3.0*minb("nodes")/5.0:
            try:
                set("nodeCover",  (3.0*maxb("nodes")-(sqrt(5.0*minb("edges")-(maxb("nodes")**2.0))))/5.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  3.0*minb("nodeCover")/2.0+sqrt(2.0*minb("edges")-(minb("nodeCover")**2.0))/2.0, ind='Min')
            except:
                pass
            try:
                set("edges",  0.2*minb("nodes")**2.0+0.2*(5.0*maxb("nodeCover")-(3.0*minb("nodes")))**2.0, ind='Max')
            except:
                pass
        
        return

class Theorem420(Theorem):
    def __init__(self):
        super(Theorem420, self).__init__(420, "if maxClique <= 2.0 and nodeInd <= 2.0*nodes/5.0 then \n{\n    nodeInd >= (2.0*nodes+sqrt(5.0*edges-(nodes**2.0)))/5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeInd","nodes","edges"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("nodeInd") <= 2.0*minb("nodes")/5.0:
            try:
                set("nodeInd",  (2.0*minb("nodes")+sqrt(5.0*minb("edges")-(minb("nodes")**2.0)))/5.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeInd")+sqrt(maxb("edges")-(maxb("nodeInd")**2.0)), ind='Max')
            except:
                pass
            try:
                set("edges",  0.2*minb("nodes")**2.0+0.2*(5.0*maxb("nodeInd")-(2.0*minb("nodes")))**2.0, ind='Max')
            except:
                pass
        
        return

