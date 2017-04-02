class Theorem1(Theorem):
    def __init__(self):
        super(Theorem1, self).__init__(1, "edges <= (1.0/2.0)*(nodes-(1.0))*(nodes-(2.0))+nodeConnec;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  (1.0/2.0)*(maxb("nodes")-(1.0))*(maxb("nodes")-(2.0))+maxb("nodeConnec"), ind='Max')
        except:
            pass
        try:
            set("nodes",  sqrt(8.0*minb("edges")-(8.0*maxb("nodeConnec"))+1.0)/2.0+3.0/2.0, ind='Min')
        except:
            pass
        try:
            set("nodeConnec",  minb("edges")-(maxb("nodes")**2.0/2.0)+3.0*maxb("nodes")/2.0-(1.0), ind='Min')
        except:
            pass
        return

class Theorem2(Theorem):
    def __init__(self):
        super(Theorem2, self).__init__(2, "chromaticNum <= (1.0/2.0)*(nodeCover+maxClique+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodeCover","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  (1.0/2.0)*(maxb("nodeCover")+maxb("maxClique")+1.0), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  2.0*minb("chromaticNum")-(maxb("maxClique"))-(1.0), ind='Min')
        except:
            pass
        try:
            set("maxClique",  2.0*minb("chromaticNum")-(maxb("nodeCover"))-(1.0), ind='Min')
        except:
            pass
        return

class Theorem3(Theorem):
    def __init__(self):
        super(Theorem3, self).__init__(3, "spectralRadius >= 2.0*edges/nodes;", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("spectralRadius",  2.0*minb("edges")/maxb("nodes"), ind='Min')
        except:
            pass
        try:
            set("edges",  maxb("nodes")*maxb("spectralRadius")/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*minb("edges")/maxb("spectralRadius"), ind='Min')
        except:
            pass
        return

class Theorem4(Theorem):
    def __init__(self):
        super(Theorem4, self).__init__(4, "spectralRadius <= (2.0*edges*nodeCover/(nodeCover+1.0))**(1.0/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","edges","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("spectralRadius",  (2.0*maxb("edges")*minb("nodeCover")/(minb("nodeCover")+1.0))**(1.0/2.0), ind='Max')
        except:
            pass
        try:
            set("edges",  1.0e26*minb("spectralRadius")**2.0*(maxb("nodeCover")+1.0)/(2.000000000000014e26*maxb("nodeCover")), ind='Min')
        except:
            pass
        try:
            set("nodeCover",  1.0e26*maxb("spectralRadius")**2.0/(2.000000000000014e26*minb("edges")-(1.0e26*maxb("spectralRadius")**2.0)), ind='Max')
        except:
            pass
        return

class Theorem5(Theorem):
    def __init__(self):
        super(Theorem5, self).__init__(5, "maxClique >= nodes**2.0/(nodes**2.0-(2.0*edges));", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("maxClique",  maxb("nodes")**2.0/(maxb("nodes")**2.0-(2.0*minb("edges"))), ind='Min')
        except:
            pass
        try:
            set("nodes",  sqrt(2.0)*sqrt(minb("edges")*maxb("maxClique")/(maxb("maxClique")-(1.0))), ind='Min')
        except:
            pass
        try:
            set("edges",  maxb("nodes")**2.0*(minb("maxClique")-(1.0))/(2.0*minb("maxClique")), ind='Max')
        except:
            pass
        return

class Theorem6(Theorem):
    def __init__(self):
        super(Theorem6, self).__init__(6, "spectralRadius <= maxdeg;", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("spectralRadius",  maxb("maxdeg"), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  minb("spectralRadius"), ind='Min')
        except:
            pass
        return

class Theorem7(Theorem):
    def __init__(self):
        super(Theorem7, self).__init__(7, "if exists diameter and mindeg > 3.0*nodeConnec-(1.0) then \n{\n    nodes >= 1.0+mindeg+diameter*nodeConnec+(diameter/3.0)*(mindeg-(3.0*nodeConnec)+1.0)\n\n} else if exists diameter then \n{\n    nodes >= nodeConnec*(diameter-(3.0))+2.0*mindeg+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","mindeg","nodeConnec","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("diameter") != 'undt'  and (((minb("mindeg") != 'undt'  and maxb("nodeConnec") != 'undt' ) and minb("mindeg") > 3.0*maxb("nodeConnec")-(1.0)))):
            try:
                set("nodes",  1.0+minb("mindeg")+minb("diameter")*maxb("nodeConnec")+(minb("diameter")/3.0)*(minb("mindeg")-(3.0*maxb("nodeConnec"))+1.0), ind='Min')
            except:
                pass
            try:
                set("mindeg",  (-(minb("diameter"))+3.0*maxb("nodes")-(3.0))/(minb("diameter")+3.0), ind='Max')
            except:
                pass
            try:
                set("diameter",  3.0*(-(minb("mindeg"))+maxb("nodes")-(1.0))/(minb("mindeg")+1.0), ind='Max')
            except:
                pass
        
        elif maxb("diameter") != 'undt' :
            try:
                set("nodes",  minb("nodeConnec")*(minb("diameter")-(3.0))+2.0*minb("mindeg")+2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  (-(2.0*minb("mindeg"))+maxb("nodes")-(2.0))/(minb("diameter")-(3.0)), ind='Max')
            except:
                pass
            try:
                set("diameter",  (-(2.0*minb("mindeg"))+3.0*minb("nodeConnec")+maxb("nodes")-(2.0))/minb("nodeConnec"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  -(minb("diameter")*minb("nodeConnec")/2.0)+3.0*minb("nodeConnec")/2.0+maxb("nodes")/2.0-(1.0), ind='Max')
            except:
                pass
        
        return

class Theorem8(Theorem):
    def __init__(self):
        super(Theorem8, self).__init__(8, "nodes >= maxdeg+1.0+(mindeg+1.0)*(numOfComponents-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxdeg","mindeg","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("nodes",  minb("maxdeg")+1.0+(minb("mindeg")+1.0)*(minb("numOfComponents")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  -(minb("mindeg")*minb("numOfComponents"))+minb("mindeg")+maxb("nodes")-(minb("numOfComponents")), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (-(minb("maxdeg"))+maxb("nodes")-(minb("numOfComponents")))/(minb("numOfComponents")-(1.0)), ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  (-(minb("maxdeg"))+minb("mindeg")+maxb("nodes"))/(minb("mindeg")+1.0), ind='Max')
        except:
            pass
        return

class Theorem9(Theorem):
    def __init__(self):
        super(Theorem9, self).__init__(9, "edgeCliqueCover <= nodes**2.0/4.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCliqueCover",  maxb("nodes")**2.0/4.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*sqrt(minb("edgeCliqueCover")), ind='Min')
        except:
            pass
        return

class Theorem10(Theorem):
    def __init__(self):
        super(Theorem10, self).__init__(10, "diameter <= 2.0*radius;", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","radius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("diameter",  2.0*maxb("radius"), ind='Max')
        except:
            pass
        try:
            set("radius",  minb("diameter")/2.0, ind='Min')
        except:
            pass
        return

class Theorem11(Theorem):
    def __init__(self):
        super(Theorem11, self).__init__(11, "edgeInd <= nodes/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeInd",  maxb("nodes")/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*minb("edgeInd"), ind='Min')
        except:
            pass
        return

class Theorem12(Theorem):
    def __init__(self):
        super(Theorem12, self).__init__(12, "edgeInd >= nodes/(maxdeg+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeInd",  minb("nodes")/(maxb("maxdeg")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("edgeInd")*(maxb("maxdeg")+1.0), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  (-(maxb("edgeInd"))+minb("nodes"))/maxb("edgeInd"), ind='Min')
        except:
            pass
        return

class Theorem13(Theorem):
    def __init__(self):
        super(Theorem13, self).__init__(13, "if girth == 2.0*diameter+1.0 then \n{\n    regular\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","diameter","regular"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((((minb("girth") != 'undt'  and maxb("diameter") != 'undt' ) and minb("girth") >= 2.0*maxb("diameter")+1.0)) and (((maxb("girth") != 'undt'  and minb("diameter") != 'undt' ) and maxb("girth") <= 2.0*minb("diameter")+1.0))):
            set("regular", True )
        
        return

class Theorem14(Theorem):
    def __init__(self):
        super(Theorem14, self).__init__(14, "chromaticNum >= nodes/(nodes-(spectralRadius));", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodes","spectralRadius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  maxb("nodes")/(maxb("nodes")-(minb("spectralRadius"))), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("chromaticNum")*minb("spectralRadius")/(maxb("chromaticNum")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("spectralRadius",  minb("nodes")-(minb("nodes")/maxb("chromaticNum")), ind='Max')
        except:
            pass
        return

class Theorem15(Theorem):
    def __init__(self):
        super(Theorem15, self).__init__(15, "if mindeg >= 3.0 then \n{\n    edges >= 2.0**(girth/2.0)+nodes-(numOfComponents)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edges","girth","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt'  and minb("mindeg") >= 3.0)):
            try:
                set("edges",  2.0**(minb("girth")/2.0)+minb("nodes")-(maxb("numOfComponents")), ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*log(maxb("edges")-(minb("nodes"))+maxb("numOfComponents"))/log(2.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  -(2.0**(minb("girth")/2.0))+maxb("edges")+maxb("numOfComponents"), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  2.0**(minb("girth")/2.0)-(maxb("edges"))+minb("nodes"), ind='Min')
            except:
                pass
        
        return

class Theorem16(Theorem):
    def __init__(self):
        super(Theorem16, self).__init__(16, "if nodeConnec == 0.0 then \n{\n    edgeConnec == 0.0\n\n};if edgeConnec == 0.0 then \n{\n    nodeConnec == 0.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (((minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 0.0)) and ((maxb("nodeConnec") != 'undt'  and maxb("nodeConnec") <= 0.0))):
            try:
                set("edgeConnec",  0.0, ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  0.0, ind='Max')
            except:
                pass
        
        if (((minb("edgeConnec") != 'undt'  and minb("edgeConnec") >= 0.0)) and ((maxb("edgeConnec") != 'undt'  and maxb("edgeConnec") <= 0.0))):
            try:
                set("nodeConnec",  0.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  0.0, ind='Max')
            except:
                pass
        
        return

class Theorem17(Theorem):
    def __init__(self):
        super(Theorem17, self).__init__(17, "edges <= (1.0/2.0)*(edgeCliqueCover*maxClique*(maxClique-(1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","edgeCliqueCover","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  (1.0/2.0)*(maxb("edgeCliqueCover")*maxb("maxClique")*(maxb("maxClique")-(1.0))), ind='Max')
        except:
            pass
        try:
            set("edgeCliqueCover",  2.0*minb("edges")/(maxb("maxClique")*(maxb("maxClique")-(1.0))), ind='Min')
        except:
            pass
        try:
            set("maxClique",  (maxb("edgeCliqueCover")+sqrt(maxb("edgeCliqueCover")*(maxb("edgeCliqueCover")+8.0*minb("edges"))))/(2.0*maxb("edgeCliqueCover")), ind='Min')
        except:
            pass
        return

class Theorem18(Theorem):
    def __init__(self):
        super(Theorem18, self).__init__(18, "chromaticNum <= (1.0/2.0)*(7.0+(1.0+48.0*genus)**(1.0/2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  (1.0/2.0)*(7.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)), ind='Max')
        except:
            pass
        try:
            set("genus",  (2.0*minb("chromaticNum")-(7.0))**2.0/48.0-(1.0/48.0), ind='Min')
        except:
            pass
        return

class Theorem19(Theorem):
    def __init__(self):
        super(Theorem19, self).__init__(19, "if maxClique == 2.0 then \n{\n    maxdeg <= nodeInd,\n    edges <= nodeCover*nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","nodeInd","edges","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (((minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0)) and ((maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0))):
            try:
                set("maxdeg",  maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("nodeInd",  minb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("edges",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("edges")/maxb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  minb("edges")/maxb("nodeCover"), ind='Min')
            except:
                pass
        
        return

class Theorem20(Theorem):
    def __init__(self):
        super(Theorem20, self).__init__(20, "if chromaticNum == 2.0 then \n{\n    edgeInd == nodeCover,\n    nodeInd == nodeCliqueCover,\n    edgeChromatic == maxdeg,\n    even girth,\n    even circumference\n\n};if chromaticNum == 2.0 and nodes > 2.0 then \n{\n    not complete\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edgeInd","nodeCover","nodeInd","nodeCliqueCover","edgeChromatic","maxdeg","girth","circumference","nodes","complete"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (((minb("chromaticNum") != 'undt'  and minb("chromaticNum") >= 2.0)) and ((maxb("chromaticNum") != 'undt'  and maxb("chromaticNum") <= 2.0))):
            try:
                set("edgeInd",  minb("nodeCover"), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("edgeInd"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("edgeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  minb("nodeCliqueCover"), ind='Min')
            except:
                pass
            try:
                set("nodeCliqueCover",  maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("nodeInd",  maxb("nodeCliqueCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCliqueCover",  minb("nodeInd"), ind='Min')
            except:
                pass
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
            if minb("girth") != 'undt' :
                if even(minb("girth")+1.0):
                    set("girth", minb("girth")+1.0, ind='Min' )
                
            
            
            if maxb("girth") != 'undt' :
                if even(maxb("girth")-(1.0)):
                    set("girth", minb("girth")-(1.0), ind='Max' )
                
            
            
            if minb("circumference") != 'undt' :
                if even(minb("circumference")+1.0):
                    set("circumference", minb("circumference")+1.0, ind='Min' )
                
            
            
            if maxb("circumference") != 'undt' :
                if even(maxb("circumference")-(1.0)):
                    set("circumference", minb("circumference")-(1.0), ind='Max' )
                
            
        
        if ((((minb("chromaticNum") != 'undt'  and minb("chromaticNum") >= 2.0)) and ((maxb("chromaticNum") != 'undt'  and maxb("chromaticNum") <= 2.0))) and ((minb("nodes") != 'undt'  and minb("nodes") > 2.0))):
            set("complete", False )
        
        return

