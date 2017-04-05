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
        super(Theorem5, self).__init__(5, "maxClique >= nodes**2.0/(nodes**2.0-(2.0*edges));\n", "")
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
        if maxb("nodes") != 'undt' and minb("edges") != 'undt':
            try:
                set("maxClique",  maxb("nodes")**2.0/(maxb("nodes")**2.0-(2.0*minb("edges"))), ind='Min')
            except:
                pass
        if minb("edges") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("nodes",  sqrt(2.0)*sqrt(minb("edges")*minb("maxClique")/(minb("maxClique")-(1.0))), ind='Min')
            except:
                pass
        if maxb("nodes") != 'undt' and minb("maxClique") != 'undt':
            try:
                set("edges",  maxb("nodes")**2.0*(minb("maxClique")-(1.0))/(2.0*minb("maxClique")), ind='Max')
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
        super(Theorem8, self).__init__(8, "nodes >= maxdeg+1.0+(mindeg+1.0)*(numOfComponents-(1.0));\n", "")
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
        if maxb("mindeg") != 'undt' and minb("numOfComponents") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("maxdeg",  -(maxb("mindeg")*minb("numOfComponents"))+maxb("mindeg")+maxb("nodes")-(minb("numOfComponents")), ind='Max')
            except:
                pass
        if minb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and minb("numOfComponents") != 'undt':
            try:
                set("mindeg",  (-(minb("maxdeg"))+maxb("nodes")-(minb("numOfComponents")))/(minb("numOfComponents")-(1.0)), ind='Max')
            except:
                pass
        if minb("maxdeg") != 'undt' and maxb("mindeg") != 'undt' and maxb("nodes") != 'undt':
            try:
                set("numOfComponents",  (-(minb("maxdeg"))+maxb("mindeg")+maxb("nodes"))/(maxb("mindeg")+1.0), ind='Max')
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
        super(Theorem27, self).__init__(27, "edgeCover <= nodes*maxdeg/(1.0+maxdeg);\n", "")
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
                set("maxdeg",  -(maxb("edgeCover")/(maxb("edgeCover")-(maxb("nodes")))), ind='Min')
            except:
                pass
        return
class Theorem28(Theorem):
    def __init__(self):
        super(Theorem28, self).__init__(28, "if exists diameter then \n{\n    if diameter <= 3.0 then \n    {\n        maxdeg <= nodes-(diameter)+1.0\n    }\n    else  \n    {\n        maxdeg <= nodes-(nodeConnec*(diameter-(4.0)))-(3.0)\n    }\n};\n", "")
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
            if (maxb("diameter") != 'undt' and maxb("diameter") <= 3.0):
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
                if maxb("nodes") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("maxdeg",  maxb("nodes")-(minb("nodeConnec")*(minb("diameter")-(4.0)))-(3.0), ind='Max')
                    except:
                        pass
                if minb("diameter") != 'undt' and minb("nodeConnec") != 'undt' and minb("maxdeg") != 'undt':
                    try:
                        set("nodes",  minb("diameter")*maxb("nodeConnec")+minb("maxdeg")-(4.0*maxb("nodeConnec"))+3.0, ind='Min')
                    except:
                        pass
                if maxb("maxdeg") != 'undt' and maxb("nodes") != 'undt' and maxb("diameter") != 'undt':
                    try:
                        set("nodeConnec",  (-(minb("maxdeg"))+maxb("nodes")-(3.0))/(minb("diameter")-(4.0)), ind='Max')
                    except:
                        pass
                if maxb("maxdeg") != 'undt' and maxb("nodeConnec") != 'undt' and maxb("nodes") != 'undt':
                    try:
                        set("diameter",  (-(minb("maxdeg"))+4.0*maxb("nodeConnec")+maxb("nodes")-(3.0))/maxb("nodeConnec"), ind='Max')
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
        super(Theorem59, self).__init__(59, "crossing <= (1.0/4.0)*floor(nodes/2.0)*floor((nodes-(1.0))/2.0)*floor((nodes-(2.0))/2.0)*floor((nodes-(3.0))/2.0);\nif complete and nodes <= 10.0 then \n{\n    crossing >= (1.0/4.0)*floor(nodes/2.0)*floor((nodes-(1.0))/2.0)*floor((nodes-(2.0))/2.0)*floor((nodes-(3.0))/2.0)\n};\n", "")
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

