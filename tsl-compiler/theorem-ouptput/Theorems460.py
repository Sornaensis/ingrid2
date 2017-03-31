class Theorem441(Theorem):
    def __init__(self):
        super(Theorem441, self).__init__(441, "if maxdeg >= 6.0 and maxClique <= maxdeg-(1.0) then \n{\n    nodeCover <= (nodes*(maxdeg-(1.0))-(1.0))/maxdeg\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","maxClique","nodeCover","nodes"]
    def run(self):
        if minb("maxdeg") >= 6.0 and maxb("maxClique") <= minb("maxdeg")-(1.0):
            try:
                set("nodeCover",  (maxb("nodes")*(maxb("maxdeg")-(1.0))-(1.0))/maxb("maxdeg"), ind='Max')
            except:
                pass
            try:
                set("nodes",  (minb("maxdeg")*minb("nodeCover")+1.0)/(minb("maxdeg")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  -((maxb("nodes")+1.0)/(minb("nodeCover")-(maxb("nodes")))), ind='Min')
            except:
                pass
        
        return

class Theorem442(Theorem):
    def __init__(self):
        super(Theorem442, self).__init__(442, "if maxClique == 2.0 then \n{\n    nodeCover <= nodes*(1.0-(((2.0*edges)/nodes*log(2.0*edges/nodes)-((2.0*edges/nodes))+1.0)/(2.0*edges/nodes-(1.0))**2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodeCover","nodes","edges"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("nodeCover",  maxb("nodes")*(1.0-(((2.0*maxb("edges"))/maxb("nodes")*log(2.0*maxb("edges")/maxb("nodes"))-((2.0*maxb("edges")/maxb("nodes")))+1.0)/(2.0*maxb("edges")/maxb("nodes")-(1.0))**2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem443(Theorem):
    def __init__(self):
        super(Theorem443, self).__init__(443, "bandwidth <= nodes-((mindeg+1.0)*(numOfComponents-(1.0)))-(1.0)-((nodes-(nodeCover)-(numOfComponents)+1.0)/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["bandwidth","nodes","mindeg","numOfComponents","nodeCover"]
    def run(self):
        try:
            set("bandwidth",  maxb("nodes")-((minb("mindeg")+1.0)*(maxb("numOfComponents")-(1.0)))-(1.0)-((maxb("nodes")-(maxb("nodeCover"))-(maxb("numOfComponents"))+1.0)/2.0), ind='Max')
        except:
            pass
        try:
            set("nodes",  2.0*minb("bandwidth")+2.0*minb("mindeg")*minb("numOfComponents")-(2.0*minb("mindeg"))-(maxb("nodeCover"))+minb("numOfComponents")+1.0, ind='Min')
        except:
            pass
        try:
            set("mindeg",  (-(2.0*minb("bandwidth"))+maxb("nodeCover")+maxb("nodes")-(minb("numOfComponents"))-(1.0))/(2.0*(minb("numOfComponents")-(1.0))), ind='Max')
        except:
            pass
        try:
            set("numOfComponents",  (-(2.0*maxb("bandwidth"))+2.0*minb("mindeg")+minb("nodeCover")+minb("nodes")-(1.0))/(2.0*minb("mindeg")+1.0), ind='Min')
        except:
            pass
        try:
            set("nodeCover",  2.0*minb("bandwidth")+2.0*minb("mindeg")*minb("numOfComponents")-(2.0*minb("mindeg"))-(maxb("nodes"))+minb("numOfComponents")+1.0, ind='Min')
        except:
            pass
        return

class Theorem444(Theorem):
    def __init__(self):
        super(Theorem444, self).__init__(444, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem445(Theorem):
    def __init__(self):
        super(Theorem445, self).__init__(445, "let m = floor((nodes-(chromaticNum))/(nodes-(nodeCover)-(1.0)));edges >= m*(nodes-(chromaticNum))+chromaticNum*(chromaticNum-(1.0))/2.0-((nodes-(nodeCover)-(1.0))*m*(m+1.0)/2.0);", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","chromaticNum","nodeCover"]
    def run(self):
        try:
            set("edges",  floor((maxb("nodes")-(maxb("chromaticNum")))/(maxb("nodes")-(maxb("nodeCover"))-(1.0)))*(maxb("nodes")-(maxb("chromaticNum")))+maxb("chromaticNum")*(maxb("chromaticNum")-(1.0))/2.0-((maxb("nodes")-(maxb("nodeCover"))-(1.0))*floor((maxb("nodes")-(maxb("chromaticNum")))/(maxb("nodes")-(maxb("nodeCover"))-(1.0)))*(floor((maxb("nodes")-(maxb("chromaticNum")))/(maxb("nodes")-(maxb("nodeCover"))-(1.0)))+1.0)/2.0), ind='Min')
        except:
            pass
        try:
            set("nodes",  (floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))**2.0*maxb("nodeCover")+floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))**2.0-(2.0*floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))*minb("chromaticNum"))+floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))*maxb("nodeCover")+floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))+minb("chromaticNum")**2.0-(minb("chromaticNum"))-(2.0*minb("edges")))/(floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))*(floor((minb("nodes")-(minb("chromaticNum")))/(minb("nodes")-(maxb("nodeCover"))-(1.0)))-(1.0))), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))+sqrt(-(4.0*floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))**2.0*minb("nodeCover"))+4.0*floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))**2.0*maxb("nodes")-(4.0*floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))*minb("nodeCover"))-(4.0*floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))*maxb("nodes"))+8.0*maxb("edges")+1.0)/2.0+1.0/2.0, ind='Max')
        except:
            pass
        try:
            set("nodeCover",  (floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))**2.0*maxb("nodes")-(floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))**2.0)+2.0*floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))*minb("chromaticNum")-(floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))*maxb("nodes"))-(floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0))))-(minb("chromaticNum")**2.0)+minb("chromaticNum")+2.0*maxb("edges"))/(floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))*(floor((maxb("nodes")-(minb("chromaticNum")))/(maxb("nodes")-(minb("nodeCover"))-(1.0)))+1.0)), ind='Max')
        except:
            pass
        return

class Theorem446(Theorem):
    def __init__(self):
        super(Theorem446, self).__init__(446, "if maxClique <= 2.0 and maxdeg <= 3.0 then \n{\n    edges >= 14.0*nodeCover-(15.0*nodes/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 3.0:
            try:
                set("edges",  14.0*minb("nodeCover")-(15.0*maxb("nodes")/2.0), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("edges")/14.0+15.0*maxb("nodes")/28.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(2.0*maxb("edges")/15.0)+28.0*minb("nodeCover")/15.0, ind='Min')
            except:
                pass
        
        return

class Theorem447(Theorem):
    def __init__(self):
        super(Theorem447, self).__init__(447, "if maxClique <= 2.0 and maxdeg <= 2.0 then \n{\n    edges >= 15.0*nodeCover-(8.0*nodes)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","maxdeg","edges","nodeCover","nodes"]
    def run(self):
        if maxb("maxClique") <= 2.0 and maxb("maxdeg") <= 2.0:
            try:
                set("edges",  15.0*minb("nodeCover")-(8.0*maxb("nodes")), ind='Min')
            except:
                pass
            try:
                set("nodeCover",  maxb("edges")/15.0+8.0*maxb("nodes")/15.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  -(maxb("edges")/8.0)+15.0*minb("nodeCover")/8.0, ind='Min')
            except:
                pass
        
        return

class Theorem448(Theorem):
    def __init__(self):
        super(Theorem448, self).__init__(448, "edges <= ((nodes-(nodeCliqueCover))*(nodeCliqueCover+maxdeg-(1.0))+mindeg)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","nodeCliqueCover","maxdeg","mindeg"]
    def run(self):
        try:
            set("edges",  ((maxb("nodes")-(maxb("nodeCliqueCover")))*(maxb("nodeCliqueCover")+maxb("maxdeg")-(1.0))+maxb("mindeg"))/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  (2.0*minb("edges")+minb("maxdeg")*minb("nodeCliqueCover")-(maxb("mindeg"))+minb("nodeCliqueCover")**2.0-(minb("nodeCliqueCover")))/(minb("maxdeg")+minb("nodeCliqueCover")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("nodeCliqueCover",  -(minb("maxdeg")/2.0)+minb("nodes")/2.0+sqrt(-(8.0*maxb("edges"))+minb("maxdeg")**2.0+2.0*minb("maxdeg")*minb("nodes")-(2.0*minb("maxdeg"))+4.0*minb("mindeg")+minb("nodes")**2.0-(2.0*minb("nodes"))+1.0)/2.0+1.0/2.0, ind='Min')
        except:
            pass
        try:
            set("maxdeg",  (-(2.0*maxb("edges"))+minb("mindeg")-(maxb("nodeCliqueCover")**2.0)+maxb("nodeCliqueCover")*minb("nodes")+maxb("nodeCliqueCover")-(minb("nodes")))/(maxb("nodeCliqueCover")-(minb("nodes"))), ind='Min')
        except:
            pass
        try:
            set("mindeg",  2.0*minb("edges")+minb("maxdeg")*minb("nodeCliqueCover")-(minb("maxdeg")*minb("nodes"))+minb("nodeCliqueCover")**2.0-(minb("nodeCliqueCover")*minb("nodes"))-(minb("nodeCliqueCover"))+minb("nodes"), ind='Min')
        except:
            pass
        return

class Theorem449(Theorem):
    def __init__(self):
        super(Theorem449, self).__init__(449, "if nodeInd == 2.0 and mindeg >= nodes-(5.0) then \n{\n    edges <= nodes*(nodes-(13.0))/2.0+13.0*maxClique\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","edges","maxClique"]
    def run(self):
        if minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0 and minb("mindeg") >= maxb("nodes")-(5.0):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(13.0))/2.0+13.0*maxb("maxClique"), ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(8.0*minb("edges")-(104.0*maxb("maxClique"))+169.0)/2.0+13.0/2.0, ind='Min')
            except:
                pass
            try:
                set("maxClique",  minb("edges")/13.0-(maxb("nodes")**2.0/26.0)+maxb("nodes")/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem450(Theorem):
    def __init__(self):
        super(Theorem450, self).__init__(450, "if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes-(mindeg)-(1.0) and mindeg <= nodes-(10.0) then \n{\n    nodes <= 2.0*mindeg+2.0\n\n} else if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes-(mindeg)-(1.0) and mindeg >= nodes-(10.0) then \n{\n    nodes <= 2.0*mindeg+3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes","mindeg"]
    def run(self):
        if maxb("nodeInd") < minb("nodeCliqueCover") and minb("nodeCliqueCover") >= maxb("nodes")-(minb("mindeg"))-(1.0) and maxb("nodeCliqueCover") <= minb("nodes")-(maxb("mindeg"))-(1.0) and maxb("mindeg") <= minb("nodes")-(10.0):
            try:
                set("nodes",  2.0*maxb("mindeg")+2.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("nodes")/2.0-(1.0), ind='Min')
            except:
                pass
        
        elif maxb("nodeInd") < minb("nodeCliqueCover") and minb("nodeCliqueCover") >= maxb("nodes")-(minb("mindeg"))-(1.0) and maxb("nodeCliqueCover") <= minb("nodes")-(maxb("mindeg"))-(1.0) and minb("mindeg") >= maxb("nodes")-(10.0):
            try:
                set("nodes",  2.0*maxb("mindeg")+3.0, ind='Max')
            except:
                pass
            try:
                set("mindeg",  minb("nodes")/2.0-(3.0/2.0), ind='Min')
            except:
                pass
        
        return

class Theorem451(Theorem):
    def __init__(self):
        super(Theorem451, self).__init__(451, "if mindeg <= min(nodes-(7.0), nodes-(nodeInd)-(2.0)) then \n{\n    mindeg <= ((nodes-(1.0))*(maxClique-(1.0))-(2.0))/maxClique\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","nodes","nodeInd","maxClique"]
    def run(self):
        if maxb("mindeg") <= min(minb("nodes")-(7.0), minb("nodes")-(maxb("nodeInd"))-(2.0)):
            try:
                set("mindeg",  ((maxb("nodes")-(1.0))*(maxb("maxClique")-(1.0))-(2.0))/maxb("maxClique"), ind='Max')
            except:
                pass
            try:
                set("nodes",  (minb("maxClique")*minb("mindeg")+minb("maxClique")+1.0)/(minb("maxClique")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("maxClique",  -((maxb("nodes")+1.0)/(minb("mindeg")-(maxb("nodes"))+1.0)), ind='Min')
            except:
                pass
        
        return

class Theorem452(Theorem):
    def __init__(self):
        super(Theorem452, self).__init__(452, ";", "")
    def involves(self, str_invar):
        return str_invar in []
    def run(self):
        return

class Theorem453(Theorem):
    def __init__(self):
        super(Theorem453, self).__init__(453, "edges <= nodes*(nodes-(1.0))/2.0-(floor((nodes-(nodeConnec))/(maxClique-(1.0)))*(nodes-(nodeConnec)))-(nodeConnec*(nodeConnec-(1.0))/2.0)+(maxClique-(1.0))*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*(floor((nodes-(nodeConnec))/(maxClique-(1.0)))+1.0)/2.0;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodes","nodeConnec","maxClique"]
    def run(self):
        try:
            set("edges",  minb("nodes")*(minb("nodes")-(1.0))/2.0-(floor((minb("nodes")-(minb("nodeConnec")))/(maxb("maxClique")-(1.0)))*(minb("nodes")-(minb("nodeConnec"))))-(minb("nodeConnec")*(minb("nodeConnec")-(1.0))/2.0)+(maxb("maxClique")-(1.0))*floor((minb("nodes")-(minb("nodeConnec")))/(maxb("maxClique")-(1.0)))*(floor((minb("nodes")-(minb("nodeConnec")))/(maxb("maxClique")-(1.0)))+1.0)/2.0, ind='Max')
        except:
            pass
        try:
            set("nodes",  floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))+sqrt(-(4.0*floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))**2.0*maxb("maxClique"))+8.0*floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))**2.0-(4.0*floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))*maxb("maxClique"))-(8.0*floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))*maxb("nodeConnec"))+8.0*floor((minb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))+8.0*minb("edges")+4.0*maxb("nodeConnec")**2.0-(4.0*maxb("nodeConnec"))+1.0)/2.0+1.0/2.0, ind='Min')
        except:
            pass
        try:
            set("nodeConnec",  floor((maxb("nodes")-(minb("nodeConnec")))/(minb("maxClique")-(1.0)))+sqrt(4.0*floor((maxb("nodes")-(minb("nodeConnec")))/(minb("maxClique")-(1.0)))**2.0*minb("maxClique")+4.0*floor((maxb("nodes")-(minb("nodeConnec")))/(minb("maxClique")-(1.0)))*minb("maxClique")-(8.0*floor((maxb("nodes")-(minb("nodeConnec")))/(minb("maxClique")-(1.0)))*maxb("nodes"))-(8.0*minb("edges"))+4.0*maxb("nodes")**2.0-(4.0*maxb("nodes"))+1.0)/2.0+1.0/2.0, ind='Max')
        except:
            pass
        try:
            set("maxClique",  (floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))**2.0-(2.0*floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))*maxb("nodeConnec"))+2.0*floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))*maxb("nodes")+floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))+2.0*minb("edges")+maxb("nodeConnec")**2.0-(maxb("nodeConnec"))-(maxb("nodes")**2.0)+maxb("nodes"))/(floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))*(floor((maxb("nodes")-(maxb("nodeConnec")))/(maxb("maxClique")-(1.0)))+1.0)), ind='Min')
        except:
            pass
        return

class Theorem454(Theorem):
    def __init__(self):
        super(Theorem454, self).__init__(454, "if nodeInd <= 2.0 and mindeg >= nodes-(4.0) then \n{\n    edges <= nodes*(nodes-(14.0))/2.0+14.0*maxClique\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","edges","maxClique"]
    def run(self):
        if maxb("nodeInd") <= 2.0 and minb("mindeg") >= maxb("nodes")-(4.0):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(14.0))/2.0+14.0*maxb("maxClique"), ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(2.0*minb("edges")-(28.0*maxb("maxClique"))+49.0)+7.0, ind='Min')
            except:
                pass
            try:
                set("maxClique",  minb("edges")/14.0-(maxb("nodes")**2.0/28.0)+maxb("nodes")/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem455(Theorem):
    def __init__(self):
        super(Theorem455, self).__init__(455, "if nodeInd <= 2.0 and mindeg >= nodes-(3.0) then \n{\n    edges <= nodes*(nodes-(15.0))/2.0+15.0*maxClique\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","mindeg","nodes","edges","maxClique"]
    def run(self):
        if maxb("nodeInd") <= 2.0 and minb("mindeg") >= maxb("nodes")-(3.0):
            try:
                set("edges",  maxb("nodes")*(maxb("nodes")-(15.0))/2.0+15.0*maxb("maxClique"), ind='Max')
            except:
                pass
            try:
                set("nodes",  sqrt(8.0*minb("edges")-(120.0*maxb("maxClique"))+225.0)/2.0+15.0/2.0, ind='Min')
            except:
                pass
            try:
                set("maxClique",  minb("edges")/15.0-(maxb("nodes")**2.0/30.0)+maxb("nodes")/2.0, ind='Min')
            except:
                pass
        
        return

class Theorem456(Theorem):
    def __init__(self):
        super(Theorem456, self).__init__(456, "if maxClique == 2.0 then \n{\n    chromaticNum <= 1.0+3.0*(nodeCover+12.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodeCover"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("chromaticNum",  1.0+3.0*(maxb("nodeCover")+12.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodeCover",  16.0*minb("chromaticNum")/3.0-(52.0/3.0), ind='Min')
            except:
                pass
        
        return

class Theorem457(Theorem):
    def __init__(self):
        super(Theorem457, self).__init__(457, "if maxClique == 2.0 then \n{\n    chromaticNum <= (3.0*nodes-(3.0*nodeInd)+52.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","chromaticNum","nodes","nodeInd"]
    def run(self):
        if minb("maxClique") >= 2.0 and maxb("maxClique") <= 2.0:
            try:
                set("chromaticNum",  (3.0*maxb("nodes")-(3.0*minb("nodeInd"))+52.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  16.0*minb("chromaticNum")/3.0+minb("nodeInd")-(52.0/3.0), ind='Min')
            except:
                pass
            try:
                set("nodeInd",  -(16.0*minb("chromaticNum")/3.0)+maxb("nodes")+52.0/3.0, ind='Max')
            except:
                pass
        
        return

class Theorem458(Theorem):
    def __init__(self):
        super(Theorem458, self).__init__(458, "if nodeInd == 2.0 then \n{\n    nodeCliqueCover <= (3.0*nodes-(3.0*maxClique)+52.0)/16.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover","nodes","maxClique"]
    def run(self):
        if minb("nodeInd") >= 2.0 and maxb("nodeInd") <= 2.0:
            try:
                set("nodeCliqueCover",  (3.0*maxb("nodes")-(3.0*minb("maxClique"))+52.0)/16.0, ind='Max')
            except:
                pass
            try:
                set("nodes",  minb("maxClique")+16.0*minb("nodeCliqueCover")/3.0-(52.0/3.0), ind='Min')
            except:
                pass
            try:
                set("maxClique",  -(16.0*minb("nodeCliqueCover")/3.0)+maxb("nodes")+52.0/3.0, ind='Max')
            except:
                pass
        
        return

