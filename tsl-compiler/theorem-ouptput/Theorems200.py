class Theorem181(Theorem):
    def __init__(self):
        super(Theorem181, self).__init__(181, "if nodeCliqueCover > nodeInd then \n{\n    maxdeg >= 3.0*nodes/(3.0*nodeInd-(1.0))-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","nodeInd","maxdeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeCliqueCover") != 'undt'  and maxb("nodeInd") != 'undt'  and minb("nodeCliqueCover") > maxb("nodeInd")):
            if minb("nodes") != 'undt'  and maxb("nodeInd") != 'undt' :
                try:
                    set("maxdeg",  3.0*minb("nodes")/(3.0*maxb("nodeInd")-(1.0))-(1.0), ind='Min')
                except:
                    pass
            
            
            if minb("maxdeg") != 'undt'  and maxb("nodeInd") != 'undt' :
                try:
                    set("nodes",  minb("maxdeg")*maxb("nodeInd")-(minb("maxdeg")/3.0)+maxb("nodeInd")-(1.0/3.0), ind='Max')
                except:
                    pass
            
            
            if maxb("maxdeg") != 'undt'  and minb("nodes") != 'undt' :
                try:
                    set("nodeInd",  (maxb("maxdeg")+3.0*minb("nodes")+1.0)/(3.0*(maxb("maxdeg")+1.0)), ind='Min')
                except:
                    pass
            
        
        return

class Theorem182(Theorem):
    def __init__(self):
        super(Theorem182, self).__init__(182, "maxClique >= 2.0*nodes/(nodes-(mindeg)+nodeInd);", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","mindeg","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt'  and minb("mindeg") != 'undt'  and maxb("nodeInd") != 'undt' :
            try:
                set("maxClique",  2.0*maxb("nodes")/(maxb("nodes")-(minb("mindeg"))+maxb("nodeInd")), ind='Min')
            except:
                pass
        
        if maxb("maxClique") != 'undt'  and minb("mindeg") != 'undt'  and maxb("nodeInd") != 'undt' :
            try:
                set("nodes",  maxb("maxClique")*(minb("mindeg")-(maxb("nodeInd")))/(maxb("maxClique")-(2.0)), ind='Min')
            except:
                pass
        
        if maxb("nodeInd") != 'undt'  and minb("nodes") != 'undt'  and maxb("maxClique") != 'undt' :
            try:
                set("mindeg",  maxb("nodeInd")+minb("nodes")-(2.0*minb("nodes")/maxb("maxClique")), ind='Max')
            except:
                pass
        
        if minb("mindeg") != 'undt'  and maxb("nodes") != 'undt'  and maxb("maxClique") != 'undt' :
            try:
                set("nodeInd",  minb("mindeg")-(maxb("nodes"))+2.0*maxb("nodes")/maxb("maxClique"), ind='Min')
            except:
                pass
        
        return

class Theorem183(Theorem):
    def __init__(self):
        super(Theorem183, self).__init__(183, "if nodeInd <= 2.0 then \n{\n    maxClique >= (1.0/2.0)*(sqrt(9.0+8.0*nodes)-(3.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","maxClique","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodeInd") != 'undt'  and maxb("nodeInd") <= 2.0):
            if minb("nodes") != 'undt' :
                try:
                    set("maxClique",  (1.0/2.0)*(sqrt(9.0+8.0*minb("nodes"))-(3.0)), ind='Min')
                except:
                    pass
            
            
            if maxb("maxClique") != 'undt' :
                try:
                    set("nodes",  maxb("maxClique")*(maxb("maxClique")+3.0)/2.0, ind='Max')
                except:
                    pass
            
        
        return

class Theorem184(Theorem):
    def __init__(self):
        super(Theorem184, self).__init__(184, "edges >= (1.0/2.0)*nodes*(nodes-(1.0))-((nodes-(maxClique))*(nodes-(mindeg)-(1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt'  and minb("maxClique") != 'undt'  and minb("mindeg") != 'undt' :
            try:
                set("edges",  (1.0/2.0)*maxb("nodes")*(maxb("nodes")-(1.0))-((maxb("nodes")-(minb("maxClique")))*(maxb("nodes")-(minb("mindeg"))-(1.0))), ind='Min')
            except:
                pass
        
        if minb("maxClique") != 'undt'  and minb("mindeg") != 'undt'  and maxb("edges") != 'undt' :
            try:
                set("nodes",  minb("maxClique")+minb("mindeg")+sqrt(-(8.0*maxb("edges"))+4.0*minb("maxClique")**2.0-(4.0*minb("maxClique"))+4.0*minb("mindeg")**2.0+4.0*minb("mindeg")+1.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        
        if minb("edges") != 'undt'  and minb("mindeg") != 'undt'  and minb("nodes") != 'undt' :
            try:
                set("maxClique",  (-(minb("edges"))+minb("mindeg")*minb("nodes")-(minb("nodes")**2.0/2.0)+minb("nodes")/2.0)/(minb("mindeg")-(minb("nodes"))+1.0), ind='Max')
            except:
                pass
        
        if minb("edges") != 'undt'  and minb("maxClique") != 'undt'  and minb("nodes") != 'undt' :
            try:
                set("mindeg",  (-(minb("edges"))+minb("maxClique")*minb("nodes")-(minb("maxClique"))-(minb("nodes")**2.0/2.0)+minb("nodes")/2.0)/(minb("maxClique")-(minb("nodes"))), ind='Max')
            except:
                pass
        
        return

class Theorem185(Theorem):
    def __init__(self):
        super(Theorem185, self).__init__(185, "if nodeCliqueCover <= 2.0 then \n{\n    maxClique == chromaticNum\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","maxClique","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodeCliqueCover") != 'undt'  and maxb("nodeCliqueCover") <= 2.0):
            if minb("chromaticNum") != 'undt' :
                try:
                    set("maxClique",  minb("chromaticNum"), ind='Min')
                except:
                    pass
            
            
            if maxb("maxClique") != 'undt' :
                try:
                    set("chromaticNum",  maxb("maxClique"), ind='Max')
                except:
                    pass
            
            
            if maxb("chromaticNum") != 'undt' :
                try:
                    set("maxClique",  maxb("chromaticNum"), ind='Max')
                except:
                    pass
            
            
            if minb("maxClique") != 'undt' :
                try:
                    set("chromaticNum",  minb("maxClique"), ind='Min')
                except:
                    pass
            
        
        return

class Theorem186(Theorem):
    def __init__(self):
        super(Theorem186, self).__init__(186, "if nodeInd == 2.0 and nodeCliqueCover >= 4.0 then \n{\n    nodes >= 11.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("nodeInd") != 'undt'  and minb("nodeInd") >= 2.0) and (maxb("nodeInd") != 'undt'  and maxb("nodeInd") <= 2.0)) and (minb("nodeCliqueCover") != 'undt'  and minb("nodeCliqueCover") >= 4.0):
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        
        return

class Theorem187(Theorem):
    def __init__(self):
        super(Theorem187, self).__init__(187, "if regular and maxdeg <= nodes-(2.0) then \n{\n    maxClique <= (1.0/2.0)*nodes-((nodeInd-(1.0))*(nodeInd-(2.0))/(2.0*(nodes-(maxdeg)-(1.0))))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","maxdeg","nodes","maxClique","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True  and (maxb("maxdeg") != 'undt'  and minb("nodes") != 'undt'  and maxb("maxdeg") <= minb("nodes")-(2.0)):
            if maxb("nodes") != 'undt'  and minb("nodeInd") != 'undt'  and minb("maxdeg") != 'undt' :
                try:
                    set("maxClique",  (1.0/2.0)*maxb("nodes")-((minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))/(2.0*(maxb("nodes")-(minb("maxdeg"))-(1.0)))), ind='Max')
                except:
                    pass
            
            
            if minb("maxClique") != 'undt'  and minb("maxdeg") != 'undt'  and minb("nodeInd") != 'undt' :
                try:
                    set("nodes",  minb("maxClique")+minb("maxdeg")/2.0+sqrt(4.0*minb("maxClique")**2.0-(4.0*minb("maxClique")*minb("maxdeg"))-(4.0*minb("maxClique"))+minb("maxdeg")**2.0+2.0*minb("maxdeg")+4.0*minb("nodeInd")**2.0-(12.0*minb("nodeInd"))+9.0)/2.0+1.0/2.0, ind='Min')
                except:
                    pass
            
            
            if minb("maxClique") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("nodes") != 'undt' :
                try:
                    set("nodeInd",  sqrt(8.0*minb("maxClique")*minb("maxdeg")-(8.0*minb("maxClique")*maxb("nodes"))+8.0*minb("maxClique")-(4.0*minb("maxdeg")*maxb("nodes"))+4.0*maxb("nodes")**2.0-(4.0*maxb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
                except:
                    pass
            
            
            if minb("maxClique") != 'undt'  and minb("nodes") != 'undt'  and maxb("nodeInd") != 'undt' :
                try:
                    set("maxdeg",  (2.0*minb("maxClique")*minb("nodes")-(2.0*minb("maxClique"))+maxb("nodeInd")**2.0-(3.0*maxb("nodeInd"))-(minb("nodes")**2.0)+minb("nodes")+2.0)/(2.0*minb("maxClique")-(minb("nodes"))), ind='Max')
                except:
                    pass
            
        
        return

class Theorem188(Theorem):
    def __init__(self):
        super(Theorem188, self).__init__(188, "if undefined girth then \n{\n    thickness == 1.0\n\n} else  \n{\n    thickness >= edges*(1.0-(2.0/girth))/(nodes-(2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","thickness","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") == 'undt' :
            try:
                set("thickness",  1.0, ind='Min')
            except:
                pass
            try:
                set("thickness",  1.0, ind='Max')
            except:
                pass
        
        elif True:
            if minb("edges") != 'undt'  and minb("girth") != 'undt'  and maxb("nodes") != 'undt' :
                try:
                    set("thickness",  minb("edges")*(1.0-(2.0/minb("girth")))/(maxb("nodes")-(2.0)), ind='Min')
                except:
                    pass
            
            
            if minb("girth") != 'undt'  and maxb("thickness") != 'undt'  and maxb("nodes") != 'undt' :
                try:
                    set("edges",  minb("girth")*maxb("thickness")*(maxb("nodes")-(2.0))/(minb("girth")-(2.0)), ind='Max')
                except:
                    pass
            
            
            if minb("edges") != 'undt'  and maxb("nodes") != 'undt'  and maxb("thickness") != 'undt' :
                try:
                    set("girth",  2.0*minb("edges")/(minb("edges")-(maxb("nodes")*maxb("thickness"))+2.0*maxb("thickness")), ind='Max')
                except:
                    pass
            
            
            if maxb("edges") != 'undt'  and maxb("thickness") != 'undt'  and minb("girth") != 'undt' :
                try:
                    set("nodes",  maxb("edges")/maxb("thickness")-(2.0*maxb("edges")/(minb("girth")*maxb("thickness")))+2.0, ind='Min')
                except:
                    pass
            
        
        return

class Theorem189(Theorem):
    def __init__(self):
        super(Theorem189, self).__init__(189, "if nodes > 10.0 or nodes < 9.0 then \n{\n    thickness <= (nodes+7.0)/6.0\n\n} else if nodes == 9.0 or nodes == 10.0 then \n{\n    thickness <= 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and minb("nodes") > 10.0) or (maxb("nodes") != 'undt'  and maxb("nodes") < 9.0):
            if maxb("nodes") != 'undt' :
                try:
                    set("thickness",  (maxb("nodes")+7.0)/6.0, ind='Max')
                except:
                    pass
            
            
            if minb("thickness") != 'undt' :
                try:
                    set("nodes",  6.0*minb("thickness")-(7.0), ind='Min')
                except:
                    pass
            
        
        elif ((minb("nodes") != 'undt'  and minb("nodes") >= 9.0) and (maxb("nodes") != 'undt'  and maxb("nodes") <= 9.0)) or ((minb("nodes") != 'undt'  and minb("nodes") >= 10.0) and (maxb("nodes") != 'undt'  and maxb("nodes") <= 10.0)):
            try:
                set("thickness",  3.0, ind='Max')
            except:
                pass
        
        return

class Theorem190(Theorem):
    def __init__(self):
        super(Theorem190, self).__init__(190, "thickness <= (1.0/2.0)*(edgeChromatic+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeChromatic") != 'undt' :
            try:
                set("thickness",  (1.0/2.0)*(maxb("edgeChromatic")+1.0), ind='Max')
            except:
                pass
        
        if minb("thickness") != 'undt' :
            try:
                set("edgeChromatic",  2.0*minb("thickness")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem191(Theorem):
    def __init__(self):
        super(Theorem191, self).__init__(191, "thickness <= max(bandwidth/2.0, 1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("bandwidth") != 'undt' :
            try:
                set("thickness",  max(maxb("bandwidth")/2.0, 1.0), ind='Max')
            except:
                pass
        
        return

class Theorem192(Theorem):
    def __init__(self):
        super(Theorem192, self).__init__(192, "if maxClique == 2.0 then \n{\n    nodeInd >= mindeg*(diameter+4.0)/4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeInd","mindeg","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0)):
            if minb("mindeg") != 'undt'  and minb("diameter") != 'undt' :
                try:
                    set("nodeInd",  minb("mindeg")*(minb("diameter")+4.0)/4.0, ind='Min')
                except:
                    pass
            
            
            if maxb("nodeInd") != 'undt'  and minb("diameter") != 'undt' :
                try:
                    set("mindeg",  4.0*maxb("nodeInd")/(minb("diameter")+4.0), ind='Max')
                except:
                    pass
            
            
            if maxb("nodeInd") != 'undt'  and minb("mindeg") != 'undt' :
                try:
                    set("diameter",  -(4.0)+4.0*maxb("nodeInd")/minb("mindeg"), ind='Max')
                except:
                    pass
            
        
        return

class Theorem193(Theorem):
    def __init__(self):
        super(Theorem193, self).__init__(193, "thickness <= (1.0/2.0)*(nodeCover+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt' :
            try:
                set("thickness",  (1.0/2.0)*(maxb("nodeCover")+1.0), ind='Max')
            except:
                pass
        
        if minb("thickness") != 'undt' :
            try:
                set("nodeCover",  2.0*minb("thickness")-(1.0), ind='Min')
            except:
                pass
        
        return

class Theorem194(Theorem):
    def __init__(self):
        super(Theorem194, self).__init__(194, "if maxClique == 9.0 or maxClique == 10.0 then \n{\n    thickness >= 3.0\n\n} else  \n{\n    thickness >= (maxClique+7.0)/6.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt'  and minb("maxClique") >= 9.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 9.0)) or ((minb("maxClique") != 'undt'  and minb("maxClique") >= 10.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 10.0)):
            try:
                set("thickness",  3.0, ind='Min')
            except:
                pass
        
        elif True:
            if minb("maxClique") != 'undt' :
                try:
                    set("thickness",  (minb("maxClique")+7.0)/6.0, ind='Min')
                except:
                    pass
            
            
            if maxb("thickness") != 'undt' :
                try:
                    set("maxClique",  6.0*maxb("thickness")-(7.0), ind='Max')
                except:
                    pass
            
        
        return

class Theorem195(Theorem):
    def __init__(self):
        super(Theorem195, self).__init__(195, "maxClique >= nodes+(1.0/2.0)*(nodeInd-(1.0))*(nodeInd-(2.0))+(nodes/2.0)*(nodes-(1.0))+edges;", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","nodeInd","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt'  and minb("nodeInd") != 'undt'  and minb("edges") != 'undt' :
            try:
                set("maxClique",  minb("nodes")+(1.0/2.0)*(minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))+(minb("nodes")/2.0)*(minb("nodes")-(1.0))+minb("edges"), ind='Min')
            except:
                pass
        
        if minb("edges") != 'undt'  and maxb("maxClique") != 'undt'  and minb("nodeInd") != 'undt' :
            try:
                set("nodes",  sqrt(-(8.0*minb("edges"))+8.0*maxb("maxClique")-(4.0*minb("nodeInd")**2.0)+12.0*minb("nodeInd")-(7.0))/2.0-(1.0/2.0), ind='Max')
            except:
                pass
        
        if minb("edges") != 'undt'  and maxb("maxClique") != 'undt'  and minb("nodes") != 'undt' :
            try:
                set("nodeInd",  sqrt(-(8.0*minb("edges"))+8.0*maxb("maxClique")-(4.0*minb("nodes")**2.0)-(4.0*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        
        if maxb("maxClique") != 'undt'  and minb("nodeInd") != 'undt'  and minb("nodes") != 'undt' :
            try:
                set("edges",  maxb("maxClique")-(minb("nodeInd")**2.0/2.0)+3.0*minb("nodeInd")/2.0-(minb("nodes")**2.0/2.0)-(minb("nodes")/2.0)-(1.0), ind='Max')
            except:
                pass
        
        return

class Theorem196(Theorem):
    def __init__(self):
        super(Theorem196, self).__init__(196, "edges <= (nodes/2.0)*(nodes-(1.0))-(maxClique*(nodes-(maxdeg)-(1.0)))-((1.0/2.0)*(nodeInd-(1.0))*(nodeInd-(2.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","maxClique","maxdeg","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt'  and minb("maxClique") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("nodeInd") != 'undt' :
            try:
                set("edges",  (maxb("nodes")/2.0)*(maxb("nodes")-(1.0))-(minb("maxClique")*(maxb("nodes")-(maxb("maxdeg"))-(1.0)))-((1.0/2.0)*(minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))), ind='Max')
            except:
                pass
        
        if minb("maxClique") != 'undt'  and minb("edges") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("nodeInd") != 'undt' :
            try:
                set("nodes",  minb("maxClique")+sqrt(8.0*minb("edges")+4.0*minb("maxClique")**2.0-(8.0*minb("maxClique")*maxb("maxdeg"))-(4.0*minb("maxClique"))+4.0*minb("nodeInd")**2.0-(12.0*minb("nodeInd"))+9.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        
        if maxb("edges") != 'undt'  and maxb("nodeInd") != 'undt'  and minb("nodes") != 'undt'  and minb("maxdeg") != 'undt' :
            try:
                set("maxClique",  (2.0*maxb("edges")+maxb("nodeInd")**2.0-(3.0*maxb("nodeInd"))-(minb("nodes")**2.0)+minb("nodes")+2.0)/(2.0*(minb("maxdeg")-(minb("nodes"))+1.0)), ind='Max')
            except:
                pass
        
        if minb("edges") != 'undt'  and maxb("maxClique") != 'undt'  and maxb("nodes") != 'undt'  and minb("nodeInd") != 'undt' :
            try:
                set("maxdeg",  (2.0*minb("edges")+2.0*maxb("maxClique")*(maxb("nodes")-(1.0))+minb("nodeInd")**2.0-(3.0*minb("nodeInd"))-(maxb("nodes")**2.0)+maxb("nodes")+2.0)/(2.0*maxb("maxClique")), ind='Min')
            except:
                pass
        
        if minb("edges") != 'undt'  and minb("maxClique") != 'undt'  and maxb("maxdeg") != 'undt'  and maxb("nodes") != 'undt' :
            try:
                set("nodeInd",  sqrt(-(8.0*minb("edges"))+8.0*minb("maxClique")*maxb("maxdeg")-(8.0*minb("maxClique")*maxb("nodes"))+8.0*minb("maxClique")+4.0*maxb("nodes")**2.0-(4.0*maxb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        
        return

class Theorem197(Theorem):
    def __init__(self):
        super(Theorem197, self).__init__(197, "if nodes >= 3.0 then \n{\n    edgeCliqueCover <= thickness*(2.0*nodes-(numOfComponents)-(3.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeCliqueCover","thickness","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and minb("nodes") >= 3.0):
            if maxb("thickness") != 'undt'  and maxb("nodes") != 'undt'  and minb("numOfComponents") != 'undt' :
                try:
                    set("edgeCliqueCover",  maxb("thickness")*(2.0*maxb("nodes")-(minb("numOfComponents"))-(3.0)), ind='Max')
                except:
                    pass
            
            
            if minb("edgeCliqueCover") != 'undt'  and maxb("nodes") != 'undt'  and minb("numOfComponents") != 'undt' :
                try:
                    set("thickness",  minb("edgeCliqueCover")/(2.0*maxb("nodes")-(minb("numOfComponents"))-(3.0)), ind='Min')
                except:
                    pass
            
            
            if minb("edgeCliqueCover") != 'undt'  and maxb("thickness") != 'undt'  and minb("numOfComponents") != 'undt' :
                try:
                    set("nodes",  (minb("edgeCliqueCover")+maxb("thickness")*(minb("numOfComponents")+3.0))/(2.0*maxb("thickness")), ind='Min')
                except:
                    pass
            
            
            if minb("edgeCliqueCover") != 'undt'  and maxb("thickness") != 'undt'  and maxb("nodes") != 'undt' :
                try:
                    set("numOfComponents",  -(minb("edgeCliqueCover")/maxb("thickness"))+2.0*maxb("nodes")-(3.0), ind='Max')
                except:
                    pass
            
        
        return

class Theorem198(Theorem):
    def __init__(self):
        super(Theorem198, self).__init__(198, "nodeCover <= nodes-(nodes/chromaticNum);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt'  and maxb("chromaticNum") != 'undt' :
            try:
                set("nodeCover",  minb("nodes")-(minb("nodes")/maxb("chromaticNum")), ind='Max')
            except:
                pass
        
        if minb("chromaticNum") != 'undt'  and maxb("nodeCover") != 'undt' :
            try:
                set("nodes",  minb("chromaticNum")*maxb("nodeCover")/(minb("chromaticNum")-(1.0)), ind='Max')
            except:
                pass
        
        if maxb("nodes") != 'undt'  and minb("nodeCover") != 'undt' :
            try:
                set("chromaticNum",  -(maxb("nodes")/(minb("nodeCover")-(maxb("nodes")))), ind='Min')
            except:
                pass
        
        return

class Theorem199(Theorem):
    def __init__(self):
        super(Theorem199, self).__init__(199, "bandwidth <= nodes-(1.0)-((nodes-(nodeCover))/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt'  and maxb("nodeCover") != 'undt' :
            try:
                set("bandwidth",  minb("nodes")-(1.0)-((minb("nodes")-(maxb("nodeCover")))/2.0), ind='Max')
            except:
                pass
        
        if maxb("bandwidth") != 'undt'  and minb("nodeCover") != 'undt' :
            try:
                set("nodes",  2.0*maxb("bandwidth")-(minb("nodeCover"))+2.0, ind='Max')
            except:
                pass
        
        if minb("bandwidth") != 'undt'  and maxb("nodes") != 'undt' :
            try:
                set("nodeCover",  2.0*minb("bandwidth")-(maxb("nodes"))+2.0, ind='Min')
            except:
                pass
        
        return

class Theorem200(Theorem):
    def __init__(self):
        super(Theorem200, self).__init__(200, "if nodes > 2.0*edgeInd+1.0 then \n{\n    nodeCover <= 2.0*edgeInd-(nodeConnec)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeInd","nodeCover","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and maxb("edgeInd") != 'undt'  and minb("nodes") > 2.0*maxb("edgeInd")+1.0):
            if maxb("edgeInd") != 'undt'  and minb("nodeConnec") != 'undt' :
                try:
                    set("nodeCover",  2.0*maxb("edgeInd")-(minb("nodeConnec")), ind='Max')
                except:
                    pass
            
            
            if minb("nodeConnec") != 'undt'  and minb("nodeCover") != 'undt' :
                try:
                    set("edgeInd",  minb("nodeConnec")/2.0+minb("nodeCover")/2.0, ind='Min')
                except:
                    pass
            
            
            if maxb("edgeInd") != 'undt'  and minb("nodeCover") != 'undt' :
                try:
                    set("nodeConnec",  2.0*maxb("edgeInd")-(minb("nodeCover")), ind='Max')
                except:
                    pass
            
        
        return

