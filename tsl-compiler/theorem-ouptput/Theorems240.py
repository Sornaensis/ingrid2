class Theorem221(Theorem):
    def __init__(self):
        super(Theorem221, self).__init__(221, "chromaticNum <= nodeCover+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","nodeCover"]
    def run(self):
        try:
            set("chromaticNum",  maxb("nodeCover")+1.0, ind='Max')
        except:
            pass
        try:
            set("nodeCover",  minb("chromaticNum")-(1.0), ind='Min')
        except:
            pass
        return

class Theorem222(Theorem):
    def __init__(self):
        super(Theorem222, self).__init__(222, "edgeInd <= nodeCover;", "")
    def involves(self, str_invar):
        return str_invar in ["edgeInd","nodeCover"]
    def run(self):
        try:
            set("edgeInd",  maxb("nodeCover"), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  minb("edgeInd"), ind='Min')
        except:
            pass
        return

class Theorem223(Theorem):
    def __init__(self):
        super(Theorem223, self).__init__(223, "nodeInd <= nodeCliqueCover;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","nodeCliqueCover"]
    def run(self):
        try:
            set("nodeInd",  maxb("nodeCliqueCover"), ind='Max')
        except:
            pass
        try:
            set("nodeCliqueCover",  minb("nodeInd"), ind='Min')
        except:
            pass
        return

class Theorem224(Theorem):
    def __init__(self):
        super(Theorem224, self).__init__(224, "nodeCliqueCover <= edgeCliqueCover;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCliqueCover","edgeCliqueCover"]
    def run(self):
        try:
            set("nodeCliqueCover",  maxb("edgeCliqueCover"), ind='Max')
        except:
            pass
        try:
            set("edgeCliqueCover",  minb("nodeCliqueCover"), ind='Min')
        except:
            pass
        return

class Theorem225(Theorem):
    def __init__(self):
        super(Theorem225, self).__init__(225, "radius <= diam;", "")
    def involves(self, str_invar):
        return str_invar in ["radius","diam"]
    def run(self):
        try:
            set("radius",  maxb("diam"), ind='Max')
        except:
            pass
        try:
            set("diam",  minb("radius"), ind='Min')
        except:
            pass
        return

class Theorem226(Theorem):
    def __init__(self):
        super(Theorem226, self).__init__(226, "nodeConnec <= edgeConnec;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeConnec","edgeConnec"]
    def run(self):
        try:
            set("nodeConnec",  maxb("edgeConnec"), ind='Max')
        except:
            pass
        try:
            set("edgeConnec",  minb("nodeConnec"), ind='Min')
        except:
            pass
        return

class Theorem227(Theorem):
    def __init__(self):
        super(Theorem227, self).__init__(227, "girth <= circumference;", "")
    def involves(self, str_invar):
        return str_invar in ["girth","circumference"]
    def run(self):
        try:
            set("girth",  maxb("circumference"), ind='Max')
        except:
            pass
        try:
            set("circumference",  minb("girth"), ind='Min')
        except:
            pass
        return

class Theorem228(Theorem):
    def __init__(self):
        super(Theorem228, self).__init__(228, "chromaticNum <= circumference;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","circumference"]
    def run(self):
        try:
            set("chromaticNum",  maxb("circumference"), ind='Max')
        except:
            pass
        try:
            set("circumference",  minb("chromaticNum"), ind='Min')
        except:
            pass
        return

class Theorem229(Theorem):
    def __init__(self):
        super(Theorem229, self).__init__(229, "genus <= crossing;", "")
    def involves(self, str_invar):
        return str_invar in ["genus","crossing"]
    def run(self):
        try:
            set("genus",  maxb("crossing"), ind='Max')
        except:
            pass
        try:
            set("crossing",  minb("genus"), ind='Min')
        except:
            pass
        return

class Theorem230(Theorem):
    def __init__(self):
        super(Theorem230, self).__init__(230, "mindeg <= circumference-(1.0);", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","circumference"]
    def run(self):
        try:
            set("mindeg",  maxb("circumference")-(1.0), ind='Max')
        except:
            pass
        try:
            set("circumference",  minb("mindeg")+1.0, ind='Min')
        except:
            pass
        return

class Theorem231(Theorem):
    def __init__(self):
        super(Theorem231, self).__init__(231, "chromaticNum <= bandwidth+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","bandwidth"]
    def run(self):
        try:
            set("chromaticNum",  maxb("bandwidth")+1.0, ind='Max')
        except:
            pass
        try:
            set("bandwidth",  minb("chromaticNum")-(1.0), ind='Min')
        except:
            pass
        return

class Theorem232(Theorem):
    def __init__(self):
        super(Theorem232, self).__init__(232, "mindeg <= bandwidth;", "")
    def involves(self, str_invar):
        return str_invar in ["mindeg","bandwidth"]
    def run(self):
        try:
            set("mindeg",  maxb("bandwidth"), ind='Max')
        except:
            pass
        try:
            set("bandwidth",  minb("mindeg"), ind='Min')
        except:
            pass
        return

class Theorem233(Theorem):
    def __init__(self):
        super(Theorem233, self).__init__(233, "nodes <= nodeInd*chromaticNum;", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeInd","chromaticNum"]
    def run(self):
        try:
            set("nodes",  maxb("nodeInd")*maxb("chromaticNum"), ind='Max')
        except:
            pass
        try:
            set("nodeInd",  minb("nodes")/maxb("chromaticNum"), ind='Min')
        except:
            pass
        try:
            set("chromaticNum",  minb("nodes")/maxb("nodeInd"), ind='Min')
        except:
            pass
        return

class Theorem234(Theorem):
    def __init__(self):
        super(Theorem234, self).__init__(234, "nodes <= nodeCliqueCover*maxClique;", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCliqueCover","maxClique"]
    def run(self):
        try:
            set("nodes",  maxb("nodeCliqueCover")*maxb("maxClique"), ind='Max')
        except:
            pass
        try:
            set("nodeCliqueCover",  minb("nodes")/maxb("maxClique"), ind='Min')
        except:
            pass
        try:
            set("maxClique",  minb("nodes")/maxb("nodeCliqueCover"), ind='Min')
        except:
            pass
        return

class Theorem235(Theorem):
    def __init__(self):
        super(Theorem235, self).__init__(235, "edges <= edgeChromatic*edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","edgeChromatic","edgeInd"]
    def run(self):
        try:
            set("edges",  maxb("edgeChromatic")*maxb("edgeInd"), ind='Max')
        except:
            pass
        try:
            set("edgeChromatic",  minb("edges")/maxb("edgeInd"), ind='Min')
        except:
            pass
        try:
            set("edgeInd",  minb("edges")/maxb("edgeChromatic"), ind='Min')
        except:
            pass
        return

class Theorem236(Theorem):
    def __init__(self):
        super(Theorem236, self).__init__(236, "edges <= nodeCover*maxdeg;", "")
    def involves(self, str_invar):
        return str_invar in ["edges","nodeCover","maxdeg"]
    def run(self):
        try:
            set("edges",  maxb("nodeCover")*maxb("maxdeg"), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  minb("edges")/maxb("maxdeg"), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  minb("edges")/maxb("nodeCover"), ind='Min')
        except:
            pass
        return

class Theorem237(Theorem):
    def __init__(self):
        super(Theorem237, self).__init__(237, "nodeCover <= bandwidth*nodeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["nodeCover","bandwidth","nodeInd"]
    def run(self):
        try:
            set("nodeCover",  maxb("bandwidth")*maxb("nodeInd"), ind='Max')
        except:
            pass
        try:
            set("bandwidth",  minb("nodeCover")/maxb("nodeInd"), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  minb("nodeCover")/maxb("bandwidth"), ind='Min')
        except:
            pass
        return

class Theorem238(Theorem):
    def __init__(self):
        super(Theorem238, self).__init__(238, "chromaticNum <= spectralRadius+1.0;", "")
    def involves(self, str_invar):
        return str_invar in ["chromaticNum","spectralRadius"]
    def run(self):
        try:
            set("chromaticNum",  maxb("spectralRadius")+1.0, ind='Max')
        except:
            pass
        try:
            set("spectralRadius",  minb("chromaticNum")-(1.0), ind='Min')
        except:
            pass
        return

class Theorem239(Theorem):
    def __init__(self):
        super(Theorem239, self).__init__(239, "nodes == nodeCover+nodeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeCover","nodeInd"]
    def run(self):
        try:
            set("nodes",  minb("nodeCover")+minb("nodeInd"), ind='Min')
        except:
            pass
        try:
            set("nodeCover",  -(minb("nodeInd"))+maxb("nodes"), ind='Max')
        except:
            pass
        try:
            set("nodeInd",  -(minb("nodeCover"))+maxb("nodes"), ind='Max')
        except:
            pass
        try:
            set("nodes",  maxb("nodeCover")+maxb("nodeInd"), ind='Max')
        except:
            pass
        try:
            set("nodeCover",  -(maxb("nodeInd"))+minb("nodes"), ind='Min')
        except:
            pass
        try:
            set("nodeInd",  -(maxb("nodeCover"))+minb("nodes"), ind='Min')
        except:
            pass
        return

class Theorem240(Theorem):
    def __init__(self):
        super(Theorem240, self).__init__(240, "nodes == edgeCover+edgeInd;", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","edgeCover","edgeInd"]
    def run(self):
        try:
            set("nodes",  minb("edgeCover")+minb("edgeInd"), ind='Min')
        except:
            pass
        try:
            set("edgeCover",  -(minb("edgeInd"))+maxb("nodes"), ind='Max')
        except:
            pass
        try:
            set("edgeInd",  -(minb("edgeCover"))+maxb("nodes"), ind='Max')
        except:
            pass
        try:
            set("nodes",  maxb("edgeCover")+maxb("edgeInd"), ind='Max')
        except:
            pass
        try:
            set("edgeCover",  -(maxb("edgeInd"))+minb("nodes"), ind='Min')
        except:
            pass
        try:
            set("edgeInd",  -(maxb("edgeCover"))+minb("nodes"), ind='Min')
        except:
            pass
        return

