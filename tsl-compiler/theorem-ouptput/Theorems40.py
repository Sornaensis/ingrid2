class Theorem21(Theorem):
    def __init__(self):
        super(Theorem21, self).__init__(21, "genus <= ((nodes-(3.0))*(nodes-(4.0))+11.0)/12.0;", "")
    def involves(self, str_invar):
        return str_invar in ["genus","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("genus",  ((maxb("nodes")-(3.0))*(maxb("nodes")-(4.0))+11.0)/12.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  sqrt(48.0*minb("genus")-(43.0))/2.0+7.0/2.0, ind='Min')
        except:
            pass
        return

class Theorem22(Theorem):
    def __init__(self):
        super(Theorem22, self).__init__(22, "if edges > maxdeg*edgeInd then \n{\n    edgeChromatic == maxdeg+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","edgeInd","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt'  and maxb("maxdeg") != 'undt'  and maxb("edgeInd") != 'undt'  and minb("edges") > maxb("maxdeg")*maxb("edgeInd")):
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

class Theorem23(Theorem):
    def __init__(self):
        super(Theorem23, self).__init__(23, "edgeCliqueCover <= edgeCover*edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edgeCover","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCliqueCover",  maxb("edgeCover")*maxb("edgeInd"), ind='Max')
        except:
            pass
        try:
            set("edgeCover",  minb("edgeCliqueCover")/maxb("edgeInd"), ind='Min')
        except:
            pass
        try:
            set("edgeInd",  minb("edgeCliqueCover")/maxb("edgeCover"), ind='Min')
        except:
            pass
        return

class Theorem24(Theorem):
    def __init__(self):
        super(Theorem24, self).__init__(24, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        return

class Theorem25(Theorem):
    def __init__(self):
        super(Theorem25, self).__init__(25, "edgeCover >= (1.0/2.0)*nodes;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCover",  (1.0/2.0)*minb("nodes"), ind='Min')
        except:
            pass
        try:
            set("nodes",  2.0*maxb("edgeCover"), ind='Max')
        except:
            pass
        return

class Theorem26(Theorem):
    def __init__(self):
        super(Theorem26, self).__init__(26, "edges <= (1.0/2.0)*(nodes-(1.0))*(nodes-(2.0))+nodes/domination-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  (1.0/2.0)*(maxb("nodes")-(1.0))*(maxb("nodes")-(2.0))+maxb("nodes")/minb("domination")-(1.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  (3.0*maxb("domination")+sqrt(8.0*maxb("domination")**2.0*minb("edges")+9.0*maxb("domination")**2.0-(12.0*maxb("domination"))+4.0)-(2.0))/(2.0*maxb("domination")), ind='Min')
        except:
            pass
        try:
            set("domination",  2.0*maxb("nodes")/(2.0*minb("edges")-(maxb("nodes")**2.0)+3.0*maxb("nodes")), ind='Max')
        except:
            pass
        return

class Theorem27(Theorem):
    def __init__(self):
        super(Theorem27, self).__init__(27, "edgeCover <= nodes*maxdeg/(1.0+maxdeg);", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCover",  maxb("nodes")*minb("maxdeg")/(1.0+minb("maxdeg")), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("edgeCover")+minb("edgeCover")/maxb("maxdeg"), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  -(maxb("edgeCover")/(maxb("edgeCover")-(minb("nodes")))), ind='Max')
        except:
            pass
        return

class Theorem28(Theorem):
    def __init__(self):
        super(Theorem28, self).__init__(28, "if exists diameter then \n{\n    if diameter <= 3.0 then \n    {\n        maxdeg <= nodes-(diameter)+1.0\n    \n    } else  \n    {\n        maxdeg <= nodes-(nodeConnec*(diameter-(4.0)))-(3.0)\n    \n    }\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("diameter") != 'undt' :
            if (maxb("diameter") != 'undt'  and maxb("diameter") <= 3.0):
                try:
                    set("maxdeg",  maxb("nodes")-(minb("diameter"))+1.0, ind='Max')
                except:
                    pass
                try:
                    set("nodes",  minb("diameter")+minb("maxdeg")-(1.0), ind='Min')
                except:
                    pass
                try:
                    set("diameter",  -(minb("maxdeg"))+maxb("nodes")+1.0, ind='Max')
                except:
                    pass
            
            elif True:
                try:
                    set("maxdeg",  maxb("nodes")-(minb("nodeConnec")*(minb("diameter")-(4.0)))-(3.0), ind='Max')
                except:
                    pass
                try:
                    set("nodes",  minb("diameter")*maxb("nodeConnec")+minb("maxdeg")-(4.0*maxb("nodeConnec"))+3.0, ind='Min')
                except:
                    pass
                try:
                    set("nodeConnec",  (-(minb("maxdeg"))+maxb("nodes")-(3.0))/(minb("diameter")-(4.0)), ind='Max')
                except:
                    pass
                try:
                    set("diameter",  (-(minb("maxdeg"))+4.0*minb("nodeConnec")+maxb("nodes")-(3.0))/minb("nodeConnec"), ind='Max')
                except:
                    pass
            
        
        return

class Theorem29(Theorem):
    def __init__(self):
        super(Theorem29, self).__init__(29, "edgeCliqueCover <= edges-((1.0/2.0)*maxClique(maxClique-(1.0)))+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edges","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCliqueCover",  maxb("edges")-((1.0/2.0)*maxClique(minb("maxClique")-(1.0)))+1.0, ind='Max')
        except:
            pass
        try:
            set("edges",  maxClique(minb("maxClique")-(1.0))/2.0+minb("edgeCliqueCover")-(1.0), ind='Min')
        except:
            pass
        return

class Theorem30(Theorem):
    def __init__(self):
        super(Theorem30, self).__init__(30, "if connected and radius <= min(2.0, nodes/2.0) then \n{\n    edges <= (1.0/2.0)*nodes*(nodes-(radius))\n\n} else if connected and radius >= 3.0 and radius <= nodes/2.0 then \n{\n    edges <= (1.0/2.0)*(nodes**2.0+4.0*radius*nodes+5.0*nodes+4.0*radius**2.0-(6.0*radius))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","radius","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True  and (maxb("radius") != 'undt'  and minb("nodes") != 'undt'  and maxb("radius") <= min(2.0, minb("nodes")/2.0)):
            try:
                set("edges",  (1.0/2.0)*maxb("nodes")*(maxb("nodes")-(minb("radius"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("radius")/2.0+sqrt(8.0*minb("edges")+minb("radius")**2.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("radius",  -(2.0*minb("edges")/maxb("nodes"))+maxb("nodes"), ind='Max')
            except:
                pass
        
        elif get("connected") == True  and (minb("radius") != 'undt'  and minb("radius") >= 3.0) and (maxb("radius") != 'undt'  and minb("nodes") != 'undt'  and maxb("radius") <= minb("nodes")/2.0):
            try:
                set("edges",  (1.0/2.0)*(maxb("nodes")**2.0+4.0*maxb("radius")*maxb("nodes")+5.0*maxb("nodes")+4.0*maxb("radius")**2.0-(6.0*maxb("radius"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  -(2.0*maxb("radius"))+sqrt(8.0*minb("edges")+64.0*maxb("radius")+25.0)/2.0-(5.0/2.0), ind='Min')
            except:
                pass
            try:
                set("radius",  -(maxb("nodes")/2.0)+sqrt(8.0*minb("edges")-(32.0*maxb("nodes"))+9.0)/4.0+3.0/4.0, ind='Min')
            except:
                pass
        
        return

class Theorem31(Theorem):
    def __init__(self):
        super(Theorem31, self).__init__(31, "chromaticNum <= (nodes+1.0)**2.0/(4.0*nodeCliqueCover);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodes","nodeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  (maxb("nodes")+1.0)**2.0/(4.0*minb("nodeCliqueCover")), ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*sqrt(minb("chromaticNum")*minb("nodeCliqueCover"))-(1.0), ind='Min')
        except:
            pass
        try:
            set("nodeCliqueCover",  (maxb("nodes")+1.0)**2.0/(4.0*minb("chromaticNum")), ind='Max')
        except:
            pass
        return

class Theorem32(Theorem):
    def __init__(self):
        super(Theorem32, self).__init__(32, "chromaticNum >= 2.0*nodes**(1.0/2.0)-(nodeCliqueCover);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodes","nodeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  2.0*minb("nodes")**(1.0/2.0)-(maxb("nodeCliqueCover")), ind='Min')
        except:
            pass
        try:
            set("nodes",  (maxb("chromaticNum")+maxb("nodeCliqueCover"))**2.0/4.0, ind='Max')
        except:
            pass
        try:
            set("nodeCliqueCover",  -(maxb("chromaticNum"))+2.0*sqrt(minb("nodes")), ind='Min')
        except:
            pass
        return

class Theorem33(Theorem):
    def __init__(self):
        super(Theorem33, self).__init__(33, "domination <= nodes+1.0-((1.0+2.0*edges)**(1.0/2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("domination",  maxb("nodes")+1.0-((1.0+2.0*minb("edges"))**(1.0/2.0)), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("domination")+sqrt(2.0*minb("edges")+1.0)-(1.0), ind='Min')
        except:
            pass
        try:
            set("edges",  (-(minb("domination"))+maxb("nodes")+1.0)**2.0/2.0-(1.0/2.0), ind='Max')
        except:
            pass
        return

class Theorem34(Theorem):
    def __init__(self):
        super(Theorem34, self).__init__(34, "if nodeConnec > 0.0 and not tree then \n{\n    girth <= 2.0*diameter+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","tree","girth","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt'  and minb("nodeConnec") > 0.0) and get("tree") == False :
            try:
                set("girth",  2.0*maxb("diameter")+1.0, ind='Max')
            except:
                pass
            try:
                set("diameter",  minb("girth")/2.0-(1.0/2.0), ind='Min')
            except:
                pass
        
        return

class Theorem35(Theorem):
    def __init__(self):
        super(Theorem35, self).__init__(35, "if planar and maxClique < 3.0 then \n{\n    nodeInd >= (1.0/3.0)*(nodes+1.0),\n    nodeCover <= (2.0*nodes-(1.0))/3.0\n\n} else if planar and (nodeInd < (1.0/3.0)*(nodes+1.0) or nodeCover > (2.0*nodes-(1.0))/3.0) then \n{\n    maxClique >= 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","maxClique","nodeInd","nodes","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True  and (maxb("maxClique") != 'undt'  and maxb("maxClique") < 3.0):
            try:
                set("nodeInd",  (1.0/3.0)*(minb("nodes")+1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  3.0*maxb("nodeInd")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  (2.0*maxb("nodes")-(1.0))/3.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  3.0*minb("nodeCover")/2.0+1.0/2.0, ind='Min')
            except:
                pass
        
        elif get("planar") == True  and ((maxb("nodeInd") != 'undt'  and minb("nodes") != 'undt'  and maxb("nodeInd") < (1.0/3.0)*(minb("nodes")+1.0)) or (minb("nodeCover") != 'undt'  and maxb("nodes") != 'undt'  and minb("nodeCover") > (2.0*maxb("nodes")-(1.0))/3.0)):
            try:
                set("maxClique",  3.0, ind='Min')
            except:
                pass
        
        return

class Theorem36(Theorem):
    def __init__(self):
        super(Theorem36, self).__init__(36, "if not planar then \n{\n    maxdeg >= 3.0,\n    nodes >= 5.0,\n    edges >= 9.0,\n    edgeInd >= 2.0,\n    nodeCover >= 3.0,\n    edgeCover >= 3.0,\n    bandwidth >= 4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","maxdeg","nodes","edges","edgeInd","nodeCover","edgeCover","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == False :
            try:
                set("maxdeg",  3.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  5.0, ind='Min')
            except:
                pass
            try:
                set("edges",  9.0, ind='Min')
            except:
                pass
            try:
                set("edgeInd",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeCover",  3.0, ind='Min')
            except:
                pass
            try:
                set("edgeCover",  3.0, ind='Min')
            except:
                pass
            try:
                set("bandwidth",  4.0, ind='Min')
            except:
                pass
        
        return

class Theorem37(Theorem):
    def __init__(self):
        super(Theorem37, self).__init__(37, "edges <= numOfComponents-(1.0)+(nodes+2.0-(2.0*numOfComponents))*(nodes+1.0-(2.0*numOfComponents))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","numOfComponents","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  minb("numOfComponents")-(1.0)+(maxb("nodes")+2.0-(2.0*minb("numOfComponents")))*(maxb("nodes")+1.0-(2.0*minb("numOfComponents")))/2.0, ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  maxb("nodes")/2.0+sqrt(2.0*maxb("edges")-(maxb("nodes"))+1.0)/2.0+1.0/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*minb("numOfComponents")+sqrt(8.0*minb("edges")-(8.0*minb("numOfComponents"))+9.0)/2.0-(3.0/2.0), ind='Min')
        except:
            pass
        return

class Theorem38(Theorem):
    def __init__(self):
        super(Theorem38, self).__init__(38, "domination >= nodes/(maxdeg+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("domination",  minb("nodes")/(maxb("maxdeg")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("domination")*(maxb("maxdeg")+1.0), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  (-(maxb("domination"))+minb("nodes"))/maxb("domination"), ind='Min')
        except:
            pass
        return

class Theorem39(Theorem):
    def __init__(self):
        super(Theorem39, self).__init__(39, "if girth >= 4.0 or maxClique <= 2.0 then \n{\n    maxClique <= 2.0,\n    girth >= 4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt'  and minb("girth") >= 4.0) or (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0):
            try:
                set("maxClique",  2.0, ind='Max')
            except:
                pass
            try:
                set("girth",  4.0, ind='Min')
            except:
                pass
        
        return

class Theorem40(Theorem):
    def __init__(self):
        super(Theorem40, self).__init__(40, "if complete or mindeg == nodes-(1.0) or nodeInd == 1.0 or nodeCliqueCover == 1.0 or edgeCliqueCover == 1.0 or diameter == 1.0 then \n{\n    complete,\n    mindeg == nodes-(1.0),\n    nodeInd == 1.0,\n    nodeCliqueCover == 1.0,\n    edgeCliqueCover == 1.0,\n    diameter == 1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["complete","mindeg","nodes","nodeInd","nodeCliqueCover","edgeCliqueCover","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("complete") == True  or (minb("mindeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("mindeg") >= maxb("nodes")-(1.0)) and (maxb("mindeg") != 'undt'  and minb("nodes") != 'undt'  and maxb("mindeg") <= minb("nodes")-(1.0)) or (minb("nodeInd") != 'undt'  and minb("nodeInd") >= 1.0) and (maxb("nodeInd") != 'undt'  and maxb("nodeInd") <= 1.0) or (minb("nodeCliqueCover") != 'undt'  and minb("nodeCliqueCover") >= 1.0) and (maxb("nodeCliqueCover") != 'undt'  and maxb("nodeCliqueCover") <= 1.0) or (minb("edgeCliqueCover") != 'undt'  and minb("edgeCliqueCover") >= 1.0) and (maxb("edgeCliqueCover") != 'undt'  and maxb("edgeCliqueCover") <= 1.0) or (minb("diameter") != 'undt'  and minb("diameter") >= 1.0) and (maxb("diameter") != 'undt'  and maxb("diameter") <= 1.0):
            set("complete", True )
            try:
                set("mindeg",  minb("nodes")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("mindeg")+1.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  maxb("nodes")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("mindeg")+1.0, ind='Min')
            except:
                pass
            try:
                set("nodeInd",  1.0, ind='Min')
            except:
                pass
            try:
                set("nodeInd",  1.0, ind='Max')
            except:
                pass
            try:
                set("nodeCliqueCover",  1.0, ind='Min')
            except:
                pass
            try:
                set("nodeCliqueCover",  1.0, ind='Max')
            except:
                pass
            try:
                set("edgeCliqueCover",  1.0, ind='Min')
            except:
                pass
            try:
                set("edgeCliqueCover",  1.0, ind='Max')
            except:
                pass
            try:
                set("diameter",  1.0, ind='Min')
            except:
                pass
            try:
                set("diameter",  1.0, ind='Max')
            except:
                pass
        
        return

