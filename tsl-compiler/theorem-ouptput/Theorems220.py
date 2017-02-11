class Theorem201(Theorem):
	def __init__(self):
		super(Theorem201, self).__init__(201, "if nodes >= 6 and connected and nodes >= 3*edgeInd-1 then {nodeCover <= 2*edgeInd - mindeg};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edgeInd","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		connected = ingrid_obj.get('connected')
		edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
		if (nodes_Min>=6.0) and (connected == True) and (edgeInd_Max != 'undt' and (nodes_Min>=3.0*edgeInd_Max-(1.0))):
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeCover', 2.0*edgeInd-(1.0*mindeg), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*nodeCover+0.5*mindeg, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('mindeg', -(1.0*nodeCover)+2.0*edgeInd, ind='Max')
				except:
					pass
		return

class Theorem202(Theorem):
	def __init__(self):
		super(Theorem202, self).__init__(202, "if regular then { nodeCover >= nodes/2 + (maxClique-1)*(maxClique-2)/(2*mindeg) };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","mindeg","nodeCover","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		if (regular == True):
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeCover', (0.5*maxClique**2.0-(1.5*maxClique)+0.5*mindeg*nodes+1.0)/mindeg, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if mindeg != 'undt' and nodeCover != 'undt':
				try:
					ingrid_obj.set('maxClique', 0.5*(8.0*nodeCover*mindeg-(4.0*mindeg*nodes)+1.0)**(1/2)+1.5, ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('mindeg', (0.5*maxClique**2.0-(1.5*maxClique)+1.0)/(1.0*nodeCover-(0.5*nodes)), ind='Min')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if maxClique != 'undt' and mindeg != 'undt' and nodeCover != 'undt':
				try:
					ingrid_obj.set('nodes', (2.0*nodeCover*mindeg-(1.0*maxClique**2.0)+3.0*maxClique-(2.0))/mindeg, ind='Max')
				except:
					pass
		return

class Theorem203(Theorem):
	def __init__(self):
		super(Theorem203, self).__init__(203, "if maxClique == 2 then {nodeCover <= (1/2)*(2*nodes +3-sqrt(8*nodes+9))};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 1.0*nodes-(0.5*(8.0*nodes+9.0)**0.5)+1.5, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', (1.0/2.0)*(-(((8.0*nodes+9.0)**(1.0/2.0)))+3.0+2.0*nodes), ind='Max')
				except:
					pass
		return

class Theorem204(Theorem):
	def __init__(self):
		super(Theorem204, self).__init__(204, "if maxClique == 2 and nodes < 2*nodeCover and nodeCover <= 3*nodes/5 then {nodeCover <= (2*nodes-sqrt(5*edges - nodes**2))/5};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodeCover_Min = ingrid_obj.get('nodeCover', ind='Min')
		nodeCover_Max = ingrid_obj.get('nodeCover', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (nodes_Max != 'undt' and (nodes_Max<2.0*nodeCover_Min)) and (nodeCover_Max != 'undt' and (nodeCover_Max<=3.0*nodes_Min/5.0)):
		return

class Theorem205(Theorem):
	def __init__(self):
		super(Theorem205, self).__init__(205, "if mindeg == 2 then {edgeCover <= nodes * max(4, maxdeg)/(2+max(4,maxdeg))};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 1.0*max(4.0, maxdeg)*nodes/(1.0*max(4.0, maxdeg)+2.0), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', edgeCover*(1.0*max(4.0, maxdeg)+2.0)/max(4.0, maxdeg), ind='Min')
				except:
					pass
		return

class Theorem206(Theorem):
	def __init__(self):
		super(Theorem206, self).__init__(206, "nodeCover <= (nodes*maxdeg+1)/(maxdeg+1) - 1/(mindeg+1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*(maxdeg*mindeg*nodes+maxdeg*nodes-(maxdeg)+mindeg)/(maxdeg*mindeg+maxdeg+mindeg+1.0), ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeCover*mindeg)-(nodeCover)+mindeg)/(nodeCover*mindeg+nodeCover-(mindeg*nodes)-(nodes)+1.0), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*(-(nodeCover*maxdeg)-(nodeCover)+maxdeg*nodes-(maxdeg))/(nodeCover*maxdeg+nodeCover-(maxdeg*nodes)-(1.0)), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*(nodeCover*maxdeg*mindeg+nodeCover*maxdeg+nodeCover*mindeg+nodeCover+maxdeg-(mindeg))/(maxdeg*(mindeg+1.0)), ind='Min')
		except:
			pass
		return

class Theorem207(Theorem):
	def __init__(self):
		super(Theorem207, self).__init__(207, "if maxClique == 2 and maxdeg >= 3 then {nodeCover <= nodes*(maxdeg-(6/5)/(maxdeg-(1/5)))} else if nodes>=3 and connected and not complete and not cycle or (cycle and isset nodes and even nodes) then {nodeCover <= nodes *(maxdeg - 1)/maxdeg + 1/(maxdeg+1) - 1/(mindeg+1)};", "")
	def involves(self, str_invar):
		return str_invar in ["complete","connected","cycle","maxClique","maxdeg","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		connected = ingrid_obj.get('connected')
		complete = ingrid_obj.get('complete')
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (maxdeg_Min>=3.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodes*(1.0*maxdeg**2.0-(0.2*maxdeg)-(1.2))/(1.0*maxdeg-(0.2)), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', (0.5*nodeCover+0.1*nodes+0.5*(1.0*nodeCover**2.0-(0.4*nodeCover*nodes)+4.84*nodes**2.0)**(1/2))/nodes, ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', nodeCover*(-(1.0*maxdeg)+0.2)/(-(1.0*maxdeg**2.0)+0.2*maxdeg+1.2), ind='Min')
			except:
				pass
		elif (nodes_Min>=3.0) and (connected == True) and (complete == False) and (cycle == False) or (cycle == True) and (nodes_Min == nodes_Max) and (even(nodes_Min) and even(nodes_Max)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 1.0*(maxdeg**2.0*mindeg*nodes+maxdeg**2.0*nodes-(maxdeg**2.0)+maxdeg*mindeg-(mindeg*nodes)-(nodes))/(maxdeg*(maxdeg*mindeg+maxdeg+mindeg+1.0)), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodeCover != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 0.5*(-(nodeCover*mindeg)-(nodeCover)+mindeg+(1.0*nodeCover**2.0*mindeg**2.0+2.0*nodeCover**2.0*mindeg+1.0*nodeCover**2.0-(4.0*nodeCover*mindeg**2.0*nodes)-(2.0*nodeCover*mindeg**2.0)-(8.0*nodeCover*mindeg*nodes)-(2.0*nodeCover*mindeg)-(4.0*nodeCover*nodes)+4.0*mindeg**2.0*nodes**2.0+1.0*mindeg**2.0+8.0*mindeg*nodes**2.0-(4.0*mindeg*nodes)+4.0*nodes**2.0-(4.0*nodes))**(1/2))/(nodeCover*mindeg+nodeCover-(mindeg*nodes)-(nodes)+1.0), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*(-(nodeCover*maxdeg**2.0)-(nodeCover*maxdeg)+maxdeg**2.0*nodes-(maxdeg**2.0)-(nodes))/(nodeCover*maxdeg**2.0+nodeCover*maxdeg-(maxdeg**2.0*nodes)-(maxdeg)+nodes), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg*(nodeCover*maxdeg*mindeg+nodeCover*maxdeg+nodeCover*mindeg+nodeCover+maxdeg-(mindeg))/(maxdeg**2.0*mindeg+maxdeg**2.0-(mindeg)-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem208(Theorem):
	def __init__(self):
		super(Theorem208, self).__init__(208, "if connected and not complete then {nodeCover <= (2*edges*nodes*nodes - 3*nodes - 1)/(2*edges*nodes + nodes *nodes)};", "")
	def involves(self, str_invar):
		return str_invar in ["complete","connected","edges","nodeCover","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		complete = ingrid_obj.get('complete')
		if (connected == True) and (complete == False):
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', (2.0*edges*nodes**2.0-(3.0*nodes)-(1.0))/(nodes*(2.0*edges+1.0*nodes)), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeCover != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', -((0.5*nodeCover*nodes**2.0+1.5*nodes+0.5)/(nodes*(nodeCover-(nodes)))), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', -((2.0*nodeCover*edges+1.0*(4.0*nodeCover**2.0*edges**2.0+12.0*nodeCover*edges-(4.0*nodeCover)+8.0*edges+9.0)**(1/2)+3.0)/(2.0*nodeCover-(4.0*edges))), ind='Min')
				except:
					pass
		return

class Theorem209(Theorem):
	def __init__(self):
		super(Theorem209, self).__init__(209, "nodeCover <= nodes * (1-2/(maxdeg+maxClique+1));", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*nodes*(maxClique+maxdeg-(1.0))/(maxClique+maxdeg+1.0), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxClique', 1.0*(-(nodeCover*maxdeg)-(nodeCover)+maxdeg*nodes-(nodes))/(nodeCover-(nodes)), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeCover*maxClique)-(nodeCover)+maxClique*nodes-(nodes))/(nodeCover-(nodes)), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*nodeCover*(maxClique+maxdeg+1.0)/(maxClique+maxdeg-(1.0)), ind='Min')
		except:
			pass
		return

class Theorem210(Theorem):
	def __init__(self):
		super(Theorem210, self).__init__(210, "nodeCover <= ((nodes-2)*maxdeg + maxClique + mindeg - 1)/(maxdeg+1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*(1.0*maxClique+1.0*maxdeg*nodes-(2.0*maxdeg)+1.0*mindeg-(1.0))/(maxdeg+1.0), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxClique', 1.0*nodeCover*maxdeg+1.0*nodeCover-(1.0*maxdeg*nodes)+2.0*maxdeg-(1.0*mindeg)+1.0, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeCover)+maxClique+mindeg-(1.0))/(1.0*nodeCover-(1.0*nodes)+2.0), ind='Max')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*nodeCover*maxdeg+1.0*nodeCover-(1.0*maxClique)-(1.0*maxdeg*nodes)+2.0*maxdeg+1.0, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if maxClique != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('nodes', (1.0*nodeCover*maxdeg+1.0*nodeCover-(1.0*maxClique)+2.0*maxdeg-(1.0*mindeg)+1.0)/maxdeg, ind='Min')
			except:
				pass
		return

class Theorem211(Theorem):
	def __init__(self):
		super(Theorem211, self).__init__(211, "if nodeCover > nodes - nodeCliqueCover then {nodeCover <= nodes*maxdeg/(maxdeg+1) - (1/3)};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodeCliqueCover","nodeCover","nodes"]
	def run(self, ingrid_obj):
		nodeCover_Min = ingrid_obj.get('nodeCover', ind='Min')
		nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeCliqueCover_Max != 'undt' and nodes_Max != 'undt' and (nodeCover_Min>nodes_Max-(nodeCliqueCover_Max))):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 1.0*(1.0*maxdeg*nodes-(0.333333333333333*maxdeg)-(0.333333333333333))/(maxdeg+1.0), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Nax')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('maxdeg', -((1.0*nodeCover+0.333333333333333)/(1.0*nodeCover-(1.0*nodes)+0.333333333333333)), ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*nodeCover+1.0*nodeCover/maxdeg+0.333333333333333+0.333333333333333/maxdeg, ind='Min')
				except:
					pass
		return

class Theorem212(Theorem):
	def __init__(self):
		super(Theorem212, self).__init__(212, "nodeCliqueCover <= edgeCover;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","nodeCliqueCover"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', edgeCover, ind='Max')
			except:
				pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('edgeCover', nodeCliqueCover, ind='Min')
		except:
			pass
		return

class Theorem213(Theorem):
	def __init__(self):
		super(Theorem213, self).__init__(213, "domination <= nodeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","nodeInd"]
	def run(self, ingrid_obj):
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('domination', nodeInd, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		try:
			ingrid_obj.set('nodeInd', domination, ind='Min')
		except:
			pass
		return

class Theorem214(Theorem):
	def __init__(self):
		super(Theorem214, self).__init__(214, "domination <= edgeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edgeInd"]
	def run(self, ingrid_obj):
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('domination', edgeInd, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		try:
			ingrid_obj.set('edgeInd', domination, ind='Min')
		except:
			pass
		return

class Theorem215(Theorem):
	def __init__(self):
		super(Theorem215, self).__init__(215, "numOfComponents <= domination;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","numOfComponents"]
	def run(self, ingrid_obj):
		domination = ingrid_obj.get('domination', ind='Max')
		if domination != 'undt':
			try:
				ingrid_obj.set('numOfComponents', domination, ind='Max')
			except:
				pass
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		try:
			ingrid_obj.set('domination', numOfComponents, ind='Min')
		except:
			pass
		return

class Theorem216(Theorem):
	def __init__(self):
		super(Theorem216, self).__init__(216, "maxdeg <= edgeChromatic;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg"]
	def run(self, ingrid_obj):
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
		if edgeChromatic != 'undt':
			try:
				ingrid_obj.set('maxdeg', edgeChromatic, ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		try:
			ingrid_obj.set('edgeChromatic', maxdeg, ind='Min')
		except:
			pass
		return

class Theorem217(Theorem):
	def __init__(self):
		super(Theorem217, self).__init__(217, "edgeChromatic <= maxdeg + 1;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('edgeChromatic', 1.0*maxdeg+1.0, ind='Max')
			except:
				pass
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
		try:
			ingrid_obj.set('maxdeg', 1.0*edgeChromatic-(1.0), ind='Min')
		except:
			pass
		return

class Theorem218(Theorem):
	def __init__(self):
		super(Theorem218, self).__init__(218, "mindeg <= nodeCover;", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeCover"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('mindeg', nodeCover, ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('nodeCover', mindeg, ind='Min')
		except:
			pass
		return

class Theorem219(Theorem):
	def __init__(self):
		super(Theorem219, self).__init__(219, "edgeConnec <= mindeg;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","mindeg"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		if mindeg != 'undt':
			try:
				ingrid_obj.set('edgeConnec', mindeg, ind='Max')
			except:
				pass
		edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
		try:
			ingrid_obj.set('mindeg', edgeConnec, ind='Min')
		except:
			pass
		return

class Theorem220(Theorem):
	def __init__(self):
		super(Theorem220, self).__init__(220, "maxClique <= chromaticNum;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('maxClique', chromaticNum, ind='Max')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('chromaticNum', maxClique, ind='Min')
		except:
			pass
		return

