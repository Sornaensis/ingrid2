class Theorem261(Theorem):
    def __init__(self):
        super(Theorem261, self).__init__(261, "if genus <= 2.0 and girth >= 5.0 then \n{\n    chromaticNum <= 4.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","chromaticNum"]
    def run(self):
        if maxb("genus") <= 2.0 and minb("girth") >= 5.0:
            try:
                set("chromaticNum",  4.0, ind='Max')
            except:
                pass
        
        return

class Theorem262(Theorem):
    def __init__(self):
        super(Theorem262, self).__init__(262, "if (genus == 0.0 and girth >= 4.0) or (genus <= 1.0 and girth >= 6.0) or (genus <= 2.0 and girth >= 7.0) or (girth >= 9.0) then \n{\n    chromaticNum <= 3.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["genus","girth","chromaticNum"]
    def run(self):
        if (minb("genus") >= 0.0 and maxb("genus") <= 0.0 and minb("girth") >= 4.0) or (maxb("genus") <= 1.0 and minb("girth") >= 6.0) or (maxb("genus") <= 2.0 and minb("girth") >= 7.0) or (minb("girth") >= 9.0):
            try:
                set("chromaticNum",  3.0, ind='Max')
            except:
                pass
        
        return

class Theorem263(Theorem):
    def __init__(self):
        super(Theorem263, self).__init__(263, "maxdeg >= (nodes-(1.0))**(1.0/radius);", "")
    def involves(self, str_invar):
        return str_invar in ["maxdeg","nodes","radius"]
    def run(self):
        try:
            set("maxdeg",  (minb("nodes")-(1.0))**(1.0/maxb("radius")), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("maxdeg")**maxb("radius")+1.0, ind='Max')
        except:
            pass
        return

class Theorem264(Theorem):
    def __init__(self):
        super(Theorem264, self).__init__(264, "if connected then \n{\n    diameter <= 3.0*domination-(1.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","diameter","domination"]
    def run(self):
        if get("connected") == True :
            try:
                set("diameter",  3.0*maxb("domination")-(1.0), ind='Max')
            except:
                pass
            try:
                set("domination",  minb("diameter")/3.0+1.0/3.0, ind='Min')
            except:
                pass
        
        return

class Theorem265(Theorem):
    def __init__(self):
        super(Theorem265, self).__init__(265, "if connected and maxdeg >= 3.0 then \n{\n    nodes <= 1.0+mindeg*((maxdeg-(1.0))**diameter-(1.0))/(maxdeg-(2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","nodes","mindeg","diameter"]
    def run(self):
        if get("connected") == True  and minb("maxdeg") >= 3.0:
            try:
                set("nodes",  1.0+maxb("mindeg")*((maxb("maxdeg")-(1.0))**maxb("diameter")-(1.0))/(maxb("maxdeg")-(2.0)), ind='Max')
            except:
                pass
            try:
                set("mindeg",  (minb("maxdeg")*minb("nodes")-(minb("maxdeg"))-(2.0*minb("nodes"))+2.0)/((minb("maxdeg")-(1.0))**maxb("diameter")-(1.0)), ind='Min')
            except:
                pass
        
        return

class Theorem266(Theorem):
    def __init__(self):
        super(Theorem266, self).__init__(266, "if diameter >= 2.0 and maxdeg >= 3.0 then \n{\n    maxdeg >= ceil((nodes-(1.0))/mindeg)**(1.0/(diameter-(1.0)))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","maxdeg","nodes","mindeg"]
    def run(self):
        if minb("diameter") >= 2.0 and minb("maxdeg") >= 3.0:
            try:
                set("maxdeg",  ceil((minb("nodes")-(1.0))/maxb("mindeg"))**(1.0/(maxb("diameter")-(1.0))), ind='Min')
            except:
                pass
        
        return

class Theorem267(Theorem):
    def __init__(self):
        super(Theorem267, self).__init__(267, "if diameter == radius and radius == 2.0 then \n{\n    mindeg >= 2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","radius","mindeg"]
    def run(self):
        if minb("diameter") >= maxb("radius") and maxb("diameter") <= minb("radius") and minb("radius") >= 2.0 and maxb("radius") <= 2.0:
            try:
                set("mindeg",  2.0, ind='Min')
            except:
                pass
        
        return

class Theorem268(Theorem):
    def __init__(self):
        super(Theorem268, self).__init__(268, "if not forest then \n{\n    bandwidth >= (girth-(1.0))*(arboricity-(2.0))+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","bandwidth","girth","arboricity"]
    def run(self):
        if get("forest") == False :
            try:
                set("bandwidth",  (minb("girth")-(1.0))*(minb("arboricity")-(2.0))+2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (maxb("arboricity")+maxb("bandwidth")-(4.0))/(maxb("arboricity")-(2.0)), ind='Max')
            except:
                pass
            try:
                set("arboricity",  (maxb("bandwidth")+2.0*maxb("girth")-(4.0))/(maxb("girth")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem269(Theorem):
    def __init__(self):
        super(Theorem269, self).__init__(269, "if not forest then \n{\n    bandwidth >= (girth-(1.0))*nodes/(2.0*nodeInd)-(girth)+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","bandwidth","girth","nodes","nodeInd"]
    def run(self):
        if get("forest") == False :
            try:
                set("bandwidth",  (minb("girth")-(1.0))*minb("nodes")/(2.0*maxb("nodeInd"))-(minb("girth"))+2.0, ind='Min')
            except:
                pass
            try:
                set("girth",  (-(2.0*minb("bandwidth")*maxb("nodeInd"))+4.0*maxb("nodeInd")-(maxb("nodes")))/(2.0*maxb("nodeInd")-(maxb("nodes"))), ind='Max')
            except:
                pass
            try:
                set("nodes",  2.0*maxb("nodeInd")*(maxb("bandwidth")+maxb("girth")-(2.0))/(maxb("girth")-(1.0)), ind='Max')
            except:
                pass
            try:
                set("nodeInd",  minb("nodes")*(minb("girth")-(1.0))/(2.0*(maxb("bandwidth")+minb("girth")-(2.0))), ind='Min')
            except:
                pass
        
        return

class Theorem270(Theorem):
    def __init__(self):
        super(Theorem270, self).__init__(270, "if not forest then \n{\n    domination <= nodes-(floor(2.0*circumference/3.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","domination","nodes","circumference"]
    def run(self):
        if get("forest") == False :
            try:
                set("domination",  maxb("nodes")-(floor(2.0*minb("circumference")/3.0)), ind='Max')
            except:
                pass
            try:
                set("nodes",  floor(2.0*minb("circumference")/3.0)+minb("domination"), ind='Min')
            except:
                pass
        
        return

class Theorem271(Theorem):
    def __init__(self):
        super(Theorem271, self).__init__(271, "let k = ceil(nodes/mindeg);circumference >= floor(nodes/(k-(1.0)));", "")
    def involves(self, str_invar):
        return str_invar in ["circumference","nodes","mindeg"]
    def run(self):
        try:
            set("circumference",  floor(minb("nodes")/(ceil(minb("nodes")/minb("mindeg"))-(1.0))), ind='Min')
        except:
            pass
        return

class Theorem272(Theorem):
    def __init__(self):
        super(Theorem272, self).__init__(272, "if diameter == 2.0 then \n{\n    domination <= nodeConnec\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["diameter","domination","nodeConnec"]
    def run(self):
        if minb("diameter") >= 2.0 and maxb("diameter") <= 2.0:
            try:
                set("domination",  maxb("nodeConnec"), ind='Max')
            except:
                pass
            try:
                set("nodeConnec",  minb("domination"), ind='Min')
            except:
                pass
        
        return

class Theorem273(Theorem):
    def __init__(self):
        super(Theorem273, self).__init__(273, "if tree then \n{\n    radius == floor((diameter+1.0)/2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["tree","radius","diameter"]
    def run(self):
        if get("tree") == True :
            try:
                set("radius",  floor((minb("diameter")+1.0)/2.0), ind='Min')
            except:
                pass
            
            try:
                set("radius",  floor((maxb("diameter")+1.0)/2.0), ind='Max')
            except:
                pass
        
        return

class Theorem274(Theorem):
    def __init__(self):
        super(Theorem274, self).__init__(274, "if Hamiltonian then \n{\n    nodes >= (maxdeg-(1.0))*(girth-(2.0))+2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["Hamiltonian","nodes","maxdeg","girth"]
    def run(self):
        if get("Hamiltonian") == True :
            try:
                set("nodes",  (minb("maxdeg")-(1.0))*(minb("girth")-(2.0))+2.0, ind='Min')
            except:
                pass
            try:
                set("maxdeg",  (maxb("girth")+maxb("nodes")-(4.0))/(maxb("girth")-(2.0)), ind='Max')
            except:
                pass
            try:
                set("girth",  (2.0*maxb("maxdeg")+maxb("nodes")-(4.0))/(maxb("maxdeg")-(1.0)), ind='Max')
            except:
                pass
        
        return

class Theorem275(Theorem):
    def __init__(self):
        super(Theorem275, self).__init__(275, "nodeInd >= maxdeg/(chromaticNum-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["nodeInd","maxdeg","chromaticNum"]
    def run(self):
        try:
            set("nodeInd",  minb("maxdeg")/(maxb("chromaticNum")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("maxdeg",  maxb("nodeInd")*(maxb("chromaticNum")-(1.0)), ind='Max')
        except:
            pass
        try:
            set("chromaticNum",  (minb("maxdeg")+minb("nodeInd"))/minb("nodeInd"), ind='Min')
        except:
            pass
        return

class Theorem276(Theorem):
    def __init__(self):
        super(Theorem276, self).__init__(276, "maxClique >= (nodes-(mindeg)-(1.0))/(nodeCliqueCover-(1.0));", "")
    def involves(self, str_invar):
        return str_invar in ["maxClique","nodes","mindeg","nodeCliqueCover"]
    def run(self):
        try:
            set("maxClique",  (minb("nodes")-(maxb("mindeg"))-(1.0))/(maxb("nodeCliqueCover")-(1.0)), ind='Min')
        except:
            pass
        try:
            set("nodes",  maxb("maxClique")*maxb("nodeCliqueCover")-(maxb("maxClique"))+maxb("mindeg")+1.0, ind='Max')
        except:
            pass
        try:
            set("mindeg",  -(minb("maxClique")*maxb("nodeCliqueCover"))+minb("maxClique")+minb("nodes")-(1.0), ind='Min')
        except:
            pass
        try:
            set("nodeCliqueCover",  (minb("maxClique")-(maxb("mindeg"))+minb("nodes")-(1.0))/minb("maxClique"), ind='Min')
        except:
            pass
        return

class Theorem277(Theorem):
    def __init__(self):
        super(Theorem277, self).__init__(277, "if nodes >= 3.0 and nodeConnec <= 1.0 then \n{\n    edgeConnec <= maxdeg/2.0\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["nodes","nodeConnec","edgeConnec","maxdeg"]
    def run(self):
        if minb("nodes") >= 3.0 and maxb("nodeConnec") <= 1.0:
            try:
                set("edgeConnec",  maxb("maxdeg")/2.0, ind='Max')
            except:
                pass
            try:
                set("maxdeg",  2.0*minb("edgeConnec"), ind='Min')
            except:
                pass
        
        return

class Theorem278(Theorem):
    def __init__(self):
        super(Theorem278, self).__init__(278, "if connected and maxdeg >= 3.0 then \n{\n    nodes <= 1.0+maxdeg*((maxdeg-(1.0))**radius-(1.0))/(maxdeg-(2.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","maxdeg","nodes","radius"]
    def run(self):
        if get("connected") == True  and minb("maxdeg") >= 3.0:
            try:
                set("nodes",  1.0+maxb("maxdeg")*((maxb("maxdeg")-(1.0))**maxb("radius")-(1.0))/(maxb("maxdeg")-(2.0)), ind='Max')
            except:
                pass
        
        return

class Theorem279(Theorem):
    def __init__(self):
        super(Theorem279, self).__init__(279, "if connected then \n{\n    nodes >= maxdeg+2.0*radius-(2.0)\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["connected","nodes","maxdeg","radius"]
    def run(self):
        if get("connected") == True :
            try:
                set("nodes",  minb("maxdeg")+2.0*minb("radius")-(2.0), ind='Min')
            except:
                pass
            try:
                set("maxdeg",  maxb("nodes")-(2.0*minb("radius"))+2.0, ind='Max')
            except:
                pass
            try:
                set("radius",  -(minb("maxdeg")/2.0)+maxb("nodes")/2.0+1.0, ind='Max')
            except:
                pass
        
        return

class Theorem280(Theorem):
    def __init__(self):
        super(Theorem280, self).__init__(280, "if forest then \n{\n    nodes >= 2.0*(bandwidth+numOfComponents-(1.0))\n\n};", "")
    def involves(self, str_invar):
        return str_invar in ["forest","nodes","bandwidth","numOfComponents"]
    def run(self):
        if get("forest") == True :
            try:
                set("nodes",  2.0*(minb("bandwidth")+minb("numOfComponents")-(1.0)), ind='Min')
            except:
                pass
            try:
                set("bandwidth",  maxb("nodes")/2.0-(minb("numOfComponents"))+1.0, ind='Max')
            except:
                pass
            try:
                set("numOfComponents",  -(minb("bandwidth"))+maxb("nodes")/2.0+1.0, ind='Max')
            except:
                pass
        
        return

