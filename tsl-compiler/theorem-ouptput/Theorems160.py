class Theorem141(Theorem):
    def __init__(self):
        super(Theorem141, self).__init__(141, "circumference >= 2.0*edges/(nodes-(1.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("edges") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("circumference",  2.0*minb("edges")/(maxb("nodes")-(1.0)), ind='Min')
            except:
                pass
        if maxb("circumference") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  maxb("circumference")*(maxb("nodes")-(1.0))/2.0, ind='Max')
            except:
                pass
        if minb("circumference") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodes",  (minb("circumference")+2.0*minb("edges"))/minb("circumference"), ind='Min')
            except:
                pass
        return

class Theorem142(Theorem):
    def __init__(self):
        super(Theorem142, self).__init__(142, ";\n", "REPLACED BY R343")
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

class Theorem143(Theorem):
    def __init__(self):
        super(Theorem143, self).__init__(143, "nodeCliqueCover <= (1.0/2.0)+sqrt(1.0/4.0+nodes**2.0-(nodes)-(2.0*edges));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodeCliqueCover",  (1.0/2.0)+sqrt(1.0/4.0+maxb("nodes")**2.0-(maxb("nodes"))-(2.0*minb("edges"))), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  sqrt(8.0*minb("edges")+(2.0*minb("nodeCliqueCover")-(1.0))**2.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        if minb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  -(minb("nodeCliqueCover")**2.0/2.0)+minb("nodeCliqueCover")/2.0+maxb("nodes")**2.0/2.0-(maxb("nodes")/2.0), ind='Max')
            except:
                pass
        return

class Theorem144(Theorem):
    def __init__(self):
        super(Theorem144, self).__init__(144, "chromaticNum <= 1.0/2.0+sqrt(1.0/4.0+2.0*edges);\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edges") != 'undt':
            try:
                set("chromaticNum",  1.0/2.0+sqrt(1.0/4.0+2.0*maxb("edges")), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("edges",  minb("chromaticNum")*(minb("chromaticNum")-(1.0))/2.0, ind='Min')
            except:
                pass
        return

class Theorem145(Theorem):
    def __init__(self):
        super(Theorem145, self).__init__(145, "if maxClique == 2.0 then \n{\n    nodeInd >= 1.0/2.0*sqrt(8.0*nodes+9.0)-(3.0)\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeInd","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if minb("nodes") != 'undt':
                try:
                    set("nodeInd",  1.0/2.0*sqrt(8.0*minb("nodes")+9.0)-(3.0), ind='Min')
                except:
                    pass
            
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  (maxb("nodeInd")+3.0)**2.0/2.0-(9.0/8.0), ind='Max')
                except:
                    pass
        return

class Theorem146(Theorem):
    def __init__(self):
        super(Theorem146, self).__init__(146, "if connected then \n{\n    bandwidth <= nodes-(diam)\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","bandwidth","nodes","diam"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if maxb("nodes") != 'undt' and minb("diam") != 'undt':
                try:
                    set("bandwidth",  maxb("nodes")-(minb("diam")), ind='Max')
                except:
                    pass
            
            if minb("bandwidth") != 'undt' and minb("diam") != 'undt':
                try:
                    set("nodes",  minb("bandwidth")+minb("diam"), ind='Min')
                except:
                    pass
            
            if minb("bandwidth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("diam",  -(minb("bandwidth"))+maxb("nodes"), ind='Max')
                except:
                    pass
        return

class Theorem147(Theorem):
    def __init__(self):
        super(Theorem147, self).__init__(147, "if maxClique == 2.0 and (maxdeg >= nodes-(2.0) or nodes <= 4.0) then \n{\n    chromaticNum <= 2.0\n\n} else if maxClique == 2.0 and nodes >= 5.0 and nodes <= 10.0 then \n{\n    chromaticNum <= 3.0\n\n} else if maxClique == 2.0 then \n{\n    chromaticNum <= (nodes-(maxdeg)+10.0)/4.0\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","nodes","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(2.0)) or (maxb("nodes") != 'undt' and maxb("nodes") <= 4.0)):
            try:
                set("chromaticNum",  2.0, ind='Max')
            except:
                pass
        
        elif ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (minb("nodes") != 'undt' and minb("nodes") >= 5.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 10.0):
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        
        elif ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("chromaticNum",  (maxb("nodes")-(minb("maxdeg"))+10.0)/4.0, ind='Max')
                except:
                    pass
            
            if minb("chromaticNum") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  4.0*minb("chromaticNum")+minb("maxdeg")-(10.0), ind='Min')
                except:
                    pass
            
            if minb("chromaticNum") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(4.0*minb("chromaticNum"))+maxb("nodes")+10.0, ind='Max')
                except:
                    pass
        return

class Theorem148(Theorem):
    def __init__(self):
        super(Theorem148, self).__init__(148, "if mindeg == 3.0 and maxdeg == 3.0 and planar and edgeConnec >= 2.0 then \n{\n    edgeChromatic == maxdeg\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","planar","edgeConnec","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and minb("mindeg") >= 3.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 3.0)) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and get("planar") == True and (minb("edgeConnec") != 'undt' and minb("edgeConnec") >= 2.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  minb("maxdeg"), ind='Min')
                except:
                    pass
            
            if maxb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  maxb("edgeChromatic"), ind='Max')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  maxb("maxdeg"), ind='Max')
                except:
                    pass
            
            if minb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  minb("edgeChromatic"), ind='Min')
                except:
                    pass
        return

class Theorem149(Theorem):
    def __init__(self):
        super(Theorem149, self).__init__(149, "if planar and maxdeg >= 8.0 then \n{\n    edgeChromatic == maxdeg\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","maxdeg","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 8.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  minb("maxdeg"), ind='Min')
                except:
                    pass
            
            if maxb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  maxb("edgeChromatic"), ind='Max')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  maxb("maxdeg"), ind='Max')
                except:
                    pass
            
            if minb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  minb("edgeChromatic"), ind='Min')
                except:
                    pass
        return

class Theorem150(Theorem):
    def __init__(self):
        super(Theorem150, self).__init__(150, "if spectralRadius <= maxdeg/2.0 then \n{\n    edgeChromatic == maxdeg\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","maxdeg","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("spectralRadius") != 'undt' and minb("maxdeg") != 'undt' and maxb("spectralRadius") <= minb("maxdeg")/2.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  minb("maxdeg"), ind='Min')
                except:
                    pass
            
            if maxb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  maxb("edgeChromatic"), ind='Max')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  maxb("maxdeg"), ind='Max')
                except:
                    pass
            
            if minb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  minb("edgeChromatic"), ind='Min')
                except:
                    pass
        return

class Theorem151(Theorem):
    def __init__(self):
        super(Theorem151, self).__init__(151, "if nodes > 2.0 and regular and nodeConnec == 1.0 then \n{\n    edgeChromatic == maxdeg+1.0\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","regular","nodeConnec","edgeChromatic","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt' and minb("nodes") > 2.0) and get("regular") == True and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 1.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 1.0)):
            if minb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  minb("maxdeg")+1.0, ind='Min')
                except:
                    pass
            
            if maxb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  maxb("edgeChromatic")-(1.0), ind='Max')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt':
                try:
                    set("edgeChromatic",  maxb("maxdeg")+1.0, ind='Max')
                except:
                    pass
            
            if minb("edgeChromatic") != 'undt':
                try:
                    set("maxdeg",  minb("edgeChromatic")-(1.0), ind='Min')
                except:
                    pass
        return

class Theorem152(Theorem):
    def __init__(self):
        super(Theorem152, self).__init__(152, "if maxClique == 2.0 and nodeInd >= 2.0*nodes/5.0 and nodeInd <= nodes/2.0 then \n{\n    edges <= nodeInd**2.0+4.0*(nodes/2.0-(nodeInd))**2.0\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeInd","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (minb("nodeInd") != 'undt' and maxb("nodes") != 'undt' and minb("nodeInd") >= 2.0*maxb("nodes")/5.0) and (maxb("nodeInd") != 'undt' and minb("nodes") != 'undt' and maxb("nodeInd") <= minb("nodes")/2.0):
            if minb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("edges",  minb("nodeInd")**2.0+4.0*(maxb("nodes")/2.0-(minb("nodeInd")))**2.0, ind='Max')
                except:
                    pass
            
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodeInd",  2.0*maxb("nodes")/5.0+sqrt(5.0*maxb("edges")-(maxb("nodes")**2.0))/5.0, ind='Max')
                except:
                    pass
            
            if minb("nodeInd") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeInd")+sqrt(minb("edges")-(minb("nodeInd")**2.0)), ind='Min')
                except:
                    pass
        return

class Theorem153(Theorem):
    def __init__(self):
        super(Theorem153, self).__init__(153, "if maxdeg == 2.0 or radius == 1.0 then \n{\n    bandwidth <= maxdeg\n\n} else  \n{\n    bandwidth <= maxdeg*(maxdeg-(1.0))**(radius-(1.0))\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","radius","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0)) or ((minb("radius") != 'undt' and minb("radius") >= 1.0) and (maxb("radius") != 'undt' and maxb("radius") <= 1.0)):
            if maxb("maxdeg") != 'undt':
                try:
                    set("bandwidth",  maxb("maxdeg"), ind='Max')
                except:
                    pass
            
            if minb("bandwidth") != 'undt':
                try:
                    set("maxdeg",  minb("bandwidth"), ind='Min')
                except:
                    pass
        
        elif True:
            if maxb("maxdeg") != 'undt' and maxb("radius") != 'undt':
                try:
                    set("bandwidth",  maxb("maxdeg")*(maxb("maxdeg")-(1.0))**(maxb("radius")-(1.0)), ind='Max')
                except:
                    pass
            
        return

class Theorem154(Theorem):
    def __init__(self):
        super(Theorem154, self).__init__(154, ";\n", "RETIRED by R265")
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

class Theorem155(Theorem):
    def __init__(self):
        super(Theorem155, self).__init__(155, "if mindeg == 2.0 then \n{\n    nodes <= (2.0+max(4.0, maxdeg))/edgeInd/2.0\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","maxdeg","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)):
            if maxb("maxdeg") != 'undt' and minb("edgeInd") != 'undt':
                try:
                    set("nodes",  (2.0+max(4.0, maxb("maxdeg")))/minb("edgeInd")/2.0, ind='Max')
                except:
                    pass
            
        return

class Theorem156(Theorem):
    def __init__(self):
        super(Theorem156, self).__init__(156, "if mindeg <= nodes/2.0 then \n{\n    edgeInd >= mindeg\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("mindeg") != 'undt' and minb("nodes") != 'undt' and maxb("mindeg") <= minb("nodes")/2.0):
            if minb("mindeg") != 'undt':
                try:
                    set("edgeInd",  minb("mindeg"), ind='Min')
                except:
                    pass
            
            if maxb("edgeInd") != 'undt':
                try:
                    set("mindeg",  maxb("edgeInd"), ind='Max')
                except:
                    pass
        return

class Theorem157(Theorem):
    def __init__(self):
        super(Theorem157, self).__init__(157, "if maxClique <= (mindeg-(1.0))/2.0 then \n{\n    chromaticNum <= maxdeg-(1.0)\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","mindeg","chromaticNum","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and minb("mindeg") != 'undt' and maxb("maxClique") <= (minb("mindeg")-(1.0))/2.0):
            if maxb("maxdeg") != 'undt':
                try:
                    set("chromaticNum",  maxb("maxdeg")-(1.0), ind='Max')
                except:
                    pass
            
            if minb("chromaticNum") != 'undt':
                try:
                    set("maxdeg",  minb("chromaticNum")+1.0, ind='Min')
                except:
                    pass
        return

class Theorem158(Theorem):
    def __init__(self):
        super(Theorem158, self).__init__(158, "if connected and edges <= nodes+3.0 then \n{\n    genus <= 0.0\n\n} else if connected and edges <= nodes+6.0 then \n{\n    genus <= 1.0\n\n} else if connected and edges <= nodes+9.0 then \n{\n    genus <= 2.0\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","edges","nodes","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+3.0):
            try:
                set("genus",  0.0, ind='Max')
            except:
                pass
        
        elif get("connected") == True and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+6.0):
            try:
                set("genus",  1.0, ind='Max')
            except:
                pass
        
        elif get("connected") == True and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+9.0):
            try:
                set("genus",  2.0, ind='Max')
            except:
                pass
        return

class Theorem159(Theorem):
    def __init__(self):
        super(Theorem159, self).__init__(159, "nodeInd >= (nodes-(1.0))/(maxdeg+1.0)+1.0/(mindeg+1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","maxdeg","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodeInd",  (minb("nodes")-(1.0))/(maxb("maxdeg")+1.0)+1.0/(maxb("mindeg")+1.0), ind='Min')
            except:
                pass
        if maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodes",  (maxb("maxdeg")*maxb("mindeg")*maxb("nodeInd")+maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg"))+maxb("mindeg")*maxb("nodeInd")+maxb("mindeg")+maxb("nodeInd"))/(maxb("mindeg")+1.0), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt' and maxb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(minb("mindeg")*maxb("nodeInd"))+minb("mindeg")*minb("nodes")-(minb("mindeg"))-(maxb("nodeInd"))+minb("nodes"))/(minb("mindeg")*maxb("nodeInd")+maxb("nodeInd")-(1.0)), ind='Min')
            except:
                pass
        if minb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("mindeg",  (-(minb("maxdeg")*maxb("nodeInd"))+minb("maxdeg")-(maxb("nodeInd"))+minb("nodes"))/(minb("maxdeg")*maxb("nodeInd")+maxb("nodeInd")-(minb("nodes"))+1.0), ind='Min')
            except:
                pass
        return

class Theorem160(Theorem):
    def __init__(self):
        super(Theorem160, self).__init__(160, "if maxClique == 2.0 and maxdeg >= 3.0 then \n{\n    nodeInd >= nodes/(maxdeg-((1.0/5.0)))\n\n} else if maxClique == 2.0 and nodes >= 3.0 and connected and (not cycle or (cycle and isset nodes and even nodes)) and (edges >= nodes or maxdeg > 2.0 or (isset nodes and odd nodes)) then \n{\n    nodeInd >= nodes/maxdeg-(1.0/(maxdeg+1.0))+1.0/(mindeg+1.0)\n\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","nodeInd","nodes","connected","cycle","edges","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
            if minb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodeInd",  minb("nodes")/(maxb("maxdeg")-((1.0/5.0))), ind='Min')
                except:
                    pass
            
            if maxb("nodeInd") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("nodeInd")*(maxb("maxdeg")-(1.0/5.0)), ind='Max')
                except:
                    pass
            
            if minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxdeg",  (minb("nodeInd")/5.0+minb("nodes"))/minb("nodeInd"), ind='Min')
                except:
                    pass
        
        elif ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (minb("nodes") != 'undt' and minb("nodes") >= 3.0) and get("connected") == True and (get("cycle") == False or (get("cycle") == True and maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and evenInvar("nodes"))) and ((minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= maxb("nodes")) or (minb("maxdeg") != 'undt' and minb("maxdeg") > 2.0) or (maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and oddInvar("nodes"))):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("nodeInd",  minb("nodes")/minb("maxdeg")-(1.0/(minb("maxdeg")+1.0))+1.0/(maxb("mindeg")+1.0), ind='Min')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("maxdeg")*(maxb("maxdeg")*maxb("mindeg")*maxb("nodeInd")+maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg"))+maxb("mindeg")*maxb("nodeInd")+maxb("mindeg")+maxb("nodeInd"))/(maxb("maxdeg")*maxb("mindeg")+maxb("maxdeg")+maxb("mindeg")+1.0), ind='Max')
                except:
                    pass
            
            if minb("mindeg") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  (-(minb("mindeg")*maxb("nodeInd"))+minb("mindeg")*maxb("nodes")-(minb("mindeg"))-(maxb("nodeInd"))+maxb("nodes")+sqrt(minb("mindeg")**2.0*maxb("nodeInd")**2.0+2.0*minb("mindeg")**2.0*maxb("nodeInd")*maxb("nodes")+2.0*minb("mindeg")**2.0*maxb("nodeInd")+minb("mindeg")**2.0*maxb("nodes")**2.0-(2.0*minb("mindeg")**2.0*maxb("nodes"))+minb("mindeg")**2.0+2.0*minb("mindeg")*maxb("nodeInd")**2.0+4.0*minb("mindeg")*maxb("nodeInd")*maxb("nodes")+2.0*minb("mindeg")*maxb("nodeInd")+2.0*minb("mindeg")*maxb("nodes")**2.0-(6.0*minb("mindeg")*maxb("nodes"))+maxb("nodeInd")**2.0+2.0*maxb("nodeInd")*maxb("nodes")+maxb("nodes")**2.0-(4.0*maxb("nodes"))))/(2.0*(minb("mindeg")*maxb("nodeInd")+maxb("nodeInd")-(1.0))), ind='Max')
                except:
                    pass
            
            if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("mindeg",  (-(maxb("maxdeg")**2.0*maxb("nodeInd"))+maxb("maxdeg")**2.0-(maxb("maxdeg")*maxb("nodeInd"))+maxb("maxdeg")*minb("nodes")+minb("nodes"))/(maxb("maxdeg")**2.0*maxb("nodeInd")+maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg")*minb("nodes"))+maxb("maxdeg")-(minb("nodes"))), ind='Min')
                except:
                    pass
        return

