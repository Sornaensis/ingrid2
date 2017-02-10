TypeError('unorderable types: float() <= complex()',)
SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
TypeError('unorderable types: float() <= complex()',)
class Theorem441(Theorem):
	def __init__(self):
		super(Theorem441, self).__init__(441, "if maxdeg >= 6 and maxClique <= maxdeg - 1 then {nodeCover <=  (nodes * (maxdeg - 1) -1)/maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxdeg_Min>=6.0) and (maxClique_Max != 'undt' and (maxClique_Max<=maxdeg_Min-(1.0))):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 1.0*(maxdeg*nodes-(nodes)-(1.0))/maxdeg, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('maxdeg', -((1.0*nodes+1.0)/(nodeCover-(nodes))), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*(nodeCover*maxdeg+1.0)/(maxdeg-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem442(Theorem):
	def __init__(self):
		super(Theorem442, self).__init__(442, "if maxClique == 2 then {nodeCover <= nodes *(1 - ((2*edges)/nodes * log(2*edges/nodes) - (2*edges/nodes) +1)/(2*edges/nodes -1)**2)};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 1.0*(2.0*edges/nodes-(1.0))**(-(2.0))*(-(2.0*edges*log(edges/nodes))+0.613705638880109*edges+1.0*nodes*(2.0*edges/nodes-(1.0))**2.0-(1.0*nodes)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodes*(-(((1.0-(((2.0*edges/nodes)))+(2.0*edges)/nodes*log(2.0*edges/nodes))/(-((1.0))+2.0*edges/nodes)**2.0))+1.0), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodes*(-(((1.0-(((2.0*edges/nodes)))+(2.0*edges)/nodes*log(2.0*edges/nodes))/(-((1.0))+2.0*edges/nodes)**2.0))+1.0), ind='Max')
				except:
					pass
		return

class Theorem443(Theorem):
	def __init__(self):
		super(Theorem443, self).__init__(443, "bandwidth <= nodes - (mindeg + 1)*(numOfComponents -1) - 1 - (nodes - nodeCover - numOfComponents + 1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","mindeg","nodeCover","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('bandwidth', -(1.0*mindeg*numOfComponents)+1.0*mindeg+0.5*nodeCover+0.5*nodes-(0.5*numOfComponents)-(0.5), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*(-(1.0*bandwidth)+0.5*nodeCover+0.5*nodes-(0.5*numOfComponents)-(0.5))/(numOfComponents-(1.0)), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 2.0*bandwidth+2.0*mindeg*numOfComponents-(2.0*mindeg)-(1.0*nodes)+1.0*numOfComponents+1.0, ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*bandwidth+2.0*mindeg*numOfComponents-(2.0*mindeg)-(1.0*nodeCover)+1.0*numOfComponents+1.0, ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('numOfComponents', (-(1.0*bandwidth)+1.0*mindeg+0.5*nodeCover+0.5*nodes-(0.5))/(1.0*mindeg+0.5), ind='Max')
			except:
				pass
		return

class Theorem444(Theorem):
	def __init__(self):
		super(Theorem444, self).__init__(444, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem445(Theorem):
	def __init__(self):
		super(Theorem445, self).__init__(445, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem446(Theorem):
	def __init__(self):
		super(Theorem446, self).__init__(446, "if maxClique <= 2 and maxdeg <= 3 then {edges >= 14*nodeCover - 15*nodes/2};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=3.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 14.0*nodeCover-(7.5*nodes), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 7.14285714285714e-2*edges+0.535714285714286*nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', -(0.133333333333333*edges)+1.86666666666667*nodeCover, ind='Min')
				except:
					pass
		return

class Theorem447(Theorem):
	def __init__(self):
		super(Theorem447, self).__init__(447, "if maxClique <= 2 and maxdeg <= 2 then {edges >= 15*nodeCover - 8*nodes};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)) and (maxdeg_Max != 'undt' and (maxdeg_Max<=2.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 15.0*nodeCover-(8.0*nodes), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 6.66666666666667e-2*edges+0.533333333333333*nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', -(0.125*edges)+1.875*nodeCover, ind='Min')
				except:
					pass
		return

class Theorem448(Theorem):
	def __init__(self):
		super(Theorem448, self).__init__(448, "edges <= ((nodes - nodeCliqueCover)*(nodeCliqueCover + maxdeg - 1) + mindeg)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","mindeg","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodeCliqueCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', -(0.5*maxdeg*nodeCliqueCover)+0.5*maxdeg*nodes+0.5*mindeg-(0.5*nodeCliqueCover**2.0)+0.5*nodeCliqueCover*nodes+0.5*nodeCliqueCover-(0.5*nodes), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodeCliqueCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', 2.0*(-(1.0*edges)+0.5*mindeg-(0.5*nodeCliqueCover**2.0)+0.5*nodeCliqueCover*nodes+0.5*nodeCliqueCover-(0.5*nodes))/(nodeCliqueCover-(nodes)), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('mindeg', 2.0*edges+1.0*maxdeg*nodeCliqueCover-(1.0*maxdeg*nodes)+1.0*nodeCliqueCover**2.0-(1.0*nodeCliqueCover*nodes)-(1.0*nodeCliqueCover)+1.0*nodes, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		if mindeg != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*maxdeg*nodeCliqueCover-(0.5*mindeg)+0.5*nodeCliqueCover**2.0-(0.5*nodeCliqueCover))/(maxdeg+nodeCliqueCover-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem449(Theorem):
	def __init__(self):
		super(Theorem449, self).__init__(449, "if nodeInd == 2 and mindeg >= nodes - 5 then {edges <= nodes*(nodes-13)/2 + 13*maxClique};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(5.0))):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 13.0*maxClique+0.5*nodes**2.0-(6.5*nodes), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxClique', 7.69230769230769e-2*edges-(3.84615384615385e-2*nodes**2.0)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*(8.0*edges-(104.0*maxClique)+169.0)**(1/2)+6.5, ind='Max')
				except:
					pass
		return

class Theorem450(Theorem):
	def __init__(self):
		super(Theorem450, self).__init__(450, "if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes - mindeg - 1 and mindeg <= nodes - 10 then {nodes <= 2*mindeg + 2} else if nodeInd < nodeCliqueCover and nodeCliqueCover == nodes - mindeg - 1 and mindeg >= nodes - 10 then {nodes <= 2*mindeg + 3};", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeInd_Max != 'undt' and (nodeInd_Max<nodeCliqueCover_Min)) and (nodeCliqueCover_Max != 'undt' and (nodeCliqueCover_Max<=nodes_Min-(mindeg_Min)-(1.0))) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (nodeCliqueCover_Min>=nodes_Max-(mindeg_Max)-(1.0))) and (mindeg_Max != 'undt' and (mindeg_Max<=nodes_Min-(10.0))):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*mindeg+2.0, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*nodes-(1.0), ind='Min')
			except:
				pass
		elif (nodeInd_Max != 'undt' and (nodeInd_Max<nodeCliqueCover_Min)) and (nodeCliqueCover_Max != 'undt' and (nodeCliqueCover_Max<=nodes_Min-(mindeg_Min)-(1.0))) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (nodeCliqueCover_Min>=nodes_Max-(mindeg_Max)-(1.0))) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(10.0))):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*mindeg+3.0, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*nodes-(1.5), ind='Min')
			except:
				pass
		return

class Theorem451(Theorem):
	def __init__(self):
		super(Theorem451, self).__init__(451, "if mindeg <= min(nodes-7, nodes - nodeInd - 2) then {mindeg <= ((nodes - 1)*(maxClique - 1) - 2)/maxClique};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (mindeg_Max != 'undt' and (mindeg_Max<=min(nodes_Min-(7.0), nodes_Min-(nodeInd_Min)-(2.0)))):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*nodes-(1.0)-(1.0*nodes/maxClique)-(1.0/maxClique), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('maxClique', -((1.0*nodes+1.0)/(mindeg-(nodes)+1.0)), ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*(mindeg*maxClique+maxClique+1.0)/(maxClique-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem452(Theorem):
	def __init__(self):
		super(Theorem452, self).__init__(452, "if nodeInd == 2 then {maxClique >= nodes*((nodes - 1 - 2*edges/nodes)*ln(nodes - 1 - 2*edges/nodes) - (nodes - 2 - 2*edges/nodes)**2)/(nodes - 2 - 2*edges/nodes)**2};", "")
	def involves(self, str_invar):
		return str_invar in ["nodeInd"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)):
		return

class Theorem453(Theorem):
	def __init__(self):
		super(Theorem453, self).__init__(453, "edges <= nodes*(nodes - 1)/2 - floor((nodes-nodeConnec)/(maxClique-1))*(nodes-nodeConnec) - nodeConnec*(nodeConnec - 1)/2 + (maxClique - 1)*floor((nodes-nodeConnec)/(maxClique-1))*(floor((nodes-nodeConnec)/(maxClique-1))+1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*maxClique-(0.5*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*floor((nodes-(nodeConnec))/(maxClique-(1.0))))+0.5*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*maxClique-(0.5*floor((nodes-(nodeConnec))/(maxClique-(1.0))))+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*nodeConnec-(1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*nodes)-(0.5*nodeConnec**2.0)+0.5*nodeConnec+0.5*nodes**2.0-(0.5*nodes), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('maxClique', 1.0*(2.0*edges+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*floor((nodes-(nodeConnec))/(maxClique-(1.0)))+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))-(2.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*nodeConnec)+2.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*nodes+1.0*nodeConnec**2.0-(1.0*nodeConnec)-(1.0*nodes**2.0)+1.0*nodes)/(floor((nodes-(nodeConnec))/(maxClique-(1.0)))*(floor((nodes-(nodeConnec))/(maxClique-(1.0)))+1.0)), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*(1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))+0.5)+1.0*(2.0*edges-(1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*maxClique)+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*floor((nodes-(nodeConnec))/(maxClique-(1.0)))-(1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*maxClique)+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))**2.0-(2.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))*nodeConnec)+1.0*floor((nodes-(nodeConnec))/(maxClique-(1.0)))+1.0*nodeConnec**2.0-(1.0*nodeConnec)+0.25)**(1/2), ind='Min')
		except:
			pass
		return

class Theorem454(Theorem):
	def __init__(self):
		super(Theorem454, self).__init__(454, "if nodeInd <= 2 and mindeg >= nodes - 4 then {edges <= nodes*(nodes - 14)/2 + 14*maxClique};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeInd_Max != 'undt' and (nodeInd_Max<=2.0)) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(4.0))):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 14.0*maxClique+0.5*nodes**2.0-(7.0*nodes), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxClique', 7.14285714285714e-2*edges-(3.57142857142857e-2*nodes**2.0)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*(2.0*edges-(28.0*maxClique)+49.0)**(1/2)+7.0, ind='Max')
				except:
					pass
		return

class Theorem455(Theorem):
	def __init__(self):
		super(Theorem455, self).__init__(455, "if nodeInd <= 2 and mindeg >= nodes - 3 then {edges <= nodes*(nodes - 15)/2 + 15*maxClique};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeInd_Max != 'undt' and (nodeInd_Max<=2.0)) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(3.0))):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 15.0*maxClique+0.5*nodes**2.0-(7.5*nodes), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxClique', 6.66666666666667e-2*edges-(3.33333333333333e-2*nodes**2.0)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*(8.0*edges-(120.0*maxClique)+225.0)**(1/2)+7.5, ind='Max')
				except:
					pass
		return

class Theorem456(Theorem):
	def __init__(self):
		super(Theorem456, self).__init__(456, "if maxClique == 2 then {chromaticNum <= 1 + 3*(nodeCover + 12)/16};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodeCover"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.1875*nodeCover+3.25, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('nodeCover', 5.33333333333333*chromaticNum-(17.3333333333333), ind='Min')
			except:
				pass
		return

class Theorem457(Theorem):
	def __init__(self):
		super(Theorem457, self).__init__(457, "if maxClique == 2 then {chromaticNum <= (3*nodes - 3*nodeInd + 52)/16};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', -(0.1875*nodeInd)+0.1875*nodes+3.25, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', -(5.33333333333333*chromaticNum)+1.0*nodes+17.3333333333333, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			try:
				ingrid_obj.set('nodes', 5.33333333333333*chromaticNum+1.0*nodeInd-(17.3333333333333), ind='Min')
			except:
				pass
		return

class Theorem458(Theorem):
	def __init__(self):
		super(Theorem458, self).__init__(458, "if nodeInd == 2 then {nodeCliqueCover <= (3*nodes - 3*maxClique + 52)/16};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)):
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCliqueCover', -(0.1875*maxClique)+0.1875*nodes+3.25, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxClique', -(5.33333333333333*nodeCliqueCover)+1.0*nodes+17.3333333333333, ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 5.33333333333333*nodeCliqueCover+1.0*maxClique-(17.3333333333333), ind='Min')
			except:
				pass
		return

