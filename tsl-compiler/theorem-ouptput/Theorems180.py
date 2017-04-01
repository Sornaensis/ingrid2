class Theorem161(Theorem):
    def __init__(self):
        super(Theorem161, self).__init__(161, "if genus > 2.0 and girth >= 4.0 and mindeg >= (5.0+(16.0*genus+1.0)**(1.0/2.0))/2.0 and mindeg == (3.0+(16.0*genus+9.0)**(1.0/2.0))/2.0 then \n{\n    regular,\n    hamiltonian,\n    nodes == 2.0*mindeg+2.0\n\n} else if genus > 2.0 and girth >= 4.0 and mindeg >= (5.0+(16.0*genus+1.0)**(1.0/2.0))/2.0 then \n{\n    regular,\n    hamiltonian,\n    nodes == 2.0*mindeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","mindeg","regular","hamiltonian","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") > 2.0) and (minb("girth") != 'undt'  and minb("girth") >= 4.0) and (minb("mindeg") != 'undt'  and maxb("genus") != 'undt'  and minb("mindeg") >= (5.0+(16.0*maxb("genus")+1.0)**(1.0/2.0))/2.0) and (minb("mindeg") != 'undt'  and maxb("genus") != 'undt'  and minb("mindeg") >= (3.0+(16.0*maxb("genus")+9.0)**(1.0/2.0))/2.0) and (maxb("mindeg") != 'undt'  and minb("genus") != 'undt'  and maxb("mindeg") <= (3.0+(16.0*minb("genus")+9.0)**(1.0/2.0))/2.0):
            set("regular", True )
            set("hamiltonian", True )
            try:
                set("nodes",  2.0*minb("mindeg")+2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("nodes")/2.0-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("mindeg")+2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("nodes")/2.0-(1.0), ind='Min')
            except:
                pass
        
        elif (minb("genus") != 'undt'  and minb("genus") > 2.0) and (minb("girth") != 'undt'  and minb("girth") >= 4.0) and (minb("mindeg") != 'undt'  and maxb("genus") != 'undt'  and minb("mindeg") >= (5.0+(16.0*maxb("genus")+1.0)**(1.0/2.0))/2.0):
            set("regular", True )
            set("hamiltonian", True )
            try:
                set("nodes",  2.0*minb("mindeg"), ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("nodes")/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem162(Theorem):
    def __init__(self):
        super(Theorem162, self).__init__(162, "if nodeConnec >= 2.0 and regular and ((even nodes and mindeg >= (nodes-((2.0*nodes)**(1.0/2.0)))/2.0) or (odd nodes and mindeg >= (nodes-(nodes**(1.0/2.0)))/2.0)) then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","regular","nodes","mindeg","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 2.0) and get("regular") == True  and ((evenInvar("nodes") and (minb("mindeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("mindeg") >= (maxb("nodes")-((2.0*maxb("nodes"))**(1.0/2.0)))/2.0)) or (oddInvar("nodes") and (minb("mindeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("mindeg") >= (maxb("nodes")-(maxb("nodes")**(1.0/2.0)))/2.0))):
            set("hamiltonian", True )
        
        return

class Theorem163(Theorem):
    def __init__(self):
        super(Theorem163, self).__init__(163, "if regular and nodeConnec >= 2.0 and nodes <= 3.0*mindeg then \n{\n    hamiltonian\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeConnec","nodes","mindeg","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True  and (minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 2.0) and (maxb("nodes") != 'undt'  and minb("mindeg") != 'undt'  and maxb("nodes") <= 3.0*minb("mindeg")):
            set("hamiltonian", True )
        
        return

class Theorem164(Theorem):
    def __init__(self):
        super(Theorem164, self).__init__(164, "if spectralRadius > edges**(1.0/2.0) then \n{\n    girth == 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","edges","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("spectralRadius") != 'undt'  and maxb("edges") != 'undt'  and minb("spectralRadius") > maxb("edges")**(1.0/2.0)):
            try:
                set("girth",  3.0, ind='Min')
            except:
                pass
            try:
                set("girth",  3.0, ind='Max')
            except:
                pass
        
        return

class Theorem165(Theorem):
    def __init__(self):
        super(Theorem165, self).__init__(165, "spectralRadius >= maxdeg**(1.0/2.0);", "")
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
            set("spectralRadius",  minb("maxdeg")**(1.0/2.0), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  maxb("spectralRadius")**2.0, ind='Max')
        except:
            pass
        return

class Theorem166(Theorem):
    def __init__(self):
        super(Theorem166, self).__init__(166, "if diameter > 1.0 and nodeConnec > 1.0 then \n{\n    edges >= (nodes*diameter-(2.0*diameter)+1.0)/(diameter-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("diameter") != 'undt'  and minb("diameter") > 1.0) and (minb("nodeConnec") != 'undt'  and minb("nodeConnec") > 1.0):
            try:
                set("edges",  (minb("nodes")*maxb("diameter")-(2.0*maxb("diameter"))+1.0)/(maxb("diameter")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("nodes",  (minb("diameter")*(minb("edges")+2.0)-(minb("edges"))-(1.0))/minb("diameter"), ind='Max')
            except:
                pass
            try:
                set("diameter",  (maxb("edges")+1.0)/(maxb("edges")-(minb("nodes"))+2.0), ind='Min')
            except:
                pass
        
        return

class Theorem167(Theorem):
    def __init__(self):
        super(Theorem167, self).__init__(167, "if girth >= 5.0 then \n{\n    chromaticNum <= (maxdeg+3.0)*2.0/3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","chromaticNum","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt'  and minb("girth") >= 5.0):
            try:
                set("chromaticNum",  (maxb("maxdeg")+3.0)*2.0/3.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  3.0*minb("chromaticNum")/2.0-(3.0), ind='Min')
            except:
                pass
        
        return

class Theorem168(Theorem):
    def __init__(self):
        super(Theorem168, self).__init__(168, "if girth >= 2.0*maxdeg**2.0 then \n{\n    chromaticNum <= (maxdeg+4.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","maxdeg","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("girth") >= 2.0*maxb("maxdeg")**2.0):
            try:
                set("chromaticNum",  (maxb("maxdeg")+4.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  2.0*minb("chromaticNum")-(4.0), ind='Min')
            except:
                pass
        
        return

class Theorem169(Theorem):
    def __init__(self):
        super(Theorem169, self).__init__(169, "nodeInd >= nodes**2.0/(2.0*edges+nodes);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("nodeInd",  minb("nodes")**2.0/(2.0*maxb("edges")+minb("nodes")), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("nodeInd")/2.0+sqrt(maxb("nodeInd")*(8.0*maxb("edges")+maxb("nodeInd")))/2.0, ind='Max')
        except:
            pass
        try:
            set("edges",  minb("nodes")*(-(maxb("nodeInd"))+minb("nodes"))/(2.0*maxb("nodeInd")), ind='Min')
        except:
            pass
        return

class Theorem170(Theorem):
    def __init__(self):
        super(Theorem170, self).__init__(170, "if connected and not complete then \n{\n    nodeInd >= (nodes**3.0+3.0*nodes+1.0)/(nodes*(2.0*edges+nodes))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","complete","nodeInd","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True  and get("complete") == False :
            try:
                set("nodeInd",  (minb("nodes")**3.0+3.0*minb("nodes")+1.0)/(minb("nodes")*(2.0*maxb("edges")+minb("nodes"))), ind='Min')
            except:
                pass
            try:
                set("nodes",  minb("nodeInd")/3.0-((6.0*minb("edges")*minb("nodeInd")+minb("nodeInd")**2.0-(9.0))/(3.0*(-(minb("nodeInd")**3.0)+9.0*minb("nodeInd")*(-(2.0*minb("edges")*minb("nodeInd"))+3.0)/2.0+sqrt((-(2.0*minb("nodeInd")**3.0)+9.0*minb("nodeInd")*(-(2.0*minb("edges")*minb("nodeInd"))+3.0)+27.0)**2.0-(4.0*(6.0*minb("edges")*minb("nodeInd")+minb("nodeInd")**2.0-(9.0))**3.0))/2.0+27.0/2.0)**(1.0/3.0)))-((-(minb("nodeInd")**3.0)+9.0*minb("nodeInd")*(-(2.0*minb("edges")*minb("nodeInd"))+3.0)/2.0+sqrt((-(2.0*minb("nodeInd")**3.0)+9.0*minb("nodeInd")*(-(2.0*minb("edges")*minb("nodeInd"))+3.0)+27.0)**2.0-(4.0*(6.0*minb("edges")*minb("nodeInd")+minb("nodeInd")**2.0-(9.0))**3.0))/2.0+27.0/2.0)**(1.0/3.0)/3.0), ind='Max')
            except:
                pass
            try:
                set("edges",  (-(maxb("nodeInd")*minb("nodes")**2.0)+minb("nodes")*(minb("nodes")**2.0+3.0)+1.0)/(2.0*maxb("nodeInd")*minb("nodes")), ind='Min')
            except:
                pass
        
        return

class Theorem171(Theorem):
    def __init__(self):
        super(Theorem171, self).__init__(171, "if genus > 1.0 and girth >= 4.0 then \n{\n    mindeg <= 2.0+2.0*genus**(1.0/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") > 1.0) and (minb("girth") != 'undt'  and minb("girth") >= 4.0):
            try:
                set("mindeg",  2.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("mindeg")-(2.0))**2.0/4.0, ind='Min')
            except:
                pass
        
        return

class Theorem172(Theorem):
    def __init__(self):
        super(Theorem172, self).__init__(172, "if connected then \n{\n    diameter <= 2.0*nodeCover\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","nodeCover"]
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
                set("diameter",  2.0*maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("diameter")/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem173(Theorem):
    def __init__(self):
        super(Theorem173, self).__init__(173, "nodeInd >= 2.0*nodes/(maxdeg+maxClique+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","maxdeg","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("nodeInd",  2.0*minb("nodes")/(maxb("maxdeg")+maxb("maxClique")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("nodeInd")*(maxb("maxClique")+maxb("maxdeg")+1.0)/2.0, ind='Max')
        except:
            pass
        try:
            set("maxdeg",  -(maxb("maxClique"))-(1.0)+2.0*minb("nodes")/maxb("nodeInd"), ind='Min')
        except:
            pass
        try:
            set("maxClique",  -(maxb("maxdeg"))-(1.0)+2.0*minb("nodes")/maxb("nodeInd"), ind='Min')
        except:
            pass
        return

class Theorem174(Theorem):
    def __init__(self):
        super(Theorem174, self).__init__(174, "nodeInd >= (nodes+2.0*maxdeg+1.0-(maxClique)-(mindeg))/(maxdeg+1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","maxdeg","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("nodeInd",  (minb("nodes")+2.0*maxb("maxdeg")+1.0-(maxb("maxClique"))-(maxb("mindeg")))/(maxb("maxdeg")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("maxClique")+minb("maxdeg")*maxb("nodeInd")-(2.0*minb("maxdeg"))+maxb("mindeg")+maxb("nodeInd")-(1.0), ind='Max')
        except:
            pass
        try:
            set("maxdeg",  (-(maxb("maxClique"))-(maxb("mindeg"))-(maxb("nodeInd"))+minb("nodes")+1.0)/(maxb("nodeInd")-(2.0)), ind='Min')
        except:
            pass
        try:
            set("maxClique",  -(maxb("maxdeg")*maxb("nodeInd"))+2.0*maxb("maxdeg")-(maxb("mindeg"))-(maxb("nodeInd"))+minb("nodes")+1.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  -(maxb("maxClique"))-(maxb("maxdeg")*maxb("nodeInd"))+2.0*maxb("maxdeg")-(maxb("nodeInd"))+minb("nodes")+1.0, ind='Min')
        except:
            pass
        return

class Theorem175(Theorem):
    def __init__(self):
        super(Theorem175, self).__init__(175, "bandwidth >= (1.0/2.0)*(2.0*nodes-(1.0)-(sqrt((2.0*nodes-(1.0))**2.0-(8.0*edges))));", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("bandwidth",  (1.0/2.0)*(2.0*maxb("nodes")-(1.0)-(sqrt((2.0*maxb("nodes")-(1.0))**2.0-(8.0*minb("edges"))))), ind='Min')
        except:
            pass
        try:
            set("nodes",  (minb("bandwidth")*(minb("bandwidth")+1.0)/2.0+minb("edges"))/minb("bandwidth"), ind='Min')
        except:
            pass
        try:
            set("edges",  minb("bandwidth")*(-(minb("bandwidth"))+2.0*maxb("nodes")-(1.0))/2.0, ind='Max')
        except:
            pass
        return

class Theorem176(Theorem):
    def __init__(self):
        super(Theorem176, self).__init__(176, "if maxClique == 2.0 then \n{\n    bandwidth >= (1.0/2.0)*(3.0*mindeg-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","bandwidth","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0):
            try:
                set("bandwidth",  (1.0/2.0)*(3.0*minb("mindeg")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0*maxb("bandwidth")/3.0+1.0/3.0, ind='Max')
            except:
                pass
        
        return

class Theorem177(Theorem):
    def __init__(self):
        super(Theorem177, self).__init__(177, ";", "Replaced by r280")
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

class Theorem178(Theorem):
    def __init__(self):
        super(Theorem178, self).__init__(178, "nodeCliqueCover <= nodes-(mindeg)-((nodes-(mindeg))/max(4.0, nodeInd+1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","nodes","mindeg","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("nodeCliqueCover",  minb("nodes")-(minb("mindeg"))-((minb("nodes")-(minb("mindeg")))/max(4.0, maxb("nodeInd")+1.0)), ind='Max')
        except:
            pass
        try:
            set("nodes",  (max(4.0, minb("nodeInd")+1.0)*minb("mindeg")+max(4.0, minb("nodeInd")+1.0)*maxb("nodeCliqueCover")-(minb("mindeg")))/(max(4.0, minb("nodeInd")+1.0)-(1.0)), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (-(max(4.0, minb("nodeInd")+1.0)*minb("nodeCliqueCover"))+max(4.0, minb("nodeInd")+1.0)*minb("nodes")-(minb("nodes")))/(max(4.0, minb("nodeInd")+1.0)-(1.0)), ind='Max')
        except:
            pass
        return

class Theorem179(Theorem):
    def __init__(self):
        super(Theorem179, self).__init__(179, "if domination >= 2.0 then \n{\n    edges <= (1.0/2.0)*(nodes-(nodeInd))*(nodes+nodeInd-(2.0*domination)+2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["domination","edges","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("domination") != 'undt'  and minb("domination") >= 2.0):
            try:
                set("edges",  (1.0/2.0)*(maxb("nodes")-(minb("nodeInd")))*(maxb("nodes")+minb("nodeInd")-(2.0*minb("domination"))+2.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("domination")+sqrt(minb("domination")**2.0-(2.0*minb("domination")*minb("nodeInd"))-(2.0*minb("domination"))+2.0*minb("edges")+minb("nodeInd")**2.0+2.0*minb("nodeInd")+1.0)-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  maxb("domination")+sqrt(maxb("domination")**2.0-(2.0*maxb("domination")*maxb("nodes"))-(2.0*maxb("domination"))-(2.0*minb("edges"))+maxb("nodes")**2.0+2.0*maxb("nodes")+1.0)-(1.0), ind='Max')
            except:
                pass
            try:
                set("domination",  (maxb("edges")+maxb("nodeInd")**2.0/2.0+maxb("nodeInd")-(minb("nodes")**2.0/2.0)-(minb("nodes")))/(maxb("nodeInd")-(minb("nodes"))), ind='Max')
            except:
                pass
        
        return

class Theorem180(Theorem):
    def __init__(self):
        super(Theorem180, self).__init__(180, "if regular and maxdeg >= nodes/2.0 and maxdeg <= nodes-(2.0) and ((odd nodes and even maxdeg) or (odd maxdeg and even nodes)) then \n{\n    chromaticNum <= min(maxdeg, 3.0*nodes/5.0)\n\n} else if regular and maxdeg >= nodes/2.0 and maxdeg <= nodes-(2.0) then \n{\n    chromaticNum <= min(maxdeg, (2.0*(nodes-(maxdeg))-(3.0))*nodes/(3.0*(nodes-(maxdeg))-(4.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","maxdeg","nodes","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True  and (minb("maxdeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("maxdeg") >= maxb("nodes")/2.0) and (maxb("maxdeg") != 'undt'  and minb("nodes") != 'undt'  and maxb("maxdeg") <= minb("nodes")-(2.0)) and ((oddInvar("nodes") and evenInvar("maxdeg")) or (oddInvar("maxdeg") and evenInvar("nodes"))):
            try:
                set("chromaticNum",  min(maxb("maxdeg"), 3.0*maxb("nodes")/5.0), ind='Max')
            except:
                pass
        
        elif get("regular") == True  and (minb("maxdeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("maxdeg") >= maxb("nodes")/2.0) and (maxb("maxdeg") != 'undt'  and minb("nodes") != 'undt'  and maxb("maxdeg") <= minb("nodes")-(2.0)):
            try:
                set("chromaticNum",  min(minb("maxdeg"), (2.0*(maxb("nodes")-(minb("maxdeg")))-(3.0))*maxb("nodes")/(3.0*(maxb("nodes")-(minb("maxdeg")))-(4.0))), ind='Max')
            except:
                pass
        
        return

