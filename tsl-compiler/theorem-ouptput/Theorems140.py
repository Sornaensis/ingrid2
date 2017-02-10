TypeError('unorderable types: float() <= complex()',)
TypeError('unorderable types: float() <= complex()',)
TypeError('unorderable types: float() <= complex()',)
TypeError('unorderable types: float() >= complex()',)
class Theorem121(Theorem):
	def __init__(self):
		super(Theorem121, self).__init__(121, "chromaticNum <= nodes - nodeConnec*(diameter - 3) - 2;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","diameter","nodeConnec","nodes"]
	def run(self, ingrid_obj):
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
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		diameter = ingrid_obj.get('diameter', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if chromaticNum != 'undt' and diameter != 'undt':
			try:
				ingrid_obj.set('nodeConnec', (-(1.0*chromaticNum)+1.0*nodes-(2.0))/(1.0*diameter-(3.0)), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		diameter = ingrid_obj.get('diameter', ind='Min')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*chromaticNum+1.0*diameter*nodeConnec-(3.0*nodeConnec)+2.0, ind='Min')
		except:
			pass
		return

class Theorem122(Theorem):
	def __init__(self):
		super(Theorem122, self).__init__(122, "if edges >= nodes**2/4 then {edgeCliqueCover <= ((1/2)*nodes*(nodes-1) - edges) + (1 + sqrt(1 + 4*((1/2)*nodes*(nodes-1) - edges)))};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodes"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (edges_Min>=nodes_Max**2.0/4.0)):
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
		genus_Min = ingrid_obj.get('genus', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind = 'Min')
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		
		if (genus_Min>=1.0) and (girth_Min == girth_Max):
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.25*girth-(1.25), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.444444444444444*nodes+0.555555555555556, ind='Max')
				except:
					pass
		elif (True):
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.25*girth-(2.25), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.444444444444444*nodes+1.0, ind='Max')
				except:
					pass
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
		super(Theorem129, self).__init__(129, "if defined girth and girth > 3 then {mindeg <= (nodes - diam + 3*(diam/3 + 1) -3)/ (diam/3+1)};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Max != 'undt') and (girth_Min>3.0):
			diam = ingrid_obj.get('diam', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*nodes/(0.333333333333333*diam+1.0), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diam', -(3.0)+3.0*nodes/mindeg, ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg*(0.333333333333333*diam+1.0), ind='Min')
			except:
				pass
		return

class Theorem130(Theorem):
	def __init__(self):
		super(Theorem130, self).__init__(130, "if diam == 2 and nodes >= maxdeg * maxdeg / 8 then {edges >= nodes *(nodes - 1)/(2 * maxdeg)} else if diam == 2 and nodes < maxdeg * maxdeg /8 then {edges >= maxdeg * nodes * (nodes - 1)/ (maxdeg * maxdeg + 8*nodes)};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","edges","maxdeg","nodes"]
	def run(self, ingrid_obj):
		diam_Min = ingrid_obj.get('diam', ind='Min')
		diam_Max = ingrid_obj.get('diam', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (diam_Max==diam_Min and (diam_Min==2.0)) and (maxdeg_Max != 'undt' and (nodes_Min>=maxdeg_Max*maxdeg_Max/8.0)):
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
		elif (diam_Max==diam_Min and (diam_Min==2.0)) and (nodes_Max != 'undt' and (nodes_Max<maxdeg_Min*maxdeg_Min/8.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*maxdeg*nodes*(nodes-(1.0))/(1.0*maxdeg**2.0+8.0*nodes), ind='Min')
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
				ingrid_obj.set('chromaticNum', 1.0*maxdeg-(1.0)+1.0*maxdeg/max(4.0, maxClique+1.0)+1.0/max(4.0, maxClique+1.0), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(chromaticNum*max(4.0, maxClique+1.0)+max(4.0, maxClique+1.0)-(1.0))/(max(4.0, maxClique+1.0)+1.0), ind='Min')
			except:
				pass
		return

class Theorem132(Theorem):
	def __init__(self):
		super(Theorem132, self).__init__(132, "if istrue congruent(nodes, 3, 4) then {mindeg <= (nodes-1)**2 / (4*(nodes-1-maxdeg))} else {mindeg <= (nodes-3)*(nodes+1)/(4*(nodes-1-maxdeg))};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		
		if (nodes_Min == nodes_Max):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('mindeg', -(0.25*(nodes-(1.0))**2.0/(maxdeg-(nodes)+1.0)), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(1.0)-(0.25*(nodes-(1.0))**2.0/mindeg), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (-((1.0))+nodes)**2.0/(4.0*(-((maxdeg))-((1.0))+nodes)), ind='Max')
				except:
					pass
		elif (True):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.25*(-(1.0*nodes**2.0)+2.0*nodes+3.0)/(maxdeg-(nodes)+1.0), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', (1.0*mindeg*nodes-(1.0*mindeg)-(0.25*nodes**2.0)+0.5*nodes+0.75)/mindeg, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*mindeg+2.0*(mindeg**2.0-(mindeg*maxdeg)+1.0)**(1/2)+1.0, ind='Min')
				except:
					pass
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
		super(Theorem134, self).__init__(134, "if radius == 2 and diam == 2 and nodes == 4 then {edges >= 4} else if radius == 2 and diam == 2 and nodes >= 5 then {edges >= 2*nodes - 5};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","edges","nodes","radius"]
	def run(self, ingrid_obj):
		radius_Min = ingrid_obj.get('radius', ind='Min')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		diam_Min = ingrid_obj.get('diam', ind='Min')
		diam_Max = ingrid_obj.get('diam', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (radius_Max==radius_Min and (radius_Min==2.0)) and (diam_Max==diam_Min and (diam_Min==2.0)) and (nodes_Max==nodes_Min and (nodes_Min==4.0)):
			try:
				ingrid_obj.set('edges', 4.0, ind='Min')
			except:
				pass
		elif (radius_Max==radius_Min and (radius_Min==2.0)) and (diam_Max==diam_Min and (diam_Min==2.0)) and (nodes_Min>=5.0):
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
		super(Theorem137, self).__init__(137, "if defined diam then {edges >= nodes * (nodes - 1)*(maxdeg - 2)/(2*((maxdeg-1)**diam - 1))};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","edges","maxdeg","nodes"]
	def run(self, ingrid_obj):
		diam_Max = ingrid_obj.get('diam', ind = 'Max')
		if (diam_Max != 'undt'):
			diam = ingrid_obj.get('diam', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diam != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*nodes*(maxdeg*nodes-(1.0*maxdeg)-(2.0*nodes)+2.0)/((maxdeg-(1.0))**diam-(1.0)), ind='Min')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', nodes*(-((1.0))+nodes)*(-((2.0))+maxdeg)/(2.0*(-((1.0))+(-((1.0))+maxdeg)**diam)), ind='Min')
			except:
				pass
			diam = ingrid_obj.get('diam', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', nodes*(-((1.0))+nodes)*(-((2.0))+maxdeg)/(2.0*(-((1.0))+(-((1.0))+maxdeg)**diam)), ind='Min')
			except:
				pass
			diam = ingrid_obj.get('diam', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', (1.0*maxdeg+(2.0*edges*(4.0*maxdeg-(8.0))*((maxdeg-(1.0))**diam-(1.0))+(1.0*maxdeg-(2.0))**2.0)**(1/2)-(2.0))/(2.0*maxdeg-(4.0)), ind='Min')
			except:
				pass
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
			nodes = ingrid_obj.get('nodes', ind='Min')
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

