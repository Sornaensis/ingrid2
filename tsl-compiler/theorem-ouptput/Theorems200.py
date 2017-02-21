class Theorem181(Theorem):
	def __init__(self):
		super(Theorem181, self).__init__(181, "if nodeCliqueCover > nodeInd then { maxdeg >= 3*nodes/(3*nodeInd - 1) - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max != 'undt' and (nodeCliqueCover_Min>nodeInd_Max)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', (-(3.0*nodeInd)+3.0*nodes+1.0)/(3.0*nodeInd-(1.0)), ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', (maxdeg+3.0*nodes+1.0)/(3.0*(maxdeg+1.0)), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxdeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg*nodeInd-(maxdeg/3.0)+nodeInd-(1.0/3.0), ind='Max')
				except:
					pass
		return

class Theorem182(Theorem):
	def __init__(self):
		super(Theorem182, self).__init__(182, "maxClique >= 2*nodes/(nodes-mindeg+nodeInd);", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('maxClique', 2.0*nodes/(-(mindeg)+nodeInd+nodes), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', nodeInd+nodes-(2.0*nodes/maxClique), ind='Max')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('nodeInd', mindeg-(nodes)+2.0*nodes/maxClique, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', maxClique*(mindeg-(nodeInd))/(maxClique-(2.0)), ind='Min')
			except:
				pass
		return

class Theorem183(Theorem):
	def __init__(self):
		super(Theorem183, self).__init__(183, "if nodeInd <= 2 then { maxClique >= (1/2)*(sqrt(9+8*nodes)-3) };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max != 'undt' and (nodeInd_Max<=2.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxClique', (8.0*nodes+9.0)**(1/2)/2.0-(3.0/2.0), ind='Min')
			except:
				pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			if maxClique != 'undt':
				try:
					ingrid_obj.set('nodes', maxClique*(maxClique+3.0)/2.0, ind='Max')
				except:
					pass
		return

class Theorem184(Theorem):
	def __init__(self):
		super(Theorem184, self).__init__(184, "edges >= (1/2)*nodes*(nodes-1) - (nodes-maxClique)*(nodes-mindeg-1);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","mindeg","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', -(maxClique*mindeg)+maxClique*nodes-(maxClique)+mindeg*nodes-(nodes**2.0/2.0)+nodes/2.0, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('maxClique', (-(edges)+mindeg*nodes-(nodes**2.0/2.0)+nodes/2.0)/(mindeg-(nodes)+1.0), ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', (-(edges)+maxClique*nodes-(maxClique)-(nodes**2.0/2.0)+nodes/2.0)/(maxClique-(nodes)), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodes', maxClique+mindeg+(-(8.0*edges)+4.0*maxClique**2.0-(4.0*maxClique)+4.0*mindeg**2.0+4.0*mindeg+1.0)**(1/2)/2.0+1.0/2.0, ind='Min')
			except:
				pass
		return

class Theorem185(Theorem):
	def __init__(self):
		super(Theorem185, self).__init__(185, "if nodeCliqueCover <= 2 then { maxClique == chromaticNum };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodeCliqueCover"]
	def run(self, ingrid_obj):
		nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if (nodeCliqueCover_Max != 'undt' and (nodeCliqueCover_Max<=2.0)):
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
			if chromaticNum != 'undt':
				try:
					ingrid_obj.set('maxClique', chromaticNum, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('maxClique', chromaticNum, ind='Min')
			except:
				pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			if maxClique != 'undt':
				try:
					ingrid_obj.set('chromaticNum', maxClique, ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			try:
				ingrid_obj.set('chromaticNum', maxClique, ind='Min')
			except:
				pass
		return

class Theorem186(Theorem):
	def __init__(self):
		super(Theorem186, self).__init__(186, "if nodeInd == 2 and nodeCliqueCover >= 4 then { nodes >= 11 };", "")
	def involves(self, str_invar):
		return str_invar in ["nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)) and (nodeCliqueCover_Min>=4.0):
			try:
				ingrid_obj.set('nodes', 11.0, ind='Min')
			except:
				pass
		return

class Theorem187(Theorem):
	def __init__(self):
		super(Theorem187, self).__init__(187, "if regular and maxdeg <= nodes - 2 then { maxClique <= (1/2)*nodes-(nodeInd - 1)*(nodeInd - 2)/(2*(nodes - maxdeg - 1)) };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","nodeInd","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (regular == True) and (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min-(2.0))):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxClique', (maxdeg*nodes+nodeInd**2.0-(3.0*nodeInd)-(nodes**2.0)+nodes+2.0)/(2.0*(maxdeg-(nodes)+1.0)), ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodeInd != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', (2.0*maxClique*nodes-(2.0*maxClique)+nodeInd**2.0-(3.0*nodeInd)-(nodes**2.0)+nodes+2.0)/(2.0*maxClique-(nodes)), ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', (8.0*maxClique*maxdeg-(8.0*maxClique*nodes)+8.0*maxClique-(4.0*maxdeg*nodes)+4.0*nodes**2.0-(4.0*nodes)+1.0)**(1/2)/2.0+3.0/2.0, ind='Min')
			except:
				pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxClique != 'undt' and maxdeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', maxClique+maxdeg/2.0+(4.0*maxClique**2.0-(4.0*maxClique*maxdeg)-(4.0*maxClique)+maxdeg**2.0+2.0*maxdeg+4.0*nodeInd**2.0-(12.0*nodeInd)+9.0)**(1/2)/2.0+1.0/2.0, ind='Max')
				except:
					pass
		return

class Theorem188(Theorem):
	def __init__(self):
		super(Theorem188, self).__init__(188, "if undefined girth then { thickness == 1 } else { thickness >= edges*(1-2/girth)/(nodes - 2) };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","nodes","thickness"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind = 'Min')
		
		if (girth_Min == 'undt'):
			try:
				ingrid_obj.set('thickness', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('thickness', 1.0, ind='Min')
			except:
				pass
		elif (True):
			edges = ingrid_obj.get('edges', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('thickness', edges*(girth-(2.0))/(girth*(nodes-(2.0))), ind='Min')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Max')
			if girth != 'undt' and nodes != 'undt' and thickness != 'undt':
				try:
					ingrid_obj.set('edges', thickness*girth*(nodes-(2.0))/(girth-(2.0)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('girth', 2.0*edges/(-(thickness*nodes)+2.0*thickness+edges), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0+edges/thickness-(2.0*edges/(thickness*girth)), ind='Min')
			except:
				pass
		return

class Theorem189(Theorem):
	def __init__(self):
		super(Theorem189, self).__init__(189, "if nodes > 10 or nodes < 9 then { thickness <= (nodes+7)/6 } else if nodes == 9 or nodes == 10 then { thickness <= 3 };", "")
	def involves(self, str_invar):
		return str_invar in ["nodes","thickness"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Min>10.0) or (nodes_Max != 'undt' and (nodes_Max<9.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('thickness', nodes/6.0+7.0/6.0, ind='Max')
				except:
					pass
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('nodes', 6.0*thickness-(7.0), ind='Min')
			except:
				pass
		elif (nodes_Max==nodes_Min and (nodes_Min==9.0)) or (nodes_Max==nodes_Min and (nodes_Min==10.0)):
			try:
				ingrid_obj.set('thickness', 3.0, ind='Max')
			except:
				pass
		return

class Theorem190(Theorem):
	def __init__(self):
		super(Theorem190, self).__init__(190, "thickness <= (1/2)*(edgeChromatic + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","thickness"]
	def run(self, ingrid_obj):
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
		if edgeChromatic != 'undt':
			try:
				ingrid_obj.set('thickness', edgeChromatic/2.0+1.0/2.0, ind='Max')
			except:
				pass
		thickness = ingrid_obj.get('thickness', ind='Min')
		try:
			ingrid_obj.set('edgeChromatic', 2.0*thickness-(1.0), ind='Min')
		except:
			pass
		return

class Theorem191(Theorem):
	def __init__(self):
		super(Theorem191, self).__init__(191, "thickness <= max(bandwidth/2,1);", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","thickness"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('thickness', max(bandwidth/2.0, 1.0), ind='Max')
			except:
				pass
		return

class Theorem192(Theorem):
	def __init__(self):
		super(Theorem192, self).__init__(192, "if maxClique == 2 then { nodeInd >= mindeg * (diameter+4)/4 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxClique","mindeg","nodeInd"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodeInd', mindeg*(diameter+4.0)/4.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('diameter', 4.0*nodeInd/mindeg-(4.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('mindeg', 4.0*nodeInd/(diameter+4.0), ind='Max')
				except:
					pass
		return

class Theorem193(Theorem):
	def __init__(self):
		super(Theorem193, self).__init__(193, "thickness <= (1/2)*(nodeCover+1);", "")
	def involves(self, str_invar):
		return str_invar in ["nodeCover","thickness"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('thickness', nodeCover/2.0+1.0/2.0, ind='Max')
			except:
				pass
		thickness = ingrid_obj.get('thickness', ind='Min')
		try:
			ingrid_obj.set('nodeCover', 2.0*thickness-(1.0), ind='Min')
		except:
			pass
		return

class Theorem194(Theorem):
	def __init__(self):
		super(Theorem194, self).__init__(194, "if maxClique == 9 or maxClique == 10 then { thickness >= 3 } else { thickness >= (maxClique + 7)/6 };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","thickness"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		
		if (maxClique_Max==maxClique_Min and (maxClique_Min==9.0)) or (maxClique_Max==maxClique_Min and (maxClique_Min==10.0)):
			try:
				ingrid_obj.set('thickness', 3.0, ind='Min')
			except:
				pass
		elif (True):
			maxClique = ingrid_obj.get('maxClique', ind='Min')
			try:
				ingrid_obj.set('thickness', maxClique/6.0+7.0/6.0, ind='Min')
			except:
				pass
			thickness = ingrid_obj.get('thickness', ind='Max')
			if thickness != 'undt':
				try:
					ingrid_obj.set('maxClique', 6.0*thickness-(7.0), ind='Max')
				except:
					pass
		return

class Theorem195(Theorem):
	def __init__(self):
		super(Theorem195, self).__init__(195, "maxClique >= nodes + (1/2)*(nodeInd-1)*(nodeInd-2)+(nodes/2)*(nodes-1)+edges;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('maxClique', edges+nodeInd**2.0/2.0-(3.0*nodeInd/2.0)+nodes**2.0/2.0+nodes/2.0+1.0, ind='Min')
		except:
			pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', maxClique-(nodeInd**2.0/2.0)+3.0*nodeInd/2.0-(nodes**2.0/2.0)-(nodes/2.0)-(1.0), ind='Max')
			except:
				pass
		return

class Theorem196(Theorem):
	def __init__(self):
		super(Theorem196, self).__init__(196, "edges <= (nodes/2)*(nodes-1)-maxClique*(nodes-maxdeg-1)-(1/2)*(nodeInd-1)*(nodeInd-2);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', maxClique*maxdeg-(maxClique*nodes)+maxClique-(nodeInd**2.0/2.0)+3.0*nodeInd/2.0+nodes**2.0/2.0-(nodes/2.0)-(1.0), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('maxClique', (2.0*edges+nodeInd**2.0-(3.0*nodeInd)-(nodes**2.0)+nodes+2.0)/(2.0*(maxdeg-(nodes)+1.0)), ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('maxdeg', (2.0*edges+2.0*maxClique*nodes-(2.0*maxClique)+nodeInd**2.0-(3.0*nodeInd)-(nodes**2.0)+nodes+2.0)/(2.0*maxClique), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxClique != 'undt' and maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', (-(8.0*edges)+8.0*maxClique*maxdeg-(8.0*maxClique*nodes)+8.0*maxClique+4.0*nodes**2.0-(4.0*nodes)+1.0)**(1/2)/2.0+3.0/2.0, ind='Max')
			except:
				pass
		return

class Theorem197(Theorem):
	def __init__(self):
		super(Theorem197, self).__init__(197, "if nodes >= 3 then { edgeCliqueCover <= thickness*(2*nodes-numOfComponents-3) };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","nodes","numOfComponents","thickness"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodes_Min>=3.0):
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			thickness = ingrid_obj.get('thickness', ind='Max')
			if nodes != 'undt' and thickness != 'undt':
				try:
					ingrid_obj.set('edgeCliqueCover', thickness*(2.0*nodes-(numOfComponents)-(3.0)), ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('nodes', (edgeCliqueCover+numOfComponents*thickness+3.0*thickness)/(2.0*thickness), ind='Min')
			except:
				pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Max')
			if nodes != 'undt' and thickness != 'undt':
				try:
					ingrid_obj.set('numOfComponents', -(edgeCliqueCover/thickness)+2.0*nodes-(3.0), ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('thickness', edgeCliqueCover/(2.0*nodes-(numOfComponents)-(3.0)), ind='Min')
				except:
					pass
		return

class Theorem198(Theorem):
	def __init__(self):
		super(Theorem198, self).__init__(198, "nodeCover <= nodes - nodes/chromaticNum;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeCover","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', nodes-(nodes/chromaticNum), ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('chromaticNum', -(nodes/(nodeCover-(nodes))), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('nodes', nodeCover*chromaticNum/(chromaticNum-(1.0)), ind='Min')
		except:
			pass
		return

class Theorem199(Theorem):
	def __init__(self):
		super(Theorem199, self).__init__(199, "bandwidth <= nodes - 1 - (nodes - nodeCover)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodeCover","nodes"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('bandwidth', nodeCover/2.0+nodes/2.0-(1.0), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 2.0*bandwidth-(nodes)+2.0, ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*bandwidth-(nodeCover)+2.0, ind='Min')
			except:
				pass
		return

class Theorem200(Theorem):
	def __init__(self):
		super(Theorem200, self).__init__(200, "if nodes > 2*edgeInd + 1 then { nodeCover <= 2*edgeInd - nodeConnec };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","nodeConnec","nodeCover","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
		if (edgeInd_Max != 'undt' and (nodes_Min>2.0*edgeInd_Max+1.0)):
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeCover', 2.0*edgeInd-(nodeConnec), ind='Max')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('edgeInd', nodeCover/2.0+nodeConnec/2.0, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeConnec', -(nodeCover)+2.0*edgeInd, ind='Max')
				except:
					pass
		return

