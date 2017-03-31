class Theorem281(Theorem):
    def __init__(self):
        super(Theorem281, self).__init__(281, "if nodeConnec >= 2.0 and nodes <= 3.0*mindeg and edges <= ((nodes-(1.0))*mindeg-(1.0))/2.0 then \n{\n    Hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","mindeg","edges","Hamiltonian"]
    def run(self):
        if minb("nodeConnec") >= 2.0 and maxb("nodes") <= 3.0*minb("mindeg") and maxb("edges") <= ((minb("nodes")-(1.0))*minb("mindeg")-(1.0))/2.0:
            set("Hamiltonian", True )
        
        return

class Theorem282(Theorem):
    def __init__(self):
        super(Theorem282, self).__init__(282, "if even nodes and not bipartite then \n{\n    not cycle\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","bipartite","cycle"]
    def run(self):
        if evenInvar("nodes") and get("bipartite") == False :
            set("cycle", False )
        
        return

class Theorem283(Theorem):
    def __init__(self):
        super(Theorem283, self).__init__(283, "if mindeg == maxdeg and maxdeg == nodeConnec and nodeConnec == 3.0 then \n{\n    circumference >= nodes**(2.0/3.0)+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","circumference","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= maxb("nodeConnec") and maxb("maxdeg") <= minb("nodeConnec") and minb("nodeConnec") >= 3.0 and maxb("nodeConnec") <= 3.0:
            try:
                set("circumference",  minb("nodes")**(2.0/3.0)+1.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (maxb("circumference")-(1.0))**(3.0/2.0), ind='Max')
            except:
                pass
        
        return

class Theorem284(Theorem):
    def __init__(self):
        super(Theorem284, self).__init__(284, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem285(Theorem):
    def __init__(self):
        super(Theorem285, self).__init__(285, "edgeCliqueCover <= nodeCliqueCover+nodes*(maxdeg+1.0-(nodes/nodeCliqueCover))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodeCliqueCover","nodes","maxdeg"]
    def run(self):
        try:
            set("edgeCliqueCover",  maxb("nodeCliqueCover")+maxb("nodes")*(maxb("maxdeg")+1.0-(maxb("nodes")/maxb("nodeCliqueCover")))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodeCliqueCover",  minb("edgeCliqueCover")/2.0-(minb("maxdeg")*minb("nodes")/4.0)-(minb("nodes")/4.0)+sqrt(4.0*minb("edgeCliqueCover")**2.0-(4.0*minb("edgeCliqueCover")*minb("maxdeg")*minb("nodes"))-(4.0*minb("edgeCliqueCover")*minb("nodes"))+minb("maxdeg")**2.0*minb("nodes")**2.0+2.0*minb("maxdeg")*minb("nodes")**2.0+9.0*minb("nodes")**2.0)/4.0, ind='Min')
        except:
            pass
        try:
            set("nodes",  minb("nodeCliqueCover")*(minb("maxdeg")+1.0)/2.0+sqrt(minb("nodeCliqueCover")*(-(8.0*maxb("edgeCliqueCover"))+minb("maxdeg")**2.0*minb("nodeCliqueCover")+2.0*minb("maxdeg")*minb("nodeCliqueCover")+9.0*minb("nodeCliqueCover")))/2.0, ind='Min')
        except:
            pass
        try:
            set("maxdeg",  2.0*minb("edgeCliqueCover")/minb("nodes")-(2.0*maxb("nodeCliqueCover")/minb("nodes"))-(1.0)+minb("nodes")/maxb("nodeCliqueCover"), ind='Min')
        except:
            pass
        return

class Theorem286(Theorem):
    def __init__(self):
        super(Theorem286, self).__init__(286, "edges >= (maxdeg+(chromaticNum-(1.0))**2.0+(nodes-(chromaticNum))*mindeg)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","chromaticNum","nodes","mindeg"]
    def run(self):
        try:
            set("edges",  (minb("maxdeg")+(minb("chromaticNum")-(1.0))**2.0+(minb("nodes")-(minb("chromaticNum")))*minb("mindeg"))/2.0, ind='Min')
        except:
            pass
        try:
            set("maxdeg",  minb("chromaticNum")*maxb("mindeg")+2.0*maxb("edges")-(maxb("mindeg")*minb("nodes"))-((minb("chromaticNum")-(1.0))**2.0), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  maxb("mindeg")/2.0+sqrt(8.0*maxb("edges")-(4.0*minb("maxdeg"))+maxb("mindeg")**2.0-(4.0*maxb("mindeg")*minb("nodes"))+4.0*maxb("mindeg"))/2.0+1.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  (minb("chromaticNum")*maxb("mindeg")+2.0*maxb("edges")-(minb("maxdeg"))-((minb("chromaticNum")-(1.0))**2.0))/maxb("mindeg"), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (-(2.0*minb("edges"))+maxb("maxdeg")+(maxb("chromaticNum")-(1.0))**2.0)/(maxb("chromaticNum")-(maxb("nodes"))), ind='Max')
        except:
            pass
        return

class Theorem287(Theorem):
    def __init__(self):
        super(Theorem287, self).__init__(287, "if planar then \n{\n    mindeg <= nodeInd+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","nodeInd"]
    def run(self):
        if get("planar") == True :
            try:
                set("mindeg",  maxb("nodeInd")+2.0, ind='Max')
            except:
                pass
            try:
                set("nodeInd",  minb("mindeg")-(2.0), ind='Min')
            except:
                pass
        
        return

class Theorem288(Theorem):
    def __init__(self):
        super(Theorem288, self).__init__(288, "if diameter == 2.0 and maxClique == 2.0 and regular and not bipartite and istrue congruent(maxdeg, 0.0, 2.0) then \n{\n    nodes >= 3.0*maxdeg-(maxdeg/2.0)\n\n};if diameter == 2.0 and maxClique == 2.0 and regular and bipartite and istrue congruent(maxdeg, 0.0, 3.0) then \n{\n    nodes >= 3.0*maxdeg-(maxdeg/3.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxClique","regular","bipartite","maxdeg","nodes"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and get("regular") == True  and get("bipartite") == False  and congruent("maxdeg", 0.0, 2.0):
            try:
                set("nodes",  3.0*minb("maxdeg")-(minb("maxdeg")/2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  2.0*maxb("nodes")/5.0, ind='Max')
            except:
                pass
        
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0 and minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0 and get("regular") == True  and get("bipartite") == True  and congruent("maxdeg", 0.0, 3.0):
            try:
                set("nodes",  3.0*minb("maxdeg")-(minb("maxdeg")/3.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  3.0*maxb("nodes")/8.0, ind='Max')
            except:
                pass
        
        return

class Theorem289(Theorem):
    def __init__(self):
        super(Theorem289, self).__init__(289, "if connected and not hamiltonian and not tree and circumference >= (nodes-(2.0))/2.0 then \n{\n    domination <= (2.0*nodes-(circumference))/3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","hamiltonian","tree","circumference","nodes","domination"]
    def run(self):
        if get("connected") == True  and get("hamiltonian") == False  and get("tree") == False  and minb("circumference") >= (maxb("nodes")-(2.0))/2.0:
            try:
                set("domination",  (2.0*maxb("nodes")-(minb("circumference")))/3.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("circumference")/2.0+3.0*minb("domination")/2.0, ind='Min')
            except:
                pass
            try:
                set("circumference",  -(3.0*minb("domination"))+2.0*maxb("nodes"), ind='Max')
            except:
                pass
        
        return

class Theorem290(Theorem):
    def __init__(self):
        super(Theorem290, self).__init__(290, "if connected and domination >= 3.0 then \n{\n    edges <= (nodes-(domination)+1.0)*(nodes-(domination))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","domination","edges","nodes"]
    def run(self):
        if get("connected") == True  and minb("domination") >= 3.0:
            try:
                set("edges",  (maxb("nodes")-(minb("domination"))+1.0)*(maxb("nodes")-(minb("domination")))/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("domination")+sqrt(8.0*minb("edges")+1.0)/2.0-(1.0/2.0), ind='Min')
            except:
                pass
            try:
                set("domination",  maxb("nodes")+sqrt(8.0*maxb("edges")+1.0)/2.0+1.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem291(Theorem):
    def __init__(self):
        super(Theorem291, self).__init__(291, "domination <= nodes*(1.0+ln(mindeg))/(mindeg+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","mindeg"]
    def run(self):
        try:
            set("domination",  maxb("nodes")*(1.0+ln(maxb("mindeg")))/(maxb("mindeg")+1.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("domination")*(minb("mindeg")+1.0)/(log(minb("mindeg"))+1.0), ind='Min')
        except:
            pass
        try:
            set("mindeg",  -(maxb("nodes")*LambertW(-(minb("domination")*exp((minb("domination")-(maxb("nodes")))/maxb("nodes"))/maxb("nodes")))/minb("domination")), ind='Min')
        except:
            pass
        return

class Theorem292(Theorem):
    def __init__(self):
        super(Theorem292, self).__init__(292, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem293(Theorem):
    def __init__(self):
        super(Theorem293, self).__init__(293, "if connected and maxdeg == 2.0 and mindeg == 1.0 then \n{\n    nodes == diameter+1.0\n\n} else if connected and maxdeg == 2.0 and mindeg == 2.0 then \n{\n    nodes >= 2.0*diameter,\n    nodes <= 2.0*diameter+1.0\n\n};", "HELP - ensure this is correct")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","mindeg","nodes","diameter"]
    def run(self):
        if get("connected") == True  and minb("maxdeg") >= 2.0 and maxb("maxdeg") <= 2.0 and minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0:
            try:
                set("nodes",  minb("diameter")+1.0, ind='Min')
            except:
                pass
            try:
                set("diameter",  maxb("nodes")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  maxb("diameter")+1.0, ind='Max')
            except:
                pass
            try:
                set("diameter",  minb("nodes")-(1.0), ind='Min')
            except:
                pass
        
        elif get("connected") == True  and minb("maxdeg") >= 2.0 and maxb("maxdeg") <= 2.0 and minb("mindeg") >= 2.0 and maxb("mindeg") <= 2.0:
            try:
                set("nodes",  2.0*minb("diameter"), ind='Min')
            except:
                pass
            try:
                set("diameter",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("diameter")+1.0, ind='Max')
            except:
                pass
            try:
                set("diameter",  minb("nodes")/2.0-(1.0/2.0), ind='Min')
            except:
                pass
        
        return

class Theorem294(Theorem):
    def __init__(self):
        super(Theorem294, self).__init__(294, "edgeCliqueCover <= (nodes-(maxClique)+2.0)**2.0/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodes","maxClique"]
    def run(self):
        try:
            set("edgeCliqueCover",  (maxb("nodes")-(minb("maxClique"))+2.0)**2.0/4.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*sqrt(minb("edgeCliqueCover"))+minb("maxClique")-(2.0), ind='Min')
        except:
            pass
        try:
            set("maxClique",  2.0*sqrt(maxb("edgeCliqueCover"))+maxb("nodes")+2.0, ind='Max')
        except:
            pass
        return

class Theorem295(Theorem):
    def __init__(self):
        super(Theorem295, self).__init__(295, "edges <= max(edgeInd*(2.0*edgeInd+1.0), edgeInd*nodes-(edgeInd*(edgeInd+1.0)/2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","edgeInd","nodes"]
    def run(self):
        try:
            set("edges",  max(minb("edgeInd")*(2.0*minb("edgeInd")+1.0), minb("edgeInd")*maxb("nodes")-(minb("edgeInd")*(minb("edgeInd")+1.0)/2.0)), ind='Max')
        except:
            pass
        return

class Theorem296(Theorem):
    def __init__(self):
        super(Theorem296, self).__init__(296, "if mindeg == maxdeg and maxdeg == 3.0 then \n{\n    nodeConnec == edgeConnec\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","edgeConnec"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0:
            try:
                set("nodeConnec",  minb("edgeConnec"), ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  maxb("nodeConnec"), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  maxb("edgeConnec"), ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  minb("nodeConnec"), ind='Min')
            except:
                pass
        
        return

class Theorem297(Theorem):
    def __init__(self):
        super(Theorem297, self).__init__(297, "if nodeConnec >= 3.0 and planar and not hamiltonian then \n{\n    nodes >= 11.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","planar","hamiltonian","nodes"]
    def run(self):
        if minb("nodeConnec") >= 3.0 and get("planar") == True  and get("hamiltonian") == False :
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        
        return

class Theorem298(Theorem):
    def __init__(self):
        super(Theorem298, self).__init__(298, "if mindeg == maxdeg and maxdeg == 3.0 and not planar and not bipartite then \n{\n    nodes >= 8.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","planar","bipartite","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and get("planar") == False  and get("bipartite") == False :
            try:
                set("nodes",  8.0, ind='Min')
            except:
                pass
        
        return

class Theorem299(Theorem):
    def __init__(self):
        super(Theorem299, self).__init__(299, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 1.0 then \n{\n    nodes >= 10.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 1.0 and maxb("nodeConnec") <= 1.0:
            try:
                set("nodes",  10.0, ind='Min')
            except:
                pass
        
        return

class Theorem300(Theorem):
    def __init__(self):
        super(Theorem300, self).__init__(300, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 1.0 and not planar then \n{\n    nodes >= 12.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","nodes"]
    def run(self):
        if minb("mindeg") >= maxb("maxdeg") and maxb("mindeg") <= minb("maxdeg") and minb("maxdeg") >= 3.0 and maxb("maxdeg") <= 3.0 and minb("nodeConnec") >= 1.0 and maxb("nodeConnec") <= 1.0 and get("planar") == False :
            try:
                set("nodes",  12.0, ind='Min')
            except:
                pass
        
        return

