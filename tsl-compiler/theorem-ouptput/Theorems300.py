class Theorem281(Theorem):
	def __init__(self):
		super(Theorem281, self).__init__(281, "if nodeConnec >= 2 and nodes <= 3*mindeg and edges <= ((nodes-1)*mindeg - 1)/2 then {Hamiltonian};", "")
	def involves(self, str_invar):
		return str_invar in ["Hamiltonian","edges","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodeConnec_Min>=2.0) and (nodes_Max != 'undt' and (nodes_Max<=3.0*mindeg_Min)) and (edges_Max != 'undt' and (edges_Max<=((nodes_Min-(1.0))*mindeg_Min-(1.0))/2.0)):
			ingrid_obj.set('Hamiltonian', True)
		return

class Theorem282(Theorem):
	def __init__(self):
		super(Theorem282, self).__init__(282, "if even nodes  and not bipartite then {not cycle};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","cycle","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		bipartite = ingrid_obj.get('bipartite')
		if (even(nodes_Min) and even(nodes_Max)) and (bipartite == False):
			ingrid_obj.set('cycle', False)
		return

class Theorem283(Theorem):
	def __init__(self):
		super(Theorem283, self).__init__(283, "if mindeg == maxdeg and maxdeg == nodeConnec and nodeConnec == 3 then {circumference >= nodes^(2/3) + 1};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","maxdeg","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodeConnec_Min)) and (nodeConnec_Max != 'undt' and (maxdeg_Min>=nodeConnec_Max)) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==3.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', 1.0*nodes**0.666666666666667+1.0, ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			if circumference != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*(circumference-(1.0))**1.5, ind='Max')
				except:
					pass
		return

class Theorem284(Theorem):
	def __init__(self):
		super(Theorem284, self).__init__(284, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem285(Theorem):
	def __init__(self):
		super(Theorem285, self).__init__(285, "edgeCliqueCover <= nodeCliqueCover + nodes*(maxdeg + 1 - nodes/nodeCliqueCover)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","maxdeg","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and nodeCliqueCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 0.5*maxdeg*nodes+1.0*nodeCliqueCover+0.5*nodes-(0.5*nodes**2.0/nodeCliqueCover), ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('maxdeg', 2.0*edgeCliqueCover/nodes-(2.0*nodeCliqueCover/nodes)-(1.0)+1.0*nodes/nodeCliqueCover, ind='Min')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeCliqueCover', 0.5*edgeCliqueCover-(0.25*maxdeg*nodes)-(0.25*nodes)+0.5*(1.0*edgeCliqueCover**2.0-(1.0*edgeCliqueCover*maxdeg*nodes)-(1.0*edgeCliqueCover*nodes)+0.25*maxdeg**2.0*nodes**2.0+0.5*maxdeg*nodes**2.0+2.25*nodes**2.0)**(1/2), ind='Min')
		except:
			pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if maxdeg != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', 0.5*nodeCliqueCover*(maxdeg+1.0)+0.5*(-(nodeCliqueCover*(8.0*edgeCliqueCover-(1.0*maxdeg**2.0*nodeCliqueCover)-(2.0*maxdeg*nodeCliqueCover)-(9.0*nodeCliqueCover))))**(1/2), ind='Max')
			except:
				pass
		return

class Theorem286(Theorem):
	def __init__(self):
		super(Theorem286, self).__init__(286, "edges >= (maxdeg + (chromaticNum - 1)**2 + (nodes -chromaticNum)*mindeg)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', -(0.5*chromaticNum*mindeg)+0.5*maxdeg+0.5*mindeg*nodes+0.5*(chromaticNum-(1.0))**2.0, ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', ((-((chromaticNum))+nodes)*mindeg+(-((1.0))+chromaticNum)**2.0+maxdeg)/2.0, ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if chromaticNum != 'undt' and edges != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('maxdeg', 2.0*edges+1.0*chromaticNum*mindeg-(1.0*mindeg*nodes)-(1.0*(chromaticNum-(1.0))**2.0), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('mindeg', 2.0*(-(edges)+0.5*maxdeg+0.5*(chromaticNum-(1.0))**2.0)/(chromaticNum-(nodes)), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		if chromaticNum != 'undt' and edges != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('nodes', (2.0*edges+chromaticNum*mindeg-(1.0*maxdeg)-(1.0*(chromaticNum-(1.0))**2.0))/mindeg, ind='Max')
			except:
				pass
		return

class Theorem287(Theorem):
	def __init__(self):
		super(Theorem287, self).__init__(287, "if planar then {mindeg <= nodeInd + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeInd","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		if (planar == True):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*nodeInd+2.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 1.0*mindeg-(2.0), ind='Min')
			except:
				pass
		return

class Theorem288(Theorem):
	def __init__(self):
		super(Theorem288, self).__init__(288, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem289(Theorem):
	def __init__(self):
		super(Theorem289, self).__init__(289, "if connected and not hamiltonian and not tree and circumference >= (nodes - 2)/2 then {domination <= (2*nodes - circumference)/3};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","connected","domination","hamiltonian","nodes","tree"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		hamiltonian = ingrid_obj.get('hamiltonian')
		tree = ingrid_obj.get('tree')
		circumference_Min = ingrid_obj.get('circumference', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (connected == True) and (hamiltonian == False) and (tree == False) and (nodes_Max != 'undt' and (circumference_Min>=(nodes_Max-(2.0))/2.0)):
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.333333333333333*circumference)+0.666666666666667*nodes, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('circumference', -(3.0*domination)+2.0*nodes, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			domination = ingrid_obj.get('domination', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.5*domination+0.5*circumference, ind='Min')
			except:
				pass
		return

class Theorem290(Theorem):
	def __init__(self):
		super(Theorem290, self).__init__(290, "if connected and domination >= 3 then { edges <= (nodes - domination + 1)*(nodes - domination)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","domination","edges","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		domination_Min = ingrid_obj.get('domination', ind='Min')
		if (connected == True) and (domination_Min>=3.0):
			domination = ingrid_obj.get('domination', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if domination != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*domination**2.0-(1.0*domination*nodes)-(0.5*domination)+0.5*nodes**2.0+0.5*nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			try:
				ingrid_obj.set('domination', 1.0*nodes+0.5*(8.0*edges+1.0)**(1/2)+0.5, ind='Max')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*domination+0.5*(8.0*edges+1.0)**(1/2)-(0.5), ind='Min')
			except:
				pass
		return

class Theorem291(Theorem):
	def __init__(self):
		super(Theorem291, self).__init__(291, "domination <= nodes*(1 + ln(mindeg))/(mindeg+1);", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem292(Theorem):
	def __init__(self):
		super(Theorem292, self).__init__(292, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem293(Theorem):
	def __init__(self):
		super(Theorem293, self).__init__(293, "if connected and maxdeg == 2 and mindeg == 1 then {nodes == diameter + 1} else if connected and maxdeg == 2 and mindeg == 2 then {nodes  >= 2*diameter and nodes <= 2*diameter + 1};", "HELP - ensure this is correct")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (connected == True) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==2.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==1.0)):
			diameter = ingrid_obj.get('diameter', ind='Max')
			if diameter != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*diameter+1.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*diameter+1.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 1.0*nodes-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('diameter', 1.0*nodes-(1.0), ind='Min')
			except:
				pass
		elif (connected == True) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==2.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)):
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*diameter, ind='Min')
			except:
				pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			if diameter != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*diameter+1.0, ind='Max')
				except:
					pass
		return

class Theorem294(Theorem):
	def __init__(self):
		super(Theorem294, self).__init__(294, "edgeCliqueCover <= (nodes - maxClique + 2)**2/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","maxClique","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 0.25*(-(maxClique)+nodes+2.0)**2.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('maxClique', -(2.0*edgeCliqueCover**0.5)+nodes+2.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*edgeCliqueCover**0.5+maxClique-(2.0), ind='Min')
		except:
			pass
		return

class Theorem295(Theorem):
	def __init__(self):
		super(Theorem295, self).__init__(295, "edges <= max(edgeInd*(2*edgeInd + 1), edgeInd*nodes - edgeInd*(edgeInd + 1)/2);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","edges","nodes"]
	def run(self, ingrid_obj):
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edgeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', max(edgeInd*(2.0*edgeInd+1.0), edgeInd*nodes-(edgeInd*(edgeInd+1.0)/2.0)), ind='Max')
			except:
				pass
		return

class Theorem296(Theorem):
	def __init__(self):
		super(Theorem296, self).__init__(296, "if mindeg == maxdeg and maxdeg == 3 then {nodeConnec == edgeConnec};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","maxdeg","mindeg","nodeConnec"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)):
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			if edgeConnec != 'undt':
				try:
					ingrid_obj.set('nodeConnec', edgeConnec, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', edgeConnec, ind='Min')
			except:
				pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('edgeConnec', nodeConnec, ind='Max')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', nodeConnec, ind='Min')
			except:
				pass
		return

class Theorem297(Theorem):
	def __init__(self):
		super(Theorem297, self).__init__(297, "if nodeConnec >= 3 and planar and not hamiltonian then {nodes >= 11};", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		planar = ingrid_obj.get('planar')
		hamiltonian = ingrid_obj.get('hamiltonian')
		if (nodeConnec_Min>=3.0) and (planar == True) and (hamiltonian == False):
			try:
				ingrid_obj.set('nodes', 11.0, ind='Min')
			except:
				pass
		return

class Theorem298(Theorem):
	def __init__(self):
		super(Theorem298, self).__init__(298, "if mindeg == maxdeg and maxdeg == 3 and not planar and not bipartite then {nodes >= 8};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","maxdeg","mindeg","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		planar = ingrid_obj.get('planar')
		bipartite = ingrid_obj.get('bipartite')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (planar == False) and (bipartite == False):
			try:
				ingrid_obj.set('nodes', 8.0, ind='Min')
			except:
				pass
		return

class Theorem299(Theorem):
	def __init__(self):
		super(Theorem299, self).__init__(299, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec == 1 then {nodes >= 10};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==1.0)):
			try:
				ingrid_obj.set('nodes', 10.0, ind='Min')
			except:
				pass
		return

class Theorem300(Theorem):
	def __init__(self):
		super(Theorem300, self).__init__(300, "if mindeg == maxdeg and maxdeg == 3 and nodeConnec == 1 and not planar then {nodes >= 12};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		planar = ingrid_obj.get('planar')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==1.0)) and (planar == False):
			try:
				ingrid_obj.set('nodes', 12.0, ind='Min')
			except:
				pass
		return

