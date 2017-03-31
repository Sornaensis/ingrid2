class Theorem121(Theorem):
    def __init__(self):
        super(Theorem121, self).__init__(121, "chromaticNum <= nodes-(nodeConnec*(diameter-(3.0)))-(2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodes","nodeConnec","diameter"]
    def run(self):
        try:
            set("chromaticNum",  maxb("nodes")-(minb("nodeConnec")*(minb("diameter")-(3.0)))-(2.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("chromaticNum")+minb("diameter")*minb("nodeConnec")-(3.0*minb("nodeConnec"))+2.0, ind='Min')
        except:
            pass
        try:
            set("nodeConnec",  (-(minb("chromaticNum"))+maxb("nodes")-(2.0))/(minb("diameter")-(3.0)), ind='Max')
        except:
            pass
        try:
            set("diameter",  (-(minb("chromaticNum"))+3.0*maxb("nodeConnec")+maxb("nodes")-(2.0))/maxb("nodeConnec"), ind='Max')
        except:
            pass
        return

class Theorem122(Theorem):
    def __init__(self):
        super(Theorem122, self).__init__(122, "if edges >= nodes**2.0/4.0 then \n{\n    edgeCliqueCover <= ((1.0/2.0)*nodes*(nodes-(1.0))-(edges))+(1.0+sqrt(1.0+4.0*((1.0/2.0)*nodes*(nodes-(1.0))-(edges))))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","edgeCliqueCover"]
    def run(self):
        if minb("edges") >= maxb("nodes")**2.0/4.0:
            try:
                set("edgeCliqueCover",  ((1.0/2.0)*maxb("nodes")*(maxb("nodes")-(1.0))-(minb("edges")))+(1.0+sqrt(1.0+4.0*((1.0/2.0)*maxb("nodes")*(maxb("nodes")-(1.0))-(minb("edges"))))), ind='Max')
            except:
                pass
            try:
                set("nodes",  0.5*sqrt(8.0*minb("edgeCliqueCover")+8.0*minb("edges")+8.0*sqrt(4.0*minb("edgeCliqueCover")+1.0)+9.0)+0.5, ind='Min')
            except:
                pass
            try:
                set("edges",  -(1.0*minb("edgeCliqueCover"))+0.5*maxb("nodes")**2.0-(0.5*maxb("nodes"))+1.0*sqrt(4.0*minb("edgeCliqueCover")+1.0)-(1.0), ind='Max')
            except:
                pass
        
        return

class Theorem123(Theorem):
    def __init__(self):
        super(Theorem123, self).__init__(123, "if nodes <= 2.0*edges then \n{\n    mindeg == edgeConnec\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","mindeg","edgeConnec"]
    def run(self):
        if maxb("nodes") <= 2.0*minb("edges"):
            try:
                set("mindeg",  minb("edgeConnec"), ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  maxb("edgeConnec"), ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  minb("mindeg"), ind='Min')
            except:
                pass
        
        return

class Theorem124(Theorem):
    def __init__(self):
        super(Theorem124, self).__init__(124, "if connected then \n{\n    bandwidth >= (nodes-(1.0))/diameter\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","bandwidth","nodes","diameter"]
    def run(self):
        if get("connected") == True :
            try:
                set("bandwidth",  (minb("nodes")-(1.0))/maxb("diameter"), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("bandwidth")*maxb("diameter")+1.0, ind='Max')
            except:
                pass
            try:
                set("diameter",  (minb("nodes")-(1.0))/maxb("bandwidth"), ind='Min')
            except:
                pass
        
        return

class Theorem125(Theorem):
    def __init__(self):
        super(Theorem125, self).__init__(125, "if genus >= 1.0 and istrue congruent(girth, 3.0, 4.0) then \n{\n    nodes >= 9.0*(girth-(1.0))/4.0+1.0\n\n} else if genus >= 1.0 then \n{\n    nodes >= 9.0*(girth-(1.0))/4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","nodes"]
    def run(self):
        if minb("genus") >= 1.0 and congruent("girth", 3.0, 4.0):
            try:
                set("nodes",  9.0*(minb("girth")-(1.0))/4.0+1.0, ind='Min')
            except:
                pass
            try:
                set("girth",  4.0*maxb("nodes")/9.0+5.0/9.0, ind='Max')
            except:
                pass
        
        elif minb("genus") >= 1.0:
            try:
                set("nodes",  9.0*(minb("girth")-(1.0))/4.0, ind='Min')
            except:
                pass
            try:
                set("girth",  4.0*maxb("nodes")/9.0+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem126(Theorem):
    def __init__(self):
        super(Theorem126, self).__init__(126, "if nodes <= mindeg*2.0 then \n{\n    nodes <= 2.0*edgeConnec+3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","edgeConnec"]
    def run(self):
        if maxb("nodes") <= minb("mindeg")*2.0:
            try:
                set("nodes",  2.0*maxb("edgeConnec")+3.0, ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  minb("nodes")/2.0-(3.0/2.0), ind='Min')
            except:
                pass
        
        return

class Theorem127(Theorem):
    def __init__(self):
        super(Theorem127, self).__init__(127, "if hamiltonian and even nodes and maxdeg == 3.0 then \n{\n    edgeChromatic == maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodes","maxdeg","edgeChromatic"]
    def run(self):
        if get("hamiltonian") == True  and evenInvar("nodes") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0:
            try:
                set("edgeChromatic",  minb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("edgeChromatic"), ind='Max')
            except:
                pass
            try:
                set("edgeChromatic",  maxb("maxdeg"), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  minb("edgeChromatic"), ind='Min')
            except:
                pass
        
        return

class Theorem128(Theorem):
    def __init__(self):
        super(Theorem128, self).__init__(128, "if nodes >= 2.0*edgeInd+1.0 and (maxdeg <= 2.0*edgeInd and nodes <= 2.0*edgeInd+floor(edgeInd/floor((maxdeg+1.0)/2.0)) and odd maxdeg) then \n{\n    edges <= min(nodes*maxdeg/2.0, edgeInd*maxdeg+floor(2.0*(nodes-(edgeInd))/(maxdeg+3.0))*(maxdeg-(1.0))/2.0)\n\n} else if nodes >= 2.0*edgeInd+1.0 and (maxdeg <= 2.0*edgeInd and nodes <= 2.0*edgeInd+floor(edgeInd/floor((maxdeg+1.0)/2.0)) and even maxdeg) then \n{\n    edges <= nodes*maxdeg/2.0\n\n};if nodes >= 2.0*edgeInd and (maxdeg <= 2.0*edgeInd and nodes <= 2.0*edgeInd+floor(edgeInd/floor((maxdeg+1.0)/2.0))) then \n{\n    edges <= edgeInd*maxdeg+floor(edgeInd*floor((maxdeg+1.0)/2.0))*floor(maxdeg/2.0)\n\n};if nodes >= 2.0*edgeInd and maxdeg >= 2.0*edgeInd+1.0 and nodes >= edgeInd+maxdeg then \n{\n    edges <= edgeInd*maxdeg\n\n} else if nodes >= 2.0*edgeInd and maxdeg >= 2.0*edgeInd+1.0 and nodes < edgeInd+maxdeg then \n{\n    edges <= max(edgeInd*(2.0*edgeInd+1.0), floor(edgeInd*(nodes+maxdeg-(edgeInd))/2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeInd","maxdeg","edges"]
    def run(self):
        if minb("nodes") >= 2.0*maxb("edgeInd")+1.0 and (maxb("maxdeg") <= 2.0*minb("edgeInd") and maxb("nodes") <= 2.0*minb("edgeInd")+floor(minb("edgeInd")/floor((maxb("maxdeg")+1.0)/2.0)) and oddInvar("maxdeg")):
            try:
                set("edges",  min(maxb("nodes")*maxb("maxdeg")/2.0, maxb("edgeInd")*maxb("maxdeg")+floor(2.0*(maxb("nodes")-(maxb("edgeInd")))/(maxb("maxdeg")+3.0))*(maxb("maxdeg")-(1.0))/2.0), ind='Max')
            except:
                pass
        
        elif minb("nodes") >= 2.0*maxb("edgeInd")+1.0 and (maxb("maxdeg") <= 2.0*minb("edgeInd") and maxb("nodes") <= 2.0*minb("edgeInd")+floor(minb("edgeInd")/floor((maxb("maxdeg")+1.0)/2.0)) and evenInvar("maxdeg")):
            try:
                set("edges",  maxb("nodes")*maxb("maxdeg")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("edges")/maxb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  2.0*minb("edges")/maxb("nodes"), ind='Min')
            except:
                pass
        
        if minb("nodes") >= 2.0*maxb("edgeInd") and (maxb("maxdeg") <= 2.0*minb("edgeInd") and maxb("nodes") <= 2.0*minb("edgeInd")+floor(minb("edgeInd")/floor((maxb("maxdeg")+1.0)/2.0))):
            try:
                set("edges",  maxb("edgeInd")*maxb("maxdeg")+floor(maxb("edgeInd")*floor((maxb("maxdeg")+1.0)/2.0))*floor(maxb("maxdeg")/2.0), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  (-(floor(maxb("edgeInd")*floor((maxb("maxdeg")+1.0)/2.0))*floor(maxb("maxdeg")/2.0))+minb("edges"))/maxb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(floor(maxb("edgeInd")*floor((maxb("maxdeg")+1.0)/2.0))*floor(maxb("maxdeg")/2.0))+minb("edges"))/maxb("edgeInd"), ind='Min')
            except:
                pass
        
        if minb("nodes") >= 2.0*maxb("edgeInd") and minb("maxdeg") >= 2.0*maxb("edgeInd")+1.0 and minb("nodes") >= maxb("edgeInd")+maxb("maxdeg"):
            try:
                set("edges",  maxb("edgeInd")*maxb("maxdeg"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("edges")/maxb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  minb("edges")/maxb("edgeInd"), ind='Min')
            except:
                pass
        
        elif minb("nodes") >= 2.0*maxb("edgeInd") and minb("maxdeg") >= 2.0*maxb("edgeInd")+1.0 and maxb("nodes") < minb("edgeInd")+minb("maxdeg"):
            try:
                set("edges",  max(maxb("edgeInd")*(2.0*maxb("edgeInd")+1.0), floor(maxb("edgeInd")*(maxb("nodes")+maxb("maxdeg")-(maxb("edgeInd")))/2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem129(Theorem):
    def __init__(self):
        super(Theorem129, self).__init__(129, "if defined girth and girth > 3.0 then \n{\n    mindeg <= (nodes-(diameter)+3.0*(diameter/3.0+1.0)-(3.0))/(diameter/3.0+1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodes","diameter"]
    def run(self):
        if minb("girth") != 'undt'  and minb("girth") > 3.0:
            try:
                set("mindeg",  (maxb("nodes")-(maxb("diameter"))+3.0*(maxb("diameter")/3.0+1.0)-(3.0))/(maxb("diameter")/3.0+1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("mindeg")*(minb("diameter")+3.0)/3.0, ind='Min')
            except:
                pass
            try:
                set("diameter",  -(3.0)+3.0*minb("nodes")/maxb("mindeg"), ind='Min')
            except:
                pass
        
        return

class Theorem130(Theorem):
    def __init__(self):
        super(Theorem130, self).__init__(130, "if diam == 2.0 and nodes >= maxdeg*maxdeg/8.0 then \n{\n    edges >= nodes*(nodes-(1.0))/(2.0*maxdeg)\n\n} else if diam == 2.0 and nodes < maxdeg*maxdeg/8.0 then \n{\n    edges >= maxdeg*nodes*(nodes-(1.0))/(maxdeg*maxdeg+8.0*nodes)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diam","nodes","maxdeg","edges"]
    def run(self):
        if minb("diam") >= 2.0 and maxb("diam") <= 2.0 and minb("nodes") >= maxb("maxdeg")*maxb("maxdeg")/8.0:
            try:
                set("edges",  minb("nodes")*(minb("nodes")-(1.0))/(2.0*maxb("maxdeg")), ind='Min')
            except:
                pass
            try:
                set("nodes",  sqrt(8.0*maxb("edges")*maxb("maxdeg")+1.0)/2.0+1.0/2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  minb("nodes")*(minb("nodes")-(1.0))/(2.0*maxb("edges")), ind='Min')
            except:
                pass
        
        elif minb("diam") >= 2.0 and maxb("diam") <= 2.0 and maxb("nodes") < minb("maxdeg")*minb("maxdeg")/8.0:
            try:
                set("edges",  maxb("maxdeg")*minb("nodes")*(minb("nodes")-(1.0))/(maxb("maxdeg")*maxb("maxdeg")+8.0*minb("nodes")), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (minb("nodes")**2.0-(minb("nodes"))+sqrt(minb("nodes")*(-(32.0*maxb("edges")**2.0)+minb("nodes")**3.0-(2.0*minb("nodes")**2.0)+minb("nodes"))))/(2.0*maxb("edges")), ind='Min')
            except:
                pass
            try:
                set("nodes",  (8.0*maxb("edges")+maxb("maxdeg")+sqrt(64.0*maxb("edges")**2.0+4.0*maxb("edges")*maxb("maxdeg")**3.0+16.0*maxb("edges")*maxb("maxdeg")+maxb("maxdeg")**2.0))/(2.0*maxb("maxdeg")), ind='Max')
            except:
                pass
        
        return

class Theorem131(Theorem):
    def __init__(self):
        super(Theorem131, self).__init__(131, "chromaticNum <= maxdeg-(1.0)+(maxdeg+1.0)/max(4.0, maxClique+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxdeg","maxClique"]
    def run(self):
        try:
            set("chromaticNum",  maxb("maxdeg")-(1.0)+(maxb("maxdeg")+1.0)/max(4.0, minb("maxClique")+1.0), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  (max(4.0, minb("maxClique")+1.0)*minb("chromaticNum")+max(4.0, minb("maxClique")+1.0)-(1.0))/(max(4.0, minb("maxClique")+1.0)+1.0), ind='Min')
        except:
            pass
        return

class Theorem132(Theorem):
    def __init__(self):
        super(Theorem132, self).__init__(132, "if istrue congruent(nodes, 3.0, 4.0) then \n{\n    mindeg <= (nodes-(3.0))*(nodes+1.0)/(4.0*(nodes-(1.0)-(maxdeg)))\n\n} else  \n{\n    mindeg <= (nodes-(1.0))**2.0/(4.0*(nodes-(1.0)-(maxdeg)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","maxdeg"]
    def run(self):
        if congruent("nodes", 3.0, 4.0):
            try:
                set("mindeg",  (maxb("nodes")-(3.0))*(maxb("nodes")+1.0)/(4.0*(maxb("nodes")-(1.0)-(maxb("maxdeg")))), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("mindeg")+2.0*sqrt(-(maxb("maxdeg")*minb("mindeg"))+minb("mindeg")**2.0+1.0)+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (4.0*minb("mindeg")*(maxb("nodes")-(1.0))-(maxb("nodes")**2.0)+2.0*maxb("nodes")+3.0)/(4.0*minb("mindeg")), ind='Min')
            except:
                pass
        
        elif True:
            try:
                set("mindeg",  (maxb("nodes")-(1.0))**2.0/(4.0*(maxb("nodes")-(1.0)-(maxb("maxdeg")))), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("mindeg")+2.0*sqrt(minb("mindeg")*(-(maxb("maxdeg"))+minb("mindeg")))+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (minb("nodes")-(1.0))*(4.0*minb("mindeg")-(minb("nodes"))+1.0)/(4.0*minb("mindeg")), ind='Min')
            except:
                pass
        
        return

class Theorem133(Theorem):
    def __init__(self):
        super(Theorem133, self).__init__(133, "let z = 1.0+floor(2.0*edges/nodes);let k = ceil(nodes-(2.0*edges/z));nodeInd >= k+ceil((nodes-(k*z))/(1.0+z));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges"]
    def run(self):
        try:
            set("nodeInd",  ceil(minb("nodes")-(2.0*maxb("edges")/1.0+floor(2.0*maxb("edges")/minb("nodes"))))+ceil((minb("nodes")-(ceil(minb("nodes")-(2.0*maxb("edges")/1.0+floor(2.0*maxb("edges")/minb("nodes"))))*1.0+floor(2.0*maxb("edges")/minb("nodes"))))/(1.0+1.0+floor(2.0*maxb("edges")/minb("nodes")))), ind='Min')
        except:
            pass
        return

class Theorem134(Theorem):
    def __init__(self):
        super(Theorem134, self).__init__(134, "if radius == 2.0 and diam == 2.0 and nodes == 4.0 then \n{\n    edges >= 4.0\n\n} else if radius == 2.0 and diam == 2.0 and nodes >= 5.0 then \n{\n    edges >= 2.0*nodes-(5.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diam","nodes","edges"]
    def run(self):
        if minb("radius") >= 2.0 and maxb("radius") <= 2.0 and minb("diam") >= 2.0 and maxb("diam") <= 2.0 and minb("nodes") >= 4.0 and maxb("nodes") <= 4.0:
            try:
                set("edges",  4.0, ind='Min')
            except:
                pass
        
        elif minb("radius") >= 2.0 and maxb("radius") <= 2.0 and minb("diam") >= 2.0 and maxb("diam") <= 2.0 and minb("nodes") >= 5.0:
            try:
                set("edges",  2.0*minb("nodes")-(5.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/2.0+5.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem135(Theorem):
    def __init__(self):
        super(Theorem135, self).__init__(135, "edges >= 2.0*nodeCover-(numOfComponents);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","numOfComponents"]
    def run(self):
        try:
            set("edges",  2.0*minb("nodeCover")-(maxb("numOfComponents")), ind='Min')
        except:
            pass
        try:
            set("nodeCover",  maxb("edges")/2.0+maxb("numOfComponents")/2.0, ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  -(maxb("edges"))+2.0*minb("nodeCover"), ind='Min')
        except:
            pass
        return

class Theorem136(Theorem):
    def __init__(self):
        super(Theorem136, self).__init__(136, "if maxdeg <= 2.0*edgeInd and odd maxdeg then \n{\n    edges <= edgeInd*maxdeg+(maxdeg-(1.0))/2.0*2.0*edgeInd/(maxdeg+1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","edgeInd","edges"]
    def run(self):
        if maxb("maxdeg") <= 2.0*minb("edgeInd") and oddInvar("maxdeg"):
            try:
                set("edges",  maxb("edgeInd")*maxb("maxdeg")+(maxb("maxdeg")-(1.0))/2.0*2.0*maxb("edgeInd")/(maxb("maxdeg")+1.0), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("edges")*(maxb("maxdeg")+1.0)/(maxb("maxdeg")**2.0+2.0*maxb("maxdeg")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (-(2.0*minb("edgeInd"))+minb("edges")+sqrt(8.0*minb("edgeInd")**2.0+minb("edges")**2.0))/(2.0*minb("edgeInd")), ind='Min')
            except:
                pass
        
        return

class Theorem137(Theorem):
    def __init__(self):
        super(Theorem137, self).__init__(137, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem138(Theorem):
    def __init__(self):
        super(Theorem138, self).__init__(138, "if edges >= (1.0/2.0)*(nodes*nodes-(5.0*nodes)+14.0) then \n{\n    circumference >= nodes-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","circumference"]
    def run(self):
        if minb("edges") >= (1.0/2.0)*(maxb("nodes")*maxb("nodes")-(5.0*maxb("nodes"))+14.0):
            try:
                set("circumference",  minb("nodes")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("circumference")+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem139(Theorem):
    def __init__(self):
        super(Theorem139, self).__init__(139, "if edges >= (1.0/4.0)*(circumference*(2.0*nodes-(circumference))+1.0) then \n{\n    girth == 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","circumference","nodes","girth"]
    def run(self):
        if minb("edges") >= (1.0/4.0)*(maxb("circumference")*(2.0*maxb("nodes")-(maxb("circumference")))+1.0):
            try:
                set("girth",  3.0, ind='Min')
            except:
                pass
            try:
                set("girth",  3.0, ind='Max')
            except:
                pass
        
        return

class Theorem140(Theorem):
    def __init__(self):
        super(Theorem140, self).__init__(140, "if edges >= 4.0*nodes then \n{\n    crossing >= edges**3.0/(100.0*nodes**2.0)+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","crossing"]
    def run(self):
        if minb("edges") >= 4.0*maxb("nodes"):
            try:
                set("crossing",  minb("edges")**3.0/(100.0*maxb("nodes")**2.0)+1.0, ind='Min')
            except:
                pass
            try:
                set("edges",  (100.0*maxb("crossing")*minb("nodes")**2.0-(100.0*minb("nodes")**2.0))**(1.0/3.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(minb("edges")**3.0/(maxb("crossing")-(1.0)))/10.0, ind='Min')
            except:
                pass
        
        return

