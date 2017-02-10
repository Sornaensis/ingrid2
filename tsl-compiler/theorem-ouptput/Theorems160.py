TypeError('unorderable types: float() <= complex()',)
TypeError('unorderable types: float() <= complex()',)
TypeError('unorderable types: float() <= complex()',)
class Theorem141(Theorem):
	def __init__(self):
		super(Theorem141, self).__init__(141, "circumference >= 2*edges/(nodes-1);", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edges","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('circumference', 2.0*edges/(nodes-(1.0)), ind='Min')
			except:
				pass
		circumference = ingrid_obj.get('circumference', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if circumference != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*circumference*(nodes-(1.0)), ind='Max')
			except:
				pass
		circumference = ingrid_obj.get('circumference', ind='Max')
		edges = ingrid_obj.get('edges', ind='Min')
		if circumference != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0+2.0*edges/circumference, ind='Min')
			except:
				pass
		return

class Theorem142(Theorem):
	def __init__(self):
		super(Theorem142, self).__init__(142, "if edges >= nodes + 1 + (1/2)*(nodes**(3/2)) then {girth <= 4};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","nodes"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (edges_Min>=nodes_Max+1.0+(1.0/2.0)*(nodes_Max**(3.0/2.0)))):
			try:
				ingrid_obj.set('girth', 4.0, ind='Max')
			except:
				pass
		return

class Theorem143(Theorem):
	def __init__(self):
		super(Theorem143, self).__init__(143, "nodeCliqueCover <= (1/2) + sqrt(1/4 + nodes**2 - nodes - 2*edges);", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem144(Theorem):
	def __init__(self):
		super(Theorem144, self).__init__(144, "chromaticNum <= 1/2 + sqrt(1/4 + 2*edges);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		if edges != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*(2.0*edges+0.25)**0.5+0.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*(1.0*chromaticNum-(0.5))**2.0-(0.125), ind='Min')
		except:
			pass
		return

class Theorem145(Theorem):
	def __init__(self):
		super(Theorem145, self).__init__(145, "if maxClique == 2 then {nodeInd >= 1/2 * sqrt(8*nodes + 9) - 3};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.5*(8.0*nodes+9.0)**0.5-(3.0), ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*(1.0*nodeInd+3.0)**2.0-(1.125), ind='Max')
				except:
					pass
		return

class Theorem146(Theorem):
	def __init__(self):
		super(Theorem146, self).__init__(146, "if connected then {bandwidth <= nodes - diam};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","connected","diam","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			diam = ingrid_obj.get('diam', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('bandwidth', -(diam)+nodes, ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diam', -(bandwidth)+nodes, ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			diam = ingrid_obj.get('diam', ind='Min')
			try:
				ingrid_obj.set('nodes', bandwidth+diam, ind='Min')
			except:
				pass
		return

class Theorem147(Theorem):
	def __init__(self):
		super(Theorem147, self).__init__(147, "if maxClique == 2 and (maxdeg >= nodes-2 or nodes <= 4) then {chromaticNum <= 2} else if maxClique == 2 and nodes >= 5 and nodes <= 10 then {chromaticNum <= 3} else if maxClique == 2 then {chromaticNum <= (nodes - maxdeg + 10)/4};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max-(2.0))) or (nodes_Max != 'undt' and (nodes_Max<=4.0)):
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Max')
			except:
				pass
		elif (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (nodes_Min>=5.0) and (nodes_Max != 'undt' and (nodes_Max<=10.0)):
			try:
				ingrid_obj.set('chromaticNum', 3.0, ind='Max')
			except:
				pass
		elif (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', -(0.25*maxdeg)+0.25*nodes+2.5, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(4.0*chromaticNum)+1.0*nodes+10.0, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 4.0*chromaticNum+1.0*maxdeg-(10.0), ind='Min')
			except:
				pass
		return

class Theorem148(Theorem):
	def __init__(self):
		super(Theorem148, self).__init__(148, "if mindeg == 3 and maxdeg == 3 and planar and edgeConnec >= 2 then {edgeChromatic == maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edgeConnec","maxdeg","mindeg","planar"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		planar = ingrid_obj.get('planar')
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		if (mindeg_Max==mindeg_Min and (mindeg_Min==3.0)) and (maxdeg_Max==maxdeg_Min and (maxdeg_Min==3.0)) and (planar == True) and (edgeConnec_Min>=2.0):
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

class Theorem149(Theorem):
	def __init__(self):
		super(Theorem149, self).__init__(149, "if planar and maxdeg >= 8 then {edgeChromatic == maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (planar == True) and (maxdeg_Min>=8.0):
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

class Theorem150(Theorem):
	def __init__(self):
		super(Theorem150, self).__init__(150, "if spectralRadius <= maxdeg/2 then {edgeChromatic == maxdeg};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg","spectralRadius"]
	def run(self, ingrid_obj):
		spectralRadius_Max = ingrid_obj.get('spectralRadius', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (spectralRadius_Max != 'undt' and (spectralRadius_Max<=maxdeg_Min/2.0)):
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

class Theorem151(Theorem):
	def __init__(self):
		super(Theorem151, self).__init__(151, "if nodes > 2 and regular and nodeConnec == 1 then { edgeChromatic == maxdeg + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","maxdeg","nodeConnec","nodes","regular"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		regular = ingrid_obj.get('regular')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (nodes_Min>2.0) and (regular == True) and (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==1.0)):
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

class Theorem152(Theorem):
	def __init__(self):
		super(Theorem152, self).__init__(152, "if maxClique == 2 and nodeInd >= 2*nodes/5 and nodeInd <= nodes/2 then { edges <= nodeInd**2 + 4*(nodes/2 - nodeInd)**2 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (nodes_Max != 'undt' and (nodeInd_Min>=2.0*nodes_Max/5.0)) and (nodeInd_Max != 'undt' and (nodeInd_Max<=nodes_Min/2.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', nodeInd**2.0+4.0*(-(nodeInd)+0.5*nodes)**2.0, ind='Max')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 4.0*(-((nodeInd))+nodes/2.0)**2.0+nodeInd**2.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if edges != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*nodeInd+1.0*(edges-(nodeInd**2.0))**0.5, ind='Max')
				except:
					pass
		return

class Theorem153(Theorem):
	def __init__(self):
		super(Theorem153, self).__init__(153, "bandwidth <= maxdeg*(maxdeg - 1)**(radius - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","maxdeg","radius"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		radius = ingrid_obj.get('radius', ind='Max')
		if maxdeg != 'undt' and radius != 'undt':
			try:
				ingrid_obj.set('bandwidth', maxdeg*(maxdeg-(1.0))**(radius-(1.0)), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		radius = ingrid_obj.get('radius', ind='Max')
		if maxdeg != 'undt' and radius != 'undt':
			try:
				ingrid_obj.set('bandwidth', maxdeg*(-((1.0))+maxdeg)**(-((1.0))+radius), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		radius = ingrid_obj.get('radius', ind='Max')
		if maxdeg != 'undt' and radius != 'undt':
			try:
				ingrid_obj.set('bandwidth', maxdeg*(-((1.0))+maxdeg)**(-((1.0))+radius), ind='Max')
			except:
				pass
		return

class Theorem154(Theorem):
	def __init__(self):
		super(Theorem154, self).__init__(154, "if maxdeg >= 3 then { nodes <= 1 + maxdeg*((maxdeg - 1)**diameter - 1 )/(maxdeg - 2) };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (maxdeg_Min>=3.0):
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', (maxdeg*(maxdeg-(1.0))**diameter-(2.0))/(maxdeg-(2.0)), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg*(-((1.0))+(-((1.0))+maxdeg)**diameter)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg*(-((1.0))+(-((1.0))+maxdeg)**diameter)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
		return

class Theorem155(Theorem):
	def __init__(self):
		super(Theorem155, self).__init__(155, "if mindeg == 2 then { nodes <= (2 + max(4, maxdeg))/edgeInd/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (mindeg_Max==mindeg_Min and (mindeg_Min==2.0)):
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if edgeInd != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', (0.5*max(4.0, maxdeg)+1.0)/edgeInd, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeInd', (0.5*max(4.0, maxdeg)+1.0)/nodes, ind='Max')
				except:
					pass
		return

class Theorem156(Theorem):
	def __init__(self):
		super(Theorem156, self).__init__(156, "if mindeg <= nodes/2 then { edgeInd >= mindeg };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (mindeg_Max != 'undt' and (mindeg_Max<=nodes_Min/2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('edgeInd', mindeg, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('mindeg', edgeInd, ind='Max')
				except:
					pass
		return

class Theorem157(Theorem):
	def __init__(self):
		super(Theorem157, self).__init__(157, "if maxClique <= (mindeg - 1)/2 then { chromaticNum <= maxdeg - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","maxdeg","mindeg"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (maxClique_Max != 'undt' and (maxClique_Max<=(mindeg_Min-(1.0))/2.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 1.0*maxdeg-(1.0), ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 1.0*chromaticNum+1.0, ind='Min')
			except:
				pass
		return

class Theorem158(Theorem):
	def __init__(self):
		super(Theorem158, self).__init__(158, "if connected and edges <= nodes + 3 then { genus <= 0 } else if connected and edges <= nodes + 6 then { genus <= 1 } else if connected and edges <= nodes + 9 then { genus <= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edges","genus","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (connected == True) and (edges_Max != 'undt' and (edges_Max<=nodes_Min+3.0)):
			try:
				ingrid_obj.set('genus', 0.0, ind='Max')
			except:
				pass
		elif (connected == True) and (edges_Max != 'undt' and (edges_Max<=nodes_Min+6.0)):
			try:
				ingrid_obj.set('genus', 1.0, ind='Max')
			except:
				pass
		elif (connected == True) and (edges_Max != 'undt' and (edges_Max<=nodes_Min+9.0)):
			try:
				ingrid_obj.set('genus', 2.0, ind='Max')
			except:
				pass
		return

class Theorem159(Theorem):
	def __init__(self):
		super(Theorem159, self).__init__(159, "nodeInd >= (nodes - 1)/(maxdeg + 1) + 1/(mindeg + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeInd', 1.0*(maxdeg+mindeg*nodes-(mindeg)+nodes)/(maxdeg*mindeg+maxdeg+mindeg+1.0), ind='Min')
		except:
			pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*(-(nodeInd*mindeg)-(nodeInd)+mindeg*nodes-(mindeg)+nodes)/(nodeInd*mindeg+nodeInd-(1.0)), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*(-(nodeInd*maxdeg)-(nodeInd)+maxdeg+nodes)/(nodeInd*maxdeg+nodeInd-(nodes)+1.0), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*(nodeInd*maxdeg*mindeg+nodeInd*maxdeg+nodeInd*mindeg+nodeInd-(maxdeg)+mindeg)/(mindeg+1.0), ind='Max')
			except:
				pass
		return

class Theorem160(Theorem):
	def __init__(self):
		super(Theorem160, self).__init__(160, "if maxClique == 2 and maxdeg >= 3 then { nodeInd >= nodes/(maxdeg - (1/5)) } else if maxClique == 2 and nodes >= 3 and connected and (not cycle or (cycle and isset nodes and even nodes)) and (edges >= nodes or maxdeg > 2 or (isset nodes and odd nodes)) then { nodeInd >= nodes/maxdeg - 1/(maxdeg+1) + 1/(mindeg + 1) };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","cycle","edges","maxClique","maxdeg","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		connected = ingrid_obj.get('connected')
		cycle = ingrid_obj.get('cycle')
		nodes_Min = ingrid_obj.get('nodes', ind = 'Min')
		nodes_Max = ingrid_obj.get('nodes', ind = 'Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (maxdeg_Min>=3.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodeInd', 1.0*nodes/(1.0*maxdeg-(0.2)), ind='Min')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', 0.2+1.0*nodes/nodeInd, ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxdeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', nodeInd*(1.0*maxdeg-(0.2)), ind='Max')
				except:
					pass
		elif (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (nodes_Min>=3.0) and (connected == True) and (cycle == False) or (cycle == True) and (nodes_Min == nodes_Max) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (edges_Min>=nodes_Max)) or (maxdeg_Min>2.0) or (nodes_Min == nodes_Max) and (odd(nodes_Min) and odd(nodes_Max)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 1.0*(maxdeg**2.0+maxdeg*mindeg*nodes-(maxdeg*mindeg)+maxdeg*nodes+mindeg*nodes+nodes)/(maxdeg*(maxdeg*mindeg+maxdeg+mindeg+1.0)), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 0.5*(-(nodeInd*mindeg)-(nodeInd)+mindeg*nodes-(mindeg)+nodes+(1.0*nodeInd**2.0*mindeg**2.0+2.0*nodeInd**2.0*mindeg+1.0*nodeInd**2.0+2.0*nodeInd*mindeg**2.0*nodes+2.0*nodeInd*mindeg**2.0+4.0*nodeInd*mindeg*nodes+2.0*nodeInd*mindeg+2.0*nodeInd*nodes+1.0*mindeg**2.0*nodes**2.0-(2.0*mindeg**2.0*nodes)+1.0*mindeg**2.0+2.0*mindeg*nodes**2.0-(6.0*mindeg*nodes)+1.0*nodes**2.0-(4.0*nodes))**(1/2))/(nodeInd*mindeg+nodeInd-(1.0)), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*(-(nodeInd*maxdeg**2.0)-(nodeInd*maxdeg)+maxdeg**2.0+maxdeg*nodes+nodes)/(nodeInd*maxdeg**2.0+nodeInd*maxdeg-(maxdeg*nodes)+maxdeg-(nodes)), ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxdeg != 'undt' and mindeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*maxdeg*(nodeInd*maxdeg*mindeg+nodeInd*maxdeg+nodeInd*mindeg+nodeInd-(maxdeg)+mindeg)/(maxdeg*mindeg+maxdeg+mindeg+1.0), ind='Max')
				except:
					pass
		return

