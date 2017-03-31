class Theorem381(Theorem):
    def __init__(self):
        super(Theorem381, self).__init__(381, "if planar and nodes >= 4.0 then \n{\n    edges <= 3.0*nodes-(9.0)+min(3.0, edgeConnec)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","nodes","edges","edgeConnec"]
    def run(self):
        if get("planar") == True  and minb("nodes") >= 4.0:
            try:
                set("edges",  3.0*maxb("nodes")-(9.0)+min(3.0, maxb("edgeConnec")), ind='Max')
            except:
                pass
            try:
                set("nodes",  -(min(3.0, maxb("edgeConnec"))/3.0)+minb("edges")/3.0+3.0, ind='Min')
            except:
                pass
        
        return

class Theorem382(Theorem):
    def __init__(self):
        super(Theorem382, self).__init__(382, "if planer and edgeConnec < mindeg and (nodes >= 5.0 or mindeg >= 2.0) then \n{\n    if mindeg == edgeConnec+1.0 and mindeg == 1.0 then \n    {\n        edges <= 3.0*nodes-(11.0)\n    \n    } else  \n    {\n        edges <= 3.0*nodes-(12.0)+nodeConnec\n    \n    }\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planer","edgeConnec","mindeg","nodes","edges","nodeConnec"]
    def run(self):
        if get("planer") == True  and maxb("edgeConnec") < minb("mindeg") and (minb("nodes") >= 5.0 or minb("mindeg") >= 2.0):
            if minb("mindeg") >= maxb("edgeConnec")+1.0 and maxb("mindeg") <= minb("edgeConnec")+1.0 and minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0:
                try:
                    set("edges",  3.0*maxb("nodes")-(11.0), ind='Max')
                except:
                    pass
                try:
                    set("nodes",  minb("edges")/3.0+11.0/3.0, ind='Min')
                except:
                    pass
            
            elif True:
                try:
                    set("edges",  3.0*maxb("nodes")-(12.0)+maxb("nodeConnec"), ind='Max')
                except:
                    pass
                try:
                    set("nodes",  minb("edges")/3.0-(maxb("nodeConnec")/3.0)+4.0, ind='Min')
                except:
                    pass
                try:
                    set("nodeConnec",  minb("edges")-(3.0*maxb("nodes"))+12.0, ind='Min')
                except:
                    pass
            
        
        return

class Theorem383(Theorem):
    def __init__(self):
        super(Theorem383, self).__init__(383, "if not forest then \n{\n    nodes >= maxdeg+numOfComponents-(2.0)+((circumference*(girth-(3.0))+2.0)/(girth/2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodes","maxdeg","numOfComponents","circumference","girth"]
    def run(self):
        if get("forest") == False :
            try:
                set("nodes",  minb("maxdeg")+minb("numOfComponents")-(2.0)+((minb("circumference")*(minb("girth")-(3.0))+2.0)/(minb("girth")/2.0)), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (6.0*maxb("circumference")+maxb("girth")*(-(2.0*maxb("circumference"))+maxb("nodes")-(minb("numOfComponents"))+2.0)-(4.0))/maxb("girth"), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  (6.0*maxb("circumference")+maxb("girth")*(-(2.0*maxb("circumference"))-(minb("maxdeg"))+maxb("nodes")+2.0)-(4.0))/maxb("girth"), ind='Max')
            except:
                pass
            try:
                set("circumference",  (-(maxb("girth")*minb("maxdeg"))+maxb("girth")*maxb("nodes")-(maxb("girth")*minb("numOfComponents"))+2.0*maxb("girth")-(4.0))/(2.0*(maxb("girth")-(3.0))), ind='Max')
            except:
                pass
            try:
                set("girth",  2.0*(3.0*maxb("circumference")-(2.0))/(2.0*maxb("circumference")+minb("maxdeg")-(maxb("nodes"))+minb("numOfComponents")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem384(Theorem):
    def __init__(self):
        super(Theorem384, self).__init__(384, "nodeCover <= (2.0*nodes+edges-(edgeInd))/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","edges","edgeInd"]
    def run(self):
        try:
            set("nodeCover",  (2.0*maxb("nodes")+maxb("edges")-(minb("edgeInd")))/4.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("edgeInd")/2.0-(maxb("edges")/2.0)+2.0*minb("nodeCover"), ind='Min')
        except:
            pass
        try:
            set("edges",  minb("edgeInd")+4.0*minb("nodeCover")-(2.0*maxb("nodes")), ind='Min')
        except:
            pass
        try:
            set("edgeInd",  maxb("edges")-(4.0*minb("nodeCover"))+2.0*maxb("nodes"), ind='Max')
        except:
            pass
        return

class Theorem385(Theorem):
    def __init__(self):
        super(Theorem385, self).__init__(385, "if genus <= nodes*(sqrt(2.0*nodes)-(7.0))/12.0+1.0 then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","nodes","edgeCliqueCover","nodeCover","nodeInd"]
    def run(self):
        if maxb("genus") <= minb("nodes")*(sqrt(2.0*minb("nodes"))-(7.0))/12.0+1.0:
            try:
                set("edgeCliqueCover",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("edgeCliqueCover")/maxb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  minb("edgeCliqueCover")/maxb("nodeCover"), ind='Min')
            except:
                pass
        
        return

class Theorem386(Theorem):
    def __init__(self):
        super(Theorem386, self).__init__(386, "if mindeg >= 2.0 then \n{\n    domination >= (girth+2.0)/3.0*numOfComponents\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","domination","girth","numOfComponents"]
    def run(self):
        if minb("mindeg") >= 2.0:
            try:
                set("domination",  (minb("girth")+2.0)/3.0*minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("girth",  3.0*maxb("domination")/minb("numOfComponents")-(2.0), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  3.0*maxb("domination")/(minb("girth")+2.0), ind='Max')
            except:
                pass
        
        return

class Theorem387(Theorem):
    def __init__(self):
        super(Theorem387, self).__init__(387, "if mindeg >= 2.0 and girth >= 5.0 then \n{\n    domination <= (nodes-(girth/3.0)-((g-(4.0))*(mindeg-(2.0))*(mindeg-(3.0))/2.0)-(2.0*(mindeg-(2.0)))+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","domination","nodes","g"]
    def run(self):
        if minb("mindeg") >= 2.0 and minb("girth") >= 5.0:
            try:
                set("domination",  (maxb("nodes")-(minb("girth")/3.0)-((minb("g")-(4.0))*(minb("mindeg")-(2.0))*(minb("mindeg")-(3.0))/2.0)-(2.0*(minb("mindeg")-(2.0)))+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("domination")+minb("g")*maxb("mindeg")**2.0/2.0-(5.0*minb("g")*maxb("mindeg")/2.0)+3.0*minb("g")+minb("girth")/3.0-(2.0*maxb("mindeg")**2.0)+12.0*maxb("mindeg")-(17.0), ind='Min')
            except:
                pass
            try:
                set("girth",  -(6.0*minb("domination"))-(3.0*maxb("g")*minb("mindeg")**2.0/2.0)+15.0*maxb("g")*minb("mindeg")/2.0-(9.0*maxb("g"))+6.0*minb("mindeg")**2.0-(36.0*minb("mindeg"))+3.0*maxb("nodes")+51.0, ind='Max')
            except:
                pass
            try:
                set("g",  2.0*(-(6.0*minb("domination"))-(minb("girth"))+6.0*minb("mindeg")**2.0-(36.0*minb("mindeg"))+3.0*maxb("nodes")+51.0)/(3.0*(minb("mindeg")**2.0-(5.0*minb("mindeg"))+6.0)), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (5.0*maxb("g")/2.0+sqrt(-(144.0*maxb("domination")*maxb("g"))+576.0*maxb("domination")+9.0*maxb("g")**2.0-(24.0*maxb("g")*maxb("girth"))+72.0*maxb("g")*maxb("nodes")-(72.0*maxb("g"))+96.0*maxb("girth")-(288.0*maxb("nodes"))+288.0)/6.0-(12.0))/(maxb("g")-(4.0)), ind='Max')
            except:
                pass
        
        return

class Theorem388(Theorem):
    def __init__(self):
        super(Theorem388, self).__init__(388, "if mindeg >= 2.0 and girth >= 9.0 then \n{\n    domination <= (nodes-(girth/3.0)-((girth-(4.0))*(mindeg-(2.0))*(mindeg-(3.0))/2.0)+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","domination","nodes"]
    def run(self):
        if minb("mindeg") >= 2.0 and minb("girth") >= 9.0:
            try:
                set("domination",  (maxb("nodes")-(minb("girth")/3.0)-((minb("girth")-(4.0))*(minb("mindeg")-(2.0))*(minb("mindeg")-(3.0))/2.0)+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("domination")+minb("girth")*maxb("mindeg")**2.0/2.0-(5.0*minb("girth")*maxb("mindeg")/2.0)+10.0*minb("girth")/3.0-(2.0*maxb("mindeg")**2.0)+10.0*maxb("mindeg")-(13.0), ind='Min')
            except:
                pass
            try:
                set("girth",  6.0*(-(2.0*minb("domination"))+2.0*minb("mindeg")**2.0-(10.0*minb("mindeg"))+maxb("nodes")+13.0)/(3.0*minb("mindeg")**2.0-(15.0*minb("mindeg"))+20.0), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (5.0*maxb("girth")/2.0+sqrt(-(144.0*maxb("domination")*maxb("girth"))+576.0*maxb("domination")-(15.0*maxb("girth")**2.0)+72.0*maxb("girth")*maxb("nodes")+96.0*maxb("girth")-(288.0*maxb("nodes"))-(144.0))/6.0-(10.0))/(maxb("girth")-(4.0)), ind='Max')
            except:
                pass
        
        return

class Theorem389(Theorem):
    def __init__(self):
        super(Theorem389, self).__init__(389, "if maxdeg >= 6.0 and maxClique <= maxdeg-(1.0) then \n{\n    nodes <= maxdeg*nodeInd-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","maxClique","nodes","nodeInd"]
    def run(self):
        if minb("maxdeg") >= 6.0 and maxb("maxClique") <= minb("maxdeg")-(1.0):
            try:
                set("nodes",  maxb("maxdeg")*maxb("nodeInd")-(1.0), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  (minb("nodes")+1.0)/maxb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  (minb("nodes")+1.0)/maxb("maxdeg"), ind='Min')
            except:
                pass
        
        return

class Theorem390(Theorem):
    def __init__(self):
        super(Theorem390, self).__init__(390, "if (nodes > 5.0 or nodes < 5.0) or (edges > 5.0 or edges < 5.0) or not cycle then \n{\n    if maxClique > nodeInd then \n    {\n        maxClique >= (1.0/2.0)*log(2.0*nodes*sqrt(3.14159265359879), 2.0)\n    \n    } else  \n    {\n        nodeInd >= (1.0/2.0)*log(2.0*nodes*sqrt(3.14159265359879), 2.0)\n    \n    }\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","cycle","maxClique","nodeInd"]
    def run(self):
        if (minb("nodes") > 5.0 or maxb("nodes") < 5.0) or (minb("edges") > 5.0 or maxb("edges") < 5.0) or get("cycle") == False :
            if minb("maxClique") > maxb("nodeInd"):
                try:
                    set("maxClique",  (1.0/2.0)*log(2.0*minb("nodes")*sqrt(3.14159265359879), 2.0), ind='Min')
                except:
                    pass
                try:
                    set("nodes",  0.282094791773474*exp(1.38629436111989*maxb("maxClique")), ind='Max')
                except:
                    pass
            
            elif True:
                try:
                    set("nodeInd",  (1.0/2.0)*log(2.0*minb("nodes")*sqrt(3.14159265359879), 2.0), ind='Min')
                except:
                    pass
                try:
                    set("nodes",  0.282094791773474*exp(1.38629436111989*maxb("nodeInd")), ind='Max')
                except:
                    pass
            
        
        return

class Theorem391(Theorem):
    def __init__(self):
        super(Theorem391, self).__init__(391, "if circumference <= nodes-(mindeg) then \n{\n    edges <= nodes*(nodes-(1.0))/2.0-(mindeg*(nodes-(mindeg)-(1.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","nodes","mindeg","edges"]
    def run(self):
        if maxb("circumference") <= minb("nodes")-(maxb("mindeg")):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/2.0-(minb("mindeg")*(maxb("nodes")-(minb("mindeg"))-(1.0))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("mindeg")+sqrt(8.0*minb("edges")-(4.0*minb("mindeg")**2.0)-(4.0*minb("mindeg"))+1.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("nodes")/2.0+sqrt(4.0*maxb("edges")-(maxb("nodes")**2.0)+1.0)/2.0-(1.0/2.0), ind='Max')
            except:
                pass
        
        return

class Theorem392(Theorem):
    def __init__(self):
        super(Theorem392, self).__init__(392, "if girth == 5.0 and mindeg >= 6.0 then \n{\n    nodes >= 40.0\n\n} else if girth == 5.0 and mindeg == 5.0 then \n{\n    nodes >= 5.0\n\n} else if girth == 5.0 and mindeg == 4.0 then \n{\n    nodes >= 19.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodes"]
    def run(self):
        if minb("girth") >= 5.0 and maxb("girth") <= 5.0 and minb("mindeg") >= 6.0:
            try:
                set("nodes",  40.0, ind='Min')
            except:
                pass
        
        elif minb("girth") >= 5.0 and maxb("girth") <= 5.0 and minb("mindeg") >= 5.0 and maxb("mindeg") <= 5.0:
            try:
                set("nodes",  5.0, ind='Min')
            except:
                pass
        
        elif minb("girth") >= 5.0 and maxb("girth") <= 5.0 and minb("mindeg") >= 4.0 and maxb("mindeg") <= 4.0:
            try:
                set("nodes",  19.0, ind='Min')
            except:
                pass
        
        return

class Theorem393(Theorem):
    def __init__(self):
        super(Theorem393, self).__init__(393, "if girth == 6.0 and mindeg >= 7.0 and regular then \n{\n    nodes >= 90.0\n\n} else if girth == 6.0 and mindeg >= 7.0 and not regular then \n{\n    nodes >= 93.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","regular","nodes"]
    def run(self):
        if minb("girth") >= 6.0 and maxb("girth") <= 6.0 and minb("mindeg") >= 7.0 and get("regular") == True :
            try:
                set("nodes",  90.0, ind='Min')
            except:
                pass
        
        elif minb("girth") >= 6.0 and maxb("girth") <= 6.0 and minb("mindeg") >= 7.0 and get("regular") == False :
            try:
                set("nodes",  93.0, ind='Min')
            except:
                pass
        
        return

class Theorem394(Theorem):
    def __init__(self):
        super(Theorem394, self).__init__(394, "if maxClique == 2.0 then \n{\n    nodeInd >= nodes*(2.0*edges/nodes*ln(2.0*edges/nodes)-(2.0*edges/nodes)+1.0)/((2.0*edges/nodes-(1.0))**2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeInd","nodes","edges"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("nodeInd",  maxb("nodes")*(2.0*maxb("edges")/maxb("nodes")*ln(2.0*maxb("edges")/maxb("nodes"))-(2.0*maxb("edges")/maxb("nodes"))+1.0)/((2.0*maxb("edges")/maxb("nodes")-(1.0))**2.0), ind='Min')
            except:
                pass
        
        return

class Theorem395(Theorem):
    def __init__(self):
        super(Theorem395, self).__init__(395, "let k = (1.0+(-(1.0))**girth)/2.0;let t = floor(girth/2.0);if connected and not tree and mindeg == 1.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg-(k*(mindeg-(1.0))**t))\n\n} else if connected and not tree and mindeg == 2.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg*t-(k*(mindeg-(1.0))**t))\n\n} else if connected and not tree and mindeg >= 3.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg*(((mindeg-(1.0))**t-(1.0))/(mindeg-(2.0)))-(k*(mindeg-(1.0))**t))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","tree","mindeg","nodes","diameter","girth"]
    def run(self):
        if get("connected") == True  and get("tree") == False  and minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0:
            try:
                set("nodes",  ceil((minb("diameter")+1.0)/(maxb("girth")+(1.0+(-(1.0))**maxb("girth"))/2.0))*(1.0+maxb("mindeg")-((1.0+(-(1.0))**maxb("girth"))/2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))), ind='Min')
            except:
                pass
        
        elif get("connected") == True  and get("tree") == False  and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0:
            try:
                set("nodes",  ceil((minb("diameter")+1.0)/(minb("girth")+(1.0+(-(1.0))**minb("girth"))/2.0))*(1.0+maxb("mindeg")*floor(minb("girth")/2.0)-((1.0+(-(1.0))**minb("girth"))/2.0*(maxb("mindeg")-(1.0))**floor(minb("girth")/2.0))), ind='Min')
            except:
                pass
        
        elif get("connected") == True  and get("tree") == False  and minb("mindeg") >= 3.0:
            try:
                set("nodes",  ceil((minb("diameter")+1.0)/(minb("girth")+(1.0+(-(1.0))**minb("girth"))/2.0))*(1.0+minb("mindeg")*(((minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(1.0))/(minb("mindeg")-(2.0)))-((1.0+(-(1.0))**minb("girth"))/2.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))), ind='Min')
            except:
                pass
        
        return

class Theorem396(Theorem):
    def __init__(self):
        super(Theorem396, self).__init__(396, "let t = floor(girth/2.0);if not forest and mindeg == 1.0 and odd girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(1.0-((mindeg-(1.0))**(t-(1.0))/2.0)))+nodes/2.0\n\n} else if not forest and mindeg == 1.0 and even girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(1.0-((mindeg-(1.0))**(t-(1.0)))))+nodes/2.0\n\n} else if not forest and mindeg == 2.0 and odd girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(t-((mindeg-(1.0))**(t-(1.0))/2.0)))+nodes/2.0\n\n} else if not forest and mindeg == 2.0 and even girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(t-((mindeg-(1.0))**(t-(1.0)))))+nodes/2.0\n\n} else if not forest and mindeg == 3.0 and odd girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(((mindeg-(1.0))**t-(1.0))/(mindeg-(2.0))-((mindeg-(1.0))**(t-(1.0))/2.0)))+nodes/2.0\n\n} else if not forest and mindeg == 3.0 and even girth then \n{\n    edges <= nodes*(nodes-(1.0))/(4.0*(((mindeg-(1.0))**t-(1.0))/(mindeg-(2.0))-((mindeg-(1.0))**(t-(1.0)))))+nodes/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","mindeg","girth","edges","nodes"]
    def run(self):
        if get("forest") == False  and minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0 and oddInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(1.0-((maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0))/2.0)))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (-(minb("mindeg"))+(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+sqrt(16.0*minb("edges")*minb("mindeg")**2.0-(8.0*minb("edges")*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))-(32.0*minb("edges")*minb("mindeg"))+8.0*minb("edges")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+16.0*minb("edges")+minb("mindeg")**2.0-(2.0*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))-(2.0*minb("mindeg"))+(minb("mindeg")-(1.0))**(2.0*floor(minb("girth")/2.0))+2.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+1.0)+1.0)/(2.0*(minb("mindeg")-(1.0))), ind='Min')
            except:
                pass
            try:
                set("mindeg",  ((4.0*minb("edges")-(maxb("nodes")**2.0)-(maxb("nodes")))/(2.0*minb("edges")-(maxb("nodes"))))**(1.0/(floor(maxb("girth")/2.0)-(1.0)))+1.0, ind='Min')
            except:
                pass
        
        elif get("forest") == False  and minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0 and evenInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(1.0-((maxb("mindeg")-(1.0))**(floor(maxb("girth")/2.0)-(1.0)))))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (-(minb("mindeg"))+2.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+sqrt(16.0*minb("edges")*minb("mindeg")**2.0-(16.0*minb("edges")*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))-(32.0*minb("edges")*minb("mindeg"))+16.0*minb("edges")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+16.0*minb("edges")+minb("mindeg")**2.0-(4.0*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))-(2.0*minb("mindeg"))+4.0*(minb("mindeg")-(1.0))**(2.0*floor(minb("girth")/2.0))+4.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+1.0)+1.0)/(2.0*(minb("mindeg")-(1.0))), ind='Min')
            except:
                pass
            try:
                set("mindeg",  ((4.0*minb("edges")-(maxb("nodes")**2.0)-(maxb("nodes")))/(2.0*(2.0*minb("edges")-(maxb("nodes")))))**(1.0/(floor(maxb("girth")/2.0)-(1.0)))+1.0, ind='Min')
            except:
                pass
        
        elif get("forest") == False  and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and oddInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(floor(minb("girth")/2.0)-((maxb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0))/2.0)))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (-(2.0*floor(minb("girth")/2.0)*minb("mindeg"))+2.0*floor(minb("girth")/2.0)+minb("mindeg")+(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+sqrt(4.0*floor(minb("girth")/2.0)**2.0*minb("mindeg")**2.0-(8.0*floor(minb("girth")/2.0)**2.0*minb("mindeg"))+4.0*floor(minb("girth")/2.0)**2.0+16.0*floor(minb("girth")/2.0)*minb("edges")*minb("mindeg")**2.0-(32.0*floor(minb("girth")/2.0)*minb("edges")*minb("mindeg"))+16.0*floor(minb("girth")/2.0)*minb("edges")-(4.0*floor(minb("girth")/2.0)*minb("mindeg")**2.0)-(4.0*floor(minb("girth")/2.0)*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+8.0*floor(minb("girth")/2.0)*minb("mindeg")+4.0*floor(minb("girth")/2.0)*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(4.0*floor(minb("girth")/2.0))-(8.0*minb("edges")*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+8.0*minb("edges")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+minb("mindeg")**2.0+2.0*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(2.0*minb("mindeg"))+(minb("mindeg")-(1.0))**(2.0*floor(minb("girth")/2.0))-(2.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+1.0)-(1.0))/(2.0*(minb("mindeg")-(1.0))), ind='Min')
            except:
                pass
        
        elif get("forest") == False  and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and evenInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(floor(minb("girth")/2.0)-((maxb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0)))))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (-(floor(minb("girth")/2.0)*minb("mindeg"))+floor(minb("girth")/2.0)+minb("mindeg")/2.0+(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+sqrt(4.0*floor(minb("girth")/2.0)**2.0*minb("mindeg")**2.0-(8.0*floor(minb("girth")/2.0)**2.0*minb("mindeg"))+4.0*floor(minb("girth")/2.0)**2.0+16.0*floor(minb("girth")/2.0)*minb("edges")*minb("mindeg")**2.0-(32.0*floor(minb("girth")/2.0)*minb("edges")*minb("mindeg"))+16.0*floor(minb("girth")/2.0)*minb("edges")-(4.0*floor(minb("girth")/2.0)*minb("mindeg")**2.0)-(8.0*floor(minb("girth")/2.0)*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+8.0*floor(minb("girth")/2.0)*minb("mindeg")+8.0*floor(minb("girth")/2.0)*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(4.0*floor(minb("girth")/2.0))-(16.0*minb("edges")*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+16.0*minb("edges")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)+minb("mindeg")**2.0+4.0*minb("mindeg")*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(2.0*minb("mindeg"))+4.0*(minb("mindeg")-(1.0))**(2.0*floor(minb("girth")/2.0))-(4.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))+1.0)/2.0-(1.0/2.0))/(minb("mindeg")-(1.0)), ind='Min')
            except:
                pass
        
        elif get("forest") == False  and minb("mindeg") >= 3.0 and maxb("mindeg") <= 3.0 and oddInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(((minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(1.0))/(minb("mindeg")-(2.0))-((minb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0))/2.0)))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (maxb("mindeg")**2.0-(maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))-(maxb("mindeg"))+sqrt(8.0*minb("edges")*maxb("mindeg")**3.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(16.0*minb("edges")*maxb("mindeg")**3.0)-(24.0*minb("edges")*maxb("mindeg")**2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))+64.0*minb("edges")*maxb("mindeg")**2.0+16.0*minb("edges")*maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(80.0*minb("edges")*maxb("mindeg"))+32.0*minb("edges")+maxb("mindeg")**4.0-(2.0*maxb("mindeg")**3.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))-(2.0*maxb("mindeg")**3.0)+maxb("mindeg")**2.0*(maxb("mindeg")-(1.0))**(2.0*floor(maxb("girth")/2.0))+2.0*maxb("mindeg")**2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)+maxb("mindeg")**2.0))/(2.0*maxb("mindeg")**2.0-(6.0*maxb("mindeg"))+4.0), ind='Min')
            except:
                pass
        
        elif get("forest") == False  and minb("mindeg") >= 3.0 and maxb("mindeg") <= 3.0 and evenInvar("girth"):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/(4.0*(((minb("mindeg")-(1.0))**floor(minb("girth")/2.0)-(1.0))/(minb("mindeg")-(2.0))-((minb("mindeg")-(1.0))**(floor(minb("girth")/2.0)-(1.0)))))+maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  (maxb("mindeg")**2.0-(maxb("mindeg"))-(2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))+sqrt(-(16.0*minb("edges")*maxb("mindeg")**3.0)+16.0*minb("edges")*maxb("mindeg")**2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)+64.0*minb("edges")*maxb("mindeg")**2.0-(48.0*minb("edges")*maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))-(80.0*minb("edges")*maxb("mindeg"))+32.0*minb("edges")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)+32.0*minb("edges")+maxb("mindeg")**4.0-(2.0*maxb("mindeg")**3.0)-(4.0*maxb("mindeg")**2.0*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0))+maxb("mindeg")**2.0+4.0*maxb("mindeg")*(maxb("mindeg")-(1.0))**floor(maxb("girth")/2.0)+4.0*(maxb("mindeg")-(1.0))**(2.0*floor(maxb("girth")/2.0))))/(2.0*maxb("mindeg")**2.0-(6.0*maxb("mindeg"))+4.0), ind='Min')
            except:
                pass
        
        return

class Theorem397(Theorem):
    def __init__(self):
        super(Theorem397, self).__init__(397, "if girth >= 5.0+log(max(1.0, genus), 3.0) then \n{\n    arboricity <= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","genus","arboricity"]
    def run(self):
        if minb("girth") >= 5.0+log(max(1.0, maxb("genus")), 3.0):
            try:
                set("arboricity",  2.0, ind='Max')
            except:
                pass
        
        return

class Theorem398(Theorem):
    def __init__(self):
        super(Theorem398, self).__init__(398, "if mindeg >= 2.0 then \n{\n    nodes >= girth*numOfComponents+maxdeg-(2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","girth","numOfComponents","maxdeg"]
    def run(self):
        if minb("mindeg") >= 2.0:
            try:
                set("nodes",  minb("girth")*minb("numOfComponents")+minb("maxdeg")-(2.0), ind='Min')
            except:
                pass
            try:
                set("girth",  (-(minb("maxdeg"))+maxb("nodes")+2.0)/minb("numOfComponents"), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  (-(minb("maxdeg"))+maxb("nodes")+2.0)/minb("girth"), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(minb("girth")*minb("numOfComponents"))+maxb("nodes")+2.0, ind='Max')
            except:
                pass
        
        return

class Theorem399(Theorem):
    def __init__(self):
        super(Theorem399, self).__init__(399, "if nodeConnec > 0.0 then \n{\n    nodeConnec >= (nodes*(maxdeg-(2.0)))/((maxdeg-(1.0))**diam+maxdeg-(3.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","maxdeg","diam"]
    def run(self):
        if minb("nodeConnec") > 0.0:
            try:
                set("nodeConnec",  (minb("nodes")*(minb("maxdeg")-(2.0)))/((minb("maxdeg")-(1.0))**maxb("diam")+minb("maxdeg")-(3.0)), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("nodeConnec")*(maxb("maxdeg")+(maxb("maxdeg")-(1.0))**maxb("diam")-(3.0))/(maxb("maxdeg")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem400(Theorem):
    def __init__(self):
        super(Theorem400, self).__init__(400, "if diameter == 2.0 and (maxdeg >= (2.0*nodes-(2.0))/3.0 and maxdeg < nodes-(4.0) or maxdeg == nodes-(2.0)) then \n{\n    edges >= 2.0*nodes-(4.0)\n\n} else if diameter == 2.0 and (maxdeg >= (3.0*nodes-(5.0))/5.0 and maxdeg < (2.0*nodes-(2.0))/3.0) then \n{\n    edges >= 3.0*nodes-(maxdeg)-(6.0)\n\n} else if diameter == 2.0 and (maxdeg >= (5.0*nodes-(3.0))/9.0 and maxdeg < (3.0*nodes-(5.0))/5.0) then \n{\n    edges >= 5.0*nodes-(4.0*maxdeg)-(10.0)\n\n} else if diameter == 2.0 and (maxdeg >= (nodes+1.0)/2.0 and maxdeg < (5.0*nodes-(3.0))/9.0) then \n{\n    edges >= 4.0*nodes-(2.0*maxdeg)-(13.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","edges"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and (minb("maxdeg") >= (2.0*maxb("nodes")-(2.0))/3.0 and maxb("maxdeg") < minb("nodes")-(4.0) or minb("maxdeg") >= maxb("nodes")-(2.0) and maxb("maxdeg") <= minb("nodes")-(2.0)):
            try:
                set("edges",  2.0*minb("nodes")-(4.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/2.0+2.0, ind='Max')
            except:
                pass
        
        elif minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and (minb("maxdeg") >= (3.0*maxb("nodes")-(5.0))/5.0 and maxb("maxdeg") < (2.0*minb("nodes")-(2.0))/3.0):
            try:
                set("edges",  3.0*minb("nodes")-(maxb("maxdeg"))-(6.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/3.0+maxb("maxdeg")/3.0+2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(maxb("edges"))+3.0*minb("nodes")-(6.0), ind='Min')
            except:
                pass
        
        elif minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and (minb("maxdeg") >= (5.0*maxb("nodes")-(3.0))/9.0 and maxb("maxdeg") < (3.0*minb("nodes")-(5.0))/5.0):
            try:
                set("edges",  5.0*minb("nodes")-(4.0*maxb("maxdeg"))-(10.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/5.0+4.0*maxb("maxdeg")/5.0+2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(maxb("edges")/4.0)+5.0*minb("nodes")/4.0-(5.0/2.0), ind='Min')
            except:
                pass
        
        elif minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and (minb("maxdeg") >= (maxb("nodes")+1.0)/2.0 and maxb("maxdeg") < (5.0*minb("nodes")-(3.0))/9.0):
            try:
                set("edges",  4.0*minb("nodes")-(2.0*maxb("maxdeg"))-(13.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/4.0+maxb("maxdeg")/2.0+13.0/4.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  -(maxb("edges")/2.0)+2.0*minb("nodes")-(13.0/2.0), ind='Min')
            except:
                pass
        
        return

