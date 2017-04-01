class Theorem61(Theorem):
    def __init__(self):
        super(Theorem61, self).__init__(61, "if genus <= 1.0 then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","edgeCliqueCover","nodeCover","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("genus") != 'undt'  and maxb("genus") <= 1.0):
            try:
                set("edgeCliqueCover",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("edgeCliqueCover")/maxb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  minb("edgeCliqueCover")/maxb("nodeCover"), ind='Min')
            except:
                pass
        
        return

class Theorem62(Theorem):
    def __init__(self):
        super(Theorem62, self).__init__(62, "if mindeg >= nodes/2.0 then \n{\n    nodeConnec >= nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","nodeConnec","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("mindeg") >= maxb("nodes")/2.0):
            try:
                set("nodeConnec",  minb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  maxb("nodeConnec"), ind='Max')
            except:
                pass
        
        return

class Theorem63(Theorem):
    def __init__(self):
        super(Theorem63, self).__init__(63, "if connected then \n{\n    e <= n**2.0+(d**2.0-(d)-(4.0))+3.0*n-(2.0*d*n)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","e","n","d"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True :
            try:
                set("e",  maxb("n")**2.0+(maxb("d")**2.0-(maxb("d"))-(4.0))+3.0*maxb("n")-(2.0*maxb("d")*maxb("n")), ind='Max')
            except:
                pass
            try:
                set("n",  minb("d")+sqrt(-(8.0*minb("d"))+4.0*minb("e")+25.0)/2.0-(3.0/2.0), ind='Min')
            except:
                pass
            try:
                set("d",  minb("n")+sqrt(4.0*minb("e")-(8.0*minb("n"))+17.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem64(Theorem):
    def __init__(self):
        super(Theorem64, self).__init__(64, "if nodes >= 3.0 and nodeConnec >= nodeInd then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeConnec","nodeInd","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and minb("nodes") >= 3.0) and (minb("nodeConnec") != 'undt'  and maxb("nodeInd") != 'undt'  and minb("nodeConnec") >= maxb("nodeInd")):
            set("hamiltonian", True )
        
        return

class Theorem65(Theorem):
    def __init__(self):
        super(Theorem65, self).__init__(65, "if edges >= (nodes**2.0-(3.0*nodes)+6.0) then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt'  and maxb("nodes") != 'undt'  and minb("edges") >= (maxb("nodes")**2.0-(3.0*maxb("nodes"))+6.0)):
            set("hamiltonian", True )
        
        return

class Theorem66(Theorem):
    def __init__(self):
        super(Theorem66, self).__init__(66, "if planar and nodeConnec >= 4.0 then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","nodeConnec","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True  and (minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 4.0):
            set("hamiltonian", True )
        
        return

class Theorem67(Theorem):
    def __init__(self):
        super(Theorem67, self).__init__(67, ";", "")
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

class Theorem68(Theorem):
    def __init__(self):
        super(Theorem68, self).__init__(68, "if complete then \n{\n    regular\n\n};if complete and even nodes then \n{\n    edgeChromatic == nodes-(1.0)\n\n} else  \n{\n    edgeChromatic == nodes\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["complete","regular","nodes","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("complete") == True :
            set("regular", True )
        
        if get("complete") == True  and evenInvar("nodes"):
            try:
                set("edgeChromatic",  minb("nodes")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edgeChromatic")+1.0, ind='Max')
            except:
                pass
            try:
                set("edgeChromatic",  maxb("nodes")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edgeChromatic")+1.0, ind='Min')
            except:
                pass
        
        elif True:
            try:
                set("edgeChromatic",  minb("nodes"), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edgeChromatic"), ind='Max')
            except:
                pass
            try:
                set("edgeChromatic",  maxb("nodes"), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edgeChromatic"), ind='Min')
            except:
                pass
        
        return

class Theorem69(Theorem):
    def __init__(self):
        super(Theorem69, self).__init__(69, "chromaticNum >= 2.0*edges/(2.0*edges-(spectralRadius**2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edges","spectralRadius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("chromaticNum",  2.0*minb("edges")/(2.0*minb("edges")-(minb("spectralRadius")**2.0)), ind='Min')
        except:
            pass
        try:
            set("edges",  maxb("chromaticNum")*maxb("spectralRadius")**2.0/(2.0*(maxb("chromaticNum")-(1.0))), ind='Max')
        except:
            pass
        try:
            set("spectralRadius",  sqrt(2.0)*sqrt(maxb("edges")-(maxb("edges")/maxb("chromaticNum"))), ind='Max')
        except:
            pass
        return

class Theorem70(Theorem):
    def __init__(self):
        super(Theorem70, self).__init__(70, "if genus <= 1.0 and girth == 3.0 then \n{\n    chromaticNum <= 7.0\n\n} else if genus <= 1.0 and girth >= 4.0 then \n{\n    chromaticNum <= 4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and (minb("girth") != 'undt'  and minb("girth") >= 3.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 3.0):
            try:
                set("chromaticNum",  7.0, ind='Max')
            except:
                pass
        
        elif (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and (minb("girth") != 'undt'  and minb("girth") >= 4.0):
            try:
                set("chromaticNum",  4.0, ind='Max')
            except:
                pass
        
        return

class Theorem71(Theorem):
    def __init__(self):
        super(Theorem71, self).__init__(71, "if defined girth then \n{\n    circumference <= nodes-((numOfComponents-(1.0))*(mindeg+1.0)),\n    circumference <= edges-((numOfComponents-(1.0))*mindeg),\n    maxdeg >= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","circumference","nodes","numOfComponents","mindeg","edges","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt' :
            try:
                set("circumference",  maxb("nodes")-((minb("numOfComponents")-(1.0))*(minb("mindeg")+1.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("circumference")+minb("mindeg")*minb("numOfComponents")-(minb("mindeg"))+minb("numOfComponents")-(1.0), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  (-(minb("circumference"))+maxb("mindeg")+maxb("nodes")+1.0)/(maxb("mindeg")+1.0), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (-(minb("circumference"))+maxb("nodes")-(minb("numOfComponents"))+1.0)/(minb("numOfComponents")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("circumference",  maxb("edges")-((minb("numOfComponents")-(1.0))*minb("mindeg")), ind='Max')
            except:
                pass
            try:
                set("edges",  minb("circumference")+minb("mindeg")*minb("numOfComponents")-(minb("mindeg")), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  (-(minb("circumference"))+maxb("edges")+maxb("mindeg"))/maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (-(minb("circumference"))+maxb("edges"))/(minb("numOfComponents")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  2.0, ind='Min')
            except:
                pass
        
        return

class Theorem72(Theorem):
    def __init__(self):
        super(Theorem72, self).__init__(72, "if hamiltonian or circumference == nodes then \n{\n    hamiltonian,\n    circumference == nodes\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","circumference","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("hamiltonian") == True  or (minb("circumference") != 'undt'  and maxb("nodes") != 'undt'  and minb("circumference") >= maxb("nodes")) and (maxb("circumference") != 'undt'  and minb("nodes") != 'undt'  and maxb("circumference") <= minb("nodes")):
            set("hamiltonian", True )
            try:
                set("circumference",  minb("nodes"), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("circumference"), ind='Max')
            except:
                pass
            try:
                set("circumference",  maxb("nodes"), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("circumference"), ind='Min')
            except:
                pass
        
        return

class Theorem73(Theorem):
    def __init__(self):
        super(Theorem73, self).__init__(73, "if hamiltonian then \n{\n    arboricity >= 2.0,\n    nodeConnec >= 2.0,\n    nodeInd <= nodes/2.0,\n    edgeCover <= (nodes+1.0)/2.0,\n    nodeCliqueCover <= (nodes+1.0)/2.0,\n    nodeCover >= nodes/2.0,\n    edgeInd >= (nodes-(1.0))/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","arboricity","nodeConnec","nodeInd","nodes","edgeCover","nodeCliqueCover","nodeCover","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("hamiltonian") == True :
            try:
                set("arboricity",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeInd",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeInd"), ind='Min')
            except:
                pass
            try:
                set("edgeCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("edgeCover")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodeCliqueCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeCliqueCover")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  minb("nodes")/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  (minb("nodes")-(1.0))/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeInd")+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem74(Theorem):
    def __init__(self):
        super(Theorem74, self).__init__(74, "bandwidth <= nodes-(nodeInd/2.0)-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("bandwidth",  maxb("nodes")-(minb("nodeInd")/2.0)-(1.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  minb("bandwidth")+minb("nodeInd")/2.0+1.0, ind='Min')
        except:
            pass
        try:
            set("nodeInd",  -(2.0*minb("bandwidth"))+2.0*maxb("nodes")-(2.0), ind='Max')
        except:
            pass
        return

class Theorem75(Theorem):
    def __init__(self):
        super(Theorem75, self).__init__(75, "edges >= (nodes/nodeInd)*(nodes-(nodeInd*(nodes/nodeInd+1.0)/2.0));", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  (minb("nodes")/maxb("nodeInd"))*(minb("nodes")-(maxb("nodeInd")*(minb("nodes")/maxb("nodeInd")+1.0)/2.0)), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("nodeInd")/2.0+sqrt(maxb("nodeInd")*(8.0*maxb("edges")+maxb("nodeInd")))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodeInd",  minb("nodes")**2.0/(2.0*maxb("edges")+minb("nodes")), ind='Min')
        except:
            pass
        return

class Theorem76(Theorem):
    def __init__(self):
        super(Theorem76, self).__init__(76, "edgeCliqueCover <= nodeCliqueCover+nodes*(nodeCliqueCover-(1.0))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodeCliqueCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edgeCliqueCover",  maxb("nodeCliqueCover")+maxb("nodes")*(maxb("nodeCliqueCover")-(1.0))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodeCliqueCover",  (2.0*minb("edgeCliqueCover")+minb("nodes"))/(minb("nodes")+2.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  2.0*(minb("edgeCliqueCover")-(maxb("nodeCliqueCover")))/(maxb("nodeCliqueCover")-(1.0)), ind='Min')
        except:
            pass
        return

class Theorem77(Theorem):
    def __init__(self):
        super(Theorem77, self).__init__(77, "if nodes >= 6.0*mindeg and edges > (1.0/2.0)*(nodes-(mindeg))*(nodes-(mindeg)-(1.0))+mindeg**2.0 then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","edges","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") >= 6.0*maxb("mindeg")) and (minb("edges") != 'undt'  and maxb("nodes") != 'undt'  and minb("mindeg") != 'undt'  and minb("edges") > (1.0/2.0)*(maxb("nodes")-(minb("mindeg")))*(maxb("nodes")-(minb("mindeg"))-(1.0))+minb("mindeg")**2.0):
            set("hamiltonian", True )
        
        return

class Theorem78(Theorem):
    def __init__(self):
        super(Theorem78, self).__init__(78, "if nodes >= 4.0 and edges >= 2.0*nodes-(3.0) then \n{\n    girth <= (circumference+2.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","girth","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt'  and minb("nodes") >= 4.0) and (minb("edges") != 'undt'  and maxb("nodes") != 'undt'  and minb("edges") >= 2.0*maxb("nodes")-(3.0)):
            try:
                set("girth",  (maxb("circumference")+2.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("circumference",  2.0*minb("girth")-(2.0), ind='Min')
            except:
                pass
        
        return

class Theorem79(Theorem):
    def __init__(self):
        super(Theorem79, self).__init__(79, "if not forest then \n{\n    nodeInd >= girth/2.0,\n    radius >= girth/2.0,\n    edgeInd >= circumference/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodeInd","girth","radius","edgeInd","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False :
            try:
                set("nodeInd",  minb("girth")/2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*maxb("nodeInd"), ind='Max')
            except:
                pass
            try:
                set("radius",  minb("girth")/2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  2.0*maxb("radius"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("circumference")/2.0, ind='Min')
            except:
                pass
            try:
                set("circumference",  2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        
        return

class Theorem80(Theorem):
    def __init__(self):
        super(Theorem80, self).__init__(80, "if (defined girth and girth >= 4.0) or (undefined girth and nodes > 2.0) then \n{\n    not complete\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","complete"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt'  and (minb("girth") != 'undt'  and minb("girth") >= 4.0)) or (minb("girth") == 'undt'  and (minb("nodes") != 'undt'  and minb("nodes") > 2.0)):
            set("complete", False )
        
        return

