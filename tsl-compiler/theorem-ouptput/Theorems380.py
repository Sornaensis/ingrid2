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

