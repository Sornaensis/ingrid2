from INGRID_CLASSES import Theorem 

class Theorem1(Theorem):
	def __init__(self):
		super(Theorem1, self).__init__(1, "edges <= (1/2)*(nodes-1)*(nodes-2)+nodeConnec;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeConnec != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', (1.0*1.0*2.0+-1.0*1.0*nodes+-1.0*2.0*nodes+1.0*nodes**2.0+2.0*nodeConnec)/2.0, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeConnec', (edges*2.0+-1.0*1.0*2.0+1.0*1.0*nodes+1.0*2.0*nodes+-1.0*nodes**2.0)/2.0, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		if edges != 'undt' and nodeConnec != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0/2.0+2.0/2.0+(1.0*(4.0*edges*2.0+1.0*1.0**2.0+-2.0*1.0*1.0*2.0+1.0*2.0**2.0+-4.0*2.0*nodeConnec))**(1/2)/(2.0*1.0), ind='Max')
			except:
				pass

class Theorem2(Theorem):
	def __init__(self):
		super(Theorem2, self).__init__(2, "chromaticNum <= (1/2)*(nodeCover+maxClique+1);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodeCover"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if maxClique != 'undt' and nodeCover != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*(1.0+maxClique+nodeCover)/2.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('maxClique', chromaticNum*2.0/1.0+-1.0+-nodeCover, ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('nodeCover', chromaticNum*2.0/1.0+-1.0+-maxClique, ind='Min')
			except:
				pass

class Theorem3(Theorem):
	def __init__(self):
		super(Theorem3, self).__init__(3, "spectralRadius >= 2*edges/nodes;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodes","spectralRadius"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('spectralRadius', 2.0*edges/nodes, ind='Min')
			except:
				pass
		nodes = ingrid_obj.get('nodes', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if nodes != 'undt' and spectralRadius != 'undt':
			try:
				ingrid_obj.set('edges', spectralRadius*nodes/2.0, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*edges/spectralRadius, ind='Min')
			except:
				pass

class Theorem4(Theorem):
	def __init__(self):
		super(Theorem4, self).__init__(4, "spectralRadius <= (2*edges*nodeCover/(nodeCover+1))**(1/2);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodeCover","spectralRadius"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if edges != 'undt' and nodeCover != 'undt':
			try:
				ingrid_obj.set('spectralRadius', 1.4142135623731*(edges*nodeCover/(nodeCover+1.0))**(1/2), ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('edges', 0.499999999999997*spectralRadius**2.0*(nodeCover+1.0)/nodeCover, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('nodeCover', -1.0e26*spectralRadius**2.0/(1.0e26*spectralRadius**2.0+-2.00000000000001e26*edges), ind='Min')
		except:
			pass

class Theorem5(Theorem):
	def __init__(self):
		super(Theorem5, self).__init__(5, "maxClique >= nodes**2/(nodes**2-2*edges);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('maxClique', -nodes**2.0/(2.0*edges+-nodes**2.0), ind='Min')
		except:
			pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', nodes**2.0*(maxClique+-1.0)/(maxClique*2.0), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('nodes', (maxClique*2.0*edges/(maxClique+-1.0))**(1/2), ind='Min')
		except:
			pass

class Theorem6(Theorem):
	def __init__(self):
		super(Theorem6, self).__init__(6, "spectralRadius <= maxdeg;", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","spectralRadius"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('spectralRadius', maxdeg, ind='Max')
			except:
				pass
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('maxdeg', spectralRadius, ind='Min')
		except:
			pass

class Theorem7(Theorem):
	def __init__(self):
		super(Theorem7, self).__init__(7, "if mindeg > 3*nodeConnec - 1 then { nodes >= 1 + mindeg + diameter*nodeConnec + (diameter/3)*(mindeg - 3*nodeConnec + 1) } else { nodes >= nodeConnec * (diameter-3) + 2*mindeg + 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		
		if (nodeConnec_Max != 'undt' and (mindeg_Min>3.0*nodeConnec_Max+-1.0)):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0+diameter*nodeConnec+mindeg+1.0*diameter/3.0+-3.0*diameter*nodeConnec/3.0+diameter*mindeg/3.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 3.0*(nodes+-1.0+-mindeg)/(3.0*nodeConnec+1.0+-3.0*nodeConnec+mindeg), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diameter != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (nodes*3.0+-3.0*1.0+-3.0*diameter*nodeConnec+-1.0*diameter+3.0*diameter*nodeConnec)/(3.0+diameter), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', (nodes*3.0+-3.0*1.0+-3.0*mindeg+-1.0*diameter+-diameter*mindeg)/(diameter*(3.0+-3.0)), ind='Min')
			except:
				pass
		elif (True):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0+2.0*mindeg+-3.0*nodeConnec+diameter*nodeConnec, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', (nodes+-2.0+-2.0*mindeg+3.0*nodeConnec)/nodeConnec, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diameter != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (nodes+-2.0+3.0*nodeConnec+-diameter*nodeConnec)/2.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', (-nodes+2.0+2.0*mindeg)/(3.0+-diameter), ind='Min')
			except:
				pass

                
class Theorem8(Theorem):
	def __init__(self):
		super(Theorem8, self).__init__(8, "nodes >= maxdeg + 1 + (mindeg + 1)*(numOfComponents - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		try:
			ingrid_obj.set('nodes', -1.0*1.0+1.0*numOfComponents+-1.0*mindeg+1.0+maxdeg+mindeg*numOfComponents, ind='Min')
		except:
			pass
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', nodes+1.0*1.0+-1.0*numOfComponents+1.0*mindeg+-1.0+-mindeg*numOfComponents, ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if maxdeg != 'undt' and nodes != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('mindeg', (-nodes+-1.0*1.0+1.0*numOfComponents+1.0+maxdeg)/(1.0+-numOfComponents), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('numOfComponents', (nodes+1.0*1.0+1.0*mindeg+-1.0+-maxdeg)/(1.0+mindeg), ind='Max')
			except:
				pass

class Theorem9(Theorem):
	def __init__(self):
		super(Theorem9, self).__init__(9, "edgeCliqueCover <= nodes**2/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', nodes**2.0/4.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', (edgeCliqueCover*4.0)**(1/2), ind='Min')
		except:
			pass

class Theorem10(Theorem):
	def __init__(self):
		super(Theorem10, self).__init__(10, "diameter <= 2*radius;", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","radius"]
	def run(self, ingrid_obj):
		radius = ingrid_obj.get('radius', ind='Max')
		if radius != 'undt':
			try:
				ingrid_obj.set('diameter', 2.0*radius, ind='Max')
			except:
				pass
		diameter = ingrid_obj.get('diameter', ind='Min')
		try:
			ingrid_obj.set('radius', diameter/2.0, ind='Min')
		except:
			pass

class Theorem11(Theorem):
	def __init__(self):
		super(Theorem11, self).__init__(11, "edgeInd <= nodes / 2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeInd', nodes/2.0, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', edgeInd*2.0, ind='Min')
		except:
			pass

class Theorem12(Theorem):
	def __init__(self):
		super(Theorem12, self).__init__(12, "edgeInd >= nodes/(maxdeg + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edgeInd', nodes/(1.0+maxdeg), ind='Min')
		except:
			pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', -1.0+nodes/edgeInd, ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if edgeInd != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', edgeInd*(1.0+maxdeg), ind='Max')
			except:
				pass

class Theorem13(Theorem):
	def __init__(self):
		super(Theorem13, self).__init__(13, "if g == 3*d + 1 then { regular };", "")
	def involves(self, str_invar):
		return str_invar in ["d","g","regular"]
	def run(self, ingrid_obj):
		g_Max = ingrid_obj.get('g', ind='Max')
		d_Min = ingrid_obj.get('d', ind='Min')
		g_Min = ingrid_obj.get('g', ind='Min')
		d_Max = ingrid_obj.get('d', ind='Max')
		if (g_Max != 'undt' and (g_Max<=3.0*d_Min+1.0)) and (d_Max != 'undt' and (g_Min>=3.0*d_Max+1.0)):
			ingrid_obj.set('regular', True)

