class Theorem161(Theorem):
	def __init__(self):
		super(Theorem161, self).__init__(161, "if genus > 2 and girth >= 4 and mindeg >= (5 + (16*genus + 1)**(1/2))/2 and mindeg == (3 + (16*genus + 9)**(1/2))/2 then { regular, hamiltonian, nodes == 2*mindeg+2 } else if genus > 2 and girth >= 4 and mindeg >= (5 + (16*genus + 1)**(1/2))/2 then { regular, hamiltonian, nodes == 2*mindeg }; ", "")
	def involves(self, str_invar):
		return str_invar in ["genus","girth","hamiltonian","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		genus_Max = ingrid_obj.get('genus', ind='Max')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (genus_Min>2.0) and (girth_Min>=4.0) and (genus_Max != 'undt' and (mindeg_Min>=(5.0+(16.0*genus_Max+1.0)**(1.0/2.0))/2.0)) and (mindeg_Max != 'undt' and (mindeg_Max<=(3.0+(16.0*genus_Min+9.0)**(1.0/2.0))/2.0)) and (genus_Max != 'undt' and (mindeg_Min>=(3.0+(16.0*genus_Max+9.0)**(1.0/2.0))/2.0)):
			ingrid_obj.set('regular', True)
			ingrid_obj.set('hamiltonian', True)
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*mindeg+2.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*mindeg+2.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*nodes-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*nodes-(1.0), ind='Min')
			except:
				pass
		elif (genus_Min>2.0) and (girth_Min>=4.0) and (genus_Max != 'undt' and (mindeg_Min>=(5.0+(16.0*genus_Max+1.0)**(1.0/2.0))/2.0)):
			ingrid_obj.set('regular', True)
			ingrid_obj.set('hamiltonian', True)
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*mindeg, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*mindeg, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*nodes, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*nodes, ind='Min')
			except:
				pass
		return

class Theorem162(Theorem):
	def __init__(self):
		super(Theorem162, self).__init__(162, "if nodeConnec >= 2 and regular and ((even nodes and mindeg >= (nodes-(2*nodes)**(1/2))/2) or (odd nodes and mindeg >= (nodes - nodes**(1/2))/2)) then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","mindeg","nodeConnec","nodes","regular"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		regular = ingrid_obj.get('regular')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (nodeConnec_Min>=2.0) and (regular == True) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (mindeg_Min>=(nodes_Max-((2.0*nodes_Max)**(1.0/2.0)))/2.0)) or (odd(nodes_Min) and odd(nodes_Max)) and (nodes_Max != 'undt' and (mindeg_Min>=(nodes_Max-(nodes_Max**(1.0/2.0)))/2.0)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem163(Theorem):
	def __init__(self):
		super(Theorem163, self).__init__(163, "if regular and nodeConnec >= 2 and nodes <= 3*mindeg then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","mindeg","nodeConnec","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (regular == True) and (nodeConnec_Min>=2.0) and (nodes_Max != 'undt' and (nodes_Max<=3.0*mindeg_Min)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem164(Theorem):
	def __init__(self):
		super(Theorem164, self).__init__(164, "if spectralRadius > edges**(1/2) then { girth == 3 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","spectralRadius"]
	def run(self, ingrid_obj):
		spectralRadius_Min = ingrid_obj.get('spectralRadius', ind='Min')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		if (edges_Max != 'undt' and (spectralRadius_Min>edges_Max**(1.0/2.0))):
			try:
				ingrid_obj.set('girth', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('girth', 3.0, ind='Min')
			except:
				pass
		return

class Theorem165(Theorem):
	def __init__(self):
		super(Theorem165, self).__init__(165, "spectralRadius >= maxdeg**(1/2);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","spectralRadius"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		try:
			ingrid_obj.set('spectralRadius', maxdeg**0.5, ind='Min')
		except:
			pass
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('maxdeg', spectralRadius**2.0, ind='Max')
			except:
				pass
		return

class Theorem166(Theorem):
	def __init__(self):
		super(Theorem166, self).__init__(166, "if diameter > 1 and nodeConnec > 1 then { edges >= (nodes*diameter-2*diameter + 1)/(diameter - 1) };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (diameter_Min>1.0) and (nodeConnec_Min>1.0):
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*(1.0*diameter*nodes-(2.0*diameter)+1.0)/(diameter-(1.0)), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('diameter', 1.0*(edges+1.0)/(1.0*edges-(1.0*nodes)+2.0), ind='Min')
			except:
				pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			edges = ingrid_obj.get('edges', ind='Max')
			if diameter != 'undt' and edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edges-(1.0*edges/diameter)+2.0-(1.0/diameter), ind='Max')
				except:
					pass
		return

class Theorem167(Theorem):
	def __init__(self):
		super(Theorem167, self).__init__(167, "if girth >= 5 then { chromaticNum <= (maxdeg + 3)*2/3 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","girth","maxdeg"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=5.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.666666666666667*maxdeg+2.0, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 1.5*chromaticNum-(3.0), ind='Min')
			except:
				pass
		return

class Theorem168(Theorem):
	def __init__(self):
		super(Theorem168, self).__init__(168, "if girth >= 2*maxdeg**2 then { chromaticNum <= (maxdeg + 4)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","girth","maxdeg"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxdeg_Max != 'undt' and (girth_Min>=2.0*maxdeg_Max**2.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.5*maxdeg+2.0, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 2.0*chromaticNum-(4.0), ind='Min')
			except:
				pass
		return

class Theorem169(Theorem):
	def __init__(self):
		super(Theorem169, self).__init__(169, "nodeInd >= nodes**2/(2*edges + nodes);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodes**2.0/(2.0*edges+nodes), ind='Min')
			except:
				pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', -(0.5*nodes)+0.5*nodes**2.0/nodeInd, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodes**2.0/(nodes+2.0*edges), ind='Min')
			except:
				pass
		return

class Theorem170(Theorem):
	def __init__(self):
		super(Theorem170, self).__init__(170, "if connected and not complete then { nodeInd >= (nodes**3 + 3*nodes + 1)/(nodes*(2*edges+nodes)) };", "")
	def involves(self, str_invar):
		return str_invar in ["complete","connected","edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		complete = ingrid_obj.get('complete')
		if (connected == True) and (complete == False):
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodeInd', (3.0*nodes+nodes**3.0+1.0)/(nodes*(2.0*edges+nodes)), ind='Min')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('edges', -(0.5*nodes)+0.5*nodes**2.0/nodeInd+1.5/nodeInd+0.5/(nodeInd*nodes), ind='Min')
				except:
					pass
		return

class Theorem171(Theorem):
	def __init__(self):
		super(Theorem171, self).__init__(171, "if genus > 1 and girth >= 4 then { mindeg <= 2 + 2*genus**(1/2) };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","girth","mindeg"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (genus_Min>1.0) and (girth_Min>=4.0):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('mindeg', 2.0*genus**0.5+2.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*(0.5*mindeg-(1.0))**2.0, ind='Min')
			except:
				pass
		return

class Theorem172(Theorem):
	def __init__(self):
		super(Theorem172, self).__init__(172, "if connected then { diameter <= 2*nodeCover };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","nodeCover"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('diameter', 2.0*nodeCover, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('nodeCover', 0.5*diameter, ind='Min')
			except:
				pass
		return

class Theorem173(Theorem):
	def __init__(self):
		super(Theorem173, self).__init__(173, "nodeInd >= 2*nodes/(maxdeg + maxClique + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodeInd', 2.0*nodes/(maxClique+maxdeg+1.0), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxClique', -(1.0*maxdeg)-(1.0)+2.0*nodes/nodeInd, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0*maxClique)-(1.0)+2.0*nodes/nodeInd, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 0.5*nodeInd*(maxClique+maxdeg+1.0), ind='Max')
			except:
				pass
		return

class Theorem174(Theorem):
	def __init__(self):
		super(Theorem174, self).__init__(174, "nodeInd >= (nodes + 2*maxdeg + 1 - maxClique - mindeg)/(maxdeg + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('nodeInd', 1.0*(-(1.0*maxClique)+2.0*maxdeg-(1.0*mindeg)+1.0*nodes+1.0)/(maxdeg+1.0), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if mindeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxClique', -(1.0*nodeInd*maxdeg)-(1.0*nodeInd)+2.0*maxdeg-(1.0*mindeg)+1.0*nodes+1.0, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and mindeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeInd)-(maxClique)-(mindeg)+nodes+1.0)/(1.0*nodeInd-(2.0)), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('mindeg', -(1.0*nodeInd*maxdeg)-(1.0*nodeInd)-(1.0*maxClique)+2.0*maxdeg+1.0*nodes+1.0, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and mindeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*nodeInd*maxdeg+1.0*nodeInd+1.0*maxClique-(2.0*maxdeg)+1.0*mindeg-(1.0), ind='Max')
			except:
				pass
		return

class Theorem175(Theorem):
	def __init__(self):
		super(Theorem175, self).__init__(175, "bandwidth >= (1/2)*(2*nodes-1-sqrt((2*nodes-1)**2-8*edges));", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","edges","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('bandwidth', 1.0*nodes-(0.5*(-(8.0*edges)+(2.0*nodes-(1.0))**2.0)**0.5)-(0.5), ind='Min')
		except:
			pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if bandwidth != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.125*(2.0*nodes-(1.0))**2.0-(0.125*(-(2.0*bandwidth)+2.0*nodes-(1.0))**2.0), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('bandwidth', (1.0/2.0)*(-((((2.0*nodes-((1.0)))**2.0-((8.0*edges)))**(1.0/2.0)))-((1.0))+2.0*nodes), ind='Min')
		except:
			pass
		return

class Theorem176(Theorem):
	def __init__(self):
		super(Theorem176, self).__init__(176, "if maxClique == 2 then { bandwidth >= (1/2)*(3*mindeg-1) };", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","maxClique","mindeg"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('bandwidth', 1.5*mindeg-(0.5), ind='Min')
			except:
				pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			if bandwidth != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.666666666666667*bandwidth+0.333333333333333, ind='Max')
				except:
					pass
		return

class Theorem177(Theorem):
	def __init__(self):
		super(Theorem177, self).__init__(177, "null;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodes","tree"]
	def run(self, ingrid_obj):
		return

class Theorem178(Theorem):
	def __init__(self):
		super(Theorem178, self).__init__(178, "nodeCliqueCover <= nodes - mindeg - (nodes - mindeg)/max(4,nodeInd + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', -(mindeg)+nodes+mindeg/max(4.0, nodeInd+1.0)-(nodes/max(4.0, nodeInd+1.0)), ind='Max')
			except:
				pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeCliqueCover != 'undt' and nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', (-(nodeCliqueCover*max(4.0, nodeInd+1.0))+max(4.0, nodeInd+1.0)*nodes-(nodes))/(max(4.0, nodeInd+1.0)-(1.0)), ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', (nodeCliqueCover*max(4.0, nodeInd+1.0)+max(4.0, nodeInd+1.0)*mindeg-(mindeg))/(max(4.0, nodeInd+1.0)-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem179(Theorem):
	def __init__(self):
		super(Theorem179, self).__init__(179, "if domination >= 2 then { edges <= (1/2)*(nodes-nodeInd)*(nodes+nodeInd-2*domination + 2) };", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		domination_Min = ingrid_obj.get('domination', ind='Min')
		if (domination_Min>=2.0):
			domination = ingrid_obj.get('domination', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if domination != 'undt' and nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 1.0*domination*nodeInd-(1.0*domination*nodes)-(0.5*nodeInd**2.0)-(1.0*nodeInd)+0.5*nodes**2.0+1.0*nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', 2.0*(0.5*edges+0.25*nodeInd**2.0+0.5*nodeInd-(0.25*nodes**2.0)-(0.5*nodes))/(nodeInd-(nodes)), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*domination+1.0*(2.0*edges+1.0*domination**2.0-(2.0*domination*nodeInd)-(2.0*domination)+1.0*nodeInd**2.0+2.0*nodeInd+1.0)**(1/2)-(1.0), ind='Min')
			except:
				pass
		return

class Theorem180(Theorem):
	def __init__(self):
		super(Theorem180, self).__init__(180, "if regular and maxdeg >= nodes / 2 and maxdeg <= nodes - 2 and ((odd nodes and even maxdeg) or (odd maxdeg and even nodes)) then { chromaticNum <= min(maxdeg, 3*nodes/5) } else if regular and maxdeg >= nodes/2 and maxdeg <= nodes - 2 then { chromaticNum <= min(maxdeg, (2*(nodes-maxdeg)-3)*nodes/(3*(nodes-maxdeg)-4)) };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxdeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (regular == True) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max/2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))) and (odd(nodes_Min) and odd(nodes_Max)) and (even(maxdeg_Min) and even(maxdeg_Max)) or (odd(maxdeg_Min) and odd(maxdeg_Max)) and (even(nodes_Min) and even(nodes_Max)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', min(maxdeg, 3.0*nodes/5.0), ind='Max')
				except:
					pass
		elif (regular == True) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max/2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', min(maxdeg, (2.0*(nodes-(maxdeg))-(3.0))*nodes/(3.0*(nodes-(maxdeg))-(4.0))), ind='Max')
				except:
					pass
		return

