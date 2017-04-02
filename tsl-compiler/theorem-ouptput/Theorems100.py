class Theorem81(Theorem):
    def __init__(self):
        super(Theorem81, self).__init__(81, "if regular then \n{\n    nodeInd <= nodes/2.0+(maxClique**2.0+3.0*maxClique-(2.0))/(2.0*mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeInd","nodes","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True :
            try:
                set("nodeInd",  maxb("nodes")/2.0+(maxb("maxClique")**2.0+3.0*maxb("maxClique")-(2.0))/(2.0*minb("mindeg")), ind='Max')
            except:
                pass
            try:
                set("nodes",  (-(maxb("maxClique")**2.0)-(3.0*maxb("maxClique"))+2.0*maxb("mindeg")*minb("nodeInd")+2.0)/maxb("mindeg"), ind='Min')
            except:
                pass
            try:
                set("maxClique",  sqrt(8.0*maxb("mindeg")*minb("nodeInd")-(4.0*maxb("mindeg")*maxb("nodes"))+17.0)/2.0-(3.0/2.0), ind='Min')
            except:
                pass
            try:
                set("mindeg",  (maxb("maxClique")**2.0+3.0*maxb("maxClique")-(2.0))/(2.0*minb("nodeInd")-(maxb("nodes"))), ind='Max')
            except:
                pass
        
        return

class Theorem82(Theorem):
    def __init__(self):
        super(Theorem82, self).__init__(82, "if mindeg >= nodes/2.0 then \n{\n    edgeConnec == mindeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","edgeConnec"]
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
                set("edgeConnec",  minb("mindeg"), ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("edgeConnec"), ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("edgeConnec"), ind='Min')
            except:
                pass
        
        return

class Theorem83(Theorem):
    def __init__(self):
        super(Theorem83, self).__init__(83, "if genus > 0.0 then \n{\n    arboricity <= 9.0+(1.0+48.0*genus)**(1.0/2.0)/4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","arboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") > 0.0):
            try:
                set("arboricity",  9.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)/4.0, ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("arboricity")-(9.0))**2.0/3.0-(1.0/48.0), ind='Min')
            except:
                pass
        
        return

class Theorem84(Theorem):
    def __init__(self):
        super(Theorem84, self).__init__(84, "if maxClique == 2.0 then \n{\n    arboricity <= 2.0+genus**(1.0/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","arboricity","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0)):
            try:
                set("arboricity",  2.0+maxb("genus")**(1.0/2.0), ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("arboricity")-(2.0))**2.0, ind='Min')
            except:
                pass
        
        return

class Theorem85(Theorem):
    def __init__(self):
        super(Theorem85, self).__init__(85, "if maxClique == 2.0 then \n{\n    chromaticNum <= 3.0+2.0*genus**(1.0/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0)):
            try:
                set("chromaticNum",  3.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("chromaticNum")-(3.0))**2.0/4.0, ind='Min')
            except:
                pass
        
        return

class Theorem86(Theorem):
    def __init__(self):
        super(Theorem86, self).__init__(86, "let u = floor((nodes-(mindeg)-(3.0))/(mindeg+1.0)**2.0);let k = floor((floor((nodes-(u*(mindeg+1.0)**2.0))/(mindeg+2.0)-(1.0)))/2.0);if mindeg <= maxdeg-(2.0) and nodes < maxdeg+mindeg then \n{\n    edgeInd >= min(floor(nodes/2.0), mindeg)\n\n} else if mindeg <= maxdeg-(2.0) and nodes >= maxdeg+mindeg then \n{\n    edgeInd >= ceil(nodes*mindeg/(mindeg+maxdeg))\n\n} else if (mindeg == maxdeg and even mindeg) or (mindeg == maxdeg-(1.0) and odd mindeg) then \n{\n    edgeInd >= ceil(nodes*maxdeg/(2.0*(maxdeg+1.0)))\n\n} else if mindeg == maxdeg-(1.0) then \n{\n    edgeInd >= ceil((nodes*mindeg+1.0)/(2.0*(mindeg+1.0)))\n\n} else if (mindeg == maxdeg and odd mindeg) and nodes == mindeg+1.0 then \n{\n    edgeInd >= nodes/2.0\n\n} else if (mindeg == maxdeg and odd mindeg) and nodes > mindeg+1.0 then \n{\n    edgeInd >= (nodes-(u*(mindeg-(1.0))))/2.0-(k)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodes","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg")-(2.0)) and (maxb("nodes") != 'undt'  and minb("maxdeg") != 'undt'  and minb("mindeg") != 'undt'  and maxb("nodes") < minb("maxdeg")+minb("mindeg")):
            try:
                set("edgeInd",  min(floor(minb("nodes")/2.0), minb("mindeg")), ind='Min')
            except:
                pass
        
        elif (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg")-(2.0)) and (minb("nodes") != 'undt'  and maxb("maxdeg") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") >= maxb("maxdeg")+maxb("mindeg")):
            try:
                set("edgeInd",  ceil(minb("nodes")*maxb("mindeg")/(maxb("mindeg")+maxb("maxdeg"))), ind='Min')
            except:
                pass
        
        elif (((minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg"))) and evenInvar("mindeg")) or (((minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")-(1.0)) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg")-(1.0))) and oddInvar("mindeg")):
            try:
                set("edgeInd",  ceil(minb("nodes")*maxb("maxdeg")/(2.0*(maxb("maxdeg")+1.0))), ind='Min')
            except:
                pass
        
        elif ((minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")-(1.0)) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg")-(1.0))):
            try:
                set("edgeInd",  ceil((minb("nodes")*maxb("mindeg")+1.0)/(2.0*(maxb("mindeg")+1.0))), ind='Min')
            except:
                pass
        
        elif (((minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg"))) and oddInvar("mindeg")) and ((minb("nodes") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") >= maxb("mindeg")+1.0) and (maxb("nodes") != 'undt'  and minb("mindeg") != 'undt'  and maxb("nodes") <= minb("mindeg")+1.0)):
            try:
                set("edgeInd",  minb("nodes")/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        
        elif (((minb("mindeg") != 'undt'  and maxb("maxdeg") != 'undt'  and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt'  and minb("maxdeg") != 'undt'  and maxb("mindeg") <= minb("maxdeg"))) and oddInvar("mindeg")) and (minb("nodes") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") > maxb("mindeg")+1.0):
            try:
                set("edgeInd",  (maxb("nodes")-(floor((maxb("nodes")-(maxb("mindeg"))-(3.0))/(maxb("mindeg")+1.0)**2.0)*(maxb("mindeg")-(1.0))))/2.0-(floor((floor((maxb("nodes")-(floor((maxb("nodes")-(maxb("mindeg"))-(3.0))/(maxb("mindeg")+1.0)**2.0)*(maxb("mindeg")+1.0)**2.0))/(maxb("mindeg")+2.0)-(1.0)))/2.0)), ind='Min')
            except:
                pass
            try:
                set("nodes",  floor((minb("nodes")-(minb("mindeg"))-(3.0))/(minb("mindeg")+1.0)**2.0)*minb("mindeg")-(floor((minb("nodes")-(minb("mindeg"))-(3.0))/(minb("mindeg")+1.0)**2.0))+2.0*floor((floor((minb("nodes")-(floor((minb("nodes")-(minb("mindeg"))-(3.0))/(minb("mindeg")+1.0)**2.0)*(minb("mindeg")+1.0)**2.0))/(minb("mindeg")+2.0)-(1.0)))/2.0)+2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (floor((maxb("nodes")-(maxb("mindeg"))-(3.0))/(maxb("mindeg")+1.0)**2.0)-(2.0*floor((floor((maxb("nodes")-(floor((maxb("nodes")-(maxb("mindeg"))-(3.0))/(maxb("mindeg")+1.0)**2.0)*(maxb("mindeg")+1.0)**2.0))/(maxb("mindeg")+2.0)-(1.0)))/2.0))-(2.0*maxb("edgeInd"))+maxb("nodes"))/floor((maxb("nodes")-(maxb("mindeg"))-(3.0))/(maxb("mindeg")+1.0)**2.0), ind='Min')
            except:
                pass
        
        return

class Theorem87(Theorem):
    def __init__(self):
        super(Theorem87, self).__init__(87, "if genus > 0.0 then \n{\n    mindeg <= 5.0+(1.0+48.0*genus)**(1.0/2.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") > 0.0):
            try:
                set("mindeg",  5.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)/2.0, ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("mindeg")-(5.0))**2.0/12.0-(1.0/48.0), ind='Min')
            except:
                pass
        
        return

class Theorem88(Theorem):
    def __init__(self):
        super(Theorem88, self).__init__(88, "if genus > 0.0 and maxClique <= 2.0 then \n{\n    edgeConnec <= 2.0+2.0*genus**(1.0/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","maxClique","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt'  and minb("genus") > 0.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0):
            try:
                set("edgeConnec",  2.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
            except:
                pass
            try:
                set("genus",  (minb("edgeConnec")-(2.0))**2.0/4.0, ind='Min')
            except:
                pass
        
        return

class Theorem89(Theorem):
    def __init__(self):
        super(Theorem89, self).__init__(89, "if genus == 0.0 and girth == 3.0 then \n{\n    edgeConnec <= 5.0\n\n} else if genus == 0.0 and (girth == 4.0 or girth == 5.0) then \n{\n    edgeConnec <= 3.0\n\n} else if genus == 0.0 and girth >= 6.0 then \n{\n    edgeConnec <= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("genus") != 'undt'  and minb("genus") >= 0.0) and (maxb("genus") != 'undt'  and maxb("genus") <= 0.0)) and ((minb("girth") != 'undt'  and minb("girth") >= 3.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 3.0)):
            try:
                set("edgeConnec",  5.0, ind='Max')
            except:
                pass
        
        elif ((minb("genus") != 'undt'  and minb("genus") >= 0.0) and (maxb("genus") != 'undt'  and maxb("genus") <= 0.0)) and (((minb("girth") != 'undt'  and minb("girth") >= 4.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 4.0)) or ((minb("girth") != 'undt'  and minb("girth") >= 5.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 5.0))):
            try:
                set("edgeConnec",  3.0, ind='Max')
            except:
                pass
        
        elif ((minb("genus") != 'undt'  and minb("genus") >= 0.0) and (maxb("genus") != 'undt'  and maxb("genus") <= 0.0)) and (minb("girth") != 'undt'  and minb("girth") >= 6.0):
            try:
                set("edgeConnec",  2.0, ind='Max')
            except:
                pass
        
        return

class Theorem90(Theorem):
    def __init__(self):
        super(Theorem90, self).__init__(90, "if genus <= 1.0 and girth == 3.0 then \n{\n    edgeConnec <= 6.0\n\n} else if genus <= 1.0 and girth == 4.0 then \n{\n    edgeConnec <= 4.0\n\n} else if genus <= 1.0 and (girth == 5.0 or girth == 6.0) then \n{\n    edgeConnec <= 3.0\n\n} else if genus <= 1.0 and girth >= 7.0 then \n{\n    edgeConnec <= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and ((minb("girth") != 'undt'  and minb("girth") >= 3.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 3.0)):
            try:
                set("edgeConnec",  6.0, ind='Max')
            except:
                pass
        
        elif (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and ((minb("girth") != 'undt'  and minb("girth") >= 4.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 4.0)):
            try:
                set("edgeConnec",  4.0, ind='Max')
            except:
                pass
        
        elif (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and (((minb("girth") != 'undt'  and minb("girth") >= 5.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 5.0)) or ((minb("girth") != 'undt'  and minb("girth") >= 6.0) and (maxb("girth") != 'undt'  and maxb("girth") <= 6.0))):
            try:
                set("edgeConnec",  3.0, ind='Max')
            except:
                pass
        
        elif (maxb("genus") != 'undt'  and maxb("genus") <= 1.0) and (minb("girth") != 'undt'  and minb("girth") >= 7.0):
            try:
                set("edgeConnec",  2.0, ind='Max')
            except:
                pass
        
        return

class Theorem91(Theorem):
    def __init__(self):
        super(Theorem91, self).__init__(91, "let s = floor((girth-(1.0))/4.0);if mindeg >= 3.0 and s >= 1.0 then \n{\n    nodes >= girth*(mindeg-(1.0))**s\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt'  and minb("mindeg") >= 3.0) and (minb(floor(("girth"-(1.0))/4.0)) != 'undt'  and minb(floor(("girth"-(1.0))/4.0)) >= 1.0):
            try:
                set("nodes",  minb("girth")*(minb("mindeg")-(1.0))**floor((minb("girth")-(1.0))/4.0), ind='Min')
            except:
                pass
            try:
                set("girth",  maxb("nodes")*(maxb("mindeg")-(1.0))**(-(floor((minb("girth")-(1.0))/4.0))), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (maxb("nodes")/maxb("girth"))**(1.0/floor((maxb("girth")-(1.0))/4.0))+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem92(Theorem):
    def __init__(self):
        super(Theorem92, self).__init__(92, "if nodeConnec >= 2.0 then \n{\n    circumference >= min(nodes, 2.0*mindeg)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt'  and minb("nodeConnec") >= 2.0):
            try:
                set("circumference",  min(minb("nodes"), 2.0*minb("mindeg")), ind='Min')
            except:
                pass
        
        return

class Theorem93(Theorem):
    def __init__(self):
        super(Theorem93, self).__init__(93, "if diameter == 2.0 and ((even nodes and even mindeg and nodes >= mindeg**3.0+mindeg+1.0) or ((odd nodes or odd mindeg) and nodes > mindeg**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(mindeg+1.0)+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodes","mindeg","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt'  and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt'  and maxb("diameter") <= 2.0)) and ((evenInvar("nodes") and evenInvar("mindeg") and (minb("nodes") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") >= maxb("mindeg")**3.0+maxb("mindeg")+1.0)) or ((oddInvar("nodes") or oddInvar("mindeg")) and (minb("nodes") != 'undt'  and maxb("mindeg") != 'undt'  and minb("nodes") > maxb("mindeg")**3.0+1.0))):
            try:
                set("edges",  ((minb("nodes")-(1.0))*(minb("mindeg")+1.0)+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (2.0*maxb("edges")+minb("mindeg"))/(minb("mindeg")+1.0), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem94(Theorem):
    def __init__(self):
        super(Theorem94, self).__init__(94, "if diameter == 2.0 and (nodeConnec > 2.0 or nodeConnec < 2.0) and ((even nodes and even nodeConnec and nodes >= nodeConnec**3.0+nodeConnec+1.0) or ((odd nodes or odd nodeConnec) and nodes > nodeConnec**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(nodeConnec+1.0)+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt'  and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt'  and maxb("diameter") <= 2.0)) and ((minb("nodeConnec") != 'undt'  and minb("nodeConnec") > 2.0) or (maxb("nodeConnec") != 'undt'  and maxb("nodeConnec") < 2.0)) and ((evenInvar("nodes") and evenInvar("nodeConnec") and (minb("nodes") != 'undt'  and maxb("nodeConnec") != 'undt'  and minb("nodes") >= maxb("nodeConnec")**3.0+maxb("nodeConnec")+1.0)) or ((oddInvar("nodes") or oddInvar("nodeConnec")) and (minb("nodes") != 'undt'  and maxb("nodeConnec") != 'undt'  and minb("nodes") > maxb("nodeConnec")**3.0+1.0))):
            try:
                set("edges",  ((minb("nodes")-(1.0))*(minb("nodeConnec")+1.0)+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (2.0*maxb("edges")+minb("nodeConnec"))/(minb("nodeConnec")+1.0), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem95(Theorem):
    def __init__(self):
        super(Theorem95, self).__init__(95, "if diameter == 2.0 and ((even nodes and even edgeConnec and nodes >= edgeConnec**3.0+edgeConnec+1.0) or ((odd nodes or odd edgeConnec) and nodes > edgeConnec**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(edgeConnec+1.0)+1.0)/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodes","edgeConnec","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt'  and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt'  and maxb("diameter") <= 2.0)) and ((evenInvar("nodes") and evenInvar("edgeConnec") and (minb("nodes") != 'undt'  and maxb("edgeConnec") != 'undt'  and minb("nodes") >= maxb("edgeConnec")**3.0+maxb("edgeConnec")+1.0)) or ((oddInvar("nodes") or oddInvar("edgeConnec")) and (minb("nodes") != 'undt'  and maxb("edgeConnec") != 'undt'  and minb("nodes") > maxb("edgeConnec")**3.0+1.0))):
            try:
                set("edges",  ((minb("nodes")-(1.0))*(minb("edgeConnec")+1.0)+1.0)/2.0, ind='Min')
            except:
                pass
            try:
                set("nodes",  (minb("edgeConnec")+2.0*maxb("edges"))/(minb("edgeConnec")+1.0), ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem96(Theorem):
    def __init__(self):
        super(Theorem96, self).__init__(96, "if defined girth then \n{\n    nodes >= (girth-(1.0))*(arboricity-(1.0))+1.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","arboricity"]
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
                set("nodes",  (minb("girth")-(1.0))*(minb("arboricity")-(1.0))+1.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (minb("arboricity")+maxb("nodes")-(2.0))/(minb("arboricity")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("arboricity",  (minb("girth")+maxb("nodes")-(2.0))/(minb("girth")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem97(Theorem):
    def __init__(self):
        super(Theorem97, self).__init__(97, "if maxClique == 2.0 and chromaticNum >= 4.0 then \n{\n    nodes >= 11.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt'  and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt'  and maxb("maxClique") <= 2.0)) and (minb("chromaticNum") != 'undt'  and minb("chromaticNum") >= 4.0):
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        
        return

class Theorem98(Theorem):
    def __init__(self):
        super(Theorem98, self).__init__(98, "let t = (girth/girth-(2.0));if girth >= 4.0 and genus >= 2.0 and chromaticNum >= 1.0+2.0*t then \n{\n    chromaticNum <= (3.0+6.0*t+sqrt(57.0-(60.0*t)+36.0*t*t+48.0*t*genus))/6.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["girth","genus","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt'  and minb("girth") >= 4.0) and (minb("genus") != 'undt'  and minb("genus") >= 2.0) and (minb("chromaticNum") != 'undt'  and minb("girth") != 'undt'  and minb("chromaticNum") >= 1.0+2.0*(minb("girth")/minb("girth")-(2.0))):
            try:
                set("chromaticNum",  (3.0+6.0*(minb("girth")/minb("girth")-(2.0))+sqrt(57.0-(60.0*(minb("girth")/minb("girth")-(2.0)))+36.0*(minb("girth")/minb("girth")-(2.0))*(minb("girth")/minb("girth")-(2.0))+48.0*(minb("girth")/minb("girth")-(2.0))*maxb("genus")))/6.0, ind='Max')
            except:
                pass
        
        return

class Theorem99(Theorem):
    def __init__(self):
        super(Theorem99, self).__init__(99, "if diameter <= 2.0 then \n{\n    edgeConnec == mindeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edgeConnec","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("diameter") != 'undt'  and maxb("diameter") <= 2.0):
            try:
                set("edgeConnec",  minb("mindeg"), ind='Min')
            except:
                pass
            try:
                set("mindeg",  maxb("edgeConnec"), ind='Max')
            except:
                pass
            try:
                set("edgeConnec",  maxb("mindeg"), ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("edgeConnec"), ind='Min')
            except:
                pass
        
        return

class Theorem100(Theorem):
    def __init__(self):
        super(Theorem100, self).__init__(100, "if nodeInd >= edgeInd then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","edgeInd","edgeCliqueCover","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeInd") != 'undt'  and maxb("edgeInd") != 'undt'  and minb("nodeInd") >= maxb("edgeInd")):
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

