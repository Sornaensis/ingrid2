class Theorem361(Theorem):
    def __init__(self):
        super(Theorem361, self).__init__(361, "let t = floor((girth-(1.0))/2.0);if g >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeInd >= maxdeg*floor((t+1.0)/2.0)+1.0\n\n} else if g >= 4.0 and mindeg == 2.0 and odd t then \n{\n    nodeInd >= maxdeg*floor((t+1.0)/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["g","mindeg","girth","nodeInd","maxdeg"]
    def run(self):
        if minb("g") >= 4.0 and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and evenInvar(floor(("girth"-(1.0))/2.0)):
            try:
                set("nodeInd",  minb("maxdeg")*floor((floor((minb("girth")-(1.0))/2.0)+1.0)/2.0)+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (maxb("nodeInd")-(1.0))/floor((floor((minb("girth")-(1.0))/2.0)+1.0)/2.0), ind='Max')
            except:
                pass
        
        elif minb("g") >= 4.0 and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0 and oddInvar(floor(("girth"-(1.0))/2.0)):
            try:
                set("nodeInd",  minb("maxdeg")*floor((floor((minb("girth")-(1.0))/2.0)+1.0)/2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodeInd")/floor((floor((minb("girth")-(1.0))/2.0)+1.0)/2.0), ind='Max')
            except:
                pass
        
        return

class Theorem362(Theorem):
    def __init__(self):
        super(Theorem362, self).__init__(362, "let t = (girth-(1.0))/2.0;if girth >= 4.0 and mindeg >= 3.0 and odd t then \n{\n    nodeInd >= maxdeg*((mindeg-(1.0))**(t+1.0)-(1.0))/(mindeg*(mindeg-(2.0)))\n\n} else if girth >= 4.0 and mindeg >= 3.0 and even t then \n{\n    nodeInd >= maxdeg*(mindeg-(1.0))*((mindeg-(1.0))**t-(1.0))/(mindeg*(mindeg-(2.0)))+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodeInd","maxdeg"]
    def run(self):
        if minb("girth") >= 4.0 and minb("mindeg") >= 3.0 and oddInvar(("girth"-(1.0))/2.0):
            try:
                set("nodeInd",  minb("maxdeg")*((minb("mindeg")-(1.0))**((minb("girth")-(1.0))/2.0+1.0)-(1.0))/(minb("mindeg")*(minb("mindeg")-(2.0))), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  minb("mindeg")*maxb("nodeInd")*(minb("mindeg")-(2.0))/((minb("mindeg")-(1.0))**(minb("girth")/2.0+1.0/2.0)-(1.0)), ind='Max')
            except:
                pass
        
        elif minb("girth") >= 4.0 and minb("mindeg") >= 3.0 and evenInvar(("girth"-(1.0))/2.0):
            try:
                set("nodeInd",  minb("maxdeg")*(minb("mindeg")-(1.0))*((minb("mindeg")-(1.0))**(minb("girth")-(1.0))/2.0-(1.0))/(minb("mindeg")*(minb("mindeg")-(2.0)))+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  2.0*maxb("mindeg")*(maxb("mindeg")*maxb("nodeInd")-(maxb("mindeg"))-(2.0*maxb("nodeInd"))+2.0)/(-(2.0*maxb("mindeg"))+(maxb("mindeg")-(1.0))**minb("girth")+2.0), ind='Max')
            except:
                pass
        
        return

class Theorem363(Theorem):
    def __init__(self):
        super(Theorem363, self).__init__(363, "if diameter == 2.0 and nodeConnec >= 3.0 then \n{\n    edges >= (nodes-(1.0))*(nodeConnec+1.0)/(2.0-(nodeConnec**2.0)+2.0*nodeConnec)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","edges","nodes"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and minb("nodeConnec") >= 3.0:
            try:
                set("edges",  (minb("nodes")-(1.0))*(minb("nodeConnec")+1.0)/(2.0-(minb("nodeConnec")**2.0)+2.0*minb("nodeConnec")), ind='Min')
            except:
                pass
            try:
                set("nodes",  (-(maxb("edges")*minb("nodeConnec")**2.0)+2.0*maxb("edges")*minb("nodeConnec")+2.0*maxb("edges")+minb("nodeConnec")+1.0)/(minb("nodeConnec")+1.0), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  (2.0*maxb("edges")-(minb("nodes"))+sqrt((2.0*maxb("edges")-(minb("nodes"))+1.0)*(6.0*maxb("edges")-(minb("nodes"))+1.0))+1.0)/(2.0*maxb("edges")), ind='Max')
            except:
                pass
        
        return

class Theorem364(Theorem):
    def __init__(self):
        super(Theorem364, self).__init__(364, "if diameter == 2.0 and nodeConnec >= 3.0 and nodes >= 3.0*nodeConnec**2.0+6.0 then \n{\n    edges >= (nodes-(1.0))*(nodeConnec+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","nodes","edges"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and minb("nodeConnec") >= 3.0 and minb("nodes") >= 3.0*maxb("nodeConnec")**2.0+6.0:
            try:
                set("edges",  (minb("nodes")-(1.0))*(minb("nodeConnec")+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (2.0*maxb("edges")+maxb("nodeConnec")+1.0)/(maxb("nodeConnec")+1.0), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  (2.0*maxb("edges")-(minb("nodes"))+1.0)/(minb("nodes")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem365(Theorem):
    def __init__(self):
        super(Theorem365, self).__init__(365, "if bipartite then \n{\n    if odd nodes then \n    {\n        crossing <= (nodes/4.0)**2.0*((nodes-(2.0))/4.0)**2.0\n    \n    } else  \n    {\n        crossing <= ((nodes+1.0)/4.0)*((nodes-(1.0))/4.0)**2.0*(nodes-(3.0))/4.0\n    \n    }\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","crossing"]
    def run(self):
        if get("bipartite") == True :
            if oddInvar("nodes"):
                try:
                    set("crossing",  (maxb("nodes")/4.0)**2.0*((maxb("nodes")-(2.0))/4.0)**2.0, ind='Max')
                except:
                    pass
                try:
                    set("nodes",  sqrt(16.0*sqrt(minb("crossing"))+1.0)+1.0, ind='Min')
                except:
                    pass
            
            elif True:
                try:
                    set("crossing",  ((maxb("nodes")+1.0)/4.0)*((maxb("nodes")-(1.0))/4.0)**2.0*(maxb("nodes")-(3.0))/4.0, ind='Max')
                except:
                    pass
                try:
                    set("nodes",  sqrt(2.0)*sqrt(sqrt(64.0*minb("crossing")+1.0)+1.0)+1.0, ind='Min')
                except:
                    pass
            
        
        return

class Theorem366(Theorem):
    def __init__(self):
        super(Theorem366, self).__init__(366, "if connected then \n{\n    spectralRadius >= 2.0*cos(3.14159265358979/(nodes+1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","spectralRadius","nodes"]
    def run(self):
        if get("connected") == True :
            try:
                set("spectralRadius",  2.0*cos(3.14159265358979/(maxb("nodes")+1.0)), ind='Min')
            except:
                pass
            try:
                set("nodes",  -(1.0)+3.14159265358979/acos(0.5*maxb("spectralRadius")), ind='Min')
            except:
                pass
        
        return

class Theorem367(Theorem):
    def __init__(self):
        super(Theorem367, self).__init__(367, "if regular and mindeg >= 7.0 and odd mindeg and (mindeg > 9.0 or mindeg < 9.0) and not bipartite and girth == 4.0 then \n{\n    nodes >= 2.0*(5.0*mindeg/4.0)+4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","bipartite","girth","nodes"]
    def run(self):
        if get("regular") == True  and minb("mindeg") >= 7.0 and oddInvar("mindeg") and (minb("mindeg") > 9.0 or maxb("mindeg") < 9.0) and get("bipartite") == False  and minb("girth") >= 4.0 and maxb("girth") <= 4.0:
            try:
                set("nodes",  2.0*(5.0*minb("mindeg")/4.0)+4.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0*maxb("nodes")/5.0-(8.0/5.0), ind='Max')
            except:
                pass
        
        return

class Theorem368(Theorem):
    def __init__(self):
        super(Theorem368, self).__init__(368, "if bipartite then \n{\n    thickness <= nodes/8.0+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","thickness","nodes"]
    def run(self):
        if get("bipartite") == True :
            try:
                set("thickness",  maxb("nodes")/8.0+2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  8.0*minb("thickness")-(16.0), ind='Min')
            except:
                pass
        
        return

class Theorem369(Theorem):
    def __init__(self):
        super(Theorem369, self).__init__(369, "if maxClique <= 2.0 then \n{\n    thickness <= genus+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","thickness","genus"]
    def run(self):
        if maxb("maxClique") <= 2.0:
            try:
                set("thickness",  maxb("genus")+1.0, ind='Max')
            except:
                pass
            try:
                set("genus",  minb("thickness")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem370(Theorem):
    def __init__(self):
        super(Theorem370, self).__init__(370, "if genus <= 1.0 then \n{\n    thickness == genus+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","thickness"]
    def run(self):
        if maxb("genus") <= 1.0:
            try:
                set("thickness",  minb("genus")+1.0, ind='Min')
            except:
                pass
            try:
                set("genus",  maxb("thickness")-(1.0), ind='Max')
            except:
                pass
            try:
                set("thickness",  maxb("genus")+1.0, ind='Max')
            except:
                pass
            try:
                set("genus",  minb("thickness")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem371(Theorem):
    def __init__(self):
        super(Theorem371, self).__init__(371, "arboricity <= edgeCover;", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","edgeCover"]
    def run(self):
        try:
            set("arboricity",  maxb("edgeCover"), ind='Max')
        except:
            pass
        try:
            set("edgeCover",  minb("arboricity"), ind='Min')
        except:
            pass
        return

class Theorem372(Theorem):
    def __init__(self):
        super(Theorem372, self).__init__(372, "thickness <= edgeCover;", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","edgeCover"]
    def run(self):
        try:
            set("thickness",  maxb("edgeCover"), ind='Max')
        except:
            pass
        try:
            set("edgeCover",  minb("thickness"), ind='Min')
        except:
            pass
        return

class Theorem373(Theorem):
    def __init__(self):
        super(Theorem373, self).__init__(373, "if genus >= 1.0 then \n{\n    edgeCover <= 2.0+sqrt(3.0*genus)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","edgeCover"]
    def run(self):
        if minb("genus") >= 1.0:
            try:
                set("edgeCover",  2.0+sqrt(3.0*maxb("genus")), ind='Max')
            except:
                pass
            try:
                set("genus",  1.0*(0.577350269189626*minb("edgeCover")-(1.15470053837925))**2.0, ind='Min')
            except:
                pass
        
        return

class Theorem374(Theorem):
    def __init__(self):
        super(Theorem374, self).__init__(374, "thickness <= 5.0+sqrt(2.0*genus-(2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","genus"]
    def run(self):
        try:
            set("thickness",  5.0+sqrt(2.0*maxb("genus")-(2.0)), ind='Max')
        except:
            pass
        try:
            set("genus",  0.5*(1.0*minb("thickness")-(5.0))**2.0+1.0, ind='Min')
        except:
            pass
        return

class Theorem375(Theorem):
    def __init__(self):
        super(Theorem375, self).__init__(375, "if connected and regular then \n{\n    edgeCover <= 4.0+(6.0*genus+2.0)/(nodes-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","regular","edgeCover","genus","nodes"]
    def run(self):
        if get("connected") == True  and get("regular") == True :
            try:
                set("edgeCover",  4.0+(6.0*maxb("genus")+2.0)/(minb("nodes")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("genus",  minb("edgeCover")*minb("nodes")/6.0-(minb("edgeCover")/6.0)-(2.0*minb("nodes")/3.0)+1.0/3.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (maxb("edgeCover")+6.0*maxb("genus")-(2.0))/(maxb("edgeCover")-(4.0)), ind='Max')
            except:
                pass
        
        return

class Theorem376(Theorem):
    def __init__(self):
        super(Theorem376, self).__init__(376, "genus <= (thickness-(1.0))*(nodes-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["genus","thickness","nodes"]
    def run(self):
        try:
            set("genus",  (maxb("thickness")-(1.0))*(maxb("nodes")-(1.0)), ind='Max')
        except:
            pass
        try:
            set("thickness",  (minb("genus")+minb("nodes")-(1.0))/(minb("nodes")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("nodes",  (minb("genus")+minb("thickness")-(1.0))/(minb("thickness")-(1.0)), ind='Min')
        except:
            pass
        return

class Theorem377(Theorem):
    def __init__(self):
        super(Theorem377, self).__init__(377, "edgeCover <= (maxdeg+2.0)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","maxdeg"]
    def run(self):
        try:
            set("edgeCover",  (maxb("maxdeg")+2.0)/2.0, ind='Max')
        except:
            pass
        try:
            set("maxdeg",  2.0*minb("edgeCover")-(2.0), ind='Min')
        except:
            pass
        return

class Theorem378(Theorem):
    def __init__(self):
        super(Theorem378, self).__init__(378, "edgeCover >= (mindeg+1.0)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","mindeg"]
    def run(self):
        try:
            set("edgeCover",  (minb("mindeg")+1.0)/2.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  2.0*maxb("edgeCover")-(1.0), ind='Max')
        except:
            pass
        return

class Theorem379(Theorem):
    def __init__(self):
        super(Theorem379, self).__init__(379, "edgeCover >= edges/(nodes-(numOfComponents));", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","edges","nodes","numOfComponents"]
    def run(self):
        try:
            set("edgeCover",  minb("edges")/(maxb("nodes")-(minb("numOfComponents"))), ind='Min')
        except:
            pass
        try:
            set("edges",  maxb("edgeCover")*(maxb("nodes")-(minb("numOfComponents"))), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("numOfComponents")+minb("edges")/maxb("edgeCover"), ind='Min')
        except:
            pass
        try:
            set("numOfComponents",  maxb("nodes")-(minb("edges")/maxb("edgeCover")), ind='Max')
        except:
            pass
        return

class Theorem380(Theorem):
    def __init__(self):
        super(Theorem380, self).__init__(380, "edgeCover <= 3.0*thickness;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","thickness"]
    def run(self):
        try:
            set("edgeCover",  3.0*maxb("thickness"), ind='Max')
        except:
            pass
        try:
            set("thickness",  minb("edgeCover")/3.0, ind='Min')
        except:
            pass
        return

