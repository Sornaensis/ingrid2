class Theorem341(Theorem):
    def __init__(self):
        super(Theorem341, self).__init__(341, "if mindeg >= 2.0 and girth >= 7.0 then \n{\n    domination >= maxdeg+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","domination","maxdeg"]
    def run(self):
        if minb("mindeg") >= 2.0 and minb("girth") >= 7.0:
            try:
                set("domination",  minb("maxdeg")+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("domination")-(1.0), ind='Max')
            except:
                pass
        
        return

class Theorem342(Theorem):
    def __init__(self):
        super(Theorem342, self).__init__(342, "if girth >= 5.0 and girth <= nodes/2.0 then \n{\n    edges <= (nodes**2.0-(nodes*girth)+2.0*girth)/girth\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","edges"]
    def run(self):
        if minb("girth") >= 5.0 and maxb("girth") <= minb("nodes")/2.0:
            try:
                set("edges",  (maxb("nodes")**2.0-(maxb("nodes")*maxb("girth"))+2.0*maxb("girth"))/maxb("girth"), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("girth")/2.0+sqrt(minb("girth")*(4.0*minb("edges")+minb("girth")-(8.0)))/2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  minb("nodes")**2.0/(maxb("edges")+minb("nodes")-(2.0)), ind='Min')
            except:
                pass
        
        return

class Theorem343(Theorem):
    def __init__(self):
        super(Theorem343, self).__init__(343, "if girth >= 5.0 then \n{\n    edges <= nodes*sqrt(nodes-(1.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","edges","nodes"]
    def run(self):
        if minb("girth") >= 5.0:
            try:
                set("edges",  maxb("nodes")*sqrt(maxb("nodes")-(1.0))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -((-(54.0*minb("edges")**2.0)+sqrt((-(108.0*minb("edges")**2.0)-(2.0))**2.0-(4.0))/2.0-(1.0))**(1.0/3.0)/3.0)+0.333333333333333-(0.333333333333333/(-(54.0*minb("edges")**2.0)+sqrt((-(108.0*minb("edges")**2.0)-(2.0))**2.0-(4.0))/2.0-(1.0))**(1.0/3.0)), ind='Min')
            except:
                pass
        
        return

class Theorem344(Theorem):
    def __init__(self):
        super(Theorem344, self).__init__(344, "if not forest and nodes >= floor((3.0*girth-(3.0))/2.0) then \n{\n    edges <= nodes*(nodes-(1.0))/((3.0*girth-(5.0))/2.0)-(numOfComponents)+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodes","girth","edges","numOfComponents"]
    def run(self):
        if get("forest") == False  and minb("nodes") >= floor((3.0*maxb("girth")-(3.0))/2.0):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/((3.0*minb("girth")-(5.0))/2.0)-(minb("numOfComponents"))+1.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(6.0*minb("edges")*minb("girth")-(10.0*minb("edges"))+6.0*minb("girth")*minb("numOfComponents")-(6.0*minb("girth"))-(10.0*minb("numOfComponents"))+11.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (5.0*maxb("edges")+2.0*maxb("nodes")**2.0-(2.0*maxb("nodes"))+5.0*maxb("numOfComponents")-(5.0))/(3.0*(maxb("edges")+maxb("numOfComponents")-(1.0))), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  (-(3.0*maxb("edges")*maxb("girth"))+5.0*maxb("edges")+3.0*maxb("girth")+2.0*maxb("nodes")**2.0-(2.0*maxb("nodes"))-(5.0))/(3.0*maxb("girth")-(5.0)), ind='Max')
            except:
                pass
        
        return

class Theorem345(Theorem):
    def __init__(self):
        super(Theorem345, self).__init__(345, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem346(Theorem):
    def __init__(self):
        super(Theorem346, self).__init__(346, "if not forest and (nodeConnec > 0.0 or mindeg > 1.0) then \n{\n    genus >= (edges*(1.0-(2.0/girth)-(2.0/mindeg))+2.0*numOfComponents)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodeConnec","mindeg","genus","edges","girth","numOfComponents"]
    def run(self):
        if get("forest") == False  and (minb("nodeConnec") > 0.0 or minb("mindeg") > 1.0):
            try:
                set("genus",  (minb("edges")*(1.0-(2.0/minb("girth"))-(2.0/minb("mindeg")))+2.0*minb("numOfComponents"))/2.0, ind='Min')
            except:
                pass
            try:
                set("edges",  2.0*maxb("girth")*maxb("mindeg")*(-(minb("genus"))+maxb("numOfComponents"))/(-(maxb("girth")*maxb("mindeg"))+2.0*maxb("girth")+2.0*maxb("mindeg")), ind='Max')
            except:
                pass
            try:
                set("girth",  2.0*maxb("edges")*maxb("mindeg")/(maxb("edges")*maxb("mindeg")-(2.0*maxb("edges"))-(2.0*maxb("genus")*maxb("mindeg"))+2.0*maxb("mindeg")*minb("numOfComponents")), ind='Max')
            except:
                pass
            try:
                set("mindeg",  2.0*maxb("edges")*maxb("girth")/(maxb("edges")*maxb("girth")-(2.0*maxb("edges"))-(2.0*maxb("genus")*maxb("girth"))+2.0*maxb("girth")*minb("numOfComponents")), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(maxb("edges")/2.0)+maxb("edges")/minb("mindeg")+maxb("edges")/minb("girth")+maxb("genus"), ind='Max')
            except:
                pass
        
        return

class Theorem347(Theorem):
    def __init__(self):
        super(Theorem347, self).__init__(347, "if diameter == 2.0 then \n{\n    nodes <= nodeConnec*maxdeg+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodes","nodeConnec","maxdeg"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0:
            try:
                set("nodes",  maxb("nodeConnec")*maxb("maxdeg")+1.0, ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  (minb("nodes")-(1.0))/maxb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (minb("nodes")-(1.0))/maxb("nodeConnec"), ind='Min')
            except:
                pass
        
        return

class Theorem348(Theorem):
    def __init__(self):
        super(Theorem348, self).__init__(348, "if not forest and edges >= nodes+1.0-(numOfComponents) then \n{\n    nodes >= 3.0*girth/2.0+2.0*numOfComponents-(3.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","girth"]
    def run(self):
        if get("forest") == False  and minb("edges") >= maxb("nodes")+1.0-(minb("numOfComponents")):
            try:
                set("nodes",  3.0*minb("girth")/2.0+2.0*minb("numOfComponents")-(3.0), ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*maxb("nodes")/3.0-(4.0*minb("numOfComponents")/3.0)+2.0, ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(3.0*minb("girth")/4.0)+maxb("nodes")/2.0+3.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem349(Theorem):
    def __init__(self):
        super(Theorem349, self).__init__(349, "if not forest and edges >= nodes+3.0 then \n{\n    nodes >= 2.0*girth+2.0*numOfComponents-(4.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","girth","numOfComponents"]
    def run(self):
        if get("forest") == False  and minb("edges") >= maxb("nodes")+3.0:
            try:
                set("nodes",  2.0*minb("girth")+2.0*minb("numOfComponents")-(4.0), ind='Min')
            except:
                pass
            try:
                set("girth",  maxb("nodes")/2.0-(minb("numOfComponents"))+2.0, ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(minb("girth"))+maxb("nodes")/2.0+2.0, ind='Max')
            except:
                pass
        
        return

class Theorem350(Theorem):
    def __init__(self):
        super(Theorem350, self).__init__(350, "if not forest and edges >= nodes+4.0-(numOfComponents) then \n{\n    nodes >= 9.0*girth/4.0+2.0*numOfComponents-(5.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","girth"]
    def run(self):
        if get("forest") == False  and minb("edges") >= maxb("nodes")+4.0-(minb("numOfComponents")):
            try:
                set("nodes",  9.0*minb("girth")/4.0+2.0*minb("numOfComponents")-(5.0), ind='Min')
            except:
                pass
            try:
                set("girth",  4.0*maxb("nodes")/9.0-(8.0*minb("numOfComponents")/9.0)+20.0/9.0, ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(9.0*minb("girth")/8.0)+maxb("nodes")/2.0+5.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem351(Theorem):
    def __init__(self):
        super(Theorem351, self).__init__(351, "if girth >= max((nodes+1.0)/2.0, 5.0) and edges >= nodes+3.0 then \n{\n    if girth <= 7.0 then \n    {\n        girth <= 6.0\n    \n    } else  \n    {\n        girth <= 8.0\n    \n    },\n    nodes == 2.0*girth-(1.0),\n    nodeConnec == 2.0,\n    edgeConnec == 2.0,\n    mindeg == 2.0,\n    edges == nodes+3.0,\n    nonplanar\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","edges","nodeConnec","edgeConnec","mindeg","nonplanar"]
    def run(self):
        if minb("girth") >= max((maxb("nodes")+1.0)/2.0, 5.0) and minb("edges") >= maxb("nodes")+3.0:
            if maxb("girth") <= 7.0:
                try:
                    set("girth",  6.0, ind='Max')
                except:
                    pass
            
            elif True:
                try:
                    set("girth",  8.0, ind='Max')
                except:
                    pass
            
            
            try:
                set("nodes",  2.0*minb("girth")-(1.0), ind='Min')
            except:
                pass
            try:
                set("girth",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("girth")-(1.0), ind='Max')
            except:
                pass
            try:
                set("girth",  minb("nodes")/2.0+1.0/2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  2.0, ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Max')
            except:
                pass
            try:
                set("edges",  minb("nodes")+3.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")-(3.0), ind='Max')
            except:
                pass
            try:
                set("edges",  maxb("nodes")+3.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edges")-(3.0), ind='Min')
            except:
                pass
            set("nonplanar", True )
        
        return

class Theorem352(Theorem):
    def __init__(self):
        super(Theorem352, self).__init__(352, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem353(Theorem):
    def __init__(self):
        super(Theorem353, self).__init__(353, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem354(Theorem):
    def __init__(self):
        super(Theorem354, self).__init__(354, "let k = floor((nodes-(floor((girth-(1.0))/2.0)))/girth);if not forest then \n{\n    edges <= nodes+k*(2.0*nodes-(girth*(k-(1.0))))/(2.0*floor((girth-(1.0))/4.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","girth"]
    def run(self):
        if get("forest") == False :
            try:
                set("edges",  maxb("nodes")+floor((maxb("nodes")-(floor((minb("girth")-(1.0))/2.0)))/minb("girth"))*(2.0*maxb("nodes")-(minb("girth")*(floor((maxb("nodes")-(floor((minb("girth")-(1.0))/2.0)))/minb("girth"))-(1.0))))/(2.0*floor((minb("girth")-(1.0))/4.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  (floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))**2.0*maxb("girth")/2.0-(floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))*maxb("girth")/2.0)+floor((maxb("girth")-(1.0))/4.0)*minb("edges"))/(floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))+floor((maxb("girth")-(1.0))/4.0)), ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*(floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))*minb("nodes")-(floor((maxb("girth")-(1.0))/4.0)*minb("edges"))+floor((maxb("girth")-(1.0))/4.0)*minb("nodes"))/(floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))*(floor((minb("nodes")-(floor((maxb("girth")-(1.0))/2.0)))/maxb("girth"))-(1.0))), ind='Max')
            except:
                pass
        
        return

class Theorem355(Theorem):
    def __init__(self):
        super(Theorem355, self).__init__(355, "let t = floor(girth/2.0);if mindeg == 1.0 then \n{\n    nodes >= 1.0+maxdeg-((maxdeg-(1.0))*(mindeg-(1.0))**(t-(1.0))*(1.0+(-(1.0))**girth)/2.0)\n\n} else if mindeg == 2.0 then \n{\n    nodes >= 1.0+maxdeg*t-((maxdeg-(1.0))*(mindeg-(1.0))**(t-(1.0))*(1.0+(-(1.0))**girth)/2.0)\n\n} else if mindeg >= 3.0 then \n{\n    nodes >= 1.0+maxdeg*(((mindeg-(1.0))**t-(1.0))/(mindeg-(2.0)))-((maxdeg-(1.0))*(mindeg-(1.0))**(t-(1.0))*(1.0+(-(1.0))**girth)/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","maxdeg","girth"]
    def run(self):
        if minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0:
            try:
                set("nodes",  1.0+minb("maxdeg")-((minb("maxdeg")-(1.0))*(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))*(1.0+(-(1.0))**maxb("girth"))/2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  ((-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))-(2.0*minb("nodes"))+(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))+2.0)/((-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))+(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))-(2.0)), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (2.0*(maxb("maxdeg")-(minb("nodes"))+1.0)/((-(1.0))**maxb("girth")*maxb("maxdeg")-((-(1.0))**maxb("girth"))+maxb("maxdeg")-(1.0)))**(1.0/(floor(maxb("girth")/2.0)-(1.0)))+1.0, ind='Max')
            except:
                pass
        
        elif minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0:
            try:
                set("nodes",  1.0+minb("maxdeg")*floor(minb("girth")/2.0)-((minb("maxdeg")-(1.0))*(maxb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0))*(1.0+(-(1.0))**minb("girth"))/2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  ((-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))-(2.0*minb("nodes"))+(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))+2.0)/((-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))-(2.0*floor(maxb("girth")/2.0))+(maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))), ind='Max')
            except:
                pass
        
        elif minb("mindeg") >= 3.0:
            try:
                set("nodes",  1.0+minb("maxdeg")*(((minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(1.0))/(minb("mindeg")-(2.0)))-((minb("maxdeg")-(1.0))*(minb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0))*(1.0+(-(1.0))**minb("girth"))/2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  ((-(1.0))**maxb("girth")*maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(2.0*(-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))-(2.0*maxb("mindeg")**2.0*maxb("nodes"))+2.0*maxb("mindeg")**2.0+6.0*maxb("mindeg")*maxb("nodes")+maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(6.0*maxb("mindeg"))-(4.0*maxb("nodes"))-(2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))+4.0)/((-(1.0))**maxb("girth")*maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(2.0*(-(1.0))**maxb("girth")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))-(maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))+2.0*maxb("mindeg")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem356(Theorem):
    def __init__(self):
        super(Theorem356, self).__init__(356, "if regular and edgeInd < nodes/2.0 then \n{\n    edgeChromatic == maxdeg+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","edgeInd","nodes","edgeChromatic","maxdeg"]
    def run(self):
        if get("regular") == True  and maxb("edgeInd") < minb("nodes")/2.0:
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

class Theorem357(Theorem):
    def __init__(self):
        super(Theorem357, self).__init__(357, "if regular then \n{\n    edgeInd >= nodes*maxdeg/(2.0*(maxdeg+1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","edgeInd","nodes","maxdeg"]
    def run(self):
        if get("regular") == True :
            try:
                set("edgeInd",  minb("nodes")*minb("maxdeg")/(2.0*(minb("maxdeg")+1.0)), ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeInd")*(maxb("maxdeg")+1.0)/maxb("maxdeg"), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(2.0*minb("edgeInd")/(2.0*minb("edgeInd")-(minb("nodes")))), ind='Max')
            except:
                pass
        
        return

class Theorem358(Theorem):
    def __init__(self):
        super(Theorem358, self).__init__(358, "if nodeConnec >= 2.0 and mindeg >= (nodes+nodeConnec)/3.0 then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","mindeg","nodes","hamiltonian"]
    def run(self):
        if minb("nodeConnec") >= 2.0 and minb("mindeg") >= (maxb("nodes")+maxb("nodeConnec"))/3.0:
            set("hamiltonian", True )
        
        return

class Theorem359(Theorem):
    def __init__(self):
        super(Theorem359, self).__init__(359, "if nodeConnec >= 3.0 then \n{\n    circumference >= min(nodes, 3.0*mindeg-(nodeConnec))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        if minb("nodeConnec") >= 3.0:
            try:
                set("circumference",  min(minb("nodes"), 3.0*minb("mindeg")-(maxb("nodeConnec"))), ind='Min')
            except:
                pass
        
        return

class Theorem360(Theorem):
    def __init__(self):
        super(Theorem360, self).__init__(360, "if regular and nodes == 2.0*maxdeg+1.0 then \n{\n    nodeConnec >= nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","nodeConnec","nodeInd"]
    def run(self):
        if get("regular") == True  and minb("nodes") >= 2.0*maxb("maxdeg")+1.0 and maxb("nodes") <= 2.0*minb("maxdeg")+1.0:
            try:
                set("nodeConnec",  minb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  maxb("nodeConnec"), ind='Max')
            except:
                pass
        
        return

