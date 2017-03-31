class Theorem421(Theorem):
    def __init__(self):
        super(Theorem421, self).__init__(421, "if nodeInd == 2.0 and maxClique >= 2.0*nodes/5.0 then \n{\n    maxClique >= (2.0*nodes+sqrt(nodes*(3.0*nodes-(5.0))/2.0-(5.0*edges)))/5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","maxClique","nodes","edges"]
    def run(self):
        if minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0 and minb("maxClique") >= 2.0*maxb("nodes")/5.0:
            try:
                set("maxClique",  (2.0*minb("nodes")+sqrt(minb("nodes")*(3.0*minb("nodes")-(5.0))/2.0-(5.0*maxb("edges"))))/5.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  4.0*maxb("maxClique")+5.0*sqrt(-(8.0e-2*minb("edges"))+0.24*maxb("maxClique")**2.0-(0.16*maxb("maxClique"))+1.0e-2)-(0.5), ind='Max')
            except:
                pass
            try:
                set("edges",  0.3*minb("nodes")**2.0-(0.5*minb("nodes"))-(0.2*(5.0*maxb("maxClique")-(2.0*minb("nodes")))**2.0), ind='Min')
            except:
                pass
        
        return

class Theorem422(Theorem):
    def __init__(self):
        super(Theorem422, self).__init__(422, "if not forest then \n{\n    bandwidth >= (2.0*nodeCover*(girth-(2.0))-(nodes*(girth-(3.0))))/(2.0*(nodes-(nodeCover)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","bandwidth","nodeCover","girth","nodes"]
    def run(self):
        if get("forest") == False :
            try:
                set("bandwidth",  (2.0*minb("nodeCover")*(minb("girth")-(2.0))-(maxb("nodes")*(minb("girth")-(3.0))))/(2.0*(maxb("nodes")-(minb("nodeCover")))), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("nodes")*(2.0*maxb("bandwidth")+maxb("girth")-(3.0))/(2.0*(maxb("bandwidth")+maxb("girth")-(2.0))), ind='Max')
            except:
                pass
            try:
                set("girth",  (-(2.0*maxb("bandwidth")*maxb("nodeCover"))+2.0*maxb("bandwidth")*maxb("nodes")+4.0*maxb("nodeCover")-(3.0*maxb("nodes")))/(2.0*maxb("nodeCover")-(maxb("nodes"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeCover")*(minb("bandwidth")+minb("girth")-(2.0))/(2.0*minb("bandwidth")+minb("girth")-(3.0)), ind='Min')
            except:
                pass
        
        return

class Theorem423(Theorem):
    def __init__(self):
        super(Theorem423, self).__init__(423, "nodeCover <= nodes-(maxdeg/(chromaticNum-(1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","chromaticNum"]
    def run(self):
        try:
            set("nodeCover",  maxb("nodes")-(minb("maxdeg")/(maxb("chromaticNum")-(1.0))), ind='Max')
        except:
            pass
        try:
            set("nodes",  (minb("chromaticNum")*minb("nodeCover")+minb("maxdeg")-(minb("nodeCover")))/(minb("chromaticNum")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  -(maxb("chromaticNum")*maxb("nodeCover"))+maxb("chromaticNum")*maxb("nodes")+maxb("nodeCover")-(maxb("nodes")), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  (-(maxb("maxdeg"))+minb("nodeCover")-(minb("nodes")))/(minb("nodeCover")-(minb("nodes"))), ind='Min')
        except:
            pass
        return

class Theorem424(Theorem):
    def __init__(self):
        super(Theorem424, self).__init__(424, "if connected and (not cycle or (cycle and isset nodes and even nodes)) and (edges >= nodes or maxdeg > 2.0 or (isset nodes and odd nodes)) then \n{\n    nodeCover <= (nodes*(maxdeg**2.0+maxdeg-(1.0)))/(maxdeg*(maxdeg+1.0))-(nodes**2.0/(nodes+2.0*edges))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","cycle","nodes","edges","maxdeg","nodeCover"]
    def run(self):
        if get("connected") == True  and (get("cycle") == False  or (get("cycle") == True  and maxb("nodes") != 'undt'  and minb("nodes") == maxb("nodes") and evenInvar("nodes"))) and (minb("edges") >= maxb("nodes") or minb("maxdeg") > 2.0 or (maxb("nodes") != 'undt'  and minb("nodes") == maxb("nodes") and oddInvar("nodes"))):
            try:
                set("nodeCover",  (minb("nodes")*(minb("maxdeg")**2.0+minb("maxdeg")-(1.0)))/(minb("maxdeg")*(minb("maxdeg")+1.0))-(minb("nodes")**2.0/(minb("nodes")+2.0*maxb("edges"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  maxb("edges")*minb("maxdeg")**2.0+maxb("edges")*minb("maxdeg")-(maxb("edges"))-(minb("maxdeg")**2.0*maxb("nodeCover")/2.0)-(minb("maxdeg")*maxb("nodeCover")/2.0)+sqrt(4.0*maxb("edges")**2.0*minb("maxdeg")**4.0+8.0*maxb("edges")**2.0*minb("maxdeg")**3.0-(4.0*maxb("edges")**2.0*minb("maxdeg")**2.0)-(8.0*maxb("edges")**2.0*minb("maxdeg"))+4.0*maxb("edges")**2.0-(4.0*maxb("edges")*minb("maxdeg")**4.0*maxb("nodeCover"))-(8.0*maxb("edges")*minb("maxdeg")**3.0*maxb("nodeCover"))-(8.0*maxb("edges")*minb("maxdeg")**2.0*maxb("nodeCover"))-(4.0*maxb("edges")*minb("maxdeg")*maxb("nodeCover"))+minb("maxdeg")**4.0*maxb("nodeCover")**2.0+2.0*minb("maxdeg")**3.0*maxb("nodeCover")**2.0+minb("maxdeg")**2.0*maxb("nodeCover")**2.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  (-(maxb("edges")*maxb("nodeCover"))+maxb("edges")*maxb("nodes")-(maxb("nodeCover")*maxb("nodes")/2.0)+sqrt((2.0*maxb("edges")*maxb("nodeCover")-(2.0*maxb("edges")*maxb("nodes"))+maxb("nodeCover")*maxb("nodes"))*(2.0*maxb("edges")*maxb("nodeCover")-(10.0*maxb("edges")*maxb("nodes"))+maxb("nodeCover")*maxb("nodes")-(4.0*maxb("nodes")**2.0)))/2.0)/(2.0*maxb("edges")*maxb("nodeCover")-(2.0*maxb("edges")*maxb("nodes"))+maxb("nodeCover")*maxb("nodes")), ind='Max')
            except:
                pass
            try:
                set("edges",  -(maxb("nodes")*(maxb("maxdeg")**2.0*maxb("nodeCover")+maxb("maxdeg")*maxb("nodeCover")+maxb("nodes"))/(2.0*maxb("maxdeg")**2.0*maxb("nodeCover")-(2.0*maxb("maxdeg")**2.0*maxb("nodes"))+2.0*maxb("maxdeg")*maxb("nodeCover")-(2.0*maxb("maxdeg")*maxb("nodes"))+2.0*maxb("nodes"))), ind='Min')
            except:
                pass
        
        return

class Theorem425(Theorem):
    def __init__(self):
        super(Theorem425, self).__init__(425, "if planar then \n{\n    mindeg <= nodes-(nodeCover)+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","nodes","nodeCover"]
    def run(self):
        if get("planar") == True :
            try:
                set("mindeg",  maxb("nodes")-(minb("nodeCover"))+2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("mindeg")+minb("nodeCover")-(2.0), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  -(minb("mindeg"))+maxb("nodes")+2.0, ind='Max')
            except:
                pass
        
        return

class Theorem426(Theorem):
    def __init__(self):
        super(Theorem426, self).__init__(426, "edges <= max((nodes-(edgeCover))*(2.0*nodes-(2.0*edgeCover)+1.0), (nodes-(edgeCover))*(nodes+edgeCover-(1.0))/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","edgeCover"]
    def run(self):
        try:
            set("edges",  max((maxb("nodes")-(minb("edgeCover")))*(2.0*maxb("nodes")-(2.0*minb("edgeCover"))+1.0), (maxb("nodes")-(minb("edgeCover")))*(maxb("nodes")+minb("edgeCover")-(1.0))/2.0), ind='Max')
        except:
            pass
        return

class Theorem427(Theorem):
    def __init__(self):
        super(Theorem427, self).__init__(427, "let x = mindeg*floor((mindeg+3.0)/2.0)-(1.0);if regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and even nodes then \n{\n    edgeCover <= (nodes+2.0*floor((nodes+1.0)/(2.0*x)))/2.0\n\n} else if regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and odd nodes then \n{\n    edgeCover <= (nodes+max(2.0*floor((nodes+1.0+x)/(2.0*x))-(1.0), 1.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","edgeConnec","nodes","edgeCover"]
    def run(self):
        if get("regular") == True  and minb("mindeg") >= 3.0 and minb("edgeConnec") >= maxb("mindeg")-(2.0) and evenInvar("nodes"):
            try:
                set("edgeCover",  (maxb("nodes")+2.0*floor((maxb("nodes")+1.0)/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(2.0*floor((maxb("nodes")+1.0)/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))))+2.0*minb("edgeCover"), ind='Min')
            except:
                pass
        
        elif get("regular") == True  and minb("mindeg") >= 3.0 and minb("edgeConnec") >= maxb("mindeg")-(2.0) and oddInvar("nodes"):
            try:
                set("edgeCover",  (maxb("nodes")+max(2.0*floor((maxb("nodes")+1.0+minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0)))-(1.0), 1.0))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(max(2.0*floor((maxb("nodes")+1.0+minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0)))-(1.0), 1.0))+2.0*minb("edgeCover"), ind='Min')
            except:
                pass
        
        return

class Theorem428(Theorem):
    def __init__(self):
        super(Theorem428, self).__init__(428, "if mindeg == 3.0 and maxdeg == 3.0 then \n{\n    edgeCover <= nodes/2.0+(nodes+3.0)/18.0+(numOfComponents+4.0)/6.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeCover","nodes","numOfComponents"]
    def run(self):
        if minb("mindeg") >= 3.0 and maxb("mindeg") <= 3.0 and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0:
            try:
                set("edgeCover",  maxb("nodes")/2.0+(maxb("nodes")+3.0)/18.0+(maxb("numOfComponents")+4.0)/6.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  9.0*minb("edgeCover")/5.0-(3.0*maxb("numOfComponents")/10.0)-(3.0/2.0), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  6.0*minb("edgeCover")-(10.0*maxb("nodes")/3.0)-(5.0), ind='Min')
            except:
                pass
        
        return

class Theorem429(Theorem):
    def __init__(self):
        super(Theorem429, self).__init__(429, "if maxClique == 2.0 and maxdeg <= 4.0 then \n{\n    edges >= 13.0*nodeCover-(7.0*nodes)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 4.0:
            try:
                set("edges",  13.0*minb("nodeCover")-(7.0*maxb("nodes")), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("edges")/13.0+7.0*maxb("nodes")/13.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(maxb("edges")/7.0)+13.0*minb("nodeCover")/7.0, ind='Min')
            except:
                pass
        
        return

class Theorem430(Theorem):
    def __init__(self):
        super(Theorem430, self).__init__(430, "if nodeConnec >= 2.0 and nodeCover <= nodes-(2.0) then \n{\n    circumference >= (2.0*(2.0*nodes-(nodeCover)-(2.0))/(nodes-(nodeCover)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodeCover","nodes","circumference"]
    def run(self):
        if minb("nodeConnec") >= 2.0 and maxb("nodeCover") <= minb("nodes")-(2.0):
            try:
                set("circumference",  (2.0*(2.0*minb("nodes")-(minb("nodeCover"))-(2.0))/(minb("nodes")-(minb("nodeCover")))), ind='Min')
            except:
                pass
            try:
                set("nodes",  (maxb("circumference")*maxb("nodeCover")-(2.0*maxb("nodeCover"))-(4.0))/(maxb("circumference")-(4.0)), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  (maxb("circumference")*maxb("nodes")-(4.0*maxb("nodes"))+4.0)/(maxb("circumference")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem431(Theorem):
    def __init__(self):
        super(Theorem431, self).__init__(431, "if girth >= 6.0 then \n{\n    nodeCover <= nodes*maxdeg**2.0/(maxdeg**2.0+2.0*maxdeg-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodeCover","nodes","maxdeg"]
    def run(self):
        if minb("girth") >= 6.0:
            try:
                set("nodeCover",  maxb("nodes")*minb("maxdeg")**2.0/(minb("maxdeg")**2.0+2.0*minb("maxdeg")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("nodeCover")+2.0*minb("nodeCover")/minb("maxdeg")-(minb("nodeCover")/minb("maxdeg")**2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  -((minb("nodeCover")+sqrt(minb("nodeCover")*(2.0*minb("nodeCover")-(minb("nodes")))))/(minb("nodeCover")-(minb("nodes")))), ind='Max')
            except:
                pass
        
        return

class Theorem432(Theorem):
    def __init__(self):
        super(Theorem432, self).__init__(432, "if mindeg == maxdeg and mindeg == 2.0 and girth >= 8.0 then \n{\n    nodeCover <= 33.0*nodes/53.0\n\n} else if mindeg == maxdeg and mindeg == 2.0 and girth >= 6.0 then \n{\n    nodeCover <= 33.0*nodes/52.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodeCover","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and minb("girth") >= 8.0:
            try:
                set("nodeCover",  33.0*maxb("nodes")/53.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  53.0*minb("nodeCover")/33.0, ind='Min')
            except:
                pass
        
        elif minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and minb("girth") >= 6.0:
            try:
                set("nodeCover",  33.0*maxb("nodes")/52.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  52.0*minb("nodeCover")/33.0, ind='Min')
            except:
                pass
        
        return

class Theorem433(Theorem):
    def __init__(self):
        super(Theorem433, self).__init__(433, "if regular and nodes < 2.0*nodeCover then \n{\n    edgeChromatic == maxdeg+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","nodeCover","edgeChromatic","maxdeg"]
    def run(self):
        if get("regular") == True  and maxb("nodes") < 2.0*minb("nodeCover"):
            try:
                set("edgeChromatic",  minb("maxdeg")+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("edgeChromatic")-(1.0), ind='Max')
            except:
                pass
            try:
                set("edgeChromatic",  maxb("maxdeg")+1.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  minb("edgeChromatic")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem434(Theorem):
    def __init__(self):
        super(Theorem434, self).__init__(434, "if regular then \n{\n    edgeCover <= nodes*(maxdeg+2.0)/(2.0*(maxdeg+1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","edgeCover","nodes","maxdeg"]
    def run(self):
        if get("regular") == True :
            try:
                set("edgeCover",  maxb("nodes")*(maxb("maxdeg")+2.0)/(2.0*(maxb("maxdeg")+1.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("edgeCover")*(minb("maxdeg")+1.0)/(minb("maxdeg")+2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  2.0*(-(maxb("edgeCover"))+minb("nodes"))/(2.0*maxb("edgeCover")-(minb("nodes"))), ind='Min')
            except:
                pass
        
        return

class Theorem435(Theorem):
    def __init__(self):
        super(Theorem435, self).__init__(435, "if regular and nodes == 2.0*maxdeg+1.0 then \n{\n    nodeCover >= nodes-(nodeConnec)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","nodeCover","nodeConnec"]
    def run(self):
        if get("regular") == True  and minb("nodes") >= 2.0*maxb("maxdeg")+1.0 and maxb("nodes") <= 2.0*minb("maxdeg")+1.0:
            try:
                set("nodeCover",  minb("nodes")-(maxb("nodeConnec")), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("nodeConnec")+maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  -(maxb("nodeCover"))+minb("nodes"), ind='Min')
            except:
                pass
        
        return

class Theorem436(Theorem):
    def __init__(self):
        super(Theorem436, self).__init__(436, "let t = floor((girth-(2.0))/2.0);if girth >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeCover <= nodes-(maxdeg*floor((t+2.0)/2.0))-(1.0)\n\n} else if girth >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeCover <= nodes-(maxdeg*floor((t+2.0)/2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodeCover","nodes","maxdeg"]
    def run(self):
        if minb("girth") >= 4.0 and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and evenInvar(floor(("girth"-(2.0))/2.0)):
            try:
                set("nodeCover",  maxb("nodes")-(minb("maxdeg")*floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0))-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0)*minb("maxdeg")+minb("nodeCover")+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(minb("nodeCover"))+maxb("nodes")-(1.0))/floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0), ind='Max')
            except:
                pass
        
        elif minb("girth") >= 4.0 and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and evenInvar(floor(("girth"-(2.0))/2.0)):
            try:
                set("nodeCover",  maxb("nodes")-(minb("maxdeg")*floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0)*minb("maxdeg")+minb("nodeCover"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(minb("nodeCover"))+maxb("nodes"))/floor((floor((minb("girth")-(2.0))/2.0)+2.0)/2.0), ind='Max')
            except:
                pass
        
        return

class Theorem437(Theorem):
    def __init__(self):
        super(Theorem437, self).__init__(437, "let t = floor((girth-(2.0))/2.0);if girth >= 4.0 and mindeg >= 3.0 and odd t then \n{\n    nodeCover <= nodes-(maxdeg*((mindeg-(1.0))**(t-(1.0))-(1.0))/(mindeg*(mindeg-(2.0))))\n\n} else if girth >= 4.0 and mindeg >= 3.0 and even t then \n{\n    nodeCover <= nodes-(maxdeg*(mindeg-(1.0))*((mindeg-(1.0))**t-(1.0))/(mindeg*(mindeg-(2.0))))-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodeCover","nodes","maxdeg"]
    def run(self):
        if minb("girth") >= 4.0 and minb("mindeg") >= 3.0 and oddInvar(floor(("girth"-(2.0))/2.0)):
            try:
                set("nodeCover",  maxb("nodes")-(minb("maxdeg")*((maxb("mindeg")-(1.0))**(floor((minb("girth")-(2.0))/2.0)-(1.0))-(1.0))/(maxb("mindeg")*(maxb("mindeg")-(2.0)))), ind='Max')
            except:
                pass
            try:
                set("nodes",  (minb("maxdeg")*(maxb("mindeg")-(1.0))**(floor((minb("girth")-(2.0))/2.0)-(1.0))-(minb("maxdeg"))+maxb("mindeg")**2.0*minb("nodeCover")-(2.0*maxb("mindeg")*minb("nodeCover")))/(maxb("mindeg")*(maxb("mindeg")-(2.0))), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("mindeg")*(-(maxb("mindeg")*maxb("nodeCover"))+maxb("mindeg")*maxb("nodes")+2.0*maxb("nodeCover")-(2.0*maxb("nodes")))/((maxb("mindeg")-(1.0))**(floor((minb("girth")-(2.0))/2.0)-(1.0))-(1.0)), ind='Max')
            except:
                pass
        
        elif minb("girth") >= 4.0 and minb("mindeg") >= 3.0 and evenInvar(floor(("girth"-(2.0))/2.0)):
            try:
                set("nodeCover",  maxb("nodes")-(minb("maxdeg")*(minb("mindeg")-(1.0))*((minb("mindeg")-(1.0))**floor((minb("girth")-(2.0))/2.0)-(1.0))/(minb("mindeg")*(minb("mindeg")-(2.0))))-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  (minb("maxdeg")*minb("mindeg")*(minb("mindeg")-(1.0))**floor((minb("girth")-(2.0))/2.0)-(minb("maxdeg")*minb("mindeg"))-(minb("maxdeg")*(minb("mindeg")-(1.0))**floor((minb("girth")-(2.0))/2.0))+minb("maxdeg")+minb("mindeg")**2.0*minb("nodeCover")+minb("mindeg")**2.0-(2.0*minb("mindeg")*minb("nodeCover"))-(2.0*minb("mindeg")))/(minb("mindeg")*(minb("mindeg")-(2.0))), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  minb("mindeg")*(-(minb("mindeg")*maxb("nodeCover"))+minb("mindeg")*maxb("nodes")-(minb("mindeg"))+2.0*maxb("nodeCover")-(2.0*maxb("nodes"))+2.0)/(minb("mindeg")*(minb("mindeg")-(1.0))**floor((minb("girth")-(2.0))/2.0)-(minb("mindeg"))-((minb("mindeg")-(1.0))**floor((minb("girth")-(2.0))/2.0))+1.0), ind='Max')
            except:
                pass
        
        return

class Theorem438(Theorem):
    def __init__(self):
        super(Theorem438, self).__init__(438, "nodeInd >= (2.0*nodes-(edges)+edgeInd)/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges","edgeInd"]
    def run(self):
        try:
            set("nodeInd",  (2.0*minb("nodes")-(maxb("edges"))+minb("edgeInd"))/4.0, ind='Min')
        except:
            pass
        try:
            set("nodes",  -(minb("edgeInd")/2.0)+maxb("edges")/2.0+2.0*maxb("nodeInd"), ind='Max')
        except:
            pass
        try:
            set("edges",  minb("edgeInd")-(4.0*maxb("nodeInd"))+2.0*minb("nodes"), ind='Min')
        except:
            pass
        try:
            set("edgeInd",  maxb("edges")+4.0*maxb("nodeInd")-(2.0*minb("nodes")), ind='Max')
        except:
            pass
        return

class Theorem439(Theorem):
    def __init__(self):
        super(Theorem439, self).__init__(439, "nodeCover <= (nodes+edges+edgeCover)/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","edges","edgeCover"]
    def run(self):
        try:
            set("nodeCover",  (maxb("nodes")+maxb("edges")+maxb("edgeCover"))/4.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  -(maxb("edgeCover"))-(maxb("edges"))+4.0*minb("nodeCover"), ind='Min')
        except:
            pass
        try:
            set("edges",  -(maxb("edgeCover"))+4.0*minb("nodeCover")-(maxb("nodes")), ind='Min')
        except:
            pass
        try:
            set("edgeCover",  -(maxb("edges"))+4.0*minb("nodeCover")-(maxb("nodes")), ind='Min')
        except:
            pass
        return

class Theorem440(Theorem):
    def __init__(self):
        super(Theorem440, self).__init__(440, "nodeInd >= (3.0*nodes-(edges)-(edgeCover))/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges","edgeCover"]
    def run(self):
        try:
            set("nodeInd",  (3.0*minb("nodes")-(maxb("edges"))-(maxb("edgeCover")))/4.0, ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("edgeCover")/3.0+maxb("edges")/3.0+4.0*maxb("nodeInd")/3.0, ind='Max')
        except:
            pass
        try:
            set("edges",  -(maxb("edgeCover"))-(4.0*maxb("nodeInd"))+3.0*minb("nodes"), ind='Min')
        except:
            pass
        try:
            set("edgeCover",  -(maxb("edges"))-(4.0*maxb("nodeInd"))+3.0*minb("nodes"), ind='Min')
        except:
            pass
        return

