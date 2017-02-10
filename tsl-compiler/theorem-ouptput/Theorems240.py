class Theorem221(Theorem):
	def __init__(self):
		super(Theorem221, self).__init__(221, "chromaticNum <= nodeCover + 1;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeCover"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*nodeCover+1.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('nodeCover', 1.0*chromaticNum-(1.0), ind='Min')
		except:
			pass
		return

class Theorem222(Theorem):
	def __init__(self):
		super(Theorem222, self).__init__(222, "edgeInd <= nodeCover;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","nodeCover"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('edgeInd', nodeCover, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		try:
			ingrid_obj.set('nodeCover', edgeInd, ind='Min')
		except:
			pass
		return

class Theorem223(Theorem):
	def __init__(self):
		super(Theorem223, self).__init__(223, "nodeInd <= nodeCliqueCover;", "")
	def involves(self, str_invar):
		return str_invar in ["nodeCliqueCover","nodeInd"]
	def run(self, ingrid_obj):
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodeCliqueCover, ind='Max')
			except:
				pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		try:
			ingrid_obj.set('nodeCliqueCover', nodeInd, ind='Min')
		except:
			pass
		return

class Theorem224(Theorem):
	def __init__(self):
		super(Theorem224, self).__init__(224, "nodeCliqueCover <= edgeCliqueCover;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","nodeCliqueCover"]
	def run(self, ingrid_obj):
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
		if edgeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', edgeCliqueCover, ind='Max')
			except:
				pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('edgeCliqueCover', nodeCliqueCover, ind='Min')
		except:
			pass
		return

class Theorem225(Theorem):
	def __init__(self):
		super(Theorem225, self).__init__(225, "radius <= diam;", "")
	def involves(self, str_invar):
		return str_invar in ["diam","radius"]
	def run(self, ingrid_obj):
		diam = ingrid_obj.get('diam', ind='Max')
		if diam != 'undt':
			try:
				ingrid_obj.set('radius', diam, ind='Max')
			except:
				pass
		radius = ingrid_obj.get('radius', ind='Min')
		try:
			ingrid_obj.set('diam', radius, ind='Min')
		except:
			pass
		return

class Theorem226(Theorem):
	def __init__(self):
		super(Theorem226, self).__init__(226, "nodeConnec <= edgeConnec;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","nodeConnec"]
	def run(self, ingrid_obj):
		edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
		if edgeConnec != 'undt':
			try:
				ingrid_obj.set('nodeConnec', edgeConnec, ind='Max')
			except:
				pass
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		try:
			ingrid_obj.set('edgeConnec', nodeConnec, ind='Min')
		except:
			pass
		return

class Theorem227(Theorem):
	def __init__(self):
		super(Theorem227, self).__init__(227, "girth <= circumference;", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","girth"]
	def run(self, ingrid_obj):
		circumference = ingrid_obj.get('circumference', ind='Max')
		if circumference != 'undt':
			try:
				ingrid_obj.set('girth', circumference, ind='Max')
			except:
				pass
		girth = ingrid_obj.get('girth', ind='Min')
		try:
			ingrid_obj.set('circumference', girth, ind='Min')
		except:
			pass
		return

class Theorem228(Theorem):
	def __init__(self):
		super(Theorem228, self).__init__(228, "chromaticNum <= circumference;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","circumference"]
	def run(self, ingrid_obj):
		circumference = ingrid_obj.get('circumference', ind='Max')
		if circumference != 'undt':
			try:
				ingrid_obj.set('chromaticNum', circumference, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('circumference', chromaticNum, ind='Min')
		except:
			pass
		return

class Theorem229(Theorem):
	def __init__(self):
		super(Theorem229, self).__init__(229, "genus <= crossing;", "")
	def involves(self, str_invar):
		return str_invar in ["crossing","genus"]
	def run(self, ingrid_obj):
		crossing = ingrid_obj.get('crossing', ind='Max')
		if crossing != 'undt':
			try:
				ingrid_obj.set('genus', crossing, ind='Max')
			except:
				pass
		genus = ingrid_obj.get('genus', ind='Min')
		try:
			ingrid_obj.set('crossing', genus, ind='Min')
		except:
			pass
		return

class Theorem230(Theorem):
	def __init__(self):
		super(Theorem230, self).__init__(230, "mindeg <= circumference - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg"]
	def run(self, ingrid_obj):
		circumference = ingrid_obj.get('circumference', ind='Max')
		if circumference != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*circumference-(1.0), ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('circumference', 1.0*mindeg+1.0, ind='Min')
		except:
			pass
		return

class Theorem231(Theorem):
	def __init__(self):
		super(Theorem231, self).__init__(231, "chromaticNum <= bandwidth + 1;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","chromaticNum"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*bandwidth+1.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('bandwidth', 1.0*chromaticNum-(1.0), ind='Min')
		except:
			pass
		return

class Theorem232(Theorem):
	def __init__(self):
		super(Theorem232, self).__init__(232, "mindeg <= bandwidth;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","mindeg"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('mindeg', bandwidth, ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('bandwidth', mindeg, ind='Min')
		except:
			pass
		return

class Theorem233(Theorem):
	def __init__(self):
		super(Theorem233, self).__init__(233, "nodes <= nodeInd * chromaticNum;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeInd","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if chromaticNum != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', chromaticNum*nodeInd, ind='Max')
			except:
				pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('chromaticNum', nodes/nodeInd, ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodes/chromaticNum, ind='Min')
			except:
				pass
		return

class Theorem234(Theorem):
	def __init__(self):
		super(Theorem234, self).__init__(234, "nodes <= nodeCliqueCover * maxClique;", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if maxClique != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', maxClique*nodeCliqueCover, ind='Max')
			except:
				pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('maxClique', nodes/nodeCliqueCover, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', nodes/maxClique, ind='Min')
			except:
				pass
		return

class Theorem235(Theorem):
	def __init__(self):
		super(Theorem235, self).__init__(235, "edges <= edgeChromatic * edgeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edgeInd","edges"]
	def run(self, ingrid_obj):
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeChromatic != 'undt' and edgeInd != 'undt':
			try:
				ingrid_obj.set('edges', edgeChromatic*edgeInd, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		edges = ingrid_obj.get('edges', ind='Min')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('edgeChromatic', edges/edgeInd, ind='Min')
			except:
				pass
		edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
		edges = ingrid_obj.get('edges', ind='Min')
		if edgeChromatic != 'undt':
			try:
				ingrid_obj.set('edgeInd', edges/edgeChromatic, ind='Min')
			except:
				pass
		return

class Theorem236(Theorem):
	def __init__(self):
		super(Theorem236, self).__init__(236, "edges <= nodeCover * maxdeg;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxdeg","nodeCover"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if maxdeg != 'undt' and nodeCover != 'undt':
			try:
				ingrid_obj.set('edges', maxdeg*nodeCover, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('maxdeg', edges/nodeCover, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('nodeCover', edges/maxdeg, ind='Min')
			except:
				pass
		return

class Theorem237(Theorem):
	def __init__(self):
		super(Theorem237, self).__init__(237, "nodeCover <= bandwidth * nodeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodeCover","nodeInd"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if bandwidth != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodeCover', bandwidth*nodeInd, ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('bandwidth', nodeCover/nodeInd, ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodeCover/bandwidth, ind='Min')
			except:
				pass
		return

class Theorem238(Theorem):
	def __init__(self):
		super(Theorem238, self).__init__(238, "chromaticNum <= spectralRadius + 1;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","spectralRadius"]
	def run(self, ingrid_obj):
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*spectralRadius+1.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('spectralRadius', 1.0*chromaticNum-(1.0), ind='Min')
		except:
			pass
		return

class Theorem239(Theorem):
	def __init__(self):
		super(Theorem239, self).__init__(239, "nodes == nodeCover + nodeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["nodeCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeCover != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', nodeCover+nodeInd, ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', nodeCover+nodeInd, ind='Min')
		except:
			pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', nodes-(nodeInd), ind='Max')
			except:
				pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('nodeCover', nodes-(nodeInd), ind='Min')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodes-(nodeCover), ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('nodeInd', nodes-(nodeCover), ind='Min')
			except:
				pass
		return

class Theorem240(Theorem):
	def __init__(self):
		super(Theorem240, self).__init__(240, "nodes == edgeCover + edgeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","edgeInd","nodes"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeCover != 'undt' and edgeInd != 'undt':
			try:
				ingrid_obj.set('nodes', edgeCover+edgeInd, ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', edgeCover+edgeInd, ind='Min')
		except:
			pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeCover', nodes-(edgeInd), ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('edgeCover', nodes-(edgeInd), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeInd', nodes-(edgeCover), ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('edgeInd', nodes-(edgeCover), ind='Min')
			except:
				pass
		return

