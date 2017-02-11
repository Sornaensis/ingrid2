class Theorem321(Theorem):
	def __init__(self):
		super(Theorem321, self).__init__(321, "if connected and regular and not complete and mindeg <= 3 then {edgeCliqueCover >= 3*nodes/(mindeg+1)} else if connected and regular and not complete and mindeg >= 5 then {edgeCliqueCover >= mindeg*nodes/((mindeg+1)*(mindeg-2))};", "")
	def involves(self, str_invar):
		return str_invar in ["complete","connected","edgeCliqueCover","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		regular = ingrid_obj.get('regular')
		complete = ingrid_obj.get('complete')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (connected == True) and (regular == True) and (complete == False) and (mindeg_Max != 'undt' and (mindeg_Max<=3.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('edgeCliqueCover', 3.0*nodes/(mindeg+1.0), ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edgeCliqueCover != 'undt':
				try:
					ingrid_obj.set('mindeg', -(1.0)+3.0*nodes/edgeCliqueCover, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if edgeCliqueCover != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 0.333333333333333*edgeCliqueCover*(mindeg+1.0), ind='Max')
				except:
					pass
		elif (connected == True) and (regular == True) and (complete == False) and (mindeg_Min>=5.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0*mindeg*nodes/(1.0*mindeg**2.0-(1.0*mindeg)-(2.0)), ind='Min')
			except:
				pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edgeCliqueCover != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*(edgeCliqueCover+nodes+(9.0*edgeCliqueCover**2.0+2.0*edgeCliqueCover*nodes+1.0*nodes**2.0)**(1/2))/edgeCliqueCover, ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', edgeCliqueCover*(1.0*mindeg**2.0-(1.0*mindeg)-(2.0))/mindeg, ind='Min')
			except:
				pass
		return

class Theorem322(Theorem):
	def __init__(self):
		super(Theorem322, self).__init__(322, "if connected and regular and mindeg <= 4 and not complete and (nodes == 7 or istrue congruent(nodes, 3, 5)) and ((nodes > 13 or nodes < 13) and (nodes > 18 or nodes < 18)) then {edgeCliqueCover >= floor((3*nodes+4)/5) + 1} else if connected and regular and mindeg <= 4 and not complete then {edgeCliqueCover >= floor((3*nodes+4)/5)};", "")
	def involves(self, str_invar):
		return str_invar in ["complete","connected","edgeCliqueCover","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		regular = ingrid_obj.get('regular')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		complete = ingrid_obj.get('complete')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		if (connected == True) and (regular == True) and (mindeg_Max != 'undt' and (mindeg_Max<=4.0)) and (complete == False) and (nodes_Max==nodes_Min and (nodes_Min==7.0)) or (nodes_Min == nodes_Max) and (nodes_Min>13.0) or (nodes_Max != 'undt' and (nodes_Max<13.0)) and (nodes_Min>18.0) or (nodes_Max != 'undt' and (nodes_Max<18.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0*floor((3.0*nodes+4.0)/5.0)+1.0, ind='Min')
			except:
				pass
		elif (connected == True) and (regular == True) and (mindeg_Max != 'undt' and (mindeg_Max<=4.0)) and (complete == False):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeCliqueCover', floor((3.0*nodes+4.0)/5.0), ind='Min')
			except:
				pass
		return

class Theorem323(Theorem):
	def __init__(self):
		super(Theorem323, self).__init__(323, "if girth >= 6 then {nodeInd >= (2*maxdeg-1)*nodes/(maxdeg*maxdeg + 2*maxdeg - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=6.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', nodes*(2.0*maxdeg-(1.0))/(1.0*maxdeg**2.0+2.0*maxdeg-(1.0)), ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeInd)+nodes+((nodeInd-(nodes))*(2.0*nodeInd-(nodes)))**(1/2))/nodeInd, ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxdeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', nodeInd*(1.0*maxdeg**2.0+2.0*maxdeg-(1.0))/(2.0*maxdeg-(1.0)), ind='Max')
				except:
					pass
		return

class Theorem324(Theorem):
	def __init__(self):
		super(Theorem324, self).__init__(324, "if mindeg == maxdeg and maxdeg == 3 and girth >= 6 then {nodeInd >= 19*nodes/52} else if mindeg == maxdeg and maxdeg == 3 and girth >= 8 then {nodeInd >= 20*nodes/52};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (girth_Min>=6.0):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.365384615384615*nodes, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.73684210526316*nodeInd, ind='Max')
				except:
					pass
		elif (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (girth_Min>=8.0):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.384615384615385*nodes, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.6*nodeInd, ind='Max')
				except:
					pass
		return

class Theorem325(Theorem):
	def __init__(self):
		super(Theorem325, self).__init__(325, "if regular and even girth  and girth >= 6 and connected and nodes <= (mindeg*(mindeg-3)+2*(mindeg-1)**(girth/2))/(mindeg-2) then {bipartite and diameter == girth/2 + 1};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","connected","diameter","girth","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		connected = ingrid_obj.get('connected')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (regular == True) and (even(girth_Min) and even(girth_Max)) and (girth_Min>=6.0) and (connected == True) and (nodes_Max != 'undt' and (nodes_Max<=(mindeg_Min*(mindeg_Min-(3.0))+2.0*(mindeg_Min-(1.0))**(girth_Min/2.0))/(mindeg_Min-(2.0)))):
			ingrid_obj.set('bipartite', True)
			girth = ingrid_obj.get('girth', ind='Max')
			if girth != 'undt':
				try:
					ingrid_obj.set('diameter', girth/2.0+1.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('diameter', girth/2.0+1.0, ind='Min')
			except:
				pass
		return

class Theorem326(Theorem):
	def __init__(self):
		super(Theorem326, self).__init__(326, "if bipartite and odd nodes  then {thickness <= ceil((nodes*nodes - 1)/(2*(nodes - 2)))};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","nodes","thickness"]
	def run(self, ingrid_obj):
		bipartite = ingrid_obj.get('bipartite')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (bipartite == True) and (odd(nodes_Min) and odd(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('thickness', ceil((nodes*nodes-(1.0))/(2.0*(nodes-(2.0)))), ind='Max')
				except:
					pass
		return

class Theorem327(Theorem):
	def __init__(self):
		super(Theorem327, self).__init__(327, "if edges >= 1 then {maxdeg >= 2*thickness - 1};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","thickness"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		if (edges_Min>=1.0):
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 2.0*thickness-(1.0), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('thickness', 0.5*maxdeg+0.5, ind='Max')
				except:
					pass
		return

class Theorem328(Theorem):
	def __init__(self):
		super(Theorem328, self).__init__(328, "nodeConnec <= 3*thickness - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["nodeConnec","thickness"]
	def run(self, ingrid_obj):
		thickness = ingrid_obj.get('thickness', ind='Max')
		if thickness != 'undt':
			try:
				ingrid_obj.set('nodeConnec', 3.0*thickness-(1.0), ind='Max')
			except:
				pass
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		try:
			ingrid_obj.set('thickness', 0.333333333333333*nodeConnec+0.333333333333333, ind='Min')
		except:
			pass
		return

class Theorem329(Theorem):
	def __init__(self):
		super(Theorem329, self).__init__(329, "if mindeg == maxdeg and maxdeg == 3 and girth == 10 then {nodes >= 70};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (girth_Max==girth_Min and (girth_Min==10.0)):
			try:
				ingrid_obj.set('nodes', 70.0, ind='Min')
			except:
				pass
		return

class Theorem330(Theorem):
	def __init__(self):
		super(Theorem330, self).__init__(330, "if edges >= max(((nodes - mindeg)*(nodes - mindeg - 1))/2 + mindeg*mindeg + 1, (floor((nodes+2)/2)*(floor((nodes+2)/2)-1))/2 + floor((nodes-1)/2)**2 +1) then {hamiltonian};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","hamiltonian","mindeg","nodes"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>=max(((nodes_Max-(mindeg_Max))*(nodes_Max-(mindeg_Max)-(1.0)))/2.0+mindeg_Max*mindeg_Max+1.0, (floor((nodes_Max+2.0)/2.0)*(floor((nodes_Max+2.0)/2.0)-(1.0)))/2.0+floor((nodes_Max-(1.0))/2.0)**2.0+1.0))):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem331(Theorem):
	def __init__(self):
		super(Theorem331, self).__init__(331, "edges <= nodes*(nodes-1)/2 - (mindeg - nodeConnec + 1)*(nodes - mindeg - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 1.0*mindeg**2.0-(1.0*mindeg*nodeConnec)-(1.0*mindeg*nodes)+2.0*mindeg+1.0*nodeConnec*nodes-(1.0*nodeConnec)+0.5*nodes**2.0-(1.5*nodes)+1.0, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('mindeg', 1.0*(0.5*nodeConnec+0.5*nodes-(1.0))+0.5*(4.0*edges+1.0*nodeConnec**2.0-(2.0*nodeConnec*nodes)-(1.0*nodes**2.0)+2.0*nodes)**(1/2), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeConnec', 1.0*(-(1.0*edges)+1.0*mindeg**2.0-(1.0*mindeg*nodes)+2.0*mindeg+0.5*nodes**2.0-(1.5*nodes)+1.0)/(mindeg-(nodes)+1.0), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		if edges != 'undt' and mindeg != 'undt' and nodeConnec != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*(1.0*mindeg-(1.0*nodeConnec)+1.5)+1.0*(2.0*edges-(1.0*mindeg**2.0)-(1.0*mindeg)+1.0*nodeConnec**2.0-(1.0*nodeConnec)+0.25)**(1/2), ind='Max')
			except:
				pass
		return

class Theorem332(Theorem):
	def __init__(self):
		super(Theorem332, self).__init__(332, "if tree and maxdeg <= nodes - 2 then {bandwidth <= (nodes - 1)/2};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","maxdeg","nodes","tree"]
	def run(self, ingrid_obj):
		tree = ingrid_obj.get('tree')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (tree == True) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('bandwidth', 0.5*nodes-(0.5), ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*bandwidth+1.0, ind='Min')
			except:
				pass
		return

class Theorem333(Theorem):
	def __init__(self):
		super(Theorem333, self).__init__(333, "edges >= 2*bandwidth - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","edges"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		try:
			ingrid_obj.set('edges', 2.0*bandwidth-(1.0), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		if edges != 'undt':
			try:
				ingrid_obj.set('bandwidth', 0.5*edges+0.5, ind='Max')
			except:
				pass
		return

class Theorem334(Theorem):
	def __init__(self):
		super(Theorem334, self).__init__(334, "if connected and mindeg >= 3 and girth >= 5 then {domination <= (nodes - floor(diameter/3)*(mindeg - 1) - 1 - (mindeg-1)*(mindeg-2)/2)/2};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","domination","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (connected == True) and (mindeg_Min>=3.0) and (girth_Min>=5.0):
			diameter = ingrid_obj.get('diameter', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diameter != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.5*floor(diameter/3.0)*mindeg)+0.5*floor(diameter/3.0)-(0.25*mindeg**2.0)+0.75*mindeg+0.5*nodes-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			domination = ingrid_obj.get('domination', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*domination+1.0*floor(diameter/3.0)*mindeg-(1.0*floor(diameter/3.0))+0.5*mindeg**2.0-(1.5*mindeg)+2.0, ind='Min')
			except:
				pass
		return

class Theorem335(Theorem):
	def __init__(self):
		super(Theorem335, self).__init__(335, "if bandwidth >= nodes/2 then {edges >= (2*floor(nodes/2) - 1)*(nodes/(nodes - 2))**(bandwidth - floor(nodes/2))};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodes"]
	def run(self, ingrid_obj):
		bandwidth_Min = ingrid_obj.get('bandwidth', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (bandwidth_Min>=nodes_Max/2.0)):
		return

class Theorem336(Theorem):
	def __init__(self):
		super(Theorem336, self).__init__(336, "if bandwidth >= nodes/2 then {edges >= nodes*(nodes - 1)/(2*(nodes - bandwidth))};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","edges","nodes"]
	def run(self, ingrid_obj):
		bandwidth_Min = ingrid_obj.get('bandwidth', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (bandwidth_Min>=nodes_Max/2.0)):
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if bandwidth != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*nodes*(-(nodes)+1.0)/(bandwidth-(nodes)), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('bandwidth', nodes*(1.0*edges-(0.5*nodes)+0.5)/edges, ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			edges = ingrid_obj.get('edges', ind='Max')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edges+0.5*(4.0*edges**2.0-(8.0*edges*bandwidth)+4.0*edges+1.0)**(1/2)+0.5, ind='Max')
				except:
					pass
		return

class Theorem337(Theorem):
	def __init__(self):
		super(Theorem337, self).__init__(337, "if girth >= 5 then {domination <= (2*nodes - (mindeg - 1)*(4*edges/nodes - mindeg - 2))/4};", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edges","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=5.0):
			edges = ingrid_obj.get('edges', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(1.0*edges*mindeg/nodes)+1.0*edges/nodes+0.25*mindeg**2.0+0.25*mindeg+0.5*nodes-(0.5), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 4.0*nodes*(-(0.25*domination)+6.25e-2*mindeg**2.0+6.25e-2*mindeg+0.125*nodes-(0.125))/(mindeg-(1.0)), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*(4.0*edges-(1.0*nodes))/nodes+0.5*(16.0*domination*nodes**2.0+16.0*edges**2.0-(24.0*edges*nodes)-(8.0*nodes**3.0)+9.0*nodes**2.0)**(1/2)/nodes, ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*domination-(0.25*mindeg**2.0)-(0.25*mindeg)+1.0*(1.0*domination**2.0-(0.5*domination*mindeg**2.0)-(0.5*domination*mindeg)+1.0*domination+2.0*edges*mindeg-(2.0*edges)+6.25e-2*mindeg**4.0+0.125*mindeg**3.0-(0.1875*mindeg**2.0)-(0.25*mindeg)+0.25)**(1/2)+0.5, ind='Min')
			except:
				pass
		return

class Theorem338(Theorem):
	def __init__(self):
		super(Theorem338, self).__init__(338, "if connected and girth >= 5 and mindeg >= 4 then {domination <= (nodes - maxdeg - mindeg*(mindeg - 3)/3)/2};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","domination","girth","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (connected == True) and (girth_Min>=5.0) and (mindeg_Min>=4.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.5*maxdeg)-(0.166666666666667*mindeg**2.0)+0.5*mindeg+0.5*nodes, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(2.0*domination)-(0.333333333333333*mindeg**2.0)+1.0*mindeg+1.0*nodes, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.5*maxdeg)-(0.166666666666667*mindeg**2.0)+0.5*mindeg+0.5*nodes, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*domination+1.0*maxdeg+0.333333333333333*mindeg**2.0-(1.0*mindeg), ind='Min')
			except:
				pass
		return

class Theorem339(Theorem):
	def __init__(self):
		super(Theorem339, self).__init__(339, "if girth >= 5 then {domination >= mindeg*numOfComponents};", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","mindeg","numOfComponents"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=5.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('domination', mindeg*numOfComponents, ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if domination != 'undt':
				try:
					ingrid_obj.set('mindeg', domination/numOfComponents, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			if domination != 'undt':
				try:
					ingrid_obj.set('numOfComponents', domination/mindeg, ind='Max')
				except:
					pass
		return

class Theorem340(Theorem):
	def __init__(self):
		super(Theorem340, self).__init__(340, "if girth >= 6 then {domination >= 2*(mindeg - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","mindeg"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=6.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('domination', 2.0*mindeg-(2.0), ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Max')
			if domination != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*domination+1.0, ind='Max')
				except:
					pass
		return

