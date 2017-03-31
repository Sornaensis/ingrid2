class Theorem301(Theorem):
    def __init__(self):
        super(Theorem301, self).__init__(301, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and planar and not hamiltonian and bipartite then \n{\n    nodes >= 26.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","hamiltonian","bipartite","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 2.0 and get("planar") == True  and get("hamiltonian") == False  and get("bipartite") == True :
            try:
                set("nodes",  26.0, ind='Min')
            except:
                pass
        
        return

class Theorem302(Theorem):
    def __init__(self):
        super(Theorem302, self).__init__(302, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and planar and not hamiltonian then \n{\n    nodes >= 14.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","hamiltonian","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 2.0 and get("planar") == True  and get("hamiltonian") == False :
            try:
                set("nodes",  14.0, ind='Min')
            except:
                pass
        
        return

class Theorem303(Theorem):
    def __init__(self):
        super(Theorem303, self).__init__(303, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and bipartite and not hamiltonian then \n{\n    nodes >= 20.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","bipartite","hamiltonian","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 2.0 and get("bipartite") == True  and get("hamiltonian") == False :
            try:
                set("nodes",  20.0, ind='Min')
            except:
                pass
        
        return

class Theorem304(Theorem):
    def __init__(self):
        super(Theorem304, self).__init__(304, "let x = mindeg*floor((mindeg+3.0)/2.0)-(1.0);if regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and even nodes then \n{\n    edgeInd >= (nodes-(2.0*floor((nodes+1.0)/(2.0*x))))/2.0\n\n} else if regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and odd nodes then \n{\n    edgeInd >= (nodes-(max(2.0*floor((nodes+1.0+x)/(2.0*x)), 1.0)))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","edgeConnec","nodes","edgeInd"]
    def run(self):
        if get("regular") == True  and minb("mindeg") >= 3.0 and minb("edgeConnec") >= maxb("mindeg")-(2.0) and evenInvar("nodes"):
            try:
                set("edgeInd",  (minb("nodes")-(2.0*floor((minb("nodes")+1.0)/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0)))))/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*floor((maxb("nodes")+1.0)/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0)))+2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        
        elif get("regular") == True  and minb("mindeg") >= 3.0 and minb("edgeConnec") >= maxb("mindeg")-(2.0) and oddInvar("nodes"):
            try:
                set("edgeInd",  (minb("nodes")-(max(2.0*floor((minb("nodes")+1.0+minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))), 1.0)))/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  max(2.0*floor((maxb("nodes")+1.0+minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*floor((minb("mindeg")+3.0)/2.0)-(1.0))), 1.0)+2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        
        return

class Theorem305(Theorem):
    def __init__(self):
        super(Theorem305, self).__init__(305, "if mindeg == maxdeg and maxdeg == 3.0 then \n{\n    edgeInd >= nodes/2.0-(floor((nodes+3.0)/18.0))-(floor(numOfComponents+4.0)/6.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeInd","nodes","numOfComponents"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0:
            try:
                set("edgeInd",  minb("nodes")/2.0-(floor((minb("nodes")+3.0)/18.0))-(floor(maxb("numOfComponents")+4.0)/6.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*floor((maxb("nodes")+3.0)/18.0)+floor(maxb("numOfComponents")+4.0)/3.0+2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        
        return

class Theorem306(Theorem):
    def __init__(self):
        super(Theorem306, self).__init__(306, "if maxClique == 2.0 and maxdeg <= 4.0 then \n{\n    edges >= 6.0*nodes-(13.0*nodeInd)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 4.0:
            try:
                set("edges",  6.0*minb("nodes")-(13.0*maxb("nodeInd")), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")/6.0+13.0*maxb("nodeInd")/6.0, ind='Max')
            except:
                pass
            try:
                set("nodeInd",  -(maxb("edges")/13.0)+6.0*minb("nodes")/13.0, ind='Min')
            except:
                pass
        
        return

class Theorem307(Theorem):
    def __init__(self):
        super(Theorem307, self).__init__(307, "if edgeConnec > 0.0 then \n{\n    edgeConnec >= min(mindeg, (nodes*(maxdeg-(2.0)))/((maxdeg-(1.0))**(diameter-(1.0))+maxdeg*(maxdeg-(2.0))-(1.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg","nodes","maxdeg","diameter"]
    def run(self):
        if minb("edgeConnec") > 0.0:
            try:
                set("edgeConnec",  min(minb("mindeg"), (minb("nodes")*(minb("maxdeg")-(2.0)))/((minb("maxdeg")-(1.0))**(maxb("diameter")-(1.0))+minb("maxdeg")*(minb("maxdeg")-(2.0))-(1.0))), ind='Min')
            except:
                pass
        
        return

class Theorem308(Theorem):
    def __init__(self):
        super(Theorem308, self).__init__(308, "if nodeConnec >= 2.0 and nodeInd >= 2.0 then \n{\n    circumference >= 2.0*(nodes-(2.0))/nodeInd+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodeInd","circumference","nodes"]
    def run(self):
        if minb("nodeConnec") >= 2.0 and minb("nodeInd") >= 2.0:
            try:
                set("circumference",  2.0*(minb("nodes")-(2.0))/maxb("nodeInd")+2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("circumference")*maxb("nodeInd")/2.0-(maxb("nodeInd"))+2.0, ind='Max')
            except:
                pass
            try:
                set("nodeInd",  2.0*(minb("nodes")-(2.0))/(maxb("circumference")-(2.0)), ind='Min')
            except:
                pass
        
        return

class Theorem309(Theorem):
    def __init__(self):
        super(Theorem309, self).__init__(309, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 3.0 and planar then \n{\n    circumference >= min(nodes, 17.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","circumference","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 3.0 and maxb("nodeConnec") <= 3.0 and get("planar") == True :
            try:
                set("circumference",  min(minb("nodes"), 17.0), ind='Min')
            except:
                pass
        
        return

class Theorem310(Theorem):
    def __init__(self):
        super(Theorem310, self).__init__(310, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 3.0 and planar and nodes <= 36.0 then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","nodes","hamiltonian"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 3.0 and maxb("nodeConnec") <= 3.0 and get("planar") == True  and maxb("nodes") <= 36.0:
            set("hamiltonian", True )
        
        return

class Theorem311(Theorem):
    def __init__(self):
        super(Theorem311, self).__init__(311, "if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg >= 9.0 then \n{\n    nodes >= 2.0*maxdeg\n\n} else if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg <= 8.0 then \n{\n    nodes >= 2.0*maxdeg-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","maxdeg","nodes"]
    def run(self):
        if maxb("maxClique") < minb("chromaticNum") and minb("chromaticNum") >= maxb("maxdeg") and maxb("chromaticNum") <= minb("maxdeg") and minb("maxdeg") >= 9.0:
            try:
                set("nodes",  2.0*minb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
        
        elif maxb("maxClique") < minb("chromaticNum") and minb("chromaticNum") >= maxb("maxdeg") and maxb("chromaticNum") <= minb("maxdeg") and maxb("maxdeg") <= 8.0:
            try:
                set("nodes",  2.0*minb("maxdeg")-(1.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem312(Theorem):
    def __init__(self):
        super(Theorem312, self).__init__(312, "if mindeg == maxdeg and maxdeg == 3.0 and edgeConnec >= 2.0 then \n{\n    edgeInd == nodes/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeConnec","edgeInd","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("edgeConnec") >= 2.0:
            try:
                set("edgeInd",  minb("nodes")/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("edgeInd"), ind='Min')
            except:
                pass
        
        return

class Theorem313(Theorem):
    def __init__(self):
        super(Theorem313, self).__init__(313, "if planar and nodeConnec >= 3.0 then \n{\n    circumference >= min(nodes, 2.0*mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        if get("planar") == True  and minb("nodeConnec") >= 3.0:
            try:
                set("circumference",  min(minb("nodes"), 2.0*minb("mindeg")), ind='Min')
            except:
                pass
        
        return

class Theorem314(Theorem):
    def __init__(self):
        super(Theorem314, self).__init__(314, "if regular and nodeConnec >= 2.0 and nodes < 3.0*mindeg+4.0 then \n{\n    circumference >= min(nodes, 3.0*mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeConnec","nodes","mindeg","circumference"]
    def run(self):
        if get("regular") == True  and minb("nodeConnec") >= 2.0 and maxb("nodes") < 3.0*minb("mindeg")+4.0:
            try:
                set("circumference",  min(minb("nodes"), 3.0*minb("mindeg")), ind='Min')
            except:
                pass
        
        return

class Theorem315(Theorem):
    def __init__(self):
        super(Theorem315, self).__init__(315, "if regular and nodeConnec >= 2.0 then \n{\n    circumference >= min(min(nodes, 3.0*mindeg), 2.0*mindeg+4.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        if get("regular") == True  and minb("nodeConnec") >= 2.0:
            try:
                set("circumference",  min(min(minb("nodes"), 3.0*minb("mindeg")), 2.0*minb("mindeg")+4.0), ind='Min')
            except:
                pass
        
        return

class Theorem316(Theorem):
    def __init__(self):
        super(Theorem316, self).__init__(316, "if regular and even nodes and maxdeg >= 6.0*nodes/7.0 then \n{\n    edgeChromatic == maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","edgeChromatic"]
    def run(self):
        if get("regular") == True  and evenInvar("nodes") and minb("maxdeg") >= 6.0*maxb("nodes")/7.0:
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

class Theorem317(Theorem):
    def __init__(self):
        super(Theorem317, self).__init__(317, "if maxdeg == nodes-(1.0) and even nodes and edges <= 2.0*floor((nodes-(1.0))/2.0)**2.0 then \n{\n    edgeChromatic == maxdeg\n\n} else if maxdeg == nodes-(1.0) and odd nodes and edges <= 2.0*floor((nodes-(1.0))/2.0)**2.0+mindeg then \n{\n    edgeChromatic == maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodes","edges","edgeChromatic","mindeg"]
    def run(self):
        if minb("maxdeg") >= maxb("nodes")-(1.0) and maxb("maxdeg") <= minb("nodes")-(1.0) and evenInvar("nodes") and maxb("edges") <= 2.0*floor((minb("nodes")-(1.0))/2.0)**2.0:
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
        
        elif minb("maxdeg") >= maxb("nodes")-(1.0) and maxb("maxdeg") <= minb("nodes")-(1.0) and oddInvar("nodes") and maxb("edges") <= 2.0*floor((minb("nodes")-(1.0))/2.0)**2.0+minb("mindeg"):
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

class Theorem318(Theorem):
    def __init__(self):
        super(Theorem318, self).__init__(318, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem319(Theorem):
    def __init__(self):
        super(Theorem319, self).__init__(319, "let m = mod(2.0*e, maxdeg);if spectralRadius >= (2.0*edges*(2.0*maxdeg-(1.0))-(2.0*m*(maxdeg-(m))))**(1.0/4.0) then \n{\n    girth <= 4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","edges","maxdeg","e","girth"]
    def run(self):
        if minb("spectralRadius") >= (2.0*maxb("edges")*(2.0*minb("maxdeg")-(1.0))-(2.0*mod(2.0*minb("e"), minb("maxdeg"))*(minb("maxdeg")-(mod(2.0*minb("e"), minb("maxdeg"))))))**(1.0/4.0):
            try:
                set("girth",  4.0, ind='Max')
            except:
                pass
        
        return

class Theorem320(Theorem):
    def __init__(self):
        super(Theorem320, self).__init__(320, "if connected and regular and odd nodes and nodes < 5.0*mindeg/2.0 then \n{\n    girth == 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","regular","nodes","mindeg","girth"]
    def run(self):
        if get("connected") == True  and get("regular") == True  and oddInvar("nodes") and maxb("nodes") < 5.0*minb("mindeg")/2.0:
            try:
                set("girth",  3.0, ind='Min')
            except:
                pass
            try:
                set("girth",  3.0, ind='Max')
            except:
                pass
        
        return

