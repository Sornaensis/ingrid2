class Theorem101(Theorem):
	def __init__(self):
		super(Theorem101, self).__init__(101, "if connected or odd nodes then {nodeCover <= (nodes-1)*(nodes+1)/2, edgeCover <= (nodes-1)*(nodes+1)/2 } else {nodeCover <= (nodes-2)*(nodes+2)/2, edgeCover <= (nodes-2)*(nodes+2)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edgeCover","nodeCover","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		
		if (connected == True) or (odd(nodes_Min) and odd(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(0.5), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*(2.0*nodeCover+1.0)**(1/2), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(0.5), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*(2.0*edgeCover+1.0)**(1/2), ind='Min')
			except:
				pass
		elif (True):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(2.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.5*nodes**2.0-(2.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(2.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 0.5*nodes**2.0-(2.0), ind='Max')
				except:
					pass
		return

class Theorem102(Theorem):
	def __init__(self):
		super(Theorem102, self).__init__(102, "edgeChromatic <= 2*bandwidth;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","edgeChromatic"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('edgeChromatic', 2.0*bandwidth, ind='Max')
			except:
				pass
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
		try:
			ingrid_obj.set('bandwidth', 0.5*edgeChromatic, ind='Min')
		except:
			pass
		return

class Theorem103(Theorem):
	def __init__(self):
		super(Theorem103, self).__init__(103, "circumference >= maxClique*mindeg/(maxClique - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","maxClique","mindeg"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('circumference', 1.0*maxClique*mindeg/(maxClique-(1.0)), ind='Min')
		except:
			pass
		circumference = ingrid_obj.get('circumference', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('maxClique', 1.0*circumference/(circumference-(mindeg)), ind='Min')
		except:
			pass
		circumference = ingrid_obj.get('circumference', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if circumference != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*circumference*(maxClique-(1.0))/maxClique, ind='Max')
			except:
				pass
		return

class Theorem104(Theorem):
	def __init__(self):
		super(Theorem104, self).__init__(104, "circumference >= maxClique*(chromaticNum-1)/(maxClique-1);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","circumference","maxClique"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('circumference', 1.0*maxClique*(chromaticNum-(1.0))/(maxClique-(1.0)), ind='Min')
		except:
			pass
		circumference = ingrid_obj.get('circumference', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if circumference != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*circumference-(1.0*circumference/maxClique)+1.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		circumference = ingrid_obj.get('circumference', ind='Min')
		try:
			ingrid_obj.set('maxClique', 1.0*circumference/(circumference-(chromaticNum)+1.0), ind='Min')
		except:
			pass
		return

class Theorem105(Theorem):
	def __init__(self):
		super(Theorem105, self).__init__(105, "if maxClique == 2 and chromaticNum >= 3 then { circumference >= 2*chromaticNum - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","circumference","maxClique"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (chromaticNum_Min>=3.0):
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('circumference', 2.0*chromaticNum-(1.0), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			if circumference != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.5*circumference+0.5, ind='Max')
				except:
					pass
		return

class Theorem106(Theorem):
	def __init__(self):
		super(Theorem106, self).__init__(106, "edges <= nodeCover*(nodeInd + nodeCover*(chromaticNum-1)/(2*chromaticNum));", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges","nodeCover","nodeInd"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if chromaticNum != 'undt' and nodeCover != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', nodeCover*(0.5*chromaticNum*nodeCover+1.0*chromaticNum*nodeInd-(0.5*nodeCover))/chromaticNum, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*nodeCover**2.0/(-(2.0*edges)+1.0*nodeCover**2.0+2.0*nodeCover*nodeInd), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('nodeCover', -((1.0*chromaticNum*nodeInd+1.0*(chromaticNum*(2.0*edges*chromaticNum-(2.0*edges)+1.0*chromaticNum*nodeInd**2.0))**(1/2))/(chromaticNum-(1.0))), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		edges = ingrid_obj.get('edges', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodeInd', 1.0*edges/nodeCover-(0.5*nodeCover)+0.5*nodeCover/chromaticNum, ind='Min')
			except:
				pass
		return

class Theorem107(Theorem):
	def __init__(self):
		super(Theorem107, self).__init__(107, "mindeg<=maxdeg;", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('mindeg', maxdeg, ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('maxdeg', mindeg, ind='Min')
		except:
			pass
		return

class Theorem108(Theorem):
	def __init__(self):
		super(Theorem108, self).__init__(108, "nodeCliqueCover <= (nodes + nodeInd - maxClique + 1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', -(0.5*maxClique)+0.5*nodeInd+0.5*nodes+0.5, ind='Max')
			except:
				pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxClique', -(2.0*nodeCliqueCover)+1.0*nodeInd+1.0*nodes+1.0, ind='Max')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', 2.0*nodeCliqueCover+1.0*maxClique-(1.0*nodes)-(1.0), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*nodeCliqueCover+1.0*maxClique-(1.0*nodeInd)-(1.0), ind='Min')
			except:
				pass
		return

class Theorem109(Theorem):
	def __init__(self):
		super(Theorem109, self).__init__(109, "nodeCover <= 2*edgeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","nodeCover"]
	def run(self, ingrid_obj):
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('nodeCover', 2.0*edgeInd, ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('edgeInd', 0.5*nodeCover, ind='Min')
		except:
			pass
		return

class Theorem110(Theorem):
	def __init__(self):
		super(Theorem110, self).__init__(110, "if mindeg >= 4 and girth >= 5 then { circumference >= (girth-2)*(mindeg-2)+5 };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","girth","mindeg"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Min>=4.0) and (girth_Min>=5.0):
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('circumference', 1.0*girth*mindeg-(2.0*girth)-(2.0*mindeg)+9.0, ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('girth', (1.0*circumference+2.0*mindeg-(9.0))/(1.0*mindeg-(2.0)), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('mindeg', (1.0*circumference+2.0*girth-(9.0))/(1.0*girth-(2.0)), ind='Min')
			except:
				pass
		return

class Theorem111(Theorem):
	def __init__(self):
		super(Theorem111, self).__init__(111, "if connected then { diameter <= 2*nodeInd - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","nodeInd"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('diameter', 2.0*nodeInd-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.5*diameter+0.5, ind='Min')
			except:
				pass
		return

class Theorem112(Theorem):
	def __init__(self):
		super(Theorem112, self).__init__(112, "if connected and nodeInd <= mindeg then { mindeg >= (nodes+2)/3 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (connected == True) and (nodeInd_Max != 'undt' and (nodeInd_Max<=mindeg_Min)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.333333333333333*nodes+0.666666666666667, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 3.0*mindeg-(2.0), ind='Max')
				except:
					pass
		return

class Theorem113(Theorem):
	def __init__(self):
		super(Theorem113, self).__init__(113, "edges >= nodeInd*mindeg + (maxClique-1)*(maxClique-2)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","mindeg","nodeInd"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*maxClique**2.0-(1.5*maxClique)+1.0*mindeg*nodeInd+1.0, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if mindeg != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxClique', 0.5*(8.0*edges-(8.0*mindeg*nodeInd)+1.0)**(1/2)+1.5, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('mindeg', (1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0))/nodeInd, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('nodeInd', (1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0))/mindeg, ind='Max')
			except:
				pass
		return

class Theorem114(Theorem):
	def __init__(self):
		super(Theorem114, self).__init__(114, "edges >= nodeCover + (maxClique-1)*(maxClique-2)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodeCover"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*maxClique**2.0-(1.5*maxClique)+1.0*nodeCover+1.0, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('maxClique', 0.5*(8.0*edges-(8.0*nodeCover)+1.0)**(1/2)+1.5, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*edges-(0.5*maxClique**2.0)+1.5*maxClique-(1.0), ind='Max')
			except:
				pass
		return

class Theorem115(Theorem):
	def __init__(self):
		super(Theorem115, self).__init__(115, "edges >= chromaticNum*(chromaticNum-3)/2 + nodes - numOfComponents + 1;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if numOfComponents != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*chromaticNum**2.0-(1.5*chromaticNum)+1.0*nodes-(1.0*numOfComponents)+1.0, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if edges != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 0.5*(8.0*edges-(8.0*nodes)+8.0*numOfComponents+1.0)**(1/2)+1.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if chromaticNum != 'undt' and edges != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*edges-(0.5*chromaticNum**2.0)+1.5*chromaticNum+1.0*numOfComponents-(1.0), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('numOfComponents', -(1.0*edges)+0.5*chromaticNum**2.0-(1.5*chromaticNum)+1.0*nodes+1.0, ind='Min')
			except:
				pass
		return

class Theorem116(Theorem):
	def __init__(self):
		super(Theorem116, self).__init__(116, "if bipartite and even nodes then {genus <= ((nodes-4)**2 + 15)/16}; if bipartite and odd nodes then { genus <= ((nodes-3)*(nodes-5)+15)/16};", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","genus","nodes"]
	def run(self, ingrid_obj):
		bipartite = ingrid_obj.get('bipartite')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (bipartite == True) and (even(nodes_Min) and even(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 6.25e-2*(nodes-(4.0))**2.0+0.9375, ind='Max')
				except:
					pass
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*(16.0*genus-(15.0))**0.5+4.0, ind='Max')
				except:
					pass
		bipartite = ingrid_obj.get('bipartite')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (bipartite == True) and (odd(nodes_Min) and odd(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 6.25e-2*nodes**2.0-(0.5*nodes)+1.875, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 6.25e-2*nodes**2.0-(0.5*nodes)+1.875, ind='Max')
				except:
					pass
		return

class Theorem117(Theorem):
	def __init__(self):
		super(Theorem117, self).__init__(117, "if not complete then { nodeConnec >= 2*mindeg - nodes + 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["complete","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		complete = ingrid_obj.get('complete')
		if (complete == False):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeConnec', 2.0*mindeg-(1.0*nodes)+2.0, ind='Min')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*nodeConnec+0.5*nodes-(1.0), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodes', -(1.0*nodeConnec)+2.0*mindeg+2.0, ind='Min')
				except:
					pass
		return

class Theorem118(Theorem):
	def __init__(self):
		super(Theorem118, self).__init__(118, "if (nodes>=6 and even nodes and edges >= (nodes**2)/4 +1) or (nodes>=7 and odd nodes  and edges>=(nodes-1)**2/4 +1+mindeg) then { circumference>=5 };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edges","mindeg","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (nodes_Min>=6.0) and (even(nodes_Min) and even(nodes_Max)) and (nodes_Max != 'undt' and (edges_Min>=(nodes_Max**2.0)/4.0+1.0)) or (nodes_Min>=7.0) and (odd(nodes_Min) and odd(nodes_Max)) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>=(nodes_Max-(1.0))**2.0/4.0+1.0+mindeg_Max)):
			try:
				ingrid_obj.set('circumference', 5.0, ind='Min')
			except:
				pass
		return

class Theorem119(Theorem):
	def __init__(self):
		super(Theorem119, self).__init__(119, "if chromaticNum >= maxClique then {mindeg <= (3*maxClique - 4)*nodes / (3*maxClique-1)};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","mindeg","nodes"]
	def run(self, ingrid_obj):
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max != 'undt' and (chromaticNum_Min>=maxClique_Max)):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes*(3.0*maxClique-(4.0))/(3.0*maxClique-(1.0)), ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxClique', (0.333333333333333*mindeg-(1.33333333333333*nodes))/(mindeg-(nodes)), ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if maxClique != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg*(3.0*maxClique-(1.0))/(3.0*maxClique-(4.0)), ind='Max')
				except:
					pass
		return

class Theorem120(Theorem):
	def __init__(self):
		super(Theorem120, self).__init__(120, "if hamiltonian and p>=chromaticNum-1 and chromaticNum >= 4 then { e>= (chromaticNum-1)*(chromaticNum-2)/2 + nodes }; if hamiltonian and chromaticNum==3 and even nodes then {edges >= nodes +1};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","e","hamiltonian","nodes","p","edges"]
	def run(self, ingrid_obj):
		hamiltonian = ingrid_obj.get('hamiltonian')
		p_Min = ingrid_obj.get('p', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		if (hamiltonian == True) and (chromaticNum_Max != 'undt' and (p_Min>=chromaticNum_Max-(1.0))) and (chromaticNum_Min>=4.0):
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('e', 0.5*chromaticNum**2.0-(1.5*chromaticNum)+1.0*nodes+1.0, ind='Min')
			except:
				pass
			e = ingrid_obj.get('e', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.5*(8.0*e-(8.0*nodes)+1.0)**(1/2)+1.5, ind='Min')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
			e = ingrid_obj.get('e', ind='Max')
			if chromaticNum != 'undt' and e != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*e-(0.5*chromaticNum**2.0)+1.5*chromaticNum-(1.0), ind='Max')
				except:
					pass
		hamiltonian = ingrid_obj.get('hamiltonian')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (hamiltonian == True) and (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==3.0)) and (even(nodes_Min) and even(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*nodes+1.0, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edges-(1.0), ind='Max')
				except:
					pass
		return

