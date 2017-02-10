class Theorem41(Theorem):
	def __init__(self):
		super(Theorem41, self).__init__(41, "if chromaticNum <= 2 or bipartite then { bipartite, chromaticNum <= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","chromaticNum"]
	def run(self, ingrid_obj):
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		bipartite = ingrid_obj.get('bipartite')
		if (chromaticNum_Max != 'undt' and (chromaticNum_Max<=2.0)) or (bipartite == True):
			ingrid_obj.set('bipartite', True)
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Max')
			except:
				pass
		return

class Theorem42(Theorem):
	def __init__(self):
		super(Theorem42, self).__init__(42, "if radius == 1 or maxdeg ==  nodes-1 then { maxdeg == nodes - 1, radius == 1};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodes","radius"]
	def run(self, ingrid_obj):
		radius_Min = ingrid_obj.get('radius', ind='Min')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (radius_Max==radius_Min and (radius_Min==1.0)) or (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(1.0))):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 1.0*nodes-(1.0), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*maxdeg+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('radius', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('radius', 1.0, ind='Min')
			except:
				pass
		return

class Theorem43(Theorem):
	def __init__(self):
		super(Theorem43, self).__init__(43, "if (forest and connected) or tree then { tree, forest and connected };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","forest","tree"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		connected = ingrid_obj.get('connected')
		tree = ingrid_obj.get('tree')
		if (forest == True) and (connected == True) or (tree == True):
			ingrid_obj.set('tree', True)
			ingrid_obj.set('forest', True)
			ingrid_obj.set('connected', True)
		return

class Theorem44(Theorem):
	def __init__(self):
		super(Theorem44, self).__init__(44, "if nodeConnec >= 1 or numOfComponents == 1 or radius <= nodes/2 or diameter <= nodes-1 then { nodeConnec >= 1, numOfComponents == 1, radius <= nodes/2, diameter <= nodes-1 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","nodeConnec","nodes","numOfComponents","radius"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		numOfComponents_Min = ingrid_obj.get('numOfComponents', ind='Min')
		numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (nodeConnec_Min>=1.0) or (numOfComponents_Max==numOfComponents_Min and (numOfComponents_Min==1.0)) or (radius_Max != 'undt' and (radius_Max<=nodes_Min/2.0)) or (diameter_Max != 'undt' and (diameter_Max<=nodes_Min-(1.0))):
			try:
				ingrid_obj.set('nodeConnec', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('numOfComponents', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('numOfComponents', 1.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('radius', 0.5*nodes, ind='Max')
				except:
					pass
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*radius, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 1.0*nodes-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*diameter+1.0, ind='Min')
			except:
				pass
		return

class Theorem45(Theorem):
	def __init__(self):
		super(Theorem45, self).__init__(45, "if cycle or (maxdeg == 2 and mindeg == 2 and connected) then { cycle, maxdeg == 2, mindeg == 2, connected };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","cycle","maxdeg","mindeg"]
	def run(self, ingrid_obj):
		cycle = ingrid_obj.get('cycle')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		connected = ingrid_obj.get('connected')
		if (cycle == True) or (maxdeg_Max==maxdeg_Min and (maxdeg_Min==2.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)) and (connected == True):
			ingrid_obj.set('cycle', True)
			try:
				ingrid_obj.set('maxdeg', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('maxdeg', 2.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('mindeg', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('mindeg', 2.0, ind='Min')
			except:
				pass
			ingrid_obj.set('connected', True)
		return

class Theorem46(Theorem):
	def __init__(self):
		super(Theorem46, self).__init__(46, "if regular or mindeg == maxdeg then { regular, mindeg == maxdeg };", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (regular == True) or (mindeg_Max != 'undt' and (mindeg_Max<=maxdeg_Min)) and (maxdeg_Max != 'undt' and (mindeg_Min>=maxdeg_Max)):
			ingrid_obj.set('regular', True)
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('mindeg', maxdeg, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('mindeg', maxdeg, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('maxdeg', mindeg, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('maxdeg', mindeg, ind='Min')
			except:
				pass
		return

class Theorem47(Theorem):
	def __init__(self):
		super(Theorem47, self).__init__(47, "if genus == 0 or planar or thickness == 1 then { genus == 0, planar, thickness == 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","planar","thickness"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		genus_Max = ingrid_obj.get('genus', ind='Max')
		planar = ingrid_obj.get('planar')
		thickness_Min = ingrid_obj.get('thickness', ind='Min')
		thickness_Max = ingrid_obj.get('thickness', ind='Max')
		if (genus_Max==genus_Min and (genus_Min==0.0)) or (planar == True) or (thickness_Max==thickness_Min and (thickness_Min==1.0)):
			try:
				ingrid_obj.set('genus', 0.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('genus', 0.0, ind='Min')
			except:
				pass
			ingrid_obj.set('planar', True)
			try:
				ingrid_obj.set('thickness', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('thickness', 1.0, ind='Min')
			except:
				pass
		return

class Theorem48(Theorem):
	def __init__(self):
		super(Theorem48, self).__init__(48, "if forest then { planar, chromaticNum == 2, mindeg == 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","forest","mindeg","planar"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == True):
			ingrid_obj.set('planar', True)
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('mindeg', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('mindeg', 2.0, ind='Min')
			except:
				pass
		return

class Theorem49(Theorem):
	def __init__(self):
		super(Theorem49, self).__init__(49, "if cycle then { planar, not forest, crossing == 0, nodes >= 2, edges >= 3, arboricity == 2, nodeCover == (nodes + 1)/2, edgeCover == (nodes + 1)/2, nodeInd == nodes/2, edgeInd == nodes/2, radius == edgeInd, girth == circumference, circumference == nodes, edgeChromatic == chromaticNum, nodes >= 2*nodeCover-1, nodes <= 2*nodeCover, nodes >= 2*edgeInd, nodes <= 2*edgeInd + 1, nodeConnec == 2, regular, bandwidth == 2 }; if cycle and nodes > 3 then { maxClique == 2 } else { maxClique == 3 }; if cycle and even nodes then { chromaticNum == 2 } else { chromaticNum == 3 }; if cycle and chromaticNum == 2 then { even nodes } else { odd nodes }; if cycle and maxClique == 2 then { nodes >= 4 } else { nodes == 3 }; if cycle and nodes == 3 then { nodeCliqueCover == 1 } else { nodeCliqueCover == nodeCover };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","bandwidth","chromaticNum","circumference","crossing","cycle","edgeChromatic","edgeCover","edgeInd","edges","forest","girth","nodeConnec","nodeCover","nodeInd","nodes","planar","radius","regular","maxClique","nodeCliqueCover"]
	def run(self, ingrid_obj):
		cycle = ingrid_obj.get('cycle')
		if (cycle == True):
			ingrid_obj.set('planar', True)
			ingrid_obj.set('forest', False)
			try:
				ingrid_obj.set('crossing', 0.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('crossing', 0.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodes', 2.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edges', 3.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('arboricity', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('arboricity', 2.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Min')
			except:
				pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Min')
			except:
				pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Max')
			if edgeCover != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*edgeCover-(1.0), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*edgeCover-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', 0.5*nodes, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.5*nodes, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*nodeInd, ind='Max')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*nodeInd, ind='Min')
			except:
				pass
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
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('radius', edgeInd, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Min')
			try:
				ingrid_obj.set('radius', edgeInd, ind='Min')
			except:
				pass
			radius = ingrid_obj.get('radius', ind='Max')
			if radius != 'undt':
				try:
					ingrid_obj.set('edgeInd', radius, ind='Max')
				except:
					pass
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('edgeInd', radius, ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			if circumference != 'undt':
				try:
					ingrid_obj.set('girth', circumference, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			try:
				ingrid_obj.set('girth', circumference, ind='Min')
			except:
				pass
			girth = ingrid_obj.get('girth', ind='Max')
			if girth != 'undt':
				try:
					ingrid_obj.set('circumference', girth, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('circumference', girth, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('circumference', nodes, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', nodes, ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			if circumference != 'undt':
				try:
					ingrid_obj.set('nodes', circumference, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			try:
				ingrid_obj.set('nodes', circumference, ind='Min')
			except:
				pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
			if chromaticNum != 'undt':
				try:
					ingrid_obj.set('edgeChromatic', chromaticNum, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('edgeChromatic', chromaticNum, ind='Min')
			except:
				pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
			if edgeChromatic != 'undt':
				try:
					ingrid_obj.set('chromaticNum', edgeChromatic, ind='Max')
				except:
					pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
			try:
				ingrid_obj.set('chromaticNum', edgeChromatic, ind='Min')
			except:
				pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*nodeCover-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.5*nodes+0.5, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*nodeCover, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeCover', 0.5*nodes, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*edgeInd+1.0, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*nodes-(0.5), ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeConnec', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeConnec', 2.0, ind='Min')
			except:
				pass
			ingrid_obj.set('regular', True)
			try:
				ingrid_obj.set('bandwidth', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('bandwidth', 2.0, ind='Min')
			except:
				pass
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		
		if (cycle == True) and (nodes_Min>3.0):
			try:
				ingrid_obj.set('maxClique', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('maxClique', 2.0, ind='Min')
			except:
				pass
		elif (True):
			try:
				ingrid_obj.set('maxClique', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('maxClique', 3.0, ind='Min')
			except:
				pass
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		
		if (cycle == True) and (even(nodes_Min) and even(nodes_Max)):
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Min')
			except:
				pass
		elif (True):
			try:
				ingrid_obj.set('chromaticNum', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('chromaticNum', 3.0, ind='Min')
			except:
				pass
		cycle = ingrid_obj.get('cycle')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		
		if (cycle == True) and (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)):
			nodes_Max = ingrid_obj.get('nodes', ind='Max')-1
			nodes_Min = ingrid_obj.get('nodes', ind='Min')+1
			if even(nodes_Max):
				ingrid_obj.set('nodes', ind='Max')
			if even(nodes_Min):
				ingrid_obj.set('nodes', ind='Min')
		elif (True):
			nodes_Max = ingrid_obj.get('nodes', ind='Max')-1
			nodes_Min = ingrid_obj.get('nodes', ind='Min')+1
			if odd(nodes_Max):
				ingrid_obj.set('nodes', ind='Max')
			if odd(nodes_Min):
				ingrid_obj.set('nodes', ind='Min')
		cycle = ingrid_obj.get('cycle')
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		
		if (cycle == True) and (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			try:
				ingrid_obj.set('nodes', 4.0, ind='Min')
			except:
				pass
		elif (True):
			try:
				ingrid_obj.set('nodes', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodes', 3.0, ind='Min')
			except:
				pass
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		
		if (cycle == True) and (nodes_Max==nodes_Min and (nodes_Min==3.0)):
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
		elif (True):
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodeCliqueCover', nodeCover, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodeCliqueCover', nodeCover, ind='Min')
			except:
				pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
			if nodeCliqueCover != 'undt':
				try:
					ingrid_obj.set('nodeCover', nodeCliqueCover, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('nodeCover', nodeCliqueCover, ind='Min')
			except:
				pass
		return

class Theorem50(Theorem):
	def __init__(self):
		super(Theorem50, self).__init__(50, "if forest or edges == nodes - numOfComponents or arboricity == 1 or undefined girth or undefined circumference then { forest, edges == nodes - numOfComponents, arboricity == 1, undefined girth, undefined circumference };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","circumference","edges","forest","girth","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		numOfComponents_Min = ingrid_obj.get('numOfComponents', ind='Min')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
		arboricity_Min = ingrid_obj.get('arboricity', ind='Min')
		arboricity_Max = ingrid_obj.get('arboricity', ind='Max')
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		circumference_Max = ingrid_obj.get('circumference', ind = 'Max')
		if (forest == True) or (edges_Max != 'undt' and (edges_Max<=nodes_Min-(numOfComponents_Min))) and (nodes_Max != 'undt' and numOfComponents_Max != 'undt' and (edges_Min>=nodes_Max-(numOfComponents_Max))) or (arboricity_Max==arboricity_Min and (arboricity_Min==1.0)) or (girth_Max == 'undt') or (circumference_Max == 'undt'):
			ingrid_obj.set('forest', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', nodes-(numOfComponents), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('edges', nodes-(numOfComponents), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edges != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('nodes', edges+numOfComponents, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', edges+numOfComponents, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', -(edges)+nodes, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('numOfComponents', -(edges)+nodes, ind='Min')
				except:
					pass
			try:
				ingrid_obj.set('arboricity', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('arboricity', 1.0, ind='Min')
			except:
				pass
			girth_Max = ingrid_obj.get('girth', ind='Max')-1
				ingrid_obj.set('girth', 'undt', ind='Max')
			circumference_Max = ingrid_obj.get('circumference', ind='Max')-1
				ingrid_obj.set('circumference', 'undt', ind='Max')
		return

class Theorem51(Theorem):
	def __init__(self):
		super(Theorem51, self).__init__(51, "arboricity >= chromaticNum / 2;", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","chromaticNum"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('arboricity', 0.5*chromaticNum, ind='Min')
		except:
			pass
		arboricity = ingrid_obj.get('arboricity', ind='Max')
		if arboricity != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 2.0*arboricity, ind='Max')
			except:
				pass
		return

class Theorem52(Theorem):
	def __init__(self):
		super(Theorem52, self).__init__(52, "if (connected and not cycle and not complete) or (maxClique <= maxdeg and maxdeg >= 4 and regular) then { arboricity <= (1 + maxdeg)/2 }; arboricity <= 1 + spectralRadius/2;", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","complete","connected","cycle","maxClique","maxdeg","regular","spectralRadius"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		cycle = ingrid_obj.get('cycle')
		complete = ingrid_obj.get('complete')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		regular = ingrid_obj.get('regular')
		if (connected == True) and (cycle == False) and (complete == False) or (maxClique_Max != 'undt' and (maxClique_Max<=maxdeg_Min)) and (maxdeg_Min>=4.0) and (regular == True):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('arboricity', 0.5*maxdeg+0.5, ind='Max')
				except:
					pass
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 2.0*arboricity-(1.0), ind='Min')
			except:
				pass
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('arboricity', 0.5*spectralRadius+1.0, ind='Max')
			except:
				pass
		arboricity = ingrid_obj.get('arboricity', ind='Min')
		try:
			ingrid_obj.set('spectralRadius', 2.0*arboricity-(2.0), ind='Min')
		except:
			pass
		return

class Theorem53(Theorem):
	def __init__(self):
		super(Theorem53, self).__init__(53, "arboricity <= chromaticNum - chromaticNum/(1 + nodes/((girth - 1)/2)*chromaticNum);", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","chromaticNum","girth","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		girth = ingrid_obj.get('girth', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('arboricity', 1.0*chromaticNum**2.0*nodes/(1.0*chromaticNum*nodes+0.5*girth-(0.5)), ind='Max')
			except:
				pass
		arboricity = ingrid_obj.get('arboricity', ind='Min')
		girth = ingrid_obj.get('girth', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('chromaticNum', 0.5*(arboricity*nodes+(arboricity*nodes*(1.0*arboricity*nodes+2.0*girth-(2.0)))**(1/2))/nodes, ind='Min')
		except:
			pass
		arboricity = ingrid_obj.get('arboricity', ind='Min')
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('girth', -(2.0*chromaticNum*nodes)+1.0+2.0*chromaticNum**2.0*nodes/arboricity, ind='Max')
			except:
				pass
		arboricity = ingrid_obj.get('arboricity', ind='Max')
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		girth = ingrid_obj.get('girth', ind='Min')
		if arboricity != 'undt' and chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodes', -(0.5*arboricity*(girth-(1.0))/(chromaticNum*(arboricity-(chromaticNum)))), ind='Max')
			except:
				pass
		return

class Theorem54(Theorem):
	def __init__(self):
		super(Theorem54, self).__init__(54, "if planar then { mindeg <= 5, maxClique <= 4, arboricity <= 3, crossing == 0 };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","crossing","maxClique","mindeg","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		if (planar == True):
			try:
				ingrid_obj.set('mindeg', 5.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('maxClique', 4.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('arboricity', 3.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('crossing', 0.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('crossing', 0.0, ind='Min')
			except:
				pass
		return

class Theorem55(Theorem):
	def __init__(self):
		super(Theorem55, self).__init__(55, "edges >= (maxdeg + (nodes - 1)*mindeg)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*maxdeg+0.5*mindeg*nodes-(0.5*mindeg), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('maxdeg', 2.0*edges-(1.0*mindeg*nodes)+1.0*mindeg, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('mindeg', 2.0*(1.0*edges-(0.5*maxdeg))/(nodes-(1.0)), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		if edges != 'undt' and mindeg != 'undt':
			try:
				ingrid_obj.set('nodes', (2.0*edges-(1.0*maxdeg)+1.0*mindeg)/mindeg, ind='Max')
			except:
				pass
		return

class Theorem56(Theorem):
	def __init__(self):
		super(Theorem56, self).__init__(56, "edges <= ((nodes - 1)*maxdeg + mindeg)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*maxdeg*nodes-(0.5*maxdeg)+0.5*mindeg, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', 2.0*(1.0*edges-(0.5*mindeg))/(nodes-(1.0)), ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 2.0*edges-(1.0*maxdeg*nodes)+1.0*maxdeg, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		if mindeg != 'undt':
			try:
				ingrid_obj.set('nodes', (2.0*edges+1.0*maxdeg-(1.0*mindeg))/maxdeg, ind='Min')
			except:
				pass
		return

class Theorem57(Theorem):
	def __init__(self):
		super(Theorem57, self).__init__(57, "if regular and odd mindeg then { even p };", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","p","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (regular == True) and (odd(mindeg_Min) and odd(mindeg_Max)):
			p_Max = ingrid_obj.get('p', ind='Max')-1
			p_Min = ingrid_obj.get('p', ind='Min')+1
			if even(p_Max):
				ingrid_obj.set('p', ind='Max')
			if even(p_Min):
				ingrid_obj.set('p', ind='Min')
		return

class Theorem58(Theorem):
	def __init__(self):
		super(Theorem58, self).__init__(58, "maxClique >= nodes/(nodes-spectralRadius)-1/3;", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodes","spectralRadius"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('maxClique', 1.0*(0.666666666666667*nodes+0.333333333333333*spectralRadius)/(nodes-(spectralRadius)), ind='Min')
		except:
			pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if maxClique != 'undt' and spectralRadius != 'undt':
			try:
				ingrid_obj.set('nodes', spectralRadius*(1.0*maxClique+0.333333333333333)/(1.0*maxClique-(0.666666666666667)), ind='Max')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('spectralRadius', nodes*(1.0*maxClique-(0.666666666666667))/(1.0*maxClique+0.333333333333333), ind='Min')
		except:
			pass
		return

class Theorem59(Theorem):
	def __init__(self):
		super(Theorem59, self).__init__(59, "crossing <= (1/4)*(nodes/2)*(nodes-1)/2*(nodes-2)/2*(nodes-3)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["crossing","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('crossing', nodes*(1.5625e-2*nodes**3.0-(9.375e-2*nodes**2.0)+0.171875*nodes-(9.375e-2)), ind='Max')
			except:
				pass
		crossing = ingrid_obj.get('crossing', ind='Min')
		try:
			ingrid_obj.set('nodes', 0.5*(4.0*(64.0*crossing+1.0)**(1/2)+5.0)**(1/2)+1.5, ind='Min')
		except:
			pass
		return

class Theorem60(Theorem):
	def __init__(self):
		super(Theorem60, self).__init__(60, "if defined girth and (nodeConnec > 0 or mindeg > 1) then { genus >= (1/2)*edges(1-2/girth)-(nodes/2)+numOfComponents };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","girth","mindeg","nodeConnec","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (girth_Max != 'undt') and (nodeConnec_Min>0.0) or (mindeg_Min>1.0):
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 0.5*edges(1.0-(2.0/girth))-(0.5*nodes)+1.0*numOfComponents, ind='Min')
				except:
					pass
			genus = ingrid_obj.get('genus', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt':
				try:
					ingrid_obj.set('nodes', -(2.0*genus)+1.0*edges(1.0-(2.0/girth))+2.0*numOfComponents, ind='Min')
				except:
					pass
			genus = ingrid_obj.get('genus', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*genus-(0.5*edges(1.0-(2.0/girth)))+0.5*nodes, ind='Max')
				except:
					pass
		return

