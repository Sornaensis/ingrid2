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
        super(Theorem84, self).__init__(84, "if maxClique == 2.0 then \n{\n    arboricity <= 2.0+genus**(1.0/2.0)\n};\n", "")
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
            if minb("arboricity") != 'undt':
                try:
                    set("genus",  (minb("arboricity")-(2.0))**2.0, ind='Min')
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
        super(Theorem134, self).__init__(134, "if radius == 2.0 and diam == 2.0 and nodes == 4.0 then \n{\n    edges >= 4.0\n}\nelse if radius == 2.0 and diam == 2.0 and nodes >= 5.0 then \n{\n    edges >= 2.0*nodes-(5.0)\n};\n", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diam","nodes","edges"]
    def run(self):
        get = self.get
        set = self.set
        maxb = self.maxb
        minb = self.minb
        evenInvar = self.evenInvar
        oddInvar = self.oddInvar
        congruent = self.congruent
        if ((minb("radius") != 'undt' and minb("radius") >= 2.0) and (maxb("radius") != 'undt' and maxb("radius") <= 2.0)) and ((minb("diam") != 'undt' and minb("diam") >= 2.0) and (maxb("diam") != 'undt' and maxb("diam") <= 2.0)) and ((minb("nodes") != 'undt' and minb("nodes") >= 4.0) and (maxb("nodes") != 'undt' and maxb("nodes") <= 4.0)):
            try:
                set("edges",  4.0, ind='Min')
            except:
                pass
        elif ((minb("radius") != 'undt' and minb("radius") >= 2.0) and (maxb("radius") != 'undt' and maxb("radius") <= 2.0)) and ((minb("diam") != 'undt' and minb("diam") >= 2.0) and (maxb("diam") != 'undt' and maxb("diam") <= 2.0)) and (minb("nodes") != 'undt' and minb("nodes") >= 5.0):
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
            if (minb("nodeInd") != 'undt' and _k in vars() and minb("nodeInd") > _k):
                if minb("nodeInd") != 'undt':
                    _k = minb("nodeInd")
            elif (maxb("nodeInd") != 'undt' and _k in vars() and maxb("nodeInd") < _k):
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
        super(Theorem195, self).__init__(195, "maxClique >= nodes+(1.0/2.0)*(nodeInd-(1.0))*(nodeInd-(2.0))+(nodes/2.0)*(nodes-(1.0))+edges:useMaxFor(nodes);\n", "")
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
        if minb("nodes") != 'undt' and minb("nodeInd") != 'undt' and minb("edges") != 'undt':
            try:
                set("maxClique",  maxb("nodes")+(1.0/2.0)*(minb("nodeInd")-(1.0))*(minb("nodeInd")-(2.0))+(maxb("nodes")/2.0)*(maxb("nodes")-(1.0))+minb("edges"), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("maxClique") != 'undt' and minb("nodeInd") != 'undt':
            try:
                set("nodes",  sqrt(-(8.0*maxb("edges"))+8.0*minb("maxClique")-(4.0*maxb("nodeInd")**2.0)+12.0*maxb("nodeInd")-(7.0))/2.0-(1.0/2.0), ind='Min')
            except:
                pass
        if maxb("edges") != 'undt' and maxb("maxClique") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("nodeInd",  sqrt(-(8.0*minb("edges"))+8.0*maxb("maxClique")-(4.0*minb("nodes")**2.0)-(4.0*minb("nodes"))+1.0)/2.0+3.0/2.0, ind='Max')
            except:
                pass
        if maxb("maxClique") != 'undt' and maxb("nodeInd") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("edges",  maxb("maxClique")-(minb("nodeInd")**2.0/2.0)+3.0*minb("nodeInd")/2.0-(minb("nodes")**2.0/2.0)-(minb("nodes")/2.0)-(1.0), ind='Max')
            except:
                pass
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
