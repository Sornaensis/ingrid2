class Theorem321(Theorem):
    def __init__(self):
        super(Theorem321, self).__init__(321, "if connected and regular and not complete and mindeg <= 3.0 then \n{\n    edgeCliqueCover >= 3.0*nodes/(mindeg+1.0)\n\n} else if connected and regular and not complete and mindeg >= 5.0 then \n{\n    edgeCliqueCover >= mindeg*nodes/((mindeg+1.0)*(mindeg-(2.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","regular","complete","mindeg","edgeCliqueCover","nodes"]
    def run(self):
        if get("connected") == True  and get("regular") == True  and get("complete") == False  and maxb("mindeg") <= 3.0:
            try:
                set("edgeCliqueCover",  3.0*minb("nodes")/(maxb("mindeg")+1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edgeCliqueCover")*(maxb("mindeg")+1.0)/3.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  (-(maxb("edgeCliqueCover"))+3.0*minb("nodes"))/maxb("edgeCliqueCover"), ind='Min')
            except:
                pass
        
        elif get("connected") == True  and get("regular") == True  and get("complete") == False  and minb("mindeg") >= 5.0:
            try:
                set("edgeCliqueCover",  maxb("mindeg")*minb("nodes")/((maxb("mindeg")+1.0)*(maxb("mindeg")-(2.0))), ind='Min')
            except:
                pass
            try:
                set("mindeg",  (minb("edgeCliqueCover")+minb("nodes")+sqrt(9.0*minb("edgeCliqueCover")**2.0+2.0*minb("edgeCliqueCover")*minb("nodes")+minb("nodes")**2.0))/(2.0*minb("edgeCliqueCover")), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edgeCliqueCover")*(maxb("mindeg")*(maxb("mindeg")-(1.0))-(2.0))/maxb("mindeg"), ind='Max')
            except:
                pass
        
        return

class Theorem322(Theorem):
    def __init__(self):
        super(Theorem322, self).__init__(322, "if connected and regular and mindeg <= 4.0 and not complete and (nodes == 7.0 or istrue congruent(nodes, 3.0, 5.0)) and ((nodes > 13.0 or nodes < 13.0) and (nodes > 18.0 or nodes < 18.0)) then \n{\n    edgeCliqueCover >= floor((3.0*nodes+4.0)/5.0)+1.0\n\n} else if connected and regular and mindeg <= 4.0 and not complete then \n{\n    edgeCliqueCover >= floor((3.0*nodes+4.0)/5.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","regular","mindeg","complete","nodes","edgeCliqueCover"]
    def run(self):
        if get("connected") == True  and get("regular") == True  and maxb("mindeg") <= 4.0 and get("complete") == False  and (minb("nodes") >= 7.0 and maxb("nodes") <= 7.0 or congruent("nodes", 3.0, 5.0)) and ((minb("nodes") > 13.0 or maxb("nodes") < 13.0) and (minb("nodes") > 18.0 or maxb("nodes") < 18.0)):
            try:
                set("edgeCliqueCover",  floor((3.0*minb("nodes")+4.0)/5.0)+1.0, ind='Min')
            except:
                pass
        
        elif get("connected") == True  and get("regular") == True  and maxb("mindeg") <= 4.0 and get("complete") == False :
            try:
                set("edgeCliqueCover",  floor((3.0*minb("nodes")+4.0)/5.0), ind='Min')
            except:
                pass
        
        return

class Theorem323(Theorem):
    def __init__(self):
        super(Theorem323, self).__init__(323, "if girth >= 6.0 then \n{\n    nodeInd >= (2.0*maxdeg-(1.0))*nodes/(maxdeg*maxdeg+2.0*maxdeg-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodeInd","maxdeg","nodes"]
    def run(self):
        if minb("girth") >= 6.0:
            try:
                set("nodeInd",  (2.0*maxb("maxdeg")-(1.0))*minb("nodes")/(maxb("maxdeg")*maxb("maxdeg")+2.0*maxb("maxdeg")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(minb("nodeInd"))+minb("nodes")+sqrt((minb("nodeInd")-(minb("nodes")))*(2.0*minb("nodeInd")-(minb("nodes")))))/minb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("nodeInd")*(maxb("maxdeg")**2.0+2.0*maxb("maxdeg")-(1.0))/(2.0*maxb("maxdeg")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem324(Theorem):
    def __init__(self):
        super(Theorem324, self).__init__(324, "if mindeg == maxdeg and maxdeg == 3.0 and girth >= 6.0 then \n{\n    nodeInd >= 19.0*nodes/52.0\n\n} else if mindeg == maxdeg and maxdeg == 3.0 and girth >= 8.0 then \n{\n    nodeInd >= 20.0*nodes/52.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodeInd","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("girth") >= 6.0:
            try:
                set("nodeInd",  19.0*minb("nodes")/52.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  52.0*maxb("nodeInd")/19.0, ind='Max')
            except:
                pass
        
        elif minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("girth") >= 8.0:
            try:
                set("nodeInd",  20.0*minb("nodes")/52.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  13.0*maxb("nodeInd")/5.0, ind='Max')
            except:
                pass
        
        return

class Theorem325(Theorem):
    def __init__(self):
        super(Theorem325, self).__init__(325, "if regular and even girth and girth >= 6.0 and connected and nodes <= (mindeg*(mindeg-(3.0))+2.0*(mindeg-(1.0))**(girth/2.0))/(mindeg-(2.0)) then \n{\n    bipartite,\n    diameter == girth/2.0+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","girth","connected","nodes","mindeg","bipartite","diameter"]
    def run(self):
        if get("regular") == True  and evenInvar("girth") and minb("girth") >= 6.0 and get("connected") == True  and maxb("nodes") <= (minb("mindeg")*(minb("mindeg")-(3.0))+2.0*(minb("mindeg")-(1.0))**(minb("girth")/2.0))/(minb("mindeg")-(2.0)):
            set("bipartite", True )
            try:
                set("diameter",  minb("girth")/2.0+1.0, ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*maxb("diameter")-(2.0), ind='Max')
            except:
                pass
            try:
                set("diameter",  maxb("girth")/2.0+1.0, ind='Max')
            except:
                pass
            try:
                set("girth",  2.0*minb("diameter")-(2.0), ind='Min')
            except:
                pass
        
        return

class Theorem326(Theorem):
    def __init__(self):
        super(Theorem326, self).__init__(326, "if bipartite and odd nodes then \n{\n    thickness <= ceil((nodes*nodes-(1.0))/(2.0*(nodes-(2.0))))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","thickness"]
    def run(self):
        if get("bipartite") == True  and oddInvar("nodes"):
            try:
                set("thickness",  ceil((maxb("nodes")*maxb("nodes")-(1.0))/(2.0*(maxb("nodes")-(2.0)))), ind='Max')
            except:
                pass
        
        return

class Theorem327(Theorem):
    def __init__(self):
        super(Theorem327, self).__init__(327, "if edges >= 1.0 then \n{\n    maxdeg >= 2.0*thickness-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","thickness"]
    def run(self):
        if minb("edges") >= 1.0:
            try:
                set("maxdeg",  2.0*minb("thickness")-(1.0), ind='Min')
            except:
                pass
            try:
                set("thickness",  maxb("maxdeg")/2.0+1.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem328(Theorem):
    def __init__(self):
        super(Theorem328, self).__init__(328, "nodeConnec <= 3.0*thickness-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","thickness"]
    def run(self):
        try:
            set("nodeConnec",  3.0*maxb("thickness")-(1.0), ind='Max')
        except:
            pass
        try:
            set("thickness",  minb("nodeConnec")/3.0+1.0/3.0, ind='Min')
        except:
            pass
        return

class Theorem329(Theorem):
    def __init__(self):
        super(Theorem329, self).__init__(329, "if mindeg == maxdeg and maxdeg == 3.0 and girth == 10.0 then \n{\n    nodes >= 70.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("girth") >= 10.0 and maxb("girth") <= 10.0:
            try:
                set("nodes",  70.0, ind='Min')
            except:
                pass
        
        return

class Theorem330(Theorem):
    def __init__(self):
        super(Theorem330, self).__init__(330, "if edges >= max(((nodes-(mindeg))*(nodes-(mindeg)-(1.0)))/2.0+mindeg*mindeg+1.0, (floor((nodes+2.0)/2.0)*(floor((nodes+2.0)/2.0)-(1.0)))/2.0+floor((nodes-(1.0))/2.0)**2.0+1.0) then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","mindeg","hamiltonian"]
    def run(self):
        if minb("edges") >= max(((maxb("nodes")-(minb("mindeg")))*(maxb("nodes")-(minb("mindeg"))-(1.0)))/2.0+minb("mindeg")*minb("mindeg")+1.0, (floor((maxb("nodes")+2.0)/2.0)*(floor((maxb("nodes")+2.0)/2.0)-(1.0)))/2.0+floor((maxb("nodes")-(1.0))/2.0)**2.0+1.0):
            set("hamiltonian", True )
        
        return

class Theorem331(Theorem):
    def __init__(self):
        super(Theorem331, self).__init__(331, "edges <= nodes*(nodes-(1.0))/2.0-((mindeg-(nodeConnec)+1.0)*(nodes-(mindeg)-(1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","mindeg","nodeConnec"]
    def run(self):
        try:
            set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/2.0-((minb("mindeg")-(maxb("nodeConnec"))+1.0)*(maxb("nodes")-(minb("mindeg"))-(1.0))), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("mindeg")-(minb("nodeConnec"))+sqrt(8.0*minb("edges")-(4.0*minb("mindeg")**2.0)-(4.0*minb("mindeg"))+4.0*minb("nodeConnec")**2.0-(4.0*minb("nodeConnec"))+1.0)/2.0+3.0/2.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  maxb("nodeConnec")/2.0+maxb("nodes")/2.0+sqrt(4.0*maxb("edges")+maxb("nodeConnec")**2.0-(2.0*maxb("nodeConnec")*maxb("nodes"))-(maxb("nodes")**2.0)+2.0*maxb("nodes"))/2.0-(1.0), ind='Max')
        except:
            pass
        try:
            set("nodeConnec",  (-(maxb("edges"))+minb("mindeg")**2.0-(minb("mindeg")*minb("nodes"))+2.0*minb("mindeg")+minb("nodes")**2.0/2.0-(3.0*minb("nodes")/2.0)+1.0)/(minb("mindeg")-(minb("nodes"))+1.0), ind='Min')
        except:
            pass
        return

class Theorem332(Theorem):
    def __init__(self):
        super(Theorem332, self).__init__(332, "if tree and maxdeg <= nodes-(2.0) then \n{\n    bandwidth <= (nodes-(1.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["tree","maxdeg","nodes","bandwidth"]
    def run(self):
        if get("tree") == True  and maxb("maxdeg") <= minb("nodes")-(2.0):
            try:
                set("bandwidth",  (maxb("nodes")-(1.0))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("bandwidth")+1.0, ind='Min')
            except:
                pass
        
        return

class Theorem333(Theorem):
    def __init__(self):
        super(Theorem333, self).__init__(333, "edges >= 2.0*bandwidth-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","bandwidth"]
    def run(self):
        try:
            set("edges",  2.0*minb("bandwidth")-(1.0), ind='Min')
        except:
            pass
        try:
            set("bandwidth",  maxb("edges")/2.0+1.0/2.0, ind='Max')
        except:
            pass
        return

class Theorem334(Theorem):
    def __init__(self):
        super(Theorem334, self).__init__(334, "if connected and mindeg >= 3.0 and girth >= 5.0 then \n{\n    domination <= (nodes-(floor(diameter/3.0)*(mindeg-(1.0)))-(1.0)-((mindeg-(1.0))*(mindeg-(2.0))/2.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","mindeg","girth","domination","nodes","diameter"]
    def run(self):
        if get("connected") == True  and minb("mindeg") >= 3.0 and minb("girth") >= 5.0:
            try:
                set("domination",  (maxb("nodes")-(floor(minb("diameter")/3.0)*(minb("mindeg")-(1.0)))-(1.0)-((minb("mindeg")-(1.0))*(minb("mindeg")-(2.0))/2.0))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  floor(minb("diameter")/3.0)*minb("mindeg")-(floor(minb("diameter")/3.0))+2.0*minb("domination")+minb("mindeg")**2.0/2.0-(3.0*minb("mindeg")/2.0)+2.0, ind='Min')
            except:
                pass
        
        return

class Theorem335(Theorem):
    def __init__(self):
        super(Theorem335, self).__init__(335, "if bandwidth >= nodes/2.0 then \n{\n    edges >= (2.0*floor(nodes/2.0)-(1.0))*(nodes/(nodes-(2.0)))**(bandwidth-(floor(nodes/2.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","edges"]
    def run(self):
        if minb("bandwidth") >= maxb("nodes")/2.0:
            try:
                set("edges",  (2.0*floor(minb("nodes")/2.0)-(1.0))*(minb("nodes")/(minb("nodes")-(2.0)))**(minb("bandwidth")-(floor(minb("nodes")/2.0))), ind='Min')
            except:
                pass
            try:
                set("nodes",  -(2.0/((maxb("edges")/(2.0*floor(maxb("nodes")/2.0)-(1.0)))**(1.0/(floor(maxb("nodes")/2.0)-(maxb("bandwidth"))))-(1.0))), ind='Max')
            except:
                pass
        
        return

class Theorem336(Theorem):
    def __init__(self):
        super(Theorem336, self).__init__(336, "if bandwidth >= nodes/2.0 then \n{\n    edges >= nodes*(nodes-(1.0))/(2.0*(nodes-(bandwidth)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","edges"]
    def run(self):
        if minb("bandwidth") >= maxb("nodes")/2.0:
            try:
                set("edges",  minb("nodes")*(minb("nodes")-(1.0))/(2.0*(minb("nodes")-(minb("bandwidth")))), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")+sqrt(-(8.0*minb("bandwidth")*maxb("edges"))+4.0*maxb("edges")**2.0+4.0*maxb("edges")+1.0)/2.0+1.0/2.0, ind='Max')
            except:
                pass
            try:
                set("bandwidth",  maxb("nodes")*(2.0*maxb("edges")-(maxb("nodes"))+1.0)/(2.0*maxb("edges")), ind='Max')
            except:
                pass
        
        return

class Theorem337(Theorem):
    def __init__(self):
        super(Theorem337, self).__init__(337, "if girth >= 5.0 then \n{\n    domination <= (2.0*nodes-((mindeg-(1.0))*(4.0*edges/nodes-(mindeg)-(2.0))))/4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","domination","nodes","mindeg","edges"]
    def run(self):
        if minb("girth") >= 5.0:
            try:
                set("domination",  (2.0*maxb("nodes")-((minb("mindeg")-(1.0))*(4.0*minb("edges")/maxb("nodes")-(minb("mindeg"))-(2.0))))/4.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("domination")-(maxb("mindeg")**2.0/4.0)-(maxb("mindeg")/4.0)+sqrt(16.0*minb("domination")**2.0-(8.0*minb("domination")*maxb("mindeg")**2.0)-(8.0*minb("domination")*maxb("mindeg"))+16.0*minb("domination")+32.0*minb("edges")*maxb("mindeg")-(32.0*minb("edges"))+maxb("mindeg")**4.0+2.0*maxb("mindeg")**3.0-(3.0*maxb("mindeg")**2.0)-(4.0*maxb("mindeg"))+4.0)/4.0+1.0/2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  (4.0*maxb("edges")-(minb("nodes"))+sqrt(16.0*maxb("domination")*minb("nodes")**2.0+16.0*maxb("edges")**2.0-(24.0*maxb("edges")*minb("nodes"))-(8.0*minb("nodes")**3.0)+9.0*minb("nodes")**2.0))/(2.0*minb("nodes")), ind='Max')
            except:
                pass
            try:
                set("edges",  maxb("nodes")*(-(4.0*minb("domination"))+maxb("mindeg")**2.0+maxb("mindeg")+2.0*maxb("nodes")-(2.0))/(4.0*(maxb("mindeg")-(1.0))), ind='Max')
            except:
                pass
        
        return

class Theorem338(Theorem):
    def __init__(self):
        super(Theorem338, self).__init__(338, "if connected and girth >= 5.0 and mindeg >= 4.0 then \n{\n    domination <= (nodes-(maxdeg)-(mindeg*(mindeg-(3.0))/3.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","girth","mindeg","domination","nodes","maxdeg"]
    def run(self):
        if get("connected") == True  and minb("girth") >= 5.0 and minb("mindeg") >= 4.0:
            try:
                set("domination",  (maxb("nodes")-(minb("maxdeg"))-(minb("mindeg")*(minb("mindeg")-(3.0))/3.0))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("domination")+minb("maxdeg")+minb("mindeg")**2.0/3.0-(minb("mindeg")), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  -(2.0*minb("domination"))-(minb("mindeg")**2.0/3.0)+minb("mindeg")+maxb("nodes"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  sqrt(-(24.0*minb("domination"))-(12.0*minb("maxdeg"))+12.0*maxb("nodes")+9.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem339(Theorem):
    def __init__(self):
        super(Theorem339, self).__init__(339, "if girth >= 5.0 then \n{\n    domination >= mindeg*numOfComponents\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","domination","mindeg","numOfComponents"]
    def run(self):
        if minb("girth") >= 5.0:
            try:
                set("domination",  minb("mindeg")*minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("domination")/minb("numOfComponents"), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  maxb("domination")/minb("mindeg"), ind='Max')
            except:
                pass
        
        return

class Theorem340(Theorem):
    def __init__(self):
        super(Theorem340, self).__init__(340, "if girth >= 6.0 then \n{\n    domination >= 2.0*(mindeg-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","domination","mindeg"]
    def run(self):
        if minb("girth") >= 6.0:
            try:
                set("domination",  2.0*(minb("mindeg")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("domination")/2.0+1.0, ind='Max')
            except:
                pass
        
        return

