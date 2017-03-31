class Theorem101(Theorem):
    def __init__(self):
        super(Theorem101, self).__init__(101, "if connected or odd nodes then \n{\n    nodeCover <= (nodes-(1.0))*(nodes+1.0)/2.0,\n    edgeCover <= (nodes-(1.0))*(nodes+1.0)/2.0\n\n} else  \n{\n    nodeCover <= (nodes-(2.0))*(nodes+2.0)/2.0,\n    edgeCover <= (nodes-(2.0))*(nodes+2.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodes","nodeCover","edgeCover"]
    def run(self):
        if get("connected") == True  or oddInvar("nodes"):
            try:
                set("nodeCover",  (maxb("nodes")-(1.0))*(maxb("nodes")+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*minb("nodeCover")+1.0), ind='Min')
            except:
                pass
            try:
                set("edgeCover",  (maxb("nodes")-(1.0))*(maxb("nodes")+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*minb("edgeCover")+1.0), ind='Min')
            except:
                pass
        
        elif True:
            try:
                set("nodeCover",  (maxb("nodes")-(2.0))*(maxb("nodes")+2.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*minb("nodeCover")+4.0), ind='Min')
            except:
                pass
            try:
                set("edgeCover",  (maxb("nodes")-(2.0))*(maxb("nodes")+2.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*minb("edgeCover")+4.0), ind='Min')
            except:
                pass
        
        return

class Theorem102(Theorem):
    def __init__(self):
        super(Theorem102, self).__init__(102, "edgeChromatic <= 2.0*bandwidth;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","bandwidth"]
    def run(self):
        try:
            set("edgeChromatic",  2.0*maxb("bandwidth"), ind='Max')
        except:
            pass
        try:
            set("bandwidth",  minb("edgeChromatic")/2.0, ind='Min')
        except:
            pass
        return

class Theorem103(Theorem):
    def __init__(self):
        super(Theorem103, self).__init__(103, "circumference >= maxClique*mindeg/(maxClique-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","maxClique","mindeg"]
    def run(self):
        try:
            set("circumference",  minb("maxClique")*minb("mindeg")/(minb("maxClique")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxClique",  maxb("circumference")/(maxb("circumference")-(maxb("mindeg"))), ind='Max')
        except:
            pass
        try:
            set("mindeg",  maxb("circumference")-(maxb("circumference")/maxb("maxClique")), ind='Max')
        except:
            pass
        return

class Theorem104(Theorem):
    def __init__(self):
        super(Theorem104, self).__init__(104, "circumference >= maxClique*(chromaticNum-(1.0))/(maxClique-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","maxClique","chromaticNum"]
    def run(self):
        try:
            set("circumference",  minb("maxClique")*(minb("chromaticNum")-(1.0))/(minb("maxClique")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxClique",  maxb("circumference")/(-(maxb("chromaticNum"))+maxb("circumference")+1.0), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  maxb("circumference")-(maxb("circumference")/maxb("maxClique"))+1.0, ind='Max')
        except:
            pass
        return

class Theorem105(Theorem):
    def __init__(self):
        super(Theorem105, self).__init__(105, "if maxClique == 2.0 and chromaticNum >= 3.0 then \n{\n    circumference >= 2.0*chromaticNum-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","circumference"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and minb("chromaticNum") >= 3.0:
            try:
                set("circumference",  2.0*minb("chromaticNum")-(1.0), ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  maxb("circumference")/2.0+1.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem106(Theorem):
    def __init__(self):
        super(Theorem106, self).__init__(106, "edges <= nodeCover*(nodeInd+nodeCover*(chromaticNum-(1.0))/(2.0*chromaticNum));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","nodeInd","chromaticNum"]
    def run(self):
        try:
            set("edges",  maxb("nodeCover")*(maxb("nodeInd")+maxb("nodeCover")*(maxb("chromaticNum")-(1.0))/(2.0*maxb("chromaticNum"))), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  -((maxb("chromaticNum")*maxb("nodeInd")+sqrt(maxb("chromaticNum")*(2.0*maxb("chromaticNum")*maxb("edges")+maxb("chromaticNum")*maxb("nodeInd")**2.0-(2.0*maxb("edges")))))/(maxb("chromaticNum")-(1.0))), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  minb("edges")/minb("nodeCover")-(minb("nodeCover")/2.0)+minb("nodeCover")/(2.0*maxb("chromaticNum")), ind='Min')
        except:
            pass
        try:
            set("chromaticNum",  maxb("nodeCover")**2.0/(-(2.0*minb("edges"))+maxb("nodeCover")**2.0+2.0*maxb("nodeCover")*maxb("nodeInd")), ind='Min')
        except:
            pass
        return

class Theorem107(Theorem):
    def __init__(self):
        super(Theorem107, self).__init__(107, "mindeg <= maxdeg;", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg"]
    def run(self):
        try:
            set("mindeg",  maxb("maxdeg"), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  minb("mindeg"), ind='Min')
        except:
            pass
        return

class Theorem108(Theorem):
    def __init__(self):
        super(Theorem108, self).__init__(108, "nodeCliqueCover <= (nodes+nodeInd-(maxClique)+1.0)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","nodes","nodeInd","maxClique"]
    def run(self):
        try:
            set("nodeCliqueCover",  (maxb("nodes")+maxb("nodeInd")-(minb("maxClique"))+1.0)/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("maxClique")+2.0*minb("nodeCliqueCover")-(maxb("nodeInd"))-(1.0), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  minb("maxClique")+2.0*minb("nodeCliqueCover")-(maxb("nodes"))-(1.0), ind='Min')
        except:
            pass
        try:
            set("maxClique",  -(2.0*minb("nodeCliqueCover"))+maxb("nodeInd")+maxb("nodes")+1.0, ind='Max')
        except:
            pass
        return

class Theorem109(Theorem):
    def __init__(self):
        super(Theorem109, self).__init__(109, "nodeCover <= 2.0*edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","edgeInd"]
    def run(self):
        try:
            set("nodeCover",  2.0*maxb("edgeInd"), ind='Max')
        except:
            pass
        try:
            set("edgeInd",  minb("nodeCover")/2.0, ind='Min')
        except:
            pass
        return

class Theorem110(Theorem):
    def __init__(self):
        super(Theorem110, self).__init__(110, "if mindeg >= 4.0 and girth >= 5.0 then \n{\n    circumference >= (girth-(2.0))*(mindeg-(2.0))+5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","circumference"]
    def run(self):
        if minb("mindeg") >= 4.0 and minb("girth") >= 5.0:
            try:
                set("circumference",  (minb("girth")-(2.0))*(minb("mindeg")-(2.0))+5.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (maxb("circumference")+2.0*maxb("mindeg")-(9.0))/(maxb("mindeg")-(2.0)), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (maxb("circumference")+2.0*maxb("girth")-(9.0))/(maxb("girth")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem111(Theorem):
    def __init__(self):
        super(Theorem111, self).__init__(111, "if connected then \n{\n    diameter <= 2.0*nodeInd-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","nodeInd"]
    def run(self):
        if get("connected") == True :
            try:
                set("diameter",  2.0*maxb("nodeInd")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodeInd",  minb("diameter")/2.0+1.0/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem112(Theorem):
    def __init__(self):
        super(Theorem112, self).__init__(112, "if connected and nodeInd <= mindeg then \n{\n    mindeg >= (nodes+2.0)/3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodeInd","mindeg","nodes"]
    def run(self):
        if get("connected") == True  and maxb("nodeInd") <= minb("mindeg"):
            try:
                set("mindeg",  (minb("nodes")+2.0)/3.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  3.0*maxb("mindeg")-(2.0), ind='Max')
            except:
                pass
        
        return

class Theorem113(Theorem):
    def __init__(self):
        super(Theorem113, self).__init__(113, "edges >= nodeInd*mindeg+(maxClique-(1.0))*(maxClique-(2.0))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeInd","mindeg","maxClique"]
    def run(self):
        try:
            set("edges",  minb("nodeInd")*minb("mindeg")+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/2.0, ind='Min')
        except:
            pass
        try:
            set("nodeInd",  (2.0*maxb("edges")-(minb("maxClique")**2.0)+3.0*minb("maxClique")-(2.0))/(2.0*minb("mindeg")), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (2.0*maxb("edges")-(minb("maxClique")**2.0)+3.0*minb("maxClique")-(2.0))/(2.0*minb("nodeInd")), ind='Max')
        except:
            pass
        try:
            set("maxClique",  sqrt(8.0*maxb("edges")-(8.0*minb("mindeg")*minb("nodeInd"))+1.0)/2.0+3.0/2.0, ind='Max')
        except:
            pass
        return

class Theorem114(Theorem):
    def __init__(self):
        super(Theorem114, self).__init__(114, "edges >= nodeCover+(maxClique-(1.0))*(maxClique-(2.0))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","maxClique"]
    def run(self):
        try:
            set("edges",  minb("nodeCover")+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/2.0, ind='Min')
        except:
            pass
        try:
            set("nodeCover",  maxb("edges")-(minb("maxClique")**2.0/2.0)+3.0*minb("maxClique")/2.0-(1.0), ind='Max')
        except:
            pass
        try:
            set("maxClique",  sqrt(8.0*maxb("edges")-(8.0*minb("nodeCover"))+1.0)/2.0+3.0/2.0, ind='Max')
        except:
            pass
        return

class Theorem115(Theorem):
    def __init__(self):
        super(Theorem115, self).__init__(115, "edges >= chromaticNum*(chromaticNum-(3.0))/2.0+nodes-(numOfComponents)+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","chromaticNum","nodes","numOfComponents"]
    def run(self):
        try:
            set("edges",  minb("chromaticNum")*(minb("chromaticNum")-(3.0))/2.0+minb("nodes")-(maxb("numOfComponents"))+1.0, ind='Min')
        except:
            pass
        try:
            set("chromaticNum",  sqrt(8.0*maxb("edges")-(8.0*minb("nodes"))+8.0*maxb("numOfComponents")+1.0)/2.0+3.0/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  -(minb("chromaticNum")**2.0/2.0)+3.0*minb("chromaticNum")/2.0+maxb("edges")+maxb("numOfComponents")-(1.0), ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  minb("chromaticNum")**2.0/2.0-(3.0*minb("chromaticNum")/2.0)-(maxb("edges"))+minb("nodes")+1.0, ind='Min')
        except:
            pass
        return

class Theorem116(Theorem):
    def __init__(self):
        super(Theorem116, self).__init__(116, "if bipartite and even nodes then \n{\n    genus <= ((nodes-(4.0))**2.0+15.0)/16.0\n\n};if bipartite and odd nodes then \n{\n    genus <= ((nodes-(3.0))*(nodes-(5.0))+15.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","genus"]
    def run(self):
        if get("bipartite") == True  and evenInvar("nodes"):
            try:
                set("genus",  ((maxb("nodes")-(4.0))**2.0+15.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(16.0*minb("genus")-(15.0))+4.0, ind='Min')
            except:
                pass
        
        if get("bipartite") == True  and oddInvar("nodes"):
            try:
                set("genus",  ((maxb("nodes")-(3.0))*(maxb("nodes")-(5.0))+15.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(16.0*minb("genus")-(14.0))+4.0, ind='Min')
            except:
                pass
        
        return

class Theorem117(Theorem):
    def __init__(self):
        super(Theorem117, self).__init__(117, "if not complete then \n{\n    nodeConnec >= 2.0*mindeg-(nodes)+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["complete","nodeConnec","mindeg","nodes"]
    def run(self):
        if get("complete") == False :
            try:
                set("nodeConnec",  2.0*minb("mindeg")-(maxb("nodes"))+2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("nodeConnec")/2.0+maxb("nodes")/2.0-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("mindeg")-(maxb("nodeConnec"))+2.0, ind='Min')
            except:
                pass
        
        return

class Theorem118(Theorem):
    def __init__(self):
        super(Theorem118, self).__init__(118, "if (nodes >= 6.0 and even nodes and edges >= (nodes**2.0)/4.0+1.0) or (nodes >= 7.0 and odd nodes and edges >= (nodes-(1.0))**2.0/4.0+1.0+mindeg) then \n{\n    circumference >= 5.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","mindeg","circumference"]
    def run(self):
        if (minb("nodes") >= 6.0 and evenInvar("nodes") and minb("edges") >= (maxb("nodes")**2.0)/4.0+1.0) or (minb("nodes") >= 7.0 and oddInvar("nodes") and minb("edges") >= (maxb("nodes")-(1.0))**2.0/4.0+1.0+maxb("mindeg")):
            try:
                set("circumference",  5.0, ind='Min')
            except:
                pass
        
        return

class Theorem119(Theorem):
    def __init__(self):
        super(Theorem119, self).__init__(119, "if chromaticNum >= maxClique then \n{\n    mindeg <= (3.0*maxClique-(4.0))*nodes/(3.0*maxClique-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","mindeg","nodes"]
    def run(self):
        if minb("chromaticNum") >= maxb("maxClique"):
            try:
                set("mindeg",  (3.0*maxb("maxClique")-(4.0))*maxb("nodes")/(3.0*maxb("maxClique")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("maxClique",  (minb("mindeg")-(4.0*minb("nodes")))/(3.0*(minb("mindeg")-(minb("nodes")))), ind='Min')
            except:
                pass
            try:
                set("nodes",  minb("mindeg")*(3.0*minb("maxClique")-(1.0))/(3.0*minb("maxClique")-(4.0)), ind='Min')
            except:
                pass
        
        return

class Theorem120(Theorem):
    def __init__(self):
        super(Theorem120, self).__init__(120, "if hamiltonian and nodes >= chromaticNum-(1.0) and chromaticNum >= 4.0 then \n{\n    edges >= (chromaticNum-(1.0))*(chromaticNum-(2.0))/2.0+nodes\n\n} else if hamiltonian and chromaticNum == 3.0 and even nodes then \n{\n    edges >= nodes+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodes","chromaticNum","edges"]
    def run(self):
        if get("hamiltonian") == True  and minb("nodes") >= maxb("chromaticNum")-(1.0) and minb("chromaticNum") >= 4.0:
            try:
                set("edges",  (minb("chromaticNum")-(1.0))*(minb("chromaticNum")-(2.0))/2.0+minb("nodes"), ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  sqrt(8.0*maxb("edges")-(8.0*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(minb("chromaticNum")**2.0/2.0)+3.0*minb("chromaticNum")/2.0+maxb("edges")-(1.0), ind='Max')
            except:
                pass
        
        elif get("hamiltonian") == True  and minb("chromaticNum") >= 3.0 and maxb("chromaticNum") <= 3.0 and evenInvar("nodes"):
            try:
                set("edges",  minb("nodes")+1.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")-(1.0), ind='Max')
            except:
                pass
        
        return

