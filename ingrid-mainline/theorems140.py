from INGRID_CLASSES import Theorem
from math import floor,ceil,log,sqrt,exp
import sys

def odd(x):
    return not isinstance(x, str) and x % 2 == 1
def even(x):
    return not isinstance(x, str) and x % 2 == 0

maximum = max
minimum = min

class Theorem1(Theorem):
    def __init__(self):
        super(Theorem1, self).__init__(1, "edges <= (1.0/2.0)*(nodes-(1.0))*(nodes-(2.0))+nodeConnec;\n", "")
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
        if maxb("nodes") != 'undt' and maxb("nodeConnec") != 'undt':
            try:
                set("edges",  (1.0/2.0)*(maxb("nodes")-(1.0))*(maxb("nodes")-(2.0))+maxb("nodeConnec"), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and maxb("nodeConnec") != 'undt':
            try:
                set("nodes",  sqrt(8.0*minb("edges")-(8.0*maxb("nodeConnec"))+1.0)/2.0+3.0/2.0, ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("nodeConnec",  minb("edges")-(maxb("nodes")**2.0/2.0)+3.0*maxb("nodes")/2.0-(1.0), ind='Min')
            except:
                pass
        return

class Theorem2(Theorem):
    def __init__(self):
        super(Theorem2, self).__init__(2, "chromaticNum <= (1.0/2.0)*(nodeCover+maxClique+1.0);\n", "")
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
        if maxb("nodeCover") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("chromaticNum",  (1.0/2.0)*(maxb("nodeCover")+maxb("maxClique")+1.0), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("nodeCover",  2.0*minb("chromaticNum")-(maxb("maxClique"))-(1.0), ind='Min')
            except:
                pass
        if minb("chromaticNum") != 'undt' and maxb("nodeCover") != 'undt':
            try:
                set("maxClique",  2.0*minb("chromaticNum")-(maxb("nodeCover"))-(1.0), ind='Min')
            except:
                pass
        return

class Theorem3(Theorem):
    def __init__(self):
        super(Theorem3, self).__init__(3, "spectralRadius >= 2.0*edges/nodes;\n", "")
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
        if minb("edges") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("spectralRadius",  2.0*minb("edges")/maxb("nodes"), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("spectralRadius") != 'undt':
            try:
                set("edges",  maxb("nodes")*maxb("spectralRadius")/2.0, ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and maxb("spectralRadius") != 'undt':
            try:
                set("nodes",  2.0*minb("edges")/maxb("spectralRadius"), ind='Min')
            except:
                pass
        return

class Theorem4(Theorem):
    def __init__(self):
        super(Theorem4, self).__init__(4, "spectralRadius <= (2.0*edges*nodeCover/(nodeCover+1.0))**(1.0/2.0);\n", "")
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
        if maxb("edges") != 'undt' and maxb("nodeCover") != 'undt':
            try:
                set("spectralRadius",  (2.0*maxb("edges")*maxb("nodeCover")/(maxb("nodeCover")+1.0))**(1.0/2.0), ind='Max')
            except:
                pass
        if minb("spectralRadius") != 'undt' and maxb("nodeCover") != 'undt':
            try:
                set("edges",  1.0e26*minb("spectralRadius")**2.0*(maxb("nodeCover")+1.0)/(2.000000000000014e26*maxb("nodeCover")), ind='Min')
            except:
                pass
        if minb("spectralRadius") != 'undt' and maxb("edges") != 'undt':
            try:
                set("nodeCover",  1.0e26*minb("spectralRadius")**2.0/(2.000000000000014e26*maxb("edges")-(1.0e26*minb("spectralRadius")**2.0)), ind='Min')
            except:
                pass
        return

class Theorem5(Theorem):
    def __init__(self):
        super(Theorem5, self).__init__(5, "maxClique >= nodes**2.0/(nodes**2.0-(2.0*minb(edges)));\nedges <= maxb(nodes)**2.0*(maxb(maxClique)-(1.0))/(2.0*maxb(maxClique));\n", "")
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
        if minb("nodes") != 'undt' and minb("edges") != 'undt':
            try:
                set("maxClique",  maxb("nodes")**2.0/(maxb("nodes")**2.0-(2.0*minb("edges"))), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("nodes",  sqrt(2.0)*sqrt(minb("edges")*minb("maxClique")/(minb("maxClique")-(1.0))), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("edges",  maxb("nodes")**2.0*(maxb("maxClique")-(1.0))/(2.0*maxb("maxClique")), ind='Max')
            except:
                pass
        return

class Theorem6(Theorem):
    def __init__(self):
        super(Theorem6, self).__init__(6, "spectralRadius <= maxdeg;\n", "")
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
        if maxb("maxdeg") != 'undt':
            try:
                set("spectralRadius",  maxb("maxdeg"), ind='Max')
            except:
                pass
        if minb("spectralRadius") != 'undt':
            try:
                set("maxdeg",  minb("spectralRadius"), ind='Min')
            except:
                pass
        return

class Theorem7(Theorem):
    def __init__(self):
        super(Theorem7, self).__init__(7, "if exists diameter then \n{\n    if mindeg > 3.0*nodeConnec-(1.0) then \n    {\n        nodes >= 1.0+mindeg+diameter*nodeConnec+(diameter/3.0)*(mindeg-(3.0*nodeConnec)+1.0)\n    },\n    if minb(diameter) < 3.0 then \n    {\n        nodes >= nodeConnec*(diameter-(3.0))+2.0*mindeg+2.0 and useMaxFor(nodeConnec)\n    }\n    else  \n    {\n        nodes >= nodeConnec*(diameter-(3.0))+2.0*mindeg+2.0\n    }\n};\n", "")
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
        if maxb("diameter") != 'undt':
            if (minb("mindeg") != 'undt' and maxb("nodeConnec") != 'undt' and minb("mindeg") > 3.0*maxb("nodeConnec")-(1.0)):
                if minb("mindeg") != 'undt' and minb("diameter") != 'undt' and minb("nodeConnec") != 'undt':
                    try:
                        set("nodes",  1.0+minb("mindeg")+minb("diameter")*minb("nodeConnec")+(minb("diameter")/3.0)*(minb("mindeg")-(3.0*minb("nodeConnec"))+1.0), ind='Min')
                    except:
                        pass
                if maxb("diameter") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("mindeg",  (-(minb("diameter"))+3.0*maxb("nodes")-(3.0))/(minb("diameter")+3.0), ind='Max')
                    except:
                        pass
                if maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  3.0*(-(minb("mindeg"))+maxb("nodes")-(1.0))/(minb("mindeg")+1.0), ind='Max')
                    except:
                        pass
            if (minb("diameter") != 'undt' and minb("diameter") < 3.0):
                if minb("nodeConnec") != 'undt' and minb("diameter") != 'undt' and minb("mindeg") != 'undt':
                    try:
                        set("nodes",  maxb("nodeConnec")*(minb("diameter")-(3.0))+2.0*minb("mindeg")+2.0, ind='Min')
                    except:
                        pass
                if minb("mindeg") != 'undt' and minb("nodes") != 'undt' and minb("diameter") != 'undt':
                    try:
                        set("nodeConnec",  (-(2.0*maxb("mindeg"))+minb("nodes")-(2.0))/(maxb("diameter")-(3.0)), ind='Min')
                    except:
                        pass
                if maxb("mindeg") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  (-(2.0*minb("mindeg"))+3.0*maxb("nodeConnec")+maxb("nodes")-(2.0))/maxb("nodeConnec"), ind='Max')
                    except:
                        pass
                if maxb("diameter") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("mindeg",  -(minb("diameter")*maxb("nodeConnec")/2.0)+3.0*maxb("nodeConnec")/2.0+maxb("nodes")/2.0-(1.0), ind='Max')
                    except:
                        pass
            elif True:
                if minb("nodeConnec") != 'undt' and minb("diameter") != 'undt' and minb("mindeg") != 'undt':
                    try:
                        set("nodes",  minb("nodeConnec")*(minb("diameter")-(3.0))+2.0*minb("mindeg")+2.0, ind='Min')
                    except:
                        pass
                if maxb("mindeg") != 'undt' and maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("nodeConnec",  (-(2.0*minb("mindeg"))+maxb("nodes")-(2.0))/(minb("diameter")-(3.0)), ind='Max')
                    except:
                        pass
                if maxb("mindeg") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  (-(2.0*minb("mindeg"))+3.0*maxb("nodeConnec")+maxb("nodes")-(2.0))/maxb("nodeConnec"), ind='Max')
                    except:
                        pass
                if maxb("diameter") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("mindeg",  -(minb("diameter")*maxb("nodeConnec")/2.0)+3.0*maxb("nodeConnec")/2.0+maxb("nodes")/2.0-(1.0), ind='Max')
                    except:
                        pass
        return

class Theorem8(Theorem):
    def __init__(self):
        super(Theorem8, self).__init__(8, "nodes >= minb(maxdeg)+1.0+(minb(mindeg)+1.0)*(minb(numOfComponents)-(1.0));\nmaxdeg <= -(minb(mindeg)*minb(numOfComponents))+minb(mindeg)+maxb(nodes)-(minb(numOfComponents));\nif minb(numOfComponents) > 1.0 then \n{\n    mindeg <= (-(minb(maxdeg))+maxb(nodes)-(minb(numOfComponents)))/(minb(numOfComponents)-(1.0))\n};\nnumOfComponents <= (-(minb(maxdeg))+minb(mindeg)+maxb(nodes))/(minb(mindeg)+1.0);\n", "")
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
        if minb("maxdeg") != 'undt' and minb("mindeg") != 'undt' and minb("numOfComponents") != 'undt':
            try:
                set("nodes",  minb("maxdeg")+1.0+(minb("mindeg")+1.0)*(minb("numOfComponents")-(1.0)), ind='Min')
            except:
                pass
        if maxb("mindeg") != 'undt' and maxb("numOfComponents") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxdeg",  -(minb("mindeg")*minb("numOfComponents"))+minb("mindeg")+maxb("nodes")-(minb("numOfComponents")), ind='Max')
            except:
                pass
        if (minb("numOfComponents") != 'undt' and minb("numOfComponents") > 1.0):
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("mindeg",  (-(minb("maxdeg"))+maxb("nodes")-(minb("numOfComponents")))/(minb("numOfComponents")-(1.0)), ind='Max')
                except:
                    pass
        if maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("numOfComponents",  (-(minb("maxdeg"))+minb("mindeg")+maxb("nodes"))/(minb("mindeg")+1.0), ind='Max')
            except:
                pass
        return

class Theorem9(Theorem):
    def __init__(self):
        super(Theorem9, self).__init__(9, "edgeCliqueCover <= nodes**2.0/4.0;\n", "")
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
        if maxb("nodes") != 'undt':
            try:
                set("edgeCliqueCover",  maxb("nodes")**2.0/4.0, ind='Max')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt':
            try:
                set("nodes",  2.0*sqrt(minb("edgeCliqueCover")), ind='Min')
            except:
                pass
        return

class Theorem10(Theorem):
    def __init__(self):
        super(Theorem10, self).__init__(10, "diameter <= 2.0*radius;\n", "")
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
        if maxb("radius") != 'undt':
            try:
                set("diameter",  2.0*maxb("radius"), ind='Max')
            except:
                pass
        if minb("diameter") != 'undt':
            try:
                set("radius",  minb("diameter")/2.0, ind='Min')
            except:
                pass
        return

class Theorem11(Theorem):
    def __init__(self):
        super(Theorem11, self).__init__(11, "edgeInd <= nodes/2.0;\n", "")
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
        if maxb("nodes") != 'undt':
            try:
                set("edgeInd",  maxb("nodes")/2.0, ind='Max')
            except:
                pass
        if minb("edgeInd") != 'undt':
            try:
                set("nodes",  2.0*minb("edgeInd"), ind='Min')
            except:
                pass
        return

class Theorem12(Theorem):
    def __init__(self):
        super(Theorem12, self).__init__(12, "edgeInd >= nodes/(maxdeg+1.0);\n", "")
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
        if minb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("edgeInd",  minb("nodes")/(maxb("maxdeg")+1.0), ind='Min')
            except:
                pass
        if maxb("edgeInd") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("nodes",  maxb("edgeInd")*(maxb("maxdeg")+1.0), ind='Max')
            except:
                pass
        if maxb("edgeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(maxb("edgeInd"))+minb("nodes"))/maxb("edgeInd"), ind='Min')
            except:
                pass
        return

class Theorem13(Theorem):
    def __init__(self):
        super(Theorem13, self).__init__(13, ";\n", "")
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

class Theorem14(Theorem):
    def __init__(self):
        super(Theorem14, self).__init__(14, ";\n", "")
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

class Theorem15(Theorem):
    def __init__(self):
        super(Theorem15, self).__init__(15, "if mindeg >= 3.0 then \n{\n    edges >= 2.0**(girth/2.0)+nodes-(numOfComponents)\n};\n", "")
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
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 3.0):
            if minb("girth") != 'undt' and minb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edges",  2.0**(minb("girth")/2.0)+minb("nodes")-(maxb("numOfComponents")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  2.0*log(maxb("edges")-(minb("nodes"))+maxb("numOfComponents"))/log(2.0), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("nodes",  -(2.0**(minb("girth")/2.0))+maxb("edges")+maxb("numOfComponents"), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and maxb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("numOfComponents",  2.0**(minb("girth")/2.0)-(maxb("edges"))+minb("nodes"), ind='Min')
                except:
                    pass
        return

class Theorem16(Theorem):
    def __init__(self):
        super(Theorem16, self).__init__(16, "if nodeConnec == 0.0 then \n{\n    edgeConnec == 0.0\n};\nif edgeConnec == 0.0 then \n{\n    nodeConnec == 0.0\n};\n", "")
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
        if ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 0.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 0.0)):
            try:
                set("edgeConnec",  0.0, ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  0.0, ind='Max')
            except:
                pass
        if ((minb("edgeConnec") != 'undt' and minb("edgeConnec") >= 0.0) and (maxb("edgeConnec") != 'undt' and maxb("edgeConnec") <= 0.0)):
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
        super(Theorem17, self).__init__(17, "edges <= (1.0/2.0)*(edgeCliqueCover*maxClique*(maxClique-(1.0)));\n", "")
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
        if maxb("edgeCliqueCover") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("edges",  (1.0/2.0)*(maxb("edgeCliqueCover")*maxb("maxClique")*(maxb("maxClique")-(1.0))), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("edgeCliqueCover",  2.0*minb("edges")/(maxb("maxClique")*(maxb("maxClique")-(1.0))), ind='Min')
            except:
                pass
        if maxb("edgeCliqueCover") != 'undt' and minb("edges") != 'undt':
            try:
                set("maxClique",  (maxb("edgeCliqueCover")+sqrt(maxb("edgeCliqueCover")*(maxb("edgeCliqueCover")+8.0*minb("edges"))))/(2.0*maxb("edgeCliqueCover")), ind='Min')
            except:
                pass
        return

class Theorem18(Theorem):
    def __init__(self):
        super(Theorem18, self).__init__(18, "chromaticNum <= (1.0/2.0)*(7.0+(1.0+48.0*genus)**(1.0/2.0));\n", "")
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
        if maxb("genus") != 'undt':
            try:
                set("chromaticNum",  (1.0/2.0)*(7.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("genus",  (2.0*minb("chromaticNum")-(7.0))**2.0/48.0-(1.0/48.0), ind='Min')
            except:
                pass
        return

class Theorem19(Theorem):
    def __init__(self):
        super(Theorem19, self).__init__(19, "if maxClique == 2.0 then \n{\n    maxdeg <= nodeInd,\n    edges <= nodeCover*nodeInd\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodeInd") != 'undt':
                try:
                    set("maxdeg",  maxb("nodeInd"), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt':
                try:
                    set("nodeInd",  minb("maxdeg"), ind='Min')
                except:
                    pass
            if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("edges",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodeCover",  minb("edges")/maxb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("nodeInd",  minb("edges")/maxb("nodeCover"), ind='Min')
                except:
                    pass
        return

class Theorem20(Theorem):
    def __init__(self):
        super(Theorem20, self).__init__(20, "if chromaticNum == 2.0 then \n{\n    edgeInd == nodeCover,\n    nodeInd == nodeCliqueCover,\n    edgeChromatic == maxdeg,\n    even girth,\n    even circumference\n};\nif chromaticNum == 2.0 and nodes > 2.0 then \n{\n    not complete\n};\n", "")
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
        if ((minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 2.0) and (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") <= 2.0)):
            if minb("nodeCover") != 'undt':
                try:
                    set("edgeInd",  minb("nodeCover"), ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("nodeCover",  maxb("edgeInd"), ind='Max')
                except:
                    pass
            if maxb("nodeCover") != 'undt':
                try:
                    set("edgeInd",  maxb("nodeCover"), ind='Max')
                except:
                    pass
            if minb("edgeInd") != 'undt':
                try:
                    set("nodeCover",  minb("edgeInd"), ind='Min')
                except:
                    pass
            if minb("nodeCliqueCover") != 'undt':
                try:
                    set("nodeInd",  minb("nodeCliqueCover"), ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodeCliqueCover",  maxb("nodeInd"), ind='Max')
                except:
                    pass
            if maxb("nodeCliqueCover") != 'undt':
                try:
                    set("nodeInd",  maxb("nodeCliqueCover"), ind='Max')
                except:
                    pass
            if minb("nodeInd") != 'undt':
                try:
                    set("nodeCliqueCover",  minb("nodeInd"), ind='Min')
                except:
                    pass
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
            if minb("girth") != 'undt':
                if even(minb("girth")+1.0):
                    set("girth", minb("girth")+1.0, ind='Min')
            if maxb("girth") != 'undt':
                if even(maxb("girth")-(1.0)):
                    set("girth", minb("girth")-(1.0), ind='Max')
            if minb("circumference") != 'undt':
                if even(minb("circumference")+1.0):
                    set("circumference", minb("circumference")+1.0, ind='Min')
            if maxb("circumference") != 'undt':
                if even(maxb("circumference")-(1.0)):
                    set("circumference", minb("circumference")-(1.0), ind='Max')
        if ((minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 2.0) and (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") <= 2.0)) and (minb("nodes") != 'undt' and minb("nodes") > 2.0):
            set("complete", False)
        return
class Theorem21(Theorem):
    def __init__(self):
        super(Theorem21, self).__init__(21, "genus <= ((nodes-(3.0))*(nodes-(4.0))+11.0)/12.0;\n", "")
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
        if maxb("nodes") != 'undt':
            try:
                set("genus",  ((maxb("nodes")-(3.0))*(maxb("nodes")-(4.0))+11.0)/12.0, ind='Max')
            except:
                pass
        if minb("genus") != 'undt':
            try:
                set("nodes",  sqrt(48.0*minb("genus")-(43.0))/2.0+7.0/2.0, ind='Min')
            except:
                pass
        return
class Theorem22(Theorem):
    def __init__(self):
        super(Theorem22, self).__init__(22, "if edges > maxdeg*edgeInd then \n{\n    edgeChromatic == maxdeg+1.0\n};\n", "")
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
        if (minb("edges") != 'undt' and maxb("maxdeg") != 'undt' and maxb("edgeInd") != 'undt' and minb("edges") > maxb("maxdeg")*maxb("edgeInd")):
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
class Theorem23(Theorem):
    def __init__(self):
        super(Theorem23, self).__init__(23, "edgeCliqueCover <= edgeCover*edgeInd;\n", "")
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
        if maxb("edgeCover") != 'undt' and maxb("edgeInd") != 'undt':
            try:
                set("edgeCliqueCover",  maxb("edgeCover")*maxb("edgeInd"), ind='Max')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("edgeInd") != 'undt':
            try:
                set("edgeCover",  minb("edgeCliqueCover")/maxb("edgeInd"), ind='Min')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("edgeCover") != 'undt':
            try:
                set("edgeInd",  minb("edgeCliqueCover")/maxb("edgeCover"), ind='Min')
            except:
                pass
        return
class Theorem24(Theorem):
    def __init__(self):
        super(Theorem24, self).__init__(24, "\n", "")
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
        super(Theorem25, self).__init__(25, "edgeCover >= (1.0/2.0)*nodes;\n", "")
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
        if minb("nodes") != 'undt':
            try:
                set("edgeCover",  (1.0/2.0)*minb("nodes"), ind='Min')
            except:
                pass
        if maxb("edgeCover") != 'undt':
            try:
                set("nodes",  2.0*maxb("edgeCover"), ind='Max')
            except:
                pass
        return
class Theorem26(Theorem):
    def __init__(self):
        super(Theorem26, self).__init__(26, "edges <= (1.0/2.0)*(nodes-(1.0))*(nodes-(2.0))+nodes/domination-(1.0);\n", "")
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
        if maxb("nodes") != 'undt' and maxb("domination") != 'undt':
            try:
                set("edges",  (1.0/2.0)*(maxb("nodes")-(1.0))*(maxb("nodes")-(2.0))+maxb("nodes")/minb("domination")-(1.0), ind='Max')
            except:
                pass
        if minb("domination") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodes",  (3.0*minb("domination")+sqrt(8.0*minb("domination")**2.0*minb("edges")+9.0*minb("domination")**2.0-(12.0*minb("domination"))+4.0)-(2.0))/(2.0*minb("domination")), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
            try:
                set("domination",  2.0*maxb("nodes")/(2.0*minb("edges")-(maxb("nodes")**2.0)+3.0*maxb("nodes")), ind='Max')
            except:
                pass
        return
class Theorem27(Theorem):
    def __init__(self):
        super(Theorem27, self).__init__(27, "edgeCover <= maxb(nodes)*maxb(maxdeg)/(1.0+maxb(maxdeg));\nnodes >= minb(edgeCover)+minb(edgeCover)/maxb(maxdeg);\nmaxdeg >= -(minb(edgeCover)/(minb(edgeCover)-(maxb(nodes))));\n", "")
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
        if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("edgeCover",  maxb("nodes")*maxb("maxdeg")/(1.0+maxb("maxdeg")), ind='Max')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("maxdeg") != 'undt':
            try:
                set("nodes",  minb("edgeCover")+minb("edgeCover")/maxb("maxdeg"), ind='Min')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  -(minb("edgeCover")/(minb("edgeCover")-(maxb("nodes")))), ind='Min')
            except:
                pass
        return
class Theorem28(Theorem):
    def __init__(self):
        super(Theorem28, self).__init__(28, "if exists diameter then \n{\n    if minb(diameter) <= 3.0 then \n    {\n        maxdeg <= nodes-(diameter)+1.0\n    }\n    else  \n    {\n        _nodeConnec is maximum(1.0, minb(nodeConnec)),\n        maxdeg <= nodes-(_nodeConnec*(diameter-(4.0)))-(3.0)\n    }\n};\n", "")
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
        if maxb("diameter") != 'undt':
            if (minb("diameter") != 'undt' and minb("diameter") <= 3.0):
                if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("maxdeg",  maxb("nodes")-(minb("diameter"))+1.0, ind='Max')
                    except:
                        pass
                if minb("diameter") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  minb("diameter")+minb("maxdeg")-(1.0), ind='Min')
                    except:
                        pass
                if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  -(minb("maxdeg"))+maxb("nodes")+1.0, ind='Max')
                    except:
                        pass
            elif True:
                if minb("nodeConnec") != 'undt':
                    _nodeConnec = maximum(1.0, minb("nodeConnec"))
                if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("maxdeg",  maxb("nodes")-(_nodeConnec*(minb("diameter")-(4.0)))-(3.0), ind='Max')
                    except:
                        pass
                if minb("diameter") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  _nodeConnec*minb("diameter")-(4.0*_nodeConnec)+minb("maxdeg")+3.0, ind='Min')
                    except:
                        pass
                if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  (4.0*_nodeConnec-(minb("maxdeg"))+maxb("nodes")-(3.0))/_nodeConnec, ind='Max')
                    except:
                        pass
        return
class Theorem29(Theorem):
    def __init__(self):
        super(Theorem29, self).__init__(29, "edgeCliqueCover <= edges-((1.0/2.0)*maxClique*(maxClique-(1.0)))+1.0;\n", "")
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
        if maxb("edges") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("edgeCliqueCover",  maxb("edges")-((1.0/2.0)*minb("maxClique")*(minb("maxClique")-(1.0)))+1.0, ind='Max')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("edges",  minb("edgeCliqueCover")+minb("maxClique")**2.0/2.0-(minb("maxClique")/2.0)-(1.0), ind='Min')
            except:
                pass
        if maxb("edgeCliqueCover") != 'undt' and maxb("edges") != 'undt':
            try:
                set("maxClique",  sqrt(-(8.0*minb("edgeCliqueCover"))+8.0*maxb("edges")+9.0)/2.0+1.0/2.0, ind='Max')
            except:
                pass
        return
class Theorem30(Theorem):
    def __init__(self):
        super(Theorem30, self).__init__(30, "\n", "")
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
class Theorem31(Theorem):
    def __init__(self):
        super(Theorem31, self).__init__(31, "chromaticNum <= (nodes+1.0)**2.0/(4.0*nodeCliqueCover);\n", "")
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
        if maxb("nodes") != 'undt' and maxb("nodeCliqueCover") != 'undt':
            try:
                set("chromaticNum",  (maxb("nodes")+1.0)**2.0/(4.0*minb("nodeCliqueCover")), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  2.0*sqrt(minb("chromaticNum")*minb("nodeCliqueCover"))-(1.0), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("chromaticNum") != 'undt':
            try:
                set("nodeCliqueCover",  (maxb("nodes")+1.0)**2.0/(4.0*minb("chromaticNum")), ind='Max')
            except:
                pass
        return
class Theorem32(Theorem):
    def __init__(self):
        super(Theorem32, self).__init__(32, "chromaticNum >= 2.0*nodes**(1.0/2.0)-(nodeCliqueCover);\n", "")
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
        if minb("nodes") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("chromaticNum",  2.0*minb("nodes")**(1.0/2.0)-(maxb("nodeCliqueCover")), ind='Min')
            except:
                pass
        if maxb("chromaticNum") != 'undt' and maxb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  (maxb("chromaticNum")+maxb("nodeCliqueCover"))**2.0/4.0, ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeCliqueCover",  -(maxb("chromaticNum"))+2.0*sqrt(minb("nodes")), ind='Min')
            except:
                pass
        return
class Theorem33(Theorem):
    def __init__(self):
        super(Theorem33, self).__init__(33, "domination <= nodes+1.0-((1.0+2.0*edges)**(1.0/2.0));\n", "")
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
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
            try:
                set("domination",  maxb("nodes")+1.0-((1.0+2.0*minb("edges"))**(1.0/2.0)), ind='Max')
            except:
                pass
        if minb("domination") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodes",  minb("domination")+sqrt(2.0*minb("edges")+1.0)-(1.0), ind='Min')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  (-(minb("domination"))+maxb("nodes")+1.0)**2.0/2.0-(1.0/2.0), ind='Max')
            except:
                pass
        return
class Theorem34(Theorem):
    def __init__(self):
        super(Theorem34, self).__init__(34, "if nodeConnec > 0.0 and not tree then \n{\n    girth <= 2.0*diameter+1.0\n};\n", "")
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
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") > 0.0) and get("tree") == False:
            if maxb("diameter") != 'undt':
                try:
                    set("girth",  2.0*maxb("diameter")+1.0, ind='Max')
                except:
                    pass
            if minb("girth") != 'undt':
                try:
                    set("diameter",  minb("girth")/2.0-(1.0/2.0), ind='Min')
                except:
                    pass
        return
class Theorem35(Theorem):
    def __init__(self):
        super(Theorem35, self).__init__(35, "if planar and maxClique < 3.0 then \n{\n    nodeInd >= (1.0/3.0)*(nodes+1.0),\n    nodeCover <= (2.0*nodes-(1.0))/3.0\n}\nelse if planar and (nodeInd < (1.0/3.0)*(nodes+1.0) or nodeCover > (2.0*nodes-(1.0))/3.0) then \n{\n    maxClique >= 3.0\n};\n", "")
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
        if get("planar") == True and (maxb("maxClique") != 'undt' and maxb("maxClique") < 3.0):
            if minb("nodes") != 'undt':
                try:
                    set("nodeInd",  (1.0/3.0)*(minb("nodes")+1.0), ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  3.0*maxb("nodeInd")-(1.0), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (2.0*maxb("nodes")-(1.0))/3.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  3.0*minb("nodeCover")/2.0+1.0/2.0, ind='Min')
                except:
                    pass
        elif get("planar") == True and ((maxb("nodeInd") != 'undt' and minb("nodes") != 'undt' and maxb("nodeInd") < (1.0/3.0)*(minb("nodes")+1.0)) or (minb("nodeCover") != 'undt' and maxb("nodes") != 'undt' and minb("nodeCover") > (2.0*maxb("nodes")-(1.0))/3.0)):
            try:
                set("maxClique",  3.0, ind='Min')
            except:
                pass
        return
class Theorem36(Theorem):
    def __init__(self):
        super(Theorem36, self).__init__(36, "if not planar then \n{\n    maxdeg >= 3.0,\n    nodes >= 5.0,\n    edges >= 9.0,\n    edgeInd >= 2.0,\n    nodeCover >= 3.0,\n    edgeCover >= 3.0,\n    bandwidth >= 4.0\n};\n", "")
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
        if get("planar") == False:
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
        super(Theorem37, self).__init__(37, "edges <= numOfComponents-(1.0)+(nodes+2.0-(2.0*numOfComponents))*(nodes+1.0-(2.0*numOfComponents))/2.0;\n", "")
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
        if maxb("numOfComponents") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  minb("numOfComponents")-(1.0)+(maxb("nodes")+2.0-(2.0*minb("numOfComponents")))*(maxb("nodes")+1.0-(2.0*minb("numOfComponents")))/2.0, ind='Max')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
            try:
                set("numOfComponents",  maxb("nodes")/2.0+sqrt(2.0*maxb("edges")-(maxb("nodes"))+1.0)/2.0+1.0/2.0, ind='Max')
            except:
                pass
        if minb("numOfComponents") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodes",  2.0*minb("numOfComponents")+sqrt(8.0*minb("edges")-(8.0*minb("numOfComponents"))+9.0)/2.0-(3.0/2.0), ind='Min')
            except:
                pass
        return
class Theorem38(Theorem):
    def __init__(self):
        super(Theorem38, self).__init__(38, "domination >= nodes/(maxdeg+1.0);\n", "")
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
        if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
            try:
                set("domination",  minb("nodes")/(maxb("maxdeg")+1.0), ind='Min')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("nodes",  maxb("domination")*(maxb("maxdeg")+1.0), ind='Max')
            except:
                pass
        if minb("domination") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(maxb("domination"))+minb("nodes"))/maxb("domination"), ind='Min')
            except:
                pass
        return
class Theorem39(Theorem):
    def __init__(self):
        super(Theorem39, self).__init__(39, "if girth >= 4.0 or maxClique <= 2.0 then \n{\n    maxClique <= 2.0,\n    girth >= 4.0\n};\n", "")
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
        if (minb("girth") != 'undt' and minb("girth") >= 4.0) or (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0):
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
        super(Theorem40, self).__init__(40, "if complete or mindeg == nodes-(1.0) or nodeInd == 1.0 or nodeCliqueCover == 1.0 or edgeCliqueCover == 1.0 or diameter == 1.0 then \n{\n    complete,\n    mindeg == nodes-(1.0),\n    nodeInd == 1.0,\n    nodeCliqueCover == 1.0,\n    edgeCliqueCover == 1.0,\n    diameter == 1.0\n};\n", "")
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
        if get("complete") == True or ((minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")-(1.0)) and (maxb("mindeg") != 'undt' and minb("nodes") != 'undt' and maxb("mindeg") <= minb("nodes")-(1.0))) or ((minb("nodeInd") != 'undt' and minb("nodeInd") >= 1.0) and (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 1.0)) or ((minb("nodeCliqueCover") != 'undt' and minb("nodeCliqueCover") >= 1.0) and (maxb("nodeCliqueCover") != 'undt' and maxb("nodeCliqueCover") <= 1.0)) or ((minb("edgeCliqueCover") != 'undt' and minb("edgeCliqueCover") >= 1.0) and (maxb("edgeCliqueCover") != 'undt' and maxb("edgeCliqueCover") <= 1.0)) or ((minb("diameter") != 'undt' and minb("diameter") >= 1.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 1.0)):
            set("complete", True)
            if minb("nodes") != 'undt':
                try:
                    set("mindeg",  minb("nodes")-(1.0), ind='Min')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("nodes",  maxb("mindeg")+1.0, ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("mindeg",  maxb("nodes")-(1.0), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
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

class Theorem41(Theorem):
    def __init__(self):
        super(Theorem41, self).__init__(41, "if chromaticNum <= 2.0 or bipartite then \n{\n    bipartite,\n    chromaticNum <= 2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","bipartite"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") <= 2.0) or get("bipartite") == True:
            set("bipartite", True)
            try:
                set("chromaticNum",  2.0, ind='Max')
            except:
                pass
        return
class Theorem42(Theorem):
    def __init__(self):
        super(Theorem42, self).__init__(42, "if radius == 1.0 or maxdeg == nodes-(1.0) then \n{\n    maxdeg == nodes-(1.0),\n    radius == 1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["radius","maxdeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("radius") != 'undt' and minb("radius") >= 1.0) and (maxb("radius") != 'undt' and maxb("radius") <= 1.0)) or ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(1.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(1.0))):
            if minb("nodes") != 'undt':
                try:
                    set("maxdeg",  minb("nodes")-(1.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("maxdeg")+1.0, ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  maxb("nodes")-(1.0), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt':
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
        super(Theorem43, self).__init__(43, "if (forest and connected) or tree then \n{\n    tree,\n    forest,\n    connected\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","connected","tree"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (get("forest") == True and get("connected") == True) or get("tree") == True:
            set("tree", True)
            set("forest", True)
            set("connected", True)
        return
class Theorem44(Theorem):
    def __init__(self):
        super(Theorem44, self).__init__(44, "if connected or nodeConnec >= 1.0 or numOfComponents == 1.0 or radius <= nodes/2.0 or diameter <= nodes-(1.0) then \n{\n    connected,\n    nodeConnec >= 1.0,\n    numOfComponents == 1.0,\n    radius <= nodes/2.0,\n    diameter <= nodes-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodeConnec","numOfComponents","radius","nodes","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True or (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 1.0) or ((minb("numOfComponents") != 'undt' and minb("numOfComponents") >= 1.0) and (maxb("numOfComponents") != 'undt' and maxb("numOfComponents") <= 1.0)) or (maxb("radius") != 'undt' and minb("nodes") != 'undt' and maxb("radius") <= minb("nodes")/2.0) or (maxb("diameter") != 'undt' and minb("nodes") != 'undt' and maxb("diameter") <= minb("nodes")-(1.0)):
            set("connected", True)
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
            if maxb("nodes") != 'undt':
                try:
                    set("radius",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if minb("radius") != 'undt':
                try:
                    set("nodes",  2.0*minb("radius"), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("diameter",  maxb("nodes")-(1.0), ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt':
                try:
                    set("nodes",  minb("diameter")+1.0, ind='Min')
                except:
                    pass
        return
class Theorem45(Theorem):
    def __init__(self):
        super(Theorem45, self).__init__(45, "if cycle or (maxdeg == 2.0 and mindeg == 2.0 and connected) then \n{\n    cycle,\n    maxdeg == 2.0,\n    mindeg == 2.0,\n    connected\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["cycle","maxdeg","mindeg","connected"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("cycle") == True or (((minb("maxdeg") != 'undt' and minb("maxdeg") >= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0)) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and get("connected") == True):
            set("cycle", True)
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
            set("connected", True)
        return
class Theorem46(Theorem):
    def __init__(self):
        super(Theorem46, self).__init__(46, "if regular or mindeg == maxdeg then \n{\n    regular,\n    mindeg == maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True or ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))):
            set("regular", True)
            if minb("maxdeg") != 'undt':
                try:
                    set("mindeg",  minb("maxdeg"), ind='Min')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("maxdeg",  maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt':
                try:
                    set("mindeg",  maxb("maxdeg"), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("maxdeg",  minb("mindeg"), ind='Min')
                except:
                    pass
        return
class Theorem47(Theorem):
    def __init__(self):
        super(Theorem47, self).__init__(47, "if genus == 0.0 or planar or thickness == 1.0 then \n{\n    genus == 0.0,\n    planar,\n    thickness == 1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","planar","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("genus") != 'undt' and minb("genus") >= 0.0) and (maxb("genus") != 'undt' and maxb("genus") <= 0.0)) or get("planar") == True or ((minb("thickness") != 'undt' and minb("thickness") >= 1.0) and (maxb("thickness") != 'undt' and maxb("thickness") <= 1.0)):
            try:
                set("genus",  0.0, ind='Min')
            except:
                pass
            try:
                set("genus",  0.0, ind='Max')
            except:
                pass
            set("planar", True)
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
        super(Theorem48, self).__init__(48, "if forest then \n{\n    planar,\n    chromaticNum == 2.0,\n    mindeg == 2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","planar","chromaticNum","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == True:
            set("planar", True)
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
        super(Theorem49, self).__init__(49, "if cycle then \n{\n    planar,\n    not forest,\n    crossing == 0.0,\n    nodes >= 2.0,\n    edges >= 3.0,\n    arboricity == 2.0,\n    nodeCover == (nodes+1.0)/2.0,\n    edgeCover == (nodes+1.0)/2.0,\n    nodeInd == nodes/2.0,\n    edgeInd == nodes/2.0,\n    radius == edgeInd,\n    girth == circumference,\n    circumference == nodes,\n    edgeChromatic == chromaticNum,\n    nodes >= 2.0*nodeCover-(1.0),\n    nodes <= 2.0*nodeCover,\n    nodes >= 2.0*edgeInd,\n    nodes <= 2.0*edgeInd+1.0,\n    nodeConnec == 2.0,\n    regular,\n    bandwidth == 2.0,\n    if nodes > 3.0 then \n    {\n        maxClique == 2.0\n    }\n    else  \n    {\n        maxClique == 3.0\n    },\n    if even nodes then \n    {\n        chromaticNum == 2.0\n    }\n    else  \n    {\n        chromaticNum == 3.0\n    },\n    if chromaticNum == 2.0 then \n    {\n        even nodes\n    }\n    else  \n    {\n        odd nodes\n    },\n    if maxClique == 2.0 then \n    {\n        nodes >= 4.0\n    }\n    else  \n    {\n        nodes == 3.0\n    },\n    if nodes == 3.0 then \n    {\n        nodeCliqueCover == 1.0\n    }\n    else  \n    {\n        nodeCliqueCover == nodeCover\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["cycle","planar","forest","crossing","nodes","edges","arboricity","nodeCover","edgeCover","nodeInd","edgeInd","radius","girth","circumference","edgeChromatic","chromaticNum","nodeConnec","regular","bandwidth","maxClique","nodeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("cycle") == True:
            set("planar", True)
            set("forest", False)
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
            if minb("nodes") != 'undt':
                try:
                    set("nodeCover",  (minb("nodes")+1.0)/2.0, ind='Min')
                except:
                    pass
            if maxb("nodeCover") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeCover")-(1.0), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeCover")-(1.0), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("edgeCover",  (minb("nodes")+1.0)/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeCover") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeCover")-(1.0), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeCover")-(1.0), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("nodeInd",  minb("nodes")/2.0, ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeInd"), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeInd",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if minb("nodeInd") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("edgeInd",  minb("nodes")/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeInd"), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeInd",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if minb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeInd"), ind='Min')
                except:
                    pass
            if minb("edgeInd") != 'undt':
                try:
                    set("radius",  minb("edgeInd"), ind='Min')
                except:
                    pass
            if maxb("radius") != 'undt':
                try:
                    set("edgeInd",  maxb("radius"), ind='Max')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("radius",  maxb("edgeInd"), ind='Max')
                except:
                    pass
            if minb("radius") != 'undt':
                try:
                    set("edgeInd",  minb("radius"), ind='Min')
                except:
                    pass
            if minb("circumference") != 'undt':
                try:
                    set("girth",  minb("circumference"), ind='Min')
                except:
                    pass
            if maxb("girth") != 'undt':
                try:
                    set("circumference",  maxb("girth"), ind='Max')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("girth",  maxb("circumference"), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt':
                try:
                    set("circumference",  minb("girth"), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("circumference",  minb("nodes"), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("nodes",  maxb("circumference"), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("circumference",  maxb("nodes"), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt':
                try:
                    set("nodes",  minb("circumference"), ind='Min')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("edgeChromatic",  minb("chromaticNum"), ind='Min')
                except:
                    pass
            if maxb("edgeChromatic") != 'undt':
                try:
                    set("chromaticNum",  maxb("edgeChromatic"), ind='Max')
                except:
                    pass
            if maxb("chromaticNum") != 'undt':
                try:
                    set("edgeChromatic",  maxb("chromaticNum"), ind='Max')
                except:
                    pass
            if minb("edgeChromatic") != 'undt':
                try:
                    set("chromaticNum",  minb("edgeChromatic"), ind='Min')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeCover")-(1.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
                except:
                    pass
            if maxb("nodeCover") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeCover"), ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("nodeCover",  minb("nodes")/2.0, ind='Min')
                except:
                    pass
            if minb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeInd"), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeInd",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeInd")+1.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
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
            set("regular", True)
            try:
                set("bandwidth",  2.0, ind='Min')
            except:
                pass
            try:
                set("bandwidth",  2.0, ind='Max')
            except:
                pass
            if (minb("nodes") != 'undt' and minb("nodes") > 3.0):
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
            if evenInvar("nodes"):
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
            if ((minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 2.0) and (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") <= 2.0)):
                if minb("nodes") != 'undt':
                    if even(minb("nodes")+1.0):
                        set("nodes", minb("nodes")+1.0, ind='Min')
                if maxb("nodes") != 'undt':
                    if even(maxb("nodes")-(1.0)):
                        set("nodes", minb("nodes")-(1.0), ind='Max')
            elif True:
                if minb("nodes") != 'undt':
                    if odd(minb("nodes")+1.0):
                        set("nodes", minb("nodes")+1.0, ind='Min')
                if maxb("nodes") != 'undt':
                    if odd(maxb("nodes")-(1.0)):
                        set("nodes", minb("nodes")-(1.0), ind='Max')
            if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
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
            if ((minb("nodes") != 'undt' and minb("nodes") >= 3.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 3.0)):
                try:
                    set("nodeCliqueCover",  1.0, ind='Min')
                except:
                    pass
                try:
                    set("nodeCliqueCover",  1.0, ind='Max')
                except:
                    pass
            elif True:
                if minb("nodeCover") != 'undt':
                    try:
                        set("nodeCliqueCover",  minb("nodeCover"), ind='Min')
                    except:
                        pass
                if maxb("nodeCliqueCover") != 'undt':
                    try:
                        set("nodeCover",  maxb("nodeCliqueCover"), ind='Max')
                    except:
                        pass
                if maxb("nodeCover") != 'undt':
                    try:
                        set("nodeCliqueCover",  maxb("nodeCover"), ind='Max')
                    except:
                        pass
                if minb("nodeCliqueCover") != 'undt':
                    try:
                        set("nodeCover",  minb("nodeCliqueCover"), ind='Min')
                    except:
                        pass
        return
class Theorem50(Theorem):
    def __init__(self):
        super(Theorem50, self).__init__(50, "if forest or edges == nodes-(numOfComponents) or arboricity == 1.0 or undefined girth or undefined circumference then \n{\n    forest,\n    edges == nodes-(numOfComponents),\n    arboricity == 1.0,\n    undefined girth,\n    undefined circumference\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","arboricity","girth","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == True or ((minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt' and minb("edges") >= maxb("nodes")-(minb("numOfComponents"))) and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt' and maxb("edges") <= minb("nodes")-(maxb("numOfComponents")))) or ((minb("arboricity") != 'undt' and minb("arboricity") >= 1.0) and (maxb("arboricity") != 'undt' and maxb("arboricity") <= 1.0)) or minb("girth") == 'undt' or minb("circumference") == 'undt':
            set("forest", True)
            if minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("edges",  minb("nodes")-(maxb("numOfComponents")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("nodes",  maxb("edges")+maxb("numOfComponents"), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(maxb("edges"))+minb("nodes"), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edges",  maxb("nodes")-(minb("numOfComponents")), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  minb("edges")+minb("numOfComponents"), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
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
            set("girth", 'undt', ind='Min')
            set("circumference", 'undt', ind='Min')
        return
class Theorem51(Theorem):
    def __init__(self):
        super(Theorem51, self).__init__(51, "arboricity >= chromaticNum/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("chromaticNum") != 'undt':
            try:
                set("arboricity",  minb("chromaticNum")/2.0, ind='Min')
            except:
                pass
        if maxb("arboricity") != 'undt':
            try:
                set("chromaticNum",  2.0*maxb("arboricity"), ind='Max')
            except:
                pass
        return
class Theorem52(Theorem):
    def __init__(self):
        super(Theorem52, self).__init__(52, "if (connected and not cycle and (not complete or even nodes)) or (maxClique <= maxdeg and maxdeg >= 4.0 and regular) then \n{\n    arboricity <= (1.0+maxdeg)/2.0\n};\narboricity <= 1.0+spectralRadius/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","cycle","complete","nodes","maxClique","maxdeg","regular","arboricity","spectralRadius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (get("connected") == True and get("cycle") == False and (get("complete") == False or evenInvar("nodes"))) or ((maxb("maxClique") != 'undt' and minb("maxdeg") != 'undt' and maxb("maxClique") <= minb("maxdeg")) and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 4.0) and get("regular") == True):
            if maxb("maxdeg") != 'undt':
                try:
                    set("arboricity",  (1.0+maxb("maxdeg"))/2.0, ind='Max')
                except:
                    pass
            if minb("arboricity") != 'undt':
                try:
                    set("maxdeg",  2.0*minb("arboricity")-(1.0), ind='Min')
                except:
                    pass
        if maxb("spectralRadius") != 'undt':
            try:
                set("arboricity",  1.0+maxb("spectralRadius")/2.0, ind='Max')
            except:
                pass
        if minb("arboricity") != 'undt':
            try:
                set("spectralRadius",  2.0*minb("arboricity")-(2.0), ind='Min')
            except:
                pass
        return
class Theorem53(Theorem):
    def __init__(self):
        super(Theorem53, self).__init__(53, "\n", "")
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
class Theorem54(Theorem):
    def __init__(self):
        super(Theorem54, self).__init__(54, "if planar then \n{\n    mindeg <= 5.0,\n    maxClique <= 4.0,\n    arboricity <= 3.0,\n    crossing == 0.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","maxClique","arboricity","crossing"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True:
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
        super(Theorem55, self).__init__(55, "\n", "")
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
class Theorem56(Theorem):
    def __init__(self):
        super(Theorem56, self).__init__(56, "\n", "")
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
class Theorem57(Theorem):
    def __init__(self):
        super(Theorem57, self).__init__(57, "if regular and odd mindeg then \n{\n    even nodes\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and oddInvar("mindeg"):
            if minb("nodes") != 'undt':
                if even(minb("nodes")+1.0):
                    set("nodes", minb("nodes")+1.0, ind='Min')
            if maxb("nodes") != 'undt':
                if even(maxb("nodes")-(1.0)):
                    set("nodes", minb("nodes")-(1.0), ind='Max')
        return
class Theorem58(Theorem):
    def __init__(self):
        super(Theorem58, self).__init__(58, "\n", "")
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
class Theorem59(Theorem):
    def __init__(self):
        super(Theorem59, self).__init__(59, "nosolve crossing <= (1.0/4.0)*floor(nodes/2.0)*floor((nodes-(1.0))/2.0)*floor((nodes-(2.0))/2.0)*floor((nodes-(3.0))/2.0);\nif complete and nodes <= 10.0 then \n{\n    nosolve crossing >= (1.0/4.0)*floor(nodes/2.0)*floor((nodes-(1.0))/2.0)*floor((nodes-(2.0))/2.0)*floor((nodes-(3.0))/2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["crossing","nodes","complete"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt':
            try:
                set("crossing",  (1.0/4.0)*floor(maxb("nodes")/2.0)*floor((maxb("nodes")-(1.0))/2.0)*floor((maxb("nodes")-(2.0))/2.0)*floor((maxb("nodes")-(3.0))/2.0), ind='Max')
            except:
                pass
        if get("complete") == True and (maxb("nodes") != 'undt' and maxb("nodes") <= 10.0):
            if minb("nodes") != 'undt':
                try:
                    set("crossing",  (1.0/4.0)*floor(minb("nodes")/2.0)*floor((minb("nodes")-(1.0))/2.0)*floor((minb("nodes")-(2.0))/2.0)*floor((minb("nodes")-(3.0))/2.0), ind='Min')
                except:
                    pass
        return
class Theorem60(Theorem):
    def __init__(self):
        super(Theorem60, self).__init__(60, "\n", "")
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

class Theorem61(Theorem):
    def __init__(self):
        super(Theorem61, self).__init__(61, "if genus <= 1.0 then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n};\n", "")
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
        if (maxb("genus") != 'undt' and maxb("genus") <= 1.0):
            if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("edgeCliqueCover",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("nodeCover",  minb("edgeCliqueCover")/maxb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodeInd",  minb("edgeCliqueCover")/maxb("nodeCover"), ind='Min')
                except:
                    pass
        return
class Theorem62(Theorem):
    def __init__(self):
        super(Theorem62, self).__init__(62, "if mindeg >= nodes/2.0 then \n{\n    nodeConnec >= nodeInd\n};\n", "")
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
        if (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")/2.0):
            if minb("nodeInd") != 'undt':
                try:
                    set("nodeConnec",  minb("nodeInd"), ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt':
                try:
                    set("nodeInd",  maxb("nodeConnec"), ind='Max')
                except:
                    pass
        return
class Theorem63(Theorem):
    def __init__(self):
        super(Theorem63, self).__init__(63, "if connected then \n{\n    diameter <= (2.0*nodes+1.0-(sqrt(8.0*edges-(8.0*nodes)+17.0)))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("diameter",  (2.0*maxb("nodes")+1.0-(sqrt(8.0*minb("edges")-(8.0*maxb("nodes"))+17.0)))/2.0, ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  minb("diameter")+sqrt(-(8.0*minb("diameter"))+8.0*minb("edges")+25.0)/2.0-(3.0/2.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("edges",  maxb("nodes")+(-(2.0*minb("diameter"))+2.0*maxb("nodes")+1.0)**2.0/8.0-(17.0/8.0), ind='Max')
                except:
                    pass
        return
class Theorem64(Theorem):
    def __init__(self):
        super(Theorem64, self).__init__(64, "if nodes >= 3.0 and nodeConnec >= nodeInd then \n{\n    hamiltonian\n};\n", "")
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
        if (minb("nodes") != 'undt' and minb("nodes") >= 3.0) and (minb("nodeConnec") != 'undt' and maxb("nodeInd") != 'undt' and minb("nodeConnec") >= maxb("nodeInd")):
            set("hamiltonian", True)
        return
class Theorem65(Theorem):
    def __init__(self):
        super(Theorem65, self).__init__(65, "if edges >= (nodes**2.0-(3.0*nodes)+6.0) then \n{\n    hamiltonian\n};\n", "")
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
        if (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= (maxb("nodes")**2.0-(3.0*maxb("nodes"))+6.0)):
            set("hamiltonian", True)
        return
class Theorem66(Theorem):
    def __init__(self):
        super(Theorem66, self).__init__(66, "if planar and nodeConnec >= 4.0 then \n{\n    hamiltonian\n};\n", "")
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
        if get("planar") == True and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 4.0):
            set("hamiltonian", True)
        return
class Theorem67(Theorem):
    def __init__(self):
        super(Theorem67, self).__init__(67, "\n", "")
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
        super(Theorem68, self).__init__(68, "if complete then \n{\n    regular,\n    if even nodes then \n    {\n        edgeChromatic == nodes-(1.0)\n    }\n    else  \n    {\n        edgeChromatic == nodes\n    }\n};\n", "")
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
        if get("complete") == True:
            set("regular", True)
            if evenInvar("nodes"):
                if minb("nodes") != 'undt':
                    try:
                        set("edgeChromatic",  minb("nodes")-(1.0), ind='Min')
                    except:
                        pass
                if maxb("edgeChromatic") != 'undt':
                    try:
                        set("nodes",  maxb("edgeChromatic")+1.0, ind='Max')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("edgeChromatic",  maxb("nodes")-(1.0), ind='Max')
                    except:
                        pass
                if minb("edgeChromatic") != 'undt':
                    try:
                        set("nodes",  minb("edgeChromatic")+1.0, ind='Min')
                    except:
                        pass
            elif True:
                if minb("nodes") != 'undt':
                    try:
                        set("edgeChromatic",  minb("nodes"), ind='Min')
                    except:
                        pass
                if maxb("edgeChromatic") != 'undt':
                    try:
                        set("nodes",  maxb("edgeChromatic"), ind='Max')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("edgeChromatic",  maxb("nodes"), ind='Max')
                    except:
                        pass
                if minb("edgeChromatic") != 'undt':
                    try:
                        set("nodes",  minb("edgeChromatic"), ind='Min')
                    except:
                        pass
        return
class Theorem69(Theorem):
    def __init__(self):
        super(Theorem69, self).__init__(69, "chromaticNum >= 2.0*edges/(2.0*edges-(spectralRadius**2.0)):useMaxFor(edges);\n", "")
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
        if minb("edges") != 'undt' and minb("spectralRadius") != 'undt':
            try:
                set("chromaticNum",  2.0*maxb("edges")/(2.0*maxb("edges")-(minb("spectralRadius")**2.0)), ind='Min')
            except:
                pass
        if minb("chromaticNum") != 'undt' and minb("spectralRadius") != 'undt':
            try:
                set("edges",  maxb("chromaticNum")*minb("spectralRadius")**2.0/(2.0*(maxb("chromaticNum")-(1.0))), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("chromaticNum") != 'undt':
            try:
                set("spectralRadius",  sqrt(2.0)*sqrt(maxb("edges")-(maxb("edges")/maxb("chromaticNum"))), ind='Max')
            except:
                pass
        return
class Theorem70(Theorem):
    def __init__(self):
        super(Theorem70, self).__init__(70, "if genus <= 1.0 and girth == 3.0 then \n{\n    chromaticNum <= 7.0\n}\nelse if genus <= 1.0 and girth >= 4.0 then \n{\n    chromaticNum <= 4.0\n};\n", "")
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
        if (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and ((minb("girth") != 'undt' and minb("girth") >= 3.0) and (maxb("girth") != 'undt' and maxb("girth") <= 3.0)):
            try:
                set("chromaticNum",  7.0, ind='Max')
            except:
                pass
        elif (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and (minb("girth") != 'undt' and minb("girth") >= 4.0):
            try:
                set("chromaticNum",  4.0, ind='Max')
            except:
                pass
        return
class Theorem71(Theorem):
    def __init__(self):
        super(Theorem71, self).__init__(71, "if exists girth then \n{\n    circumference <= nodes-((numOfComponents-(1.0))*(mindeg+1.0)),\n    circumference <= edges-((numOfComponents-(1.0))*mindeg),\n    maxdeg >= 2.0\n};\n", "")
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
        if maxb("girth") != 'undt':
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("circumference",  maxb("nodes")-((minb("numOfComponents")-(1.0))*(minb("mindeg")+1.0)), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt' and minb("mindeg") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  minb("circumference")+minb("mindeg")*minb("numOfComponents")-(minb("mindeg"))+minb("numOfComponents")-(1.0), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  (-(minb("circumference"))+maxb("mindeg")+maxb("nodes")+1.0)/(maxb("mindeg")+1.0), ind='Max')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("mindeg",  (-(minb("circumference"))+maxb("nodes")-(minb("numOfComponents"))+1.0)/(minb("numOfComponents")-(1.0)), ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("circumference",  maxb("edges")-((minb("numOfComponents")-(1.0))*minb("mindeg")), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt' and minb("mindeg") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("edges",  minb("circumference")+minb("mindeg")*minb("numOfComponents")-(minb("mindeg")), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("edges") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("numOfComponents",  (-(minb("circumference"))+maxb("edges")+maxb("mindeg"))/maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt':
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
        super(Theorem72, self).__init__(72, "if hamiltonian or circumference == nodes then \n{\n    hamiltonian,\n    circumference == nodes\n};\n", "")
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
        if get("hamiltonian") == True or ((minb("circumference") != 'undt' and maxb("nodes") != 'undt' and minb("circumference") >= maxb("nodes")) and (maxb("circumference") != 'undt' and minb("nodes") != 'undt' and maxb("circumference") <= minb("nodes"))):
            set("hamiltonian", True)
            if minb("nodes") != 'undt':
                try:
                    set("circumference",  minb("nodes"), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("nodes",  maxb("circumference"), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("circumference",  maxb("nodes"), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt':
                try:
                    set("nodes",  minb("circumference"), ind='Min')
                except:
                    pass
        return
class Theorem73(Theorem):
    def __init__(self):
        super(Theorem73, self).__init__(73, "if hamiltonian then \n{\n    arboricity >= 2.0,\n    nodeConnec >= 2.0,\n    nodeInd <= nodes/2.0,\n    edgeCover <= (nodes+1.0)/2.0,\n    nodeCliqueCover <= (nodes+1.0)/2.0,\n    nodeCover >= nodes/2.0,\n    edgeInd >= (nodes-(1.0))/2.0\n};\n", "")
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
        if get("hamiltonian") == True:
            try:
                set("arboricity",  2.0, ind='Min')
            except:
                pass
            try:
                set("nodeConnec",  2.0, ind='Min')
            except:
                pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeInd",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if minb("nodeInd") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeInd"), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeCover")-(1.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCliqueCover",  (maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("nodeCliqueCover") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeCliqueCover")-(1.0), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("nodeCover",  minb("nodes")/2.0, ind='Min')
                except:
                    pass
            if maxb("nodeCover") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeCover"), ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("edgeInd",  (minb("nodes")-(1.0))/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeInd")+1.0, ind='Max')
                except:
                    pass
        return
class Theorem74(Theorem):
    def __init__(self):
        super(Theorem74, self).__init__(74, "", "")
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
        return
class Theorem75(Theorem):
    def __init__(self):
        super(Theorem75, self).__init__(75, "_nind is maxb(nodeInd);\nedges >= (nodes/_nind)*(nodes-(_nind*(nodes/_nind+1.0)/2.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeInd") != 'undt':
            _nind = maxb("nodeInd")
        if minb("nodes") != 'undt':
            try:
                set("edges",  (minb("nodes")/_nind)*(minb("nodes")-(_nind*(minb("nodes")/_nind+1.0)/2.0)), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt':
            try:
                set("nodes",  _nind/2.0+sqrt(_nind*(_nind+8.0*maxb("edges")))/2.0, ind='Max')
            except:
                pass
        return
class Theorem76(Theorem):
    def __init__(self):
        super(Theorem76, self).__init__(76, "edgeCliqueCover <= nodeCliqueCover+nodes*(nodeCliqueCover-(1.0))/2.0;\n", "")
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
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edgeCliqueCover",  maxb("nodeCliqueCover")+maxb("nodes")*(maxb("nodeCliqueCover")-(1.0))/2.0, ind='Max')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeCliqueCover",  (2.0*minb("edgeCliqueCover")+minb("nodes"))/(minb("nodes")+2.0), ind='Min')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  2.0*(minb("edgeCliqueCover")-(maxb("nodeCliqueCover")))/(maxb("nodeCliqueCover")-(1.0)), ind='Min')
            except:
                pass
        return
class Theorem77(Theorem):
    def __init__(self):
        super(Theorem77, self).__init__(77, "if nodes >= 6.0*mindeg and edges > (1.0/2.0)*(nodes-(mindeg))*(nodes-(mindeg)-(1.0))+mindeg**2.0 then \n{\n    hamiltonian\n};\n", "")
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
        if (minb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodes") >= 6.0*maxb("mindeg")) and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("edges") > (1.0/2.0)*(maxb("nodes")-(maxb("mindeg")))*(maxb("nodes")-(maxb("mindeg"))-(1.0))+maxb("mindeg")**2.0):
            set("hamiltonian", True)
        return
class Theorem78(Theorem):
    def __init__(self):
        super(Theorem78, self).__init__(78, "if nodes >= 4.0 and edges >= 2.0*nodes-(3.0) then \n{\n    girth <= (circumference+2.0)/2.0\n};\n", "")
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
        if (minb("nodes") != 'undt' and minb("nodes") >= 4.0) and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= 2.0*maxb("nodes")-(3.0)):
            if maxb("circumference") != 'undt':
                try:
                    set("girth",  (maxb("circumference")+2.0)/2.0, ind='Max')
                except:
                    pass
            if minb("girth") != 'undt':
                try:
                    set("circumference",  2.0*minb("girth")-(2.0), ind='Min')
                except:
                    pass
        return
class Theorem79(Theorem):
    def __init__(self):
        super(Theorem79, self).__init__(79, "if not forest then \n{\n    nodeInd >= minb(girth)/2.0,\n    radius >= minb(girth)/2.0,\n    girth <= minimum(maxb(radius)*2.0+1.0, 2.0*maxb(nodeInd)+1.0),\n    edgeInd >= minb(circumference)/2.0,\n    circumference <= 2.0*maxb(edgeInd)\n};\n", "")
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
        if get("forest") == False:
            if minb("girth") != 'undt':
                try:
                    set("nodeInd",  minb("girth")/2.0, ind='Min')
                except:
                    pass
            if minb("girth") != 'undt':
                try:
                    set("radius",  minb("girth")/2.0, ind='Min')
                except:
                    pass
            if maxb("radius") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("girth",  minimum(maxb("radius")*2.0+1.0, 2.0*maxb("nodeInd")+1.0), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt':
                try:
                    set("edgeInd",  minb("circumference")/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("circumference",  2.0*maxb("edgeInd"), ind='Max')
                except:
                    pass
        return
class Theorem80(Theorem):
    def __init__(self):
        super(Theorem80, self).__init__(80, "if (defined girth and girth >= 4.0) or (undefined girth and nodes > 2.0) then \n{\n    not complete\n};\n", "")
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
        if (minb("girth") != 'undt' and (minb("girth") != 'undt' and minb("girth") >= 4.0)) or (minb("girth") == 'undt' and (minb("nodes") != 'undt' and minb("nodes") > 2.0)):
            set("complete", False)
        return

class Theorem81(Theorem):
    def __init__(self):
        super(Theorem81, self).__init__(81, "\n", "")
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
class Theorem82(Theorem):
    def __init__(self):
        super(Theorem82, self).__init__(82, "if mindeg >= nodes/2.0 then \n{\n    edgeConnec == mindeg\n};\n", "")
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
        if (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")/2.0):
            if minb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  minb("mindeg"), ind='Min')
                except:
                    pass
            if maxb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  maxb("edgeConnec"), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  maxb("mindeg"), ind='Max')
                except:
                    pass
            if minb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  minb("edgeConnec"), ind='Min')
                except:
                    pass
        return
class Theorem83(Theorem):
    def __init__(self):
        super(Theorem83, self).__init__(83, "if exists genus and genus > 0.0 then \n{\n    arboricity <= 9.0+(1.0+48.0*genus)**(1.0/2.0)/4.0\n};\n", "")
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
        if maxb("genus") != 'undt' and (minb("genus") != 'undt' and minb("genus") > 0.0):
            if maxb("genus") != 'undt':
                try:
                    set("arboricity",  9.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)/4.0, ind='Max')
                except:
                    pass
            if minb("arboricity") != 'undt':
                try:
                    set("genus",  (minb("arboricity")-(9.0))**2.0/3.0-(1.0/48.0), ind='Min')
                except:
                    pass
        return
class Theorem84(Theorem):
    def __init__(self):
        super(Theorem84, self).__init__(84, "if maxClique == 2.0 then \n{\n    arboricity <= 2.0+maxb(genus)**(1.0/2.0),\n    if minb(arboricity) > 3.0 then \n    {\n        arboricity <= 2.0+maxb(genus)**(1.0/2.0)\n    }\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("genus") != 'undt':
                try:
                    set("arboricity",  2.0+maxb("genus")**(1.0/2.0), ind='Max')
                except:
                    pass
            if (minb("arboricity") != 'undt' and minb("arboricity") > 3.0):
                if maxb("genus") != 'undt':
                    try:
                        set("arboricity",  2.0+maxb("genus")**(1.0/2.0), ind='Max')
                    except:
                        pass
        return
class Theorem85(Theorem):
    def __init__(self):
        super(Theorem85, self).__init__(85, "if maxClique == 2.0 then \n{\n    chromaticNum <= 3.0+2.0*genus**(1.0/2.0)\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("genus") != 'undt':
                try:
                    set("chromaticNum",  3.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("genus",  (minb("chromaticNum")-(3.0))**2.0/4.0, ind='Min')
                except:
                    pass
        return
class Theorem86(Theorem):
    def __init__(self):
        super(Theorem86, self).__init__(86, "\n", "")
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
class Theorem87(Theorem):
    def __init__(self):
        super(Theorem87, self).__init__(87, "if exists genus and genus > 0.0 then \n{\n    mindeg <= 5.0+(1.0+48.0*genus)**(1.0/2.0)/2.0\n};\n", "")
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
        if maxb("genus") != 'undt' and (minb("genus") != 'undt' and minb("genus") > 0.0):
            if maxb("genus") != 'undt':
                try:
                    set("mindeg",  5.0+(1.0+48.0*maxb("genus"))**(1.0/2.0)/2.0, ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("genus",  (minb("mindeg")-(5.0))**2.0/12.0-(1.0/48.0), ind='Min')
                except:
                    pass
        return
class Theorem88(Theorem):
    def __init__(self):
        super(Theorem88, self).__init__(88, "if exists genus and genus > 0.0 and maxClique <= 2.0 then \n{\n    edgeConnec <= 2.0+2.0*genus**(1.0/2.0)\n};\n", "")
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
        if maxb("genus") != 'undt' and (minb("genus") != 'undt' and minb("genus") > 0.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0):
            if maxb("genus") != 'undt':
                try:
                    set("edgeConnec",  2.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
                except:
                    pass
            if minb("edgeConnec") != 'undt':
                try:
                    set("genus",  (minb("edgeConnec")-(2.0))**2.0/4.0, ind='Min')
                except:
                    pass
        return
class Theorem89(Theorem):
    def __init__(self):
        super(Theorem89, self).__init__(89, "if genus == 0.0 and girth == 3.0 then \n{\n    edgeConnec <= 5.0\n}\nelse if genus == 0.0 and (girth == 4.0 or girth == 5.0) then \n{\n    edgeConnec <= 3.0\n}\nelse if genus == 0.0 and girth >= 6.0 then \n{\n    edgeConnec <= 2.0\n};\n", "")
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
        if ((minb("genus") != 'undt' and minb("genus") >= 0.0) and (maxb("genus") != 'undt' and maxb("genus") <= 0.0)) and ((minb("girth") != 'undt' and minb("girth") >= 3.0) and (maxb("girth") != 'undt' and maxb("girth") <= 3.0)):
            try:
                set("edgeConnec",  5.0, ind='Max')
            except:
                pass
        elif ((minb("genus") != 'undt' and minb("genus") >= 0.0) and (maxb("genus") != 'undt' and maxb("genus") <= 0.0)) and (((minb("girth") != 'undt' and minb("girth") >= 4.0) and (maxb("girth") != 'undt' and maxb("girth") <= 4.0)) or ((minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and maxb("girth") <= 5.0))):
            try:
                set("edgeConnec",  3.0, ind='Max')
            except:
                pass
        elif ((minb("genus") != 'undt' and minb("genus") >= 0.0) and (maxb("genus") != 'undt' and maxb("genus") <= 0.0)) and (minb("girth") != 'undt' and minb("girth") >= 6.0):
            try:
                set("edgeConnec",  2.0, ind='Max')
            except:
                pass
        return
class Theorem90(Theorem):
    def __init__(self):
        super(Theorem90, self).__init__(90, "if genus <= 1.0 and girth == 3.0 then \n{\n    edgeConnec <= 6.0\n}\nelse if genus <= 1.0 and girth == 4.0 then \n{\n    edgeConnec <= 4.0\n}\nelse if genus <= 1.0 and (girth == 5.0 or girth == 6.0) then \n{\n    edgeConnec <= 3.0\n}\nelse if genus <= 1.0 and girth >= 7.0 then \n{\n    edgeConnec <= 2.0\n};\n", "")
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
        if (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and ((minb("girth") != 'undt' and minb("girth") >= 3.0) and (maxb("girth") != 'undt' and maxb("girth") <= 3.0)):
            try:
                set("edgeConnec",  6.0, ind='Max')
            except:
                pass
        elif (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and ((minb("girth") != 'undt' and minb("girth") >= 4.0) and (maxb("girth") != 'undt' and maxb("girth") <= 4.0)):
            try:
                set("edgeConnec",  4.0, ind='Max')
            except:
                pass
        elif (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and (((minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and maxb("girth") <= 5.0)) or ((minb("girth") != 'undt' and minb("girth") >= 6.0) and (maxb("girth") != 'undt' and maxb("girth") <= 6.0))):
            try:
                set("edgeConnec",  3.0, ind='Max')
            except:
                pass
        elif (maxb("genus") != 'undt' and maxb("genus") <= 1.0) and (minb("girth") != 'undt' and minb("girth") >= 7.0):
            try:
                set("edgeConnec",  2.0, ind='Max')
            except:
                pass
        return
class Theorem91(Theorem):
    def __init__(self):
        super(Theorem91, self).__init__(91, "let s = floor((girth-(1.0))/4.0);\n_s is (minb(girth)-(1.0))/4.0;\nif mindeg >= 3.0 and _s >= 1.0 then \n{\n    nodes >= girth*(mindeg-(1.0))**s\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt':
            _s = (minb("girth")-(1.0))/4.0
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 3.0) and _s >= 1.0:
            if minb("girth") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  minb("girth")*(minb("mindeg")-(1.0))**floor((minb("girth")-(1.0))/4.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("girth",  maxb("nodes")*(maxb("mindeg")-(1.0))**(-(floor((minb("girth")-(1.0))/4.0))), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("mindeg",  (maxb("nodes")/"girth")**(1.0/floor(("girth"-(1.0))/4.0))+1.0, ind='Max')
                except:
                    pass
        return
class Theorem92(Theorem):
    def __init__(self):
        super(Theorem92, self).__init__(92, "if nodeConnec >= 2.0 then \n{\n    circumference >= minimum(nodes, 2.0*mindeg)\n};\n", "")
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
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("circumference",  minimum(minb("nodes"), 2.0*minb("mindeg")), ind='Min')
                except:
                    pass
        return
class Theorem93(Theorem):
    def __init__(self):
        super(Theorem93, self).__init__(93, "if isset diameter and diameter == 2.0 and ((even nodes and even mindeg and nodes >= mindeg**3.0+mindeg+1.0) or ((odd nodes or odd mindeg) and nodes > mindeg**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(mindeg+1.0)+1.0)/2.0\n};\n", "")
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
        if maxb("diameter") != 'undt' and minb("diameter") == maxb("diameter") and ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((evenInvar("nodes") and evenInvar("mindeg") and (minb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodes") >= maxb("mindeg")**3.0+maxb("mindeg")+1.0)) or ((oddInvar("nodes") or oddInvar("mindeg")) and (minb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodes") > maxb("mindeg")**3.0+1.0))):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("edges",  ((minb("nodes")-(1.0))*(minb("mindeg")+1.0)+1.0)/2.0, ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("nodes",  (2.0*maxb("edges")+maxb("mindeg"))/(maxb("mindeg")+1.0), ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
                except:
                    pass
        return
class Theorem94(Theorem):
    def __init__(self):
        super(Theorem94, self).__init__(94, "if isset diameter and diameter == 2.0 and (nodeConnec > 2.0 or nodeConnec < 2.0) and ((even nodes and even nodeConnec and nodes >= nodeConnec**3.0+nodeConnec+1.0) or ((odd nodes or odd nodeConnec) and nodes > nodeConnec**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(nodeConnec+1.0)+1.0)/2.0\n};\n", "")
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
        if maxb("diameter") != 'undt' and minb("diameter") == maxb("diameter") and ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") > 2.0) or (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") < 2.0)) and ((evenInvar("nodes") and evenInvar("nodeConnec") and (minb("nodes") != 'undt' and maxb("nodeConnec") != 'undt' and minb("nodes") >= maxb("nodeConnec")**3.0+maxb("nodeConnec")+1.0)) or ((oddInvar("nodes") or oddInvar("nodeConnec")) and (minb("nodes") != 'undt' and maxb("nodeConnec") != 'undt' and minb("nodes") > maxb("nodeConnec")**3.0+1.0))):
            if minb("nodes") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("edges",  ((minb("nodes")-(1.0))*(minb("nodeConnec")+1.0)+1.0)/2.0, ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("nodes",  (2.0*maxb("edges")+maxb("nodeConnec"))/(maxb("nodeConnec")+1.0), ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeConnec",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
                except:
                    pass
        return
class Theorem95(Theorem):
    def __init__(self):
        super(Theorem95, self).__init__(95, "if diameter == 2.0 and ((even nodes and even edgeConnec and nodes >= edgeConnec**3.0+edgeConnec+1.0) or ((odd nodes or odd edgeConnec) and nodes > edgeConnec**3.0+1.0)) then \n{\n    edges >= ((nodes-(1.0))*(edgeConnec+1.0)+1.0)/2.0\n};\n", "")
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
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((evenInvar("nodes") and evenInvar("edgeConnec") and (minb("nodes") != 'undt' and maxb("edgeConnec") != 'undt' and minb("nodes") >= maxb("edgeConnec")**3.0+maxb("edgeConnec")+1.0)) or ((oddInvar("nodes") or oddInvar("edgeConnec")) and (minb("nodes") != 'undt' and maxb("edgeConnec") != 'undt' and minb("nodes") > maxb("edgeConnec")**3.0+1.0))):
            if minb("nodes") != 'undt' and minb("edgeConnec") != 'undt':
                try:
                    set("edges",  ((minb("nodes")-(1.0))*(minb("edgeConnec")+1.0)+1.0)/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeConnec") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodes",  (maxb("edgeConnec")+2.0*maxb("edges"))/(maxb("edgeConnec")+1.0), ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("edgeConnec",  (2.0*maxb("edges")-(minb("nodes")))/(minb("nodes")-(1.0)), ind='Max')
                except:
                    pass
        return
class Theorem96(Theorem):
    def __init__(self):
        super(Theorem96, self).__init__(96, "if exists girth and arboricity > 2.0 then \n{\n    nosolve nodes >= (girth-(1.0))*(arboricity-(1.0))+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","arboricity","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("girth") != 'undt' and (minb("arboricity") != 'undt' and minb("arboricity") > 2.0):
            if minb("girth") != 'undt' and minb("arboricity") != 'undt':
                try:
                    set("nodes",  (minb("girth")-(1.0))*(minb("arboricity")-(1.0))+1.0, ind='Min')
                except:
                    pass
        return
class Theorem97(Theorem):
    def __init__(self):
        super(Theorem97, self).__init__(97, "if maxClique == 2.0 and chromaticNum >= 4.0 then \n{\n    nodes >= 11.0\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 4.0):
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        return
class Theorem98(Theorem):
    def __init__(self):
        super(Theorem98, self).__init__(98, "let t = (girth/girth-(2.0));\nif exists genus and girth >= 4.0 and genus >= 2.0 and chromaticNum >= 1.0+2.0*t then \n{\n    nosolve chromaticNum <= (3.0+6.0*t+sqrt(57.0-(60.0*t)+36.0*t*t+48.0*t*genus))/6.0:useMinFor(girth):useMaxFor(genus)\n};\n", "")
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
        if maxb("genus") != 'undt' and (minb("girth") != 'undt' and minb("girth") >= 4.0) and (minb("genus") != 'undt' and minb("genus") >= 2.0) and (minb("chromaticNum") != 'undt' and maxb("girth") != 'undt' and minb("chromaticNum") >= 1.0+2.0*(maxb("girth")/maxb("girth")-(2.0))):
            if maxb("girth") != 'undt' and maxb("genus") != 'undt':
                try:
                    set("chromaticNum",  (3.0+6.0*(minb("girth")/minb("girth")-(2.0))+sqrt(57.0-(60.0*(minb("girth")/minb("girth")-(2.0)))+36.0*(minb("girth")/minb("girth")-(2.0))*(minb("girth")/minb("girth")-(2.0))+48.0*(minb("girth")/minb("girth")-(2.0))*maxb("genus")))/6.0, ind='Max')
                except:
                    pass
        return
class Theorem99(Theorem):
    def __init__(self):
        super(Theorem99, self).__init__(99, "if diameter <= 2.0 then \n{\n    edgeConnec == mindeg\n};\n", "")
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
        if (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0):
            if minb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  minb("mindeg"), ind='Min')
                except:
                    pass
            if maxb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  maxb("edgeConnec"), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  maxb("mindeg"), ind='Max')
                except:
                    pass
            if minb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  minb("edgeConnec"), ind='Min')
                except:
                    pass
        return
class Theorem100(Theorem):
    def __init__(self):
        super(Theorem100, self).__init__(100, "if nodeInd >= edgeInd then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n};\n", "")
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
        if (minb("nodeInd") != 'undt' and maxb("edgeInd") != 'undt' and minb("nodeInd") >= maxb("edgeInd")):
            if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("edgeCliqueCover",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("nodeCover",  minb("edgeCliqueCover")/maxb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodeInd",  minb("edgeCliqueCover")/maxb("nodeCover"), ind='Min')
                except:
                    pass
        return
class Theorem101(Theorem):
    def __init__(self):
        super(Theorem101, self).__init__(101, "if connected or odd nodes then \n{\n    nodeCover <= (nodes-(1.0))*(nodes+1.0)/2.0,\n    edgeCover <= (nodes-(1.0))*(nodes+1.0)/2.0\n}\nelse  \n{\n    nodeCover <= (nodes-(2.0))*(nodes+2.0)/2.0,\n    edgeCover <= (nodes-(2.0))*(nodes+2.0)/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodes","nodeCover","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True or oddInvar("nodes"):
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (maxb("nodes")-(1.0))*(maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*minb("nodeCover")+1.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")-(1.0))*(maxb("nodes")+1.0)/2.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*minb("edgeCover")+1.0), ind='Min')
                except:
                    pass
        elif True:
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (maxb("nodes")-(2.0))*(maxb("nodes")+2.0)/2.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*minb("nodeCover")+4.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")-(2.0))*(maxb("nodes")+2.0)/2.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*minb("edgeCover")+4.0), ind='Min')
                except:
                    pass
        return
class Theorem102(Theorem):
    def __init__(self):
        super(Theorem102, self).__init__(102, "edgeChromatic <= 2.0*bandwidth;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("bandwidth") != 'undt':
            try:
                set("edgeChromatic",  2.0*maxb("bandwidth"), ind='Max')
            except:
                pass
        if minb("edgeChromatic") != 'undt':
            try:
                set("bandwidth",  minb("edgeChromatic")/2.0, ind='Min')
            except:
                pass
        return
class Theorem103(Theorem):
    def __init__(self):
        super(Theorem103, self).__init__(103, "circumference >= maxb(maxClique)*minb(mindeg)/(maxb(maxClique)-(1.0));\nmaxClique >= maxb(circumference)/(maxb(circumference)-(minb(mindeg)));\nmindeg <= maxb(circumference)-(maxb(circumference)/maxb(maxClique));\n", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("maxClique") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("circumference",  maxb("maxClique")*minb("mindeg")/(maxb("maxClique")-(1.0)), ind='Min')
            except:
                pass
        if minb("circumference") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("maxClique",  maxb("circumference")/(maxb("circumference")-(minb("mindeg"))), ind='Min')
            except:
                pass
        if maxb("circumference") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("mindeg",  maxb("circumference")-(maxb("circumference")/maxb("maxClique")), ind='Max')
            except:
                pass
        return
class Theorem104(Theorem):
    def __init__(self):
        super(Theorem104, self).__init__(104, "circumference >= maxb(maxClique)*(minb(chromaticNum)-(1.0))/(maxb(maxClique)-(1.0));\nmaxClique >= maxb(circumference)/(-(minb(chromaticNum))+maxb(circumference)+1.0);\nchromaticNum <= maxb(circumference)-(maxb(circumference)/maxb(maxClique))+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","maxClique","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("maxClique") != 'undt' and minb("chromaticNum") != 'undt':
            try:
                set("circumference",  maxb("maxClique")*(minb("chromaticNum")-(1.0))/(maxb("maxClique")-(1.0)), ind='Min')
            except:
                pass
        if minb("circumference") != 'undt' and minb("chromaticNum") != 'undt':
            try:
                set("maxClique",  maxb("circumference")/(-(minb("chromaticNum"))+maxb("circumference")+1.0), ind='Min')
            except:
                pass
        if maxb("circumference") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("chromaticNum",  maxb("circumference")-(maxb("circumference")/maxb("maxClique"))+1.0, ind='Max')
            except:
                pass
        return
class Theorem105(Theorem):
    def __init__(self):
        super(Theorem105, self).__init__(105, "if maxClique == 2.0 and maxb(chromaticNum) >= 3.0 then \n{\n    circumference >= 2.0*chromaticNum-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") >= 3.0):
            if minb("chromaticNum") != 'undt':
                try:
                    set("circumference",  2.0*minb("chromaticNum")-(1.0), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("chromaticNum",  maxb("circumference")/2.0+1.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem106(Theorem):
    def __init__(self):
        super(Theorem106, self).__init__(106, "if exists nodeCover and exists chromaticNum and exists nodeInd then \n{\n    edges <= maxb(nodeCover)*(maxb(nodeInd)+maxb(nodeCover)*(maxb(chromaticNum)-(1.0))/(2.0*maxb(chromaticNum))),\n    nodeCover >= -((maxb(chromaticNum)*maxb(nodeInd)+sqrt(maxb(chromaticNum)*(2.0*maxb(chromaticNum)*maxb(edges)+maxb(chromaticNum)*maxb(nodeInd)**2.0-(2.0*maxb(edges)))))/(maxb(chromaticNum)-(1.0))),\n    nodeInd >= minb(edges)/maxb(nodeCover)-(maxb(nodeCover)/2.0)+maxb(nodeCover)/(2.0*maxb(chromaticNum)),\n    chromaticNum >= maxb(nodeCover)**2.0/(-(2.0*minb(edges))+maxb(nodeCover)**2.0+2.0*maxb(nodeCover)*maxb(nodeInd))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","chromaticNum","nodeInd","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt' and maxb("chromaticNum") != 'undt' and maxb("nodeInd") != 'undt':
            if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt' and maxb("chromaticNum") != 'undt':
                try:
                    set("edges",  maxb("nodeCover")*(maxb("nodeInd")+maxb("nodeCover")*(maxb("chromaticNum")-(1.0))/(2.0*maxb("chromaticNum"))), ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt' and minb("nodeInd") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodeCover",  -((maxb("chromaticNum")*maxb("nodeInd")+sqrt(maxb("chromaticNum")*(2.0*maxb("chromaticNum")*maxb("edges")+maxb("chromaticNum")*maxb("nodeInd")**2.0-(2.0*maxb("edges")))))/(maxb("chromaticNum")-(1.0))), ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodeCover") != 'undt' and minb("chromaticNum") != 'undt':
                try:
                    set("nodeInd",  minb("edges")/maxb("nodeCover")-(maxb("nodeCover")/2.0)+maxb("nodeCover")/(2.0*maxb("chromaticNum")), ind='Min')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("edges") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("chromaticNum",  maxb("nodeCover")**2.0/(-(2.0*minb("edges"))+maxb("nodeCover")**2.0+2.0*maxb("nodeCover")*maxb("nodeInd")), ind='Min')
                except:
                    pass
        return
class Theorem107(Theorem):
    def __init__(self):
        super(Theorem107, self).__init__(107, "mindeg <= maxdeg;\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("maxdeg") != 'undt':
            try:
                set("mindeg",  maxb("maxdeg"), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt':
            try:
                set("maxdeg",  minb("mindeg"), ind='Min')
            except:
                pass
        return
class Theorem108(Theorem):
    def __init__(self):
        super(Theorem108, self).__init__(108, "nodeCliqueCover <= (nodes+nodeInd-(maxClique)+1.0)/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","nodes","nodeInd","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("nodeInd") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("nodeCliqueCover",  (maxb("nodes")+maxb("nodeInd")-(minb("maxClique"))+1.0)/2.0, ind='Max')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("nodeCliqueCover") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("nodes",  minb("maxClique")+2.0*minb("nodeCliqueCover")-(maxb("nodeInd"))-(1.0), ind='Min')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("nodeCliqueCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeInd",  minb("maxClique")+2.0*minb("nodeCliqueCover")-(maxb("nodes"))-(1.0), ind='Min')
            except:
                pass
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxClique",  -(2.0*minb("nodeCliqueCover"))+maxb("nodeInd")+maxb("nodes")+1.0, ind='Max')
            except:
                pass
        return
class Theorem109(Theorem):
    def __init__(self):
        super(Theorem109, self).__init__(109, "nodeCover <= 2.0*edgeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeInd") != 'undt':
            try:
                set("nodeCover",  2.0*maxb("edgeInd"), ind='Max')
            except:
                pass
        if minb("nodeCover") != 'undt':
            try:
                set("edgeInd",  minb("nodeCover")/2.0, ind='Min')
            except:
                pass
        return
class Theorem110(Theorem):
    def __init__(self):
        super(Theorem110, self).__init__(110, "if minb(mindeg) >= 4.0 and minb(girth) >= 5.0 then \n{\n    circumference >= (minb(girth)-(2.0))*(minb(mindeg)-(2.0))+5.0,\n    girth <= (maxb(circumference)+2.0*minb(mindeg)-(9.0))/(minb(mindeg)-(2.0)),\n    mindeg <= (maxb(circumference)+2.0*minb(girth)-(9.0))/(minb(girth)-(2.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 4.0) and (minb("girth") != 'undt' and minb("girth") >= 5.0):
            if minb("girth") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("circumference",  (minb("girth")-(2.0))*(minb("mindeg")-(2.0))+5.0, ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("girth",  (maxb("circumference")+2.0*minb("mindeg")-(9.0))/(minb("mindeg")-(2.0)), ind='Max')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("mindeg",  (maxb("circumference")+2.0*minb("girth")-(9.0))/(minb("girth")-(2.0)), ind='Max')
                except:
                    pass
        return
class Theorem111(Theorem):
    def __init__(self):
        super(Theorem111, self).__init__(111, "if connected then \n{\n    diameter <= 2.0*nodeInd-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if maxb("nodeInd") != 'undt':
                try:
                    set("diameter",  2.0*maxb("nodeInd")-(1.0), ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt':
                try:
                    set("nodeInd",  minb("diameter")/2.0+1.0/2.0, ind='Min')
                except:
                    pass
        return
class Theorem112(Theorem):
    def __init__(self):
        super(Theorem112, self).__init__(112, "if connected and nodeInd <= mindeg and mindeg >= (nodes+2.0)/3.0 then \n{\n    hamiltonian\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodeInd","mindeg","nodes","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (maxb("nodeInd") != 'undt' and minb("mindeg") != 'undt' and maxb("nodeInd") <= minb("mindeg")) and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= (maxb("nodes")+2.0)/3.0):
            set("hamiltonian", True)
        return
class Theorem113(Theorem):
    def __init__(self):
        super(Theorem113, self).__init__(113, "edges >= nodeInd*mindeg+(maxClique-(1.0))*(maxClique-(2.0))/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeInd","mindeg","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodeInd") != 'undt' and minb("mindeg") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("edges",  minb("nodeInd")*minb("mindeg")+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/2.0, ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("maxClique") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodeInd",  (2.0*maxb("edges")-(minb("maxClique")**2.0)+3.0*minb("maxClique")-(2.0))/(2.0*minb("mindeg")), ind='Max')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("maxClique") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("mindeg",  (2.0*maxb("edges")-(minb("maxClique")**2.0)+3.0*minb("maxClique")-(2.0))/(2.0*minb("nodeInd")), ind='Max')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("maxClique",  sqrt(8.0*maxb("edges")-(8.0*minb("mindeg")*minb("nodeInd"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        return
class Theorem114(Theorem):
    def __init__(self):
        super(Theorem114, self).__init__(114, "edges >= nodeCover+(maxClique-(1.0))*(maxClique-(2.0))/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodeCover") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("edges",  minb("nodeCover")+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/2.0, ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("nodeCover",  maxb("edges")-(minb("maxClique")**2.0/2.0)+3.0*minb("maxClique")/2.0-(1.0), ind='Max')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("nodeCover") != 'undt':
            try:
                set("maxClique",  sqrt(8.0*maxb("edges")-(8.0*minb("nodeCover"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        return
class Theorem115(Theorem):
    def __init__(self):
        super(Theorem115, self).__init__(115, "edges >= chromaticNum*(chromaticNum-(3.0))/2.0+nodes-(numOfComponents)+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","chromaticNum","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("chromaticNum") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
            try:
                set("edges",  minb("chromaticNum")*(minb("chromaticNum")-(3.0))/2.0+minb("nodes")-(maxb("numOfComponents"))+1.0, ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
            try:
                set("chromaticNum",  sqrt(8.0*maxb("edges")-(8.0*minb("nodes"))+8.0*maxb("numOfComponents")+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        if maxb("chromaticNum") != 'undt' and maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt':
            try:
                set("nodes",  -(minb("chromaticNum")**2.0/2.0)+3.0*minb("chromaticNum")/2.0+maxb("edges")+maxb("numOfComponents")-(1.0), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt' and minb("edges") != 'undt' and minb("nodes") != 'undt':
            try:
                set("numOfComponents",  minb("chromaticNum")**2.0/2.0-(3.0*minb("chromaticNum")/2.0)-(maxb("edges"))+minb("nodes")+1.0, ind='Min')
            except:
                pass
        return
class Theorem116(Theorem):
    def __init__(self):
        super(Theorem116, self).__init__(116, "if bipartite and even nodes then \n{\n    genus <= ((nodes-(4.0))**2.0+15.0)/16.0\n};\nif bipartite and odd nodes then \n{\n    genus <= ((nodes-(3.0))*(nodes-(5.0))+15.0)/16.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("bipartite") == True and evenInvar("nodes"):
            if maxb("nodes") != 'undt':
                try:
                    set("genus",  ((maxb("nodes")-(4.0))**2.0+15.0)/16.0, ind='Max')
                except:
                    pass
            if minb("genus") != 'undt':
                try:
                    set("nodes",  sqrt(16.0*minb("genus")-(15.0))+4.0, ind='Min')
                except:
                    pass
        if get("bipartite") == True and oddInvar("nodes"):
            if maxb("nodes") != 'undt':
                try:
                    set("genus",  ((maxb("nodes")-(3.0))*(maxb("nodes")-(5.0))+15.0)/16.0, ind='Max')
                except:
                    pass
            if minb("genus") != 'undt':
                try:
                    set("nodes",  sqrt(16.0*minb("genus")-(14.0))+4.0, ind='Min')
                except:
                    pass
        return
class Theorem117(Theorem):
    def __init__(self):
        super(Theorem117, self).__init__(117, "if not complete then \n{\n    nodeConnec >= 2.0*mindeg-(nodes)+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["complete","nodeConnec","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("complete") == False:
            if minb("mindeg") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeConnec",  2.0*minb("mindeg")-(maxb("nodes"))+2.0, ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  maxb("nodeConnec")/2.0+maxb("nodes")/2.0-(1.0), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("nodes",  2.0*minb("mindeg")-(maxb("nodeConnec"))+2.0, ind='Min')
                except:
                    pass
        return
class Theorem118(Theorem):
    def __init__(self):
        super(Theorem118, self).__init__(118, "if (nodes >= 6.0 and even nodes and edges >= (nodes**2.0)/4.0+1.0) or (nodes >= 7.0 and odd nodes and edges >= (nodes-(1.0))**2.0/4.0+1.0+mindeg) then \n{\n    circumference >= 5.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","mindeg","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("nodes") != 'undt' and minb("nodes") >= 6.0) and evenInvar("nodes") and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= (maxb("nodes")**2.0)/4.0+1.0)) or ((minb("nodes") != 'undt' and minb("nodes") >= 7.0) and oddInvar("nodes") and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("edges") >= (maxb("nodes")-(1.0))**2.0/4.0+1.0+maxb("mindeg"))):
            try:
                set("circumference",  5.0, ind='Min')
            except:
                pass
        return
class Theorem119(Theorem):
    def __init__(self):
        super(Theorem119, self).__init__(119, "if chromaticNum >= maxClique then \n{\n    mindeg <= (3.0*maxClique-(4.0))*nodes/(3.0*maxClique-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("chromaticNum") != 'undt' and maxb("maxClique") != 'undt' and minb("chromaticNum") >= maxb("maxClique")):
            if maxb("maxClique") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  (3.0*maxb("maxClique")-(4.0))*maxb("nodes")/(3.0*maxb("maxClique")-(1.0)), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxClique",  (maxb("mindeg")-(4.0*maxb("nodes")))/(3.0*(maxb("mindeg")-(maxb("nodes")))), ind='Min')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("maxClique") != 'undt':
                try:
                    set("nodes",  minb("mindeg")*(3.0*minb("maxClique")-(1.0))/(3.0*minb("maxClique")-(4.0)), ind='Min')
                except:
                    pass
        return
class Theorem120(Theorem):
    def __init__(self):
        super(Theorem120, self).__init__(120, "if hamiltonian and nodes > chromaticNum and chromaticNum >= 4.0 then \n{\n    edges >= (chromaticNum-(1.0))*(chromaticNum-(2.0))/2.0+nodes\n}\nelse if hamiltonian and chromaticNum == 3.0 and even nodes then \n{\n    edges >= nodes+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodes","chromaticNum","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("hamiltonian") == True and (minb("nodes") != 'undt' and maxb("chromaticNum") != 'undt' and minb("nodes") > maxb("chromaticNum")) and (minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 4.0):
            if minb("chromaticNum") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  (minb("chromaticNum")-(1.0))*(minb("chromaticNum")-(2.0))/2.0+minb("nodes"), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("chromaticNum",  sqrt(8.0*maxb("edges")-(8.0*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
                except:
                    pass
            if maxb("chromaticNum") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodes",  -(minb("chromaticNum")**2.0/2.0)+3.0*minb("chromaticNum")/2.0+maxb("edges")-(1.0), ind='Max')
                except:
                    pass
        elif get("hamiltonian") == True and ((minb("chromaticNum") != 'undt' and minb("chromaticNum") >= 3.0) and (maxb("chromaticNum") != 'undt' and maxb("chromaticNum") <= 3.0)) and evenInvar("nodes"):
            if minb("nodes") != 'undt':
                try:
                    set("edges",  minb("nodes")+1.0, ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt':
                try:
                    set("nodes",  maxb("edges")-(1.0), ind='Max')
                except:
                    pass
        return
class Theorem121(Theorem):
    def __init__(self):
        super(Theorem121, self).__init__(121, "if exists diameter then \n{\n    _nodeConnec is minb(nodeConnec),\n    if minb(diameter) < 3.0 then \n    {\n        _nodeConnec is maxb(nodeConnec)\n    },\n    chromaticNum <= maxb(nodes)-(_nodeConnec*(minb(diameter)-(3.0)))-(2.0),\n    nodes >= minb(chromaticNum)+minb(diameter)*_nodeConnec-(3.0*_nodeConnec)+2.0,\n    if minb(diameter) > 3.0 then \n    {\n        nodeConnec <= (-(minb(chromaticNum))+maxb(nodes)-(2.0))/(minb(diameter)-(3.0))\n    }\n    else if maxb(diameter) < 3.0 then \n    {\n        nodeConnec >= (minb(chromaticNum)-(maxb(nodes))+1.0)/(3.0-(minb(diameter)))+1.0\n    },\n    if minb(nodeConnec) > 0.0 then \n    {\n        diameter <= (-(minb(chromaticNum))+3.0*maxb(nodeConnec)+maxb(nodes)-(2.0))/maxb(nodeConnec)\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","chromaticNum","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("diameter") != 'undt':
            if minb("nodeConnec") != 'undt':
                _nodeConnec = minb("nodeConnec")
            if (minb("diameter") != 'undt' and minb("diameter") < 3.0):
                if maxb("nodeConnec") != 'undt':
                    _nodeConnec = maxb("nodeConnec")
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("chromaticNum",  maxb("nodes")-(_nodeConnec*(minb("diameter")-(3.0)))-(2.0), ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodes",  minb("chromaticNum")+minb("diameter")*_nodeConnec-(3.0*_nodeConnec)+2.0, ind='Min')
                except:
                    pass
            if (minb("diameter") != 'undt' and minb("diameter") > 3.0):
                if maxb("chromaticNum") != 'undt' and maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("nodeConnec",  (-(minb("chromaticNum"))+maxb("nodes")-(2.0))/(minb("diameter")-(3.0)), ind='Max')
                    except:
                        pass
            elif (maxb("diameter") != 'undt' and maxb("diameter") < 3.0):
                if minb("chromaticNum") != 'undt' and minb("nodes") != 'undt' and minb("diameter") != 'undt':
                    try:
                        set("nodeConnec",  (minb("chromaticNum")-(maxb("nodes"))+1.0)/(3.0-(minb("diameter")))+1.0, ind='Min')
                    except:
                        pass
            if (minb("nodeConnec") != 'undt' and minb("nodeConnec") > 0.0):
                if maxb("chromaticNum") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  (-(minb("chromaticNum"))+3.0*maxb("nodeConnec")+maxb("nodes")-(2.0))/maxb("nodeConnec"), ind='Max')
                    except:
                        pass
        return
class Theorem122(Theorem):
    def __init__(self):
        super(Theorem122, self).__init__(122, "if edges > nodes**2.0/4.0 then \n{\n    nosolve edgeCliqueCover <= ((1.0/2.0)*nodes*(nodes-(1.0))-(edges))+(1.0+sqrt(1.0+4.0*((1.0/2.0)*nodes*(nodes-(1.0))-(edges))))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","edgeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") > maxb("nodes")**2.0/4.0):
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("edgeCliqueCover",  ((1.0/2.0)*maxb("nodes")*(maxb("nodes")-(1.0))-(minb("edges")))+(1.0+sqrt(1.0+4.0*((1.0/2.0)*maxb("nodes")*(maxb("nodes")-(1.0))-(minb("edges"))))), ind='Max')
                except:
                    pass
        return
class Theorem123(Theorem):
    def __init__(self):
        super(Theorem123, self).__init__(123, "if nodes <= 2.0*edges then \n{\n    mindeg == edgeConnec\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","mindeg","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodes") != 'undt' and minb("edges") != 'undt' and maxb("nodes") <= 2.0*minb("edges")):
            if minb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  minb("edgeConnec"), ind='Min')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("edgeConnec") != 'undt':
                try:
                    set("mindeg",  maxb("edgeConnec"), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("edgeConnec",  minb("mindeg"), ind='Min')
                except:
                    pass
        return
class Theorem124(Theorem):
    def __init__(self):
        super(Theorem124, self).__init__(124, "if connected then \n{\n    bandwidth >= (nodes-(1.0))/diameter\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","bandwidth","nodes","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if minb("nodes") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("bandwidth",  (minb("nodes")-(1.0))/maxb("diameter"), ind='Min')
                except:
                    pass
            if maxb("bandwidth") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("nodes",  maxb("bandwidth")*maxb("diameter")+1.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("bandwidth") != 'undt':
                try:
                    set("diameter",  (minb("nodes")-(1.0))/maxb("bandwidth"), ind='Min')
                except:
                    pass
        return
class Theorem125(Theorem):
    def __init__(self):
        super(Theorem125, self).__init__(125, "if genus >= 1.0 and istrue congruent(girth, 3.0, 4.0) then \n{\n    nodes >= 9.0*(girth-(1.0))/4.0+1.0\n}\nelse if genus >= 1.0 then \n{\n    nodes >= 9.0*(girth-(1.0))/4.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt' and minb("genus") >= 1.0) and congruent("girth", 3.0, 4.0):
            if minb("girth") != 'undt':
                try:
                    set("nodes",  9.0*(minb("girth")-(1.0))/4.0+1.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("girth",  4.0*maxb("nodes")/9.0+5.0/9.0, ind='Max')
                except:
                    pass
        elif (minb("genus") != 'undt' and minb("genus") >= 1.0):
            if minb("girth") != 'undt':
                try:
                    set("nodes",  9.0*(minb("girth")-(1.0))/4.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("girth",  4.0*maxb("nodes")/9.0+1.0, ind='Max')
                except:
                    pass
        return
class Theorem126(Theorem):
    def __init__(self):
        super(Theorem126, self).__init__(126, "if nodes <= mindeg*2.0 then \n{\n    nodes <= 2.0*edgeConnec+3.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodes") <= minb("mindeg")*2.0):
            if maxb("edgeConnec") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeConnec")+3.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("edgeConnec",  minb("nodes")/2.0-(3.0/2.0), ind='Min')
                except:
                    pass
        return
class Theorem127(Theorem):
    def __init__(self):
        super(Theorem127, self).__init__(127, "if hamiltonian and even nodes and maxdeg == 3.0 then \n{\n    edgeChromatic == maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodes","maxdeg","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("hamiltonian") == True and evenInvar("nodes") and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)):
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
class Theorem128(Theorem):
    def __init__(self):
        super(Theorem128, self).__init__(128, "\n", "")
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
class Theorem129(Theorem):
    def __init__(self):
        super(Theorem129, self).__init__(129, "if defined diameter and diameter > 3.0 then \n{\n    mindeg <= (nodes-(minb(diameter))+3.0*(minb(diameter)/3.0+1.0)-(3.0))/(minb(diameter)/3.0+1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("diameter") != 'undt' and (minb("diameter") != 'undt' and minb("diameter") > 3.0):
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("mindeg",  (maxb("nodes")-(minb("diameter"))+3.0*(minb("diameter")/3.0+1.0)-(3.0))/(minb("diameter")/3.0+1.0), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodes",  minb("mindeg")*(minb("diameter")+3.0)/3.0, ind='Min')
                except:
                    pass
        return
class Theorem130(Theorem):
    def __init__(self):
        super(Theorem130, self).__init__(130, "if diameter == 2.0 and nodes >= maxdeg*maxdeg/8.0 then \n{\n    edges >= nodes*(nodes-(1.0))/(2.0*maxdeg)\n}\nelse if diameter == 2.0 and nodes < maxdeg*maxdeg/8.0 then \n{\n    nosolve edges >= maxdeg*nodes*(nodes-(1.0))/(maxdeg*maxdeg+8.0*nodes)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodes","maxdeg","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and (minb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and minb("nodes") >= maxb("maxdeg")*maxb("maxdeg")/8.0):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edges",  minb("nodes")*(minb("nodes")-(1.0))/(2.0*maxb("maxdeg")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  sqrt(8.0*maxb("edges")*maxb("maxdeg")+1.0)/2.0+1.0/2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("edges") != 'undt':
                try:
                    set("maxdeg",  minb("nodes")*(minb("nodes")-(1.0))/(2.0*maxb("edges")), ind='Min')
                except:
                    pass
        elif ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and (maxb("nodes") != 'undt' and minb("maxdeg") != 'undt' and maxb("nodes") < minb("maxdeg")*minb("maxdeg")/8.0):
            if minb("maxdeg") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  maxb("maxdeg")*minb("nodes")*(minb("nodes")-(1.0))/(maxb("maxdeg")*maxb("maxdeg")+8.0*minb("nodes")), ind='Min')
                except:
                    pass
        return
class Theorem131(Theorem):
    def __init__(self):
        super(Theorem131, self).__init__(131, "_k is maximum(4.0, maxb(maxClique)+1.0);\n_z is (maxb(maxdeg)+1.0)/_k;\nchromaticNum <= maxb(maxdeg)+1.0-(_z);\nmaxdeg >= (_k*minb(chromaticNum)-(1.0))/(_k-(1.0))-(1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("maxClique") != 'undt':
            _k = maximum(4.0, maxb("maxClique")+1.0)
        if maxb("maxdeg") != 'undt':
            _z = (maxb("maxdeg")+1.0)/_k
        if maxb("maxdeg") != 'undt':
            try:
                set("chromaticNum",  maxb("maxdeg")+1.0-(_z), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("maxdeg",  (_k*minb("chromaticNum")-(1.0))/(_k-(1.0))-(1.0), ind='Min')
            except:
                pass
        return
class Theorem132(Theorem):
    def __init__(self):
        super(Theorem132, self).__init__(132, "_P is maxb(nodes);\nif isset nodes then \n{\n    if istrue congruent(nodes, 3.0, 4.0) then \n    {\n        mindeg <= (_P-(3.0))*(_P+1.0)/(4.0*(_P-(1.0)-(maxdeg)))\n    }\n    else  \n    {\n        mindeg <= (_P-(1.0))**2.0/(4.0*(_P-(1.0)-(maxdeg)))\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt':
            _P = maxb("nodes")
        if maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes"):
            if congruent("nodes", 3.0, 4.0):
                if maxb("maxdeg") != 'undt':
                    try:
                        set("mindeg",  (_P-(3.0))*(_P+1.0)/(4.0*(_P-(1.0)-(maxb("maxdeg")))), ind='Max')
                    except:
                        pass
                if minb("mindeg") != 'undt':
                    try:
                        set("maxdeg",  (-(_P**2.0)+2.0*_P+4.0*minb("mindeg")*(_P-(1.0))+3.0)/(4.0*minb("mindeg")), ind='Min')
                    except:
                        pass
            elif True:
                if maxb("maxdeg") != 'undt':
                    try:
                        set("mindeg",  (_P-(1.0))**2.0/(4.0*(_P-(1.0)-(maxb("maxdeg")))), ind='Max')
                    except:
                        pass
                if minb("mindeg") != 'undt':
                    try:
                        set("maxdeg",  (_P-(1.0))*(-(_P)+4.0*minb("mindeg")+1.0)/(4.0*minb("mindeg")), ind='Min')
                    except:
                        pass
        return
class Theorem133(Theorem):
    def __init__(self):
        super(Theorem133, self).__init__(133, "let z = 1.0+floor(2.0*edges/nodes);\nlet k = ceil(nodes-(2.0*edges/z));\nif isset edges and isset nodes then \n{\n    nodeInd >= k+ceil((nodes-(k*z))/(1.0+z)):useMinFor(edges):useMaxFor(nodes)\n};\n", "")
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
        if maxb("edges") != 'undt' and minb("edges") == maxb("edges") and maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes"):
            if minb("nodes") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodeInd",  ceil(maxb("nodes")-(2.0*minb("edges")/1.0+floor(2.0*minb("edges")/maxb("nodes"))))+ceil((maxb("nodes")-(ceil(maxb("nodes")-(2.0*minb("edges")/1.0+floor(2.0*minb("edges")/maxb("nodes"))))*1.0+floor(2.0*minb("edges")/maxb("nodes"))))/(1.0+1.0+floor(2.0*minb("edges")/maxb("nodes")))), ind='Min')
                except:
                    pass
        return
class Theorem134(Theorem):
    def __init__(self):
        super(Theorem134, self).__init__(134, "if radius == 2.0 and diameter == 2.0 and nodes == 4.0 then \n{\n    edges >= 4.0\n}\nelse if radius == 2.0 and diameter == 2.0 and nodes >= 5.0 then \n{\n    edges >= 2.0*nodes-(5.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diameter","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("radius") != 'undt' and minb("radius") >= 2.0) and (maxb("radius") != 'undt' and maxb("radius") <= 2.0)) and ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("nodes") != 'undt' and minb("nodes") >= 4.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 4.0)):
            try:
                set("edges",  4.0, ind='Min')
            except:
                pass
        elif ((minb("radius") != 'undt' and minb("radius") >= 2.0) and (maxb("radius") != 'undt' and maxb("radius") <= 2.0)) and ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and (minb("nodes") != 'undt' and minb("nodes") >= 5.0):
            if minb("nodes") != 'undt':
                try:
                    set("edges",  2.0*minb("nodes")-(5.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt':
                try:
                    set("nodes",  maxb("edges")/2.0+5.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem135(Theorem):
    def __init__(self):
        super(Theorem135, self).__init__(135, "edges >= 2.0*nodeCover-(numOfComponents);\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodeCover") != 'undt' and minb("numOfComponents") != 'undt':
            try:
                set("edges",  2.0*minb("nodeCover")-(maxb("numOfComponents")), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("numOfComponents") != 'undt':
            try:
                set("nodeCover",  maxb("edges")/2.0+maxb("numOfComponents")/2.0, ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("numOfComponents",  -(maxb("edges"))+2.0*minb("nodeCover"), ind='Min')
            except:
                pass
        return
class Theorem136(Theorem):
    def __init__(self):
        super(Theorem136, self).__init__(136, "if maxdeg <= 2.0*edgeInd and odd maxdeg then \n{\n    edges <= edgeInd*maxb(maxdeg)+(maxb(maxdeg)-(1.0))/2.0*2.0*edgeInd/(maxb(maxdeg)+1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","edgeInd","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxdeg") != 'undt' and minb("edgeInd") != 'undt' and maxb("maxdeg") <= 2.0*minb("edgeInd")) and oddInvar("maxdeg"):
            if maxb("edgeInd") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("edges",  maxb("edgeInd")*maxb("maxdeg")+(maxb("maxdeg")-(1.0))/2.0*2.0*maxb("edgeInd")/(maxb("maxdeg")+1.0), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edgeInd",  minb("edges")*(maxb("maxdeg")+1.0)/(maxb("maxdeg")**2.0+2.0*maxb("maxdeg")-(1.0)), ind='Min')
                except:
                    pass
        return
class Theorem137(Theorem):
    def __init__(self):
        super(Theorem137, self).__init__(137, "edges <= nodes*(nodes-(1.0))/2.0;\nedges >= (nodes+1.0)/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt':
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/2.0, ind='Max')
            except:
                pass
        if minb("edges") != 'undt':
            try:
                set("nodes",  sqrt(8.0*minb("edges")+1.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        if minb("nodes") != 'undt':
            try:
                set("edges",  (minb("nodes")+1.0)/2.0, ind='Min')
            except:
                pass
        if maxb("edges") != 'undt':
            try:
                set("nodes",  2.0*maxb("edges")-(1.0), ind='Max')
            except:
                pass
        return
class Theorem138(Theorem):
    def __init__(self):
        super(Theorem138, self).__init__(138, "if edges >= (1.0/2.0)*(nodes*nodes-(5.0*nodes)+14.0) then \n{\n    circumference >= nodes-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= (1.0/2.0)*(maxb("nodes")*maxb("nodes")-(5.0*maxb("nodes"))+14.0)):
            if minb("nodes") != 'undt':
                try:
                    set("circumference",  minb("nodes")-(1.0), ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("nodes",  maxb("circumference")+1.0, ind='Max')
                except:
                    pass
        return
class Theorem139(Theorem):
    def __init__(self):
        super(Theorem139, self).__init__(139, "if edges >= (1.0/4.0)*(circumference*(2.0*nodes-(circumference))+1.0) then \n{\n    girth == 3.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","circumference","nodes","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt' and maxb("circumference") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= (1.0/4.0)*(maxb("circumference")*(2.0*maxb("nodes")-(maxb("circumference")))+1.0)):
            try:
                set("girth",  3.0, ind='Min')
            except:
                pass
            try:
                set("girth",  3.0, ind='Max')
            except:
                pass
        return
class Theorem140(Theorem):
    def __init__(self):
        super(Theorem140, self).__init__(140, "if minb(edges) >= 4.0*maxb(nodes) then \n{\n    crossing >= minb(edges)**3.0/(100.0*maxb(nodes)**2.0)+1.0,\n    edges <= (100.0*maxb(crossing)*maxb(nodes)**2.0-(100.0*maxb(nodes)**2.0))**(1.0/3.0),\n    nodes >= sqrt(minb(edges)**3.0/(maxb(crossing)-(1.0)))/10.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","crossing"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= 4.0*maxb("nodes")):
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("crossing",  minb("edges")**3.0/(100.0*maxb("nodes")**2.0)+1.0, ind='Min')
                except:
                    pass
            if maxb("crossing") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("edges",  (100.0*maxb("crossing")*maxb("nodes")**2.0-(100.0*maxb("nodes")**2.0))**(1.0/3.0), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("crossing") != 'undt':
                try:
                    set("nodes",  sqrt(minb("edges")**3.0/(maxb("crossing")-(1.0)))/10.0, ind='Min')
                except:
                    pass
        return
class Theorem141(Theorem):
    def __init__(self):
        super(Theorem141, self).__init__(141, "circumference >= 2.0*edges/(maxb(nodes)-(1.0));\nnodes >= (maxb(circumference)+2.0*minb(edges))/maxb(circumference);\n", "")
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
        if minb("edges") != 'undt' and minb("nodes") != 'undt':
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
                set("nodes",  (maxb("circumference")+2.0*minb("edges"))/maxb("circumference"), ind='Min')
            except:
                pass
        return
class Theorem142(Theorem):
    def __init__(self):
        super(Theorem142, self).__init__(142, "\n", "REPLACED BY R343")
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
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
            try:
                set("nodeCliqueCover",  (1.0/2.0)+sqrt(1.0/4.0+maxb("nodes")**2.0-(maxb("nodes"))-(2.0*minb("edges"))), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  sqrt(8.0*minb("edges")+(2.0*minb("nodeCliqueCover")-(1.0))**2.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
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
        super(Theorem145, self).__init__(145, "if maxClique == 2.0 then \n{\n    nodeInd >= 1.0/2.0*sqrt(8.0*nodes+9.0)-(3.0)\n};\n", "")
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
        super(Theorem146, self).__init__(146, "if connected then \n{\n    bandwidth <= nodes-(diameter)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","bandwidth","nodes","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("bandwidth",  maxb("nodes")-(minb("diameter")), ind='Max')
                except:
                    pass
            if minb("bandwidth") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodes",  minb("bandwidth")+minb("diameter"), ind='Min')
                except:
                    pass
            if maxb("bandwidth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("diameter",  -(minb("bandwidth"))+maxb("nodes"), ind='Max')
                except:
                    pass
        return
class Theorem147(Theorem):
    def __init__(self):
        super(Theorem147, self).__init__(147, "if maxClique == 2.0 then \n{\n    if maxdeg >= nodes-(2.0) or nodes <= 4.0 then \n    {\n        chromaticNum <= 2.0\n    }\n    else if nodes >= 5.0 and nodes <= 10.0 then \n    {\n        chromaticNum <= 3.0\n    }\n    else  \n    {\n        chromaticNum <= (nodes-(maxdeg)+10.0)/4.0\n    }\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if (minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(2.0)) or (maxb("nodes") != 'undt' and maxb("nodes") <= 4.0):
                try:
                    set("chromaticNum",  2.0, ind='Max')
                except:
                    pass
            elif (minb("nodes") != 'undt' and minb("nodes") >= 5.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 10.0):
                try:
                    set("chromaticNum",  3.0, ind='Max')
                except:
                    pass
            elif True:
                if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("chromaticNum",  (maxb("nodes")-(minb("maxdeg"))+10.0)/4.0, ind='Max')
                    except:
                        pass
                if minb("chromaticNum") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  4.0*minb("chromaticNum")+minb("maxdeg")-(10.0), ind='Min')
                    except:
                        pass
                if maxb("chromaticNum") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("maxdeg",  -(4.0*minb("chromaticNum"))+maxb("nodes")+10.0, ind='Max')
                    except:
                        pass
        return
class Theorem148(Theorem):
    def __init__(self):
        super(Theorem148, self).__init__(148, "if mindeg == 3.0 and maxdeg == 3.0 and planar and edgeConnec >= 2.0 then \n{\n    edgeChromatic == maxdeg\n};\n", "")
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
        super(Theorem149, self).__init__(149, "if planar and maxdeg >= 8.0 then \n{\n    edgeChromatic == maxdeg\n};\n", "")
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
        super(Theorem150, self).__init__(150, "if spectralRadius <= maxdeg/2.0 then \n{\n    edgeChromatic == maxdeg\n};\n", "")
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
        super(Theorem151, self).__init__(151, "if nodes > 2.0 and regular and nodeConnec == 1.0 then \n{\n    edgeChromatic == maxdeg+1.0\n};\n", "")
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
        super(Theorem152, self).__init__(152, "if (minb(maxClique) >= 2.0 and maxb(maxClique) <= 2.0) and minb(nodeInd) >= 2.0*maxb(nodes)/5.0 and maxb(nodeInd) <= minb(nodes)/2.0 then \n{\n    edges <= maxb(nodeInd)**2.0+4.0*(maxb(nodes)/2.0-(maxb(nodeInd)))**2.0,\n    nodeInd >= 2.0*maxb(nodes)/5.0+sqrt(5.0*minb(edges)-(maxb(nodes)**2.0))/5.0,\n    nodes >= 2.0*maxb(nodeInd)+sqrt(minb(edges)-(maxb(nodeInd)**2.0))\n};\n", "")
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
            if maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("edges",  maxb("nodeInd")**2.0+4.0*(maxb("nodes")/2.0-(maxb("nodeInd")))**2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodeInd",  2.0*maxb("nodes")/5.0+sqrt(5.0*minb("edges")-(maxb("nodes")**2.0))/5.0, ind='Min')
                except:
                    pass
            if minb("nodeInd") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeInd")+sqrt(minb("edges")-(maxb("nodeInd")**2.0)), ind='Min')
                except:
                    pass
        return
class Theorem153(Theorem):
    def __init__(self):
        super(Theorem153, self).__init__(153, "if maxdeg == 2.0 or radius == 1.0 then \n{\n    bandwidth <= maxdeg\n}\nelse  \n{\n    bandwidth <= maxdeg*(maxdeg-(1.0))**(radius-(1.0))\n};\n", "")
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
        super(Theorem154, self).__init__(154, "\n", "RETIRED by R265")
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
        super(Theorem155, self).__init__(155, "if mindeg == 2.0 then \n{\n    nodes <= (2.0+maximum(4.0, maxb(maxdeg)))*edgeInd/2.0\n};\n", "")
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
            if maxb("maxdeg") != 'undt' and maxb("edgeInd") != 'undt':
                try:
                    set("nodes",  (2.0+maximum(4.0, maxb("maxdeg")))*maxb("edgeInd")/2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edgeInd",  2.0*minb("nodes")/(maximum(4.0, maxb("maxdeg"))+2.0), ind='Min')
                except:
                    pass
        return
class Theorem156(Theorem):
    def __init__(self):
        super(Theorem156, self).__init__(156, "if mindeg <= nodes/2.0 then \n{\n    edgeInd >= mindeg\n};\n", "")
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
        super(Theorem157, self).__init__(157, "if maxClique <= (mindeg-(1.0))/2.0 then \n{\n    chromaticNum <= maxdeg-(1.0)\n};\n", "")
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
        super(Theorem158, self).__init__(158, "if connected then \n{\n    if edges <= nodes+3.0 then \n    {\n        genus <= 0.0\n    }\n    else if edges <= nodes+6.0 then \n    {\n        genus <= 1.0\n    }\n    else if edges <= nodes+9.0 then \n    {\n        genus <= 2.0\n    }\n};\n", "")
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
        if get("connected") == True:
            if (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+3.0):
                try:
                    set("genus",  0.0, ind='Max')
                except:
                    pass
            elif (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+6.0):
                try:
                    set("genus",  1.0, ind='Max')
                except:
                    pass
            elif (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= minb("nodes")+9.0):
                try:
                    set("genus",  2.0, ind='Max')
                except:
                    pass
        return
class Theorem159(Theorem):
    def __init__(self):
        super(Theorem159, self).__init__(159, "nodeInd >= (nodes-(1.0))/(maxb(maxdeg)+1.0)+1.0/(maxb(mindeg)+1.0);\nmaxdeg >= (-(maxb(mindeg)*maxb(nodeInd))+maxb(mindeg)*minb(nodes)-(maxb(mindeg))-(maxb(nodeInd))+minb(nodes))/(maxb(mindeg)*maxb(nodeInd)+maxb(nodeInd)-(1.0));\nmindeg >= (-(maxb(maxdeg)*maxb(nodeInd))+maxb(maxdeg)-(maxb(nodeInd))+minb(nodes))/(maxb(maxdeg)*maxb(nodeInd)+maxb(nodeInd)-(minb(nodes))+1.0);\n", "")
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
        if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodeInd",  (minb("nodes")-(1.0))/(maxb("maxdeg")+1.0)+1.0/(maxb("mindeg")+1.0), ind='Min')
            except:
                pass
        if maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodes",  (maxb("maxdeg")*maxb("mindeg")*maxb("nodeInd")+maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg"))+maxb("mindeg")*maxb("nodeInd")+maxb("mindeg")+maxb("nodeInd"))/(maxb("mindeg")+1.0), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(maxb("mindeg")*maxb("nodeInd"))+maxb("mindeg")*minb("nodes")-(maxb("mindeg"))-(maxb("nodeInd"))+minb("nodes"))/(maxb("mindeg")*maxb("nodeInd")+maxb("nodeInd")-(1.0)), ind='Min')
            except:
                pass
        if minb("maxdeg") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("mindeg",  (-(maxb("maxdeg")*maxb("nodeInd"))+maxb("maxdeg")-(maxb("nodeInd"))+minb("nodes"))/(maxb("maxdeg")*maxb("nodeInd")+maxb("nodeInd")-(minb("nodes"))+1.0), ind='Min')
            except:
                pass
        return
class Theorem160(Theorem):
    def __init__(self):
        super(Theorem160, self).__init__(160, "if maxClique == 2.0 then \n{\n    if maxdeg >= 3.0 then \n    {\n        nodeInd >= nodes/(maxb(maxdeg)-(1.0/5.0)),\n        maxdeg >= (maxb(nodeInd)/5.0+minb(nodes))/maxb(nodeInd)\n    }\n    else if nodes >= 3.0 and connected and (not cycle or (cycle and isset nodes and even nodes)) and (edges >= nodes or maxdeg > 2.0 or (isset nodes and odd nodes)) then \n    {\n        nodeInd >= nodes/maxb(maxdeg)-(1.0/(maxb(maxdeg)+1.0))+1.0/(mindeg+1.0)\n    }\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
                if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodeInd",  minb("nodes")/(maxb("maxdeg")-(1.0/5.0)), ind='Min')
                    except:
                        pass
                if maxb("nodeInd") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("nodes",  maxb("nodeInd")*(maxb("maxdeg")-(1.0/5.0)), ind='Max')
                    except:
                        pass
                if minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
                    try:
                        set("maxdeg",  (maxb("nodeInd")/5.0+minb("nodes"))/maxb("nodeInd"), ind='Min')
                    except:
                        pass
            elif (minb("nodes") != 'undt' and minb("nodes") >= 3.0) and get("connected") == True and (get("cycle") == False or (get("cycle") == True and maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and evenInvar("nodes"))) and ((minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= maxb("nodes")) or (minb("maxdeg") != 'undt' and minb("maxdeg") > 2.0) or (maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and oddInvar("nodes"))):
                if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("mindeg") != 'undt':
                    try:
                        set("nodeInd",  minb("nodes")/maxb("maxdeg")-(1.0/(maxb("maxdeg")+1.0))+1.0/(maxb("mindeg")+1.0), ind='Min')
                    except:
                        pass
                if maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeInd") != 'undt':
                    try:
                        set("nodes",  maxb("maxdeg")*(maxb("maxdeg")*maxb("mindeg")*maxb("nodeInd")+maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg"))+maxb("mindeg")*maxb("nodeInd")+maxb("mindeg")+maxb("nodeInd"))/(maxb("maxdeg")*maxb("mindeg")+maxb("maxdeg")+maxb("mindeg")+1.0), ind='Max')
                    except:
                        pass
        return
class Theorem161(Theorem):
    def __init__(self):
        super(Theorem161, self).__init__(161, "if genus > 2.0 and girth >= 4.0 then \n{\n    if mindeg >= (5.0+(16.0*genus+1.0)**(1.0/2.0))/2.0 and mindeg == (3.0+(16.0*genus+9.0)**(1.0/2.0))/2.0 then \n    {\n        regular,\n        hamiltonian,\n        nodes == 2.0*mindeg+2.0\n    }\n    else if mindeg >= (5.0+(16.0*genus+1.0)**(1.0/2.0))/2.0 then \n    {\n        regular,\n        hamiltonian,\n        nodes == 2.0*mindeg\n    }\n};\n", "")
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
        if (minb("genus") != 'undt' and minb("genus") > 2.0) and (minb("girth") != 'undt' and minb("girth") >= 4.0):
            if (minb("mindeg") != 'undt' and maxb("genus") != 'undt' and minb("mindeg") >= (5.0+(16.0*maxb("genus")+1.0)**(1.0/2.0))/2.0) and ((minb("mindeg") != 'undt' and maxb("genus") != 'undt' and minb("mindeg") >= (3.0+(16.0*maxb("genus")+9.0)**(1.0/2.0))/2.0) and (maxb("mindeg") != 'undt' and minb("genus") != 'undt' and maxb("mindeg") <= (3.0+(16.0*minb("genus")+9.0)**(1.0/2.0))/2.0)):
                set("regular", True)
                set("hamiltonian", True)
                if minb("mindeg") != 'undt':
                    try:
                        set("nodes",  2.0*minb("mindeg")+2.0, ind='Min')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("mindeg",  maxb("nodes")/2.0-(1.0), ind='Max')
                    except:
                        pass
                if maxb("mindeg") != 'undt':
                    try:
                        set("nodes",  2.0*maxb("mindeg")+2.0, ind='Max')
                    except:
                        pass
                if minb("nodes") != 'undt':
                    try:
                        set("mindeg",  minb("nodes")/2.0-(1.0), ind='Min')
                    except:
                        pass
            elif (minb("mindeg") != 'undt' and maxb("genus") != 'undt' and minb("mindeg") >= (5.0+(16.0*maxb("genus")+1.0)**(1.0/2.0))/2.0):
                set("regular", True)
                set("hamiltonian", True)
                if minb("mindeg") != 'undt':
                    try:
                        set("nodes",  2.0*minb("mindeg"), ind='Min')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("mindeg",  maxb("nodes")/2.0, ind='Max')
                    except:
                        pass
                if maxb("mindeg") != 'undt':
                    try:
                        set("nodes",  2.0*maxb("mindeg"), ind='Max')
                    except:
                        pass
                if minb("nodes") != 'undt':
                    try:
                        set("mindeg",  minb("nodes")/2.0, ind='Min')
                    except:
                        pass
        return
class Theorem162(Theorem):
    def __init__(self):
        super(Theorem162, self).__init__(162, "if nodeConnec >= 2.0 and regular and ((even nodes and mindeg >= (nodes-((2.0*nodes)**(1.0/2.0)))/2.0) or (odd nodes and mindeg >= (nodes-(nodes**(1.0/2.0)))/2.0)) then \n{\n    hamiltonian\n};\n", "")
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
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and get("regular") == True and ((evenInvar("nodes") and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= (maxb("nodes")-((2.0*maxb("nodes"))**(1.0/2.0)))/2.0)) or (oddInvar("nodes") and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= (maxb("nodes")-(maxb("nodes")**(1.0/2.0)))/2.0))):
            set("hamiltonian", True)
        return
class Theorem163(Theorem):
    def __init__(self):
        super(Theorem163, self).__init__(163, "if regular and nodeConnec >= 2.0 and nodes <= 3.0*mindeg then \n{\n    hamiltonian\n};\n", "")
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
        if get("regular") == True and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodes") <= 3.0*minb("mindeg")):
            set("hamiltonian", True)
        return
class Theorem164(Theorem):
    def __init__(self):
        super(Theorem164, self).__init__(164, "if spectralRadius > edges**(1.0/2.0) then \n{\n    girth == 3.0\n};\n", "")
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
        if (minb("spectralRadius") != 'undt' and maxb("edges") != 'undt' and minb("spectralRadius") > maxb("edges")**(1.0/2.0)):
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
        super(Theorem165, self).__init__(165, "spectralRadius >= maxdeg**(1.0/2.0);\n", "")
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
        if minb("maxdeg") != 'undt':
            try:
                set("spectralRadius",  minb("maxdeg")**(1.0/2.0), ind='Min')
            except:
                pass
        if maxb("spectralRadius") != 'undt':
            try:
                set("maxdeg",  maxb("spectralRadius")**2.0, ind='Max')
            except:
                pass
        return
class Theorem166(Theorem):
    def __init__(self):
        super(Theorem166, self).__init__(166, "if diameter > 1.0 and nodeConnec > 1.0 and maxb(nodeConnec) > 1.0 then \n{\n    edges >= (nodes*maxb(diameter)-(2.0*maxb(diameter))+1.0)/(maxb(diameter)-(1.0)),\n    diameter >= (maxb(edges)+1.0)/(maxb(edges)-(minb(nodes))+2.0)\n};\n", "")
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
        if (minb("diameter") != 'undt' and minb("diameter") > 1.0) and (minb("nodeConnec") != 'undt' and minb("nodeConnec") > 1.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") > 1.0):
            if minb("nodes") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("edges",  (minb("nodes")*maxb("diameter")-(2.0*maxb("diameter"))+1.0)/(maxb("diameter")-(1.0)), ind='Min')
                except:
                    pass
            if maxb("diameter") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodes",  (maxb("diameter")*(maxb("edges")+2.0)-(maxb("edges"))-(1.0))/maxb("diameter"), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("diameter",  (maxb("edges")+1.0)/(maxb("edges")-(minb("nodes"))+2.0), ind='Min')
                except:
                    pass
        return
class Theorem167(Theorem):
    def __init__(self):
        super(Theorem167, self).__init__(167, "if girth >= 5.0 then \n{\n    chromaticNum <= (maxdeg+3.0)*2.0/3.0\n};\n", "")
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
        if (minb("girth") != 'undt' and minb("girth") >= 5.0):
            if maxb("maxdeg") != 'undt':
                try:
                    set("chromaticNum",  (maxb("maxdeg")+3.0)*2.0/3.0, ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("maxdeg",  3.0*minb("chromaticNum")/2.0-(3.0), ind='Min')
                except:
                    pass
        return
class Theorem168(Theorem):
    def __init__(self):
        super(Theorem168, self).__init__(168, "if girth >= 2.0*maxdeg**2.0 then \n{\n    chromaticNum <= (maxdeg+4.0)/2.0\n};\n", "")
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
        if (minb("girth") != 'undt' and maxb("maxdeg") != 'undt' and minb("girth") >= 2.0*maxb("maxdeg")**2.0):
            if maxb("maxdeg") != 'undt':
                try:
                    set("chromaticNum",  (maxb("maxdeg")+4.0)/2.0, ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("maxdeg",  2.0*minb("chromaticNum")-(4.0), ind='Min')
                except:
                    pass
        return
class Theorem169(Theorem):
    def __init__(self):
        super(Theorem169, self).__init__(169, "nodeInd >= nodes**2.0/(2.0*edges+nodes);\n", "")
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
        if minb("nodes") != 'undt' and minb("edges") != 'undt':
            try:
                set("nodeInd",  minb("nodes")**2.0/(2.0*maxb("edges")+minb("nodes")), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("edges") != 'undt':
            try:
                set("nodes",  maxb("nodeInd")/2.0+sqrt(maxb("nodeInd")*(8.0*maxb("edges")+maxb("nodeInd")))/2.0, ind='Max')
            except:
                pass
        if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("edges",  minb("nodes")*(-(maxb("nodeInd"))+minb("nodes"))/(2.0*maxb("nodeInd")), ind='Min')
            except:
                pass
        return
class Theorem170(Theorem):
    def __init__(self):
        super(Theorem170, self).__init__(170, "if connected and not complete then \n{\n    _P is minb(nodes),\n    nodeInd >= (_P**3.0+3.0*_P+1.0)/(_P*(2.0*edges+_P))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","complete","nodes","nodeInd","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and get("complete") == False:
            if minb("nodes") != 'undt':
                _P = minb("nodes")
            if minb("edges") != 'undt':
                try:
                    set("nodeInd",  (_P**3.0+3.0*_P+1.0)/(_P*(2.0*maxb("edges")+_P)), ind='Min')
                except:
                    pass
            if minb("nodeInd") != 'undt':
                try:
                    set("edges",  (-(_P**2.0*maxb("nodeInd"))+_P*(_P**2.0+3.0)+1.0)/(2.0*_P*maxb("nodeInd")), ind='Min')
                except:
                    pass
        return
class Theorem171(Theorem):
    def __init__(self):
        super(Theorem171, self).__init__(171, "if genus > 1.0 and girth >= 4.0 then \n{\n    mindeg <= 2.0+2.0*genus**(1.0/2.0)\n};\n", "")
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
        if (minb("genus") != 'undt' and minb("genus") > 1.0) and (minb("girth") != 'undt' and minb("girth") >= 4.0):
            if maxb("genus") != 'undt':
                try:
                    set("mindeg",  2.0+2.0*maxb("genus")**(1.0/2.0), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("genus",  (minb("mindeg")-(2.0))**2.0/4.0, ind='Min')
                except:
                    pass
        return
class Theorem172(Theorem):
    def __init__(self):
        super(Theorem172, self).__init__(172, "if connected then \n{\n    diameter <= 2.0*nodeCover\n};\n", "")
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
        if get("connected") == True:
            if maxb("nodeCover") != 'undt':
                try:
                    set("diameter",  2.0*maxb("nodeCover"), ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt':
                try:
                    set("nodeCover",  minb("diameter")/2.0, ind='Min')
                except:
                    pass
        return
class Theorem173(Theorem):
    def __init__(self):
        super(Theorem173, self).__init__(173, "nodeInd >= 2.0*nodes/(maxdeg+maxClique+1.0);\n", "")
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
        if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("nodeInd",  2.0*minb("nodes")/(maxb("maxdeg")+maxb("maxClique")+1.0), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("maxClique") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("nodes",  maxb("nodeInd")*(maxb("maxClique")+maxb("maxdeg")+1.0)/2.0, ind='Max')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("maxdeg",  -(maxb("maxClique"))-(1.0)+2.0*minb("nodes")/maxb("nodeInd"), ind='Min')
            except:
                pass
        if minb("maxdeg") != 'undt' and minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("maxClique",  -(maxb("maxdeg"))-(1.0)+2.0*minb("nodes")/maxb("nodeInd"), ind='Min')
            except:
                pass
        return
class Theorem174(Theorem):
    def __init__(self):
        super(Theorem174, self).__init__(174, "_maxdeg is maxb(maxdeg);\nnodeInd >= (nodes+2.0*_maxdeg+1.0-(maxClique)-(mindeg))/(_maxdeg+1.0);\nmaxdeg >= (-(maxb(maxClique))-(maxb(mindeg))-(maxb(nodeInd))+minb(nodes)+1.0)/(maxb(nodeInd)-(2.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodeInd","nodes","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("maxdeg") != 'undt':
            _maxdeg = maxb("maxdeg")
        if minb("nodes") != 'undt' and minb("maxClique") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodeInd",  (minb("nodes")+2.0*_maxdeg+1.0-(maxb("maxClique"))-(maxb("mindeg")))/(_maxdeg+1.0), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("maxClique") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodes",  _maxdeg*maxb("nodeInd")-(2.0*_maxdeg)+maxb("maxClique")+maxb("mindeg")+maxb("nodeInd")-(1.0), ind='Max')
            except:
                pass
        if minb("nodeInd") != 'undt' and minb("mindeg") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxClique",  -(_maxdeg*maxb("nodeInd"))+2.0*_maxdeg-(maxb("mindeg"))-(maxb("nodeInd"))+minb("nodes")+1.0, ind='Min')
            except:
                pass
        if minb("nodeInd") != 'undt' and minb("maxClique") != 'undt' and minb("nodes") != 'undt':
            try:
                set("mindeg",  -(_maxdeg*maxb("nodeInd"))+2.0*_maxdeg-(maxb("maxClique"))-(maxb("nodeInd"))+minb("nodes")+1.0, ind='Min')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("mindeg") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(maxb("maxClique"))-(maxb("mindeg"))-(maxb("nodeInd"))+minb("nodes")+1.0)/(maxb("nodeInd")-(2.0)), ind='Min')
            except:
                pass
        return
class Theorem175(Theorem):
    def __init__(self):
        super(Theorem175, self).__init__(175, "_P is maxb(nodes);\nbandwidth >= (1.0/2.0)*(2.0*_P-(1.0)-(sqrt((2.0*_P-(1.0))**2.0-(8.0*edges))));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","bandwidth","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt':
            _P = maxb("nodes")
        if minb("edges") != 'undt':
            try:
                set("bandwidth",  (1.0/2.0)*(2.0*_P-(1.0)-(sqrt((2.0*_P-(1.0))**2.0-(8.0*minb("edges"))))), ind='Min')
            except:
                pass
        if maxb("bandwidth") != 'undt':
            try:
                set("edges",  maxb("bandwidth")*(2.0*_P-(maxb("bandwidth"))-(1.0))/2.0, ind='Max')
            except:
                pass
        return
class Theorem176(Theorem):
    def __init__(self):
        super(Theorem176, self).__init__(176, "if maxClique == 2.0 then \n{\n    bandwidth >= (1.0/2.0)*(3.0*mindeg-(1.0))\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if minb("mindeg") != 'undt':
                try:
                    set("bandwidth",  (1.0/2.0)*(3.0*minb("mindeg")-(1.0)), ind='Min')
                except:
                    pass
            if maxb("bandwidth") != 'undt':
                try:
                    set("mindeg",  2.0*maxb("bandwidth")/3.0+1.0/3.0, ind='Max')
                except:
                    pass
        return
class Theorem177(Theorem):
    def __init__(self):
        super(Theorem177, self).__init__(177, "\n", "Replaced by r280")
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
        super(Theorem178, self).__init__(178, "_k is maximum(4.0, maxb(nodeInd)+1.0);\nnodeCliqueCover <= nodes-(mindeg)-((nodes-(mindeg))/_k):useMinFor(mindeg);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeInd") != 'undt':
            _k = maximum(4.0, maxb("nodeInd")+1.0)
        if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodeCliqueCover",  maxb("nodes")-(minb("mindeg"))-((maxb("nodes")-(minb("mindeg")))/_k), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("nodes",  (_k*minb("mindeg")+_k*minb("nodeCliqueCover")-(minb("mindeg")))/(_k-(1.0)), ind='Min')
            except:
                pass
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("mindeg",  (-(_k*minb("nodeCliqueCover"))+_k*maxb("nodes")-(maxb("nodes")))/(_k-(1.0)), ind='Max')
            except:
                pass
        return
class Theorem179(Theorem):
    def __init__(self):
        super(Theorem179, self).__init__(179, "if minb(domination) >= 2.0 then \n{\n    edges <= (1.0/2.0)*(maxb(nodes)-(minb(nodeInd)))*(maxb(nodes)+minb(nodeInd)-(2.0*minb(domination))+2.0),\n    nodes >= minb(domination)+sqrt(minb(domination)**2.0-(2.0*minb(domination)*minb(nodeInd))-(2.0*minb(domination))+2.0*minb(edges)+minb(nodeInd)**2.0+2.0*minb(nodeInd)+1.0)-(1.0),\n    nodeInd <= minb(domination)+sqrt(minb(domination)**2.0-(2.0*minb(domination)*minb(nodes))-(2.0*minb(domination))-(2.0*minb(edges))+minb(nodes)**2.0+2.0*minb(nodes)+1.0)-(1.0),\n    _k is maxb(nodes)-(2.0*minb(edges)),\n    if minb(nodeInd) > _k then \n    {\n        _k is minb(nodeInd)\n    }\n    else if maxb(nodeInd) < _k then \n    {\n        _k is maxb(nodeInd)\n    },\n    domination <= ((maxb(nodes)+_k+2.0)*(maxb(nodes)-(_k))-(2.0*minb(edges)))/(2.0*(maxb(nodes)-(_k)))\n};\n", "")
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
        if (minb("domination") != 'undt' and minb("domination") >= 2.0):
            if maxb("nodes") != 'undt' and maxb("nodeInd") != 'undt' and maxb("domination") != 'undt':
                try:
                    set("edges",  (1.0/2.0)*(maxb("nodes")-(minb("nodeInd")))*(maxb("nodes")+minb("nodeInd")-(2.0*minb("domination"))+2.0), ind='Max')
                except:
                    pass
            if minb("domination") != 'undt' and minb("nodeInd") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  minb("domination")+sqrt(minb("domination")**2.0-(2.0*minb("domination")*minb("nodeInd"))-(2.0*minb("domination"))+2.0*minb("edges")+minb("nodeInd")**2.0+2.0*minb("nodeInd")+1.0)-(1.0), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodeInd",  minb("domination")+sqrt(minb("domination")**2.0-(2.0*minb("domination")*minb("nodes"))-(2.0*minb("domination"))-(2.0*minb("edges"))+minb("nodes")**2.0+2.0*minb("nodes")+1.0)-(1.0), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt' and minb("edges") != 'undt':
                _k = maxb("nodes")-(2.0*minb("edges"))
            if (minb("nodeInd") != 'undt' and '_k' in vars() and minb("nodeInd") > _k):
                if minb("nodeInd") != 'undt':
                    _k = minb("nodeInd")
            elif (maxb("nodeInd") != 'undt' and '_k' in vars() and maxb("nodeInd") < _k):
                if maxb("nodeInd") != 'undt':
                    _k = maxb("nodeInd")
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("domination",  ((maxb("nodes")+_k+2.0)*(maxb("nodes")-(_k))-(2.0*minb("edges")))/(2.0*(maxb("nodes")-(_k))), ind='Max')
                except:
                    pass
        return

class Theorem180(Theorem):
    def __init__(self):
        super(Theorem180, self).__init__(180, "if regular and nodes > 5.0 then \n{\n    if maxdeg >= nodes/2.0 and maxdeg <= nodes-(2.0) and ((odd nodes and even maxdeg) or (odd maxdeg and even nodes)) then \n    {\n        chromaticNum <= minimum(maxdeg, 3.0*nodes/5.0)\n    }\n    else if maxdeg >= nodes/2.0 and maxdeg <= nodes-(2.0) then \n    {\n        chromaticNum <= minimum(maxdeg, (2.0*(nodes-(maxdeg))-(3.0))*nodes/(3.0*(nodes-(maxdeg))-(4.0)))\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (minb("nodes") != 'undt' and minb("nodes") > 5.0):
            if (minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")/2.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0)) and ((oddInvar("nodes") and evenInvar("maxdeg")) or (oddInvar("maxdeg") and evenInvar("nodes"))):
                if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("chromaticNum",  minimum(maxb("maxdeg"), 3.0*maxb("nodes")/5.0), ind='Max')
                    except:
                        pass
            elif (minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")/2.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0)):
                if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("chromaticNum",  minimum(maxb("maxdeg"), (2.0*(maxb("nodes")-(maxb("maxdeg")))-(3.0))*maxb("nodes")/(3.0*(maxb("nodes")-(maxb("maxdeg")))-(4.0))), ind='Max')
                    except:
                        pass
        return
class Theorem181(Theorem):
    def __init__(self):
        super(Theorem181, self).__init__(181, "if nodeCliqueCover > nodeInd then \n{\n    maxdeg >= 3.0*nodes/(3.0*nodeInd-(1.0))-(1.0)\n};\n", "")
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
        if (minb("nodeCliqueCover") != 'undt' and maxb("nodeInd") != 'undt' and minb("nodeCliqueCover") > maxb("nodeInd")):
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("maxdeg",  3.0*minb("nodes")/(3.0*maxb("nodeInd")-(1.0))-(1.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("maxdeg")*maxb("nodeInd")-(maxb("maxdeg")/3.0)+maxb("nodeInd")-(1.0/3.0), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeInd",  (maxb("maxdeg")+3.0*minb("nodes")+1.0)/(3.0*(maxb("maxdeg")+1.0)), ind='Min')
                except:
                    pass
        return
class Theorem182(Theorem):
    def __init__(self):
        super(Theorem182, self).__init__(182, "maxClique >= 2.0*maxb(nodes)/(maxb(nodes)-(mindeg)+nodeInd);\nnodes >= maxb(maxClique)*(minb(mindeg)-(maxb(nodeInd)))/(maxb(maxClique)-(2.0));\n", "")
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
        if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("maxClique",  2.0*maxb("nodes")/(maxb("nodes")-(minb("mindeg"))+maxb("nodeInd")), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("mindeg",  maxb("nodes")-(2.0*maxb("nodes")/maxb("maxClique"))+maxb("nodeInd"), ind='Max')
            except:
                pass
        if minb("nodes") != 'undt' and minb("maxClique") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodeInd",  -(maxb("nodes"))+2.0*maxb("nodes")/maxb("maxClique")+minb("mindeg"), ind='Min')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("mindeg") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("nodes",  maxb("maxClique")*(minb("mindeg")-(maxb("nodeInd")))/(maxb("maxClique")-(2.0)), ind='Min')
            except:
                pass
        return
class Theorem183(Theorem):
    def __init__(self):
        super(Theorem183, self).__init__(183, "if nodeInd <= 2.0 then \n{\n    maxClique >= (1.0/2.0)*(sqrt(9.0+8.0*nodes)-(3.0))\n};\n", "")
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
        if (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0):
            if minb("nodes") != 'undt':
                try:
                    set("maxClique",  (1.0/2.0)*(sqrt(9.0+8.0*minb("nodes"))-(3.0)), ind='Min')
                except:
                    pass
            if maxb("maxClique") != 'undt':
                try:
                    set("nodes",  maxb("maxClique")*(maxb("maxClique")+3.0)/2.0, ind='Max')
                except:
                    pass
        return
class Theorem184(Theorem):
    def __init__(self):
        super(Theorem184, self).__init__(184, "let e1 = (maxb(nodes)*(maxb(nodes)-(1.0))+1.0)/(2.0-((maxb(nodes)-(minb(mindeg))-(1.0))*(maxb(nodes)-(minb(maxClique)))));\nlet e2 = (minb(nodes)*(minb(nodes)-(1.0))+1.0)/(2.0-((minb(nodes)-(minb(mindeg))-(1.0))*(minb(nodes)-(minb(maxClique)))));\nedges >= minimum(e1, e2);\nlet c1 = floor(minb(nodes)-((minb(nodes)*(minb(nodes)-(1.0))-(2.0*maxb(edges)))/(2.0*(minb(nodes)-(minb(mindeg))-(1.0)))));\nlet c2 = floor(maxb(nodes)-((maxb(nodes)*(maxb(nodes)-(1.0))-(2.0*maxb(edges)))/(2.0*(maxb(nodes)-(minb(mindeg))-(1.0)))));\nif minb(nodes) > minb(mindeg)+1.0 and maxb(nodes) > minb(mindeg)+1.0 then \n{\n    maxClique <= minimum(c1, c2)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","mindeg","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("edges",  minimum((maxb("nodes")*(maxb("nodes")-(1.0))+1.0)/(2.0-((maxb("nodes")-(minb("mindeg"))-(1.0))*(maxb("nodes")-(minb("maxClique"))))), (minb("nodes")*(minb("nodes")-(1.0))+1.0)/(2.0-((minb("nodes")-(minb("mindeg"))-(1.0))*(minb("nodes")-(minb("maxClique")))))), ind='Min')
            except:
                pass
        if (minb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodes") > minb("mindeg")+1.0) and (maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodes") > minb("mindeg")+1.0):
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("maxClique",  minimum(floor(minb("nodes")-((minb("nodes")*(minb("nodes")-(1.0))-(2.0*maxb("edges")))/(2.0*(minb("nodes")-(minb("mindeg"))-(1.0))))), floor(maxb("nodes")-((maxb("nodes")*(maxb("nodes")-(1.0))-(2.0*maxb("edges")))/(2.0*(maxb("nodes")-(minb("mindeg"))-(1.0)))))), ind='Max')
                except:
                    pass
        return
class Theorem185(Theorem):
    def __init__(self):
        super(Theorem185, self).__init__(185, "if nodeCliqueCover <= 2.0 then \n{\n    maxClique == chromaticNum\n};\n", "")
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
        if (maxb("nodeCliqueCover") != 'undt' and maxb("nodeCliqueCover") <= 2.0):
            if minb("chromaticNum") != 'undt':
                try:
                    set("maxClique",  minb("chromaticNum"), ind='Min')
                except:
                    pass
            if maxb("maxClique") != 'undt':
                try:
                    set("chromaticNum",  maxb("maxClique"), ind='Max')
                except:
                    pass
            if maxb("chromaticNum") != 'undt':
                try:
                    set("maxClique",  maxb("chromaticNum"), ind='Max')
                except:
                    pass
            if minb("maxClique") != 'undt':
                try:
                    set("chromaticNum",  minb("maxClique"), ind='Min')
                except:
                    pass
        return
class Theorem186(Theorem):
    def __init__(self):
        super(Theorem186, self).__init__(186, "if nodeInd == 2.0 and nodeCliqueCover >= 4.0 then \n{\n    nodes >= 11.0\n};\n", "")
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
        if ((minb("nodeInd") != 'undt' and minb("nodeInd") >= 2.0) and (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0)) and (minb("nodeCliqueCover") != 'undt' and minb("nodeCliqueCover") >= 4.0):
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        return
class Theorem187(Theorem):
    def __init__(self):
        super(Theorem187, self).__init__(187, "if regular and maxdeg <= nodes-(2.0) then \n{\n    maxClique <= (1.0/2.0)*maxb(nodes)-((minb(nodeInd)-(1.0))*(minb(nodeInd)-(2.0))/(2.0*(maxb(nodes)-(minb(maxdeg))-(1.0)))),\n    nodes >= minb(maxClique)+minb(maxdeg)/2.0+sqrt(4.0*minb(maxClique)**2.0-(4.0*minb(maxClique)*minb(maxdeg))-(4.0*minb(maxClique))+minb(maxdeg)**2.0+2.0*minb(maxdeg)+4.0*minb(nodeInd)**2.0-(12.0*minb(nodeInd))+9.0)/2.0+1.0/2.0,\n    nodeInd <= sqrt(8.0*minb(maxClique)*minb(maxdeg)-(8.0*minb(maxClique)*maxb(nodes))+8.0*minb(maxClique)-(4.0*minb(maxdeg)*maxb(nodes))+4.0*maxb(nodes)**2.0-(4.0*maxb(nodes))+1.0)/2.0+3.0/2.0,\n    maxdeg <= (2.0*minb(maxClique)*maxb(nodes)-(2.0*minb(maxClique))+minb(nodeInd)**2.0-(3.0*minb(nodeInd))-(maxb(nodes)**2.0)+maxb(nodes)+2.0)/(2.0*minb(maxClique)-(maxb(nodes)))\n};\n", "")
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
        if get("regular") == True and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0)):
            if maxb("nodes") != 'undt' and maxb("nodeInd") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("maxClique",  (1.0/2.0)*maxb("nodes")-((minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))/(2.0*(maxb("nodes")-(minb("maxdeg"))-(1.0)))), ind='Max')
                except:
                    pass
            if minb("maxClique") != 'undt' and minb("maxdeg") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("nodes",  minb("maxClique")+minb("maxdeg")/2.0+sqrt(4.0*minb("maxClique")**2.0-(4.0*minb("maxClique")*minb("maxdeg"))-(4.0*minb("maxClique"))+minb("maxdeg")**2.0+2.0*minb("maxdeg")+4.0*minb("nodeInd")**2.0-(12.0*minb("nodeInd"))+9.0)/2.0+1.0/2.0, ind='Min')
                except:
                    pass
            if maxb("maxClique") != 'undt' and maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeInd",  sqrt(8.0*minb("maxClique")*minb("maxdeg")-(8.0*minb("maxClique")*maxb("nodes"))+8.0*minb("maxClique")-(4.0*minb("maxdeg")*maxb("nodes"))+4.0*maxb("nodes")**2.0-(4.0*maxb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
                except:
                    pass
            if maxb("maxClique") != 'undt' and maxb("nodes") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("maxdeg",  (2.0*minb("maxClique")*maxb("nodes")-(2.0*minb("maxClique"))+minb("nodeInd")**2.0-(3.0*minb("nodeInd"))-(maxb("nodes")**2.0)+maxb("nodes")+2.0)/(2.0*minb("maxClique")-(maxb("nodes"))), ind='Max')
                except:
                    pass
        return
class Theorem188(Theorem):
    def __init__(self):
        super(Theorem188, self).__init__(188, "if undefined girth then \n{\n    thickness == 1.0\n}\nelse  \n{\n    thickness >= minb(edges)*(1.0-(2.0/minb(girth)))/(nodes-(2.0)),\n    edges <= minb(girth)*maxb(thickness)*(maxb(nodes)-(2.0))/(minb(girth)-(2.0)),\n    _g is 2.0*minb(edges)/(minb(edges)-(maxb(nodes)*maxb(thickness))+2.0*maxb(thickness)),\n    if _g > 2.0 and _g <= minb(nodes) then \n    {\n        girth <= _g\n    }\n};\n", "")
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
        if minb("girth") == 'undt':
            try:
                set("thickness",  1.0, ind='Min')
            except:
                pass
            try:
                set("thickness",  1.0, ind='Max')
            except:
                pass
        elif True:
            if minb("edges") != 'undt' and minb("girth") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("thickness",  minb("edges")*(1.0-(2.0/minb("girth")))/(maxb("nodes")-(2.0)), ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and minb("thickness") != 'undt' and minb("girth") != 'undt':
                try:
                    set("nodes",  minb("edges")/minb("thickness")-(2.0*minb("edges")/(minb("girth")*minb("thickness")))+2.0, ind='Min')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("thickness") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("edges",  minb("girth")*maxb("thickness")*(maxb("nodes")-(2.0))/(minb("girth")-(2.0)), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("thickness") != 'undt':
                _g = 2.0*minb("edges")/(minb("edges")-(maxb("nodes")*maxb("thickness"))+2.0*maxb("thickness"))
            if ('_g' in vars() and _g > 2.0) and (minb("nodes") != 'undt' and '_g' in vars() and _g <= minb("nodes")):
                try:
                    set("girth",  _g, ind='Max')
                except:
                    pass
        return
class Theorem189(Theorem):
    def __init__(self):
        super(Theorem189, self).__init__(189, "if nodes > 10.0 or nodes < 9.0 then \n{\n    thickness <= (nodes+7.0)/6.0\n}\nelse if nodes == 9.0 or nodes == 10.0 then \n{\n    thickness <= 3.0\n};\n", "")
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
        if (minb("nodes") != 'undt' and minb("nodes") > 10.0) or (maxb("nodes") != 'undt' and maxb("nodes") < 9.0):
            if maxb("nodes") != 'undt':
                try:
                    set("thickness",  (maxb("nodes")+7.0)/6.0, ind='Max')
                except:
                    pass
            if minb("thickness") != 'undt':
                try:
                    set("nodes",  6.0*minb("thickness")-(7.0), ind='Min')
                except:
                    pass
        elif ((minb("nodes") != 'undt' and minb("nodes") >= 9.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 9.0)) or ((minb("nodes") != 'undt' and minb("nodes") >= 10.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 10.0)):
            try:
                set("thickness",  3.0, ind='Max')
            except:
                pass
        return
class Theorem190(Theorem):
    def __init__(self):
        super(Theorem190, self).__init__(190, "thickness <= (1.0/2.0)*(edgeChromatic+1.0);\n", "")
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
        if maxb("edgeChromatic") != 'undt':
            try:
                set("thickness",  (1.0/2.0)*(maxb("edgeChromatic")+1.0), ind='Max')
            except:
                pass
        if minb("thickness") != 'undt':
            try:
                set("edgeChromatic",  2.0*minb("thickness")-(1.0), ind='Min')
            except:
                pass
        return
class Theorem191(Theorem):
    def __init__(self):
        super(Theorem191, self).__init__(191, "thickness <= maximum(bandwidth/2.0, 1.0);\n", "")
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
        if maxb("bandwidth") != 'undt':
            try:
                set("thickness",  maximum(maxb("bandwidth")/2.0, 1.0), ind='Max')
            except:
                pass
        return
class Theorem192(Theorem):
    def __init__(self):
        super(Theorem192, self).__init__(192, "if maxClique == 2.0 then \n{\n    nodeInd >= mindeg*(diameter+4.0)/4.0\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if minb("mindeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodeInd",  minb("mindeg")*(minb("diameter")+4.0)/4.0, ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("mindeg",  4.0*maxb("nodeInd")/(minb("diameter")+4.0), ind='Max')
                except:
                    pass
            if maxb("nodeInd") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("diameter",  -(4.0)+4.0*maxb("nodeInd")/minb("mindeg"), ind='Max')
                except:
                    pass
        return
class Theorem193(Theorem):
    def __init__(self):
        super(Theorem193, self).__init__(193, "thickness <= (1.0/2.0)*(nodeCover+1.0);\n", "")
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
        if maxb("nodeCover") != 'undt':
            try:
                set("thickness",  (1.0/2.0)*(maxb("nodeCover")+1.0), ind='Max')
            except:
                pass
        if minb("thickness") != 'undt':
            try:
                set("nodeCover",  2.0*minb("thickness")-(1.0), ind='Min')
            except:
                pass
        return
class Theorem194(Theorem):
    def __init__(self):
        super(Theorem194, self).__init__(194, "if maxClique == 9.0 or maxClique == 10.0 then \n{\n    thickness >= 3.0\n}\nelse  \n{\n    thickness >= (maxClique+7.0)/6.0\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 9.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 9.0)) or ((minb("maxClique") != 'undt' and minb("maxClique") >= 10.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 10.0)):
            try:
                set("thickness",  3.0, ind='Min')
            except:
                pass
        elif True:
            if minb("maxClique") != 'undt':
                try:
                    set("thickness",  (minb("maxClique")+7.0)/6.0, ind='Min')
                except:
                    pass
            if maxb("thickness") != 'undt':
                try:
                    set("maxClique",  6.0*maxb("thickness")-(7.0), ind='Max')
                except:
                    pass
        return
class Theorem195(Theorem):
    def __init__(self):
        super(Theorem195, self).__init__(195, "\n", "")
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
class Theorem196(Theorem):
    def __init__(self):
        super(Theorem196, self).__init__(196, "nosolve edges <= (nodes/2.0)*(nodes-(1.0))-(maxClique*(nodes-(maxdeg)-(1.0)))-((1.0/2.0)*(nodeInd-(1.0))*(nodeInd-(2.0)));\n", "")
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
        if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt' and maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("edges",  (maxb("nodes")/2.0)*(maxb("nodes")-(1.0))-(minb("maxClique")*(maxb("nodes")-(maxb("maxdeg"))-(1.0)))-((1.0/2.0)*(minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))), ind='Max')
            except:
                pass
        return
class Theorem197(Theorem):
    def __init__(self):
        super(Theorem197, self).__init__(197, "if nodes >= 3.0 then \n{\n    edgeCliqueCover <= thickness*(2.0*maxb(nodes)-(numOfComponents)-(3.0)),\n    nodes >= (minb(edgeCliqueCover)+maxb(thickness)*(minb(numOfComponents)+3.0))/(2.0*maxb(thickness))\n};\n", "")
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
        if (minb("nodes") != 'undt' and minb("nodes") >= 3.0):
            if maxb("thickness") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edgeCliqueCover",  maxb("thickness")*(2.0*maxb("nodes")-(minb("numOfComponents"))-(3.0)), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("thickness",  minb("edgeCliqueCover")/(2.0*maxb("nodes")-(minb("numOfComponents"))-(3.0)), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("edgeCliqueCover") != 'undt' and maxb("thickness") != 'undt':
                try:
                    set("numOfComponents",  2.0*maxb("nodes")-(minb("edgeCliqueCover")/maxb("thickness"))-(3.0), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("thickness") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  (minb("edgeCliqueCover")+maxb("thickness")*(minb("numOfComponents")+3.0))/(2.0*maxb("thickness")), ind='Min')
                except:
                    pass
        return
class Theorem198(Theorem):
    def __init__(self):
        super(Theorem198, self).__init__(198, "nodeCover <= maxb(nodes)-(maxb(nodes)/chromaticNum);\nnodes >= maxb(chromaticNum)*minb(nodeCover)/(maxb(chromaticNum)-(1.0));\n", "")
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
        if maxb("nodes") != 'undt' and maxb("chromaticNum") != 'undt':
            try:
                set("nodeCover",  maxb("nodes")-(maxb("nodes")/maxb("chromaticNum")), ind='Max')
            except:
                pass
        if minb("nodes") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("chromaticNum",  maxb("nodes")/(maxb("nodes")-(minb("nodeCover"))), ind='Min')
            except:
                pass
        if minb("chromaticNum") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("nodes",  maxb("chromaticNum")*minb("nodeCover")/(maxb("chromaticNum")-(1.0)), ind='Min')
            except:
                pass
        return
class Theorem199(Theorem):
    def __init__(self):
        super(Theorem199, self).__init__(199, "bandwidth <= nodes-(1.0)-((nodes-(nodeCover))/2.0);\n", "")
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
        if maxb("nodes") != 'undt' and maxb("nodeCover") != 'undt':
            try:
                set("bandwidth",  maxb("nodes")-(1.0)-((maxb("nodes")-(maxb("nodeCover")))/2.0), ind='Max')
            except:
                pass
        if minb("bandwidth") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("nodes",  2.0*minb("bandwidth")-(maxb("nodeCover"))+2.0, ind='Min')
            except:
                pass
        if minb("bandwidth") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeCover",  2.0*minb("bandwidth")-(maxb("nodes"))+2.0, ind='Min')
            except:
                pass
        return
class Theorem200(Theorem):
    def __init__(self):
        super(Theorem200, self).__init__(200, "if nodes > 2.0*edgeInd+1.0 then \n{\n    nodeCover <= 2.0*edgeInd-(nodeConnec)\n};\n", "")
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
        if (minb("nodes") != 'undt' and maxb("edgeInd") != 'undt' and minb("nodes") > 2.0*maxb("edgeInd")+1.0):
            if maxb("edgeInd") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("nodeCover",  2.0*maxb("edgeInd")-(minb("nodeConnec")), ind='Max')
                except:
                    pass
            if minb("nodeConnec") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("edgeInd",  minb("nodeConnec")/2.0+minb("nodeCover")/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("nodeConnec",  2.0*maxb("edgeInd")-(minb("nodeCover")), ind='Max')
                except:
                    pass
        return
class Theorem201(Theorem):
    def __init__(self):
        super(Theorem201, self).__init__(201, "if nodes >= 6.0 and connected and nodes >= 3.0*edgeInd-(1.0) then \n{\n    nodeCover <= 2.0*edgeInd-(mindeg)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","connected","edgeInd","nodeCover","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt' and minb("nodes") >= 6.0) and get("connected") == True and (minb("nodes") != 'undt' and maxb("edgeInd") != 'undt' and minb("nodes") >= 3.0*maxb("edgeInd")-(1.0)):
            if maxb("edgeInd") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("nodeCover",  2.0*maxb("edgeInd")-(minb("mindeg")), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("edgeInd",  minb("mindeg")/2.0+minb("nodeCover")/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("mindeg",  2.0*maxb("edgeInd")-(minb("nodeCover")), ind='Max')
                except:
                    pass
        return
class Theorem202(Theorem):
    def __init__(self):
        super(Theorem202, self).__init__(202, "if regular then \n{\n    nodeCover >= nodes/2.0+(maxClique-(1.0))*(maxClique-(2.0))/(2.0*mindeg)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeCover","nodes","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True:
            if minb("nodes") != 'undt' and minb("maxClique") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodeCover",  minb("nodes")/2.0+(minb("maxClique")-(1.0))*(minb("maxClique")-(2.0))/(2.0*maxb("mindeg")), ind='Min')
                except:
                    pass
            if maxb("maxClique") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("nodes",  (-(minb("maxClique")**2.0)+3.0*minb("maxClique")+2.0*maxb("mindeg")*maxb("nodeCover")-(2.0))/maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt' and maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxClique",  sqrt(8.0*maxb("mindeg")*maxb("nodeCover")-(4.0*maxb("mindeg")*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
                except:
                    pass
            if minb("maxClique") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("mindeg",  (minb("maxClique")**2.0-(3.0*minb("maxClique"))+2.0)/(2.0*maxb("nodeCover")-(minb("nodes"))), ind='Min')
                except:
                    pass
        return
class Theorem203(Theorem):
    def __init__(self):
        super(Theorem203, self).__init__(203, "if maxClique == 2.0 then \n{\n    nodeCover <= (1.0/2.0)*(2.0*nodes+3.0-(sqrt(8.0*nodes+9.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (1.0/2.0)*(2.0*maxb("nodes")+3.0-(sqrt(8.0*maxb("nodes")+9.0))), ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  minb("nodeCover")+sqrt(8.0*minb("nodeCover")+1.0)/2.0-(1.0/2.0), ind='Min')
                except:
                    pass
        return
class Theorem204(Theorem):
    def __init__(self):
        super(Theorem204, self).__init__(204, "if (minb(maxClique) >= 2.0 and maxb(maxClique) <= 2.0) and maxb(nodes) < 2.0*minb(nodeCover) and maxb(nodeCover) <= 3.0*minb(nodes)/5.0 then \n{\n    nodeCover <= (2.0*maxb(nodes)-(sqrt(5.0*minb(edges)-(maxb(nodes)**2.0))))/5.0,\n    nodes >= 2.0*minb(nodeCover)+sqrt(minb(edges)-(minb(nodeCover)**2.0)),\n    edges <= minb(nodes)**2.0/5.0+(5.0*minb(nodeCover)-(2.0*minb(nodes)))**2.0/5.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","nodeCover","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (maxb("nodes") != 'undt' and minb("nodeCover") != 'undt' and maxb("nodes") < 2.0*minb("nodeCover")) and (maxb("nodeCover") != 'undt' and minb("nodes") != 'undt' and maxb("nodeCover") <= 3.0*minb("nodes")/5.0):
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodeCover",  (2.0*maxb("nodes")-(sqrt(5.0*minb("edges")-(maxb("nodes")**2.0))))/5.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  2.0*minb("nodeCover")+sqrt(minb("edges")-(minb("nodeCover")**2.0)), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("edges",  minb("nodes")**2.0/5.0+(5.0*minb("nodeCover")-(2.0*minb("nodes")))**2.0/5.0, ind='Max')
                except:
                    pass
        return
class Theorem205(Theorem):
    def __init__(self):
        super(Theorem205, self).__init__(205, "if mindeg == 2.0 then \n{\n    edgeCover <= nodes*maximum(4.0, maxdeg)/(2.0+maximum(4.0, maxdeg))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeCover","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("edgeCover",  maxb("nodes")*maximum(4.0, maxb("maxdeg"))/(2.0+maximum(4.0, maxb("maxdeg"))), ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  minb("edgeCover")*(maximum(4.0, minb("maxdeg"))+2.0)/maximum(4.0, minb("maxdeg")), ind='Min')
                except:
                    pass
        return
class Theorem206(Theorem):
    def __init__(self):
        super(Theorem206, self).__init__(206, "nosolve nodeCover <= (nodes*maxdeg+1.0)/(maxdeg+1.0)-(1.0/(mindeg+1.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodeCover",  (maxb("nodes")*maxb("maxdeg")+1.0)/(maxb("maxdeg")+1.0)-(1.0/(maxb("mindeg")+1.0)), ind='Max')
            except:
                pass
        return
class Theorem207(Theorem):
    def __init__(self):
        super(Theorem207, self).__init__(207, "if maxClique == 2.0 then \n{\n    if maxdeg >= 3.0 then \n    {\n        nodeCover <= nodes*(maxdeg-((6.0/5.0)/(maxdeg-(1.0/5.0))))\n    }\n    else if nodes >= 3.0 and connected and not complete and not cycle or (cycle and isset nodes and even nodes) then \n    {\n        nosolve nodeCover <= nodes*(maxdeg-(1.0))/maxdeg+1.0/(maxdeg+1.0)-(1.0/(mindeg+1.0))\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","nodeCover","nodes","connected","complete","cycle","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
                if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("nodeCover",  maxb("nodes")*(maxb("maxdeg")-((6.0/5.0)/(maxb("maxdeg")-(1.0/5.0)))), ind='Max')
                    except:
                        pass
                if minb("nodeCover") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  minb("nodeCover")*(-(5.0*minb("maxdeg"))+1.0)/(-(5.0*minb("maxdeg")**2.0)+minb("maxdeg")+6.0), ind='Min')
                    except:
                        pass
                if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                    try:
                        set("maxdeg",  (5.0*minb("nodeCover")+minb("nodes")+sqrt(25.0*minb("nodeCover")**2.0-(10.0*minb("nodeCover")*minb("nodes"))+121.0*minb("nodes")**2.0))/(10.0*minb("nodes")), ind='Min')
                    except:
                        pass
            elif (minb("nodes") != 'undt' and minb("nodes") >= 3.0) and get("connected") == True and get("complete") == False and get("cycle") == False or (get("cycle") == True and maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and evenInvar("nodes")):
                if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
                    try:
                        set("nodeCover",  maxb("nodes")*(maxb("maxdeg")-(1.0))/maxb("maxdeg")+1.0/(maxb("maxdeg")+1.0)-(1.0/(maxb("mindeg")+1.0)), ind='Max')
                    except:
                        pass
        return
class Theorem208(Theorem):
    def __init__(self):
        super(Theorem208, self).__init__(208, "if connected and not complete then \n{\n    nodeCover <= (2.0*edges*nodes*nodes-(3.0*nodes)-(1.0))/(2.0*edges*nodes+nodes*nodes)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","complete","nodeCover","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and get("complete") == False:
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  (2.0*maxb("edges")*maxb("nodes")*maxb("nodes")-(3.0*maxb("nodes"))-(1.0))/(2.0*maxb("edges")*maxb("nodes")+maxb("nodes")*maxb("nodes")), ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  -((minb("nodeCover")*maxb("nodes")**2.0+3.0*maxb("nodes")+1.0)/(2.0*maxb("nodes")*(minb("nodeCover")-(maxb("nodes"))))), ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  (2.0*minb("edges")*minb("nodeCover")+sqrt(4.0*minb("edges")**2.0*minb("nodeCover")**2.0+12.0*minb("edges")*minb("nodeCover")+8.0*minb("edges")-(4.0*minb("nodeCover"))+9.0)+3.0)/(2.0*(2.0*minb("edges")-(minb("nodeCover")))), ind='Min')
                except:
                    pass
        return
class Theorem209(Theorem):
    def __init__(self):
        super(Theorem209, self).__init__(209, "nodeCover <= maxb(nodes)*(1.0-(2.0/(maxb(maxdeg)+maxb(maxClique)+1.0)));\nnodes >= minb(nodeCover)*(maxb(maxClique)+minb(maxdeg)+1.0)/(maxb(maxClique)+minb(maxdeg)-(1.0));\nmaxdeg >= (-(minb(maxClique)*minb(nodeCover))+minb(maxClique)*maxb(nodes)-(minb(nodeCover))-(maxb(nodes)))/(minb(nodeCover)-(maxb(nodes)));\nmaxClique >= (-(maxb(maxdeg)*minb(nodeCover))+maxb(maxdeg)*minb(nodes)-(minb(nodeCover))-(minb(nodes)))/(minb(nodeCover)-(minb(nodes)));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("nodeCover",  maxb("nodes")*(1.0-(2.0/(maxb("maxdeg")+maxb("maxClique")+1.0))), ind='Max')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("maxClique") != 'undt' and minb("maxdeg") != 'undt':
            try:
                set("nodes",  minb("nodeCover")*(maxb("maxClique")+minb("maxdeg")+1.0)/(maxb("maxClique")+minb("maxdeg")-(1.0)), ind='Min')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  (-(minb("maxClique")*minb("nodeCover"))+minb("maxClique")*maxb("nodes")-(minb("nodeCover"))-(maxb("nodes")))/(minb("nodeCover")-(maxb("nodes"))), ind='Min')
            except:
                pass
        if minb("maxdeg") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxClique",  (-(maxb("maxdeg")*minb("nodeCover"))+maxb("maxdeg")*minb("nodes")-(minb("nodeCover"))-(minb("nodes")))/(minb("nodeCover")-(minb("nodes"))), ind='Min')
            except:
                pass
        return
class Theorem210(Theorem):
    def __init__(self):
        super(Theorem210, self).__init__(210, "nosolve nodeCover <= (nodes-(2.0))*(maxdeg+maxClique+mindeg-(1.0))/(maxdeg+1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","maxClique","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("maxClique") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodeCover",  (maxb("nodes")-(2.0))*(maxb("maxdeg")+maxb("maxClique")+maxb("mindeg")-(1.0))/(maxb("maxdeg")+1.0), ind='Max')
            except:
                pass
        return
class Theorem211(Theorem):
    def __init__(self):
        super(Theorem211, self).__init__(211, "if nodeCover > nodes-(nodeCliqueCover) then \n{\n    nodeCover <= nodes*maxb(maxdeg)/(maxb(maxdeg)+1.0)-(1.0/3.0),\n    maxdeg >= -((3.0*minb(nodeCover)+1.0)/(3.0*minb(nodeCover)-(3.0*maxb(nodes))+1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","nodeCliqueCover","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeCover") != 'undt' and maxb("nodes") != 'undt' and maxb("nodeCliqueCover") != 'undt' and minb("nodeCover") > maxb("nodes")-(minb("nodeCliqueCover"))):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodeCover",  maxb("nodes")*maxb("maxdeg")/(maxb("maxdeg")+1.0)-(1.0/3.0), ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  minb("nodeCover")+1.0/3.0+minb("nodeCover")/maxb("maxdeg")+1.0/(3.0*maxb("maxdeg")), ind='Min')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxdeg",  -((3.0*minb("nodeCover")+1.0)/(3.0*minb("nodeCover")-(3.0*maxb("nodes"))+1.0)), ind='Min')
                except:
                    pass
        return
class Theorem212(Theorem):
    def __init__(self):
        super(Theorem212, self).__init__(212, "nodeCliqueCover <= edgeCover;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeCover") != 'undt':
            try:
                set("nodeCliqueCover",  maxb("edgeCover"), ind='Max')
            except:
                pass
        if minb("nodeCliqueCover") != 'undt':
            try:
                set("edgeCover",  minb("nodeCliqueCover"), ind='Min')
            except:
                pass
        return
class Theorem213(Theorem):
    def __init__(self):
        super(Theorem213, self).__init__(213, "domination <= nodeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeInd") != 'undt':
            try:
                set("domination",  maxb("nodeInd"), ind='Max')
            except:
                pass
        if minb("domination") != 'undt':
            try:
                set("nodeInd",  minb("domination"), ind='Min')
            except:
                pass
        return
class Theorem214(Theorem):
    def __init__(self):
        super(Theorem214, self).__init__(214, "domination <= edgeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["domination","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeInd") != 'undt':
            try:
                set("domination",  maxb("edgeInd"), ind='Max')
            except:
                pass
        if minb("domination") != 'undt':
            try:
                set("edgeInd",  minb("domination"), ind='Min')
            except:
                pass
        return
class Theorem215(Theorem):
    def __init__(self):
        super(Theorem215, self).__init__(215, "numOfComponents <= domination;\n", "")
    def involves(self, str_invar):
        return str_invar in ["numOfComponents","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("domination") != 'undt':
            try:
                set("numOfComponents",  maxb("domination"), ind='Max')
            except:
                pass
        if minb("numOfComponents") != 'undt':
            try:
                set("domination",  minb("numOfComponents"), ind='Min')
            except:
                pass
        return
class Theorem216(Theorem):
    def __init__(self):
        super(Theorem216, self).__init__(216, "maxdeg <= edgeChromatic;\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeChromatic") != 'undt':
            try:
                set("maxdeg",  maxb("edgeChromatic"), ind='Max')
            except:
                pass
        if minb("maxdeg") != 'undt':
            try:
                set("edgeChromatic",  minb("maxdeg"), ind='Min')
            except:
                pass
        return
class Theorem217(Theorem):
    def __init__(self):
        super(Theorem217, self).__init__(217, "edgeChromatic <= maxdeg+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
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
class Theorem218(Theorem):
    def __init__(self):
        super(Theorem218, self).__init__(218, "mindeg <= nodeCover;\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt':
            try:
                set("mindeg",  maxb("nodeCover"), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt':
            try:
                set("nodeCover",  minb("mindeg"), ind='Min')
            except:
                pass
        return
class Theorem219(Theorem):
    def __init__(self):
        super(Theorem219, self).__init__(219, "edgeConnec <= mindeg;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("mindeg") != 'undt':
            try:
                set("edgeConnec",  maxb("mindeg"), ind='Max')
            except:
                pass
        if minb("edgeConnec") != 'undt':
            try:
                set("mindeg",  minb("edgeConnec"), ind='Min')
            except:
                pass
        return
class Theorem220(Theorem):
    def __init__(self):
        super(Theorem220, self).__init__(220, "maxClique <= chromaticNum;\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("chromaticNum") != 'undt':
            try:
                set("maxClique",  maxb("chromaticNum"), ind='Max')
            except:
                pass
        if minb("maxClique") != 'undt':
            try:
                set("chromaticNum",  minb("maxClique"), ind='Min')
            except:
                pass
        return
class Theorem221(Theorem):
    def __init__(self):
        super(Theorem221, self).__init__(221, "chromaticNum <= nodeCover+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt':
            try:
                set("chromaticNum",  maxb("nodeCover")+1.0, ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("nodeCover",  minb("chromaticNum")-(1.0), ind='Min')
            except:
                pass
        return
class Theorem222(Theorem):
    def __init__(self):
        super(Theorem222, self).__init__(222, "edgeInd <= nodeCover;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt':
            try:
                set("edgeInd",  maxb("nodeCover"), ind='Max')
            except:
                pass
        if minb("edgeInd") != 'undt':
            try:
                set("nodeCover",  minb("edgeInd"), ind='Min')
            except:
                pass
        return
class Theorem225(Theorem):
    def __init__(self):
        super(Theorem225, self).__init__(225, "radius <= diameter;\n", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("diameter") != 'undt':
            try:
                set("radius",  maxb("diameter"), ind='Max')
            except:
                pass
        if minb("radius") != 'undt':
            try:
                set("diameter",  minb("radius"), ind='Min')
            except:
                pass
        return
class Theorem224(Theorem):
    def __init__(self):
        super(Theorem224, self).__init__(224, "nodeCliqueCover <= edgeCliqueCover;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","edgeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeCliqueCover") != 'undt':
            try:
                set("nodeCliqueCover",  maxb("edgeCliqueCover"), ind='Max')
            except:
                pass
        if minb("nodeCliqueCover") != 'undt':
            try:
                set("edgeCliqueCover",  minb("nodeCliqueCover"), ind='Min')
            except:
                pass
        return
class Theorem225(Theorem):
    def __init__(self):
        super(Theorem225, self).__init__(225, "radius <= diam;\n", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diam"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("diam") != 'undt':
            try:
                set("radius",  maxb("diam"), ind='Max')
            except:
                pass
        if minb("radius") != 'undt':
            try:
                set("diam",  minb("radius"), ind='Min')
            except:
                pass
        return
class Theorem226(Theorem):
    def __init__(self):
        super(Theorem226, self).__init__(226, "nodeConnec <= edgeConnec;\n", "")
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
        if maxb("edgeConnec") != 'undt':
            try:
                set("nodeConnec",  maxb("edgeConnec"), ind='Max')
            except:
                pass
        if minb("nodeConnec") != 'undt':
            try:
                set("edgeConnec",  minb("nodeConnec"), ind='Min')
            except:
                pass
        return
class Theorem227(Theorem):
    def __init__(self):
        super(Theorem227, self).__init__(227, "girth <= circumference;\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("circumference") != 'undt':
            try:
                set("girth",  maxb("circumference"), ind='Max')
            except:
                pass
        if minb("girth") != 'undt':
            try:
                set("circumference",  minb("girth"), ind='Min')
            except:
                pass
        return
class Theorem228(Theorem):
    def __init__(self):
        super(Theorem228, self).__init__(228, "chromaticNum <= circumference;\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("circumference") != 'undt':
            try:
                set("chromaticNum",  maxb("circumference"), ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("circumference",  minb("chromaticNum"), ind='Min')
            except:
                pass
        return
class Theorem229(Theorem):
    def __init__(self):
        super(Theorem229, self).__init__(229, "genus <= crossing;\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","crossing"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("crossing") != 'undt':
            try:
                set("genus",  maxb("crossing"), ind='Max')
            except:
                pass
        if minb("genus") != 'undt':
            try:
                set("crossing",  minb("genus"), ind='Min')
            except:
                pass
        return
class Theorem230(Theorem):
    def __init__(self):
        super(Theorem230, self).__init__(230, "mindeg <= circumference-(1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("circumference") != 'undt':
            try:
                set("mindeg",  maxb("circumference")-(1.0), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt':
            try:
                set("circumference",  minb("mindeg")+1.0, ind='Min')
            except:
                pass
        return
class Theorem231(Theorem):
    def __init__(self):
        super(Theorem231, self).__init__(231, "chromaticNum <= bandwidth+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("bandwidth") != 'undt':
            try:
                set("chromaticNum",  maxb("bandwidth")+1.0, ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("bandwidth",  minb("chromaticNum")-(1.0), ind='Min')
            except:
                pass
        return
class Theorem232(Theorem):
    def __init__(self):
        super(Theorem232, self).__init__(232, "mindeg <= bandwidth;\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("bandwidth") != 'undt':
            try:
                set("mindeg",  maxb("bandwidth"), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt':
            try:
                set("bandwidth",  minb("mindeg"), ind='Min')
            except:
                pass
        return
class Theorem233(Theorem):
    def __init__(self):
        super(Theorem233, self).__init__(233, "nodes <= nodeInd*chromaticNum;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeInd","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeInd") != 'undt' and maxb("chromaticNum") != 'undt':
            try:
                set("nodes",  maxb("nodeInd")*maxb("chromaticNum"), ind='Max')
            except:
                pass
        if minb("nodes") != 'undt' and minb("chromaticNum") != 'undt':
            try:
                set("nodeInd",  minb("nodes")/maxb("chromaticNum"), ind='Min')
            except:
                pass
        if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("chromaticNum",  minb("nodes")/maxb("nodeInd"), ind='Min')
            except:
                pass
        return
class Theorem234(Theorem):
    def __init__(self):
        super(Theorem234, self).__init__(234, "nodes <= nodeCliqueCover*maxClique;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCliqueCover","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCliqueCover") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("nodes",  maxb("nodeCliqueCover")*maxb("maxClique"), ind='Max')
            except:
                pass
        if minb("nodes") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("nodeCliqueCover",  minb("nodes")/maxb("maxClique"), ind='Min')
            except:
                pass
        if minb("nodes") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("maxClique",  minb("nodes")/maxb("nodeCliqueCover"), ind='Min')
            except:
                pass
        return
class Theorem235(Theorem):
    def __init__(self):
        super(Theorem235, self).__init__(235, "edges <= edgeChromatic*edgeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","edgeChromatic","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeChromatic") != 'undt' and maxb("edgeInd") != 'undt':
            try:
                set("edges",  maxb("edgeChromatic")*maxb("edgeInd"), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and minb("edgeInd") != 'undt':
            try:
                set("edgeChromatic",  minb("edges")/maxb("edgeInd"), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("edgeChromatic") != 'undt':
            try:
                set("edgeInd",  minb("edges")/maxb("edgeChromatic"), ind='Min')
            except:
                pass
        return
class Theorem236(Theorem):
    def __init__(self):
        super(Theorem236, self).__init__(236, "edges <= nodeCover*maxdeg;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCover") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("edges",  maxb("nodeCover")*maxb("maxdeg"), ind='Max')
            except:
                pass
        if minb("edges") != 'undt' and minb("maxdeg") != 'undt':
            try:
                set("nodeCover",  minb("edges")/maxb("maxdeg"), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("maxdeg",  minb("edges")/maxb("nodeCover"), ind='Min')
            except:
                pass
        return
class Theorem237(Theorem):
    def __init__(self):
        super(Theorem237, self).__init__(237, "nodeCover <= bandwidth*nodeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","bandwidth","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("bandwidth") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodeCover",  maxb("bandwidth")*maxb("nodeInd"), ind='Max')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("bandwidth",  minb("nodeCover")/maxb("nodeInd"), ind='Min')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("bandwidth") != 'undt':
            try:
                set("nodeInd",  minb("nodeCover")/maxb("bandwidth"), ind='Min')
            except:
                pass
        return
class Theorem238(Theorem):
    def __init__(self):
        super(Theorem238, self).__init__(238, "chromaticNum <= spectralRadius+1.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","spectralRadius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("spectralRadius") != 'undt':
            try:
                set("chromaticNum",  maxb("spectralRadius")+1.0, ind='Max')
            except:
                pass
        if minb("chromaticNum") != 'undt':
            try:
                set("spectralRadius",  minb("chromaticNum")-(1.0), ind='Min')
            except:
                pass
        return
class Theorem239(Theorem):
    def __init__(self):
        super(Theorem239, self).__init__(239, "nodes == nodeCover+nodeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCover","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodeCover") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("nodes",  minb("nodeCover")+minb("nodeInd"), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("nodeCover",  -(minb("nodeInd"))+maxb("nodes"), ind='Max')
            except:
                pass
        if maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("nodeInd",  -(minb("nodeCover"))+maxb("nodes"), ind='Max')
            except:
                pass
        if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodes",  maxb("nodeCover")+maxb("nodeInd"), ind='Max')
            except:
                pass
        if minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeCover",  -(maxb("nodeInd"))+minb("nodes"), ind='Min')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeInd",  -(maxb("nodeCover"))+minb("nodes"), ind='Min')
            except:
                pass
        return
class Theorem240(Theorem):
    def __init__(self):
        super(Theorem240, self).__init__(240, "nodes == edgeCover+edgeInd;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeCover","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("edgeCover") != 'undt' and minb("edgeInd") != 'undt':
            try:
                set("nodes",  minb("edgeCover")+minb("edgeInd"), ind='Min')
            except:
                pass
        if maxb("edgeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edgeCover",  -(minb("edgeInd"))+maxb("nodes"), ind='Max')
            except:
                pass
        if maxb("edgeCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edgeInd",  -(minb("edgeCover"))+maxb("nodes"), ind='Max')
            except:
                pass
        if maxb("edgeCover") != 'undt' and maxb("edgeInd") != 'undt':
            try:
                set("nodes",  maxb("edgeCover")+maxb("edgeInd"), ind='Max')
            except:
                pass
        if minb("edgeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edgeCover",  -(maxb("edgeInd"))+minb("nodes"), ind='Min')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edgeInd",  -(maxb("edgeCover"))+minb("nodes"), ind='Min')
            except:
                pass
        return
class Theorem241(Theorem):
    def __init__(self):
        super(Theorem241, self).__init__(241, "if maxClique == 2.0 then \n{\n    chromaticNum <= 3.0*(nodes+12.0)/16.0\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodes") != 'undt':
                try:
                    set("chromaticNum",  3.0*(maxb("nodes")+12.0)/16.0, ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("nodes",  16.0*minb("chromaticNum")/3.0-(12.0), ind='Min')
                except:
                    pass
        return
class Theorem242(Theorem):
    def __init__(self):
        super(Theorem242, self).__init__(242, "nodes >= nodeCliqueCover+chromaticNum-(1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCliqueCover","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodeCliqueCover") != 'undt' and minb("chromaticNum") != 'undt':
            try:
                set("nodes",  minb("nodeCliqueCover")+minb("chromaticNum")-(1.0), ind='Min')
            except:
                pass
        if maxb("chromaticNum") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("nodeCliqueCover",  -(minb("chromaticNum"))+maxb("nodes")+1.0, ind='Max')
            except:
                pass
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("chromaticNum",  -(minb("nodeCliqueCover"))+maxb("nodes")+1.0, ind='Max')
            except:
                pass
        return
class Theorem243(Theorem):
    def __init__(self):
        super(Theorem243, self).__init__(243, "nodes >= maxdeg+domination;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxdeg","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("maxdeg") != 'undt' and minb("domination") != 'undt':
            try:
                set("nodes",  minb("maxdeg")+minb("domination"), ind='Min')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxdeg",  -(minb("domination"))+maxb("nodes"), ind='Max')
            except:
                pass
        if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("domination",  -(minb("maxdeg"))+maxb("nodes"), ind='Max')
            except:
                pass
        return
class Theorem244(Theorem):
    def __init__(self):
        super(Theorem244, self).__init__(244, "if nodeInd == 2.0 then \n{\n    nodeCliqueCover <= 3.0*(nodes+12.0)/16.0\n};\n", "")
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
        if ((minb("nodeInd") != 'undt' and minb("nodeInd") >= 2.0) and (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0)):
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCliqueCover",  3.0*(maxb("nodes")+12.0)/16.0, ind='Max')
                except:
                    pass
            if minb("nodeCliqueCover") != 'undt':
                try:
                    set("nodes",  16.0*minb("nodeCliqueCover")/3.0-(12.0), ind='Min')
                except:
                    pass
        return
class Theorem245(Theorem):
    def __init__(self):
        super(Theorem245, self).__init__(245, "if mindeg >= 2.0 then \n{\n    edgeCliqueCover <= 2.0*(nodes-(2.0)+2.0*genus)-(4.0*(numOfComponents-(1.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeCliqueCover","nodes","genus","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 2.0):
            if maxb("nodes") != 'undt' and maxb("genus") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edgeCliqueCover",  2.0*(maxb("nodes")-(2.0)+2.0*maxb("genus"))-(4.0*(minb("numOfComponents")-(1.0))), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("genus") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  minb("edgeCliqueCover")/2.0-(2.0*maxb("genus"))+2.0*minb("numOfComponents"), ind='Min')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("genus",  minb("edgeCliqueCover")/4.0-(maxb("nodes")/2.0)+minb("numOfComponents"), ind='Min')
                except:
                    pass
            if maxb("edgeCliqueCover") != 'undt' and maxb("genus") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(minb("edgeCliqueCover")/4.0)+maxb("genus")+maxb("nodes")/2.0, ind='Max')
                except:
                    pass
        return
class Theorem246(Theorem):
    def __init__(self):
        super(Theorem246, self).__init__(246, "if nodes >= 3.0 then \n{\n    edgeCliqueCover <= 2.0*(nodes-(2.0)+2.0*genus)-(numOfComponents-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeCliqueCover","genus","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt' and minb("nodes") >= 3.0):
            if maxb("nodes") != 'undt' and maxb("genus") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edgeCliqueCover",  2.0*(maxb("nodes")-(2.0)+2.0*maxb("genus"))-(minb("numOfComponents")-(1.0)), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("genus") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  minb("edgeCliqueCover")/2.0-(2.0*maxb("genus"))+minb("numOfComponents")/2.0+3.0/2.0, ind='Min')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("genus",  minb("edgeCliqueCover")/4.0-(maxb("nodes")/2.0)+minb("numOfComponents")/4.0+3.0/4.0, ind='Min')
                except:
                    pass
            if maxb("edgeCliqueCover") != 'undt' and maxb("genus") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(minb("edgeCliqueCover"))+4.0*maxb("genus")+2.0*maxb("nodes")-(3.0), ind='Max')
                except:
                    pass
        return
class Theorem247(Theorem):
    def __init__(self):
        super(Theorem247, self).__init__(247, "nodeInd <= maxb(nodes)/(1.0+minb(mindeg)/maxb(maxdeg));\nnodes >= minb(nodeInd)*(maxb(maxdeg)+minb(mindeg))/maxb(maxdeg);\nmindeg <= maxb(maxdeg)*(-(minb(nodeInd))+maxb(nodes))/minb(nodeInd);\nmaxdeg >= -(minb(mindeg)*minb(nodeInd)/(minb(nodeInd)-(maxb(nodes))));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","mindeg","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("nodeInd",  maxb("nodes")/(1.0+minb("mindeg")/maxb("maxdeg")), ind='Max')
            except:
                pass
        if minb("nodeInd") != 'undt' and minb("maxdeg") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodes",  minb("nodeInd")*(maxb("maxdeg")+minb("mindeg"))/maxb("maxdeg"), ind='Min')
            except:
                pass
        if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("mindeg",  maxb("maxdeg")*(-(minb("nodeInd"))+maxb("nodes"))/minb("nodeInd"), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  -(minb("mindeg")*minb("nodeInd")/(minb("nodeInd")-(maxb("nodes")))), ind='Min')
            except:
                pass
        return
class Theorem248(Theorem):
    def __init__(self):
        super(Theorem248, self).__init__(248, "nodeCover >= minb(nodes)/(1.0+maxb(maxdeg)/minb(mindeg));\nnodes <= maxb(nodeCover)*(maxb(maxdeg)+minb(mindeg))/minb(mindeg);\nmaxdeg >= minb(mindeg)*(-(maxb(nodeCover))+minb(nodes))/maxb(nodeCover);\nmindeg <= -(maxb(maxdeg)*maxb(nodeCover)/(maxb(nodeCover)-(minb(nodes))));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","maxdeg","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodeCover",  minb("nodes")/(1.0+maxb("maxdeg")/minb("mindeg")), ind='Min')
            except:
                pass
        if maxb("nodeCover") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodes",  maxb("nodeCover")*(maxb("maxdeg")+minb("mindeg"))/minb("mindeg"), ind='Max')
            except:
                pass
        if minb("mindeg") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("maxdeg",  minb("mindeg")*(-(maxb("nodeCover"))+minb("nodes"))/maxb("nodeCover"), ind='Min')
            except:
                pass
        if maxb("maxdeg") != 'undt' and maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("mindeg",  -(maxb("maxdeg")*maxb("nodeCover")/(maxb("nodeCover")-(minb("nodes")))), ind='Max')
            except:
                pass
        return
class Theorem249(Theorem):
    def __init__(self):
        super(Theorem249, self).__init__(249, "nodeInd >= nodes/(bandwidth+1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("bandwidth") != 'undt':
            try:
                set("nodeInd",  minb("nodes")/(maxb("bandwidth")+1.0), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("bandwidth") != 'undt':
            try:
                set("nodes",  maxb("nodeInd")*(maxb("bandwidth")+1.0), ind='Max')
            except:
                pass
        if minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("bandwidth",  (-(maxb("nodeInd"))+minb("nodes"))/maxb("nodeInd"), ind='Min')
            except:
                pass
        return
class Theorem250(Theorem):
    def __init__(self):
        super(Theorem250, self).__init__(250, "nodeCover <= (nodes)/(1.0+1.0/maxb(bandwidth));\nbandwidth >= -(minb(nodeCover)/(minb(nodeCover)-(maxb(nodes))));\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("bandwidth") != 'undt':
            try:
                set("nodeCover",  (maxb("nodes"))/(1.0+1.0/maxb("bandwidth")), ind='Max')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("bandwidth") != 'undt':
            try:
                set("nodes",  minb("nodeCover")+minb("nodeCover")/maxb("bandwidth"), ind='Min')
            except:
                pass
        if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("bandwidth",  -(minb("nodeCover")/(minb("nodeCover")-(maxb("nodes")))), ind='Min')
            except:
                pass
        return
class Theorem251(Theorem):
    def __init__(self):
        super(Theorem251, self).__init__(251, "if defined girth then \n{\n    edges >= (girth-(1.0))*(arboricity-(1.0))**2.0+(arboricity-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","edges","arboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt':
            if minb("girth") != 'undt' and minb("arboricity") != 'undt':
                try:
                    set("edges",  (minb("girth")-(1.0))*(minb("arboricity")-(1.0))**2.0+(minb("arboricity")-(1.0)), ind='Min')
                except:
                    pass
            if maxb("arboricity") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("girth",  (-(minb("arboricity"))+maxb("edges")+(minb("arboricity")-(1.0))**2.0+1.0)/(minb("arboricity")-(1.0))**2.0, ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("arboricity",  (2.0*maxb("girth")+sqrt(4.0*maxb("edges")*maxb("girth")-(4.0*maxb("edges"))+1.0)-(3.0))/(2.0*(maxb("girth")-(1.0))), ind='Max')
                except:
                    pass
        return
class Theorem252(Theorem):
    def __init__(self):
        super(Theorem252, self).__init__(252, "if nodeConnec >= 2.0 and girth >= 4.0 then \n{\n    if istrue congruent(girth, 1.0, 4.0) then \n    {\n        edgeInd >= maxdeg*(girth-(4.0))/4.0\n    }\n    else if istrue congruent(girth, 2.0, 4.0) or (maxdeg == 2.0 and istrue congruent(girth, 3.0, 4.0)) then \n    {\n        edgeInd >= maxdeg*(girth-(4.0))/4.0+1.0\n    }\n    else if (istrue congruent(girth, 0.0, 4.0) or (istrue congruent(girth, 3.0, 4.0) and maxdeg >= 3.0)) then \n    {\n        edgeInd >= maxdeg*(girth-(4.0))/4.0+2.0\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","girth","edgeInd","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (minb("girth") != 'undt' and minb("girth") >= 4.0):
            if congruent("girth", 1.0, 4.0):
                if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                    try:
                        set("edgeInd",  minb("maxdeg")*(minb("girth")-(4.0))/4.0, ind='Min')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("girth") != 'undt':
                    try:
                        set("maxdeg",  4.0*maxb("edgeInd")/(minb("girth")-(4.0)), ind='Max')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("girth",  4.0*maxb("edgeInd")/minb("maxdeg")+4.0, ind='Max')
                    except:
                        pass
            elif congruent("girth", 2.0, 4.0) or (((minb("maxdeg") != 'undt' and minb("maxdeg") >= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0)) and congruent("girth", 3.0, 4.0)):
                if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                    try:
                        set("edgeInd",  minb("maxdeg")*(minb("girth")-(4.0))/4.0+1.0, ind='Min')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("girth") != 'undt':
                    try:
                        set("maxdeg",  4.0*(maxb("edgeInd")-(1.0))/(minb("girth")-(4.0)), ind='Max')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("girth",  4.0*(maxb("edgeInd")+maxb("maxdeg")-(1.0))/maxb("maxdeg"), ind='Max')
                    except:
                        pass
            elif (congruent("girth", 0.0, 4.0) or (congruent("girth", 3.0, 4.0) and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0))):
                if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                    try:
                        set("edgeInd",  minb("maxdeg")*(minb("girth")-(4.0))/4.0+2.0, ind='Min')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("girth") != 'undt':
                    try:
                        set("maxdeg",  4.0*(maxb("edgeInd")-(2.0))/(minb("girth")-(4.0)), ind='Max')
                    except:
                        pass
                if maxb("edgeInd") != 'undt' and maxb("maxdeg") != 'undt':
                    try:
                        set("girth",  4.0*(maxb("edgeInd")+maxb("maxdeg")-(2.0))/maxb("maxdeg"), ind='Max')
                    except:
                        pass
        return
class Theorem253(Theorem):
    def __init__(self):
        super(Theorem253, self).__init__(253, "if nodeConnec >= 1.0 then \n{\n    maxdeg <= (nodes-(1.0))/((girth-(4.0))/4.0*(nodeConnec-(1.0))+1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","maxdeg","nodes","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 1.0):
            if maxb("nodes") != 'undt' and maxb("girth") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("maxdeg",  (maxb("nodes")-(1.0))/((minb("girth")-(4.0))/4.0*(minb("nodeConnec")-(1.0))+1.0), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and minb("maxdeg") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("nodes",  minb("girth")*minb("maxdeg")*minb("nodeConnec")/4.0-(minb("girth")*minb("maxdeg")/4.0)-(minb("maxdeg")*minb("nodeConnec"))+2.0*minb("maxdeg")+1.0, ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("girth",  4.0*(minb("maxdeg")*maxb("nodeConnec")-(2.0*minb("maxdeg"))+maxb("nodes")-(1.0))/(minb("maxdeg")*(maxb("nodeConnec")-(1.0))), ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeConnec",  (maxb("girth")*minb("maxdeg")-(8.0*minb("maxdeg"))+4.0*maxb("nodes")-(4.0))/(minb("maxdeg")*(maxb("girth")-(4.0))), ind='Max')
                except:
                    pass
        return
class Theorem254(Theorem):
    def __init__(self):
        super(Theorem254, self).__init__(254, "if nodeInd == 2.0 then \n{\n    if mindeg == 1.0 or nodes <= 4.0 then \n    {\n        nodeCliqueCover <= 2.0\n    }\n    else if nodes >= 5.0 and nodes <= 10.0 then \n    {\n        nodeInd <= 3.0\n    }\n    else  \n    {\n        nodeCliqueCover <= (mindeg+11.0)/4.0\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","nodeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("nodeInd") != 'undt' and minb("nodeInd") >= 2.0) and (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0)):
            if ((minb("mindeg") != 'undt' and minb("mindeg") >= 1.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 1.0)) or (maxb("nodes") != 'undt' and maxb("nodes") <= 4.0):
                try:
                    set("nodeCliqueCover",  2.0, ind='Max')
                except:
                    pass
            elif (minb("nodes") != 'undt' and minb("nodes") >= 5.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 10.0):
                try:
                    set("nodeInd",  3.0, ind='Max')
                except:
                    pass
            elif True:
                if maxb("mindeg") != 'undt':
                    try:
                        set("nodeCliqueCover",  (maxb("mindeg")+11.0)/4.0, ind='Max')
                    except:
                        pass
                if minb("nodeCliqueCover") != 'undt':
                    try:
                        set("mindeg",  4.0*minb("nodeCliqueCover")-(11.0), ind='Min')
                    except:
                        pass
        return
class Theorem255(Theorem):
    def __init__(self):
        super(Theorem255, self).__init__(255, "if connected then \n{\n    edges >= nodes+8.0*thickness-(13.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","edges","nodes","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if minb("nodes") != 'undt' and minb("thickness") != 'undt':
                try:
                    set("edges",  minb("nodes")+8.0*minb("thickness")-(13.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("thickness") != 'undt':
                try:
                    set("nodes",  maxb("edges")-(8.0*minb("thickness"))+13.0, ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("thickness",  maxb("edges")/8.0-(minb("nodes")/8.0)+13.0/8.0, ind='Max')
                except:
                    pass
        return
class Theorem256(Theorem):
    def __init__(self):
        super(Theorem256, self).__init__(256, "\n", "")
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
class Theorem257(Theorem):
    def __init__(self):
        super(Theorem257, self).__init__(257, "if (even diameter and minb(nodeConnec) >= 2.0) then \n{\n    _k is 2.0\n}\nelse  \n{\n    _k is 1.0\n};\nif minb(diam) >= 3.0 then \n{\n    edgeInd >= (nodeConnec)*(minb(diameter)-(1.0))/2.0+_k,\n    diameter <= (-(2.0*_k)+2.0*maxb(edgeInd)+minb(nodeConnec))/minb(nodeConnec)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","diam","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (evenInvar("diameter") and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0)):
            _k = 2.0
        elif True:
            _k = 1.0
        if (minb("diam") != 'undt' and minb("diam") >= 3.0):
            if minb("nodeConnec") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("edgeInd",  (minb("nodeConnec"))*(minb("diameter")-(1.0))/2.0+_k, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("nodeConnec",  2.0*(-(_k)+maxb("edgeInd"))/(minb("diameter")-(1.0)), ind='Max')
                except:
                    pass
            if maxb("edgeInd") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("diameter",  (-(2.0*_k)+2.0*maxb("edgeInd")+minb("nodeConnec"))/minb("nodeConnec"), ind='Max')
                except:
                    pass
        return
class Theorem258(Theorem):
    def __init__(self):
        super(Theorem258, self).__init__(258, "if ((nodeConnec > 0.0 and nodes > 2.0) or mindeg > 1.0) and ((thickness > 3.0 or thickness < 3.0) and (nodes < 9.0 or nodes > 10.0)) then \n{\n    genus >= thickness+(edges-(4.0*nodes)-(1.0))/6.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","mindeg","thickness","genus","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (((minb("nodeConnec") != 'undt' and minb("nodeConnec") > 0.0) and (minb("nodes") != 'undt' and minb("nodes") > 2.0)) or (minb("mindeg") != 'undt' and minb("mindeg") > 1.0)) and (((minb("thickness") != 'undt' and minb("thickness") > 3.0) or (maxb("thickness") != 'undt' and maxb("thickness") < 3.0)) and ((maxb("nodes") != 'undt' and maxb("nodes") < 9.0) or (minb("nodes") != 'undt' and minb("nodes") > 10.0))):
            if minb("thickness") != 'undt' and minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("genus",  minb("thickness")+(minb("edges")-(4.0*maxb("nodes"))-(1.0))/6.0, ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("genus") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("thickness",  -(minb("edges")/6.0)+maxb("genus")+2.0*maxb("nodes")/3.0+1.0/6.0, ind='Max')
                except:
                    pass
            if maxb("genus") != 'undt' and maxb("nodes") != 'undt' and maxb("thickness") != 'undt':
                try:
                    set("edges",  6.0*maxb("genus")+4.0*maxb("nodes")-(6.0*minb("thickness"))+1.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("genus") != 'undt' and minb("thickness") != 'undt':
                try:
                    set("nodes",  minb("edges")/4.0-(3.0*maxb("genus")/2.0)+3.0*minb("thickness")/2.0-(1.0/4.0), ind='Min')
                except:
                    pass
        return
class Theorem259(Theorem):
    def __init__(self):
        super(Theorem259, self).__init__(259, "if girth > 1.0+2.0*(log(nodes)/log(2.0)) then \n{\n    chromaticNum <= 3.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and maxb("nodes") != 'undt' and minb("girth") > 1.0+2.0*(log(maxb("nodes"))/log(2.0))):
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        return
class Theorem260(Theorem):
    def __init__(self):
        super(Theorem260, self).__init__(260, "let c = edges-(nodes)+numOfComponents;\nnosolve genus <= c/2.0-(c/(4.0*log(c)/log(2.0)));\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","edges","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
            try:
                set("genus",  maxb("edges")-(minb("nodes"))+maxb("numOfComponents")/2.0-(maxb("edges")-(minb("nodes"))+maxb("numOfComponents")/(4.0*log(maxb("edges")-(minb("nodes"))+maxb("numOfComponents"))/log(2.0))), ind='Max')
            except:
                pass
        return
class Theorem261(Theorem):
    def __init__(self):
        super(Theorem261, self).__init__(261, "if genus <= 2.0 and girth >= 5.0 then \n{\n    chromaticNum <= 4.0\n};\n", "")
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
        if (maxb("genus") != 'undt' and maxb("genus") <= 2.0) and (minb("girth") != 'undt' and minb("girth") >= 5.0):
            try:
                set("chromaticNum",  4.0, ind='Max')
            except:
                pass
        return
class Theorem262(Theorem):
    def __init__(self):
        super(Theorem262, self).__init__(262, "if (genus == 0.0 and girth >= 4.0) or (genus <= 1.0 and girth >= 6.0) or (genus <= 2.0 and girth >= 7.0) or (girth >= 9.0) then \n{\n    chromaticNum <= 3.0\n};\n", "")
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
        if (((minb("genus") != 'undt' and minb("genus") >= 0.0) and (maxb("genus") != 'undt' and maxb("genus") <= 0.0)) and (minb("girth") != 'undt' and minb("girth") >= 4.0)) or ((maxb("genus") != 'undt' and maxb("genus") <= 1.0) and (minb("girth") != 'undt' and minb("girth") >= 6.0)) or ((maxb("genus") != 'undt' and maxb("genus") <= 2.0) and (minb("girth") != 'undt' and minb("girth") >= 7.0)) or ((minb("girth") != 'undt' and minb("girth") >= 9.0)):
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        return
class Theorem263(Theorem):
    def __init__(self):
        super(Theorem263, self).__init__(263, "nosolve maxdeg >= (nodes-(1.0))**(1.0/radius);\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodes","radius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("radius") != 'undt':
            try:
                set("maxdeg",  (minb("nodes")-(1.0))**(1.0/maxb("radius")), ind='Min')
            except:
                pass
        return
class Theorem264(Theorem):
    def __init__(self):
        super(Theorem264, self).__init__(264, "if connected then \n{\n    diameter <= 3.0*domination-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if maxb("domination") != 'undt':
                try:
                    set("diameter",  3.0*maxb("domination")-(1.0), ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt':
                try:
                    set("domination",  minb("diameter")/3.0+1.0/3.0, ind='Min')
                except:
                    pass
        return
class Theorem265(Theorem):
    def __init__(self):
        super(Theorem265, self).__init__(265, "if connected and minb(maxdeg) >= 3.0 then \n{\n    nodes <= 1.0+maxb(mindeg)*((maxb(maxdeg)-(1.0))**maxb(diameter)-(1.0))/(maxb(maxdeg)-(2.0)),\n    mindeg >= (maxb(maxdeg)*minb(nodes)-(maxb(maxdeg))-(2.0*minb(nodes))+2.0)/((maxb(maxdeg)-(1.0))**maxb(diameter)-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","nodes","mindeg","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
            if maxb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("nodes",  1.0+maxb("mindeg")*((maxb("maxdeg")-(1.0))**maxb("diameter")-(1.0))/(maxb("maxdeg")-(2.0)), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt' and minb("nodes") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("mindeg",  (maxb("maxdeg")*minb("nodes")-(maxb("maxdeg"))-(2.0*minb("nodes"))+2.0)/((maxb("maxdeg")-(1.0))**maxb("diameter")-(1.0)), ind='Min')
                except:
                    pass
        return
class Theorem266(Theorem):
    def __init__(self):
        super(Theorem266, self).__init__(266, "if diameter >= 2.0 and maxdeg >= 3.0 then \n{\n    maxdeg >= ceil((nodes-(2.0))/(mindeg+1.0))**(1.0/(diameter-(1.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("maxdeg",  ceil((minb("nodes")-(2.0))/(maxb("mindeg")+1.0))**(1.0/(maxb("diameter")-(1.0))), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("diameter",  log(ceil((minb("nodes")-(2.0))/(maxb("mindeg")+1.0)))/log(maxb("maxdeg"))+1.0, ind='Min')
                except:
                    pass
        return
class Theorem267(Theorem):
    def __init__(self):
        super(Theorem267, self).__init__(267, "if diameter == radius and radius == 2.0 then \n{\n    mindeg >= 2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","radius","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and maxb("radius") != 'undt' and minb("diameter") >= maxb("radius")) and (maxb("diameter") != 'undt' and minb("radius") != 'undt' and maxb("diameter") <= minb("radius"))) and ((minb("radius") != 'undt' and minb("radius") >= 2.0) and (maxb("radius") != 'undt' and maxb("radius") <= 2.0)):
            try:
                set("mindeg",  2.0, ind='Min')
            except:
                pass
        return
class Theorem268(Theorem):
    def __init__(self):
        super(Theorem268, self).__init__(268, "if not forest then \n{\n    bandwidth >= (minb(girth)-(1.0))*(minb(arboricity)-(2.0))+2.0,\n    girth <= (minb(arboricity)+maxb(bandwidth)-(4.0))/(minb(arboricity)-(2.0)),\n    arboricity <= (maxb(bandwidth)+2.0*minb(girth)-(4.0))/(minb(girth)-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","bandwidth","girth","arboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False:
            if minb("girth") != 'undt' and minb("arboricity") != 'undt':
                try:
                    set("bandwidth",  (minb("girth")-(1.0))*(minb("arboricity")-(2.0))+2.0, ind='Min')
                except:
                    pass
            if maxb("arboricity") != 'undt' and maxb("bandwidth") != 'undt':
                try:
                    set("girth",  (minb("arboricity")+maxb("bandwidth")-(4.0))/(minb("arboricity")-(2.0)), ind='Max')
                except:
                    pass
            if maxb("bandwidth") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("arboricity",  (maxb("bandwidth")+2.0*minb("girth")-(4.0))/(minb("girth")-(1.0)), ind='Max')
                except:
                    pass
        return
class Theorem269(Theorem):
    def __init__(self):
        super(Theorem269, self).__init__(269, "if not forest then \n{\n    bandwidth >= (minb(girth)-(1.0))*minb(nodes)/(2.0*maxb(nodeInd))-(minb(girth))+2.0,\n    girth <= (-(2.0*maxb(bandwidth)*maxb(nodeInd))+4.0*maxb(nodeInd)-(minb(nodes)))/(2.0*maxb(nodeInd)-(minb(nodes))),\n    nodes <= 2.0*maxb(nodeInd)*(maxb(bandwidth)+minb(girth)-(2.0))/(minb(girth)-(1.0)),\n    nodeInd >= minb(nodes)*(minb(girth)-(1.0))/(2.0*(maxb(bandwidth)+minb(girth)-(2.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","bandwidth","girth","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False:
            if minb("girth") != 'undt' and minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("bandwidth",  (minb("girth")-(1.0))*minb("nodes")/(2.0*maxb("nodeInd"))-(minb("girth"))+2.0, ind='Min')
                except:
                    pass
            if maxb("bandwidth") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("girth",  (-(2.0*maxb("bandwidth")*maxb("nodeInd"))+4.0*maxb("nodeInd")-(minb("nodes")))/(2.0*maxb("nodeInd")-(minb("nodes"))), ind='Max')
                except:
                    pass
            if maxb("nodeInd") != 'undt' and maxb("bandwidth") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("nodes",  2.0*maxb("nodeInd")*(maxb("bandwidth")+minb("girth")-(2.0))/(minb("girth")-(1.0)), ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("girth") != 'undt' and minb("bandwidth") != 'undt':
                try:
                    set("nodeInd",  minb("nodes")*(minb("girth")-(1.0))/(2.0*(maxb("bandwidth")+minb("girth")-(2.0))), ind='Min')
                except:
                    pass
        return
class Theorem270(Theorem):
    def __init__(self):
        super(Theorem270, self).__init__(270, "if not forest then \n{\n    domination <= nodes-(2.0*circumference/3.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","domination","nodes","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False:
            if maxb("nodes") != 'undt' and maxb("circumference") != 'undt':
                try:
                    set("domination",  maxb("nodes")-(2.0*minb("circumference")/3.0), ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt' and minb("domination") != 'undt':
                try:
                    set("nodes",  2.0*minb("circumference")/3.0+minb("domination"), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("circumference",  -(3.0*minb("domination")/2.0)+3.0*maxb("nodes")/2.0, ind='Max')
                except:
                    pass
        return
class Theorem271(Theorem):
    def __init__(self):
        super(Theorem271, self).__init__(271, "let k = ceil(nodes/mindeg);\ncircumference >= floor(nodes/(k-(1.0)));\n", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("circumference",  floor(minb("nodes")/(ceil(minb("nodes")/minb("mindeg"))-(1.0))), ind='Min')
            except:
                pass
        return
class Theorem272(Theorem):
    def __init__(self):
        super(Theorem272, self).__init__(272, "if diameter == 2.0 then \n{\n    domination <= nodeConnec\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","domination","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)):
            if maxb("nodeConnec") != 'undt':
                try:
                    set("domination",  maxb("nodeConnec"), ind='Max')
                except:
                    pass
            if minb("domination") != 'undt':
                try:
                    set("nodeConnec",  minb("domination"), ind='Min')
                except:
                    pass
        return
class Theorem273(Theorem):
    def __init__(self):
        super(Theorem273, self).__init__(273, "if tree then \n{\n    radius == ((diameter+1.0)/2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["tree","radius","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("tree") == True:
            if minb("diameter") != 'undt':
                try:
                    set("radius",  ((minb("diameter")+1.0)/2.0), ind='Min')
                except:
                    pass
            if maxb("radius") != 'undt':
                try:
                    set("diameter",  2.0*maxb("radius")-(1.0), ind='Max')
                except:
                    pass
            if maxb("diameter") != 'undt':
                try:
                    set("radius",  ((maxb("diameter")+1.0)/2.0), ind='Max')
                except:
                    pass
            if minb("radius") != 'undt':
                try:
                    set("diameter",  2.0*minb("radius")-(1.0), ind='Min')
                except:
                    pass
        return
class Theorem274(Theorem):
    def __init__(self):
        super(Theorem274, self).__init__(274, "if hamiltonian then \n{\n    nodes >= (minb(maxdeg)-(1.0))*(minb(girth)-(2.0))+2.0,\n    maxdeg <= (minb(girth)+maxb(nodes)-(4.0))/(minb(girth)-(2.0)),\n    girth <= (2.0*minb(maxdeg)+maxb(nodes)-(4.0))/(minb(maxdeg)-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodes","maxdeg","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("hamiltonian") == True:
            if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                try:
                    set("nodes",  (minb("maxdeg")-(1.0))*(minb("girth")-(2.0))+2.0, ind='Min')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  (minb("girth")+maxb("nodes")-(4.0))/(minb("girth")-(2.0)), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("girth",  (2.0*minb("maxdeg")+maxb("nodes")-(4.0))/(minb("maxdeg")-(1.0)), ind='Max')
                except:
                    pass
        return
class Theorem275(Theorem):
    def __init__(self):
        super(Theorem275, self).__init__(275, "nodeInd >= minb(maxdeg)/(maxb(chromaticNum)-(1.0));\nmaxdeg <= maxb(nodeInd)*(maxb(chromaticNum)-(1.0));\nchromaticNum >= (minb(maxdeg)+maxb(nodeInd))/maxb(nodeInd);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","maxdeg","chromaticNum"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("maxdeg") != 'undt' and minb("chromaticNum") != 'undt':
            try:
                set("nodeInd",  minb("maxdeg")/(maxb("chromaticNum")-(1.0)), ind='Min')
            except:
                pass
        if maxb("nodeInd") != 'undt' and maxb("chromaticNum") != 'undt':
            try:
                set("maxdeg",  maxb("nodeInd")*(maxb("chromaticNum")-(1.0)), ind='Max')
            except:
                pass
        if minb("maxdeg") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("chromaticNum",  (minb("maxdeg")+maxb("nodeInd"))/maxb("nodeInd"), ind='Min')
            except:
                pass
        return
class Theorem276(Theorem):
    def __init__(self):
        super(Theorem276, self).__init__(276, "maxClique >= (minb(nodes)-(maxb(mindeg))-(1.0))/(maxb(nodeCliqueCover)-(1.0));\nnodes <= maxb(maxClique)*maxb(nodeCliqueCover)-(maxb(maxClique))+maxb(mindeg)+1.0;\nmindeg >= -(maxb(maxClique)*maxb(nodeCliqueCover))+maxb(maxClique)+minb(nodes)-(1.0);\nnodeCliqueCover >= (maxb(maxClique)-(maxb(mindeg))+minb(nodes)-(1.0))/maxb(maxClique);\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","mindeg","nodeCliqueCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("nodeCliqueCover") != 'undt':
            try:
                set("maxClique",  (minb("nodes")-(maxb("mindeg"))-(1.0))/(maxb("nodeCliqueCover")-(1.0)), ind='Min')
            except:
                pass
        if maxb("maxClique") != 'undt' and maxb("nodeCliqueCover") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("nodes",  maxb("maxClique")*maxb("nodeCliqueCover")-(maxb("maxClique"))+maxb("mindeg")+1.0, ind='Max')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("nodeCliqueCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("mindeg",  -(maxb("maxClique")*maxb("nodeCliqueCover"))+maxb("maxClique")+minb("nodes")-(1.0), ind='Min')
            except:
                pass
        if minb("maxClique") != 'undt' and minb("mindeg") != 'undt' and minb("nodes") != 'undt':
            try:
                set("nodeCliqueCover",  (maxb("maxClique")-(maxb("mindeg"))+minb("nodes")-(1.0))/maxb("maxClique"), ind='Min')
            except:
                pass
        return
class Theorem277(Theorem):
    def __init__(self):
        super(Theorem277, self).__init__(277, "if nodes >= 3.0 and nodeConnec <= 1.0 then \n{\n    edgeConnec <= maxdeg/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeConnec","edgeConnec","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt' and minb("nodes") >= 3.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 1.0):
            if maxb("maxdeg") != 'undt':
                try:
                    set("edgeConnec",  maxb("maxdeg")/2.0, ind='Max')
                except:
                    pass
            if minb("edgeConnec") != 'undt':
                try:
                    set("maxdeg",  2.0*minb("edgeConnec"), ind='Min')
                except:
                    pass
        return
class Theorem278(Theorem):
    def __init__(self):
        super(Theorem278, self).__init__(278, "if connected and maxdeg >= 3.0 then \n{\n    nodes <= 1.0+maxdeg*((maxdeg-(1.0))**radius-(1.0))/(maxdeg-(2.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","nodes","radius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0):
            if maxb("maxdeg") != 'undt' and maxb("radius") != 'undt':
                try:
                    set("nodes",  1.0+maxb("maxdeg")*((maxb("maxdeg")-(1.0))**maxb("radius")-(1.0))/(maxb("maxdeg")-(2.0)), ind='Max')
                except:
                    pass
        return
class Theorem279(Theorem):
    def __init__(self):
        super(Theorem279, self).__init__(279, "if connected then \n{\n    nodes >= maxdeg+2.0*radius-(2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodes","maxdeg","radius"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if minb("maxdeg") != 'undt' and minb("radius") != 'undt':
                try:
                    set("nodes",  minb("maxdeg")+2.0*minb("radius")-(2.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("radius") != 'undt':
                try:
                    set("maxdeg",  maxb("nodes")-(2.0*minb("radius"))+2.0, ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("radius",  -(minb("maxdeg")/2.0)+maxb("nodes")/2.0+1.0, ind='Max')
                except:
                    pass
        return
class Theorem280(Theorem):
    def __init__(self):
        super(Theorem280, self).__init__(280, "if forest then \n{\n    nodes >= 2.0*(bandwidth+numOfComponents-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodes","bandwidth","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == True:
            if minb("bandwidth") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  2.0*(minb("bandwidth")+minb("numOfComponents")-(1.0)), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("bandwidth",  maxb("nodes")/2.0-(minb("numOfComponents"))+1.0, ind='Max')
                except:
                    pass
            if maxb("bandwidth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(minb("bandwidth"))+maxb("nodes")/2.0+1.0, ind='Max')
                except:
                    pass
        return
class Theorem281(Theorem):
    def __init__(self):
        super(Theorem281, self).__init__(281, "if nodeConnec >= 2.0 and nodes <= 3.0*mindeg and edges <= ((nodes-(1.0))*mindeg-(1.0))/2.0 then \n{\n    hamiltonian\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","mindeg","edges","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodes") <= 3.0*minb("mindeg")) and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("edges") <= ((minb("nodes")-(1.0))*minb("mindeg")-(1.0))/2.0):
            set("hamiltonian", True)
        return
class Theorem282(Theorem):
    def __init__(self):
        super(Theorem282, self).__init__(282, "if even nodes and not bipartite then \n{\n    not cycle\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","bipartite","cycle"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if evenInvar("nodes") and get("bipartite") == False:
            set("cycle", False)
        return
class Theorem283(Theorem):
    def __init__(self):
        super(Theorem283, self).__init__(283, "if mindeg == maxdeg and maxdeg == nodeConnec and nodeConnec == 3.0 then \n{\n    circumference >= nodes**(2.0/3.0)+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","circumference","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and maxb("nodeConnec") != 'undt' and minb("maxdeg") >= maxb("nodeConnec")) and (maxb("maxdeg") != 'undt' and minb("nodeConnec") != 'undt' and maxb("maxdeg") <= minb("nodeConnec"))) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 3.0)):
            if minb("nodes") != 'undt':
                try:
                    set("circumference",  minb("nodes")**(2.0/3.0)+1.0, ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt':
                try:
                    set("nodes",  (maxb("circumference")-(1.0))**(3.0/2.0), ind='Max')
                except:
                    pass
        return
class Theorem284(Theorem):
    def __init__(self):
        super(Theorem284, self).__init__(284, "\n", "")
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
class Theorem285(Theorem):
    def __init__(self):
        super(Theorem285, self).__init__(285, "edgeCliqueCover <= maxb(nodeCliqueCover)+maxb(nodes)*(maxb(maxdeg)+1.0-(maxb(nodes)/maxb(nodeCliqueCover)))/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodeCliqueCover","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("edgeCliqueCover",  maxb("nodeCliqueCover")+maxb("nodes")*(maxb("maxdeg")+1.0-(maxb("nodes")/maxb("nodeCliqueCover")))/2.0, ind='Max')
            except:
                pass
        return
class Theorem286(Theorem):
    def __init__(self):
        super(Theorem286, self).__init__(286, "edges >= (minb(maxdeg)+(minb(chromaticNum)-(1.0))**2.0+(minb(nodes)-(minb(chromaticNum)))*minb(mindeg))/2.0;\nmaxdeg <= maxb(chromaticNum)*maxb(mindeg)+2.0*maxb(edges)-(maxb(mindeg)*minb(nodes))-((maxb(chromaticNum)-(1.0))**2.0);\nnodes <= (maxb(chromaticNum)*minb(mindeg)+2.0*maxb(edges)-(minb(maxdeg))-((maxb(chromaticNum)-(1.0))**2.0))/minb(mindeg);\nmindeg <= (-(2.0*maxb(edges))+minb(maxdeg)+(maxb(chromaticNum)-(1.0))**2.0)/(maxb(chromaticNum)-(maxb(nodes)));\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","chromaticNum","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("maxdeg") != 'undt' and minb("chromaticNum") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("edges",  (minb("maxdeg")+(minb("chromaticNum")-(1.0))**2.0+(minb("nodes")-(minb("chromaticNum")))*minb("mindeg"))/2.0, ind='Min')
            except:
                pass
        if maxb("chromaticNum") != 'undt' and maxb("mindeg") != 'undt' and maxb("edges") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxdeg",  maxb("chromaticNum")*maxb("mindeg")+2.0*maxb("edges")-(maxb("mindeg")*minb("nodes"))-((maxb("chromaticNum")-(1.0))**2.0), ind='Max')
            except:
                pass
        if maxb("chromaticNum") != 'undt' and maxb("mindeg") != 'undt' and maxb("edges") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("nodes",  (maxb("chromaticNum")*minb("mindeg")+2.0*maxb("edges")-(minb("maxdeg"))-((maxb("chromaticNum")-(1.0))**2.0))/minb("mindeg"), ind='Max')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("maxdeg") != 'undt' and maxb("chromaticNum") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("mindeg",  (-(2.0*maxb("edges"))+minb("maxdeg")+(maxb("chromaticNum")-(1.0))**2.0)/(maxb("chromaticNum")-(maxb("nodes"))), ind='Max')
            except:
                pass
        return
class Theorem287(Theorem):
    def __init__(self):
        super(Theorem287, self).__init__(287, "if planar then \n{\n    mindeg <= nodeInd+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True:
            if maxb("nodeInd") != 'undt':
                try:
                    set("mindeg",  maxb("nodeInd")+2.0, ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("nodeInd",  minb("mindeg")-(2.0), ind='Min')
                except:
                    pass
        return
class Theorem288(Theorem):
    def __init__(self):
        super(Theorem288, self).__init__(288, "if (minb(diameter) >= 2.0 and maxb(diameter) <= 2.0) and (minb(maxClique) >= 2.0 and maxb(maxClique) <= 2.0) and regular and not bipartite then \n{\n    if istrue congruent(maxdeg, 0.0, 2.0) then \n    {\n        nodes >= minb(maxdeg)*5.0/2.0,\n        maxdeg <= 2.0*maxb(nodes)/5.0\n    }\n    else if istrue congruent(maxdeg, 0.0, 3.0) then \n    {\n        nodes >= minb(maxdeg)*8.0/3.0,\n        maxdeg <= 3.0*maxb(nodes)/8.0\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxClique","regular","bipartite","maxdeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and get("regular") == True and get("bipartite") == False:
            if congruent("maxdeg", 0.0, 2.0):
                if minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  minb("maxdeg")*5.0/2.0, ind='Min')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("maxdeg",  2.0*maxb("nodes")/5.0, ind='Max')
                    except:
                        pass
            elif congruent("maxdeg", 0.0, 3.0):
                if minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  minb("maxdeg")*8.0/3.0, ind='Min')
                    except:
                        pass
                if maxb("nodes") != 'undt':
                    try:
                        set("maxdeg",  3.0*maxb("nodes")/8.0, ind='Max')
                    except:
                        pass
        return
class Theorem289(Theorem):
    def __init__(self):
        super(Theorem289, self).__init__(289, "if connected and not hamiltonian and not tree and circumference >= (nodes-(2.0))/2.0 then \n{\n    domination <= (2.0*nodes-(circumference))/3.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","hamiltonian","tree","circumference","nodes","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and get("hamiltonian") == False and get("tree") == False and (minb("circumference") != 'undt' and maxb("nodes") != 'undt' and minb("circumference") >= (maxb("nodes")-(2.0))/2.0):
            if maxb("nodes") != 'undt' and maxb("circumference") != 'undt':
                try:
                    set("domination",  (2.0*maxb("nodes")-(minb("circumference")))/3.0, ind='Max')
                except:
                    pass
            if minb("circumference") != 'undt' and minb("domination") != 'undt':
                try:
                    set("nodes",  minb("circumference")/2.0+3.0*minb("domination")/2.0, ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("circumference",  -(3.0*minb("domination"))+2.0*maxb("nodes"), ind='Max')
                except:
                    pass
        return
class Theorem290(Theorem):
    def __init__(self):
        super(Theorem290, self).__init__(290, "if connected and domination >= 3.0 then \n{\n    edges <= (nodes-(domination)+1.0)*(nodes-(domination))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","domination","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (minb("domination") != 'undt' and minb("domination") >= 3.0):
            if maxb("nodes") != 'undt' and maxb("domination") != 'undt':
                try:
                    set("edges",  (maxb("nodes")-(minb("domination"))+1.0)*(maxb("nodes")-(minb("domination")))/2.0, ind='Max')
                except:
                    pass
            if minb("domination") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  minb("domination")+sqrt(8.0*minb("edges")+1.0)/2.0-(1.0/2.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("domination",  maxb("nodes")+sqrt(8.0*maxb("edges")+1.0)/2.0+1.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem291(Theorem):
    def __init__(self):
        super(Theorem291, self).__init__(291, "nosolve domination <= nodes*(1.0+ln(mindeg))/(mindeg+1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("domination",  maxb("nodes")*(1.0+ln(maxb("mindeg")))/(maxb("mindeg")+1.0), ind='Max')
            except:
                pass
        return
class Theorem292(Theorem):
    def __init__(self):
        super(Theorem292, self).__init__(292, "\n", "")
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
class Theorem293(Theorem):
    def __init__(self):
        super(Theorem293, self).__init__(293, "if connected and maxdeg == 2.0 then \n{\n    nodes >= mindeg*diameter-(mindeg)+2.0,\n    nodes <= mindeg*diameter+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","nodes","mindeg","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0)):
            if minb("mindeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodes",  minb("mindeg")*minb("diameter")-(minb("mindeg"))+2.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("mindeg",  (maxb("nodes")-(2.0))/(minb("diameter")-(1.0)), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("diameter",  (maxb("mindeg")+maxb("nodes")-(2.0))/maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt' and maxb("diameter") != 'undt':
                try:
                    set("nodes",  maxb("mindeg")*maxb("diameter")+1.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("mindeg",  (minb("nodes")-(1.0))/maxb("diameter"), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("diameter",  (minb("nodes")-(1.0))/maxb("mindeg"), ind='Min')
                except:
                    pass
        return
class Theorem294(Theorem):
    def __init__(self):
        super(Theorem294, self).__init__(294, "edgeCliqueCover <= (nodes-(maxClique)+2.0)**2.0/4.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodes","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt':
            try:
                set("edgeCliqueCover",  (maxb("nodes")-(minb("maxClique"))+2.0)**2.0/4.0, ind='Max')
            except:
                pass
        if minb("edgeCliqueCover") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("nodes",  2.0*sqrt(minb("edgeCliqueCover"))+minb("maxClique")-(2.0), ind='Min')
            except:
                pass
        if maxb("edgeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxClique",  2.0*sqrt(maxb("edgeCliqueCover"))+maxb("nodes")+2.0, ind='Max')
            except:
                pass
        return
class Theorem295(Theorem):
    def __init__(self):
        super(Theorem295, self).__init__(295, "edges <= maximum(edgeInd*(2.0*edgeInd+1.0), edgeInd*nodes-(edgeInd*(edgeInd+1.0)/2.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","edgeInd","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  maximum(maxb("edgeInd")*(2.0*maxb("edgeInd")+1.0), maxb("edgeInd")*maxb("nodes")-(maxb("edgeInd")*(maxb("edgeInd")+1.0)/2.0)), ind='Max')
            except:
                pass
        return
class Theorem296(Theorem):
    def __init__(self):
        super(Theorem296, self).__init__(296, "if mindeg == maxdeg and maxdeg == 3.0 then \n{\n    nodeConnec == edgeConnec\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)):
            if minb("edgeConnec") != 'undt':
                try:
                    set("nodeConnec",  minb("edgeConnec"), ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt':
                try:
                    set("edgeConnec",  maxb("nodeConnec"), ind='Max')
                except:
                    pass
            if maxb("edgeConnec") != 'undt':
                try:
                    set("nodeConnec",  maxb("edgeConnec"), ind='Max')
                except:
                    pass
            if minb("nodeConnec") != 'undt':
                try:
                    set("edgeConnec",  minb("nodeConnec"), ind='Min')
                except:
                    pass
        return
class Theorem297(Theorem):
    def __init__(self):
        super(Theorem297, self).__init__(297, "if nodeConnec >= 3.0 and planar and not hamiltonian then \n{\n    nodes >= 11.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","planar","hamiltonian","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0) and get("planar") == True and get("hamiltonian") == False:
            try:
                set("nodes",  11.0, ind='Min')
            except:
                pass
        return
class Theorem298(Theorem):
    def __init__(self):
        super(Theorem298, self).__init__(298, "if mindeg == maxdeg and maxdeg == 3.0 and not planar and not bipartite then \n{\n    nodes >= 8.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","planar","bipartite","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and get("planar") == False and get("bipartite") == False:
            try:
                set("nodes",  8.0, ind='Min')
            except:
                pass
        return
class Theorem299(Theorem):
    def __init__(self):
        super(Theorem299, self).__init__(299, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 1.0 then \n{\n    nodes >= 10.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 1.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 1.0)):
            try:
                set("nodes",  10.0, ind='Min')
            except:
                pass
        return
class Theorem300(Theorem):
    def __init__(self):
        super(Theorem300, self).__init__(300, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 1.0 and not planar then \n{\n    nodes >= 12.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 1.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 1.0)) and get("planar") == False:
            try:
                set("nodes",  12.0, ind='Min')
            except:
                pass
        return
class Theorem301(Theorem):
    def __init__(self):
        super(Theorem301, self).__init__(301, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and planar and not hamiltonian and bipartite then \n{\n    nodes >= 26.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","hamiltonian","bipartite","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and get("planar") == True and get("hamiltonian") == False and get("bipartite") == True:
            try:
                set("nodes",  26.0, ind='Min')
            except:
                pass
        return
class Theorem302(Theorem):
    def __init__(self):
        super(Theorem302, self).__init__(302, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and planar and not hamiltonian then \n{\n    nodes >= 14.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","hamiltonian","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and get("planar") == True and get("hamiltonian") == False:
            try:
                set("nodes",  14.0, ind='Min')
            except:
                pass
        return
class Theorem303(Theorem):
    def __init__(self):
        super(Theorem303, self).__init__(303, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec >= 2.0 and bipartite and not hamiltonian then \n{\n    nodes >= 20.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","bipartite","hamiltonian","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and get("bipartite") == True and get("hamiltonian") == False:
            try:
                set("nodes",  20.0, ind='Min')
            except:
                pass
        return
class Theorem304(Theorem):
    def __init__(self):
        super(Theorem304, self).__init__(304, "\n", "")
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
class Theorem305(Theorem):
    def __init__(self):
        super(Theorem305, self).__init__(305, "if mindeg == maxdeg and maxdeg == 3.0 then \n{\n    edgeInd >= nodes/2.0-((nodes+3.0)/18.0)-((numOfComponents+4.0)/6.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeInd","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)):
            if minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("edgeInd",  minb("nodes")/2.0-((minb("nodes")+3.0)/18.0)-((maxb("numOfComponents")+4.0)/6.0), ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("nodes",  9.0*maxb("edgeInd")/4.0+3.0*maxb("numOfComponents")/8.0+15.0/8.0, ind='Max')
                except:
                    pass
            if minb("edgeInd") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(6.0*maxb("edgeInd"))+8.0*minb("nodes")/3.0-(5.0), ind='Min')
                except:
                    pass
        return
class Theorem306(Theorem):
    def __init__(self):
        super(Theorem306, self).__init__(306, "if maxClique == 2.0 and maxdeg <= 4.0 then \n{\n    edges >= 6.0*nodes-(13.0*nodeInd)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 4.0):
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("edges",  6.0*minb("nodes")-(13.0*maxb("nodeInd")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("edges")/6.0+13.0*maxb("nodeInd")/6.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeInd",  -(maxb("edges")/13.0)+6.0*minb("nodes")/13.0, ind='Min')
                except:
                    pass
        return
class Theorem307(Theorem):
    def __init__(self):
        super(Theorem307, self).__init__(307, "if edgeConnec > 0.0 then \n{\n    edgeConnec >= minimum(mindeg, (nodes*(maxdeg-(2.0)))/((maxdeg-(1.0))**(diameter-(1.0))+maxdeg*(maxdeg-(2.0))-(1.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg","nodes","maxdeg","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edgeConnec") != 'undt' and minb("edgeConnec") > 0.0):
            if minb("mindeg") != 'undt' and minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("edgeConnec",  minimum(minb("mindeg"), (minb("nodes")*(maxb("maxdeg")-(2.0)))/((maxb("maxdeg")-(1.0))**(maxb("diameter")-(1.0))+maxb("maxdeg")*(maxb("maxdeg")-(2.0))-(1.0))), ind='Min')
                except:
                    pass
        return
class Theorem308(Theorem):
    def __init__(self):
        super(Theorem308, self).__init__(308, "if nodeConnec >= 2.0 and nodeInd >= 2.0 then \n{\n    circumference >= 2.0*(nodes-(2.0))/nodeInd+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodeInd","circumference","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (minb("nodeInd") != 'undt' and minb("nodeInd") >= 2.0):
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("circumference",  2.0*(minb("nodes")-(2.0))/maxb("nodeInd")+2.0, ind='Min')
                except:
                    pass
            if maxb("circumference") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("circumference")*maxb("nodeInd")/2.0-(maxb("nodeInd"))+2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("circumference") != 'undt':
                try:
                    set("nodeInd",  2.0*(minb("nodes")-(2.0))/(maxb("circumference")-(2.0)), ind='Min')
                except:
                    pass
        return
class Theorem309(Theorem):
    def __init__(self):
        super(Theorem309, self).__init__(309, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 3.0 and planar then \n{\n    circumference >= minimum(nodes, 17.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","circumference","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 3.0)) and get("planar") == True:
            if minb("nodes") != 'undt':
                try:
                    set("circumference",  minimum(minb("nodes"), 17.0), ind='Min')
                except:
                    pass
        return
class Theorem310(Theorem):
    def __init__(self):
        super(Theorem310, self).__init__(310, "if mindeg == maxdeg and maxdeg == 3.0 and nodeConnec == 3.0 and planar and nodes <= 36.0 then \n{\n    hamiltonian\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","nodeConnec","planar","nodes","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and ((minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0) and (maxb("nodeConnec") != 'undt' and maxb("nodeConnec") <= 3.0)) and get("planar") == True and (maxb("nodes") != 'undt' and maxb("nodes") <= 36.0):
            set("hamiltonian", True)
        return
class Theorem311(Theorem):
    def __init__(self):
        super(Theorem311, self).__init__(311, "if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg >= 9.0 then \n{\n    nodes >= 2.0*maxdeg\n}\nelse if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg <= 8.0 then \n{\n    nodes >= 2.0*maxdeg-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","maxdeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and minb("chromaticNum") != 'undt' and maxb("maxClique") < minb("chromaticNum")) and ((minb("chromaticNum") != 'undt' and maxb("maxdeg") != 'undt' and minb("chromaticNum") >= maxb("maxdeg")) and (maxb("chromaticNum") != 'undt' and minb("maxdeg") != 'undt' and maxb("chromaticNum") <= minb("maxdeg"))) and (minb("maxdeg") != 'undt' and minb("maxdeg") >= 9.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("nodes",  2.0*minb("maxdeg"), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
        elif (maxb("maxClique") != 'undt' and minb("chromaticNum") != 'undt' and maxb("maxClique") < minb("chromaticNum")) and ((minb("chromaticNum") != 'undt' and maxb("maxdeg") != 'undt' and minb("chromaticNum") >= maxb("maxdeg")) and (maxb("chromaticNum") != 'undt' and minb("maxdeg") != 'undt' and maxb("chromaticNum") <= minb("maxdeg"))) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 8.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("nodes",  2.0*minb("maxdeg")-(1.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem312(Theorem):
    def __init__(self):
        super(Theorem312, self).__init__(312, "if mindeg == maxdeg and maxdeg == 3.0 and edgeConnec >= 2.0 then \n{\n    edgeInd == nodes/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeConnec","edgeInd","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("edgeConnec") != 'undt' and minb("edgeConnec") >= 2.0):
            if minb("nodes") != 'undt':
                try:
                    set("edgeInd",  minb("nodes")/2.0, ind='Min')
                except:
                    pass
            if maxb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edgeInd"), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edgeInd",  maxb("nodes")/2.0, ind='Max')
                except:
                    pass
            if minb("edgeInd") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeInd"), ind='Min')
                except:
                    pass
        return
class Theorem313(Theorem):
    def __init__(self):
        super(Theorem313, self).__init__(313, "if planar and nodeConnec >= 3.0 then \n{\n    circumference >= minimum(nodes, 2.0*mindeg)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("circumference",  minimum(minb("nodes"), 2.0*minb("mindeg")), ind='Min')
                except:
                    pass
        return
class Theorem314(Theorem):
    def __init__(self):
        super(Theorem314, self).__init__(314, "if regular and nodeConnec >= 2.0 and nodes < 3.0*mindeg+4.0 then \n{\n    circumference >= minimum(nodes, 3.0*mindeg)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeConnec","nodes","mindeg","circumference"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodes") < 3.0*minb("mindeg")+4.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("circumference",  minimum(minb("nodes"), 3.0*minb("mindeg")), ind='Min')
                except:
                    pass
        return
class Theorem315(Theorem):
    def __init__(self):
        super(Theorem315, self).__init__(315, "if regular and nodeConnec >= 2.0 then \n{\n    circumference >= minimum(minimum(nodes, 3.0*mindeg), 2.0*mindeg+4.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodeConnec","circumference","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("circumference",  minimum(minimum(minb("nodes"), 3.0*minb("mindeg")), 2.0*minb("mindeg")+4.0), ind='Min')
                except:
                    pass
        return
class Theorem316(Theorem):
    def __init__(self):
        super(Theorem316, self).__init__(316, "if regular and even nodes and maxdeg >= 6.0*nodes/7.0 then \n{\n    edgeChromatic == maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","edgeChromatic"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and evenInvar("nodes") and (minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= 6.0*maxb("nodes")/7.0):
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
class Theorem317(Theorem):
    def __init__(self):
        super(Theorem317, self).__init__(317, "if maxdeg == nodes-(1.0) and even nodes and edges <= 2.0*floor((nodes-(1.0))/2.0)**2.0 then \n{\n    edgeChromatic == maxdeg\n}\nelse if maxdeg == nodes-(1.0) and odd nodes and edges <= 2.0*floor((nodes-(1.0))/2.0)**2.0+mindeg then \n{\n    edgeChromatic == maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodes","edges","edgeChromatic","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(1.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(1.0))) and evenInvar("nodes") and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= 2.0*floor((minb("nodes")-(1.0))/2.0)**2.0):
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
        elif ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(1.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(1.0))) and oddInvar("nodes") and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("edges") <= 2.0*floor((minb("nodes")-(1.0))/2.0)**2.0+minb("mindeg")):
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
class Theorem318(Theorem):
    def __init__(self):
        super(Theorem318, self).__init__(318, "\n", "")
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
class Theorem319(Theorem):
    def __init__(self):
        super(Theorem319, self).__init__(319, "let m = 2.0*e-(floor(2.0*e/maxdeg)*maxdeg);\nif spectralRadius >= (2.0*edges*(2.0*maxdeg-(1.0))-(2.0*m*(maxdeg-(m))))**(1.0/4.0) then \n{\n    girth <= 4.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","edges","maxdeg","e","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("spectralRadius") != 'undt' and maxb("edges") != 'undt' and maxb("maxdeg") != 'undt' and maxb("e") != 'undt' and minb("spectralRadius") >= (2.0*maxb("edges")*(2.0*maxb("maxdeg")-(1.0))-(2.0*2.0*minb("e")-(floor(2.0*minb("e")/maxb("maxdeg"))*maxb("maxdeg"))*(maxb("maxdeg")-(2.0*minb("e")-(floor(2.0*minb("e")/maxb("maxdeg"))*maxb("maxdeg"))))))**(1.0/4.0)):
            try:
                set("girth",  4.0, ind='Max')
            except:
                pass
        return
class Theorem320(Theorem):
    def __init__(self):
        super(Theorem320, self).__init__(320, "if connected and regular and odd nodes and nodes < 5.0*mindeg/2.0 then \n{\n    girth == 3.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","regular","nodes","mindeg","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and get("regular") == True and oddInvar("nodes") and (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodes") < 5.0*minb("mindeg")/2.0):
            try:
                set("girth",  3.0, ind='Min')
            except:
                pass
            try:
                set("girth",  3.0, ind='Max')
            except:
                pass
        return
class Theorem321(Theorem):
    def __init__(self):
        super(Theorem321, self).__init__(321, "\n", "")
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
class Theorem322(Theorem):
    def __init__(self):
        super(Theorem322, self).__init__(322, "\n", "")
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
class Theorem323(Theorem):
    def __init__(self):
        super(Theorem323, self).__init__(323, "\n", "")
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
class Theorem324(Theorem):
    def __init__(self):
        super(Theorem324, self).__init__(324, "if mindeg == maxdeg and maxdeg == 3.0 and girth >= 6.0 then \n{\n    nodeInd >= 19.0*nodes/52.0\n}\nelse if mindeg == maxdeg and maxdeg == 3.0 and girth >= 8.0 then \n{\n    nodeInd >= 20.0*nodes/52.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodeInd","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("girth") != 'undt' and minb("girth") >= 6.0):
            if minb("nodes") != 'undt':
                try:
                    set("nodeInd",  19.0*minb("nodes")/52.0, ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  52.0*maxb("nodeInd")/19.0, ind='Max')
                except:
                    pass
        elif ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and (minb("girth") != 'undt' and minb("girth") >= 8.0):
            if minb("nodes") != 'undt':
                try:
                    set("nodeInd",  20.0*minb("nodes")/52.0, ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  13.0*maxb("nodeInd")/5.0, ind='Max')
                except:
                    pass
        return
class Theorem325(Theorem):
    def __init__(self):
        super(Theorem325, self).__init__(325, "if regular and even girth and girth >= 6.0 and connected and nodes <= (mindeg*(mindeg-(3.0))+2.0*(mindeg-(1.0))**(girth/2.0))/(mindeg-(2.0)) then \n{\n    bipartite,\n    diameter == girth/2.0+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","girth","connected","nodes","mindeg","bipartite","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and evenInvar("girth") and (minb("girth") != 'undt' and minb("girth") >= 6.0) and get("connected") == True and (maxb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("girth") != 'undt' and maxb("nodes") <= (minb("mindeg")*(minb("mindeg")-(3.0))+2.0*(minb("mindeg")-(1.0))**(minb("girth")/2.0))/(minb("mindeg")-(2.0))):
            set("bipartite", True)
            if minb("girth") != 'undt':
                try:
                    set("diameter",  minb("girth")/2.0+1.0, ind='Min')
                except:
                    pass
            if maxb("diameter") != 'undt':
                try:
                    set("girth",  2.0*maxb("diameter")-(2.0), ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt':
                try:
                    set("diameter",  maxb("girth")/2.0+1.0, ind='Max')
                except:
                    pass
            if minb("diameter") != 'undt':
                try:
                    set("girth",  2.0*minb("diameter")-(2.0), ind='Min')
                except:
                    pass
        return
class Theorem326(Theorem):
    def __init__(self):
        super(Theorem326, self).__init__(326, "if bipartite and odd nodes then \n{\n    thickness <= ceil((nodes*nodes-(1.0))/(2.0*(nodes-(2.0))))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("bipartite") == True and oddInvar("nodes"):
            if maxb("nodes") != 'undt':
                try:
                    set("thickness",  ceil((maxb("nodes")*maxb("nodes")-(1.0))/(2.0*(maxb("nodes")-(2.0)))), ind='Max')
                except:
                    pass
        return
class Theorem327(Theorem):
    def __init__(self):
        super(Theorem327, self).__init__(327, "if edges >= 1.0 then \n{\n    maxdeg >= 2.0*thickness-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("edges") != 'undt' and minb("edges") >= 1.0):
            if minb("thickness") != 'undt':
                try:
                    set("maxdeg",  2.0*minb("thickness")-(1.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt':
                try:
                    set("thickness",  maxb("maxdeg")/2.0+1.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem328(Theorem):
    def __init__(self):
        super(Theorem328, self).__init__(328, "nodeConnec <= 3.0*thickness-(1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("thickness") != 'undt':
            try:
                set("nodeConnec",  3.0*maxb("thickness")-(1.0), ind='Max')
            except:
                pass
        if minb("nodeConnec") != 'undt':
            try:
                set("thickness",  minb("nodeConnec")/3.0+1.0/3.0, ind='Min')
            except:
                pass
        return
class Theorem329(Theorem):
    def __init__(self):
        super(Theorem329, self).__init__(329, "if mindeg == maxdeg and maxdeg == 3.0 and girth == 10.0 then \n{\n    nodes >= 70.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)) and ((minb("girth") != 'undt' and minb("girth") >= 10.0) and (maxb("girth") != 'undt' and maxb("girth") <= 10.0)):
            try:
                set("nodes",  70.0, ind='Min')
            except:
                pass
        return
class Theorem330(Theorem):
    def __init__(self):
        super(Theorem330, self).__init__(330, "\n", "")
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
class Theorem331(Theorem):
    def __init__(self):
        super(Theorem331, self).__init__(331, "\n", "")
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
class Theorem332(Theorem):
    def __init__(self):
        super(Theorem332, self).__init__(332, "if tree and maxdeg <= nodes-(2.0) then \n{\n    bandwidth <= (nodes-(1.0))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["tree","maxdeg","nodes","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("tree") == True and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0)):
            if maxb("nodes") != 'undt':
                try:
                    set("bandwidth",  (maxb("nodes")-(1.0))/2.0, ind='Max')
                except:
                    pass
            if minb("bandwidth") != 'undt':
                try:
                    set("nodes",  2.0*minb("bandwidth")+1.0, ind='Min')
                except:
                    pass
        return
class Theorem333(Theorem):
    def __init__(self):
        super(Theorem333, self).__init__(333, "edges >= 2.0*bandwidth-(1.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","bandwidth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("bandwidth") != 'undt':
            try:
                set("edges",  2.0*minb("bandwidth")-(1.0), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt':
            try:
                set("bandwidth",  maxb("edges")/2.0+1.0/2.0, ind='Max')
            except:
                pass
        return
class Theorem334(Theorem):
    def __init__(self):
        super(Theorem334, self).__init__(334, "\n", "")
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
class Theorem335(Theorem):
    def __init__(self):
        super(Theorem335, self).__init__(335, "\n", "")
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
class Theorem336(Theorem):
    def __init__(self):
        super(Theorem336, self).__init__(336, "\n", "")
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
class Theorem337(Theorem):
    def __init__(self):
        super(Theorem337, self).__init__(337, "\n", "")
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
class Theorem338(Theorem):
    def __init__(self):
        super(Theorem338, self).__init__(338, "if connected and girth >= 5.0 and mindeg >= 4.0 then \n{\n    domination <= (nodes-(maxdeg)-(mindeg*(mindeg-(3.0))/2.0))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","girth","mindeg","domination","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and (minb("girth") != 'undt' and minb("girth") >= 5.0) and (minb("mindeg") != 'undt' and minb("mindeg") >= 4.0):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("domination",  (maxb("nodes")-(minb("maxdeg"))-(minb("mindeg")*(minb("mindeg")-(3.0))/2.0))/2.0, ind='Max')
                except:
                    pass
            if minb("domination") != 'undt' and minb("maxdeg") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  2.0*minb("domination")+minb("maxdeg")+minb("mindeg")**2.0/2.0-(3.0*minb("mindeg")/2.0), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(2.0*minb("domination"))-(minb("mindeg")**2.0/2.0)+3.0*minb("mindeg")/2.0+maxb("nodes"), ind='Max')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  sqrt(-(16.0*minb("domination"))-(8.0*minb("maxdeg"))+8.0*maxb("nodes")+9.0)/2.0+3.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem339(Theorem):
    def __init__(self):
        super(Theorem339, self).__init__(339, "if girth >= 5.0 then \n{\n    domination >= mindeg*numOfComponents\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","domination","mindeg","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and minb("girth") >= 5.0):
            if minb("mindeg") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("domination",  minb("mindeg")*minb("numOfComponents"), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("mindeg",  maxb("domination")/minb("numOfComponents"), ind='Max')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("numOfComponents",  maxb("domination")/minb("mindeg"), ind='Max')
                except:
                    pass
        return
class Theorem340(Theorem):
    def __init__(self):
        super(Theorem340, self).__init__(340, "if girth >= 6.0 then \n{\n    domination >= 2.0*(mindeg-(1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","domination","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and minb("girth") >= 6.0):
            if minb("mindeg") != 'undt':
                try:
                    set("domination",  2.0*(minb("mindeg")-(1.0)), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt':
                try:
                    set("mindeg",  maxb("domination")/2.0+1.0, ind='Max')
                except:
                    pass
        return
class Theorem341(Theorem):
    def __init__(self):
        super(Theorem341, self).__init__(341, "if mindeg >= 2.0 and girth >= 7.0 then \n{\n    domination >= maxdeg+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","girth","domination","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (minb("girth") != 'undt' and minb("girth") >= 7.0):
            if minb("maxdeg") != 'undt':
                try:
                    set("domination",  minb("maxdeg")+1.0, ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt':
                try:
                    set("maxdeg",  maxb("domination")-(1.0), ind='Max')
                except:
                    pass
        return
class Theorem342(Theorem):
    def __init__(self):
        super(Theorem342, self).__init__(342, "if girth >= 5.0 and girth <= nodes/2.0 then \n{\n    edges <= (nodes**2.0-(nodes*girth)+2.0*girth)/girth:useMinFor(girth)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and minb("nodes") != 'undt' and maxb("girth") <= minb("nodes")/2.0):
            if maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("edges",  (maxb("nodes")**2.0-(maxb("nodes")*minb("girth"))+2.0*minb("girth"))/minb("girth"), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  minb("girth")/2.0+sqrt(minb("girth")*(4.0*minb("edges")+minb("girth")-(8.0)))/2.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("girth",  maxb("nodes")**2.0/(minb("edges")+maxb("nodes")-(2.0)), ind='Max')
                except:
                    pass
        return
class Theorem343(Theorem):
    def __init__(self):
        super(Theorem343, self).__init__(343, "\n", "")
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
class Theorem344(Theorem):
    def __init__(self):
        super(Theorem344, self).__init__(344, "\n", "")
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
class Theorem345(Theorem):
    def __init__(self):
        super(Theorem345, self).__init__(345, "\n", "")
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
class Theorem346(Theorem):
    def __init__(self):
        super(Theorem346, self).__init__(346, "\n", "")
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
class Theorem347(Theorem):
    def __init__(self):
        super(Theorem347, self).__init__(347, "if diameter == 2.0 then \n{\n    nodes <= nodeConnec*maxdeg+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodes","nodeConnec","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)):
            if maxb("nodeConnec") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("nodeConnec")*maxb("maxdeg")+1.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodeConnec",  (minb("nodes")-(1.0))/maxb("maxdeg"), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("maxdeg",  (minb("nodes")-(1.0))/maxb("nodeConnec"), ind='Min')
                except:
                    pass
        return
class Theorem348(Theorem):
    def __init__(self):
        super(Theorem348, self).__init__(348, "if not forest and edges >= nodes+1.0-(numOfComponents) then \n{\n    nodes >= 3.0*girth/2.0+2.0*numOfComponents-(3.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt' and minb("edges") >= maxb("nodes")+1.0-(minb("numOfComponents"))):
            if minb("girth") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  3.0*minb("girth")/2.0+2.0*minb("numOfComponents")-(3.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  2.0*maxb("nodes")/3.0-(4.0*minb("numOfComponents")/3.0)+2.0, ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(3.0*minb("girth")/4.0)+maxb("nodes")/2.0+3.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem349(Theorem):
    def __init__(self):
        super(Theorem349, self).__init__(349, "if not forest and edges >= nodes+3.0 then \n{\n    nodes >= 2.0*girth+2.0*numOfComponents-(4.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","girth","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= maxb("nodes")+3.0):
            if minb("girth") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  2.0*minb("girth")+2.0*minb("numOfComponents")-(4.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  maxb("nodes")/2.0-(minb("numOfComponents"))+2.0, ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(minb("girth"))+maxb("nodes")/2.0+2.0, ind='Max')
                except:
                    pass
        return
class Theorem350(Theorem):
    def __init__(self):
        super(Theorem350, self).__init__(350, "if not forest and edges >= nodes+4.0-(numOfComponents) then \n{\n    nodes >= 9.0*girth/4.0+2.0*numOfComponents-(5.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","numOfComponents","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt' and minb("edges") >= maxb("nodes")+4.0-(minb("numOfComponents"))):
            if minb("girth") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  9.0*minb("girth")/4.0+2.0*minb("numOfComponents")-(5.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  4.0*maxb("nodes")/9.0-(8.0*minb("numOfComponents")/9.0)+20.0/9.0, ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("numOfComponents",  -(9.0*minb("girth")/8.0)+maxb("nodes")/2.0+5.0/2.0, ind='Max')
                except:
                    pass
        return
class Theorem351(Theorem):
    def __init__(self):
        super(Theorem351, self).__init__(351, "if girth >= maximum((nodes+1.0)/2.0, 5.0) and edges >= nodes+3.0 then \n{\n    if girth <= 7.0 then \n    {\n        girth <= 6.0\n    }\n    else  \n    {\n        girth <= 8.0\n    },\n    nodes == 2.0*girth-(1.0),\n    nodeConnec == 2.0,\n    edgeConnec == 2.0,\n    mindeg == 2.0,\n    edges == nodes+3.0,\n    not planar\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","nodes","edges","nodeConnec","edgeConnec","mindeg","planar"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and maxb("nodes") != 'undt' and minb("girth") >= maximum((maxb("nodes")+1.0)/2.0, 5.0)) and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= maxb("nodes")+3.0):
            if (maxb("girth") != 'undt' and maxb("girth") <= 7.0):
                try:
                    set("girth",  6.0, ind='Max')
                except:
                    pass
            elif True:
                try:
                    set("girth",  8.0, ind='Max')
                except:
                    pass
            if minb("girth") != 'undt':
                try:
                    set("nodes",  2.0*minb("girth")-(1.0), ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("girth",  maxb("nodes")/2.0+1.0/2.0, ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt':
                try:
                    set("nodes",  2.0*maxb("girth")-(1.0), ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("girth",  minb("nodes")/2.0+1.0/2.0, ind='Min')
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
            try:
                set("edgeConnec",  2.0, ind='Min')
            except:
                pass
            try:
                set("edgeConnec",  2.0, ind='Max')
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
            if minb("nodes") != 'undt':
                try:
                    set("edges",  minb("nodes")+3.0, ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt':
                try:
                    set("nodes",  maxb("edges")-(3.0), ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("edges",  maxb("nodes")+3.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt':
                try:
                    set("nodes",  minb("edges")-(3.0), ind='Min')
                except:
                    pass
            set("planar", False)
        return
class Theorem352(Theorem):
    def __init__(self):
        super(Theorem352, self).__init__(352, "_t is floor((minb(girth)-(1.0))/2.0);\nif minb(mindeg) <= 2.0 then \n{\n    _s is (_t-(1.0))\n}\nelse  \n{\n    _s is ((minb(mindeg)-(1.0))**(_t-(1.0))-(1.0))/(minb(mindeg)-(2.0))\n};\nif minb(girth) >= 5.0 then \n{\n    edges <= maxb(nodes)*(0.5+sqrt((maxb(nodes)-(minb(mindeg))-(1.0))/_s+0.25))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","edges","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt':
            _t = floor((minb("girth")-(1.0))/2.0)
        if (minb("mindeg") != 'undt' and minb("mindeg") <= 2.0):
            _s = (_t-(1.0))
        elif True:
            if minb("mindeg") != 'undt':
                _s = ((minb("mindeg")-(1.0))**(_t-(1.0))-(1.0))/(minb("mindeg")-(2.0))
        if (minb("girth") != 'undt' and minb("girth") >= 5.0):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("edges",  maxb("nodes")*(0.5+sqrt((maxb("nodes")-(minb("mindeg"))-(1.0))/_s+0.25))/2.0, ind='Max')
                except:
                    pass
        return
class Theorem353(Theorem):
    def __init__(self):
        super(Theorem353, self).__init__(353, "_t is floor((minb(girth))/2.0);\n_k is floor(minb(edges)/maxb(nodes));\nif _k <= 1.0 then \n{\n    _r is _t-(1.0)\n}\nelse  \n{\n    _r is (k**(t-(1.0))-(1.0))/(k-(1.0))\n};\nif minb(girth) >= 5.0 then \n{\n    edges <= maxb(nodes)*(0.5+sqrt((maxb(nodes)-(_k)-(2.0))/_r+0.25))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","edges","nodes","k","t"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("girth") != 'undt':
            _t = floor((minb("girth"))/2.0)
        if minb("edges") != 'undt' and maxb("nodes") != 'undt':
            _k = floor(minb("edges")/maxb("nodes"))
        if ('_k' in vars() and _k <= 1.0):
            _r = _t-(1.0)
        elif True:
            _r = ("k"**("t"-(1.0))-(1.0))/("k"-(1.0))
        if (minb("girth") != 'undt' and minb("girth") >= 5.0):
            if maxb("nodes") != 'undt':
                try:
                    set("edges",  maxb("nodes")*(0.5+sqrt((maxb("nodes")-(_k)-(2.0))/_r+0.25))/2.0, ind='Max')
                except:
                    pass
        return
class Theorem354(Theorem):
    def __init__(self):
        super(Theorem354, self).__init__(354, "let k = floor((nodes-(floor((girth-(1.0))/2.0)))/girth);\nif not forest then \n{\n    nosolve edges <= nodes+k*(2.0*nodes-(girth*(k-(1.0))))/(2.0*floor((girth-(1.0))/4.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["forest","edges","nodes","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("forest") == False:
            if maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("edges",  maxb("nodes")+floor((maxb("nodes")-(floor((minb("girth")-(1.0))/2.0)))/minb("girth"))*(2.0*maxb("nodes")-(minb("girth")*(floor((maxb("nodes")-(floor((minb("girth")-(1.0))/2.0)))/minb("girth"))-(1.0))))/(2.0*floor((minb("girth")-(1.0))/4.0)), ind='Max')
                except:
                    pass
        return
class Theorem355(Theorem):
    def __init__(self):
        super(Theorem355, self).__init__(355, "\n", "")
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
class Theorem356(Theorem):
    def __init__(self):
        super(Theorem356, self).__init__(356, "if regular and edgeInd < nodes/2.0 then \n{\n    edgeChromatic == maxdeg+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","edgeInd","nodes","edgeChromatic","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (maxb("edgeInd") != 'undt' and minb("nodes") != 'undt' and maxb("edgeInd") < minb("nodes")/2.0):
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
class Theorem357(Theorem):
    def __init__(self):
        super(Theorem357, self).__init__(357, "\n", "")
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
class Theorem358(Theorem):
    def __init__(self):
        super(Theorem358, self).__init__(358, "if nodeConnec >= 2.0 and mindeg >= (nodes+nodeConnec)/3.0 then \n{\n    hamiltonian\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","mindeg","nodes","hamiltonian"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 2.0) and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and maxb("nodeConnec") != 'undt' and minb("mindeg") >= (maxb("nodes")+maxb("nodeConnec"))/3.0):
            set("hamiltonian", True)
        return
class Theorem359(Theorem):
    def __init__(self):
        super(Theorem359, self).__init__(359, "if nodeConnec >= 3.0 then \n{\n    circumference >= minimum(nodes, 3.0*mindeg-(nodeConnec))\n};\n", "")
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
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") >= 3.0):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("circumference",  minimum(minb("nodes"), 3.0*minb("mindeg")-(maxb("nodeConnec"))), ind='Min')
                except:
                    pass
        return
class Theorem360(Theorem):
    def __init__(self):
        super(Theorem360, self).__init__(360, "if regular and nodes == 2.0*maxdeg+1.0 then \n{\n    nodeConnec >= nodeInd\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","nodeConnec","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and ((minb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and minb("nodes") >= 2.0*maxb("maxdeg")+1.0) and (maxb("nodes") != 'undt' and minb("maxdeg") != 'undt' and maxb("nodes") <= 2.0*minb("maxdeg")+1.0)):
            if minb("nodeInd") != 'undt':
                try:
                    set("nodeConnec",  minb("nodeInd"), ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt':
                try:
                    set("nodeInd",  maxb("nodeConnec"), ind='Max')
                except:
                    pass
        return
class Theorem361(Theorem):
    def __init__(self):
        super(Theorem361, self).__init__(361, "let t = ((girth-(1.0))/2.0);\nif g >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeInd >= maxdeg*((t+1.0)/2.0)+1.0\n}\nelse if g >= 4.0 and mindeg == 2.0 and odd t then \n{\n    nodeInd >= maxdeg*((t+1.0)/2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["g","mindeg","girth","nodeInd","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("g") != 'undt' and minb("g") >= 4.0) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and evenInvar((("girth"-(1.0))/2.0)):
            if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                try:
                    set("nodeInd",  minb("maxdeg")*((((minb("girth")-(1.0))/2.0)+1.0)/2.0)+1.0, ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("maxdeg",  4.0*(maxb("nodeInd")-(1.0))/(minb("girth")+1.0), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("girth",  (-(minb("maxdeg"))+4.0*maxb("nodeInd")-(4.0))/minb("maxdeg"), ind='Max')
                except:
                    pass
        elif (minb("g") != 'undt' and minb("g") >= 4.0) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and oddInvar((("girth"-(1.0))/2.0)):
            if minb("maxdeg") != 'undt' and minb("girth") != 'undt':
                try:
                    set("nodeInd",  minb("maxdeg")*((((minb("girth")-(1.0))/2.0)+1.0)/2.0), ind='Min')
                except:
                    pass
            if maxb("nodeInd") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("maxdeg",  4.0*maxb("nodeInd")/(minb("girth")+1.0), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("girth",  (-(minb("maxdeg"))+4.0*maxb("nodeInd"))/minb("maxdeg"), ind='Max')
                except:
                    pass
        return
class Theorem362(Theorem):
    def __init__(self):
        super(Theorem362, self).__init__(362, "\n", "")
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
class Theorem363(Theorem):
    def __init__(self):
        super(Theorem363, self).__init__(363, "\n", "")
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
class Theorem364(Theorem):
    def __init__(self):
        super(Theorem364, self).__init__(364, "\n", "")
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
class Theorem365(Theorem):
    def __init__(self):
        super(Theorem365, self).__init__(365, "if bipartite then \n{\n    if odd nodes then \n    {\n        crossing <= (nodes/4.0)**2.0*((nodes-(2.0))/4.0)**2.0\n    }\n    else  \n    {\n        crossing <= ((nodes+1.0)/4.0)*((nodes-(1.0))/4.0)**2.0*(nodes-(3.0))/4.0\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","nodes","crossing"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("bipartite") == True:
            if oddInvar("nodes"):
                if maxb("nodes") != 'undt':
                    try:
                        set("crossing",  (maxb("nodes")/4.0)**2.0*((maxb("nodes")-(2.0))/4.0)**2.0, ind='Max')
                    except:
                        pass
                if minb("crossing") != 'undt':
                    try:
                        set("nodes",  sqrt(16.0*sqrt(minb("crossing"))+1.0)+1.0, ind='Min')
                    except:
                        pass
            elif True:
                if maxb("nodes") != 'undt':
                    try:
                        set("crossing",  ((maxb("nodes")+1.0)/4.0)*((maxb("nodes")-(1.0))/4.0)**2.0*(maxb("nodes")-(3.0))/4.0, ind='Max')
                    except:
                        pass
                if minb("crossing") != 'undt':
                    try:
                        set("nodes",  sqrt(2.0)*sqrt(sqrt(64.0*minb("crossing")+1.0)+1.0)+1.0, ind='Min')
                    except:
                        pass
        return
class Theorem366(Theorem):
    def __init__(self):
        super(Theorem366, self).__init__(366, "if connected then \n{\n    nosolve spectralRadius >= 2.0*cos(3.14159265358979/(nodes+1.0)):useMinFor(nodes)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","spectralRadius","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True:
            if minb("nodes") != 'undt':
                try:
                    set("spectralRadius",  2.0*cos(3.14159265358979/(minb("nodes")+1.0)), ind='Min')
                except:
                    pass
        return
class Theorem367(Theorem):
    def __init__(self):
        super(Theorem367, self).__init__(367, "if regular and mindeg >= 7.0 and odd mindeg and (mindeg > 9.0 or mindeg < 9.0) and not bipartite and girth == 4.0 then \n{\n    nodes >= 2.0*(5.0*mindeg/4.0)+4.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","bipartite","girth","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (minb("mindeg") != 'undt' and minb("mindeg") >= 7.0) and oddInvar("mindeg") and ((minb("mindeg") != 'undt' and minb("mindeg") > 9.0) or (maxb("mindeg") != 'undt' and maxb("mindeg") < 9.0)) and get("bipartite") == False and ((minb("girth") != 'undt' and minb("girth") >= 4.0) and (maxb("girth") != 'undt' and maxb("girth") <= 4.0)):
            if minb("mindeg") != 'undt':
                try:
                    set("nodes",  2.0*(5.0*minb("mindeg")/4.0)+4.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("mindeg",  2.0*maxb("nodes")/5.0-(8.0/5.0), ind='Max')
                except:
                    pass
        return
class Theorem368(Theorem):
    def __init__(self):
        super(Theorem368, self).__init__(368, "if bipartite then \n{\n    thickness <= nodes/8.0+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","thickness","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("bipartite") == True:
            if maxb("nodes") != 'undt':
                try:
                    set("thickness",  maxb("nodes")/8.0+2.0, ind='Max')
                except:
                    pass
            if minb("thickness") != 'undt':
                try:
                    set("nodes",  8.0*minb("thickness")-(16.0), ind='Min')
                except:
                    pass
        return
class Theorem369(Theorem):
    def __init__(self):
        super(Theorem369, self).__init__(369, "if maxClique <= 2.0 then \n{\n    thickness <= genus+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","thickness","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0):
            if maxb("genus") != 'undt':
                try:
                    set("thickness",  maxb("genus")+1.0, ind='Max')
                except:
                    pass
            if minb("thickness") != 'undt':
                try:
                    set("genus",  minb("thickness")-(1.0), ind='Min')
                except:
                    pass
        return
class Theorem370(Theorem):
    def __init__(self):
        super(Theorem370, self).__init__(370, "if genus <= 1.0 then \n{\n    thickness == genus+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("genus") != 'undt' and maxb("genus") <= 1.0):
            if minb("genus") != 'undt':
                try:
                    set("thickness",  minb("genus")+1.0, ind='Min')
                except:
                    pass
            if maxb("thickness") != 'undt':
                try:
                    set("genus",  maxb("thickness")-(1.0), ind='Max')
                except:
                    pass
            if maxb("genus") != 'undt':
                try:
                    set("thickness",  maxb("genus")+1.0, ind='Max')
                except:
                    pass
            if minb("thickness") != 'undt':
                try:
                    set("genus",  minb("thickness")-(1.0), ind='Min')
                except:
                    pass
        return
class Theorem371(Theorem):
    def __init__(self):
        super(Theorem371, self).__init__(371, "arboricity <= edgeArboricity;\n", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","edgeArboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeArboricity") != 'undt':
            try:
                set("arboricity",  maxb("edgeArboricity"), ind='Max')
            except:
                pass
        if minb("arboricity") != 'undt':
            try:
                set("edgeArboricity",  minb("arboricity"), ind='Min')
            except:
                pass
        return
class Theorem372(Theorem):
    def __init__(self):
        super(Theorem372, self).__init__(372, "thickness <= edgeArboricity;\n", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","edgeArboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("edgeArboricity") != 'undt':
            try:
                set("thickness",  maxb("edgeArboricity"), ind='Max')
            except:
                pass
        if minb("thickness") != 'undt':
            try:
                set("edgeArboricity",  minb("thickness"), ind='Min')
            except:
                pass
        return
class Theorem373(Theorem):
    def __init__(self):
        super(Theorem373, self).__init__(373, "if genus >= 1.0 then \n{\n    edgeArboricity <= 2.0+sqrt(3.0*genus)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","edgeArboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("genus") != 'undt' and minb("genus") >= 1.0):
            if maxb("genus") != 'undt':
                try:
                    set("edgeArboricity",  2.0+sqrt(3.0*maxb("genus")), ind='Max')
                except:
                    pass
            if minb("edgeArboricity") != 'undt':
                try:
                    set("genus",  1.5625e26*(minb("edgeArboricity")-(2.0))**2.0/4.6875000000000146e26, ind='Min')
                except:
                    pass
        return
class Theorem374(Theorem):
    def __init__(self):
        super(Theorem374, self).__init__(374, "thickness <= 5.0+sqrt(2.0*genus-(2.0));\n", "")
    def involves(self, str_invar):
        return str_invar in ["thickness","genus"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("genus") != 'undt':
            try:
                set("thickness",  5.0+sqrt(2.0*maxb("genus")-(2.0)), ind='Max')
            except:
                pass
        if minb("thickness") != 'undt':
            try:
                set("genus",  (minb("thickness")-(5.0))**2.0/2.0+1.0, ind='Min')
            except:
                pass
        return
class Theorem375(Theorem):
    def __init__(self):
        super(Theorem375, self).__init__(375, "\n", "")
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
class Theorem376(Theorem):
    def __init__(self):
        super(Theorem376, self).__init__(376, "\n", "")
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
class Theorem377(Theorem):
    def __init__(self):
        super(Theorem377, self).__init__(377, "edgeArboricity <= (maxdeg+2.0)/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeArboricity","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("maxdeg") != 'undt':
            try:
                set("edgeArboricity",  (maxb("maxdeg")+2.0)/2.0, ind='Max')
            except:
                pass
        if minb("edgeArboricity") != 'undt':
            try:
                set("maxdeg",  2.0*minb("edgeArboricity")-(2.0), ind='Min')
            except:
                pass
        return
class Theorem378(Theorem):
    def __init__(self):
        super(Theorem378, self).__init__(378, "edgeArboricity >= (mindeg+1.0)/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeArboricity","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("mindeg") != 'undt':
            try:
                set("edgeArboricity",  (minb("mindeg")+1.0)/2.0, ind='Min')
            except:
                pass
        if maxb("edgeArboricity") != 'undt':
            try:
                set("mindeg",  2.0*maxb("edgeArboricity")-(1.0), ind='Max')
            except:
                pass
        return
class Theorem379(Theorem):
    def __init__(self):
        super(Theorem379, self).__init__(379, "edgeArboricity >= edges/(nodes-(numOfComponents));\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeArboricity","edges","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("edges") != 'undt' and minb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
            try:
                set("edgeArboricity",  minb("edges")/(maxb("nodes")-(minb("numOfComponents"))), ind='Min')
            except:
                pass
        if maxb("edgeArboricity") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
            try:
                set("edges",  maxb("edgeArboricity")*(maxb("nodes")-(minb("numOfComponents"))), ind='Max')
            except:
                pass
        if minb("numOfComponents") != 'undt' and minb("edges") != 'undt' and minb("edgeArboricity") != 'undt':
            try:
                set("nodes",  minb("numOfComponents")+minb("edges")/maxb("edgeArboricity"), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt' and maxb("edgeArboricity") != 'undt':
            try:
                set("numOfComponents",  maxb("nodes")-(minb("edges")/maxb("edgeArboricity")), ind='Max')
            except:
                pass
        return
class Theorem380(Theorem):
    def __init__(self):
        super(Theorem380, self).__init__(380, "edgeArboricity <= 3.0*thickness;\n", "")
    def involves(self, str_invar):
        return str_invar in ["edgeArboricity","thickness"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("thickness") != 'undt':
            try:
                set("edgeArboricity",  3.0*maxb("thickness"), ind='Max')
            except:
                pass
        if minb("edgeArboricity") != 'undt':
            try:
                set("thickness",  minb("edgeArboricity")/3.0, ind='Min')
            except:
                pass
        return
class Theorem381(Theorem):
    def __init__(self):
        super(Theorem381, self).__init__(381, "if planar and nodes >= 4.0 then \n{\n    edges <= 3.0*nodes-(9.0)+minimum(3.0, edgeConnec)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","nodes","edges","edgeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True and (minb("nodes") != 'undt' and minb("nodes") >= 4.0):
            if maxb("nodes") != 'undt' and maxb("edgeConnec") != 'undt':
                try:
                    set("edges",  3.0*maxb("nodes")-(9.0)+minimum(3.0, maxb("edgeConnec")), ind='Max')
                except:
                    pass
            if minb("edgeConnec") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  -(minimum(3.0, maxb("edgeConnec"))/3.0)+minb("edges")/3.0+3.0, ind='Min')
                except:
                    pass
        return
class Theorem382(Theorem):
    def __init__(self):
        super(Theorem382, self).__init__(382, "if planer and edgeConnec < mindeg and (nodes >= 5.0 or mindeg >= 2.0) then \n{\n    if mindeg == edgeConnec+1.0 and mindeg == 1.0 then \n    {\n        edges <= 3.0*nodes-(11.0)\n    }\n    else  \n    {\n        edges <= 3.0*nodes-(12.0)+nodeConnec\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planer","edgeConnec","mindeg","nodes","edges","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planer") == True and (maxb("edgeConnec") != 'undt' and minb("mindeg") != 'undt' and maxb("edgeConnec") < minb("mindeg")) and ((minb("nodes") != 'undt' and minb("nodes") >= 5.0) or (minb("mindeg") != 'undt' and minb("mindeg") >= 2.0)):
            if ((minb("mindeg") != 'undt' and maxb("edgeConnec") != 'undt' and minb("mindeg") >= maxb("edgeConnec")+1.0) and (maxb("mindeg") != 'undt' and minb("edgeConnec") != 'undt' and maxb("mindeg") <= minb("edgeConnec")+1.0)) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 1.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 1.0)):
                if maxb("nodes") != 'undt':
                    try:
                        set("edges",  3.0*maxb("nodes")-(11.0), ind='Max')
                    except:
                        pass
                if minb("edges") != 'undt':
                    try:
                        set("nodes",  minb("edges")/3.0+11.0/3.0, ind='Min')
                    except:
                        pass
            elif True:
                if maxb("nodes") != 'undt' and maxb("nodeConnec") != 'undt':
                    try:
                        set("edges",  3.0*maxb("nodes")-(12.0)+maxb("nodeConnec"), ind='Max')
                    except:
                        pass
                if minb("edges") != 'undt' and minb("nodeConnec") != 'undt':
                    try:
                        set("nodes",  minb("edges")/3.0-(maxb("nodeConnec")/3.0)+4.0, ind='Min')
                    except:
                        pass
                if minb("edges") != 'undt' and minb("nodes") != 'undt':
                    try:
                        set("nodeConnec",  minb("edges")-(3.0*maxb("nodes"))+12.0, ind='Min')
                    except:
                        pass
        return
class Theorem383(Theorem):
    def __init__(self):
        super(Theorem383, self).__init__(383, "\n", "")
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
class Theorem384(Theorem):
    def __init__(self):
        super(Theorem384, self).__init__(384, "nodeCover <= (2.0*nodes+edges-(edgeInd))/4.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","edges","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt' and maxb("edgeInd") != 'undt':
            try:
                set("nodeCover",  (2.0*maxb("nodes")+maxb("edges")-(minb("edgeInd")))/4.0, ind='Max')
            except:
                pass
        if minb("edgeInd") != 'undt' and minb("edges") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("nodes",  minb("edgeInd")/2.0-(maxb("edges")/2.0)+2.0*minb("nodeCover"), ind='Min')
            except:
                pass
        if minb("edgeInd") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edges",  minb("edgeInd")+4.0*minb("nodeCover")-(2.0*maxb("nodes")), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edgeInd",  maxb("edges")-(4.0*minb("nodeCover"))+2.0*maxb("nodes"), ind='Max')
            except:
                pass
        return
class Theorem385(Theorem):
    def __init__(self):
        super(Theorem385, self).__init__(385, "if genus <= nodes*(sqrt(2.0*nodes)-(7.0))/12.0+1.0 then \n{\n    edgeCliqueCover <= nodeCover*nodeInd\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["genus","nodes","edgeCliqueCover","nodeCover","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("genus") != 'undt' and minb("nodes") != 'undt' and maxb("genus") <= minb("nodes")*(sqrt(2.0*minb("nodes"))-(7.0))/12.0+1.0):
            if maxb("nodeCover") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("edgeCliqueCover",  maxb("nodeCover")*maxb("nodeInd"), ind='Max')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("nodeCover",  minb("edgeCliqueCover")/maxb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("edgeCliqueCover") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodeInd",  minb("edgeCliqueCover")/maxb("nodeCover"), ind='Min')
                except:
                    pass
        return
class Theorem386(Theorem):
    def __init__(self):
        super(Theorem386, self).__init__(386, "if mindeg >= 2.0 then \n{\n    domination >= (girth+2.0)/3.0*numOfComponents\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","domination","girth","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 2.0):
            if minb("girth") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("domination",  (minb("girth")+2.0)/3.0*minb("numOfComponents"), ind='Min')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  3.0*maxb("domination")/minb("numOfComponents")-(2.0), ind='Max')
                except:
                    pass
            if maxb("domination") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("numOfComponents",  3.0*maxb("domination")/(minb("girth")+2.0), ind='Max')
                except:
                    pass
        return
class Theorem387(Theorem):
    def __init__(self):
        super(Theorem387, self).__init__(387, "\n", "")
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
class Theorem388(Theorem):
    def __init__(self):
        super(Theorem388, self).__init__(388, "\n", "")
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
class Theorem389(Theorem):
    def __init__(self):
        super(Theorem389, self).__init__(389, "if maxdeg >= 6.0 and maxClique <= maxdeg-(1.0) then \n{\n    nodes <= maxdeg*nodeInd-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","maxClique","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("maxdeg") != 'undt' and minb("maxdeg") >= 6.0) and (maxb("maxClique") != 'undt' and minb("maxdeg") != 'undt' and maxb("maxClique") <= minb("maxdeg")-(1.0)):
            if maxb("maxdeg") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("maxdeg")*maxb("nodeInd")-(1.0), ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("maxdeg",  (minb("nodes")+1.0)/maxb("nodeInd"), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodeInd",  (minb("nodes")+1.0)/maxb("maxdeg"), ind='Min')
                except:
                    pass
        return
class Theorem390(Theorem):
    def __init__(self):
        super(Theorem390, self).__init__(390, "if (nodes > 5.0 or nodes < 5.0) or (edges > 5.0 or edges < 5.0) or not cycle then \n{\n    if maxClique > nodeInd then \n    {\n        maxClique >= (1.0/2.0)*log(2.0*nodes*sqrt(3.14159265359879), 2.0)\n    }\n    else  \n    {\n        nodeInd >= (1.0/2.0)*log(2.0*nodes*sqrt(3.14159265359879), 2.0)\n    }\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edges","cycle","maxClique","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("nodes") != 'undt' and minb("nodes") > 5.0) or (maxb("nodes") != 'undt' and maxb("nodes") < 5.0)) or ((minb("edges") != 'undt' and minb("edges") > 5.0) or (maxb("edges") != 'undt' and maxb("edges") < 5.0)) or get("cycle") == False:
            if (minb("maxClique") != 'undt' and maxb("nodeInd") != 'undt' and minb("maxClique") > maxb("nodeInd")):
                if minb("nodes") != 'undt':
                    try:
                        set("maxClique",  (1.0/2.0)*log(2.0*minb("nodes")*sqrt(3.14159265359879), 2.0), ind='Min')
                    except:
                        pass
                if maxb("maxClique") != 'undt':
                    try:
                        set("nodes",  0.282094791773474*exp(1.38629436111989*maxb("maxClique")), ind='Max')
                    except:
                        pass
            elif True:
                if minb("nodes") != 'undt':
                    try:
                        set("nodeInd",  (1.0/2.0)*log(2.0*minb("nodes")*sqrt(3.14159265359879), 2.0), ind='Min')
                    except:
                        pass
                if maxb("nodeInd") != 'undt':
                    try:
                        set("nodes",  0.282094791773474*exp(1.38629436111989*maxb("nodeInd")), ind='Max')
                    except:
                        pass
        return
class Theorem391(Theorem):
    def __init__(self):
        super(Theorem391, self).__init__(391, "if circumference <= nodes-(mindeg) then \n{\n    edges <= nodes*(nodes-(1.0))/2.0-(mindeg*(nodes-(mindeg)-(1.0)))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","nodes","mindeg","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("circumference") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("circumference") <= minb("nodes")-(maxb("mindeg"))):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("edges",  maxb("nodes")*(maxb("nodes")-(1.0))/2.0-(minb("mindeg")*(maxb("nodes")-(minb("mindeg"))-(1.0))), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodes",  maxb("mindeg")+sqrt(8.0*minb("edges")-(4.0*maxb("mindeg")**2.0)-(4.0*maxb("mindeg"))+1.0)/2.0+1.0/2.0, ind='Min')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("mindeg",  maxb("nodes")/2.0+sqrt(4.0*maxb("edges")-(maxb("nodes")**2.0)+1.0)/2.0-(1.0/2.0), ind='Max')
                except:
                    pass
        return
class Theorem392(Theorem):
    def __init__(self):
        super(Theorem392, self).__init__(392, "if girth == 5.0 and mindeg >= 6.0 then \n{\n    nodes >= 40.0\n}\nelse if girth == 5.0 and mindeg == 5.0 then \n{\n    nodes >= 5.0\n}\nelse if girth == 5.0 and mindeg == 4.0 then \n{\n    nodes >= 19.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and maxb("girth") <= 5.0)) and (minb("mindeg") != 'undt' and minb("mindeg") >= 6.0):
            try:
                set("nodes",  40.0, ind='Min')
            except:
                pass
        elif ((minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and maxb("girth") <= 5.0)) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 5.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 5.0)):
            try:
                set("nodes",  5.0, ind='Min')
            except:
                pass
        elif ((minb("girth") != 'undt' and minb("girth") >= 5.0) and (maxb("girth") != 'undt' and maxb("girth") <= 5.0)) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 4.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 4.0)):
            try:
                set("nodes",  19.0, ind='Min')
            except:
                pass
        return
class Theorem393(Theorem):
    def __init__(self):
        super(Theorem393, self).__init__(393, "if girth == 6.0 and mindeg >= 7.0 and regular then \n{\n    nodes >= 90.0\n}\nelse if girth == 6.0 and mindeg >= 7.0 and not regular then \n{\n    nodes >= 93.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","regular","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("girth") != 'undt' and minb("girth") >= 6.0) and (maxb("girth") != 'undt' and maxb("girth") <= 6.0)) and (minb("mindeg") != 'undt' and minb("mindeg") >= 7.0) and get("regular") == True:
            try:
                set("nodes",  90.0, ind='Min')
            except:
                pass
        elif ((minb("girth") != 'undt' and minb("girth") >= 6.0) and (maxb("girth") != 'undt' and maxb("girth") <= 6.0)) and (minb("mindeg") != 'undt' and minb("mindeg") >= 7.0) and get("regular") == False:
            try:
                set("nodes",  93.0, ind='Min')
            except:
                pass
        return
class Theorem394(Theorem):
    def __init__(self):
        super(Theorem394, self).__init__(394, "if maxClique == 2.0 then \n{\n    nodeInd >= nodes*(2.0*edges/nodes*ln(2.0*edges/nodes)-(2.0*edges/nodes)+1.0)/((2.0*edges/nodes-(1.0))**2.0)\n};\n", "")
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
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if minb("nodes") != 'undt' and minb("edges") != 'undt':
                try:
                    set("nodeInd",  maxb("nodes")*(2.0*minb("edges")/maxb("nodes")*ln(2.0*minb("edges")/maxb("nodes"))-(2.0*minb("edges")/maxb("nodes"))+1.0)/((2.0*minb("edges")/maxb("nodes")-(1.0))**2.0), ind='Min')
                except:
                    pass
        return
class Theorem395(Theorem):
    def __init__(self):
        super(Theorem395, self).__init__(395, "let k = (1.0+(-(1.0))**girth)/2.0;\nlet t = floor(girth/2.0);\nif connected and not tree and mindeg == 1.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg-(k*(mindeg-(1.0))**t))\n}\nelse if connected and not tree and mindeg == 2.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg*t-(k*(mindeg-(1.0))**t))\n}\nelse if connected and not tree and mindeg >= 3.0 then \n{\n    nodes >= ceil((diameter+1.0)/(girth+k))*(1.0+mindeg*(((mindeg-(1.0))**t-(1.0))/(mindeg-(2.0)))-(k*(mindeg-(1.0))**t))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["connected","tree","mindeg","nodes","diameter","girth"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("connected") == True and get("tree") == False and ((minb("mindeg") != 'undt' and minb("mindeg") >= 1.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 1.0)):
            if minb("diameter") != 'undt' and minb("girth") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  ceil((minb("diameter")+1.0)/(maxb("girth")+(1.0+(-(1.0))**maxb("girth"))/2.0))*(1.0+minb("mindeg")-((1.0+(-(1.0))**maxb("girth"))/2.0*(minb("mindeg")-(1.0))**floor(maxb("girth")/2.0))), ind='Min')
                except:
                    pass
        elif get("connected") == True and get("tree") == False and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)):
            if minb("diameter") != 'undt' and minb("girth") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  ceil((minb("diameter")+1.0)/(minb("girth")+(1.0+(-(1.0))**minb("girth"))/2.0))*(1.0+minb("mindeg")*floor(minb("girth")/2.0)-((1.0+(-(1.0))**minb("girth"))/2.0*(minb("mindeg")-(1.0))**floor(minb("girth")/2.0))), ind='Min')
                except:
                    pass
        elif get("connected") == True and get("tree") == False and (minb("mindeg") != 'undt' and minb("mindeg") >= 3.0):
            if minb("diameter") != 'undt' and minb("girth") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  ceil((minb("diameter")+1.0)/(maxb("girth")+(1.0+(-(1.0))**maxb("girth"))/2.0))*(1.0+minb("mindeg")*(((minb("mindeg")-(1.0))**floor(maxb("girth")/2.0)-(1.0))/(minb("mindeg")-(2.0)))-((1.0+(-(1.0))**maxb("girth"))/2.0*(minb("mindeg")-(1.0))**floor(maxb("girth")/2.0))), ind='Min')
                except:
                    pass
        return
class Theorem396(Theorem):
    def __init__(self):
        super(Theorem396, self).__init__(396, "\n", "")
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
class Theorem397(Theorem):
    def __init__(self):
        super(Theorem397, self).__init__(397, "if girth >= 5.0+log(maximum(1.0, genus), 3.0) then \n{\n    arboricity <= 2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","genus","arboricity"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and maxb("genus") != 'undt' and minb("girth") >= 5.0+log(maximum(1.0, maxb("genus")), 3.0)):
            try:
                set("arboricity",  2.0, ind='Max')
            except:
                pass
        return
class Theorem398(Theorem):
    def __init__(self):
        super(Theorem398, self).__init__(398, "if mindeg >= 2.0 then \n{\n    nodes >= girth*numOfComponents+maxdeg-(2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","girth","numOfComponents","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and minb("mindeg") >= 2.0):
            if minb("girth") != 'undt' and minb("numOfComponents") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  minb("girth")*minb("numOfComponents")+minb("maxdeg")-(2.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("girth",  (-(minb("maxdeg"))+maxb("nodes")+2.0)/minb("numOfComponents"), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("numOfComponents",  (-(minb("maxdeg"))+maxb("nodes")+2.0)/minb("girth"), ind='Max')
                except:
                    pass
            if maxb("girth") != 'undt' and maxb("numOfComponents") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(minb("girth")*minb("numOfComponents"))+maxb("nodes")+2.0, ind='Max')
                except:
                    pass
        return
class Theorem399(Theorem):
    def __init__(self):
        super(Theorem399, self).__init__(399, "if nodeConnec > 0.0 then \n{\n    nodeConnec >= (nodes*(maxdeg-(2.0)))/((maxdeg-(1.0))**diam+maxdeg-(3.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","nodes","maxdeg","diam"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodeConnec") != 'undt' and minb("nodeConnec") > 0.0):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt' and minb("diam") != 'undt':
                try:
                    set("nodeConnec",  (minb("nodes")*(minb("maxdeg")-(2.0)))/((minb("maxdeg")-(1.0))**maxb("diam")+minb("maxdeg")-(3.0)), ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt' and maxb("maxdeg") != 'undt' and maxb("diam") != 'undt':
                try:
                    set("nodes",  maxb("nodeConnec")*(maxb("maxdeg")+(maxb("maxdeg")-(1.0))**maxb("diam")-(3.0))/(maxb("maxdeg")-(2.0)), ind='Max')
                except:
                    pass
        return
class Theorem400(Theorem):
    def __init__(self):
        super(Theorem400, self).__init__(400, "if diameter == 2.0 and (maxdeg >= (2.0*nodes-(2.0))/3.0 and maxdeg < nodes-(4.0) or maxdeg == nodes-(2.0)) then \n{\n    edges >= 2.0*nodes-(4.0)\n}\nelse if diameter == 2.0 and (maxdeg >= (3.0*nodes-(5.0))/5.0 and maxdeg < (2.0*nodes-(2.0))/3.0) then \n{\n    edges >= 3.0*nodes-(maxdeg)-(6.0)\n}\nelse if diameter == 2.0 and (maxdeg >= (5.0*nodes-(3.0))/9.0 and maxdeg < (3.0*nodes-(5.0))/5.0) then \n{\n    edges >= 5.0*nodes-(4.0*maxdeg)-(10.0)\n}\nelse if diameter == 2.0 and (maxdeg >= (nodes+1.0)/2.0 and maxdeg < (5.0*nodes-(3.0))/9.0) then \n{\n    edges >= 4.0*nodes-(2.0*maxdeg)-(13.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= (2.0*maxb("nodes")-(2.0))/3.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") < minb("nodes")-(4.0)) or ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(2.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0)))):
            if minb("nodes") != 'undt':
                try:
                    set("edges",  2.0*minb("nodes")-(4.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt':
                try:
                    set("nodes",  maxb("edges")/2.0+2.0, ind='Max')
                except:
                    pass
        elif ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= (3.0*maxb("nodes")-(5.0))/5.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") < (2.0*minb("nodes")-(2.0))/3.0)):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edges",  3.0*minb("nodes")-(maxb("maxdeg"))-(6.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("edges")/3.0+maxb("maxdeg")/3.0+2.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(maxb("edges"))+3.0*minb("nodes")-(6.0), ind='Min')
                except:
                    pass
        elif ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= (5.0*maxb("nodes")-(3.0))/9.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") < (3.0*minb("nodes")-(5.0))/5.0)):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edges",  5.0*minb("nodes")-(4.0*maxb("maxdeg"))-(10.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("edges")/5.0+4.0*maxb("maxdeg")/5.0+2.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(maxb("edges")/4.0)+5.0*minb("nodes")/4.0-(5.0/2.0), ind='Min')
                except:
                    pass
        elif ((minb("diameter") != 'undt' and minb("diameter") >= 2.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 2.0)) and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= (maxb("nodes")+1.0)/2.0) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") < (5.0*minb("nodes")-(3.0))/9.0)):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edges",  4.0*minb("nodes")-(2.0*maxb("maxdeg"))-(13.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("edges")/4.0+maxb("maxdeg")/2.0+13.0/4.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(maxb("edges")/2.0)+2.0*minb("nodes")-(13.0/2.0), ind='Min')
                except:
                    pass
        return
class Theorem401(Theorem):
    def __init__(self):
        super(Theorem401, self).__init__(401, "if planar and edges == 3.0*nodes-(6.0) and maxdeg <= mindeg+1.0 then \n{\n    mindeg == nodeConnec\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","edges","nodes","maxdeg","mindeg","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True and ((minb("edges") != 'undt' and maxb("nodes") != 'undt' and minb("edges") >= 3.0*maxb("nodes")-(6.0)) and (maxb("edges") != 'undt' and minb("nodes") != 'undt' and maxb("edges") <= 3.0*minb("nodes")-(6.0))) and (maxb("maxdeg") != 'undt' and minb("mindeg") != 'undt' and maxb("maxdeg") <= minb("mindeg")+1.0):
            if minb("nodeConnec") != 'undt':
                try:
                    set("mindeg",  minb("nodeConnec"), ind='Min')
                except:
                    pass
            if maxb("mindeg") != 'undt':
                try:
                    set("nodeConnec",  maxb("mindeg"), ind='Max')
                except:
                    pass
            if maxb("nodeConnec") != 'undt':
                try:
                    set("mindeg",  maxb("nodeConnec"), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt':
                try:
                    set("nodeConnec",  minb("mindeg"), ind='Min')
                except:
                    pass
        return
class Theorem402(Theorem):
    def __init__(self):
        super(Theorem402, self).__init__(402, "\n", "")
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
class Theorem403(Theorem):
    def __init__(self):
        super(Theorem403, self).__init__(403, "\n", "")
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
class Theorem404(Theorem):
    def __init__(self):
        super(Theorem404, self).__init__(404, "if mindeg > edgeConnec and edgeConnec == nodeConnec then \n{\n    nodes >= mindeg+maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeConnec","nodeConnec","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and maxb("edgeConnec") != 'undt' and minb("mindeg") > maxb("edgeConnec")) and ((minb("edgeConnec") != 'undt' and maxb("nodeConnec") != 'undt' and minb("edgeConnec") >= maxb("nodeConnec")) and (maxb("edgeConnec") != 'undt' and minb("nodeConnec") != 'undt' and maxb("edgeConnec") <= minb("nodeConnec"))):
            if minb("mindeg") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  minb("mindeg")+minb("maxdeg"), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  -(minb("maxdeg"))+maxb("nodes"), ind='Max')
                except:
                    pass
            if maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  -(minb("mindeg"))+maxb("nodes"), ind='Max')
                except:
                    pass
        return
class Theorem405(Theorem):
    def __init__(self):
        super(Theorem405, self).__init__(405, "if mindeg > edgeConnec and edgeConnec == nodeConnec and nodeConnec > 0.0 and diam == 3.0 then \n{\n    domination <= edgeConnec+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","edgeConnec","nodeConnec","diam","domination"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("mindeg") != 'undt' and maxb("edgeConnec") != 'undt' and minb("mindeg") > maxb("edgeConnec")) and ((minb("edgeConnec") != 'undt' and maxb("nodeConnec") != 'undt' and minb("edgeConnec") >= maxb("nodeConnec")) and (maxb("edgeConnec") != 'undt' and minb("nodeConnec") != 'undt' and maxb("edgeConnec") <= minb("nodeConnec"))) and (minb("nodeConnec") != 'undt' and minb("nodeConnec") > 0.0) and ((minb("diam") != 'undt' and minb("diam") >= 3.0) and (maxb("diam") != 'undt' and maxb("diam") <= 3.0)):
            if maxb("edgeConnec") != 'undt':
                try:
                    set("domination",  maxb("edgeConnec")+1.0, ind='Max')
                except:
                    pass
            if minb("domination") != 'undt':
                try:
                    set("edgeConnec",  minb("domination")-(1.0), ind='Min')
                except:
                    pass
        return
class Theorem406(Theorem):
    def __init__(self):
        super(Theorem406, self).__init__(406, "\n", "")
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
class Theorem407(Theorem):
    def __init__(self):
        super(Theorem407, self).__init__(407, "domination <= (nodes-(minb(maxdeg))-(1.0))*(nodes-(minb(mindeg))-(2.0))/(nodes-(1.0))+2.0;\nnosolve maxdeg <= (domination*nodes-(domination)+mindeg*nodes-(mindeg)-(nodes**2.0)+nodes)/(mindeg-(nodes)+2.0):useMinFor(domination):useMaxFor(nodes):useMinFor(mindeg);\nnosolve mindeg <= (domination*nodes-(domination)+maxdeg*nodes-(2.0*maxdeg)-(nodes**2.0)+nodes)/(maxdeg-(nodes)+1.0):useMinFor(domination):useMaxFor(nodes):useMinFor(maxdeg);\n", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","maxdeg","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("domination",  (maxb("nodes")-(minb("maxdeg"))-(1.0))*(maxb("nodes")-(minb("mindeg"))-(2.0))/(maxb("nodes")-(1.0))+2.0, ind='Max')
            except:
                pass
        if minb("maxdeg") != 'undt' and minb("mindeg") != 'undt' and minb("domination") != 'undt':
            try:
                set("nodes",  minb("maxdeg")/2.0+minb("mindeg")/2.0+minb("domination")/2.0+sqrt(minb("maxdeg")**2.0-(2.0*minb("maxdeg")*minb("mindeg"))+2.0*minb("maxdeg")*minb("domination")-(6.0*minb("maxdeg"))+minb("mindeg")**2.0+2.0*minb("mindeg")*minb("domination")-(2.0*minb("mindeg"))+minb("domination")**2.0-(2.0*minb("domination"))+1.0)/2.0+1.0/2.0, ind='Min')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("maxdeg",  (minb("domination")*maxb("nodes")-(minb("domination"))+minb("mindeg")*maxb("nodes")-(minb("mindeg"))-(maxb("nodes")**2.0)+maxb("nodes"))/(minb("mindeg")-(maxb("nodes"))+2.0), ind='Max')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
            try:
                set("mindeg",  (minb("domination")*maxb("nodes")-(minb("domination"))+minb("maxdeg")*maxb("nodes")-(2.0*minb("maxdeg"))-(maxb("nodes")**2.0)+maxb("nodes"))/(minb("maxdeg")-(maxb("nodes"))+1.0), ind='Max')
            except:
                pass
        return
class Theorem408(Theorem):
    def __init__(self):
        super(Theorem408, self).__init__(408, "let s = floor((maxdeg+2.0-(sqrt((maxdeg+2.0)**2.0-(4.0*nodes))))/2.0);\nif diameter == 3.0 and s <= floor((nodes/2.0)**(1.0/3.0)) then \n{\n    edges >= nodes+s*(s-(1.0))/2.0-(1.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("diameter") != 'undt' and minb("diameter") >= 3.0) and (maxb("diameter") != 'undt' and maxb("diameter") <= 3.0)) and floor(("maxdeg"+2.0-(sqrt(("maxdeg"+2.0)**2.0-(4.0*"nodes"))))/2.0) <= floor(("nodes"/2.0)**(1.0/3.0)):
            if minb("nodes") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("edges",  minb("nodes")+floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)*(floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)-(1.0))/2.0-(1.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and maxb("edges") != 'undt':
                try:
                    set("nodes",  -(floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)**2.0/2.0)+floor((minb("maxdeg")+2.0-(sqrt((minb("maxdeg")+2.0)**2.0-(4.0*minb("nodes")))))/2.0)/2.0+maxb("edges")+1.0, ind='Max')
                except:
                    pass
        return
class Theorem409(Theorem):
    def __init__(self):
        super(Theorem409, self).__init__(409, "if nodes >= 4.0 and maxClique == 2.0 and hamiltonian then \n{\n    edges <= floor((nodes-(4.0))/2.0)*floor(nodes/2.0)+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxClique","hamiltonian","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("nodes") != 'undt' and minb("nodes") >= 4.0) and ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and get("hamiltonian") == True:
            if maxb("nodes") != 'undt':
                try:
                    set("edges",  floor((maxb("nodes")-(4.0))/2.0)*floor(maxb("nodes")/2.0)+2.0, ind='Max')
                except:
                    pass
        return
class Theorem410(Theorem):
    def __init__(self):
        super(Theorem410, self).__init__(410, "spectralRadius >= mindeg;\n", "")
    def involves(self, str_invar):
        return str_invar in ["spectralRadius","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("mindeg") != 'undt':
            try:
                set("spectralRadius",  minb("mindeg"), ind='Min')
            except:
                pass
        if maxb("spectralRadius") != 'undt':
            try:
                set("mindeg",  maxb("spectralRadius"), ind='Max')
            except:
                pass
        return
class Theorem411(Theorem):
    def __init__(self):
        super(Theorem411, self).__init__(411, "if isset nodes and isset mindeg then \n{\n    _k is maxb(nodes)-(floor(maxb(nodes)/(maxb(mindeg)+1.0))*(maxb(mindeg)+1.0))\n}\nelse  \n{\n    _k is 2.0\n};\nif _k > 2.0 then \n{\n    _k is 2.0\n};\nif connected and nodes >= 2.0*mindeg+2.0 then \n{\n    diameter <= 3.0*nodes/(mindeg+1.0)+_k-(3.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","mindeg","connected","diameter"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and minb("nodes") == maxb("nodes") and maxb("mindeg") != 'undt' and minb("mindeg") == maxb("mindeg"):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                _k = maxb("nodes")-(floor(maxb("nodes")/(maxb("mindeg")+1.0))*(maxb("mindeg")+1.0))
        elif True:
            _k = 2.0
        if ('_k' in vars() and _k > 2.0):
            _k = 2.0
        if get("connected") == True and (minb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodes") >= 2.0*maxb("mindeg")+2.0):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("diameter",  3.0*maxb("nodes")/(minb("mindeg")+1.0)+_k-(3.0), ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("diameter") != 'undt':
                try:
                    set("nodes",  -(_k*minb("mindeg")/3.0)-(_k/3.0)+minb("diameter")*minb("mindeg")/3.0+minb("diameter")/3.0+minb("mindeg")+1.0, ind='Min')
                except:
                    pass
            if maxb("diameter") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  (_k-(minb("diameter"))+3.0*maxb("nodes")-(3.0))/(-(_k)+minb("diameter")+3.0), ind='Max')
                except:
                    pass
        return
class Theorem412(Theorem):
    def __init__(self):
        super(Theorem412, self).__init__(412, "\n", "")
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
class Theorem413(Theorem):
    def __init__(self):
        super(Theorem413, self).__init__(413, "nosolve edges >= (nodes-(chromaticNum))**2.0/(nodeInd-(1.0))+chromaticNum*(chromaticNum-(1.0))/2.0-((nodeInd-(1.0))*((nodes-(chromaticNum))/(nodeInd-(1.0)))*((nodes-(chromaticNum))/(nodeInd-(1.0)))/2.0):useMinFor(chromaticNum);\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","chromaticNum","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("chromaticNum") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("edges",  (minb("nodes")-(minb("chromaticNum")))**2.0/(maxb("nodeInd")-(1.0))+minb("chromaticNum")*(minb("chromaticNum")-(1.0))/2.0-((maxb("nodeInd")-(1.0))*((minb("nodes")-(minb("chromaticNum")))/(maxb("nodeInd")-(1.0)))*((minb("nodes")-(minb("chromaticNum")))/(maxb("nodeInd")-(1.0)))/2.0), ind='Min')
            except:
                pass
        return
class Theorem414(Theorem):
    def __init__(self):
        super(Theorem414, self).__init__(414, "if diameter <= 4.0 then \n{\n    nosolve edges <= ((nodes-(2.0))*(nodes-(3.0))-(2.0*(nodes-(2.0))*(diameter-(4.0))*nodeConnec)-(4.0*nodeConnec*(nodeConnec+1.0))+nodeConnec**2.0*(diameter-(2.0))*(diameter-(3.0)))/2.0:useMinFor(diameter):useMinFor(nodeConnec),\n    nosolve edges <= ((nodes-(2.0))*(nodes-(3.0))-(2.0*(nodes-(2.0))*(diameter-(4.0))*nodeConnec)-(4.0*nodeConnec*(nodeConnec+1.0))+nodeConnec**2.0*(diameter-(2.0))*(diameter-(3.0)))/2.0:useMinFor(diameter):useMaxFor(nodeConnec)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edges","nodes","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("diameter") != 'undt' and maxb("diameter") <= 4.0):
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("edges",  ((maxb("nodes")-(2.0))*(maxb("nodes")-(3.0))-(2.0*(maxb("nodes")-(2.0))*(minb("diameter")-(4.0))*minb("nodeConnec"))-(4.0*minb("nodeConnec")*(minb("nodeConnec")+1.0))+minb("nodeConnec")**2.0*(minb("diameter")-(2.0))*(minb("diameter")-(3.0)))/2.0, ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt' and maxb("diameter") != 'undt' and maxb("nodeConnec") != 'undt':
                try:
                    set("edges",  ((maxb("nodes")-(2.0))*(maxb("nodes")-(3.0))-(2.0*(maxb("nodes")-(2.0))*(minb("diameter")-(4.0))*maxb("nodeConnec"))-(4.0*maxb("nodeConnec")*(maxb("nodeConnec")+1.0))+maxb("nodeConnec")**2.0*(minb("diameter")-(2.0))*(minb("diameter")-(3.0)))/2.0, ind='Max')
                except:
                    pass
        return
class Theorem415(Theorem):
    def __init__(self):
        super(Theorem415, self).__init__(415, "domination <= (nodes+2.0-(mindeg))/2.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["domination","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
            try:
                set("domination",  (maxb("nodes")+2.0-(minb("mindeg")))/2.0, ind='Max')
            except:
                pass
        if minb("domination") != 'undt' and minb("mindeg") != 'undt':
            try:
                set("nodes",  2.0*minb("domination")+minb("mindeg")-(2.0), ind='Min')
            except:
                pass
        if maxb("domination") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("mindeg",  -(2.0*minb("domination"))+maxb("nodes")+2.0, ind='Max')
            except:
                pass
        return
class Theorem416(Theorem):
    def __init__(self):
        super(Theorem416, self).__init__(416, "if even nodes and maxdeg == nodes-(2.0) and edgeChromatic == maxdeg+1.0 then \n{\n    edges >= (nodes-(2.0))**2.0/2.0+1.0+mindeg\n};\nif even nodes and maxdeg == nodes-(2.0) and edges >= (nodes-(2.0))**2.0/2.0+1.0+mindeg then \n{\n    maxdeg == nodes-(2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","maxdeg","edgeChromatic","edges","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if evenInvar("nodes") and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(2.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0))) and ((minb("edgeChromatic") != 'undt' and maxb("maxdeg") != 'undt' and minb("edgeChromatic") >= maxb("maxdeg")+1.0) and (maxb("edgeChromatic") != 'undt' and minb("maxdeg") != 'undt' and maxb("edgeChromatic") <= minb("maxdeg")+1.0)):
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("edges",  (minb("nodes")-(2.0))**2.0/2.0+1.0+minb("mindeg"), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*maxb("edges")-(2.0*minb("mindeg"))-(2.0))+2.0, ind='Max')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  maxb("edges")-((minb("nodes")-(2.0))**2.0/2.0)-(1.0), ind='Max')
                except:
                    pass
        if evenInvar("nodes") and ((minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("maxdeg") >= maxb("nodes")-(2.0)) and (maxb("maxdeg") != 'undt' and minb("nodes") != 'undt' and maxb("maxdeg") <= minb("nodes")-(2.0))) and (minb("edges") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("edges") >= (maxb("nodes")-(2.0))**2.0/2.0+1.0+maxb("mindeg")):
            if minb("nodes") != 'undt':
                try:
                    set("maxdeg",  minb("nodes")-(2.0), ind='Min')
                except:
                    pass
            if maxb("maxdeg") != 'undt':
                try:
                    set("nodes",  maxb("maxdeg")+2.0, ind='Max')
                except:
                    pass
            if maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  maxb("nodes")-(2.0), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt':
                try:
                    set("nodes",  minb("maxdeg")+2.0, ind='Min')
                except:
                    pass
        return
class Theorem417(Theorem):
    def __init__(self):
        super(Theorem417, self).__init__(417, "if maxClique <= 2.0 and maxdeg <= 3.0 then \n{\n    edges >= 13.0*nodes/2.0-(14.0*nodeInd)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0):
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("edges",  13.0*minb("nodes")/2.0-(14.0*maxb("nodeInd")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  2.0*maxb("edges")/13.0+28.0*maxb("nodeInd")/13.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeInd",  -(maxb("edges")/14.0)+13.0*minb("nodes")/28.0, ind='Min')
                except:
                    pass
        return
class Theorem418(Theorem):
    def __init__(self):
        super(Theorem418, self).__init__(418, "if maxClique <= 2.0 and maxdeg <= 2.0 then \n{\n    edges >= 7.0*nodes-(15.0*nodeInd)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0):
            if minb("nodes") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("edges",  7.0*minb("nodes")-(15.0*maxb("nodeInd")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("nodes",  maxb("edges")/7.0+15.0*maxb("nodeInd")/7.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeInd",  -(maxb("edges")/15.0)+7.0*minb("nodes")/15.0, ind='Min')
                except:
                    pass
        return
class Theorem419(Theorem):
    def __init__(self):
        super(Theorem419, self).__init__(419, "\n", "")
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
class Theorem420(Theorem):
    def __init__(self):
        super(Theorem420, self).__init__(420, "\n", "")
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
class Theorem421(Theorem):
    def __init__(self):
        super(Theorem421, self).__init__(421, "\n", "")
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
class Theorem422(Theorem):
    def __init__(self):
        super(Theorem422, self).__init__(422, "\n", "")
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
class Theorem423(Theorem):
    def __init__(self):
        super(Theorem423, self).__init__(423, "\n", "")
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
class Theorem424(Theorem):
    def __init__(self):
        super(Theorem424, self).__init__(424, "\n", "")
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
class Theorem425(Theorem):
    def __init__(self):
        super(Theorem425, self).__init__(425, "if planar then \n{\n    mindeg <= nodes-(nodeCover)+2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["planar","mindeg","nodes","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("planar") == True:
            if maxb("nodes") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("mindeg",  maxb("nodes")-(minb("nodeCover"))+2.0, ind='Max')
                except:
                    pass
            if minb("mindeg") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  minb("mindeg")+minb("nodeCover")-(2.0), ind='Min')
                except:
                    pass
            if maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  -(minb("mindeg"))+maxb("nodes")+2.0, ind='Max')
                except:
                    pass
        return
class Theorem426(Theorem):
    def __init__(self):
        super(Theorem426, self).__init__(426, "edges <= maximum((nodes-(edgeCover))*(2.0*nodes-(2.0*edgeCover)+1.0), (nodes-(edgeCover))*(nodes+edgeCover-(1.0))/2.0);\n", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("edgeCover") != 'undt':
            try:
                set("edges",  maximum((maxb("nodes")-(minb("edgeCover")))*(2.0*maxb("nodes")-(2.0*minb("edgeCover"))+1.0), (maxb("nodes")-(minb("edgeCover")))*(maxb("nodes")+minb("edgeCover")-(1.0))/2.0), ind='Max')
            except:
                pass
        return
class Theorem427(Theorem):
    def __init__(self):
        super(Theorem427, self).__init__(427, "let x = mindeg*((mindeg+3.0)/2.0)-(1.0);\nif regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and even nodes then \n{\n    edgeCover <= (nodes+2.0*((nodes+1.0)/(2.0*x)))/2.0\n}\nelse if regular and mindeg >= 3.0 and edgeConnec >= mindeg-(2.0) and odd nodes then \n{\n    edgeCover <= (nodes+maximum(2.0*((nodes+1.0+x)/(2.0*x))-(1.0), 1.0))/2.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","mindeg","edgeConnec","nodes","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (minb("mindeg") != 'undt' and minb("mindeg") >= 3.0) and (minb("edgeConnec") != 'undt' and maxb("mindeg") != 'undt' and minb("edgeConnec") >= maxb("mindeg")-(2.0)) and evenInvar("nodes"):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")+2.0*((maxb("nodes")+1.0)/(2.0*minb("mindeg")*((minb("mindeg")+3.0)/2.0)-(1.0))))/2.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt' and minb("mindeg") != 'undt':
                try:
                    set("nodes",  2.0*(minb("edgeCover")*minb("mindeg")**2.0+3.0*minb("edgeCover")*minb("mindeg")-(minb("edgeCover"))-(1.0))/(minb("mindeg")**2.0+3.0*minb("mindeg")+1.0), ind='Min')
                except:
                    pass
            if maxb("edgeCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("mindeg",  (-(6.0*maxb("edgeCover"))+3.0*minb("nodes")+sqrt((2.0*maxb("edgeCover")-(minb("nodes")))*(26.0*maxb("edgeCover")-(5.0*minb("nodes"))+8.0)))/(2.0*(2.0*maxb("edgeCover")-(minb("nodes")))), ind='Max')
                except:
                    pass
        elif get("regular") == True and (minb("mindeg") != 'undt' and minb("mindeg") >= 3.0) and (minb("edgeConnec") != 'undt' and maxb("mindeg") != 'undt' and minb("edgeConnec") >= maxb("mindeg")-(2.0)) and oddInvar("nodes"):
            if maxb("nodes") != 'undt' and maxb("mindeg") != 'undt':
                try:
                    set("edgeCover",  (maxb("nodes")+maximum(2.0*((maxb("nodes")+1.0+minb("mindeg")*((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*((minb("mindeg")+3.0)/2.0)-(1.0)))-(1.0), 1.0))/2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("mindeg") != 'undt' and minb("edgeCover") != 'undt':
                try:
                    set("nodes",  -(maximum(2.0*((maxb("nodes")+1.0+minb("mindeg")*((minb("mindeg")+3.0)/2.0)-(1.0))/(2.0*minb("mindeg")*((minb("mindeg")+3.0)/2.0)-(1.0)))-(1.0), 1.0))+2.0*minb("edgeCover"), ind='Min')
                except:
                    pass
        return
class Theorem428(Theorem):
    def __init__(self):
        super(Theorem428, self).__init__(428, "if mindeg == 3.0 and maxdeg == 3.0 then \n{\n    edgeCover <= nodes/2.0+(nodes+3.0)/18.0+(numOfComponents+4.0)/6.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","edgeCover","nodes","numOfComponents"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and minb("mindeg") >= 3.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 3.0)) and ((minb("maxdeg") != 'undt' and minb("maxdeg") >= 3.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0)):
            if maxb("nodes") != 'undt' and maxb("numOfComponents") != 'undt':
                try:
                    set("edgeCover",  maxb("nodes")/2.0+(maxb("nodes")+3.0)/18.0+(maxb("numOfComponents")+4.0)/6.0, ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt' and minb("numOfComponents") != 'undt':
                try:
                    set("nodes",  9.0*minb("edgeCover")/5.0-(3.0*maxb("numOfComponents")/10.0)-(3.0/2.0), ind='Min')
                except:
                    pass
            if minb("edgeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("numOfComponents",  6.0*minb("edgeCover")-(10.0*maxb("nodes")/3.0)-(5.0), ind='Min')
                except:
                    pass
        return
class Theorem429(Theorem):
    def __init__(self):
        super(Theorem429, self).__init__(429, "if maxClique == 2.0 and maxdeg <= 4.0 then \n{\n    edges >= 13.0*nodeCover-(7.0*nodes)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 4.0):
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  13.0*minb("nodeCover")-(7.0*maxb("nodes")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  maxb("edges")/13.0+7.0*maxb("nodes")/13.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  -(maxb("edges")/7.0)+13.0*minb("nodeCover")/7.0, ind='Min')
                except:
                    pass
        return
class Theorem430(Theorem):
    def __init__(self):
        super(Theorem430, self).__init__(430, "\n", "")
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
class Theorem431(Theorem):
    def __init__(self):
        super(Theorem431, self).__init__(431, "\n", "")
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
class Theorem432(Theorem):
    def __init__(self):
        super(Theorem432, self).__init__(432, "if mindeg == maxdeg and mindeg == 2.0 and girth >= 8.0 then \n{\n    nodeCover <= 33.0*nodes/53.0\n}\nelse if mindeg == maxdeg and mindeg == 2.0 and girth >= 6.0 then \n{\n    nodeCover <= 33.0*nodes/52.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","maxdeg","girth","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and (minb("girth") != 'undt' and minb("girth") >= 8.0):
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  33.0*maxb("nodes")/53.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  53.0*minb("nodeCover")/33.0, ind='Min')
                except:
                    pass
        elif ((minb("mindeg") != 'undt' and maxb("maxdeg") != 'undt' and minb("mindeg") >= maxb("maxdeg")) and (maxb("mindeg") != 'undt' and minb("maxdeg") != 'undt' and maxb("mindeg") <= minb("maxdeg"))) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and (minb("girth") != 'undt' and minb("girth") >= 6.0):
            if maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  33.0*maxb("nodes")/52.0, ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt':
                try:
                    set("nodes",  52.0*minb("nodeCover")/33.0, ind='Min')
                except:
                    pass
        return
class Theorem433(Theorem):
    def __init__(self):
        super(Theorem433, self).__init__(433, "if regular and nodes < 2.0*nodeCover then \n{\n    edgeChromatic == maxdeg+1.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","nodeCover","edgeChromatic","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and (maxb("nodes") != 'undt' and minb("nodeCover") != 'undt' and maxb("nodes") < 2.0*minb("nodeCover")):
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
class Theorem434(Theorem):
    def __init__(self):
        super(Theorem434, self).__init__(434, "if regular then \n{\n    edgeCover <= nodes*(maxdeg+2.0)/(2.0*(maxdeg+1.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","edgeCover","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True:
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("edgeCover",  maxb("nodes")*(minb("maxdeg")+2.0)/(2.0*(minb("maxdeg")+1.0)), ind='Max')
                except:
                    pass
            if minb("edgeCover") != 'undt' and minb("maxdeg") != 'undt':
                try:
                    set("nodes",  2.0*minb("edgeCover")*(minb("maxdeg")+1.0)/(minb("maxdeg")+2.0), ind='Min')
                except:
                    pass
            if maxb("edgeCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxdeg",  2.0*(-(minb("edgeCover"))+maxb("nodes"))/(2.0*minb("edgeCover")-(maxb("nodes"))), ind='Max')
                except:
                    pass
        return
class Theorem435(Theorem):
    def __init__(self):
        super(Theorem435, self).__init__(435, "if regular and nodes == 2.0*maxdeg+1.0 then \n{\n    nodeCover >= nodes-(nodeConnec)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["regular","nodes","maxdeg","nodeCover","nodeConnec"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if get("regular") == True and ((minb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and minb("nodes") >= 2.0*maxb("maxdeg")+1.0) and (maxb("nodes") != 'undt' and minb("maxdeg") != 'undt' and maxb("nodes") <= 2.0*minb("maxdeg")+1.0)):
            if minb("nodes") != 'undt' and minb("nodeConnec") != 'undt':
                try:
                    set("nodeCover",  minb("nodes")-(maxb("nodeConnec")), ind='Min')
                except:
                    pass
            if maxb("nodeConnec") != 'undt' and maxb("nodeCover") != 'undt':
                try:
                    set("nodes",  maxb("nodeConnec")+maxb("nodeCover"), ind='Max')
                except:
                    pass
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("nodeConnec",  -(maxb("nodeCover"))+minb("nodes"), ind='Min')
                except:
                    pass
        return
class Theorem436(Theorem):
    def __init__(self):
        super(Theorem436, self).__init__(436, "let t = ((girth-(2.0))/2.0);\nif girth >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeCover <= nodes-(maxdeg*((t+2.0)/2.0))-(1.0)\n}\nelse if girth >= 4.0 and mindeg == 2.0 and even t then \n{\n    nodeCover <= nodes-(maxdeg*((t+2.0)/2.0))\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["girth","mindeg","nodeCover","nodes","maxdeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("girth") != 'undt' and minb("girth") >= 4.0) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and evenInvar((("girth"-(2.0))/2.0)):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("nodeCover",  maxb("nodes")-(minb("maxdeg")*((((minb("girth")-(2.0))/2.0)+2.0)/2.0))-(1.0), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and minb("maxdeg") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  minb("girth")*minb("maxdeg")/4.0+minb("maxdeg")/2.0+minb("nodeCover")+1.0, ind='Min')
                except:
                    pass
            if maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("maxdeg",  4.0*(-(minb("nodeCover"))+maxb("nodes")-(1.0))/(minb("girth")+2.0), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("girth",  2.0*(-(minb("maxdeg"))-(2.0*minb("nodeCover"))+2.0*maxb("nodes")-(2.0))/minb("maxdeg"), ind='Max')
                except:
                    pass
        elif (minb("girth") != 'undt' and minb("girth") >= 4.0) and ((minb("mindeg") != 'undt' and minb("mindeg") >= 2.0) and (maxb("mindeg") != 'undt' and maxb("mindeg") <= 2.0)) and evenInvar((("girth"-(2.0))/2.0)):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("nodeCover",  maxb("nodes")-(minb("maxdeg")*((((minb("girth")-(2.0))/2.0)+2.0)/2.0)), ind='Max')
                except:
                    pass
            if minb("girth") != 'undt' and minb("maxdeg") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  minb("girth")*minb("maxdeg")/4.0+minb("maxdeg")/2.0+minb("nodeCover"), ind='Min')
                except:
                    pass
            if maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt' and maxb("girth") != 'undt':
                try:
                    set("maxdeg",  4.0*(-(minb("nodeCover"))+maxb("nodes"))/(minb("girth")+2.0), ind='Max')
                except:
                    pass
            if maxb("maxdeg") != 'undt' and maxb("nodeCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("girth",  2.0*(-(minb("maxdeg"))-(2.0*minb("nodeCover"))+2.0*maxb("nodes"))/minb("maxdeg"), ind='Max')
                except:
                    pass
        return
class Theorem437(Theorem):
    def __init__(self):
        super(Theorem437, self).__init__(437, "\n", "")
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
class Theorem438(Theorem):
    def __init__(self):
        super(Theorem438, self).__init__(438, "nodeInd >= (2.0*nodes-(edges)+edgeInd)/4.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges","edgeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("edges") != 'undt' and minb("edgeInd") != 'undt':
            try:
                set("nodeInd",  (2.0*minb("nodes")-(maxb("edges"))+minb("edgeInd"))/4.0, ind='Min')
            except:
                pass
        if maxb("edgeInd") != 'undt' and maxb("edges") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodes",  -(minb("edgeInd")/2.0)+maxb("edges")/2.0+2.0*maxb("nodeInd"), ind='Max')
            except:
                pass
        if minb("edgeInd") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edges",  minb("edgeInd")-(4.0*maxb("nodeInd"))+2.0*minb("nodes"), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edgeInd",  maxb("edges")+4.0*maxb("nodeInd")-(2.0*minb("nodes")), ind='Max')
            except:
                pass
        return
class Theorem439(Theorem):
    def __init__(self):
        super(Theorem439, self).__init__(439, "nodeCover <= (nodes+edges+edgeCover)/4.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","nodes","edges","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if maxb("nodes") != 'undt' and maxb("edges") != 'undt' and maxb("edgeCover") != 'undt':
            try:
                set("nodeCover",  (maxb("nodes")+maxb("edges")+maxb("edgeCover"))/4.0, ind='Max')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("edges") != 'undt' and minb("nodeCover") != 'undt':
            try:
                set("nodes",  -(maxb("edgeCover"))-(maxb("edges"))+4.0*minb("nodeCover"), ind='Min')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edges",  -(maxb("edgeCover"))+4.0*minb("nodeCover")-(maxb("nodes")), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edgeCover",  -(maxb("edges"))+4.0*minb("nodeCover")-(maxb("nodes")), ind='Min')
            except:
                pass
        return
class Theorem440(Theorem):
    def __init__(self):
        super(Theorem440, self).__init__(440, "nodeInd >= (3.0*nodes-(edges)-(edgeCover))/4.0;\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodes","edges","edgeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if minb("nodes") != 'undt' and minb("edges") != 'undt' and minb("edgeCover") != 'undt':
            try:
                set("nodeInd",  (3.0*minb("nodes")-(maxb("edges"))-(maxb("edgeCover")))/4.0, ind='Min')
            except:
                pass
        if maxb("edgeCover") != 'undt' and maxb("edges") != 'undt' and maxb("nodeInd") != 'undt':
            try:
                set("nodes",  maxb("edgeCover")/3.0+maxb("edges")/3.0+4.0*maxb("nodeInd")/3.0, ind='Max')
            except:
                pass
        if minb("edgeCover") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edges",  -(maxb("edgeCover"))-(4.0*maxb("nodeInd"))+3.0*minb("nodes"), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("nodeInd") != 'undt' and minb("nodes") != 'undt':
            try:
                set("edgeCover",  -(maxb("edges"))-(4.0*maxb("nodeInd"))+3.0*minb("nodes"), ind='Min')
            except:
                pass
        return
class Theorem441(Theorem):
    def __init__(self):
        super(Theorem441, self).__init__(441, "if maxdeg >= 6.0 and maxClique <= maxdeg-(1.0) then \n{\n    nodeCover <= (nodes*(maxdeg-(1.0))-(1.0))/maxdeg\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","maxClique","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (minb("maxdeg") != 'undt' and minb("maxdeg") >= 6.0) and (maxb("maxClique") != 'undt' and minb("maxdeg") != 'undt' and maxb("maxClique") <= minb("maxdeg")-(1.0)):
            if maxb("nodes") != 'undt' and maxb("maxdeg") != 'undt':
                try:
                    set("nodeCover",  (maxb("nodes")*(maxb("maxdeg")-(1.0))-(1.0))/maxb("maxdeg"), ind='Max')
                except:
                    pass
            if minb("maxdeg") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  (minb("maxdeg")*minb("nodeCover")+1.0)/(minb("maxdeg")-(1.0)), ind='Min')
                except:
                    pass
            if minb("nodes") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("maxdeg",  -((maxb("nodes")+1.0)/(minb("nodeCover")-(maxb("nodes")))), ind='Min')
                except:
                    pass
        return
class Theorem442(Theorem):
    def __init__(self):
        super(Theorem442, self).__init__(442, "\n", "")
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
class Theorem443(Theorem):
    def __init__(self):
        super(Theorem443, self).__init__(443, "\n", "")
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
class Theorem444(Theorem):
    def __init__(self):
        super(Theorem444, self).__init__(444, "\n", "")
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
class Theorem445(Theorem):
    def __init__(self):
        super(Theorem445, self).__init__(445, "\n", "")
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
class Theorem446(Theorem):
    def __init__(self):
        super(Theorem446, self).__init__(446, "if maxClique <= 2.0 and maxdeg <= 3.0 then \n{\n    edges >= 14.0*nodeCover-(15.0*nodes/2.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 3.0):
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  14.0*minb("nodeCover")-(15.0*maxb("nodes")/2.0), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  maxb("edges")/14.0+15.0*maxb("nodes")/28.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  -(2.0*maxb("edges")/15.0)+28.0*minb("nodeCover")/15.0, ind='Min')
                except:
                    pass
        return
class Theorem447(Theorem):
    def __init__(self):
        super(Theorem447, self).__init__(447, "if maxClique <= 2.0 and maxdeg <= 2.0 then \n{\n    edges >= 15.0*nodeCover-(8.0*nodes)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0) and (maxb("maxdeg") != 'undt' and maxb("maxdeg") <= 2.0):
            if minb("nodeCover") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("edges",  15.0*minb("nodeCover")-(8.0*maxb("nodes")), ind='Min')
                except:
                    pass
            if maxb("edges") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeCover",  maxb("edges")/15.0+8.0*maxb("nodes")/15.0, ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodeCover") != 'undt':
                try:
                    set("nodes",  -(maxb("edges")/8.0)+15.0*minb("nodeCover")/8.0, ind='Min')
                except:
                    pass
        return
class Theorem448(Theorem):
    def __init__(self):
        super(Theorem448, self).__init__(448, "\n", "")
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
class Theorem449(Theorem):
    def __init__(self):
        super(Theorem449, self).__init__(449, "\n", "")
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
class Theorem450(Theorem):
    def __init__(self):
        super(Theorem450, self).__init__(450, "if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes-(mindeg)-(1.0) and mindeg <= nodes-(10.0) then \n{\n    nodes <= 2.0*mindeg+2.0\n}\nelse if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes-(mindeg)-(1.0) and mindeg >= nodes-(10.0) then \n{\n    nodes <= 2.0*mindeg+3.0\n};\n", "Original Code is WRONG!")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes","mindeg"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodeInd") != 'undt' and minb("nodeCliqueCover") != 'undt' and maxb("nodeInd") < minb("nodeCliqueCover")) and ((minb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodeCliqueCover") >= maxb("nodes")-(minb("mindeg"))-(1.0)) and (maxb("nodeCliqueCover") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodeCliqueCover") <= minb("nodes")-(maxb("mindeg"))-(1.0))) and (maxb("mindeg") != 'undt' and minb("nodes") != 'undt' and maxb("mindeg") <= minb("nodes")-(10.0)):
            if maxb("mindeg") != 'undt':
                try:
                    set("nodes",  2.0*maxb("mindeg")+2.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("mindeg",  minb("nodes")/2.0-(1.0), ind='Min')
                except:
                    pass
        elif (maxb("nodeInd") != 'undt' and minb("nodeCliqueCover") != 'undt' and maxb("nodeInd") < minb("nodeCliqueCover")) and ((minb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt' and maxb("mindeg") != 'undt' and minb("nodeCliqueCover") >= maxb("nodes")-(minb("mindeg"))-(1.0)) and (maxb("nodeCliqueCover") != 'undt' and minb("nodes") != 'undt' and minb("mindeg") != 'undt' and maxb("nodeCliqueCover") <= minb("nodes")-(maxb("mindeg"))-(1.0))) and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")-(10.0)):
            if maxb("mindeg") != 'undt':
                try:
                    set("nodes",  2.0*maxb("mindeg")+3.0, ind='Max')
                except:
                    pass
            if minb("nodes") != 'undt':
                try:
                    set("mindeg",  minb("nodes")/2.0-(3.0/2.0), ind='Min')
                except:
                    pass
        return
class Theorem451(Theorem):
    def __init__(self):
        super(Theorem451, self).__init__(451, "\n", "")
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
class Theorem452(Theorem):
    def __init__(self):
        super(Theorem452, self).__init__(452, "\n", "")
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
class Theorem453(Theorem):
    def __init__(self):
        super(Theorem453, self).__init__(453, "\n", "")
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
class Theorem454(Theorem):
    def __init__(self):
        super(Theorem454, self).__init__(454, "if nodeInd <= 2.0 and mindeg >= nodes-(4.0) then \n{\n    edges <= nodes*(nodes-(14.0))/2.0+14.0*maxClique\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","edges","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0) and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")-(4.0)):
            if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt':
                try:
                    set("edges",  maxb("nodes")*(maxb("nodes")-(14.0))/2.0+14.0*maxb("maxClique"), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("maxClique") != 'undt':
                try:
                    set("nodes",  sqrt(2.0*minb("edges")-(28.0*maxb("maxClique"))+49.0)+7.0, ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxClique",  minb("edges")/14.0-(maxb("nodes")**2.0/28.0)+maxb("nodes")/2.0, ind='Min')
                except:
                    pass
        return
class Theorem455(Theorem):
    def __init__(self):
        super(Theorem455, self).__init__(455, "if nodeInd <= 2.0 and mindeg >= nodes-(3.0) then \n{\n    edges <= nodes*(nodes-(15.0))/2.0+15.0*maxClique\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","edges","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0) and (minb("mindeg") != 'undt' and maxb("nodes") != 'undt' and minb("mindeg") >= maxb("nodes")-(3.0)):
            if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt':
                try:
                    set("edges",  maxb("nodes")*(maxb("nodes")-(15.0))/2.0+15.0*maxb("maxClique"), ind='Max')
                except:
                    pass
            if minb("edges") != 'undt' and minb("maxClique") != 'undt':
                try:
                    set("nodes",  sqrt(8.0*minb("edges")-(120.0*maxb("maxClique"))+225.0)/2.0+15.0/2.0, ind='Min')
                except:
                    pass
            if minb("edges") != 'undt' and minb("nodes") != 'undt':
                try:
                    set("maxClique",  minb("edges")/15.0-(maxb("nodes")**2.0/30.0)+maxb("nodes")/2.0, ind='Min')
                except:
                    pass
        return
class Theorem456(Theorem):
    def __init__(self):
        super(Theorem456, self).__init__(456, "if maxClique == 2.0 then \n{\n    chromaticNum <= 1.0+3.0*(nodeCover+12.0)/16.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodeCover"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodeCover") != 'undt':
                try:
                    set("chromaticNum",  1.0+3.0*(maxb("nodeCover")+12.0)/16.0, ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt':
                try:
                    set("nodeCover",  16.0*minb("chromaticNum")/3.0-(52.0/3.0), ind='Min')
                except:
                    pass
        return
class Theorem457(Theorem):
    def __init__(self):
        super(Theorem457, self).__init__(457, "if maxClique == 2.0 then \n{\n    chromaticNum <= (3.0*nodes-(3.0*nodeInd)+52.0)/16.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodes","nodeInd"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("maxClique") != 'undt' and minb("maxClique") >= 2.0) and (maxb("maxClique") != 'undt' and maxb("maxClique") <= 2.0)):
            if maxb("nodes") != 'undt' and maxb("nodeInd") != 'undt':
                try:
                    set("chromaticNum",  (3.0*maxb("nodes")-(3.0*minb("nodeInd"))+52.0)/16.0, ind='Max')
                except:
                    pass
            if minb("chromaticNum") != 'undt' and minb("nodeInd") != 'undt':
                try:
                    set("nodes",  16.0*minb("chromaticNum")/3.0+minb("nodeInd")-(52.0/3.0), ind='Min')
                except:
                    pass
            if maxb("chromaticNum") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("nodeInd",  -(16.0*minb("chromaticNum")/3.0)+maxb("nodes")+52.0/3.0, ind='Max')
                except:
                    pass
        return
class Theorem458(Theorem):
    def __init__(self):
        super(Theorem458, self).__init__(458, "if nodeInd == 2.0 then \n{\n    nodeCliqueCover <= (3.0*nodes-(3.0*maxClique)+52.0)/16.0\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes","maxClique"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("nodeInd") != 'undt' and minb("nodeInd") >= 2.0) and (maxb("nodeInd") != 'undt' and maxb("nodeInd") <= 2.0)):
            if maxb("nodes") != 'undt' and maxb("maxClique") != 'undt':
                try:
                    set("nodeCliqueCover",  (3.0*maxb("nodes")-(3.0*minb("maxClique"))+52.0)/16.0, ind='Max')
                except:
                    pass
            if minb("maxClique") != 'undt' and minb("nodeCliqueCover") != 'undt':
                try:
                    set("nodes",  minb("maxClique")+16.0*minb("nodeCliqueCover")/3.0-(52.0/3.0), ind='Min')
                except:
                    pass
            if maxb("nodeCliqueCover") != 'undt' and maxb("nodes") != 'undt':
                try:
                    set("maxClique",  -(16.0*minb("nodeCliqueCover")/3.0)+maxb("nodes")+52.0/3.0, ind='Max')
                except:
                    pass
        return
