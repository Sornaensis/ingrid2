class Theorem401(Theorem):
	def __init__(self):
		super(Theorem401, self).__init__(401, "if planar and edges == 3*nodes - 6 and maxdeg <= mindeg + 1 then {mindeg == nodeConnec};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","mindeg","nodeConnec","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (planar == True) and (edges_Max != 'undt' and (edges_Max<=3.0*nodes_Min-(6.0))) and (nodes_Max != 'undt' and (edges_Min>=3.0*nodes_Max-(6.0))) and (maxdeg_Max != 'undt' and (maxdeg_Max<=mindeg_Min+1.0)):
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('mindeg', nodeConnec, ind='Max')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodeConnec, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodeConnec', mindeg, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', mindeg, ind='Min')
			except:
				pass
		return

class Theorem402(Theorem):
	def __init__(self):
		super(Theorem402, self).__init__(402, "bandwidth <= nodes - (mindeg + 1)*(numOfComponents -1) - 1 - (nodeInd - numOfComponents + 1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","mindeg","nodeInd","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('bandwidth', -(1.0*mindeg*numOfComponents)+1.0*mindeg-(0.5*nodeInd)+1.0*nodes-(0.5*numOfComponents)-(0.5), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*(-(1.0*bandwidth)-(0.5*nodeInd)+1.0*nodes-(0.5*numOfComponents)-(0.5))/(numOfComponents-(1.0)), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', -(2.0*bandwidth)-(2.0*mindeg*numOfComponents)+2.0*mindeg+2.0*nodes-(1.0*numOfComponents)-(1.0), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*bandwidth+1.0*mindeg*numOfComponents-(1.0*mindeg)+0.5*nodeInd+0.5*numOfComponents+0.5, ind='Min')
		except:
			pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('numOfComponents', (-(1.0*bandwidth)+1.0*mindeg-(0.5*nodeInd)+1.0*nodes-(0.5))/(1.0*mindeg+0.5), ind='Max')
			except:
				pass
		return

class Theorem403(Theorem):
	def __init__(self):
		super(Theorem403, self).__init__(403, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem404(Theorem):
	def __init__(self):
		super(Theorem404, self).__init__(404, "if mindeg >edgeConnec and edgeConnec == nodeConnec then { nodes >= mindeg + maxdeg };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","maxdeg","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (edgeConnec_Max != 'undt' and (mindeg_Min>edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (edgeConnec_Max<=nodeConnec_Min)) and (nodeConnec_Max != 'undt' and (edgeConnec_Min>=nodeConnec_Max)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', maxdeg+mindeg, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', nodes-(mindeg), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes-(maxdeg), ind='Max')
				except:
					pass
		return

class Theorem405(Theorem):
	def __init__(self):
		super(Theorem405, self).__init__(405, "if mindeg > edgeConnec and edgeConnec == nodeConnec and nodeConnec > 0 and diam == 3 then {domination <= edgeConnec + 1};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","domination","edgeConnec","mindeg","nodeConnec"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		diam_Min = ingrid_obj.get('diam', ind='Min')
		diam_Max = ingrid_obj.get('diam', ind='Max')
		if (edgeConnec_Max != 'undt' and (mindeg_Min>edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (edgeConnec_Max<=nodeConnec_Min)) and (nodeConnec_Max != 'undt' and (edgeConnec_Min>=nodeConnec_Max)) and (nodeConnec_Min>0.0) and (diam_Max==diam_Min and (diam_Min==3.0)):
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			if edgeConnec != 'undt':
				try:
					ingrid_obj.set('domination', 1.0*edgeConnec+1.0, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', 1.0*domination-(1.0), ind='Min')
			except:
				pass
		return

class Theorem406(Theorem):
	def __init__(self):
		super(Theorem406, self).__init__(406, "if edges > (nodes - 1)**2/4 and edges <= (nodes-1)*(nodes-2)/2 then {mindeg <= edgeConnec - 1 + (nodes - sqrt(4*edges + 2*nodes - nodes**2))/2};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","edges","mindeg","nodes"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodes_Max != 'undt' and (edges_Min>(nodes_Max-(1.0))**2.0/4.0)) and (edges_Max != 'undt' and (edges_Max<=(nodes_Min-(1.0))*(nodes_Min-(2.0))/2.0)):
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edgeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', edgeConnec+0.5*nodes-(0.5*(4.0*edges+2.0*nodes-(nodes**2.0))**0.5)-(1.0), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', mindeg-(0.5*nodes)+0.5*(4.0*edges+2.0*nodes-(nodes**2.0))**0.5+1.0, ind='Min')
			except:
				pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edgeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', -(0.5*nodes)+0.25*nodes**2.0+0.25*(-(2.0*mindeg)+2.0*edgeConnec+1.0*nodes-(2.0))**2.0, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edgeConnec != 'undt' and edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (-(((4.0*edges+2.0*nodes-((nodes**2.0)))**(1.0/2.0)))+nodes)/2.0-((1.0))+edgeConnec, ind='Max')
				except:
					pass
		return

class Theorem407(Theorem):
	def __init__(self):
		super(Theorem407, self).__init__(407, "domination <= (nodes - maxdeg - 1)*(nodes - mindeg - 2)/(nodes - 1) + 2;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('domination', 1.0*(1.0*maxdeg*mindeg-(1.0*maxdeg*nodes)+2.0*maxdeg-(1.0*mindeg*nodes)+1.0*mindeg+1.0*nodes**2.0-(1.0*nodes))/(nodes-(1.0)), ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('maxdeg', 1.0*(domination*nodes-(domination)+mindeg*nodes-(mindeg)-(nodes**2.0)+nodes)/(1.0*mindeg-(1.0*nodes)+2.0), ind='Min')
		except:
			pass
		domination = ingrid_obj.get('domination', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('mindeg', 1.0*(1.0*domination*nodes-(1.0*domination)+1.0*maxdeg*nodes-(2.0*maxdeg)-(1.0*nodes**2.0)+1.0*nodes)/(maxdeg-(nodes)+1.0), ind='Min')
		except:
			pass
		return

class Theorem408(Theorem):
	def __init__(self):
		super(Theorem408, self).__init__(408, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem409(Theorem):
	def __init__(self):
		super(Theorem409, self).__init__(409, "if nodes >= 4 and maxClique == 2 and hamiltonian then {edges <= (nodes - 4)*nodes/4 + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","hamiltonian","maxClique","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		hamiltonian = ingrid_obj.get('hamiltonian')
		if (nodes_Min>=4.0) and (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (hamiltonian == True):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.25*nodes**2.0-(1.0*nodes)+2.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*(edges-(1.0))**(1/2)+2.0, ind='Max')
				except:
					pass
		return

class Theorem410(Theorem):
	def __init__(self):
		super(Theorem410, self).__init__(410, "spectralRadius >= mindeg;", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","spectralRadius"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('spectralRadius', mindeg, ind='Min')
		except:
			pass
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('mindeg', spectralRadius, ind='Max')
			except:
				pass
		return

class Theorem411(Theorem):
	def __init__(self):
		super(Theorem411, self).__init__(411, "if connected and nodes >= 2*mindeg + 2 and istrue congruent(nodes, mindeg+1, 0) then {diameter <= 3*nodes/(mindeg+1) - 3} else if connected and nodes >= 2*mindeg + 2 and istrue congruent(nodes, mindeg+1, 1) then {diam <= 3*nodes/(mindeg+1)+2} else if connected and nodes >= 2*mindeg + 2 then {diam <= 3*nodes/(mindeg+1) - 1};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diam","diameter","mindeg","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind = 'Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind = 'Max')
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		if (connected == True) and (mindeg_Max != 'undt' and (nodes_Min>=2.0*mindeg_Max+2.0)) and (mindeg_Min == mindeg_Max) and (nodes_Min == nodes_Max):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 3.0*(-(mindeg)+nodes-(1.0))/(mindeg+1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (-(1.0*diameter)+3.0*nodes-(3.0))/(1.0*diameter+3.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diameter*mindeg+0.333333333333333*diameter+1.0*mindeg+1.0, ind='Min')
			except:
				pass
		elif (connected == True) and (mindeg_Max != 'undt' and (nodes_Min>=2.0*mindeg_Max+2.0)) and (mindeg_Min == mindeg_Max) and (nodes_Min == nodes_Max):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diam', 1.0*(2.0*mindeg+3.0*nodes+2.0)/(mindeg+1.0), ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diam != 'undt':
				try:
					ingrid_obj.set('mindeg', (-(1.0*diam)+3.0*nodes+2.0)/(1.0*diam-(2.0)), ind='Min')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diam*mindeg+0.333333333333333*diam-(0.666666666666667*mindeg)-(0.666666666666667), ind='Min')
			except:
				pass
		elif (connected == True) and (mindeg_Max != 'undt' and (nodes_Min>=2.0*mindeg_Max+2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diam', 1.0*(-(1.0*mindeg)+3.0*nodes-(1.0))/(mindeg+1.0), ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (-(1.0*diam)+3.0*nodes-(1.0))/(diam+1.0), ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diam*mindeg+0.333333333333333*diam+0.333333333333333*mindeg+0.333333333333333, ind='Min')
			except:
				pass
		return

class Theorem412(Theorem):
	def __init__(self):
		super(Theorem412, self).__init__(412, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem413(Theorem):
	def __init__(self):
		super(Theorem413, self).__init__(413, "edges >= (nodes - chromaticNum)**2/(nodeInd-1) + chromaticNum *(chromaticNum - 1)/2 - (nodeInd-1)*((nodes-chromaticNum)/(nodeInd-1)) * ((nodes-chromaticNum)/(nodeInd-1))/2;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', (0.5*chromaticNum**2.0*nodeInd-(1.0*chromaticNum**2.0)-(0.5*chromaticNum*nodeInd)+1.0*chromaticNum*nodes+0.5*chromaticNum-(0.5*nodes**2.0)+(-(chromaticNum)+nodes)**2.0)/(nodeInd-(1.0)), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', -(((-((1.0))+nodeInd)*((-((chromaticNum))+nodes)/(-((1.0))+nodeInd))*((-((chromaticNum))+nodes)/(-((1.0))+nodeInd))/2.0))+chromaticNum*(-((1.0))+chromaticNum)/2.0+(-((chromaticNum))+nodes)**2.0/(-((1.0))+nodeInd), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeInd', (1.0*edges-(1.0*chromaticNum**2.0)+1.0*chromaticNum*nodes+0.5*chromaticNum-(0.5*nodes**2.0)+(-(chromaticNum)+nodes)**2.0)/(edges-(0.5*chromaticNum**2.0)+0.5*chromaticNum), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', -(((-((1.0))+nodeInd)*((-((chromaticNum))+nodes)/(-((1.0))+nodeInd))*((-((chromaticNum))+nodes)/(-((1.0))+nodeInd))/2.0))+chromaticNum*(-((1.0))+chromaticNum)/2.0+(-((chromaticNum))+nodes)**2.0/(-((1.0))+nodeInd), ind='Min')
		except:
			pass
		return

class Theorem414(Theorem):
	def __init__(self):
		super(Theorem414, self).__init__(414, "if diam <= 4 then {edges <= ((nodes-2)*(nodes - 3) - 2*(nodes-2)*(diam-4)*nodeConnec - 4 * nodeConnec * (nodeConnec+1) + nodeConnec**2*(diam-2)*(diam-3))/2};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diam_Max = ingrid_obj.get('diam', ind='Max')
		if (diam_Max != 'undt' and (diam_Max<=4.0)):
			diam = ingrid_obj.get('diam', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diam != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*diam**2.0*nodeConnec**2.0-(1.0*diam*nodeConnec*nodes)+2.0*diam*nodeConnec-(2.5*diam*nodeConnec**2.0)-(2.0*nodeConnec**2.0)+4.0*nodeConnec*nodes-(10.0*nodeConnec)+3.0*nodeConnec**2.0+0.5*nodes**2.0-(2.5*nodes)+3.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('diam', nodeConnec**(-(3.0))*(1.0*nodeConnec**1.0*(nodeConnec**2.0*(2.0*edges+4.0*nodeConnec**2.0-(8.0*nodeConnec*nodes)+20.0*nodeConnec-(6.0*nodeConnec**2.0)-(1.0*nodes**2.0)+5.0*nodes-(6.0))+(1.0*nodeConnec*nodes-(2.0*nodeConnec)+2.5*nodeConnec**2.0)**2.0)**(1/2)+nodeConnec**2.0*(2.5*nodeConnec**1.0+1.0*nodes-(2.0))), ind='Min')
			except:
				pass
			diam = ingrid_obj.get('diam', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diam != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', (nodeConnec**2.0*(-((2.0))+diam)*(-((3.0))+diam)-((4.0*nodeConnec*(1.0+nodeConnec)))-((2.0*(-((2.0))+nodes)*(-((4.0))+diam)*nodeConnec))+(-((2.0))+nodes)*(-((3.0))+nodes))/2.0, ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*diam*nodeConnec-(4.0*nodeConnec)+1.0*(2.0*edges-(1.0*diam**2.0*nodeConnec**2.0)-(4.0*diam*nodeConnec)+5.0*diam*nodeConnec**2.0+4.0*nodeConnec**2.0+20.0*nodeConnec-(6.0*nodeConnec**2.0)+(1.0*diam*nodeConnec-(4.0*nodeConnec)+2.5)**2.0-(6.0))**(1/2)+2.5, ind='Min')
			except:
				pass
		return

class Theorem415(Theorem):
	def __init__(self):
		super(Theorem415, self).__init__(415, "domination <= (nodes + 2 - mindeg)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('domination', -(0.5*mindeg)+0.5*nodes+1.0, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', -(2.0*domination)+1.0*nodes+2.0, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*domination+1.0*mindeg-(2.0), ind='Min')
		except:
			pass
		return

class Theorem416(Theorem):
	def __init__(self):
		super(Theorem416, self).__init__(416, "if even nodes and maxdeg == nodes - 2 and edgeChromatic == maxdeg + 1 then {edges >= (nodes - 2)**2 / 2 + 1 + mindeg}; if even nodes and maxdeg == nodes - 2 and edges >= (nodes-2)**2 / 2 + 1 + mindeg then {maxdeg == nodes - 2};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edges","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		edgeChromatic_Max = ingrid_obj.get('edgeChromatic', ind='Max')
		edgeChromatic_Min = ingrid_obj.get('edgeChromatic', ind='Min')
		if (even(nodes_Min) and even(nodes_Max)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(2.0))) and (edgeChromatic_Max != 'undt' and (edgeChromatic_Max<=maxdeg_Min+1.0)) and (maxdeg_Max != 'undt' and (edgeChromatic_Min>=maxdeg_Max+1.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*mindeg+0.5*(nodes-(2.0))**2.0+1.0, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*edges-(0.5*(nodes-(2.0))**2.0)-(1.0), ind='Max')
				except:
					pass
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (even(nodes_Min) and even(nodes_Max)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(2.0))) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>=(nodes_Max-(2.0))**2.0/2.0+1.0+mindeg_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(2.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 1.0*nodes-(2.0), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*maxdeg+2.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg+2.0, ind='Min')
			except:
				pass
		return

class Theorem417(Theorem):
	def __init__(self):
		super(Theorem417, self).__init__(417, "if maxClique <= 2 and maxdeg <= 3 then {edges >= 13*nodes/2 - 14*nodeInd};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=3.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('edges', -(14.0*nodeInd)+6.5*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodeInd', -(7.14285714285714e-2*edges)+0.464285714285714*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if edges != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 0.153846153846154*edges+2.15384615384615*nodeInd, ind='Max')
				except:
					pass
		return

class Theorem418(Theorem):
	def __init__(self):
		super(Theorem418, self).__init__(418, "if maxClique <= 2 and maxdeg <= 2 then {edges >= 7*nodes - 15*nodeInd};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=2.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('edges', -(15.0*nodeInd)+7.0*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodeInd', -(6.66666666666667e-2*edges)+0.466666666666667*nodes, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if edges != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 0.142857142857143*edges+2.14285714285714*nodeInd, ind='Max')
				except:
					pass
		return

class Theorem419(Theorem):
	def __init__(self):
		super(Theorem419, self).__init__(419, "if maxClique <= 2 and nodeCover <= 3*nodes/5 then {nodeCover <= (3*nodes - sqrt(5*edges - nodes**2))/5};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		nodeCover_Max = ingrid_obj.get('nodeCover', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (nodeCover_Max != 'undt' and (nodeCover_Max<=3.0*nodes_Min/5.0)):
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.6*nodes-(0.2*(5.0*edges-(nodes**2.0))**0.5), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('edges', 0.2*nodes**2.0+0.2*(-(5.0*nodeCover)+3.0*nodes)**2.0, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', (-(((5.0*edges-((nodes**2.0)))**(1.0/2.0)))+3.0*nodes)/5.0, ind='Max')
				except:
					pass
		return

class Theorem420(Theorem):
	def __init__(self):
		super(Theorem420, self).__init__(420, "if maxClique <= 2 and nodeInd <= 2*nodes/5 then {nodeInd >= (2*nodes + sqrt(5*edges - nodes**2))/5};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (nodeInd_Max != 'undt' and (nodeInd_Max<=2.0*nodes_Min/5.0)):
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.4*nodes+0.2*(5.0*edges-(nodes**2.0))**0.5, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.2*nodes**2.0+0.2*(5.0*nodeInd-(2.0*nodes))**2.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', ((5.0*edges-((nodes**2.0)))**(1.0/2.0)+2.0*nodes)/5.0, ind='Min')
			except:
				pass
		return

