class Theorem241(Theorem):
    def __init__(self):
        super(Theorem241, self).__init__(241, "if maxClique == 2.0 then \n{\n    chromaticNum <= 3.0*(nodes+12.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodes"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("chromaticNum",  3.0*(maxb("nodes")+12.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  16.0*minb("chromaticNum")/3.0-(12.0), ind='Min')
            except:
                pass
        
        return

class Theorem242(Theorem):
    def __init__(self):
        super(Theorem242, self).__init__(242, "nodes >= nodeCliqueCover+chromaticNum-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCliqueCover","chromaticNum"]
    def run(self):
        try:
            set("nodes",  minb("nodeCliqueCover")+minb("chromaticNum")-(1.0), ind='Min')
        except:
            pass
        try:
            set("nodeCliqueCover",  -(minb("chromaticNum"))+maxb("nodes")+1.0, ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  -(minb("nodeCliqueCover"))+maxb("nodes")+1.0, ind='Max')
        except:
            pass
        return

class Theorem243(Theorem):
    def __init__(self):
        super(Theorem243, self).__init__(243, "nodes >= maxdeg+domination;", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxdeg","domination"]
    def run(self):
        try:
            set("nodes",  minb("maxdeg")+minb("domination"), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  -(minb("domination"))+maxb("nodes"), ind='Max')
        except:
            pass
        try:
            set("domination",  -(minb("maxdeg"))+maxb("nodes"), ind='Max')
        except:
            pass
        return

class Theorem244(Theorem):
    def __init__(self):
        super(Theorem244, self).__init__(244, "if nodeInd == 2.0 then \n{\n    nodeCliqueCover <= 3.0*(nodes+12.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes"]
    def run(self):
        if minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0:
            try:
                set("nodeCliqueCover",  3.0*(maxb("nodes")+12.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  16.0*minb("nodeCliqueCover")/3.0-(12.0), ind='Min')
            except:
                pass
        
        return

class Theorem245(Theorem):
    def __init__(self):
        super(Theorem245, self).__init__(245, "if mindeg >= 2.0 then \n{\n    edgeCliqueCover <= 2.0*(nodes-(2.0)+2.0*genus)-(4.0*(numOfComponents-(1.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeCliqueCover","nodes","genus","numOfComponents"]
    def run(self):
        if minb("mindeg") >= 2.0:
            try:
                set("edgeCliqueCover",  2.0*(maxb("nodes")-(2.0)+2.0*maxb("genus"))-(4.0*(minb("numOfComponents")-(1.0))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edgeCliqueCover")/2.0-(2.0*maxb("genus"))+2.0*minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("genus",  minb("edgeCliqueCover")/4.0-(maxb("nodes")/2.0)+minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  -(minb("edgeCliqueCover")/4.0)+maxb("genus")+maxb("nodes")/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem246(Theorem):
    def __init__(self):
        super(Theorem246, self).__init__(246, "if nodes >= 3.0 then \n{\n    edgeCliqueCover <= 2.0*(nodes-(2.0)+2.0*genus)-((numOfComponents-(1.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeCliqueCover","genus","numOfComponents"]
    def run(self):
        if minb("nodes") >= 3.0:
            try:
                set("edgeCliqueCover",  2.0*(maxb("nodes")-(2.0)+2.0*maxb("genus"))-((minb("numOfComponents")-(1.0))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edgeCliqueCover")/2.0-(2.0*maxb("genus"))+minb("numOfComponents")/2.0+3.0/2.0, ind='Min')
            except:
                pass
            try:
                set("genus",  minb("edgeCliqueCover")/4.0-(maxb("nodes")/2.0)+minb("numOfComponents")/4.0+3.0/4.0, ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  -(minb("edgeCliqueCover"))+4.0*maxb("genus")+2.0*maxb("nodes")-(3.0), ind='Max')
            except:
                pass
        
        return

class Theorem247(Theorem):
    def __init__(self):
        super(Theorem247, self).__init__(247, "nodeInd <= nodes/(1.0+mindeg/maxdeg);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","mindeg","maxdeg"]
    def run(self):
        try:
            set("nodeInd",  maxb("nodes")/(1.0+minb("mindeg")/maxb("maxdeg")), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("nodeInd")*(minb("maxdeg")+minb("mindeg"))/minb("maxdeg"), ind='Min')
        except:
            pass
        try:
            set("mindeg",  maxb("maxdeg")*(-(minb("nodeInd"))+maxb("nodes"))/minb("nodeInd"), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  -(maxb("mindeg")*maxb("nodeInd")/(maxb("nodeInd")-(maxb("nodes")))), ind='Min')
        except:
            pass
        return

class Theorem248(Theorem):
    def __init__(self):
        super(Theorem248, self).__init__(248, "nodeCover >= nodes/(1.0+maxdeg/mindeg);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","mindeg"]
    def run(self):
        try:
            set("nodeCover",  minb("nodes")/(1.0+maxb("maxdeg")/minb("mindeg")), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("nodeCover")*(maxb("maxdeg")+maxb("mindeg"))/maxb("mindeg"), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  minb("mindeg")*(-(maxb("nodeCover"))+minb("nodes"))/maxb("nodeCover"), ind='Min')
        except:
            pass
        try:
            set("mindeg",  -(minb("maxdeg")*minb("nodeCover")/(minb("nodeCover")-(minb("nodes")))), ind='Max')
        except:
            pass
        return

class Theorem249(Theorem):
    def __init__(self):
        super(Theorem249, self).__init__(249, "nodeInd >= nodes/(bandwidth+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","bandwidth"]
    def run(self):
        try:
            set("nodeInd",  minb("nodes")/(maxb("bandwidth")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("nodeInd")*(maxb("bandwidth")+1.0), ind='Max')
        except:
            pass
        try:
            set("bandwidth",  (-(maxb("nodeInd"))+minb("nodes"))/maxb("nodeInd"), ind='Min')
        except:
            pass
        return

class Theorem250(Theorem):
    def __init__(self):
        super(Theorem250, self).__init__(250, "nodeCover <= nodes/(1.0+1.0/bandwidth);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","bandwidth"]
    def run(self):
        try:
            set("nodeCover",  maxb("nodes")/(1.0+1.0/maxb("bandwidth")), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("nodeCover")+minb("nodeCover")/maxb("bandwidth"), ind='Min')
        except:
            pass
        try:
            set("bandwidth",  -(maxb("nodeCover")/(maxb("nodeCover")-(maxb("nodes")))), ind='Min')
        except:
            pass
        return

class Theorem251(Theorem):
    def __init__(self):
        super(Theorem251, self).__init__(251, "if defined girth then \n{\n    edge >= (girth-(1.0))*(arboricity-(1.0))**2.0+(arboricity-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","edge","arboricity"]
    def run(self):
        if minb("girth") != 'undt' :
            try:
                set("edge",  (minb("girth")-(1.0))*(minb("arboricity")-(1.0))**2.0+(minb("arboricity")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("girth",  (-(minb("arboricity"))+maxb("edge")+(minb("arboricity")-(1.0))**2.0+1.0)/(minb("arboricity")-(1.0))**2.0, ind='Max')
            except:
                pass
            try:
                set("arboricity",  (2.0*maxb("girth")+sqrt(4.0*maxb("edge")*maxb("girth")-(4.0*maxb("edge"))+1.0)-(3.0))/(2.0*(maxb("girth")-(1.0))), ind='Max')
            except:
                pass
        
        return

class Theorem252(Theorem):
    def __init__(self):
        super(Theorem252, self).__init__(252, "if nodeConnec >= 2.0 and girth >= 4.0 and istrue congruent(girth, 1.0, 4.0) then \n{\n    edgeInd >= maxdeg*(girth-(1.0))/4.0\n\n} else if nodeConnec >= 2.0 and girth >= 4.0 and (istrue congruent(girth, 2.0, 4.0) or (maxdeg == 2.0 and istrue congruent(girth, 3.0, 4.0))) then \n{\n    edgeInd >= maxdeg*(girth-(1.0))/4.0+1.0\n\n} else if nodeConnec >= 2.0 and girth >= 4.0 and (istrue congruent(g, 0.0, 4.0) or (maxdeg >= 3.0 and istrue congruent(g, 3.0, 4.0))) then \n{\n    edgeInd >= maxdeg*(girth-(1.0))/4.0+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","girth","edgeInd","maxdeg","g"]
    def run(self):
        if minb("nodeConnec") >= 2.0 and minb("girth") >= 4.0 and congruent("girth", 1.0, 4.0):
            try:
                set("edgeInd",  minb("maxdeg")*(minb("girth")-(1.0))/4.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  4.0*maxb("edgeInd")/(minb("girth")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("girth",  (4.0*maxb("edgeInd")+maxb("maxdeg"))/maxb("maxdeg"), ind='Max')
            except:
                pass
        
        elif minb("nodeConnec") >= 2.0 and minb("girth") >= 4.0 and (congruent("girth", 2.0, 4.0) or (minb("maxdeg") >= 2.0 and maxb("maxdeg") <= 2.0 and congruent("girth", 3.0, 4.0))):
            try:
                set("edgeInd",  minb("maxdeg")*(minb("girth")-(1.0))/4.0+1.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  4.0*(maxb("edgeInd")-(1.0))/(minb("girth")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("girth",  (4.0*maxb("edgeInd")+maxb("maxdeg")-(4.0))/maxb("maxdeg"), ind='Max')
            except:
                pass
        
        elif minb("nodeConnec") >= 2.0 and minb("girth") >= 4.0 and (congruent("g", 0.0, 4.0) or (minb("maxdeg") >= 3.0 and congruent("g", 3.0, 4.0))):
            try:
                set("edgeInd",  minb("maxdeg")*(minb("girth")-(1.0))/4.0+2.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  4.0*(maxb("edgeInd")-(2.0))/(minb("girth")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("girth",  (4.0*maxb("edgeInd")+maxb("maxdeg")-(8.0))/maxb("maxdeg"), ind='Max')
            except:
                pass
        
        return

class Theorem253(Theorem):
    def __init__(self):
        super(Theorem253, self).__init__(253, "if nodeConnec >= 1.0 then \n{\n    maxdeg <= (nodes-(1.0))/((girth-(1.0))/4.0*(nodeConnec-(1.0))+1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","maxdeg","nodes","girth"]
    def run(self):
        if minb("nodeConnec") >= 1.0:
            try:
                set("maxdeg",  (maxb("nodes")-(1.0))/((minb("girth")-(1.0))/4.0*(minb("nodeConnec")-(1.0))+1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("girth")*minb("maxdeg")*minb("nodeConnec")/4.0-(minb("girth")*minb("maxdeg")/4.0)-(minb("maxdeg")*minb("nodeConnec")/4.0)+5.0*minb("maxdeg")/4.0+1.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (maxb("maxdeg")*maxb("nodeConnec")-(5.0*maxb("maxdeg"))+4.0*maxb("nodes")-(4.0))/(maxb("maxdeg")*(maxb("nodeConnec")-(1.0))), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  (maxb("girth")*maxb("maxdeg")-(5.0*maxb("maxdeg"))+4.0*maxb("nodes")-(4.0))/(maxb("maxdeg")*(maxb("girth")-(1.0))), ind='Max')
            except:
                pass
        
        return

class Theorem254(Theorem):
    def __init__(self):
        super(Theorem254, self).__init__(254, "if nodeInd == 2.0 and (mindeg == 1.0 or nodes <= 4.0) then \n{\n    nodeCliqueCover <= 2.0\n\n} else if nodeInd == 2.0 and (nodes >= 5.0 and nodes <= 10.0) then \n{\n    nodeInd <= 3.0\n\n} else if nodeInd == 2.0 then \n{\n    nodeCliqueCover <= (mindeg+11.0)/4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","nodeCliqueCover"]
    def run(self):
        if minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0 and (minb("mindeg") >= 1.0 and maxb("mindeg") <= 1.0 or maxb("nodes") <= 4.0):
            try:
                set("nodeCliqueCover",  2.0, ind='Max')
            except:
                pass
        
        elif minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0 and (minb("nodes") >= 5.0 and maxb("nodes") <= 10.0):
            try:
                set("nodeInd",  3.0, ind='Max')
            except:
                pass
        
        elif minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0:
            try:
                set("nodeCliqueCover",  (maxb("mindeg")+11.0)/4.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  4.0*minb("nodeCliqueCover")-(11.0), ind='Min')
            except:
                pass
        
        return

class Theorem255(Theorem):
    def __init__(self):
        super(Theorem255, self).__init__(255, "if connected then \n{\n    edges >= nodes+8.0*thickness-(13.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","edges","nodes","thickness"]
    def run(self):
        if get("connected") == True :
            try:
                set("edges",  minb("nodes")+8.0*minb("thickness")-(13.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")-(8.0*minb("thickness"))+13.0, ind='Max')
            except:
                pass
            try:
                set("thickness",  maxb("edges")/8.0-(minb("nodes")/8.0)+13.0/8.0, ind='Max')
            except:
                pass
        
        return

class Theorem256(Theorem):
    def __init__(self):
        super(Theorem256, self).__init__(256, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem257(Theorem):
    def __init__(self):
        super(Theorem257, self).__init__(257, "if diam >= 3.0 and (odd diam or nodeConnec == 1.0) then \n{\n    edgeInd >= nodeConnec*(diam-(1.0))/2.0\n\n} else if diam >= 3.0 and (even diam and nodeConnec >= 2.0) then \n{\n    edgeInd >= nodeConnec*(diam-(1.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diam","nodeConnec","edgeInd"]
    def run(self):
        if minb("diam") >= 3.0 and (oddInvar("diam") or minb("nodeConnec") >= 1.0 and maxb("nodeConnec") <= 1.0):
            try:
                set("edgeInd",  minb("nodeConnec")*(minb("diam")-(1.0))/2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0*maxb("edgeInd")/(minb("diam")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("diam",  (2.0*maxb("edgeInd")+maxb("nodeConnec"))/maxb("nodeConnec"), ind='Max')
            except:
                pass
        
        elif minb("diam") >= 3.0 and (evenInvar("diam") and minb("nodeConnec") >= 2.0):
            try:
                set("edgeInd",  minb("nodeConnec")*(minb("diam")-(1.0))/2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0*maxb("edgeInd")/(minb("diam")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("diam",  (2.0*maxb("edgeInd")+maxb("nodeConnec"))/maxb("nodeConnec"), ind='Max')
            except:
                pass
        
        return

class Theorem258(Theorem):
    def __init__(self):
        super(Theorem258, self).__init__(258, "if ((nodeConnec > 0.0 and nodes > 2.0) or mindeg > 1.0) and ((thickness > 3.0 or thickness < 3.0) and (nodes < 9.0 or nodes > 10.0)) then \n{\n    genus >= thickness+(edges-(4.0*nodes)-(1.0))/6.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","mindeg","thickness","genus","edges"]
    def run(self):
        if ((minb("nodeConnec") > 0.0 and minb("nodes") > 2.0) or minb("mindeg") > 1.0) and ((minb("thickness") > 3.0 or maxb("thickness") < 3.0) and (maxb("nodes") < 9.0 or minb("nodes") > 10.0)):
            try:
                set("genus",  minb("thickness")+(minb("edges")-(4.0*maxb("nodes"))-(1.0))/6.0, ind='Min')
            except:
                pass
            try:
                set("thickness",  -(minb("edges")/6.0)+maxb("genus")+2.0*maxb("nodes")/3.0+1.0/6.0, ind='Max')
            except:
                pass
            try:
                set("edges",  6.0*maxb("genus")+4.0*maxb("nodes")-(6.0*minb("thickness"))+1.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edges")/4.0-(3.0*maxb("genus")/2.0)+3.0*minb("thickness")/2.0-(1.0/4.0), ind='Min')
            except:
                pass
        
        return

class Theorem259(Theorem):
    def __init__(self):
        super(Theorem259, self).__init__(259, "if girth > 1.0+2.0*(log(nodes)/log(2.0)) then \n{\n    chromaticNum <= 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","chromaticNum"]
    def run(self):
        if minb("girth") > 1.0+2.0*(log(maxb("nodes"))/log(2.0)):
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        
        return

class Theorem260(Theorem):
    def __init__(self):
        super(Theorem260, self).__init__(260, "let c = edges-(nodes)+numOfComponents;genus <= c/2.0-(c/(4.0*log(c)/log(2.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["genus","edges","nodes","numOfComponents"]
    def run(self):
        try:
            set("genus",  maxb("edges")-(minb("nodes"))+maxb("numOfComponents")/2.0-(maxb("edges")-(minb("nodes"))+maxb("numOfComponents")/(4.0*log(maxb("edges")-(minb("nodes"))+maxb("numOfComponents"))/log(2.0))), ind='Max')
        except:
            pass
        try:
            set("edges",  minb("nodes")-(maxb("numOfComponents"))+exp(-(0.173286795139986*maxb("numOfComponents")/(1.0*minb("genus")-(0.5*maxb("numOfComponents"))))), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("edges")+maxb("numOfComponents")-(exp(-(0.173286795139986*maxb("numOfComponents")/(1.0*minb("genus")-(0.5*maxb("numOfComponents")))))), ind='Max')
        except:
            pass
        return

