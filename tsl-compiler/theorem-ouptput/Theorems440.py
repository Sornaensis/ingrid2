TypeError('unorderable types: float() >= complex()',)
TypeError('unorderable types: float() >= complex()',)
TypeError('unorderable types: float() >= complex()',)
class Theorem421(Theorem):
	def __init__(self):
		super(Theorem421, self).__init__(421, "if nodeInd == 2 and maxClique >= 2*nodes/5 then {maxClique >= (2*nodes + sqrt(nodes*(3*nodes-5)/2 - 5*edges))/5};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)) and (nodes_Max != 'undt' and (maxClique_Min>=2.0*nodes_Max/5.0)):
		return

class Theorem422(Theorem):
	def __init__(self):
		super(Theorem422, self).__init__(422, "if not forest then {bandwidth >= (2*nodeCover*(girth - 2) - nodes*(girth-3))/(2*(nodes-nodeCover))};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","forest","girth","nodeCover","nodes"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			girth = ingrid_obj.get('girth', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('bandwidth', 0.5*(-(2.0*girth*nodeCover)+1.0*girth*nodes+4.0*nodeCover-(3.0*nodes))/(nodeCover-(nodes)), ind='Min')
			except:
				pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('girth', (-(2.0*bandwidth*nodeCover)+2.0*bandwidth*nodes+4.0*nodeCover-(3.0*nodes))/(2.0*nodeCover-(1.0*nodes)), ind='Min')
			except:
				pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if bandwidth != 'undt' and girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodes*(2.0*bandwidth+1.0*girth-(3.0))/(2.0*bandwidth+2.0*girth-(4.0)), ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if bandwidth != 'undt' and girth != 'undt' and nodeCover != 'undt':
				try:
					ingrid_obj.set('nodes', nodeCover*(2.0*bandwidth+2.0*girth-(4.0))/(2.0*bandwidth+1.0*girth-(3.0)), ind='Max')
				except:
					pass
		return

class Theorem423(Theorem):
	def __init__(self):
		super(Theorem423, self).__init__(423, "nodeCover <= nodes - maxdeg / (chromaticNum - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*(chromaticNum*nodes-(maxdeg)-(nodes))/(chromaticNum-(1.0)), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*(nodeCover-(maxdeg)-(nodes))/(nodeCover-(nodes)), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0*nodeCover*chromaticNum)+1.0*nodeCover+1.0*chromaticNum*nodes-(1.0*nodes), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*(nodeCover*chromaticNum-(nodeCover)+maxdeg)/(chromaticNum-(1.0)), ind='Min')
		except:
			pass
		return

class Theorem424(Theorem):
	def __init__(self):
		super(Theorem424, self).__init__(424, "if connected and (not cycle or (cycle and isset nodes and even nodes)) and (edges >= nodes or maxdeg > 2 or (isset nodes and odd nodes)) then {nodeCover <= (nodes * (maxdeg**2 + maxdeg - 1))/(maxdeg*(maxdeg+1)) - nodes**2/(nodes+2*edges)};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","cycle","edges","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (connected == True) and (cycle == False) or (cycle == True) and (nodes_Min == nodes_Max) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (edges_Min>=nodes_Max)) or (maxdeg_Min>2.0) or (nodes_Min == nodes_Max) and (odd(nodes_Min) and odd(nodes_Max)):
			edges = ingrid_obj.get('edges', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', (2.0*edges*maxdeg*nodes+2.0*edges*maxdeg**2.0*nodes-(2.0*edges*nodes)-(maxdeg**2.0*nodes**2.0)+maxdeg*nodes**2.0-(1.0*maxdeg*nodes**2.0)+maxdeg**2.0*nodes**2.0-(1.0*nodes**2.0))/(maxdeg*(2.0*edges*maxdeg+2.0*edges+maxdeg*nodes+1.0*nodes)), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*(-(nodeCover*maxdeg**2.0*nodes)-(nodeCover*maxdeg*nodes)-(maxdeg**2.0*nodes**2.0)+maxdeg*nodes**2.0-(maxdeg*nodes**2.0)+maxdeg**2.0*nodes**2.0-(nodes**2.0))/(nodeCover*maxdeg**2.0+nodeCover*maxdeg-(maxdeg*nodes)-(maxdeg**2.0*nodes)+nodes), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', -((nodes**2.0/(2.0*edges+nodes)))+(nodes*(-((1.0))+maxdeg+maxdeg**2.0))/(maxdeg*(1.0+maxdeg)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', -((nodes**2.0/(2.0*edges+nodes)))+(nodes*(-((1.0))+maxdeg+maxdeg**2.0))/(maxdeg*(1.0+maxdeg)), ind='Max')
				except:
					pass
		return

class Theorem425(Theorem):
	def __init__(self):
		super(Theorem425, self).__init__(425, "if planar then {mindeg <= nodes - nodeCover + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeCover","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		if (planar == True):
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', -(1.0*nodeCover)+1.0*nodes+2.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', -(1.0*mindeg)+1.0*nodes+2.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*mindeg+1.0*nodeCover-(2.0), ind='Min')
			except:
				pass
		return

class Theorem426(Theorem):
	def __init__(self):
		super(Theorem426, self).__init__(426, "edges <= max((nodes-edgeCover)*(2*nodes - 2*edgeCover + 1), (nodes-edgeCover)*(nodes+edgeCover-1)/2);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","edges","nodes"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edgeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', max((nodes-(edgeCover))*(2.0*nodes-(2.0*edgeCover)+1.0), (nodes-(edgeCover))*(nodes+edgeCover-(1.0))/2.0), ind='Max')
			except:
				pass
		return

class Theorem427(Theorem):
	def __init__(self):
		super(Theorem427, self).__init__(427, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem428(Theorem):
	def __init__(self):
		super(Theorem428, self).__init__(428, "if mindeg == 3 and maxdeg == 3 then {edgeCover <= nodes/2 + (nodes+3)/18 + (numOfComponents + 4)/6};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","maxdeg","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (mindeg_Max==mindeg_Min and (mindeg_Min==3.0)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if nodes != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.555555555555556*nodes+0.166666666666667*numOfComponents+0.833333333333333, ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('nodes', 1.8*edgeCover-(0.3*numOfComponents)-(1.5), ind='Min')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 6.0*edgeCover-(3.33333333333333*nodes)-(5.0), ind='Min')
				except:
					pass
		return

class Theorem429(Theorem):
	def __init__(self):
		super(Theorem429, self).__init__(429, "if maxClique == 2 and maxdeg <= 4 then {edges >= 13*nodeCover - 7*nodes};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=4.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 13.0*nodeCover-(7.0*nodes), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 7.69230769230769e-2*edges+0.538461538461539*nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', -(0.142857142857143*edges)+1.85714285714286*nodeCover, ind='Min')
				except:
					pass
		return

class Theorem430(Theorem):
	def __init__(self):
		super(Theorem430, self).__init__(430, "if nodeConnec >= 2 and nodeCover <= nodes - 2 then {circumference >= (2*(2*nodes - nodeCover - 2)/(nodes - nodeCover))};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","nodeConnec","nodeCover","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeCover_Max = ingrid_obj.get('nodeCover', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodeConnec_Min>=2.0) and (nodeCover_Max != 'undt' and (nodeCover_Max<=nodes_Min-(2.0))):
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', 1.0*(2.0*nodeCover-(4.0*nodes)+4.0)/(nodeCover-(nodes)), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeCover', (1.0*circumference*nodes-(4.0*nodes)+4.0)/(1.0*circumference-(2.0)), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', (1.0*circumference*nodeCover-(2.0*nodeCover)-(4.0))/(1.0*circumference-(4.0)), ind='Min')
			except:
				pass
		return

class Theorem431(Theorem):
	def __init__(self):
		super(Theorem431, self).__init__(431, "if girth >= 6 then {nodeCover <= nodes*maxdeg**2 / (maxdeg**2 + 2*maxdeg -1)};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=6.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', maxdeg**2.0*nodes/(2.0*maxdeg+maxdeg**2.0-(1.0)), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodes*maxdeg**2.0/(-((1.0))+2.0*maxdeg+maxdeg**2.0), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', nodeCover*maxdeg**(-(2.0))*(2.0*maxdeg+maxdeg**2.0-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem432(Theorem):
	def __init__(self):
		super(Theorem432, self).__init__(432, "if mindeg == maxdeg and mindeg == 2 and girth >= 8 then {nodeCover <= 33*nodes/53} else if mindeg==maxdeg and mindeg==2 and girth >= 6 then {nodeCover <= 33*nodes/52};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)) and (girth_Min>=8.0):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.622641509433962*nodes, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.60606060606061*nodeCover, ind='Min')
			except:
				pass
		elif (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)) and (girth_Min>=6.0):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.634615384615385*nodes, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.57575757575758*nodeCover, ind='Min')
			except:
				pass
		return

class Theorem433(Theorem):
	def __init__(self):
		super(Theorem433, self).__init__(433, "if regular and nodes < 2*nodeCover then {edgeChromatic == maxdeg + 1};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg","nodeCover","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodeCover_Min = ingrid_obj.get('nodeCover', ind='Min')
		if (regular == True) and (nodes_Max != 'undt' and (nodes_Max<2.0*nodeCover_Min)):
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

class Theorem434(Theorem):
	def __init__(self):
		super(Theorem434, self).__init__(434, "if regular then {edgeCover <= nodes*(maxdeg +2)/(2*(maxdeg+1))};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","maxdeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		if (regular == True):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.5*nodes*(1.0*maxdeg+2.0)/(maxdeg+1.0), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 2.0*(-(edgeCover)+nodes)/(2.0*edgeCover-(1.0*nodes)), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*edgeCover*(maxdeg+1.0)/(1.0*maxdeg+2.0), ind='Min')
			except:
				pass
		return

class Theorem435(Theorem):
	def __init__(self):
		super(Theorem435, self).__init__(435, "if regular and nodes == 2*maxdeg + 1 then {nodeCover >= nodes - nodeConnec};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodeConnec","nodeCover","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (regular == True) and (nodes_Max != 'undt' and (nodes_Max<=2.0*maxdeg_Min+1.0)) and (maxdeg_Max != 'undt' and (nodes_Min>=2.0*maxdeg_Max+1.0)):
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodeCover', -(nodeConnec)+nodes, ind='Min')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodeConnec', -(nodeCover)+nodes, ind='Min')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeConnec != 'undt' and nodeCover != 'undt':
				try:
					ingrid_obj.set('nodes', nodeCover+nodeConnec, ind='Max')
				except:
					pass
		return

class Theorem436(Theorem):
	def __init__(self):
		super(Theorem436, self).__init__(436, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem437(Theorem):
	def __init__(self):
		super(Theorem437, self).__init__(437, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem438(Theorem):
	def __init__(self):
		super(Theorem438, self).__init__(438, "nodeInd >= (2*nodes - edges + edgeInd)/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodeInd', 0.25*edgeInd-(0.25*edges)+0.5*nodes, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('edgeInd', 4.0*nodeInd+1.0*edges-(2.0*nodes), ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', -(4.0*nodeInd)+1.0*edgeInd+2.0*nodes, ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if edges != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*nodeInd-(0.5*edgeInd)+0.5*edges, ind='Max')
			except:
				pass
		return

class Theorem439(Theorem):
	def __init__(self):
		super(Theorem439, self).__init__(439, "nodeCover <= (nodes +edges + edgeCover)/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","edges","nodeCover","nodes"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edgeCover != 'undt' and edges != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 0.25*edgeCover+0.25*edges+0.25*nodes, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edges != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edgeCover', 4.0*nodeCover-(1.0*edges)-(1.0*nodes), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edgeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 4.0*nodeCover-(1.0*edgeCover)-(1.0*nodes), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if edgeCover != 'undt' and edges != 'undt':
			try:
				ingrid_obj.set('nodes', 4.0*nodeCover-(1.0*edgeCover)-(1.0*edges), ind='Min')
			except:
				pass
		return

class Theorem440(Theorem):
	def __init__(self):
		super(Theorem440, self).__init__(440, "nodeInd >= (3*nodes - edges - edgeCover)/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeCover != 'undt' and edges != 'undt':
			try:
				ingrid_obj.set('nodeInd', -(0.25*edgeCover)-(0.25*edges)+0.75*nodes, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('edgeCover', -(4.0*nodeInd)-(1.0*edges)+3.0*nodes, ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeCover != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', -(4.0*nodeInd)-(1.0*edgeCover)+3.0*nodes, ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if edgeCover != 'undt' and edges != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 1.33333333333333*nodeInd+0.333333333333333*edgeCover+0.333333333333333*edges, ind='Max')
			except:
				pass
		return

