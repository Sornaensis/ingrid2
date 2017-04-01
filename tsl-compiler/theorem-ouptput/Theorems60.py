class Theorem41(Theorem):
    def __init__(self):
        super(Theorem41, self).__init__(41, "if chromaticNum <= 2.0 or bipartite then \n{\n    bipartite,\n    chromaticNum <= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","bipartite"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("chromaticNum") != 'undt'  and maxb("chromaticNum") <= 2.0) or get("bipartite") == True :
            set("bipartite", True )
            try:
                set("chromaticNum",  2.0, ind='Max')
            except:
                pass
        
        return

class Theorem42(Theorem):
    def __init__(self):
        super(Theorem42, self).__init__(42, "if radius == 1.0 or maxdeg == nodes-(1.0) then \n{\n    maxdeg == nodes-(1.0),\n    radius == 1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["radius","maxdeg","nodes"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("radius") != 'undt'  and minb("radius") >= 1.0) and (maxb("radius") != 'undt'  and maxb("radius") <= 1.0) or (minb("maxdeg") != 'undt'  and maxb("nodes") != 'undt'  and minb("maxdeg") >= maxb("nodes")-(1.0)) and (maxb("maxdeg") != 'undt'  and minb("nodes") != 'undt'  and maxb("maxdeg") <= minb("nodes")-(1.0)):
            try:
                set("maxdeg",  minb("nodes")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("maxdeg")+1.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodes")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("maxdeg")+1.0, ind='Min')
            except:
                pass
            try:
                set("radius",  1.0, ind='Min')
            except:
                pass
            try:
                set("radius",  1.0, ind='Max')
            except:
                pass
        
        return

class Theorem43(Theorem):
    def __init__(self):
        super(Theorem43, self).__init__(43, "if (forest and connected) or tree then \n{\n    tree,\n    forest,\n    connected\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","connected","tree"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (get("forest") == True  and get("connected") == True ) or get("tree") == True :
            set("tree", True )
            set("forest", True )
            set("connected", True )
        
        return

class Theorem44(Theorem):
    def __init__(self):
        super(Theorem44, self).__init__(44, "if nodeConnec >= 1.0 or numOfComponents == 1.0 or radius <= nodes/2.0 or diameter <= nodes-(1.0) then \n{\n    nodeConnec >= 1.0,\n    numOfComponents == 1.0,\n    radius <= nodes/2.0,\n    diameter <= nodes-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","numOfComponents","radius","nodes","diameter"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 1.0) or (minb("numOfComponents") != 'undt'  and minb("numOfComponents") >= 1.0) and (maxb("numOfComponents") != 'undt'  and maxb("numOfComponents") <= 1.0) or (maxb("radius") != 'undt'  and minb("nodes") != 'undt'  and maxb("radius") <= minb("nodes")/2.0) or (maxb("diameter") != 'undt'  and minb("nodes") != 'undt'  and maxb("diameter") <= minb("nodes")-(1.0)):
            try:
                set("nodeConnec",  1.0, ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  1.0, ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  1.0, ind='Max')
            except:
                pass
            try:
                set("radius",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("radius"), ind='Min')
            except:
                pass
            try:
                set("diameter",  maxb("nodes")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("diameter")+1.0, ind='Min')
            except:
                pass
        
        return

class Theorem45(Theorem):
    def __init__(self):
        super(Theorem45, self).__init__(45, "if cycle or (maxdeg == 2.0 and mindeg == 2.0 and connected) then \n{\n    cycle,\n    maxdeg == 2.0,\n    mindeg == 2.0,\n    connected\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["cycle","maxdeg","mindeg","connected"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("cycle") == True  or ((minb("maxdeg") != 'undt'  and minb("maxdeg") >= 2.0) and (maxb("maxdeg") != 'undt'  and maxb("maxdeg") <= 2.0) and (minb("mindeg") != 'undt'  and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt'  and maxb("mindeg") <= 2.0) and get("connected") == True ):
            set("cycle", True )
            try:
                set("maxdeg",  2.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Max')
            except:
                pass
            set("connected", True )
        
        return

class Theorem46(Theorem):
    def __init__(self):
        super(Theorem46, self).__init__(46, "if regular or mindeg == maxdeg then \n{\n    regular,\n    mindeg == maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","maxdeg"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True  or (minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg")):
            set("regular", True )
            try:
                set("mindeg",  minb("maxdeg"), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  maxb("maxdeg"), ind='Max')
            except:
                pass
            try:
                set("maxdeg",  minb("mindeg"), ind='Min')
            except:
                pass
        
        return

class Theorem47(Theorem):
    def __init__(self):
        super(Theorem47, self).__init__(47, "if genus == 0.0 or planar or thickness == 1.0 then \n{\n    genus == 0.0,\n    planar,\n    thickness == 1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","planar","thickness"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") >= 0.0) and (maxb("genus") != 'undt'  and maxb("genus") <= 0.0) or get("planar") == True  or (minb("thickness") != 'undt'  and minb("thickness") >= 1.0) and (maxb("thickness") != 'undt'  and maxb("thickness") <= 1.0):
            try:
                set("genus",  0.0, ind='Min')
            except:
                pass
            try:
                set("genus",  0.0, ind='Max')
            except:
                pass
            set("planar", True )
            try:
                set("thickness",  1.0, ind='Min')
            except:
                pass
            try:
                set("thickness",  1.0, ind='Max')
            except:
                pass
        
        return

class Theorem48(Theorem):
    def __init__(self):
        super(Theorem48, self).__init__(48, "if forest then \n{\n    planar,\n    chromaticNum == 2.0,\n    mindeg == 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","planar","chromaticNum","mindeg"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == True :
            set("planar", True )
            try:
                set("chromaticNum",  2.0, ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Min')
            except:
                pass
            try:
                set("mindeg",  2.0, ind='Max')
            except:
                pass
        
        return

class Theorem49(Theorem):
    def __init__(self):
        super(Theorem49, self).__init__(49, "if cycle then \n{\n    planar,\n    not forest,\n    crossing == 0.0,\n    nodes >= 2.0,\n    edges >= 3.0,\n    arboricity == 2.0,\n    nodeCover == (nodes+1.0)/2.0,\n    edgeCover == (nodes+1.0)/2.0,\n    nodeInd == nodes/2.0,\n    edgeInd == nodes/2.0,\n    radius == edgeInd,\n    girth == circumference,\n    circumference == nodes,\n    edgeChromatic == chromaticNum,\n    nodes >= 2.0*nodeCover-(1.0),\n    nodes <= 2.0*nodeCover,\n    nodes >= 2.0*edgeInd,\n    nodes <= 2.0*edgeInd+1.0,\n    nodeConnec == 2.0,\n    regular,\n    bandwidth == 2.0\n\n};if cycle and nodes > 3.0 then \n{\n    maxClique == 2.0\n\n} else  \n{\n    maxClique == 3.0\n\n};if cycle and even nodes then \n{\n    chromaticNum == 2.0\n\n} else  \n{\n    chromaticNum == 3.0\n\n};if cycle and chromaticNum == 2.0 then \n{\n    even nodes\n\n} else  \n{\n    odd nodes\n\n};if cycle and maxClique == 2.0 then \n{\n    nodes >= 4.0\n\n} else  \n{\n    nodes == 3.0\n\n};if cycle and nodes == 3.0 then \n{\n    nodeCliqueCover == 1.0\n\n} else  \n{\n    nodeCliqueCover == nodeCover\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["cycle","planar","forest","crossing","nodes","edges","arboricity","nodeCover","edgeCover","nodeInd","edgeInd","radius","girth","circumference","edgeChromatic","chromaticNum","nodeConnec","regular","bandwidth","maxClique","nodeCliqueCover"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("cycle") == True :
            set("planar", True )
            set("forest", False )
            try:
                set("crossing",  0.0, ind='Min')
            except:
                pass
            try:
                set("crossing",  0.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0, ind='Min')
            except:
                pass
            try:
                set("edges",  3.0, ind='Min')
            except:
                pass
            try:
                set("arboricity",  2.0, ind='Min')
            except:
                pass
            try:
                set("arboricity",  2.0, ind='Max')
            except:
                pass
            try:
                set("nodeCover",  (minb("nodes")+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeCover")-(1.0), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeCover")-(1.0), ind='Min')
            except:
                pass
            try:
                set("edgeCover",  (minb("nodes")+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeCover")-(1.0), ind='Max')
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
                set("nodeInd",  minb("nodes")/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeInd"), ind='Max')
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
            try:
                set("radius",  minb("edgeInd"), ind='Min')
            except:
                pass
            try:
                set("edgeInd",  maxb("radius"), ind='Max')
            except:
                pass
            try:
                set("radius",  maxb("edgeInd"), ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("radius"), ind='Min')
            except:
                pass
            try:
                set("girth",  minb("circumference"), ind='Min')
            except:
                pass
            try:
                set("circumference",  maxb("girth"), ind='Max')
            except:
                pass
            try:
                set("girth",  maxb("circumference"), ind='Max')
            except:
                pass
            try:
                set("circumference",  minb("girth"), ind='Min')
            except:
                pass
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
            try:
                set("edgeChromatic",  minb("chromaticNum"), ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  maxb("edgeChromatic"), ind='Max')
            except:
                pass
            try:
                set("edgeChromatic",  maxb("chromaticNum"), ind='Max')
            except:
                pass
            try:
                set("chromaticNum",  minb("edgeChromatic"), ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*minb("nodeCover")-(1.0), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("nodes")/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*minb("edgeInd"), ind='Min')
            except:
                pass
            try:
                set("edgeInd",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeInd")+1.0, ind='Max')
            except:
                pass
            try:
                set("edgeInd",  minb("nodes")/2.0-(1.0/2.0), ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Max')
            except:
                pass
            set("regular", True )
            try:
                set("bandwidth",  2.0, ind='Min')
            except:
                pass
            try:
                set("bandwidth",  2.0, ind='Max')
            except:
                pass
        
        if get("cycle") == True  and (minb("nodes") != 'undt'  and minb("nodes") > 3.0):
            try:
                set("maxClique",  2.0, ind='Min')
            except:
                pass
            try:
                set("maxClique",  2.0, ind='Max')
            except:
                pass
        
        elif True:
            try:
                set("maxClique",  3.0, ind='Min')
            except:
                pass
            try:
                set("maxClique",  3.0, ind='Max')
            except:
                pass
        
        if get("cycle") == True  and evenInvar("nodes"):
            try:
                set("chromaticNum",  2.0, ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  2.0, ind='Max')
            except:
                pass
        
        elif True:
            try:
                set("chromaticNum",  3.0, ind='Min')
            except:
                pass
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        
        if get("cycle") == True  and (minb("chromaticNum") != 'undt'  and minb("chromaticNum") >= 2.0) and (maxb("chromaticNum") != 'undt'  and maxb("chromaticNum") <= 2.0):
            if minb("nodes") != 'undt' :
                if even(minb("nodes")+1.0):
                    set("nodes", minb("nodes")+1.0, ind='Min' )
                
            
            
            if maxb("nodes") != 'undt' :
                if even(maxb("nodes")-(1.0)):
                    set("nodes", minb("nodes")-(1.0), ind='Max' )
                
            
        
        elif True:
            if minb("nodes") != 'undt' :
                if odd(minb("nodes")+1.0):
                    set("nodes", minb("nodes")+1.0, ind='Min' )
                
            
            
            if maxb("nodes") != 'undt' :
                if odd(maxb("nodes")-(1.0)):
                    set("nodes", minb("nodes")-(1.0), ind='Max' )
                
            
        
        if get("cycle") == True  and (minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0):
            try:
                set("nodes",  4.0, ind='Min')
            except:
                pass
        
        elif True:
            try:
                set("nodes",  3.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  3.0, ind='Max')
            except:
                pass
        
        if get("cycle") == True  and (minb("nodes") != 'undt'  and minb("nodes") >= 3.0) and (maxb("nodes") != 'undt'  and maxb("nodes") <= 3.0):
            try:
                set("nodeCliqueCover",  1.0, ind='Min')
            except:
                pass
            try:
                set("nodeCliqueCover",  1.0, ind='Max')
            except:
                pass
        
        elif True:
            try:
                set("nodeCliqueCover",  minb("nodeCover"), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("nodeCliqueCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCliqueCover",  maxb("nodeCover"), ind='Max')
            except:
                pass
            try:
                set("nodeCover",  minb("nodeCliqueCover"), ind='Min')
            except:
                pass
        
        return

class Theorem50(Theorem):
    def __init__(self):
        super(Theorem50, self).__init__(50, "if forest or edges == nodes-(numOfComponents) or arboricity == 1.0 or undefined girth or undefined circumference then \n{\n    forest,\n    edges == nodes-(numOfComponents),\n    arboricity == 1.0,\n    undefined girth,\n    undefined circumference\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","arboricity","girth","circumference"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == True  or (minb("edges") != 'undt'  and maxb("nodes") != 'undt'  and minb("numOfComponents") != 'undt'  and minb("edges") >= maxb("nodes")-(minb("numOfComponents"))) and (maxb("edges") != 'undt'  and minb("nodes") != 'undt'  and maxb("numOfComponents") != 'undt'  and maxb("edges") <= minb("nodes")-(maxb("numOfComponents"))) or (minb("arboricity") != 'undt'  and minb("arboricity") >= 1.0) and (maxb("arboricity") != 'undt'  and maxb("arboricity") <= 1.0) or minb("girth") == 'undt'  or minb("circumference") == 'undt' :
            set("forest", True )
            try:
                set("edges",  minb("nodes")-(maxb("numOfComponents")), ind='Min')
            except:
                pass
            try:
                set("nodes",  maxb("edges")+maxb("numOfComponents"), ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(maxb("edges"))+minb("nodes"), ind='Min')
            except:
                pass
            try:
                set("edges",  maxb("nodes")-(minb("numOfComponents")), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edges")+minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  -(minb("edges"))+maxb("nodes"), ind='Max')
            except:
                pass
            try:
                set("arboricity",  1.0, ind='Min')
            except:
                pass
            try:
                set("arboricity",  1.0, ind='Max')
            except:
                pass
            set("girth", 'undt' , ind='Min' )
            set("circumference", 'undt' , ind='Min' )
        
        return

class Theorem51(Theorem):
    def __init__(self):
        super(Theorem51, self).__init__(51, "arboricity >= chromaticNum/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","chromaticNum"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("arboricity",  minb("chromaticNum")/2.0, ind='Min')
        except:
            pass
        try:
            set("chromaticNum",  2.0*maxb("arboricity"), ind='Max')
        except:
            pass
        return

class Theorem52(Theorem):
    def __init__(self):
        super(Theorem52, self).__init__(52, "if (connected and not cycle and (not complete or even nodes)) or (maxClique <= maxdeg and maxdeg >= 4.0 and regular) then \n{\n    arboricity <= (1.0+maxdeg)/2.0\n\n};arboricity <= 1.0+spectralRadius/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["connected","cycle","complete","nodes","maxClique","maxdeg","regular","arboricity","spectralRadius"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (get("connected") == True  and get("cycle") == False  and (get("complete") == False  or evenInvar("nodes"))) or ((maxb("maxClique") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("maxClique") <= minb("maxdeg")) and (minb("maxdeg") != 'undt'  and minb("maxdeg") >= 4.0) and get("regular") == True ):
            try:
                set("arboricity",  (1.0+maxb("maxdeg"))/2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  2.0*minb("arboricity")-(1.0), ind='Min')
            except:
                pass
        
        try:
            set("arboricity",  1.0+maxb("spectralRadius")/2.0, ind='Max')
        except:
            pass
        try:
            set("spectralRadius",  2.0*minb("arboricity")-(2.0), ind='Min')
        except:
            pass
        return

class Theorem53(Theorem):
    def __init__(self):
        super(Theorem53, self).__init__(53, "arboricity <= chromaticNum-(chromaticNum/(1.0+nodes/((girth-(1.0))/2.0)*chromaticNum));", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","chromaticNum","nodes","girth"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("arboricity",  maxb("chromaticNum")-(maxb("chromaticNum")/(1.0+maxb("nodes")/((minb("girth")-(1.0))/2.0)*maxb("chromaticNum"))), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  (minb("arboricity")*minb("nodes")+sqrt(minb("arboricity")*minb("nodes")*(minb("arboricity")*minb("nodes")+2.0*minb("girth")-(2.0))))/(2.0*minb("nodes")), ind='Min')
        except:
            pass
        try:
            set("nodes",  minb("arboricity")*(-(maxb("girth"))+1.0)/(2.0*maxb("chromaticNum")*(minb("arboricity")-(maxb("chromaticNum")))), ind='Min')
        except:
            pass
        try:
            set("girth",  -(2.0*maxb("chromaticNum")*maxb("nodes"))+1.0+2.0*maxb("chromaticNum")**2.0*maxb("nodes")/minb("arboricity"), ind='Max')
        except:
            pass
        return

class Theorem54(Theorem):
    def __init__(self):
        super(Theorem54, self).__init__(54, "if planar then \n{\n    mindeg <= 5.0,\n    maxClique <= 4.0,\n    arboricity <= 3.0,\n    crossing == 0.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","maxClique","arboricity","crossing"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True :
            try:
                set("mindeg",  5.0, ind='Max')
            except:
                pass
            try:
                set("maxClique",  4.0, ind='Max')
            except:
                pass
            try:
                set("arboricity",  3.0, ind='Max')
            except:
                pass
            try:
                set("crossing",  0.0, ind='Min')
            except:
                pass
            try:
                set("crossing",  0.0, ind='Max')
            except:
                pass
        
        return

class Theorem55(Theorem):
    def __init__(self):
        super(Theorem55, self).__init__(55, "edges >= (maxdeg+(nodes-(1.0))*mindeg)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","nodes","mindeg"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  (minb("maxdeg")+(minb("nodes")-(1.0))*minb("mindeg"))/2.0, ind='Min')
        except:
            pass
        try:
            set("maxdeg",  2.0*maxb("edges")-(maxb("mindeg")*minb("nodes"))+maxb("mindeg"), ind='Max')
        except:
            pass
        try:
            set("nodes",  (2.0*maxb("edges")-(minb("maxdeg"))+maxb("mindeg"))/maxb("mindeg"), ind='Max')
        except:
            pass
        try:
            set("mindeg",  (2.0*maxb("edges")-(minb("maxdeg")))/(minb("nodes")-(1.0)), ind='Max')
        except:
            pass
        return

class Theorem56(Theorem):
    def __init__(self):
        super(Theorem56, self).__init__(56, "edges <= ((nodes-(1.0))*maxdeg+mindeg)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","maxdeg","mindeg"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("edges",  ((maxb("nodes")-(1.0))*maxb("maxdeg")+maxb("mindeg"))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  (2.0*minb("edges")+minb("maxdeg")-(maxb("mindeg")))/minb("maxdeg"), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (2.0*minb("edges")-(maxb("mindeg")))/(maxb("nodes")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("mindeg",  2.0*minb("edges")-(minb("maxdeg")*maxb("nodes"))+minb("maxdeg"), ind='Min')
        except:
            pass
        return

class Theorem57(Theorem):
    def __init__(self):
        super(Theorem57, self).__init__(57, "if regular and odd mindeg then \n{\n    even p\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","p"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True  and oddInvar("mindeg"):
            if minb("p") != 'undt' :
                if even(minb("p")+1.0):
                    set("p", minb("p")+1.0, ind='Min' )
                
            
            
            if maxb("p") != 'undt' :
                if even(maxb("p")-(1.0)):
                    set("p", minb("p")-(1.0), ind='Max' )
                
            
        
        return

class Theorem58(Theorem):
    def __init__(self):
        super(Theorem58, self).__init__(58, "maxClique >= nodes/(nodes-(spectralRadius))-(1.0/3.0);", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","spectralRadius"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("maxClique",  minb("nodes")/(minb("nodes")-(minb("spectralRadius")))-(1.0/3.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("spectralRadius")*(3.0*maxb("maxClique")+1.0)/(3.0*maxb("maxClique")-(2.0)), ind='Max')
        except:
            pass
        try:
            set("spectralRadius",  maxb("nodes")*(3.0*maxb("maxClique")-(2.0))/(3.0*maxb("maxClique")+1.0), ind='Max')
        except:
            pass
        return

class Theorem59(Theorem):
    def __init__(self):
        super(Theorem59, self).__init__(59, "crossing <= (1.0/4.0)*(nodes/2.0)*(nodes-(1.0))/2.0*(nodes-(2.0))/2.0*(nodes-(3.0))/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["crossing","nodes"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        try:
            set("crossing",  (1.0/4.0)*(maxb("nodes")/2.0)*(maxb("nodes")-(1.0))/2.0*(maxb("nodes")-(2.0))/2.0*(maxb("nodes")-(3.0))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  sqrt(4.0*sqrt(64.0*minb("crossing")+1.0)+5.0)/2.0+3.0/2.0, ind='Min')
        except:
            pass
        return

class Theorem60(Theorem):
    def __init__(self):
        super(Theorem60, self).__init__(60, "if defined girth and (nodeConnec > 0.0 or mindeg > 1.0) then \n{\n    genus >= (1.0/2.0)*edges*(1.0-(2.0/girth))-((nodes/2.0))+numOfComponents\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodeConnec","mindeg","genus","edges","nodes","numOfComponents"]
    def run(self):
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt'  and ((minb("nodeConnec") != 'undt'  and minb("nodeConnec") > 0.0) or (minb("mindeg") != 'undt'  and minb("mindeg") > 1.0)):
            try:
                set("genus",  (1.0/2.0)*minb("edges")*(1.0-(2.0/minb("girth")))-((maxb("nodes")/2.0))+minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("edges",  maxb("girth")*(2.0*maxb("genus")+maxb("nodes")-(2.0*minb("numOfComponents")))/(maxb("girth")-(2.0)), ind='Max')
            except:
                pass
            try:
                set("girth",  2.0*maxb("edges")/(maxb("edges")-(2.0*maxb("genus"))-(maxb("nodes"))+2.0*minb("numOfComponents")), ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("edges")-(2.0*minb("edges")/minb("girth"))-(2.0*maxb("genus"))+2.0*minb("numOfComponents"), ind='Min')
            except:
                pass
            try:
                set("numOfComponents",  -(maxb("edges")/2.0)+maxb("edges")/minb("girth")+maxb("genus")+maxb("nodes")/2.0, ind='Max')
            except:
                pass
        
        return

