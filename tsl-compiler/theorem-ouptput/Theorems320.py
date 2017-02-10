class Theorem301(Theorem):
	def __init__(self):
		super(Theorem301, self).__init__(301, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec >= 2 and planar and not hamiltonian and bipartite then {nodes >= 26};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","hamiltonian","maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		planar = ingrid_obj.get('planar')
		hamiltonian = ingrid_obj.get('hamiltonian')
		bipartite = ingrid_obj.get('bipartite')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Min>=2.0) and (planar == True) and (hamiltonian == False) and (bipartite == True):
			try:
				ingrid_obj.set('nodes', 26.0, ind='Min')
			except:
				pass
		return

class Theorem302(Theorem):
	def __init__(self):
		super(Theorem302, self).__init__(302, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec >= 2 and planar and not hamiltonian then {nodes >= 14};", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		planar = ingrid_obj.get('planar')
		hamiltonian = ingrid_obj.get('hamiltonian')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Min>=2.0) and (planar == True) and (hamiltonian == False):
			try:
				ingrid_obj.set('nodes', 14.0, ind='Min')
			except:
				pass
		return

class Theorem303(Theorem):
	def __init__(self):
		super(Theorem303, self).__init__(303, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec >= 2 and bipartite and not hamiltonian then {nodes >= 20};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","hamiltonian","maxdeg","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		bipartite = ingrid_obj.get('bipartite')
		hamiltonian = ingrid_obj.get('hamiltonian')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Min>=2.0) and (bipartite == True) and (hamiltonian == False):
			try:
				ingrid_obj.set('nodes', 20.0, ind='Min')
			except:
				pass
		return

class Theorem304(Theorem):
	def __init__(self):
		super(Theorem304, self).__init__(304, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem305(Theorem):
	def __init__(self):
		super(Theorem305, self).__init__(305, "if mindeg == maxdeg and maxdeg == 3 then {edgeInd >= nodes/2 - floor((nodes + 3)/18) - floor(numOfComponents + 4)/6};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","maxdeg","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('edgeInd', -(0.166666666666667*floor(numOfComponents+4.0))-(1.0*floor((nodes+3.0)/18.0))+0.5*nodes, ind='Min')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edgeInd != 'undt' and nodes != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*edgeInd+0.333333333333333*floor(numOfComponents+4.0)+2.0*floor((nodes+3.0)/18.0), ind='Max')
				except:
					pass
		return

class Theorem306(Theorem):
	def __init__(self):
		super(Theorem306, self).__init__(306, "if maxClique == 2 and maxdeg <= 4 then {edges >= 6*nodes - 13*nodeInd};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=4.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('edges', -(13.0*nodeInd)+6.0*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodeInd', -(7.69230769230769e-2*edges)+0.461538461538462*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if edges != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 0.166666666666667*edges+2.16666666666667*nodeInd, ind='Max')
				except:
					pass
		return

class Theorem307(Theorem):
	def __init__(self):
		super(Theorem307, self).__init__(307, "if edgeConnec > 0 then { edgeConnec >= min(mindeg, (nodes * (maxdeg - 2))/((maxdeg - 1)**(diameter - 1) + maxdeg*(maxdeg - 2) - 1)) };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edgeConnec","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		if (edgeConnec_Min>0.0):
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', min(mindeg, (nodes*(maxdeg-(2.0)))/((maxdeg-(1.0))**(diameter-(1.0))+maxdeg*(maxdeg-(2.0))-(1.0))), ind='Min')
			except:
				pass
		return

class Theorem308(Theorem):
	def __init__(self):
		super(Theorem308, self).__init__(308, "if nodeConnec >= 2 and nodeInd >= 2 then {circumference >= 2*(nodes - 2)/nodeInd + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","nodeConnec","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		if (nodeConnec_Min>=2.0) and (nodeInd_Min>=2.0):
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', (2.0*nodeInd+2.0*nodes-(4.0))/nodeInd, ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', (2.0*nodes-(4.0))/(1.0*circumference-(2.0)), ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if circumference != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*circumference*nodeInd-(1.0*nodeInd)+2.0, ind='Max')
				except:
					pass
		return

class Theorem309(Theorem):
	def __init__(self):
		super(Theorem309, self).__init__(309, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec == 3 and planar then {circumference >= min(nodes, 17)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		planar = ingrid_obj.get('planar')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==3.0)) and (planar == True):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(nodes, 17.0), ind='Min')
			except:
				pass
		return

class Theorem310(Theorem):
	def __init__(self):
		super(Theorem310, self).__init__(310, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec == 3 and planar and nodes <= 36 then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		planar = ingrid_obj.get('planar')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==3.0)) and (planar == True) and (nodes_Max != 'undt' and (nodes_Max<=36.0)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem311(Theorem):
	def __init__(self):
		super(Theorem311, self).__init__(311, "if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg >= 9 then {nodes >= 2*maxdeg} else if maxClique < chromaticNum and chromaticNum == maxdeg and maxdeg <= 8 then {nodes >= 2*maxdeg - 1};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<chromaticNum_Min)) and (chromaticNum_Max != 'undt' and (chromaticNum_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (chromaticNum_Min>=maxdeg_Max)) and (maxdeg_Min>=9.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*maxdeg, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 0.5*nodes, ind='Max')
				except:
					pass
		elif (maxClique_Max != 'undt' and (maxClique_Max<chromaticNum_Min)) and (chromaticNum_Max != 'undt' and (chromaticNum_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (chromaticNum_Min>=maxdeg_Max)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=8.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*maxdeg-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 0.5*nodes+0.5, ind='Max')
				except:
					pass
		return

class Theorem312(Theorem):
	def __init__(self):
		super(Theorem312, self).__init__(312, "if mindeg == maxdeg and maxdeg == 3 and edgeConnec >= 2 then {edgeInd == nodes/2};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","edgeInd","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (edgeConnec_Min>=2.0):
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
		return

class Theorem313(Theorem):
	def __init__(self):
		super(Theorem313, self).__init__(313, "if planar and nodeConnec >= 3 then {circumference >= min(nodes, 2*mindeg)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (planar == True) and (nodeConnec_Min>=3.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(nodes, 2.0*mindeg), ind='Min')
			except:
				pass
		return

class Theorem314(Theorem):
	def __init__(self):
		super(Theorem314, self).__init__(314, "if regular and nodeConnec >= 2 and nodes < 3*mindeg + 4 then {circumference >= min(nodes, 3*mindeg)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg","nodeConnec","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (regular == True) and (nodeConnec_Min>=2.0) and (nodes_Max != 'undt' and (nodes_Max<3.0*mindeg_Min+4.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(nodes, 3.0*mindeg), ind='Min')
			except:
				pass
		return

class Theorem315(Theorem):
	def __init__(self):
		super(Theorem315, self).__init__(315, "if regular and nodeConnec >= 2 then {circumference >= min(min(nodes, 3*mindeg), 2*mindeg + 4)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg","nodeConnec","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (regular == True) and (nodeConnec_Min>=2.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(min(nodes, 3.0*mindeg), 2.0*mindeg+4.0), ind='Min')
			except:
				pass
		return

class Theorem316(Theorem):
	def __init__(self):
		super(Theorem316, self).__init__(316, "if regular and even nodes  and maxdeg >= 6*nodes/7 then {edgeChromatic == maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (regular == True) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (maxdeg_Min>=6.0*nodes_Max/7.0)):
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

class Theorem317(Theorem):
	def __init__(self):
		super(Theorem317, self).__init__(317, "if maxdeg == nodes - 1 and even nodes  and edges <= 2*floor((nodes-1)/2)**2 then {edgeChromatic == maxdeg} else if maxdeg == nodes - 1 and odd nodes  and edges <= 2*floor((nodes-1)/2)**2 + mindeg then {edgeChromatic == maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edges","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(1.0))) and (even(nodes_Min) and even(nodes_Max)) and (edges_Max != 'undt' and (edges_Max<=2.0*floor((nodes_Min-(1.0))/2.0)**2.0)):
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
		elif (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(1.0))) and (odd(nodes_Min) and odd(nodes_Max)) and (edges_Max != 'undt' and (edges_Max<=2.0*floor((nodes_Min-(1.0))/2.0)**2.0+mindeg_Min)):
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

class Theorem318(Theorem):
	def __init__(self):
		super(Theorem318, self).__init__(318, "null;", "HELP - WTF IS A CATALAN NUMBER")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem319(Theorem):
	def __init__(self):
		super(Theorem319, self).__init__(319, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem320(Theorem):
	def __init__(self):
		super(Theorem320, self).__init__(320, "if connected and regular and odd nodes  and nodes < 5*mindeg/2 then {girth == 3};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","girth","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		regular = ingrid_obj.get('regular')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (connected == True) and (regular == True) and (odd(nodes_Min) and odd(nodes_Max)) and (nodes_Max != 'undt' and (nodes_Max<5.0*mindeg_Min/2.0)):
			try:
				ingrid_obj.set('girth', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('girth', 3.0, ind='Min')
			except:
				pass
		return

