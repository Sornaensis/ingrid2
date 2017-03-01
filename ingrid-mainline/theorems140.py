from INGRID_CLASSES import Theorem
from math import floor,ceil,log,sqrt,exp
import sys

def even(n):
    if n == 'undt':
        return False
    return n % 2 == 0
def odd(n):
    if n == 'undt':
        return False
    return not even(n)

def congruence(a,b,m):
    return a-b % m == 0  

class Theorem1(Theorem):
    def __init__(self):
        super(Theorem1, self).__init__(1, "edges <= (1/2)*(nodes-1)*(nodes-2)+nodeConnec;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodeConnec != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edges', 1.0*nodeConnec+0.5*nodes**2.0-(1.5*nodes)+1.0, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        try:
            ingrid_obj.set('nodeConnec', 1.0*edges-(0.5*nodes**2.0)+1.5*nodes-(1.0), ind='Min')
        except:
            pass
        edges = ingrid_obj.get('edges', ind='Min')
        nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
        if nodeConnec != 'undt':
            try:
                ingrid_obj.set('nodes', 1.0*(2.0*edges-(2.0*nodeConnec)+0.25)**(1/2)+1.5, ind='Min')
            except:
                pass
        return

class Theorem2(Theorem):
    def __init__(self):
        super(Theorem2, self).__init__(2, "chromaticNum <= (1/2)*(nodeCover+maxClique+1);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","nodeCover"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        if maxClique != 'undt' and nodeCover != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 0.5*maxClique+0.5*nodeCover+0.5, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        if nodeCover != 'undt':
            try:
                ingrid_obj.set('maxClique', 2.0*chromaticNum-(1.0*nodeCover)-(1.0), ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if maxClique != 'undt':
            try:
                ingrid_obj.set('nodeCover', 2.0*chromaticNum-(1.0*maxClique)-(1.0), ind='Min')
            except:
                pass
        return

class Theorem3(Theorem):
    def __init__(self):
        super(Theorem3, self).__init__(3, "spectralRadius >= 2*edges/nodes;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","spectralRadius"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('spectralRadius', 2.0*edges/nodes, ind='Min')
            except:
                pass
        nodes = ingrid_obj.get('nodes', ind='Max')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
        if nodes != 'undt' and spectralRadius != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*spectralRadius*nodes, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
        if spectralRadius != 'undt':
            try:
                ingrid_obj.set('nodes', 2.0*edges/spectralRadius, ind='Min')
            except:
                pass
        return

class Theorem4(Theorem):
    def __init__(self):
        super(Theorem4, self).__init__(4, "spectralRadius <= (2*edges*nodeCover/(nodeCover+1))**(1/2);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","spectralRadius"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Max')
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        if edges != 'undt' and nodeCover != 'undt':
            try:
                ingrid_obj.set('spectralRadius', 1.4142135623731*(edges*nodeCover/(nodeCover+1.0))**0.5, ind='Max')
            except:
                pass
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        try:
            ingrid_obj.set('edges', 0.5*spectralRadius**2.0*(nodeCover+1.0)/nodeCover, ind='Min')
        except:
            pass
        edges = ingrid_obj.get('edges', ind='Max')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('nodeCover', -(0.5*spectralRadius**2.0/(0.5*spectralRadius**2.0-(edges))), ind='Min')
            except:
                pass
        return

class Theorem5(Theorem):
    def __init__(self):
        super(Theorem5, self).__init__(5, "maxClique >= nodes**2/(nodes**2-2*edges);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxClique","nodes"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('maxClique', -(1.0*nodes**2.0/(2.0*edges-(1.0*nodes**2.0))), ind='Min')
            except:
                pass
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if maxClique != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*nodes**2.0*(maxClique-(1.0))/maxClique, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        try:
            ingrid_obj.set('nodes', 1.4142135623731*(maxClique*edges/(maxClique-(1.0)))**0.5, ind='Min')
        except:
            pass
        return

class Theorem6(Theorem):
    def __init__(self):
        super(Theorem6, self).__init__(6, "spectralRadius <= maxdeg;", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","spectralRadius"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        if maxdeg != 'undt':
            try:
                ingrid_obj.set('spectralRadius', maxdeg, ind='Max')
            except:
                pass
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        try:
            ingrid_obj.set('maxdeg', spectralRadius, ind='Min')
        except:
            pass
        return

class Theorem7(Theorem):
    def __init__(self):
        super(Theorem7, self).__init__(7, "if defined diameter and mindeg > 3*nodeConnec - 1 then { nodes >= 1 + mindeg + diameter*nodeConnec + (diameter/3)*(mindeg - 3*nodeConnec + 1) } else if defined diameter then { nodes >= nodeConnec * (diameter-3) + 2*mindeg + 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","mindeg","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        return

class Theorem8(Theorem):
    def __init__(self):
        super(Theorem8, self).__init__(8, "nodes >= maxdeg + 1 + (mindeg + 1)*(numOfComponents - 1);", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","mindeg","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        try:
            ingrid_obj.set('nodes', 1.0*maxdeg+1.0*mindeg*numOfComponents-(1.0*mindeg)+1.0*numOfComponents, ind='Min')
        except:
            pass
        mindeg = ingrid_obj.get('mindeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        if mindeg != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('maxdeg', 1.0*nodes-(1.0*mindeg*numOfComponents)+1.0*mindeg-(1.0*numOfComponents), ind='Max')
            except:
                pass
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        if nodes != 'undt':
            try:
                ingrid_obj.set('mindeg', 1.0*(nodes-(maxdeg)-(numOfComponents))/(numOfComponents-(1.0)), ind='Max')
            except:
                pass
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if mindeg != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('numOfComponents', 1.0*(nodes-(maxdeg)+mindeg)/(mindeg+1.0), ind='Max')
            except:
                pass
        return

class Theorem9(Theorem):
    def __init__(self):
        super(Theorem9, self).__init__(9, "edgeCliqueCover <= nodes**2/4;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodes"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('edgeCliqueCover', 0.25*nodes**2.0, ind='Max')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        try:
            ingrid_obj.set('nodes', 2.0*edgeCliqueCover**0.5, ind='Min')
        except:
            pass
        return

class Theorem10(Theorem):
    def __init__(self):
        super(Theorem10, self).__init__(10, "diameter <= 2*radius;", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","radius"]
    def run(self, ingrid_obj):
        radius = ingrid_obj.get('radius', ind='Max')
        if radius != 'undt':
            try:
                ingrid_obj.set('diameter', 2.0*radius, ind='Max')
            except:
                pass
        diameter = ingrid_obj.get('diameter', ind='Min')
        try:
            ingrid_obj.set('radius', 0.5*diameter, ind='Min')
        except:
            pass
        return

class Theorem11(Theorem):
    def __init__(self):
        super(Theorem11, self).__init__(11, "edgeInd <= nodes / 2;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodes"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
            except:
                pass
        edgeInd = ingrid_obj.get('edgeInd', ind='Min')
        try:
            ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
        except:
            pass
        return

class Theorem12(Theorem):
    def __init__(self):
        super(Theorem12, self).__init__(12, "edgeInd >= nodes/(maxdeg + 1);", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","maxdeg","nodes"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if maxdeg != 'undt':
            try:
                ingrid_obj.set('edgeInd', 1.0*nodes/(maxdeg+1.0), ind='Min')
            except:
                pass
        edgeInd = ingrid_obj.get('edgeInd', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if edgeInd != 'undt':
            try:
                ingrid_obj.set('maxdeg', -(1.0)+1.0*nodes/edgeInd, ind='Min')
            except:
                pass
        edgeInd = ingrid_obj.get('edgeInd', ind='Max')
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        if edgeInd != 'undt' and maxdeg != 'undt':
            try:
                ingrid_obj.set('nodes', 1.0*edgeInd*(maxdeg+1.0), ind='Max')
            except:
                pass
        return

class Theorem13(Theorem):
    def __init__(self):
        super(Theorem13, self).__init__(13, "null; if g == 2*d + 1 then { regular };", "")
    def involves(self, str_invar):
        return str_invar in ["d","g","regular"]
    def run(self, ingrid_obj):
        return

class Theorem14(Theorem):
    def __init__(self):
        super(Theorem14, self).__init__(14, "null; chromaticNum >= nodes / (nodes - spectralRadius);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodes","spectralRadius"]
    def run(self, ingrid_obj):
        return

class Theorem15(Theorem):
    def __init__(self):
        super(Theorem15, self).__init__(15, "if mindeg >= 3 then { edges >= 2**(girth/2) + nodes - numOfComponents };", "")
    def involves(self, str_invar):
        return str_invar in ["edges","girth","mindeg","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        if (mindeg_Min>=3.0):
            girth = ingrid_obj.get('girth', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
            if numOfComponents != 'undt':
                try:
                    ingrid_obj.set('edges', 2.0**(0.5*girth)+nodes-(numOfComponents), ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
            if edges != 'undt' and numOfComponents != 'undt':
                try:
                    ingrid_obj.set('girth', 2.88539008177793*log(edges-(nodes)+numOfComponents), ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            girth = ingrid_obj.get('girth', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
            if edges != 'undt' and numOfComponents != 'undt':
                try:
                    ingrid_obj.set('nodes', -(2.0**(0.5*girth))+edges+numOfComponents, ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            girth = ingrid_obj.get('girth', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if edges != 'undt':
                try:
                    ingrid_obj.set('numOfComponents', 2.0**(0.5*girth)-(edges)+nodes, ind='Min')
                except:
                    pass
        return

class Theorem16(Theorem):
    def __init__(self):
        super(Theorem16, self).__init__(16, "if nodeConnec == 0 then { edgeConnec == 0 }; if edgeConnec == 0 then { nodeConnec == 0};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","nodeConnec"]
    def run(self, ingrid_obj):
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
        if (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==0.0)):
            try:
                ingrid_obj.set('edgeConnec', 0.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('edgeConnec', 0.0, ind='Min')
            except:
                pass
        edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
        edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
        if (edgeConnec_Max==edgeConnec_Min and (edgeConnec_Min==0.0)):
            try:
                ingrid_obj.set('nodeConnec', 0.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodeConnec', 0.0, ind='Min')
            except:
                pass
        return

class Theorem17(Theorem):
    def __init__(self):
        super(Theorem17, self).__init__(17, "edges <= (1/2)*(edgeCliqueCover*maxClique*(maxClique-1));", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edges","maxClique"]
    def run(self, ingrid_obj):
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if edgeCliqueCover != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*edgeCliqueCover*maxClique*(maxClique-(1.0)), ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if maxClique != 'undt':
            try:
                ingrid_obj.set('edgeCliqueCover', 2.0*edges/(maxClique*(maxClique-(1.0))), ind='Min')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
        edges = ingrid_obj.get('edges', ind='Min')
        try:
            ingrid_obj.set('maxClique', 0.5+0.5*(edgeCliqueCover*(8.0*edges+1.0*edgeCliqueCover))**(1/2)/edgeCliqueCover, ind='Min')
        except:
            pass
        return

class Theorem18(Theorem):
    def __init__(self):
        super(Theorem18, self).__init__(18, "chromaticNum <= (1/2)*(7+(1+48*genus)**(1/2));", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","genus"]
    def run(self, ingrid_obj):
        genus = ingrid_obj.get('genus', ind='Max')
        if genus != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 0.5*(48.0*genus+1.0)**0.5+3.5, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        try:
            ingrid_obj.set('genus', 2.08333333333333e-2*(2.0*chromaticNum-(7.0))**2.0-(2.08333333333333e-2), ind='Min')
        except:
            pass
        return

class Theorem19(Theorem):
    def __init__(self):
        super(Theorem19, self).__init__(19, "if maxClique == 2 then { maxdeg <= nodeInd, edges <= nodeCover * nodeInd };", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxClique","maxdeg","nodeCover","nodeInd"]
    def run(self, ingrid_obj):
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('maxdeg', nodeInd, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('nodeInd', maxdeg, ind='Min')
            except:
                pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeCover != 'undt' and nodeInd != 'undt':
                try:
                    ingrid_obj.set('edges', nodeCover*nodeInd, ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('nodeCover', edges/nodeInd, ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodeInd', edges/nodeCover, ind='Min')
                except:
                    pass
        return

class Theorem20(Theorem):
    def __init__(self):
        super(Theorem20, self).__init__(20, "if chromaticNum == 2 then { edgeInd == nodeCover, nodeInd == nodeCliqueCover, edgeChromatic == maxdeg, even girth, even circumference }; if chromaticNum == 2 and nodes > 2 then { not complete };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","circumference","edgeChromatic","edgeInd","girth","maxdeg","nodeCliqueCover","nodeCover","nodeInd","complete","nodes"]
    def run(self, ingrid_obj):
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
        if (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)):
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('edgeInd', nodeCover, ind='Max')
                except:
                    pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Min')
            try:
                ingrid_obj.set('edgeInd', nodeCover, ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('nodeCover', edgeInd, ind='Max')
                except:
                    pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Min')
            try:
                ingrid_obj.set('nodeCover', edgeInd, ind='Min')
            except:
                pass
            nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
            if nodeCliqueCover != 'undt':
                try:
                    ingrid_obj.set('nodeInd', nodeCliqueCover, ind='Max')
                except:
                    pass
            nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
            try:
                ingrid_obj.set('nodeInd', nodeCliqueCover, ind='Min')
            except:
                pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('nodeCliqueCover', nodeInd, ind='Max')
                except:
                    pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            try:
                ingrid_obj.set('nodeCliqueCover', nodeInd, ind='Min')
            except:
                pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', maxdeg, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', maxdeg, ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('maxdeg', edgeChromatic, ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('maxdeg', edgeChromatic, ind='Min')
            except:
                pass
            try:
                girth_Min = ingrid_obj.get('girth', ind='Min')+1
                if even(girth_Max):
                    ingrid_obj.set('girth', ind='Max')
            except:
                pass
            try:
                girth_Max = ingrid_obj.get('girth', ind='Max')-1
                if even(girth_Min):
                    ingrid_obj.set('girth', ind='Min')
            except:
                pass
            try:
                circumference_Min = ingrid_obj.get('circumference', ind='Min')+1
                if even(circumference_Max):
                    ingrid_obj.set('circumference', ind='Max')
            except:
                pass
            try:
                circumference_Max = ingrid_obj.get('circumference', ind='Max')-1
                if even(circumference_Min):
                    ingrid_obj.set('circumference', ind='Min')
            except:
                pass
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        if (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)) and (nodes_Min>2.0):
            ingrid_obj.set('complete', False)
        return

class Theorem21(Theorem):
    def __init__(self):
        super(Theorem21, self).__init__(21, "genus <= ((nodes-3)*(nodes-4)+11)/12;", "")
    def involves(self, str_invar):
        return str_invar in ["genus","nodes"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('genus', 8.33333333333333e-2*nodes**2.0-(0.583333333333333*nodes)+1.91666666666667, ind='Max')
            except:
                pass
        genus = ingrid_obj.get('genus', ind='Min')
        try:
            ingrid_obj.set('nodes', float(0.5*(48.0*genus-(43.0))**(1/2)+3.5), ind='Min')
        except: 
            pass
        return

class Theorem22(Theorem):
    def __init__(self):
        super(Theorem22, self).__init__(22, "if edges  > maxdeg*edgeInd then { edgeChromatic == maxdeg + 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","edgeInd","edges","maxdeg"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        if (edgeInd_Max != 'undt' and maxdeg_Max != 'undt' and (edges_Min>maxdeg_Max*edgeInd_Max)):
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', 1.0*maxdeg+1.0, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', 1.0*maxdeg+1.0, ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('maxdeg', 1.0*edgeChromatic-(1.0), ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('maxdeg', 1.0*edgeChromatic-(1.0), ind='Min')
            except:
                pass
        return

class Theorem23(Theorem):
    def __init__(self):
        super(Theorem23, self).__init__(23, "edgeCliqueCover <= edgeCover * edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edgeCover","edgeInd"]
    def run(self, ingrid_obj):
        edgeCover = ingrid_obj.get('edgeCover', ind='Max')
        edgeInd = ingrid_obj.get('edgeInd', ind='Max')
        if edgeCover != 'undt' and edgeInd != 'undt':
            try:
                ingrid_obj.set('edgeCliqueCover', edgeCover*edgeInd, ind='Max')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        edgeInd = ingrid_obj.get('edgeInd', ind='Max')
        if edgeInd != 'undt':
            try:
                ingrid_obj.set('edgeCover', edgeCliqueCover/edgeInd, ind='Min')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        edgeCover = ingrid_obj.get('edgeCover', ind='Max')
        if edgeCover != 'undt':
            try:
                ingrid_obj.set('edgeInd', edgeCliqueCover/edgeCover, ind='Min')
            except:
                pass
        return

class Theorem24(Theorem):
    def __init__(self):
        super(Theorem24, self).__init__(24, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem25(Theorem):
    def __init__(self):
        super(Theorem25, self).__init__(25, "edgeCover >= (1/2)*nodes;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","nodes"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Min')
        try:
            ingrid_obj.set('edgeCover', 0.5*nodes, ind='Min')
        except:
            pass
        edgeCover = ingrid_obj.get('edgeCover', ind='Max')
        if edgeCover != 'undt':
            try:
                ingrid_obj.set('nodes', 2.0*edgeCover, ind='Max')
            except:
                pass
        return

class Theorem26(Theorem):
    def __init__(self):
        super(Theorem26, self).__init__(26, "edges <= (1/2)*(nodes - 1)*(nodes-2)+nodes/domination - 1;", "")
    def involves(self, str_invar):
        return str_invar in ["domination","edges","nodes"]
    def run(self, ingrid_obj):
        domination = ingrid_obj.get('domination', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if domination != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edges', nodes*(0.5*domination*nodes-(1.5*domination)+1.0)/domination, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                res = 1.0*nodes/(1.0*edges-(0.5*nodes**2.0)+1.5*nodes)
                if res > 0:
                    ingrid_obj.set('domination', res, ind='Max')
            except:
                pass
        domination = ingrid_obj.get('domination', ind='Min')
        edges = ingrid_obj.get('edges', ind='Min')
        try:
            ingrid_obj.set('nodes', 1.0*(1.5*domination-(1.0))/domination+1.0*(2.0*edges*domination**2.0+2.25*domination**2.0-(3.0*domination)+1.0)**(1/2)/domination, ind='Min')
        except:
            pass
        return

class Theorem27(Theorem):
    def __init__(self):
        super(Theorem27, self).__init__(27, "edgeCover <= nodes*maxdeg/(1 + maxdeg);", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCover","maxdeg","nodes"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if maxdeg != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edgeCover', 1.0*maxdeg*nodes/(maxdeg+1.0), ind='Max')
            except:
                pass
        edgeCover = ingrid_obj.get('edgeCover', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('maxdeg', -(1.0*edgeCover/(edgeCover-(nodes))), ind='Min')
            except:
                pass
        edgeCover = ingrid_obj.get('edgeCover', ind='Min')
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        try:
            ingrid_obj.set('nodes', 1.0*edgeCover*(maxdeg+1.0)/maxdeg, ind='Min')
        except:
            pass
        return

class Theorem28(Theorem):
    def __init__(self):
        super(Theorem28, self).__init__(28, "if defined diameter { if diameter <= 3 then { maxdeg <= nodes - diameter + 1 } else { maxdeg <= nodes - nodeConnec*(diameter - 4)-3 } };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        if diameter_Max != 'undt':
            diameter_Max = ingrid_obj.get('diameter', ind='Max')
            
            if (diameter_Max != 'undt' and (diameter_Max<=3.0)):
                diameter = ingrid_obj.get('diameter', ind='Min')
                nodes = ingrid_obj.get('nodes', ind='Max')
                if nodes != 'undt':
                    try:
                        ingrid_obj.set('maxdeg', -(1.0*diameter)+1.0*nodes+1.0, ind='Max')
                    except:
                        pass
                maxdeg = ingrid_obj.get('maxdeg', ind='Min')
                nodes = ingrid_obj.get('nodes', ind='Max')
                if nodes != 'undt':
                    try:
                        ingrid_obj.set('diameter', -(1.0*maxdeg)+1.0*nodes+1.0, ind='Max')
                    except:
                        pass
                diameter = ingrid_obj.get('diameter', ind='Min')
                maxdeg = ingrid_obj.get('maxdeg', ind='Min')
                try:
                    ingrid_obj.set('nodes', 1.0*maxdeg+1.0*diameter-(1.0), ind='Min')
                except:
                    pass
            elif (True):
                diameter = ingrid_obj.get('diameter', ind='Min')
                nodeConnec = max(1,ingrid_obj.get('nodeConnec', ind='Min'))
                nodes = ingrid_obj.get('nodes', ind='Max')
                if nodeConnec != 'undt' and nodes != 'undt':
                    try:
                        ingrid_obj.set('maxdeg', -(1.0*diameter*nodeConnec)+4.0*nodeConnec+1.0*nodes-(3.0), ind='Max')
                    except:
                        pass
                maxdeg = ingrid_obj.get('maxdeg', ind='Min')
                nodeConnec = max(1,ingrid_obj.get('nodeConnec', ind='Min'))
                nodes = ingrid_obj.get('nodes', ind='Max')
                if nodeConnec != 'undt' and nodes != 'undt':
                    try:
                        ingrid_obj.set('diameter', (-(1.0*maxdeg)+4.0*nodeConnec+1.0*nodes-(3.0))/nodeConnec, ind='Max')
                    except:
                        pass
                diameter = ingrid_obj.get('diameter', ind='Min')
                maxdeg = ingrid_obj.get('maxdeg', ind='Max')
                nodes = ingrid_obj.get('nodes', ind='Max')
                if nodes != 'undt':
                    try:
                        ingrid_obj.set('nodeConnec', (-(1.0*maxdeg)+1.0*nodes-(3.0))/(1.0*diameter-(4.0)), ind='Min')
                    except:
                        pass
                diameter = ingrid_obj.get('diameter', ind='Min')
                maxdeg = ingrid_obj.get('maxdeg', ind='Min')
                nodeConnec = max(1,ingrid_obj.get('nodeConnec', ind='Min'))
                try:
                    ingrid_obj.set('nodes', 1.0*maxdeg+1.0*diameter*nodeConnec-(4.0*nodeConnec)+3.0, ind='Min')
                except:
                    pass
        return

class Theorem29(Theorem):
    def __init__(self):
        super(Theorem29, self).__init__(29, "edgeCliqueCover <= edges - (1/2)*maxClique(maxClique - 1)+1;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edges","maxClique"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('edgeCliqueCover', -(0.5*maxClique(maxClique-(1.0)))+1.0*edges+1.0, ind='Max')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        try:
            ingrid_obj.set('edges', 1.0*edgeCliqueCover+0.5*maxClique(maxClique-(1.0))-(1.0), ind='Min')
        except:
            pass
        return

class Theorem30(Theorem):
    def __init__(self):
        super(Theorem30, self).__init__(30, "if connected and radius <= min(2,nodes/2) then { edges <= (1/2)*nodes*(nodes-radius) } else if connected and radius >= 3 and radius <= nodes/2 then { edges <= (1/2)*(nodes**2+4*radius*nodes+5*nodes+4*radius**2-6*radius) };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","edges","nodes","radius"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        radius_Max = ingrid_obj.get('radius', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        radius_Min = ingrid_obj.get('radius', ind='Min')
        if (connected == True) and (radius_Max != 'undt' and (radius_Max<=min(2.0, nodes_Min/2.0))):
            nodes = ingrid_obj.get('nodes', ind='Max')
            radius = ingrid_obj.get('radius', ind='Min')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edges', 0.5*nodes*(nodes-(radius)), ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            radius = ingrid_obj.get('radius', ind='Min')
            try:
                ingrid_obj.set('nodes', 0.5*radius+0.5*(8.0*edges+1.0*radius**2.0)**(1/2), ind='Min')
            except:
                pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('radius', -(2.0*edges/nodes)+1.0*nodes, ind='Max')
                except:
                    pass
        elif (connected == True) and (radius_Min>=3.0) and (radius_Max != 'undt' and (radius_Max<=nodes_Min/2.0)):
            nodes = ingrid_obj.get('nodes', ind='Max')
            radius = ingrid_obj.get('radius', ind='Max')
            if nodes != 'undt' and radius != 'undt':
                try:
                    ingrid_obj.set('edges', 2.0*nodes*radius+2.5*nodes+0.5*nodes**2.0-(3.0*radius)+2.0*radius**2.0, ind='Max')
                except:
                    pass
        return

class Theorem31(Theorem):
    def __init__(self):
        super(Theorem31, self).__init__(31, "chromaticNum <= (nodes + 1 )**2/(4*nodeCliqueCover);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodeCliqueCover","nodes"]
    def run(self, ingrid_obj):
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 0.25*(nodes+1.0)**2.0/nodeCliqueCover, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('nodeCliqueCover', 0.25*(nodes+1.0)**2.0/chromaticNum, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
        try:
            ingrid_obj.set('nodes', 2.0*(chromaticNum*nodeCliqueCover)**0.5-(1.0), ind='Min')
        except:
            pass
        return

class Theorem32(Theorem):
    def __init__(self):
        super(Theorem32, self).__init__(32, "chromaticNum >= 2*nodes**(1/2)-nodeCliqueCover;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodeCliqueCover","nodes"]
    def run(self, ingrid_obj):
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if nodeCliqueCover != 'undt':
            try:
                ingrid_obj.set('chromaticNum', -(1.0*nodeCliqueCover)+2.0*nodes**0.5, ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if chromaticNum != 'undt':
            try:
                ingrid_obj.set('nodeCliqueCover', -(1.0*chromaticNum)+2.0*nodes**0.5, ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
        if chromaticNum != 'undt' and nodeCliqueCover != 'undt':
            try:
                ingrid_obj.set('nodes', 0.25*(chromaticNum+nodeCliqueCover)**2.0, ind='Max')
            except:
                pass
        return

class Theorem33(Theorem):
    def __init__(self):
        super(Theorem33, self).__init__(33, "domination <= nodes + 1 - (1+2*edges)**(1/2);", "")
    def involves(self, str_invar):
        return str_invar in ["domination","edges","nodes"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('domination', 1.0*nodes-(1.0*(2.0*edges+1.0)**0.5)+1.0, ind='Max')
            except:
                pass
        domination = ingrid_obj.get('domination', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*(-(domination)+nodes+1.0)**2.0-(0.5), ind='Max')
            except:
                pass
        domination = ingrid_obj.get('domination', ind='Min')
        edges = ingrid_obj.get('edges', ind='Min')
        try:
            ingrid_obj.set('nodes', 1.0*domination+1.0*(2.0*edges+1.0)**0.5-(1.0), ind='Min')
        except:
            pass
        return

class Theorem34(Theorem):
    def __init__(self):
        super(Theorem34, self).__init__(34, "if nodeConnec > 0 and not tree then { girth <= 2*diameter+1 };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","girth","nodeConnec","tree"]
    def run(self, ingrid_obj):
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        tree = ingrid_obj.get('tree')
        if (nodeConnec_Min>0.0) and (tree == False):
            diameter = ingrid_obj.get('diameter', ind='Max')
            if diameter != 'undt':
                try:
                    ingrid_obj.set('girth', 2.0*diameter+1.0, ind='Max')
                except:
                    pass
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('diameter', 0.5*girth-(0.5), ind='Min')
            except:
                pass
        return

class Theorem35(Theorem):
    def __init__(self):
        super(Theorem35, self).__init__(35, "if planar and maxClique < 3 then { nodeInd >= (1/3)*(nodes+1), nodeCover <= (2*nodes-1)/3 } else if planar then { maxClique >= 3 }; ", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCover","nodeInd","nodes","planar"]
    def run(self, ingrid_obj):
        # planar = ingrid_obj.get('planar')
        # maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        # if (planar == True) and (maxClique_Max != 'undt' and (maxClique_Max<3.0)):
        #     nodes = ingrid_obj.get('nodes', ind='Min')
        #     try:
        #         ingrid_obj.set('nodeInd', 0.333333333333333*nodes+0.333333333333333, ind='Min')
        #     except:
        #         pass
        #     nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        #     if nodeInd != 'undt':
        #         try:
        #             ingrid_obj.set('nodes', 3.0*nodeInd-(1.0), ind='Max')
        #         except:
        #             pass
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if nodes != 'undt':
        #         try:
        #             ingrid_obj.set('nodeCover', 0.666666666666667*nodes-(0.333333333333333), ind='Max')
        #         except:
        #             pass
        #     nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        #     try:
        #         ingrid_obj.set('nodes', 1.5*nodeCover+0.5, ind='Min')
        #     except:
        #         pass
        # elif (planar == True):
        #     try:
        #         ingrid_obj.set('maxClique', 3.0, ind='Min')
        #     except:
        #         pass
        return

class Theorem36(Theorem):
    def __init__(self):
        super(Theorem36, self).__init__(36, "if not planar then { maxdeg >= 3, nodes >= 5, edges >= 9, edgeInd >= 2, nodeCover >= 3, edgeCover >= 3, bandwidth >= 4 };", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","edgeCover","edgeInd","edges","maxdeg","nodeCover","nodes","planar"]
    def run(self, ingrid_obj):
        planar = ingrid_obj.get('planar')
        if (planar == False):
            try:
                ingrid_obj.set('maxdeg', 3.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodes', 5.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('edges', 9.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('edgeInd', 2.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodeCover', 3.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('edgeCover', 3.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('bandwidth', 4.0, ind='Min')
            except:
                pass
        return

class Theorem37(Theorem):
    def __init__(self):
        super(Theorem37, self).__init__(37, "edges <= numOfComponents - 1 + (nodes+2-2*numOfComponents)*(nodes+1-2*numOfComponents)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Max')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        if nodes != 'undt' and numOfComponents != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*nodes**2.0-(2.0*nodes*numOfComponents)+1.5*nodes+2.0*numOfComponents**2.0-(2.0*numOfComponents), ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        if edges != 'undt' and numOfComponents != 'undt':
            try:
                ingrid_obj.set('nodes', 2.0*numOfComponents+0.5*(8.0*edges-(8.0*numOfComponents)+9.0)**(1/2)-(1.5), ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if edges != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('numOfComponents', 0.5*(nodes+1.0)+0.5*(2.0*edges-(1.0*nodes)+1.0)**(1/2), ind='Max')
            except:
                pass
        return

class Theorem38(Theorem):
    def __init__(self):
        super(Theorem38, self).__init__(38, "domination >= nodes / (maxdeg + 1);", "")
    def involves(self, str_invar):
        return str_invar in ["domination","maxdeg","nodes"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if maxdeg != 'undt':
            try:
                ingrid_obj.set('domination', 1.0*nodes/(maxdeg+1.0), ind='Min')
            except:
                pass
        domination = ingrid_obj.get('domination', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if domination != 'undt':
            try:
                ingrid_obj.set('maxdeg', -(1.0)+1.0*nodes/domination, ind='Min')
            except:
                pass
        domination = ingrid_obj.get('domination', ind='Max')
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        if domination != 'undt' and maxdeg != 'undt':
            try:
                ingrid_obj.set('nodes', 1.0*domination*(maxdeg+1.0), ind='Max')
            except:
                pass
        return

class Theorem39(Theorem):
    def __init__(self):
        super(Theorem39, self).__init__(39, "if girth >= 4 or maxClique <= 2 then { maxClique <= 2, girth >= 4 };", "")
    def involves(self, str_invar):
        return str_invar in ["girth","maxClique"]
    def run(self, ingrid_obj):
        girth_Min = ingrid_obj.get('girth', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (girth_Min != 'undt' and girth_Min>=4.0) or (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
            try:
                ingrid_obj.set('maxClique', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('girth', 4.0, ind='Min')
            except:
                pass
        return

class Theorem40(Theorem):
    def __init__(self):
        super(Theorem40, self).__init__(40, "if complete or mindeg == nodes - 1 or nodeInd == 1 or nodeCliqueCover == 1 or edgeCliqueCover == 1 or diameter == 1 then { complete, mindeg == nodes - 1, nodeInd == 1, nodeCliqueCover == 1, edgeCliqueCover == 1, diameter == 1};", "")
    def involves(self, str_invar):
        return str_invar in ["complete","diameter","edgeCliqueCover","mindeg","nodeCliqueCover","nodeInd","nodes"]
    def run(self, ingrid_obj):
        complete = ingrid_obj.get('complete')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
        nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
        nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
        nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
        edgeCliqueCover_Min = ingrid_obj.get('edgeCliqueCover', ind='Min')
        edgeCliqueCover_Max = ingrid_obj.get('edgeCliqueCover', ind='Max')
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        if (complete == True) or (mindeg_Max != 'undt' and (mindeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(1.0))) or (nodeInd_Max==nodeInd_Min and (nodeInd_Min==1.0)) or (nodeCliqueCover_Max==nodeCliqueCover_Min and (nodeCliqueCover_Min==1.0)) or (edgeCliqueCover_Max==edgeCliqueCover_Min and (edgeCliqueCover_Min==1.0)) or (diameter_Max==diameter_Min and (diameter_Min==1.0)):
            ingrid_obj.set('complete', True)
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', 1.0*nodes-(1.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('mindeg', 1.0*nodes-(1.0), ind='Min')
            except:
                pass
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('nodes', 1.0*mindeg+1.0, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*mindeg+1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodeInd', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodeInd', 1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('diameter', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('diameter', 1.0, ind='Min')
            except:
                pass
        return

class Theorem41(Theorem):
    def __init__(self):
        super(Theorem41, self).__init__(41, "if chromaticNum <= 2 or bipartite then { bipartite, chromaticNum <= 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","chromaticNum"]
    def run(self, ingrid_obj):
        chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
        bipartite = ingrid_obj.get('bipartite')
        if (chromaticNum_Max != 'undt' and (chromaticNum_Max<=2.0)) or (bipartite == True):
            ingrid_obj.set('bipartite', True)
            try:
                ingrid_obj.set('chromaticNum', 2.0, ind='Max')
            except:
                pass
        return

class Theorem42(Theorem):
    def __init__(self):
        super(Theorem42, self).__init__(42, "if radius == 1 or maxdeg ==  nodes-1 then { maxdeg == nodes - 1, radius == 1};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodes","radius"]
    def run(self, ingrid_obj):
        radius_Min = ingrid_obj.get('radius', ind='Min')
        radius_Max = ingrid_obj.get('radius', ind='Max')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (radius_Max==radius_Min and (radius_Min==1.0)) or (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(1.0))):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('maxdeg', 1.0*nodes-(1.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('maxdeg', 1.0*nodes-(1.0), ind='Min')
            except:
                pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('nodes', 1.0*maxdeg+1.0, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*maxdeg+1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('radius', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('radius', 1.0, ind='Min')
            except:
                pass
        return

class Theorem43(Theorem):
    def __init__(self):
        super(Theorem43, self).__init__(43, "if (forest and connected) or tree then { tree, forest and connected };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","forest","tree"]
    def run(self, ingrid_obj):
        forest = ingrid_obj.get('forest')
        connected = ingrid_obj.get('connected')
        tree = ingrid_obj.get('tree')
        if (forest == True) and (connected == True) or (tree == True):
            ingrid_obj.set('tree', True)
            ingrid_obj.set('forest', True)
            ingrid_obj.set('connected', True)
        return

class Theorem44(Theorem):
    def __init__(self):
        super(Theorem44, self).__init__(44, "if connected or nodeConnec >= 1 or numOfComponents == 1 or radius <= nodes/2 or diameter <= nodes-1 then { connected, nodeConnec >= 1, numOfComponents == 1, radius <= nodes/2, diameter <= nodes-1 };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","nodeConnec","nodes","numOfComponents","radius"]
    def run(self, ingrid_obj):
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        numOfComponents_Min = ingrid_obj.get('numOfComponents', ind='Min')
        numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
        radius_Max = ingrid_obj.get('radius', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        connected = ingrid_obj.get('connected')
        if (connected==True) or (nodeConnec_Min>=1.0) or (numOfComponents_Max==numOfComponents_Min and (numOfComponents_Min==1.0)) or (radius_Max != 'undt' and (radius_Max<=nodes_Min/2.0)) or (diameter_Max != 'undt' and (diameter_Max<=nodes_Min-(1.0))):
            ingrid_obj.set('connected', True)
            try:
                ingrid_obj.set('nodeConnec', 1.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('numOfComponents', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('numOfComponents', 1.0, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('radius', 0.5*nodes, ind='Max')
                except:
                    pass
            radius = ingrid_obj.get('radius', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*radius, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('diameter', 1.0*nodes-(1.0), ind='Max')
                except:
                    pass
            diameter = ingrid_obj.get('diameter', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*diameter+1.0, ind='Min')
            except:
                pass
        return

class Theorem45(Theorem):
    def __init__(self):
        super(Theorem45, self).__init__(45, "if cycle or (maxdeg == 2 and mindeg == 2 and connected) then { cycle, maxdeg == 2, mindeg == 2, connected };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","cycle","maxdeg","mindeg"]
    def run(self, ingrid_obj):
        cycle = ingrid_obj.get('cycle')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        connected = ingrid_obj.get('connected')
        if (cycle == True) or (maxdeg_Max==maxdeg_Min and (maxdeg_Min==2.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)) and (connected == True):
            ingrid_obj.set('cycle', True)
            try:
                ingrid_obj.set('maxdeg', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('maxdeg', 2.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('mindeg', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('mindeg', 2.0, ind='Min')
            except:
                pass
            ingrid_obj.set('connected', True)
        return

class Theorem46(Theorem):
    def __init__(self):
        super(Theorem46, self).__init__(46, "if regular or mindeg == maxdeg then { regular, mindeg == maxdeg };", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","mindeg","regular"]
    def run(self, ingrid_obj):
        regular = ingrid_obj.get('regular')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        if (regular == True) or (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)):
            ingrid_obj.set('regular', True)
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('mindeg', maxdeg, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('mindeg', maxdeg, ind='Min')
            except:
                pass
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('maxdeg', mindeg, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('maxdeg', mindeg, ind='Min')
            except:
                pass
        return

class Theorem47(Theorem):
    def __init__(self):
        super(Theorem47, self).__init__(47, "if genus == 0 or planar or thickness == 1 then { genus == 0, planar, thickness == 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["genus","planar","thickness"]
    def run(self, ingrid_obj):
        genus_Min = ingrid_obj.get('genus', ind='Min')
        genus_Max = ingrid_obj.get('genus', ind='Max')
        planar = ingrid_obj.get('planar')
        thickness_Min = ingrid_obj.get('thickness', ind='Min')
        thickness_Max = ingrid_obj.get('thickness', ind='Max')
        if (genus_Max==genus_Min and (genus_Min==0.0)) or (planar == True) or (thickness_Max==thickness_Min and (thickness_Min==1.0)):
            try:
                ingrid_obj.set('genus', 0.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('genus', 0.0, ind='Min')
            except:
                pass
            ingrid_obj.set('planar', True)
            try:
                ingrid_obj.set('thickness', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('thickness', 1.0, ind='Min')
            except:
                pass
        return

class Theorem48(Theorem):
    def __init__(self):
        super(Theorem48, self).__init__(48, "if forest then { planar, chromaticNum == 2, mindeg == 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","forest","mindeg","planar"]
    def run(self, ingrid_obj):
        forest = ingrid_obj.get('forest')
        if (forest == True):
            ingrid_obj.set('planar', True)
            try:
                ingrid_obj.set('chromaticNum', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('chromaticNum', 2.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('mindeg', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('mindeg', 1.0, ind='Min')
            except:
                pass
        return

class Theorem49(Theorem):
    def __init__(self):
        super(Theorem49, self).__init__(49, "if cycle then { planar, not forest, crossing == 0, nodes >= 2, edges >= 3, arboricity == 2, nodeCover == (nodes + 1)/2, edgeCover == (nodes + 1)/2, nodeInd == nodes/2, edgeInd == nodes/2, radius == edgeInd, girth == circumference, circumference == nodes, edgeChromatic == chromaticNum, nodes >= 2*nodeCover-1, nodes <= 2*nodeCover, nodes >= 2*edgeInd, nodes <= 2*edgeInd + 1, nodeConnec == 2, regular, bandwidth == 2 }; if cycle and nodes > 3 then { maxClique == 2 } else { maxClique == 3 }; if cycle and even nodes then { chromaticNum == 2 } else { chromaticNum == 3 }; if cycle and chromaticNum == 2 then { even nodes } else { odd nodes }; if cycle and maxClique == 2 then { nodes >= 4 } else { nodes == 3 }; if cycle and nodes == 3 then { nodeCliqueCover == 1 } else { nodeCliqueCover == nodeCover };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","bandwidth","chromaticNum","circumference","crossing","cycle","edgeChromatic","edgeCover","edgeInd","edges","forest","girth","nodeConnec","nodeCover","nodeInd","nodes","planar","radius","regular","maxClique","nodeCliqueCover"]
    def run(self, ingrid_obj):
        cycle = ingrid_obj.get('cycle')
        if (cycle == True):
            ingrid_obj.set('planar', True)
            ingrid_obj.set('forest', False)
            try:
                ingrid_obj.set('crossing', 0.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('crossing', 0.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodes', 2.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('edges', 3.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('arboricity', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('arboricity', 2.0, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Min')
            except:
                pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Max')
                except:
                    pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Min')
            except:
                pass
            edgeCover = ingrid_obj.get('edgeCover', ind='Max')
            if edgeCover != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*edgeCover-(1.0), ind='Max')
                except:
                    pass
            edgeCover = ingrid_obj.get('edgeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*edgeCover-(1.0), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeInd', 0.5*nodes, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('nodeInd', 0.5*nodes, ind='Min')
            except:
                pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*nodeInd, ind='Max')
                except:
                    pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*nodeInd, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeInd', 0.5*nodes, ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*edgeInd, ind='Max')
                except:
                    pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('radius', edgeInd, ind='Max')
                except:
                    pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Min')
            try:
                ingrid_obj.set('radius', edgeInd, ind='Min')
            except:
                pass
            radius = ingrid_obj.get('radius', ind='Max')
            if radius != 'undt':
                try:
                    ingrid_obj.set('edgeInd', radius, ind='Max')
                except:
                    pass
            radius = ingrid_obj.get('radius', ind='Min')
            try:
                ingrid_obj.set('edgeInd', radius, ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('girth', circumference, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            try:
                ingrid_obj.set('girth', circumference, ind='Min')
            except:
                pass
            girth = ingrid_obj.get('girth', ind='Max')
            if girth != 'undt':
                try:
                    ingrid_obj.set('circumference', girth, ind='Max')
                except:
                    pass
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('circumference', girth, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('circumference', nodes, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('circumference', nodes, ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('nodes', circumference, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            try:
                ingrid_obj.set('nodes', circumference, ind='Min')
            except:
                pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
            if chromaticNum != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', chromaticNum, ind='Max')
                except:
                    pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', chromaticNum, ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('chromaticNum', edgeChromatic, ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('chromaticNum', edgeChromatic, ind='Min')
            except:
                pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Max')
                except:
                    pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*nodeCover, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('nodeCover', 0.5*nodes, ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
                except:
                    pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*edgeInd+1.0, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeInd', 0.5*nodes-(0.5), ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodeConnec', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodeConnec', 2.0, ind='Min')
            except:
                pass
            ingrid_obj.set('regular', True)
            try:
                ingrid_obj.set('bandwidth', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('bandwidth', 2.0, ind='Min')
            except:
                pass
        cycle = ingrid_obj.get('cycle')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        
        if (cycle == True) and (nodes_Min>3.0):
            try:
                ingrid_obj.set('maxClique', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('maxClique', 2.0, ind='Min')
            except:
                pass
        elif (cycle == True):
            try:
                ingrid_obj.set('maxClique', 3.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('maxClique', 3.0, ind='Min')
            except:
                pass
        cycle = ingrid_obj.get('cycle')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        
        if (cycle == True) and (even(nodes_Min) and even(nodes_Max)):
            try:
                ingrid_obj.set('chromaticNum', 2.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('chromaticNum', 2.0, ind='Min')
            except:
                pass
        elif (cycle == True):
            try:
                ingrid_obj.set('chromaticNum', 3.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('chromaticNum', 3.0, ind='Min')
            except:
                pass
        cycle = ingrid_obj.get('cycle')
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
        
        if (cycle == True) and (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)):
            nodes_Max = ingrid_obj.get('nodes', ind='Max')-1
            nodes_Min = ingrid_obj.get('nodes', ind='Min')+1
            if even(nodes_Max):
                ingrid_obj.set('nodes', ind='Max')
            if even(nodes_Min):
                ingrid_obj.set('nodes', ind='Min')
        elif (cycle==True):
            try:
                nodes_Max = ingrid_obj.get('nodes', ind='Max')-1
                if odd(nodes_Max):
                    ingrid_obj.set('nodes', nodes_Max, ind='Max')
            except:
                pass
            try:
                nodes_Min = ingrid_obj.get('nodes', ind='Min')+1
                if odd(nodes_Min):
                    ingrid_obj.set('nodes', nodes_Min, ind='Min')
            except:
                pass
        cycle = ingrid_obj.get('cycle')
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        
        if (cycle == True) and (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
            try:
                ingrid_obj.set('nodes', 4.0, ind='Min')
            except:
                pass
        elif (maxClique_Max==maxClique_Min and cycle==True):
            try:
                ingrid_obj.set('nodes', 3.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodes', 3.0, ind='Min')
            except:
                pass
        cycle = ingrid_obj.get('cycle')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        
        if (cycle == True) and (nodes_Max==nodes_Min and (nodes_Min==3.0)):
            try:
                ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
            except:
                pass
        elif (cycle==True):
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodeCliqueCover', nodeCover, ind='Max')
                except:
                    pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Min')
            try:
                ingrid_obj.set('nodeCliqueCover', nodeCover, ind='Min')
            except:
                pass
            nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
            if nodeCliqueCover != 'undt':
                try:
                    ingrid_obj.set('nodeCover', nodeCliqueCover, ind='Max')
                except:
                    pass
            nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
            try:
                ingrid_obj.set('nodeCover', nodeCliqueCover, ind='Min')
            except:
                pass
        return

class Theorem50(Theorem):
    def __init__(self):
        super(Theorem50, self).__init__(50, "if forest or edges == nodes - numOfComponents or arboricity == 1 or undefined girth or undefined circumference then { forest, edges == nodes - numOfComponents, arboricity == 1, undefined girth, undefined circumference };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","circumference","edges","forest","girth","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        forest = ingrid_obj.get('forest')
        edges_Max = ingrid_obj.get('edges', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        numOfComponents_Min = ingrid_obj.get('numOfComponents', ind='Min')
        arboricity_Min = ingrid_obj.get('arboricity', ind='Min')
        arboricity_Max = ingrid_obj.get('arboricity', ind='Max')
        girth_Min = ingrid_obj.get('girth', ind = 'Min')
        circumference_Min = ingrid_obj.get('circumference', ind = 'Min')
        if (forest == True) or (edges_Max != 'undt' and numOfComponents_Max != 'undt' and (edges_Max<=nodes_Min-(numOfComponents_Max)) and nodes_Max != 'undt' and (edges_Min>=nodes_Max-(numOfComponents_Min))) or (arboricity_Max==arboricity_Min and (arboricity_Min==1.0)) or (girth_Min == 'undt') or (circumference_Min == 'undt'):
            ingrid_obj.set('forest', True)
            nodes = ingrid_obj.get('nodes', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edges', nodes-(numOfComponents), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
            if numOfComponents != 'undt':
                try:
                    ingrid_obj.set('edges', nodes-(numOfComponents), ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
            if edges != 'undt' and numOfComponents != 'undt':
                try:
                    ingrid_obj.set('nodes', edges+numOfComponents, ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            try:
                ingrid_obj.set('nodes', edges+numOfComponents, ind='Min')
            except:
                pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('numOfComponents', -(edges)+nodes, ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if edges != 'undt':
                try:
                    ingrid_obj.set('numOfComponents', -(edges)+nodes, ind='Min')
                except:
                    pass
            try:
                ingrid_obj.set('arboricity', 1.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('arboricity', 1.0, ind='Min')
            except:
                pass
            ingrid_obj.set('girth', 'undt', ind='Max')
            ingrid_obj.set('girth', 'undt', ind='Min')
            ingrid_obj.set('circumference', 'undt', ind='Max')
            ingrid_obj.set('circumference', 'undt', ind='Min')
        return

class Theorem51(Theorem):
    def __init__(self):
        super(Theorem51, self).__init__(51, "arboricity >= chromaticNum / 2;", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","chromaticNum"]
    def run(self, ingrid_obj):
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        try:
            ingrid_obj.set('arboricity', 0.5*chromaticNum, ind='Min')
        except:
            pass
        arboricity = ingrid_obj.get('arboricity', ind='Max')
        if arboricity != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 2.0*arboricity, ind='Max')
            except:
                pass
        return

class Theorem52(Theorem):
    def __init__(self):
        super(Theorem52, self).__init__(52, "if (connected and not cycle and not complete) or (maxClique <= maxdeg and maxdeg >= 4 and regular) then { arboricity <= (1 + maxdeg)/2 }; arboricity <= 1 + spectralRadius/2;", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","complete","connected","cycle","maxClique","maxdeg","regular","spectralRadius"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        cycle = ingrid_obj.get('cycle')
        complete = ingrid_obj.get('complete')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        regular = ingrid_obj.get('regular')
        if (connected == True) and (cycle == False) and (complete == False) or (maxClique_Max != 'undt' and (maxClique_Max<=maxdeg_Min)) and (maxdeg_Min>=4.0) and (regular == True):
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('arboricity', 0.5*maxdeg+0.5, ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            try:
                ingrid_obj.set('maxdeg', 2.0*arboricity-(1.0), ind='Min')
            except:
                pass
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
        if spectralRadius != 'undt':
            try:
                ingrid_obj.set('arboricity', 0.5*spectralRadius+1.0, ind='Max')
            except:
                pass
        arboricity = ingrid_obj.get('arboricity', ind='Min')
        try:
            ingrid_obj.set('spectralRadius', 2.0*arboricity-(2.0), ind='Min')
        except:
            pass
        return

class Theorem53(Theorem):
    def __init__(self):
        super(Theorem53, self).__init__(53, "if defined girth then { arboricity <= chromaticNum - chromaticNum/(1 + nodes/((girth - 1)/2)*chromaticNum) };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","chromaticNum","girth","nodes"]
    def run(self, ingrid_obj):
        girth_Min = ingrid_obj.get('girth', ind='Min')
        girth_Max = ingrid_obj.get('girth', ind='Max')
        if girth_Min != 'undt' and girth_Max != 'undt':
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
            girth = ingrid_obj.get('girth', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if chromaticNum != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('arboricity', 1.0*chromaticNum**2.0*nodes/(1.0*chromaticNum*nodes+0.5*girth-(0.5)), ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            girth = ingrid_obj.get('girth', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('chromaticNum', 0.5*(arboricity*nodes+(arboricity*nodes*(1.0*arboricity*nodes+2.0*girth-(2.0)))**(1/2))/nodes, ind='Min')
            except:
                pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if chromaticNum != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('girth', -(2.0*chromaticNum*nodes)+1.0+2.0*chromaticNum**2.0*nodes/arboricity, ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            girth = ingrid_obj.get('girth', ind='Max')
            if girth != 'undt':
                try:
                    ingrid_obj.set('nodes', -(0.5*arboricity*(girth-(1.0))/(chromaticNum*(arboricity-(chromaticNum)))), ind='Min')
                except:
                    pass
        return

class Theorem54(Theorem):
    def __init__(self):
        super(Theorem54, self).__init__(54, "if planar then { mindeg <= 5, maxClique <= 4, arboricity <= 3, crossing == 0 };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","crossing","maxClique","mindeg","planar"]
    def run(self, ingrid_obj):
        planar = ingrid_obj.get('planar')
        if (planar == True):
            try:
                ingrid_obj.set('mindeg', 5.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('maxClique', 4.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('arboricity', 3.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('crossing', 0.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('crossing', 0.0, ind='Min')
            except:
                pass
        return

class Theorem55(Theorem):
    def __init__(self):
        super(Theorem55, self).__init__(55, "edges >= (maxdeg + (nodes - 1)*mindeg)/2; edges >= nodes/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","mindeg","nodes"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Min')
        try:
            ingrid_obj.set('edges', 0.5*maxdeg+0.5*mindeg*nodes-(0.5*mindeg), ind='Min')
        except:
            pass
        edges = ingrid_obj.get('edges', ind='Max')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if edges != 'undt' and mindeg != 'undt':
            try:
                ingrid_obj.set('maxdeg', 2.0*edges-(1.0*mindeg*nodes)+1.0*mindeg, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('mindeg', 2.0*(1.0*edges-(0.5*maxdeg))/(nodes-(1.0)), ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        if edges != 'undt' and mindeg != 'undt':
            try:
                ingrid_obj.set('nodes', (2.0*edges-(1.0*maxdeg)+1.0*mindeg)/mindeg, ind='Max')
            except:
                pass
        nodes = ingrid_obj.get('nodes', 'Min')
        try:
            ingrid_obj.set('edges', (nodes+1)/2, ind='Min')
        except:
            pass
        return

class Theorem56(Theorem):
    def __init__(self):
        super(Theorem56, self).__init__(56, "edges <= ((nodes - 1)*maxdeg + mindeg)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxdeg","mindeg","nodes"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        mindeg = ingrid_obj.get('mindeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*maxdeg*nodes-(0.5*maxdeg)+0.5*mindeg, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if mindeg != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('maxdeg', 2.0*(1.0*edges-(0.5*mindeg))/(nodes-(1.0)), ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('mindeg', 2.0*edges-(1.0*maxdeg*nodes)+1.0*maxdeg, ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        mindeg = ingrid_obj.get('mindeg', ind='Max')
        if mindeg != 'undt':
            try:
                ingrid_obj.set('nodes', (2.0*edges+1.0*maxdeg-(1.0*mindeg))/maxdeg, ind='Min')
            except:
                pass
        return

class Theorem57(Theorem):
    def __init__(self):
        super(Theorem57, self).__init__(57, "if regular and odd mindeg then { even nodes };", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","regular"]
    def run(self, ingrid_obj):
        regular = ingrid_obj.get('regular')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        if (regular == True) and (odd(mindeg_Min) and odd(mindeg_Max)):
            nodes_Max = ingrid_obj.get('nodes', ind='Max')-1
            nodes_Min = ingrid_obj.get('nodes', ind='Min')+1
            if even(nodes_Max):
                ingrid_obj.set('nodes', ind='Max')
            if even(nodes_Min):
                ingrid_obj.set('nodes', ind='Min')
        return

class Theorem58(Theorem):
    def __init__(self):
        super(Theorem58, self).__init__(58, "maxClique >= nodes/(nodes-spectralRadius)-1/3;", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","spectralRadius"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Min')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        try:
            ingrid_obj.set('maxClique', 1.0*(0.666666666666667*nodes+0.333333333333333*spectralRadius)/(nodes-(spectralRadius)), ind='Min')
        except:
            pass
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        try:
            ingrid_obj.set('nodes', spectralRadius*(1.0*maxClique+0.333333333333333)/(1.0*maxClique-(0.666666666666667)), ind='Min')
        except:
            pass
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        try:
            ingrid_obj.set('spectralRadius', nodes*(1.0*maxClique-(0.666666666666667))/(1.0*maxClique+0.333333333333333), ind='Max')
        except:
            pass
        return

class Theorem59(Theorem):
    def __init__(self):
        super(Theorem59, self).__init__(59, "crossing <= (1/4)*(nodes/2)*(nodes-1)/2*(nodes-2)/2*(nodes-3)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["crossing","nodes"]
    def run(self, ingrid_obj):
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('crossing', nodes*(1.5625e-2*nodes**3.0-(9.375e-2*nodes**2.0)+0.171875*nodes-(9.375e-2)), ind='Max')
            except:
                pass
        return

class Theorem60(Theorem):
    def __init__(self):
        super(Theorem60, self).__init__(60, "if defined girth and (nodeConnec > 0 or mindeg > 1) then { genus >= (1/2)*edges*(1-2/girth)-(nodes/2)+numOfComponents };", "")
    def involves(self, str_invar):
        return str_invar in ["edges","genus","girth","mindeg","nodeConnec","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        # girth_Max = ingrid_obj.get('girth', ind = 'Max')
        # nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        # mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        # if (girth_Max != 'undt') and ((nodeConnec_Min>0.0) or (mindeg_Min>1.0)):
        #     edges = ingrid_obj.get('edges', ind='Min')
        #     girth = ingrid_obj.get('girth', ind='Min')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        #     if nodes != 'undt':
        #         try:
        #             ingrid_obj.set('genus', 0.5*edges-(1.0*edges/girth)-(0.5*nodes)+1.0*numOfComponents, ind='Min')
        #         except:
        #             pass
        #     genus = ingrid_obj.get('genus', ind='Max')
        #     girth = ingrid_obj.get('girth', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        #     if genus != 'undt' and girth != 'undt' and nodes != 'undt':
        #         try:
        #             ingrid_obj.set('edges', girth*(1.0*genus+0.5*nodes-(1.0*numOfComponents))/(0.5*girth-(1.0)), ind='Max')
        #         except:
        #             pass
        #     edges = ingrid_obj.get('edges', ind='Min')
        #     genus = ingrid_obj.get('genus', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        #     if edges != 'undt' and numOfComponents != 'undt':
        #         try:
        #             ingrid_obj.set('girth', -(1.0*edges/(1.0*genus-(0.5*edges)+0.5*nodes-(1.0*numOfComponents))), ind='Max')
        #         except:
        #             pass
        #     edges = ingrid_obj.get('edges', ind='Min')
        #     genus = ingrid_obj.get('genus', ind='Max')
        #     girth = ingrid_obj.get('girth', ind='Min')
        #     numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
        #     if genus != 'undt':
        #         try:
        #             ingrid_obj.set('nodes', -(2.0*genus)+1.0*edges-(2.0*edges/girth)+2.0*numOfComponents, ind='Min')
        #         except:
        #             pass
        #     edges = ingrid_obj.get('edges', ind='Min')
        #     genus = ingrid_obj.get('genus', ind='Max')
        #     girth = ingrid_obj.get('girth', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Min')
        #     if edges != 'undt' and genus != 'undt' and nodes != 'undt':
        #         try:
        #             ingrid_obj.set('numOfComponents', 1.0*genus-(0.5*edges)+1.0*edges/girth+0.5*nodes, ind='Min')
        #         except:
        #             pass
        return

class Theorem81(Theorem):
    def __init__(self):
        super(Theorem81, self).__init__(81, "if regular then { nodeInd <= nodes/2 + (maxClique**2 + 3*maxClique - 2)/2*mindeg };", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","mindeg","nodeInd","nodes","regular"]
    def run(self, ingrid_obj):
        regular = ingrid_obj.get('regular')
        if (regular == True):
            maxClique = ingrid_obj.get('maxClique', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if maxClique != 'undt' and mindeg != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('nodeInd', 1.5*maxClique*mindeg+0.5*maxClique**2.0*mindeg-(1.0*mindeg)+0.5*nodes, ind='Max')
                except:
                    pass
            maxClique = ingrid_obj.get('maxClique', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if maxClique != 'undt' and mindeg != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('nodeInd', (-((2.0))+3.0*maxClique+maxClique**2.0)/2.0*mindeg+nodes/2.0, ind='Max')
                except:
                    pass
            maxClique = ingrid_obj.get('maxClique', ind='Max')
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if maxClique != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', (nodeInd-(0.5*nodes))/(1.5*maxClique+0.5*maxClique**2.0-(1.0)), ind='Min')
                except:
                    pass
            maxClique = ingrid_obj.get('maxClique', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            if maxClique != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*nodeInd-(3.0*maxClique*mindeg)-(1.0*maxClique**2.0*mindeg)+2.0*mindeg, ind='Min')
                except:
                    pass
        return

class Theorem82(Theorem):
    def __init__(self):
        super(Theorem82, self).__init__(82, "if mindeg >= nodes/2 then { edgeConnec == mindeg };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg","nodes"]
    def run(self, ingrid_obj):
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max/2.0)):
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('edgeConnec', mindeg, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('edgeConnec', mindeg, ind='Min')
            except:
                pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
            if edgeConnec != 'undt':
                try:
                    ingrid_obj.set('mindeg', edgeConnec, ind='Max')
                except:
                    pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
            try:
                ingrid_obj.set('mindeg', edgeConnec, ind='Min')
            except:
                pass
        return

class Theorem83(Theorem):
    def __init__(self):
        super(Theorem83, self).__init__(83, "if genus > 0 then { arboricity <= 9 + (1+48*genus)**(1/2)/4 };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","genus"]
    def run(self, ingrid_obj):
        genus_Min = ingrid_obj.get('genus', ind='Min')
        if (genus_Min>0.0):
            genus = ingrid_obj.get('genus', ind='Max')
            if genus != 'undt':
                try:
                    ingrid_obj.set('arboricity', 0.25*(48.0*genus+1.0)**0.5+9.0, ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            try:
                ingrid_obj.set('genus', 0.333333333333333*(1.0*arboricity-(9.0))**2.0-(2.08333333333333e-2), ind='Min')
            except:
                pass
        return

class Theorem84(Theorem):
    def __init__(self):
        super(Theorem84, self).__init__(84, "if maxClique == 2 then { arboricity <= 2 + genus**(1/2) };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","genus","maxClique"]
    def run(self, ingrid_obj):
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
            genus = ingrid_obj.get('genus', ind='Max')
            if genus != 'undt':
                try:
                    ingrid_obj.set('arboricity', int(1.0*genus**0.5)+2.0, ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            if arboricity > 2:
                try:
                    ingrid_obj.set('genus', 1.0*(1.0*arboricity-(2.0))**2.0, ind='Min')
                except:
                    pass
        return

class Theorem85(Theorem):
    def __init__(self):
        super(Theorem85, self).__init__(85, "if maxClique == 2 then { chromaticNum <= 3 + 2*genus**(1/2) };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","genus","maxClique"]
    def run(self, ingrid_obj):
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
            genus = ingrid_obj.get('genus', ind='Max')
            if genus != 'undt':
                try:
                    ingrid_obj.set('chromaticNum', 2.0*genus**0.5+3.0, ind='Max')
                except:
                    pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            try:
                ingrid_obj.set('genus', 1.0*(0.5*chromaticNum-(1.5))**2.0, ind='Min')
            except:
                pass
        return

class Theorem86(Theorem):
    def __init__(self):
        super(Theorem86, self).__init__(86, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem87(Theorem):
    def __init__(self):
        super(Theorem87, self).__init__(87, "if genus > 0 then { mindeg <= 5 + (1 + 48*genus)**(1/2)/2 };", "")
    def involves(self, str_invar):
        return str_invar in ["genus","mindeg"]
    def run(self, ingrid_obj):
        genus_Min = ingrid_obj.get('genus', ind='Min')
        if (genus_Min>0.0):
            genus = ingrid_obj.get('genus', ind='Max')
            if genus != 'undt':
                try:
                    ingrid_obj.set('mindeg', 0.5*(48.0*genus+1.0)**0.5+5.0, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('genus', 8.33333333333333e-2*(1.0*mindeg-(5.0))**2.0-(2.08333333333333e-2), ind='Min')
            except:
                pass
        return

class Theorem88(Theorem):
    def __init__(self):
        super(Theorem88, self).__init__(88, "if genus > 0 and maxClique <= 2 then { edgeConnec <= 2 + 2*genus**(1/2) };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","genus","maxClique"]
    def run(self, ingrid_obj):
        genus_Min = ingrid_obj.get('genus', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (genus_Min>0.0) and (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
            genus = ingrid_obj.get('genus', ind='Max')
            if genus != 'undt':
                try:
                    ingrid_obj.set('edgeConnec', 2.0*genus**0.5+2.0, ind='Max')
                except:
                    pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
            try:
                ingrid_obj.set('genus', 1.0*(0.5*edgeConnec-(1.0))**2.0, ind='Min')
            except:
                pass
        return

class Theorem89(Theorem):
    def __init__(self):
        super(Theorem89, self).__init__(89, "if genus == 0 and girth == 3 then { edgeConnec <= 5 } else if genus == 0 and (girth == 4 or girth == 5) then { edgeConnec <= 3 } else if genus == 0 and girth >= 6 then { edgeConnec <= 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","genus","girth"]
    def run(self, ingrid_obj):
        genus_Min = ingrid_obj.get('genus', ind='Min')
        genus_Max = ingrid_obj.get('genus', ind='Max')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        girth_Max = ingrid_obj.get('girth', ind='Max')
        if (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
            try:
                ingrid_obj.set('edgeConnec', 5.0, ind='Max')
            except:
                pass
        elif (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Max==girth_Min and (girth_Min==4.0)) or (girth_Max==girth_Min and (girth_Min==5.0)):
            try:
                ingrid_obj.set('edgeConnec', 3.0, ind='Max')
            except:
                pass
        elif (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Min != 'undt' and girth_Min>=6.0):
            try:
                ingrid_obj.set('edgeConnec', 2.0, ind='Max')
            except:
                pass
        return

class Theorem90(Theorem):
    def __init__(self):
        super(Theorem90, self).__init__(90, "if genus <= 1 and girth == 3 then { edgeConnec <= 6 } else if genus <= 1 and girth == 4 then { edgeConnec <= 4 } else if genus <= 1 and (girth == 5 or girth == 6) then { edgeConnec <= 3 } else if genus <= 1 and girth >= 7 then { edgeConnec <= 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","genus","girth"]
    def run(self, ingrid_obj):
        genus_Max = ingrid_obj.get('genus', ind='Max')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        girth_Max = ingrid_obj.get('girth', ind='Max')
        if (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
            try:
                ingrid_obj.set('edgeConnec', 6.0, ind='Max')
            except:
                pass
        elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==4.0)):
            try:
                ingrid_obj.set('edgeConnec', 4.0, ind='Max')
            except:
                pass
        elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==5.0)) or (girth_Max==girth_Min and (girth_Min==6.0)):
            try:
                ingrid_obj.set('edgeConnec', 3.0, ind='Max')
            except:
                pass
        elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Min != 'undt' and girth_Min>=7.0):
            try:
                ingrid_obj.set('edgeConnec', 2.0, ind='Max')
            except:
                pass
        return

class Theorem91(Theorem):
    def __init__(self):
        super(Theorem91, self).__init__(91, "if mindeg >= 3 and domination >= 1 and domination == (girth - 1)/4 then { nodes >= girth*(mindeg - 1)**domination };", "")
    def involves(self, str_invar):
        return str_invar in ["domination","girth","mindeg","nodes"]
    def run(self, ingrid_obj):
        return

class Theorem92(Theorem):
    def __init__(self):
        super(Theorem92, self).__init__(92, "if nodeConnec >= 2 then { circumference >= min(nodes, 2*mindeg) };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","mindeg","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        if (nodeConnec_Min>=2.0):
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('circumference', min(nodes, 2.0*mindeg), ind='Min')
            except:
                pass
        return

class Theorem93(Theorem):
    def __init__(self):
        super(Theorem93, self).__init__(93, "if diameter == 2 then { if ((even nodes and even mindeg and nodes >= mindeg**3 + mindeg + 1) or ((odd nodes or odd mindeg) and nodes > mindeg**3 + 1)) then { edges >= ((nodes-1)*(mindeg+1)+1)/2  } };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edges","mindeg","nodes"]
    def run(self, ingrid_obj):
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        if (diameter_Max==diameter_Min and (diameter_Min==2.0)):
            if (even(nodes_Min) and even(nodes_Max)) and (even(mindeg_Min) and even(mindeg_Max)) and (mindeg_Max != 'undt' and (nodes_Min>=mindeg_Max**3.0+mindeg_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(mindeg_Min) and odd(mindeg_Max)) and (mindeg_Max != 'undt' and (nodes_Min>mindeg_Max**3.0+1.0)):
                mindeg = ingrid_obj.get('mindeg', ind='Min')
                nodes = ingrid_obj.get('nodes', ind='Min')
                try:
                    ingrid_obj.set('edges', 0.5*mindeg*nodes-(0.5*mindeg)+0.5*nodes, ind='Min')
                except:
                    pass
                edges = ingrid_obj.get('edges', ind='Max')
                nodes = ingrid_obj.get('nodes', ind='Min')
                if edges != 'undt':
                    try:
                        ingrid_obj.set('mindeg', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
                    except:
                        pass
                edges = ingrid_obj.get('edges', ind='Max')
                mindeg = ingrid_obj.get('mindeg', ind='Max')
                if edges != 'undt' and mindeg != 'undt':
                    try:
                        ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*mindeg)/(mindeg+1.0), ind='Max')
                    except:
                        pass
        return

class Theorem94(Theorem):
    def __init__(self):
        super(Theorem94, self).__init__(94, "if diameter == 2 then { if (nodeConnec > 2 or nodeConnec < 2) and ((even nodes and even nodeConnec and nodes >= nodeConnec**3 + nodeConnec + 1) or ((odd nodes or odd nodeConnec) and nodes > nodeConnec**3 + 1)) then { edges >= ((nodes-1)*(nodeConnec+1)+1)/2  }};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edges","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (diameter_Max==diameter_Min and (diameter_Min==2.0)):
            if (nodeConnec_Min>2.0) or (nodeConnec_Max != 'undt' and (nodeConnec_Max<2.0)) and (even(nodes_Min) and even(nodes_Max)) and (even(nodeConnec_Min) and even(nodeConnec_Max)) and (nodeConnec_Max != 'undt' and (nodes_Min>=nodeConnec_Max**3.0+nodeConnec_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(nodeConnec_Min) and odd(nodeConnec_Max)) and (nodeConnec_Max != 'undt' and (nodes_Min>nodeConnec_Max**3.0+1.0)):
                nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
                nodes = ingrid_obj.get('nodes', ind='Min')
                try:
                    ingrid_obj.set('edges', 0.5*nodeConnec*nodes-(0.5*nodeConnec)+0.5*nodes, ind='Min')
                except:
                    pass
                edges = ingrid_obj.get('edges', ind='Max')
                nodes = ingrid_obj.get('nodes', ind='Min')
                if edges != 'undt':
                    try:
                        ingrid_obj.set('nodeConnec', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
                    except:
                        pass
                edges = ingrid_obj.get('edges', ind='Max')
                nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
                if edges != 'undt' and nodeConnec != 'undt':
                    try:
                        ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*nodeConnec)/(nodeConnec+1.0), ind='Max')
                    except:
                        pass
        return

class Theorem95(Theorem):
    def __init__(self):
        super(Theorem95, self).__init__(95, "if diameter == 2 then { if ((even nodes and even edgeConnec and nodes >= edgeConnec**3 + edgeConnec + 1) or ((odd nodes or odd edgeConnec) and nodes > edgeConnec**3 + 1)) then { edges >= ((nodes-1)*(edgeConnec+1)+1)/2 }};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edgeConnec","edges","nodes"]
    def run(self, ingrid_obj):
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
        edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
        if (diameter_Max==diameter_Min and (diameter_Min==2.0)):
            if (even(nodes_Min) and even(nodes_Max)) and (even(edgeConnec_Min) and even(edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (nodes_Min>=edgeConnec_Max**3.0+edgeConnec_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(edgeConnec_Min) and odd(edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (nodes_Min>edgeConnec_Max**3.0+1.0)):
                edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
                nodes = ingrid_obj.get('nodes', ind='Min')
                try:
                    ingrid_obj.set('edges', 0.5*edgeConnec*nodes-(0.5*edgeConnec)+0.5*nodes, ind='Min')
                except:
                    pass
                edges = ingrid_obj.get('edges', ind='Max')
                nodes = ingrid_obj.get('nodes', ind='Min')
                if edges != 'undt':
                    try:
                        ingrid_obj.set('edgeConnec', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
                    except:
                        pass
                edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
                edges = ingrid_obj.get('edges', ind='Max')
                if edgeConnec != 'undt' and edges != 'undt':
                    try:
                        ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*edgeConnec)/(edgeConnec+1.0), ind='Max')
                    except:
                        pass
        return

class Theorem96(Theorem):
    def __init__(self):
        super(Theorem96, self).__init__(96, "if defined girth then { nodes >= (girth - 1)*(arboricity - 1) + 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","girth","nodes"]
    def run(self, ingrid_obj):
        girth_Max = ingrid_obj.get('girth', ind = 'Max')
        if (girth_Max != 'undt'):
            arboricity = ingrid_obj.get('arboricity', ind='Min')
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*arboricity*girth-(1.0*arboricity)-(1.0*girth)+2.0, ind='Min')
            except:
                pass
            girth = ingrid_obj.get('girth', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if girth != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('arboricity', 1.0*(1.0*nodes+1.0*girth-(2.0))/(girth-(1.0)), ind='Max')
                except:
                    pass
            arboricity = ingrid_obj.get('arboricity', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if arboricity != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('girth', 1.0*(1.0*nodes+1.0*arboricity-(2.0))/(arboricity-(1.0)), ind='Max')
                except:
                    pass
        return

class Theorem97(Theorem):
    def __init__(self):
        super(Theorem97, self).__init__(97, "if maxClique == 2 and chromaticNum >= 4 then { nodes >= 11 };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","nodes"]
    def run(self, ingrid_obj):
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (chromaticNum_Min>=4.0):
            try:
                ingrid_obj.set('nodes', 11.0, ind='Min')
            except:
                pass
        return

class Theorem98(Theorem):
    def __init__(self):
        super(Theorem98, self).__init__(98, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem99(Theorem):
    def __init__(self):
        super(Theorem99, self).__init__(99, "if diameter <= 2 then { edgeConnec == mindeg };", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edgeConnec","mindeg"]
    def run(self, ingrid_obj):
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        if (diameter_Max != 'undt' and (diameter_Max<=2.0)):
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('edgeConnec', mindeg, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('edgeConnec', mindeg, ind='Min')
            except:
                pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
            if edgeConnec != 'undt':
                try:
                    ingrid_obj.set('mindeg', edgeConnec, ind='Max')
                except:
                    pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
            try:
                ingrid_obj.set('mindeg', edgeConnec, ind='Min')
            except:
                pass
        return

class Theorem100(Theorem):
    def __init__(self):
        super(Theorem100, self).__init__(100, "if nodeInd >= edgeInd then { edgeCliqueCover <= nodeCover * nodeInd } ;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edgeInd","nodeCover","nodeInd"]
    def run(self, ingrid_obj):
        nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
        edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
        if (edgeInd_Max != 'undt' and (nodeInd_Min>=edgeInd_Max)):
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeCover != 'undt' and nodeInd != 'undt':
                try:
                    ingrid_obj.set('edgeCliqueCover', nodeCover*nodeInd, ind='Max')
                except:
                    pass
            edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('nodeCover', edgeCliqueCover/nodeInd, ind='Min')
                except:
                    pass
            edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodeInd', edgeCliqueCover/nodeCover, ind='Min')
                except:
                    pass
        return

class Theorem61(Theorem):
    def __init__(self):
        super(Theorem61, self).__init__(61, "if genus <= 1 then { edgeCliqueCover <= nodeCover*nodeInd };", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","genus","nodeCover","nodeInd"]
    def run(self, ingrid_obj):
        genus_Max = ingrid_obj.get('genus', ind='Max')
        if (genus_Max != 'undt' and (genus_Max<=1.0)):
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeCover != 'undt' and nodeInd != 'undt':
                try:
                    ingrid_obj.set('edgeCliqueCover', nodeCover*nodeInd, ind='Max')
                except:
                    pass
            edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('nodeCover', edgeCliqueCover/nodeInd, ind='Min')
                except:
                    pass
            edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodeInd', edgeCliqueCover/nodeCover, ind='Min')
                except:
                    pass
        return

class Theorem62(Theorem):
    def __init__(self):
        super(Theorem62, self).__init__(62, "if mindeg >= nodes/2 then { nodeConnec >= nodeInd };", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodeConnec","nodeInd","nodes"]
    def run(self, ingrid_obj):
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max/2.0)):
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            try:
                ingrid_obj.set('nodeConnec', nodeInd, ind='Min')
            except:
                pass
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
            if nodeConnec != 'undt':
                try:
                    ingrid_obj.set('nodeInd', nodeConnec, ind='Max')
                except:
                    pass
        return

class Theorem63(Theorem):
    def __init__(self):
        super(Theorem63, self).__init__(63, "null; diam<=(2*nodes + 1 - sqrt(8*edges-8*nodes+17))/2", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem64(Theorem):
    def __init__(self):
        super(Theorem64, self).__init__(64, "if nodes >= 3 and nodeConnec >= nodeInd then { hamiltonian };", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodeConnec","nodeInd","nodes"]
    def run(self, ingrid_obj):
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
        if (nodes_Min>=3.0) and (nodeInd_Max != 'undt' and (nodeConnec_Min>=nodeInd_Max)):
            ingrid_obj.set('hamiltonian', True)
        return

class Theorem65(Theorem):
    def __init__(self):
        super(Theorem65, self).__init__(65, "if edges >= (nodes**2 - 3*nodes + 6) then { hamiltonian };", "")
    def involves(self, str_invar):
        return str_invar in ["edges","hamiltonian","nodes"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (edges_Min>=(nodes_Max**2.0-(3.0*nodes_Max)+6.0))):
            ingrid_obj.set('hamiltonian', True)
        return

class Theorem66(Theorem):
    def __init__(self):
        super(Theorem66, self).__init__(66, "if planar and nodeConnec >= 4 then { hamiltonian };", "")
    def involves(self, str_invar):
        return str_invar in ["hamiltonian","nodeConnec","planar"]
    def run(self, ingrid_obj):
        planar = ingrid_obj.get('planar')
        nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
        if (planar == True) and (nodeConnec_Min>=4.0):
            ingrid_obj.set('hamiltonian', True)
        return

class Theorem67(Theorem):
    def __init__(self):
        super(Theorem67, self).__init__(67, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem68(Theorem):
    def __init__(self):
        super(Theorem68, self).__init__(68, "if complete then { regular, if complete and even nodes then { edgeChromatic == nodes - 1 } else { edgeChromatic == nodes }};", "")
    def involves(self, str_invar):
        return str_invar in ["complete","regular","edgeChromatic","nodes"]
    def run(self, ingrid_obj):
        complete = ingrid_obj.get('complete')
        if (complete == True):
            ingrid_obj.set('regular', True)
        complete = ingrid_obj.get('complete')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        
        if (complete == True) and (even(nodes_Min) and even(nodes_Max)):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', 1.0*nodes-(1.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', 1.0*nodes-(1.0), ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('nodes', 1.0*edgeChromatic+1.0, ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*edgeChromatic+1.0, ind='Min')
            except:
                pass
        elif (complete==True):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', nodes, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', nodes, ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('nodes', edgeChromatic, ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('nodes', edgeChromatic, ind='Min')
            except:
                pass
        return

class Theorem69(Theorem):
    def __init__(self):
        super(Theorem69, self).__init__(69, "chromaticNum >= 2*edges/(2*edges - spectralRadius**2);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edges","spectralRadius"]
    def run(self, ingrid_obj):
        edges = ingrid_obj.get('edges', ind='Max')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        try:
            ingrid_obj.set('chromaticNum', 2.0*edges/(2.0*edges-(1.0*spectralRadius**2.0)), ind='Min')
        except:
            pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
        if chromaticNum != 'undt' and spectralRadius != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*chromaticNum*spectralRadius**2.0/(chromaticNum-(1.0)), ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        edges = ingrid_obj.get('edges', ind='Max')
        try:
            ingrid_obj.set('spectralRadius', 1.4142135623731*(edges-(edges/chromaticNum))**0.5, ind='Max')
        except:
            pass
        return

class Theorem70(Theorem):
    def __init__(self):
        super(Theorem70, self).__init__(70, "if genus <= 1 and girth == 3 then { chromaticNum <= 7 } else if genus <= 1 and girth >= 4 then { chromaticNum <= 4 };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","genus","girth"]
    def run(self, ingrid_obj):
        genus_Max = ingrid_obj.get('genus', ind='Max')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        girth_Max = ingrid_obj.get('girth', ind='Max')
        if (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
            try:
                ingrid_obj.set('chromaticNum', 7.0, ind='Max')
            except:
                pass
        elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Min != 'undt' and girth_Min>=4.0):
            try:
                ingrid_obj.set('chromaticNum', 4.0, ind='Max')
            except:
                pass
        return

class Theorem71(Theorem):
    def __init__(self):
        super(Theorem71, self).__init__(71, "if exists girth then { circumference <= nodes, circumference <= edges, circumference <= nodes - (numOfComponents - 1)*(mindeg + 1), circumference <= edges - (numOfComponents - 1)*mindeg, maxdeg >= 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","girth","maxdeg","mindeg","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        girth_Max = ingrid_obj.get('girth', ind = 'Max')
        if (girth_Max != 'undt'):
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            if mindeg != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('circumference', -(1.0*mindeg*numOfComponents)+1.0*mindeg+1.0*nodes-(1.0*numOfComponents)+1.0, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', 1.0*(-(circumference)+nodes-(numOfComponents)+1.0)/(numOfComponents-(1.0)), ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*circumference+1.0*mindeg*numOfComponents-(1.0*mindeg)+1.0*numOfComponents-(1.0), ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if mindeg != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('numOfComponents', 1.0*(-(circumference)+mindeg+nodes+1.0)/(mindeg+1.0), ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            if edges != 'undt' and mindeg != 'undt':
                try:
                    ingrid_obj.set('circumference', 1.0*edges-(1.0*mindeg*numOfComponents)+1.0*mindeg, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            try:
                ingrid_obj.set('edges', 1.0*circumference+1.0*mindeg*numOfComponents-(1.0*mindeg), ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            edges = ingrid_obj.get('edges', ind='Max')
            numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
            if edges != 'undt':
                try:
                    ingrid_obj.set('mindeg', 1.0*(-(circumference)+edges)/(numOfComponents-(1.0)), ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            edges = ingrid_obj.get('edges', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            if edges != 'undt' and mindeg != 'undt':
                try:
                    ingrid_obj.set('numOfComponents', 1.0*(-(circumference)+edges+mindeg)/mindeg, ind='Max')
                except:
                    pass
            try:
                ingrid_obj.set('maxdeg', 2.0, ind='Min')
            except:
                pass
        return

class Theorem72(Theorem):
    def __init__(self):
        super(Theorem72, self).__init__(72, "if hamiltonian or circumference == nodes then { hamiltonian, circumference == nodes };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","hamiltonian","nodes"]
    def run(self, ingrid_obj):
        hamiltonian = ingrid_obj.get('hamiltonian')
        circumference_Max = ingrid_obj.get('circumference', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        circumference_Min = ingrid_obj.get('circumference', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (hamiltonian == True) or (circumference_Max != 'undt' and (circumference_Max<=nodes_Min)) and (nodes_Max != 'undt' and (circumference_Min>=nodes_Max)):
            ingrid_obj.set('hamiltonian', True)
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('circumference', nodes, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('circumference', nodes, ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('nodes', circumference, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            try:
                ingrid_obj.set('nodes', circumference, ind='Min')
            except:
                pass
        return

class Theorem73(Theorem):
    def __init__(self):
        super(Theorem73, self).__init__(73, "if hamiltonian then { arboricity >= 2, nodeConnec >= 2, nodeInd <= nodes/2, edgeCover <= (nodes + 1)/2, nodeCliqueCover <= (nodes + 1)/2, nodeCover >= nodes/2, edgeInd >= (nodes - 1)/2 };", "")
    def involves(self, str_invar):
        return str_invar in ["arboricity","edgeCover","edgeInd","hamiltonian","nodeCliqueCover","nodeConnec","nodeCover","nodeInd","nodes"]
    def run(self, ingrid_obj):
        hamiltonian = ingrid_obj.get('hamiltonian')
        if (hamiltonian == True):
            try:
                ingrid_obj.set('arboricity', 2.0, ind='Min')
            except:
                pass
            try:
                ingrid_obj.set('nodeConnec', 2.0, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeInd', 0.5*nodes, ind='Max')
                except:
                    pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*nodeInd, ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Max')
                except:
                    pass
            edgeCover = ingrid_obj.get('edgeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*edgeCover-(1.0), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCliqueCover', 0.5*nodes+0.5, ind='Max')
                except:
                    pass
            nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 2.0*nodeCliqueCover-(1.0), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('nodeCover', 0.5*nodes, ind='Min')
            except:
                pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Max')
            if nodeCover != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*nodeCover, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeInd', 0.5*nodes-(0.5), ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*edgeInd+1.0, ind='Max')
                except:
                    pass
        return

class Theorem74(Theorem):
    def __init__(self):
        super(Theorem74, self).__init__(74, "null; bandwidth <= nodes - nodeInd/2 - 1;", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodeInd","nodes"]
    def run(self, ingrid_obj):
        return

class Theorem75(Theorem):
    def __init__(self):
        super(Theorem75, self).__init__(75, "edges >= (nodes/nodeInd)*(nodes-nodeInd*(nodes/nodeInd+1)/2);", "Turan\'s Theorem")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeInd","nodes"]
    def run(self, ingrid_obj):
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if nodeInd != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*nodes*(-(nodeInd)+nodes)/nodeInd, ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('nodeInd', 0.5*nodes**2.0/(1.0*edges+0.5*nodes), ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        if edges != 'undt' and nodeInd != 'undt':
            try:
                ingrid_obj.set('nodes', 0.5*nodeInd+1.0*(nodeInd*(2.0*edges+0.25*nodeInd))**(1/2), ind='Max')
            except:
                pass
        return

class Theorem76(Theorem):
    def __init__(self):
        super(Theorem76, self).__init__(76, "edgeCliqueCover <= nodeCliqueCover + nodes*(nodeCliqueCover - 1)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","nodeCliqueCover","nodes"]
    def run(self, ingrid_obj):
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodeCliqueCover != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('edgeCliqueCover', 0.5*nodeCliqueCover*nodes+1.0*nodeCliqueCover-(0.5*nodes), ind='Max')
            except:
                pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        try:
            ingrid_obj.set('nodeCliqueCover', (1.0*edgeCliqueCover+0.5*nodes)/(0.5*nodes+1.0), ind='Min')
        except:
            pass
        edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
        if nodeCliqueCover != 'undt':
            try:
                ingrid_obj.set('nodes', 2.0*(edgeCliqueCover-(nodeCliqueCover))/(nodeCliqueCover-(1.0)), ind='Min')
            except:
                pass
        return

class Theorem77(Theorem):
    def __init__(self):
        super(Theorem77, self).__init__(77, "if nodes >= 6*mindeg and edges > (1/2)*(nodes-mindeg)*(nodes - mindeg - 1) + mindeg**2 then { hamiltonian };", "")
    def involves(self, str_invar):
        return str_invar in ["edges","hamiltonian","mindeg","nodes"]
    def run(self, ingrid_obj):
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (mindeg_Max != 'undt' and (nodes_Min>=6.0*mindeg_Max)) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>(1.0/2.0)*(nodes_Max-(mindeg_Max))*(nodes_Max-(mindeg_Max)-(1.0))+mindeg_Max**2.0)):
            ingrid_obj.set('hamiltonian', True)
        return

class Theorem78(Theorem):
    def __init__(self):
        super(Theorem78, self).__init__(78, "if nodes >= 4 and edges >= 2*nodes - 3 then { girth <= (circumference + 2)/2 };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","girth","nodes"]
    def run(self, ingrid_obj):
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Min>=4.0) and (nodes_Max != 'undt' and (edges_Min>=2.0*nodes_Max-(3.0))):
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('girth', 0.5*circumference+1.0, ind='Max')
                except:
                    pass
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('circumference', 2.0*girth-(2.0), ind='Min')
            except:
                pass
        return

class Theorem79(Theorem):
    def __init__(self):
        super(Theorem79, self).__init__(79, "if not forest then { nodeInd >= girth/2, radius >= girth/2, edgeInd >= circumference/2 };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edgeInd","forest","girth","nodeInd","radius"]
    def run(self, ingrid_obj):
        forest = ingrid_obj.get('forest')
        if (forest == False):
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('nodeInd', 0.5*girth, ind='Min')
            except:
                pass
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('girth', 2.0*nodeInd, ind='Max')
                except:
                    pass
            girth = ingrid_obj.get('girth', ind='Min')
            try:
                ingrid_obj.set('radius', 0.5*girth, ind='Min')
            except:
                pass
            radius = ingrid_obj.get('radius', ind='Max')
            if radius != 'undt':
                try:
                    ingrid_obj.set('girth', 2.0*radius, ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Min')
            try:
                ingrid_obj.set('edgeInd', 0.5*circumference, ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            if edgeInd != 'undt':
                try:
                    ingrid_obj.set('circumference', 2.0*edgeInd, ind='Max')
                except:
                    pass
        return

class Theorem80(Theorem):
    def __init__(self):
        super(Theorem80, self).__init__(80, "if (defined girth and girth >= 4) or (undefined girth and nodes > 2) then { not complete };", "")
    def involves(self, str_invar):
        return str_invar in ["complete","girth","nodes"]
    def run(self, ingrid_obj):
        girth_Max = ingrid_obj.get('girth', ind = 'Max')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        if (girth_Min != 'undt' and girth_Min>=4.0) or (girth_Min == 'undt' and nodes_Min>2.0):
            ingrid_obj.set('complete', False)
        return

class Theorem101(Theorem):
    def __init__(self):
        super(Theorem101, self).__init__(101, "if connected or odd nodes then {nodeCover <= (nodes-1)*(nodes+1)/2, edgeCover <= (nodes-1)*(nodes+1)/2 } else {nodeCover <= (nodes-2)*(nodes+2)/2, edgeCover <= (nodes-2)*(nodes+2)/2 };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","edgeCover","nodeCover","nodes"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        
        if (connected == True) or (odd(nodes_Max)):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(0.5), ind='Max')
                except:
                    pass
            nodeCover = ingrid_obj.get('nodeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*(2.0*nodeCover+1.0)**(1/2), ind='Min')
            except:
                pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(0.5), ind='Max')
                except:
                    pass
            edgeCover = ingrid_obj.get('edgeCover', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*(2.0*edgeCover+1.0)**(1/2), ind='Min')
            except:
                pass
        elif (True):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(2.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(2.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(2.0), ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(2.0), ind='Max')
                except:
                    pass
        return

class Theorem102(Theorem):
    def __init__(self):
        super(Theorem102, self).__init__(102, "edgeChromatic <= 2*bandwidth;", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","edgeChromatic"]
    def run(self, ingrid_obj):
        bandwidth = ingrid_obj.get('bandwidth', ind='Max')
        if bandwidth != 'undt':
            try:
                ingrid_obj.set('edgeChromatic', 2.0*bandwidth, ind='Max')
            except:
                pass
        edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
        try:
            ingrid_obj.set('bandwidth', 0.5*edgeChromatic, ind='Min')
        except:
            pass
        return

class Theorem103(Theorem):
    def __init__(self):
        super(Theorem103, self).__init__(103, "circumference >= maxClique*mindeg/(maxClique - 1);", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","maxClique","mindeg"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        try:
            ingrid_obj.set('circumference', 1.0*maxClique*mindeg/(maxClique-(1.0)), ind='Min')
        except:
            pass
        circumference = ingrid_obj.get('circumference', ind='Max')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        if circumference != 'undt' and mindeg != 'undt':
            try:
                ingrid_obj.set('maxClique', 1.0*circumference/(circumference-(mindeg)), ind='Min')
            except:
                pass
        circumference = ingrid_obj.get('circumference', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if circumference != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('mindeg', 1.0*circumference*(maxClique-(1.0))/maxClique, ind='Max')
            except:
                pass
        return

class Theorem104(Theorem):
    def __init__(self):
        super(Theorem104, self).__init__(104, "circumference >= maxClique*(chromaticNum-1)/(maxClique-1);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","circumference","maxClique"]
    def run(self, ingrid_obj):
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        if chromaticNum != 'undt':
            ingrid_obj.set('maxClique', chromaticNum, ind='Max')

        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        try:
            ingrid_obj.set('circumference', 1.0*maxClique*(chromaticNum-(1.0))/(maxClique-(1.0)), ind='Min')
        except:
            pass
        circumference = ingrid_obj.get('circumference', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if circumference != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 1.0*circumference-(1.0*circumference/maxClique)+1.0, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        circumference = ingrid_obj.get('circumference', ind='Max')
        try:
            ingrid_obj.set('maxClique', 1.0*circumference/(circumference-(chromaticNum)+1.0), ind='Min')
        except:
            pass
        return

class Theorem105(Theorem):
    def __init__(self):
        super(Theorem105, self).__init__(105, "if maxClique == 2 and chromaticNum >= 3 then { circumference >= 2*chromaticNum - 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","circumference","maxClique"]
    def run(self, ingrid_obj):
        maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (chromaticNum_Min>=3.0):
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            try:
                ingrid_obj.set('circumference', 2.0*chromaticNum-(1.0), ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('chromaticNum', 0.5*circumference+0.5, ind='Max')
                except:
                    pass
        return

class Theorem106(Theorem):
    def __init__(self):
        super(Theorem106, self).__init__(106, "edges <= nodeCover*(nodeInd + nodeCover*(chromaticNum-1)/(2*chromaticNum));", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edges","nodeCover","nodeInd"]
    def run(self, ingrid_obj):
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        if chromaticNum != 'undt' and nodeCover != 'undt' and nodeInd != 'undt':
            try:
                ingrid_obj.set('edges', nodeCover*(0.5*chromaticNum*nodeCover+1.0*chromaticNum*nodeInd-(0.5*nodeCover))/chromaticNum, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Min')
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        if nodeInd != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 1.0*nodeCover**2.0/(-(2.0*edges)+1.0*nodeCover**2.0+2.0*nodeCover*nodeInd), ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        edges = ingrid_obj.get('edges', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        if nodeInd != 'undt':
            try:
                ingrid_obj.set('nodeCover', -((1.0*chromaticNum*nodeInd+1.0*(chromaticNum*(2.0*edges*chromaticNum-(2.0*edges)+1.0*chromaticNum*nodeInd**2.0))**(1/2))/(chromaticNum-(1.0))), ind='Min')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
        edges = ingrid_obj.get('edges', ind='Min')
        nodeCover = ingrid_obj.get('nodeCover', ind='Max')
        if chromaticNum != 'undt':
            try:
                ingrid_obj.set('nodeInd', 1.0*edges/nodeCover-(0.5*nodeCover)+0.5*nodeCover/chromaticNum, ind='Min')
            except:
                pass
        return

class Theorem107(Theorem):
    def __init__(self):
        super(Theorem107, self).__init__(107, "mindeg<=maxdeg;", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","mindeg"]
    def run(self, ingrid_obj):
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        if maxdeg != 'undt':
            try:
                ingrid_obj.set('mindeg', maxdeg, ind='Max')
            except:
                pass
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        try:
            ingrid_obj.set('maxdeg', mindeg, ind='Min')
        except:
            pass
        return

class Theorem108(Theorem):
    def __init__(self):
        super(Theorem108, self).__init__(108, "nodeCliqueCover <= (nodes + nodeInd - maxClique + 1)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCliqueCover","nodeInd","nodes"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodeInd != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('nodeCliqueCover', -(0.5*maxClique)+0.5*nodeInd+0.5*nodes+0.5, ind='Max')
            except:
                pass
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodeInd != 'undt' and nodes != 'undt':
            try:
                ingrid_obj.set('maxClique', -(2.0*nodeCliqueCover)+1.0*nodeInd+1.0*nodes+1.0, ind='Max')
            except:
                pass
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Max')
        if nodes != 'undt':
            try:
                ingrid_obj.set('nodeInd', 2.0*nodeCliqueCover+1.0*maxClique-(1.0*nodes)-(1.0), ind='Min')
            except:
                pass
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Max')
        if nodeInd != 'undt':
            try:
                ingrid_obj.set('nodes', 2.0*nodeCliqueCover+1.0*maxClique-(1.0*nodeInd)-(1.0), ind='Min')
            except:
                pass
        return

class Theorem109(Theorem):
    def __init__(self):
        super(Theorem109, self).__init__(109, "nodeCover <= 2*edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodeCover"]
    def run(self, ingrid_obj):
        edgeInd = ingrid_obj.get('edgeInd', ind='Max')
        if edgeInd != 'undt':
            try:
                ingrid_obj.set('nodeCover', 2.0*edgeInd, ind='Max')
            except:
                pass
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        try:
            ingrid_obj.set('edgeInd', 0.5*nodeCover, ind='Min')
        except:
            pass
        return

class Theorem110(Theorem):
    def __init__(self):
        super(Theorem110, self).__init__(110, "if mindeg >= 4 and girth >= 5 then { circumference >= (girth-2)*(mindeg-2)+5 };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","girth","mindeg"]
    def run(self, ingrid_obj):
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        if (mindeg_Min>=4.0) and (girth_Min != 'undt' and girth_Min>=5.0):
            girth = ingrid_obj.get('girth', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('circumference', 1.0*girth*mindeg-(2.0*girth)-(2.0*mindeg)+9.0, ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if circumference != 'undt' and mindeg != 'undt':
                try:
                    ingrid_obj.set('girth', (1.0*circumference+2.0*mindeg-(9.0))/(1.0*mindeg-(2.0)), ind='Max')
                except:
                    pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            girth = ingrid_obj.get('girth', ind='Max')
            if circumference != 'undt' and girth != 'undt':
                try:
                    ingrid_obj.set('mindeg', (1.0*circumference+2.0*girth-(9.0))/(1.0*girth-(2.0)), ind='Max')
                except:
                    pass
        return

class Theorem111(Theorem):
    def __init__(self):
        super(Theorem111, self).__init__(111, "if connected then { diameter <= 2*nodeInd - 1 };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","nodeInd"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        if (connected == True):
            nodeInd = ingrid_obj.get('nodeInd', ind='Max')
            if nodeInd != 'undt':
                try:
                    ingrid_obj.set('diameter', 2.0*nodeInd-(1.0), ind='Max')
                except:
                    pass
            diameter = ingrid_obj.get('diameter', ind='Min')
            try:
                ingrid_obj.set('nodeInd', 0.5*diameter+0.5, ind='Min')
            except:
                pass
        return

class Theorem112(Theorem):
    def __init__(self):
        super(Theorem112, self).__init__(112, "if connected and nodeInd <= mindeg then { mindeg >= (nodes+2)/3 };", "")
    def involves(self, str_invar):
        return str_invar in ["connected","mindeg","nodeInd","nodes"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        if (connected == True) and (nodeInd_Max != 'undt' and (nodeInd_Max<=mindeg_Min)):
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('mindeg', 0.333333333333333*nodes+0.666666666666667, ind='Min')
            except:
                pass
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('nodes', 3.0*mindeg-(2.0), ind='Max')
                except:
                    pass
        return

class Theorem113(Theorem):
    def __init__(self):
        super(Theorem113, self).__init__(113, "edges >= nodeInd*mindeg + (maxClique-1)*(maxClique-2)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxClique","mindeg","nodeInd"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Min')
        try:
            ingrid_obj.set('edges', 0.5*maxClique**2.0-(1.5*maxClique)+1.0*mindeg*nodeInd+1.0, ind='Min')
        except:
            pass
        edges = ingrid_obj.get('edges', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        nodeInd = ingrid_obj.get('nodeInd', ind='Min')
        if edges != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('mindeg', (1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0))/nodeInd, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        mindeg = ingrid_obj.get('mindeg', ind='Min')
        if edges != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('nodeInd', (1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0))/mindeg, ind='Max')
            except:
                pass
        return

class Theorem114(Theorem):
    def __init__(self):
        super(Theorem114, self).__init__(114, "edges >= nodeCover + (maxClique-1)*(maxClique-2)/2;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","maxClique","nodeCover"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        try:
            ingrid_obj.set('edges', 0.5*maxClique**2.0-(1.5*maxClique)+1.0*nodeCover+1.0, ind='Min')
        except:
            pass
        edges = ingrid_obj.get('edges', ind='Max')
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('maxClique', 0.5*(8.0*edges-(8.0*nodeCover)+1.0)**(1/2)+1.5, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        maxClique = ingrid_obj.get('maxClique', ind='Min')
        if edges != 'undt' and maxClique != 'undt':
            try:
                ingrid_obj.set('nodeCover', 1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0), ind='Max')
            except:
                pass
        return

class Theorem115(Theorem):
    def __init__(self):
        super(Theorem115, self).__init__(115, "edges >= chromaticNum*(chromaticNum-3)/2 + nodes - numOfComponents + 1;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","edges","nodes","numOfComponents"]
    def run(self, ingrid_obj):
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        nodes = ingrid_obj.get('nodes', ind='Min')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
        if numOfComponents != 'undt':
            try:
                ingrid_obj.set('edges', 0.5*chromaticNum**2.0-(1.5*chromaticNum)+1.0*nodes-(1.0*numOfComponents)+1.0, ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
        if edges != 'undt' and numOfComponents != 'undt':
            try:
                ingrid_obj.set('chromaticNum', 0.5*(8.0*edges-(8.0*nodes)+8.0*numOfComponents+1.0)**(1/2)+1.5, ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        edges = ingrid_obj.get('edges', ind='Max')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
        if chromaticNum != 'undt' and edges != 'undt' and numOfComponents != 'undt':
            try:
                ingrid_obj.set('nodes', 1.0*edges-(0.5*chromaticNum**2.0)+1.5*chromaticNum+1.0*numOfComponents-(1.0), ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        edges = ingrid_obj.get('edges', ind='Max')
        nodes = ingrid_obj.get('nodes', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('numOfComponents', -(1.0*edges)+0.5*chromaticNum**2.0-(1.5*chromaticNum)+1.0*nodes+1.0, ind='Min')
            except:
                pass
        return

class Theorem116(Theorem):
    def __init__(self):
        super(Theorem116, self).__init__(116, "if bipartite and even nodes then {genus <= ((nodes-4)**2 + 15)/16}; if bipartite and odd nodes then { genus <= ((nodes-3)*(nodes-5)+15)/16};", "")
    def involves(self, str_invar):
        return str_invar in ["bipartite","genus","nodes"]
    def run(self, ingrid_obj):
        bipartite = ingrid_obj.get('bipartite')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (bipartite == True) and (even(nodes_Min) and even(nodes_Max)):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('genus', 6.25e-2*(nodes-(4.0))**2.0+0.9375, ind='Max')
                except:
                    pass
            genus = ingrid_obj.get('genus', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*(16.0*genus-(15.0))**0.5+4.0, ind='Min')
            except:
                pass
        bipartite = ingrid_obj.get('bipartite')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (bipartite == True) and (odd(nodes_Min) and odd(nodes_Max)):
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('genus', 6.25e-2*nodes**2.0-(0.5*nodes)+1.875, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('genus', 6.25e-2*nodes**2.0-(0.5*nodes)+1.875, ind='Max')
                except:
                    pass
        return

class Theorem117(Theorem):
    def __init__(self):
        super(Theorem117, self).__init__(117, "if not complete then { nodeConnec >= 2*mindeg - nodes + 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["complete","mindeg","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        complete = ingrid_obj.get('complete')
        if (complete == False):
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('nodeConnec', 2.0*mindeg-(1.0*nodes)+2.0, ind='Min')
                except:
                    pass
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodeConnec != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', 0.5*nodeConnec+0.5*nodes-(1.0), ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
            if nodeConnec != 'undt':
                try:
                    ingrid_obj.set('nodes', -(1.0*nodeConnec)+2.0*mindeg+2.0, ind='Min')
                except:
                    pass
        return

class Theorem118(Theorem):
    def __init__(self):
        super(Theorem118, self).__init__(118, "if (nodes>=6 and even nodes and edges >= (nodes**2)/4 +1) or (nodes>=7 and odd nodes  and edges>=(nodes-1)**2/4 +1+mindeg) then { circumference>=5 };", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","mindeg","nodes"]
    def run(self, ingrid_obj):
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        edges_Min = ingrid_obj.get('edges', ind='Min')
        mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
        if (nodes_Min>=6.0) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (edges_Min>=(nodes_Max**2.0)/4.0+1.0)) or (nodes_Min>=7.0) and (odd(nodes_Min) and odd(nodes_Max)) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>=(nodes_Max-(1.0))**2.0/4.0+1.0+mindeg_Max)):
            try:
                ingrid_obj.set('circumference', 5.0, ind='Min')
            except:
                pass
        return

class Theorem119(Theorem):
    def __init__(self):
        super(Theorem119, self).__init__(119, "if chromaticNum >= maxClique then {mindeg <= (3*maxClique - 4)*nodes / (3*maxClique-1)};", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","mindeg","nodes"]
    def run(self, ingrid_obj):
        chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
        maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
        if (maxClique_Max != 'undt' and (chromaticNum_Min>=maxClique_Max)):
            maxClique = ingrid_obj.get('maxClique', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if maxClique != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', nodes*(3.0*maxClique-(4.0))/(3.0*maxClique-(1.0)), ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('maxClique', (0.333333333333333*mindeg-(1.33333333333333*nodes))/(mindeg-(nodes)), ind='Min')
            except:
                pass
            maxClique = ingrid_obj.get('maxClique', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('nodes', mindeg*(3.0*maxClique-(1.0))/(3.0*maxClique-(4.0)), ind='Min')
            except:
                pass
        return

class Theorem120(Theorem):
    def __init__(self):
        super(Theorem120, self).__init__(120, "if hamiltonian and nodes>=chromaticNum-1 and chromaticNum >= 4 then { edges>= (chromaticNum-1)*(chromaticNum-2)/2 + nodes }; if hamiltonian and chromaticNum==3 and even nodes then {edges >= nodes +1};", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","e","hamiltonian","nodes","p","edges"]
    def run(self, ingrid_obj):
        return

class Theorem121(Theorem):
    def __init__(self):
        super(Theorem121, self).__init__(121, "if defined diameter  { chromaticNum <= nodes - nodeConnec*(diameter - 3) - 2 };", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","diameter","nodeConnec","nodes"]
    def run(self, ingrid_obj):
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        if diameter_Max != 'undt':
            diameter = ingrid_obj.get('diameter', ind='Min')
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodeConnec != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('chromaticNum', -(1.0*diameter*nodeConnec)+3.0*nodeConnec+1.0*nodes-(2.0), ind='Max')
                except:
                    pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodeConnec != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('diameter', (-(1.0*chromaticNum)+3.0*nodeConnec+1.0*nodes-(2.0))/nodeConnec, ind='Max')
                except:
                    pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            diameter = ingrid_obj.get('diameter', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                if diameter > 3:
                    try:
                        ingrid_obj.set('nodeConnec', (-(1.0*chromaticNum)+1.0*nodes-(2.0))/(1.0*diameter-(3.0)), ind='Max')
                    except:
                        pass
            chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
            diameter = ingrid_obj.get('diameter', ind='Min')
            nodeConnec = ingrid_obj.get('nodeConnec', ind='Max') if diameter < 3 else ingrid_obj.get('nodeConnec', ind='Min')
            try:
                ingrid_obj.set('nodes', 1.0*chromaticNum+1.0*diameter*nodeConnec-(3.0*nodeConnec)+2.0, ind='Min')
            except:
                pass
        return

class Theorem122(Theorem):
    def __init__(self):
        super(Theorem122, self).__init__(122, "if edges >= nodes**2/4 then {edgeCliqueCover <= ((1/2)*nodes*(nodes-1) - edges) + (1 + sqrt(1 + 4*((1/2)*nodes*(nodes-1) - edges)))};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeCliqueCover","edges","nodes"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (edges_Min>=nodes_Max**2.0/4.0)):
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCliqueCover', -(edges)+0.5*nodes**2.0-(0.5*nodes)+(-(4.0*edges)+2.0*nodes**2.0-(2.0*nodes)+1.0)**0.5+1.0, ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCliqueCover', ((1.0+4.0*((1.0/2.0)*nodes*(nodes-((1.0)))-((edges))))**(1.0/2.0)+1.0)+(-((edges))+(1.0/2.0)*nodes*(-((1.0))+nodes)), ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('edgeCliqueCover', ((1.0+4.0*((1.0/2.0)*nodes*(nodes-((1.0)))-((edges))))**(1.0/2.0)+1.0)+(-((edges))+(1.0/2.0)*nodes*(-((1.0))+nodes)), ind='Max')
                except:
                    pass
        return

class Theorem123(Theorem):
    def __init__(self):
        super(Theorem123, self).__init__(123, "if nodes <= 2*edges then {mindeg == edgeConnec};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","edges","mindeg","nodes"]
    def run(self, ingrid_obj):
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        edges_Min = ingrid_obj.get('edges', ind='Min')
        if (nodes_Max != 'undt' and (nodes_Max<=2.0*edges_Min)):
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
            if edgeConnec != 'undt':
                try:
                    ingrid_obj.set('mindeg', edgeConnec, ind='Max')
                except:
                    pass
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
            try:
                ingrid_obj.set('mindeg', edgeConnec, ind='Min')
            except:
                pass
            mindeg = ingrid_obj.get('mindeg', ind='Max')
            if mindeg != 'undt':
                try:
                    ingrid_obj.set('edgeConnec', mindeg, ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('edgeConnec', mindeg, ind='Min')
            except:
                pass
        return

class Theorem124(Theorem):
    def __init__(self):
        super(Theorem124, self).__init__(124, "if connected then { bandwidth >= (nodes-1)/diameter };", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","connected","diameter","nodes"]
    def run(self, ingrid_obj):
        connected = ingrid_obj.get('connected')
        if (connected == True):
            diameter = ingrid_obj.get('diameter', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if diameter != 'undt':
                try:
                    ingrid_obj.set('bandwidth', 1.0*(nodes-(1.0))/diameter, ind='Min')
                except:
                    pass
            bandwidth = ingrid_obj.get('bandwidth', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if bandwidth != 'undt':
                try:
                    ingrid_obj.set('diameter', 1.0*(nodes-(1.0))/bandwidth, ind='Min')
                except:
                    pass
            bandwidth = ingrid_obj.get('bandwidth', ind='Max')
            diameter = ingrid_obj.get('diameter', ind='Max')
            if bandwidth != 'undt' and diameter != 'undt':
                try:
                    ingrid_obj.set('nodes', 1.0*bandwidth*diameter+1.0, ind='Max')
                except:
                    pass
        return

class Theorem125(Theorem):
    def __init__(self):
        super(Theorem125, self).__init__(125, "if genus >= 1 and istrue congruent(girth, 3, 4) then { nodes >= 9*(girth-1)/4 + 1 } else { nodes >= 9*(girth-1)/4 };", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","nodes"]
    def run(self, ingrid_obj):
        # genus_Min = ingrid_obj.get('genus', ind='Min')
        # girth_Min = ingrid_obj.get('girth', ind = 'Min')
        # girth_Max = ingrid_obj.get('girth', ind = 'Max')
        
        # if (genus_Min>=1.0) and (girth_Min == girth_Max):
        #     girth = ingrid_obj.get('girth', ind='Min')
        #     try:
        #         ingrid_obj.set('nodes', 2.25*girth-(1.25), ind='Min')
        #     except:
        #         pass
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if nodes != 'undt':
        #         try:
        #             ingrid_obj.set('girth', 0.444444444444444*nodes+0.555555555555556, ind='Max')
        #         except:
        #             pass
        # elif (True):
        #     girth = ingrid_obj.get('girth', ind='Min')
        #     try:
        #         ingrid_obj.set('nodes', 2.25*girth-(2.25), ind='Min')
        #     except:
        #         pass
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if nodes != 'undt':
        #         try:
        #             ingrid_obj.set('girth', 0.444444444444444*nodes+1.0, ind='Max')
        #         except:
        #             pass
        return

class Theorem126(Theorem):
    def __init__(self):
        super(Theorem126, self).__init__(126, "if nodes <= mindeg * 2 then {nodes <= 2*edgeConnec + 3};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeConnec","mindeg","nodes"]
    def run(self, ingrid_obj):
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
        if (nodes_Max != 'undt' and (nodes_Max<=mindeg_Min*2.0)):
            edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
            if edgeConnec != 'undt':
                try:
                    ingrid_obj.set('nodes', 2.0*edgeConnec+3.0, ind='Max')
                except:
                    pass
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edgeConnec', 0.5*nodes-(1.5), ind='Min')
            except:
                pass
        return

class Theorem127(Theorem):
    def __init__(self):
        super(Theorem127, self).__init__(127, "if hamiltonian and even nodes and maxdeg == 3 then {edgeChromatic == maxdeg};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeChromatic","hamiltonian","maxdeg","nodes"]
    def run(self, ingrid_obj):
        hamiltonian = ingrid_obj.get('hamiltonian')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        if (hamiltonian == True) and (even(nodes_Min) and even(nodes_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)):
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('edgeChromatic', maxdeg, ind='Max')
                except:
                    pass
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('edgeChromatic', maxdeg, ind='Min')
            except:
                pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
            if edgeChromatic != 'undt':
                try:
                    ingrid_obj.set('maxdeg', edgeChromatic, ind='Max')
                except:
                    pass
            edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
            try:
                ingrid_obj.set('maxdeg', edgeChromatic, ind='Min')
            except:
                pass
        return

class Theorem128(Theorem):
    def __init__(self):
        super(Theorem128, self).__init__(128, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem129(Theorem):
    def __init__(self):
        super(Theorem129, self).__init__(129, "if defined girth and girth > 3 then {mindeg <= (nodes - diameter + 3*(diameter/3 + 1) -3)/ (diameter/3+1)};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","girth","mindeg","nodes"]
    def run(self, ingrid_obj):
        girth_Max = ingrid_obj.get('girth', ind = 'Max')
        girth_Min = ingrid_obj.get('girth', ind='Min')
        if (girth_Max != 'undt') and (girth_Min != 'undt' and girth_Min>3.0):
            diameter = ingrid_obj.get('diameter', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('mindeg', 1.0*nodes/(0.333333333333333*diameter+1.0), ind='Max')
                except:
                    pass
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if nodes != 'undt':
                try:
                    ingrid_obj.set('diameter', -(3.0)+3.0*nodes/mindeg, ind='Max')
                except:
                    pass
            diameter = ingrid_obj.get('diameter', ind='Min')
            mindeg = ingrid_obj.get('mindeg', ind='Min')
            try:
                ingrid_obj.set('nodes', mindeg*(0.333333333333333*diameter+1.0), ind='Min')
            except:
                pass
        return

class Theorem130(Theorem):
    def __init__(self):
        super(Theorem130, self).__init__(130, "if diameter == 2 and nodes >= maxdeg * maxdeg / 8 then {edges >= nodes *(nodes - 1)/(2 * maxdeg)} else if diameter == 2 and nodes < maxdeg * maxdeg /8 then {edges >= maxdeg * nodes * (nodes - 1)/ (maxdeg * maxdeg + 8*nodes)};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edges","maxdeg","nodes"]
    def run(self, ingrid_obj):
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (maxdeg_Max != 'undt' and (nodes_Min>=maxdeg_Max*maxdeg_Max/8.0)):
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if maxdeg != 'undt':
                try:
                    ingrid_obj.set('edges', 0.5*nodes*(nodes-(1.0))/maxdeg, ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if edges != 'undt':
                try:
                    ingrid_obj.set('maxdeg', 0.5*nodes*(nodes-(1.0))/edges, ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if edges != 'undt' and maxdeg != 'undt':
                try:
                    ingrid_obj.set('nodes', 0.5*(8.0*edges*maxdeg+1.0)**(1/2)+0.5, ind='Max')
                except:
                    pass
        elif (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodes_Max != 'undt' and (nodes_Max<maxdeg_Min*maxdeg_Min/8.0)):
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edges', 1.0*maxdeg*nodes*(nodes-(1.0))/(1.0*maxdeg**2.0+8.0*nodes), ind='Min')
            except:
                pass
            edges = ingrid_obj.get('edges', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Min')
            if edges != 'undt':
                try:
                    ingrid_obj.set('maxdeg', 0.5*(nodes*(nodes-(1.0))+(-(nodes*(32.0*edges**2.0-(1.0*nodes**3.0)+2.0*nodes**2.0-(1.0*nodes))))**(1/2))/edges, ind='Min')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Max')
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if edges != 'undt' and maxdeg != 'undt':
                try:
                    ingrid_obj.set('nodes', (4.0*edges+0.5*maxdeg+0.5*(64.0*edges**2.0+4.0*edges*maxdeg**3.0+16.0*edges*maxdeg+1.0*maxdeg**2.0)**(1/2))/maxdeg, ind='Max')
                except:
                    pass
        return

class Theorem131(Theorem):
    def __init__(self):
        super(Theorem131, self).__init__(131, "chromaticNum <= maxdeg - 1 + (maxdeg+1)/max(4, maxClique + 1);", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","maxClique","maxdeg"]
    def run(self, ingrid_obj):
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        if maxClique != 'undt' and maxdeg != 'undt':
            try:
                ingrid_obj.set('chromaticNum', maxdeg+1.0+int((maxdeg+1.0)/max(4.0, maxClique+1.0)), ind='Max')
            except:
                pass
        chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
        maxClique = ingrid_obj.get('maxClique', ind='Max')
        if maxClique != 'undt':
            try:
                ingrid_obj.set('maxdeg', (chromaticNum*max(4.0, maxClique+1.0)-(1.0))/(max(4.0, maxClique+1.0)-1.0)-1, ind='Min')
            except:
                pass
        return

class Theorem132(Theorem):
    def __init__(self):
        super(Theorem132, self).__init__(132, "if istrue congruent(nodes, 3, 4) then {mindeg <= (nodes-1)**2 / (4*(nodes-1-maxdeg))} else {mindeg <= (nodes-3)*(nodes+1)/(4*(nodes-1-maxdeg))};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","mindeg","nodes"]
    def run(self, ingrid_obj):
        # nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
        # nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
        
        # if (nodes_Min == nodes_Max):
        #     maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Min')
        #     if maxdeg != 'undt':
        #         try:
        #             ingrid_obj.set('mindeg', -(0.25*(nodes-(1.0))**2.0/(maxdeg-(nodes)+1.0)), ind='Max')
        #         except:
        #             pass
        #     mindeg = ingrid_obj.get('mindeg', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if mindeg != 'undt' and nodes != 'undt':
        #         try:
        #             ingrid_obj.set('maxdeg', 1.0*nodes-(1.0)-(0.25*(nodes-(1.0))**2.0/mindeg), ind='Min')
        #         except:
        #             pass
        #     maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if maxdeg != 'undt' and nodes != 'undt':
        #         try:
        #             ingrid_obj.set('mindeg', (-((1.0))+nodes)**2.0/(4.0*(-((maxdeg))-((1.0))+nodes)), ind='Max')
        #         except:
        #             pass
        # elif (True):
        #     maxdeg = ingrid_obj.get('maxdeg', ind='Min')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if nodes != 'undt':
        #         try:
        #             ingrid_obj.set('mindeg', 0.25*(-(1.0*nodes**2.0)+2.0*nodes+3.0)/(maxdeg-(nodes)+1.0), ind='Max')
        #         except:
        #             pass
        #     mindeg = ingrid_obj.get('mindeg', ind='Max')
        #     nodes = ingrid_obj.get('nodes', ind='Max')
        #     if mindeg != 'undt' and nodes != 'undt':
        #         try:
        #             ingrid_obj.set('maxdeg', (1.0*mindeg*nodes-(1.0*mindeg)-(0.25*nodes**2.0)+0.5*nodes+0.75)/mindeg, ind='Min')
        #         except:
        #             pass
        #     maxdeg = ingrid_obj.get('maxdeg', ind='Max')
        #     mindeg = ingrid_obj.get('mindeg', ind='Min')
        #     if maxdeg != 'undt':
        #         try:
        #             ingrid_obj.set('nodes', 2.0*mindeg+2.0*(mindeg**2.0-(mindeg*maxdeg)+1.0)**(1/2)+1.0, ind='Min')
        #         except:
        #             pass
        return

class Theorem133(Theorem):
    def __init__(self):
        super(Theorem133, self).__init__(133, "null;", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self, ingrid_obj):
        return

class Theorem134(Theorem):
    def __init__(self):
        super(Theorem134, self).__init__(134, "if radius == 2 and diameter == 2 and nodes == 4 then {edges >= 4} else if radius == 2 and diameter == 2 and nodes >= 5 then {edges >= 2*nodes - 5};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","edges","nodes","radius"]
    def run(self, ingrid_obj):
        radius_Min = ingrid_obj.get('radius', ind='Min')
        radius_Max = ingrid_obj.get('radius', ind='Max')
        diameter_Min = ingrid_obj.get('diameter', ind='Min')
        diameter_Max = ingrid_obj.get('diameter', ind='Max')
        nodes_Min = ingrid_obj.get('nodes', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (radius_Max==radius_Min and (radius_Min==2.0)) and (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodes_Max==nodes_Min and (nodes_Min==4.0)):
            try:
                ingrid_obj.set('edges', 4.0, ind='Min')
            except:
                pass
        elif (radius_Max==radius_Min and (radius_Min==2.0)) and (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodes_Min>=5.0):
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('edges', 2.0*nodes-(5.0), ind='Min')
            except:
                pass
            edges = ingrid_obj.get('edges', ind='Max')
            if edges != 'undt':
                try:
                    ingrid_obj.set('nodes', 0.5*edges+2.5, ind='Max')
                except:
                    pass
        return

class Theorem135(Theorem):
    def __init__(self):
        super(Theorem135, self).__init__(135, "edges >= 2*nodeCover - numOfComponents;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","numOfComponents"]
    def run(self, ingrid_obj):
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
        if numOfComponents != 'undt':
            try:
                ingrid_obj.set('edges', 2.0*nodeCover-(1.0*numOfComponents), ind='Min')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
        if edges != 'undt' and numOfComponents != 'undt':
            try:
                ingrid_obj.set('nodeCover', 0.5*edges+0.5*numOfComponents, ind='Max')
            except:
                pass
        edges = ingrid_obj.get('edges', ind='Max')
        nodeCover = ingrid_obj.get('nodeCover', ind='Min')
        if edges != 'undt':
            try:
                ingrid_obj.set('numOfComponents', -(1.0*edges)+2.0*nodeCover, ind='Min')
            except:
                pass
        return

class Theorem136(Theorem):
    def __init__(self):
        super(Theorem136, self).__init__(136, "if maxdeg <= 2*edgeInd and odd maxdeg then {edges <= edgeInd*maxdeg + (maxdeg-1)/2 * 2*edgeInd/(maxdeg+1)};", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","edges","maxdeg"]
    def run(self, ingrid_obj):
        maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
        edgeInd_Min = ingrid_obj.get('edgeInd', ind='Min')
        maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
        if (maxdeg_Max != 'undt' and (maxdeg_Max<=2.0*edgeInd_Min)) and (odd(maxdeg_Min) and odd(maxdeg_Max)):
            edgeInd = ingrid_obj.get('edgeInd', ind='Max')
            maxdeg = ingrid_obj.get('maxdeg', ind='Max')
            if edgeInd != 'undt' and maxdeg != 'undt':
                try:
                    ingrid_obj.set('edges', 1.0*edgeInd*(1.0*maxdeg**2.0+2.0*maxdeg-(1.0))/(maxdeg+1.0), ind='Max')
                except:
                    pass
            edges = ingrid_obj.get('edges', ind='Min')
            maxdeg = ingrid_obj.get('maxdeg', ind='Min')
            try:
                ingrid_obj.set('edgeInd', 1.0*edges*(maxdeg+1.0)/(1.0*maxdeg**2.0+2.0*maxdeg-(1.0)), ind='Min')
            except:
                pass
            edgeInd = ingrid_obj.get('edgeInd', ind='Min')
            edges = ingrid_obj.get('edges', ind='Min')
            try:
                ingrid_obj.set('maxdeg', (0.5*edges-(1.0*edgeInd)+0.5*(1.0*edges**2.0+8.0*edgeInd**2.0)**(1/2))/edgeInd, ind='Min')
            except:
                pass
        return

class Theorem137(Theorem):
    def __init__(self):
        super(Theorem137, self).__init__(137, "null;", "")
    def involves(self, str_invar):
        return str_invar in ["diam","edges","maxdeg","nodes"]
    def run(self, ingrid_obj):
        return

class Theorem138(Theorem):
    def __init__(self):
        super(Theorem138, self).__init__(138, "if edges >= (1/2) * (nodes*nodes - 5*nodes + 14) then {circumference >= nodes - 1};", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","nodes"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (edges_Min>=(1.0/2.0)*(nodes_Max*nodes_Max-(5.0*nodes_Max)+14.0))):
            nodes = ingrid_obj.get('nodes', ind='Min')
            try:
                ingrid_obj.set('circumference', 1.0*nodes-(1.0), ind='Min')
            except:
                pass
            circumference = ingrid_obj.get('circumference', ind='Max')
            if circumference != 'undt':
                try:
                    ingrid_obj.set('nodes', 1.0*circumference+1.0, ind='Max')
                except:
                    pass
        return

class Theorem139(Theorem):
    def __init__(self):
        super(Theorem139, self).__init__(139, "if edges >= (1/4) * (circumference*(2*nodes - circumference)+1) then {girth == 3};", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","edges","girth","nodes"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        circumference_Max = ingrid_obj.get('circumference', ind='Max')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (circumference_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>=(1.0/4.0)*(circumference_Max*(2.0*nodes_Max-(circumference_Max))+1.0))):
            try:
                ingrid_obj.set('girth', 3.0, ind='Max')
            except:
                pass
            try:
                ingrid_obj.set('girth', 3.0, ind='Min')
            except:
                pass
        return

class Theorem140(Theorem):
    def __init__(self):
        super(Theorem140, self).__init__(140, "if edges >= 4*nodes then {crossing >= edges**3/(100*nodes**2) + 1};", "")
    def involves(self, str_invar):
        return str_invar in ["crossing","edges","nodes"]
    def run(self, ingrid_obj):
        edges_Min = ingrid_obj.get('edges', ind='Min')
        nodes_Max = ingrid_obj.get('nodes', ind='Max')
        if (nodes_Max != 'undt' and (edges_Min>=4.0*nodes_Max)):
            edges = ingrid_obj.get('edges', ind='Min')
            nodes = ingrid_obj.get('nodes', ind='Max')
            try:
                ingrid_obj.set('crossing', 1.0e-2*edges**3.0*nodes**(-(2.0))+1.0, ind='Min')
            except:
                pass
            crossing = ingrid_obj.get('crossing', ind='Max')
            nodes = ingrid_obj.get('nodes', ind='Max')
            if crossing != 'undt' and nodes != 'undt':
                try:
                    ingrid_obj.set('edges', 4.64158883361278*(nodes**2.0*(crossing-(1.0)))**0.333333333333333, ind='Max')
                except:
                    pass
            crossing = ingrid_obj.get('crossing', ind='Max')
            edges = ingrid_obj.get('edges', ind='Min')
            if crossing != 'undt':
                try:
                    ingrid_obj.set('nodes', 0.1*(edges**3.0/(crossing-(1.0)))**0.5, ind='Min')
                except:
                    pass
        return

