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
				ingrid_obj.set('edges', 1.0*nodeConnec+0.5*nodes**2.0-(1.5*nodes)+1.0, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeConnec', 1.0*edges-(0.5*nodes**2.0)+1.5*nodes-(1.0), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*(2.0*edges-(2.0*nodeConnec)+0.25)**(1/2)+1.5, ind='Max')
			except:
				pass
		return

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
				ingrid_obj.set('chromaticNum', 0.5*maxClique+0.5*nodeCover+0.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('maxClique', 2.0*chromaticNum-(1.0*nodeCover)-(1.0), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('nodeCover', 2.0*chromaticNum-(1.0*maxClique)-(1.0), ind='Min')
			except:
				pass
		return

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
				ingrid_obj.set('edges', 0.5*spectralRadius*nodes, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*edges/spectralRadius, ind='Min')
			except:
				pass
		return

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
				ingrid_obj.set('spectralRadius', 1.4142135623731*(edges*nodeCover/(nodeCover+1.0))**0.5, ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*spectralRadius**2.0*(nodeCover+1.0)/nodeCover, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodeCover', -(0.5*spectralRadius**2.0/(0.5*spectralRadius**2.0-(edges))), ind='Min')
			except:
				pass
		return

class Theorem5(Theorem):
	def __init__(self):
		super(Theorem5, self).__init__(5, "maxClique >= nodes**2/(nodes**2-2*edges);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('maxClique', -(1.0*nodes**2.0/(2.0*edges-(1.0*nodes**2.0))), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*nodes**2.0*(maxClique-(1.0))/maxClique, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('nodes', 1.4142135623731*(maxClique*edges/(maxClique-(1.0)))**0.5, ind='Max')
			except:
				pass
		return

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
		return

class Theorem7(Theorem):
	def __init__(self):
		super(Theorem7, self).__init__(7, "if defined diameter and mindeg > 3*nodeConnec - 1 then { nodes >= 1 + mindeg + diameter*nodeConnec + (diameter/3)*(mindeg - 3*nodeConnec + 1) } else if defined diameter then { nodes >= nodeConnec * (diameter-3) + 2*mindeg + 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Max = ingrid_obj.get('diameter', ind = 'Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (diameter_Max != 'undt') and (nodeConnec_Max != 'undt' and (mindeg_Min>3.0*nodeConnec_Max-(1.0))):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diameter*mindeg+0.333333333333333*diameter+1.0*mindeg+1.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 3.0*(nodes-(mindeg)-(1.0))/(mindeg+1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (1.0*nodes-(0.333333333333333*diameter)-(1.0))/(0.333333333333333*diameter+1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diameter*mindeg+0.333333333333333*diameter+1.0*mindeg+1.0, ind='Min')
			except:
				pass
		elif (diameter_Max != 'undt'):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*diameter*nodeConnec+2.0*mindeg-(3.0*nodeConnec)+2.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', (1.0*nodes-(2.0*mindeg)+3.0*nodeConnec-(2.0))/nodeConnec, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*nodes-(0.5*diameter*nodeConnec)+1.5*nodeConnec-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diameter != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodeConnec', (1.0*nodes-(2.0*mindeg)-(2.0))/(1.0*diameter-(3.0)), ind='Min')
				except:
					pass
		return

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
			ingrid_obj.set('nodes', 1.0*maxdeg+1.0*mindeg*numOfComponents-(1.0*mindeg)+1.0*numOfComponents, ind='Min')
		except:
			pass
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*nodes-(1.0*mindeg*numOfComponents)+1.0*mindeg-(1.0*numOfComponents), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', 1.0*(nodes-(maxdeg)-(numOfComponents))/(numOfComponents-(1.0)), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('numOfComponents', 1.0*(nodes-(maxdeg)+mindeg)/(mindeg+1.0), ind='Max')
			except:
				pass
		return

class Theorem9(Theorem):
	def __init__(self):
		super(Theorem9, self).__init__(9, "edgeCliqueCover <= nodes**2/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 0.25*nodes**2.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*edgeCliqueCover**0.5, ind='Min')
		except:
			pass
		return

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
			ingrid_obj.set('radius', 0.5*diameter, ind='Min')
		except:
			pass
		return

class Theorem11(Theorem):
	def __init__(self):
		super(Theorem11, self).__init__(11, "edgeInd <= nodes / 2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
		except:
			pass
		return

class Theorem12(Theorem):
	def __init__(self):
		super(Theorem12, self).__init__(12, "edgeInd >= nodes/(maxdeg + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('edgeInd', 1.0*nodes/(maxdeg+1.0), ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0)+1.0*nodes/edgeInd, ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if edgeInd != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*edgeInd*(maxdeg+1.0), ind='Max')
			except:
				pass
		return

class Theorem13(Theorem):
	def __init__(self):
		super(Theorem13, self).__init__(13, "if g == 2*d + 1 then { regular };", "")
	def involves(self, str_invar):
		return str_invar in ["d","g","regular"]
	def run(self, ingrid_obj):
		g_Max = ingrid_obj.get('g', ind='Max')
		d_Min = ingrid_obj.get('d', ind='Min')
		g_Min = ingrid_obj.get('g', ind='Min')
		d_Max = ingrid_obj.get('d', ind='Max')
		if (g_Max != 'undt' and (g_Max<=2.0*d_Min+1.0)) and (d_Max != 'undt' and (g_Min>=2.0*d_Max+1.0)):
			ingrid_obj.set('regular', True)
		return

class Theorem14(Theorem):
	def __init__(self):
		super(Theorem14, self).__init__(14, "chromaticNum >= nodes / (nodes - spectralRadius);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodes","spectralRadius"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('chromaticNum', nodes/(nodes-(spectralRadius)), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Max')
		if chromaticNum != 'undt' and spectralRadius != 'undt':
			try:
				ingrid_obj.set('nodes', chromaticNum*spectralRadius/(chromaticNum-(1.0)), ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if chromaticNum != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('spectralRadius', nodes-(nodes/chromaticNum), ind='Max')
			except:
				pass
		return

class Theorem15(Theorem):
	def __init__(self):
		super(Theorem15, self).__init__(15, "if mindeg >= 3 then { edges >= 2**(girth/2) + nodes - numOfComponents };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (mindeg_Min>=3.0):
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('edges', 2.0**(0.5*girth)+nodes-(numOfComponents), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edges != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('girth', 2.88539008177793*log(edges-(nodes)+numOfComponents), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edges != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('nodes', -(2.0**(0.5*girth))+edges+numOfComponents, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 2.0**(0.5*girth)-(edges)+nodes, ind='Min')
				except:
					pass
		return

class Theorem16(Theorem):
	def __init__(self):
		super(Theorem16, self).__init__(16, "if nodeConnec == 0 then { edgeConnec == 0 }; if edgeConnec == 0 then { nodeConnec == 0};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","nodeConnec"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==0.0)):
			try:
				ingrid_obj.set('edgeConnec', 0.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeConnec', 0.0, ind='Min')
			except:
				pass
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
		if (edgeConnec_Max==edgeConnec_Min and (edgeConnec_Min==0.0)):
			try:
				ingrid_obj.set('nodeConnec', 0.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeConnec', 0.0, ind='Min')
			except:
				pass
		return

class Theorem17(Theorem):
	def __init__(self):
		super(Theorem17, self).__init__(17, "edges <= (1/2)*(edgeCliqueCover*maxClique*(maxClique-1));", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","edges","maxClique"]
	def run(self, ingrid_obj):
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if edgeCliqueCover != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*edgeCliqueCover*maxClique*(maxClique-(1.0)), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 2.0*edges/(maxClique*(maxClique-(1.0))), ind='Min')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('maxClique', 0.5+0.5*(edgeCliqueCover*(8.0*edges+1.0*edgeCliqueCover))**(1/2)/edgeCliqueCover, ind='Min')
		except:
			pass
		return

class Theorem18(Theorem):
	def __init__(self):
		super(Theorem18, self).__init__(18, "chromaticNum <= (1/2)*(7+(1+48*genus)**(1/2));", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus"]
	def run(self, ingrid_obj):
		genus = ingrid_obj.get('genus', ind='Max')
		if genus != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 0.5*(48.0*genus+1.0)**0.5+3.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		try:
			ingrid_obj.set('genus', 2.08333333333333e-2*(2.0*chromaticNum-(7.0))**2.0-(2.08333333333333e-2), ind='Min')
		except:
			pass
		return

class Theorem19(Theorem):
	def __init__(self):
		super(Theorem19, self).__init__(19, "if maxClique == 2 then { maxdeg <= nodeInd, edges <= nodeCover * nodeInd };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","maxClique","maxdeg","nodeCover","nodeInd"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', nodeInd, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodeInd', maxdeg, ind='Min')
			except:
				pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeCover != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('edges', nodeCover*nodeInd, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodeCover', edges/nodeInd, ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodeInd', edges/nodeCover, ind='Min')
				except:
					pass
		return

class Theorem20(Theorem):
	def __init__(self):
		super(Theorem20, self).__init__(20, "if chromaticNum == 2 then { edgeInd == nodeCover, nodeInd == nodeCliqueCover, edgeChromatic == maxdeg, even girth, even circumference }; if chromaticNum == 2 and nodes > 2 then { not complete };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","circumference","edgeChromatic","edgeInd","girth","maxdeg","nodeCliqueCover","nodeCover","nodeInd","complete","nodes"]
	def run(self, ingrid_obj):
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		if (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('edgeInd', nodeCover, ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('edgeInd', nodeCover, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeCover', edgeInd, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Min')
			try:
				ingrid_obj.set('nodeCover', edgeInd, ind='Min')
			except:
				pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
			if nodeCliqueCover != 'undt':
				try:
					ingrid_obj.set('nodeInd', nodeCliqueCover, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('nodeInd', nodeCliqueCover, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodeCliqueCover', nodeInd, ind='Max')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			try:
				ingrid_obj.set('nodeCliqueCover', nodeInd, ind='Min')
			except:
				pass
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
			girth_Max = ingrid_obj.get('girth', ind='Max')-1
			girth_Min = ingrid_obj.get('girth', ind='Min')+1
			if even(girth_Max):
				ingrid_obj.set('girth', ind='Max')
			if even(girth_Min):
				ingrid_obj.set('girth', ind='Min')
			circumference_Max = ingrid_obj.get('circumference', ind='Max')-1
			circumference_Min = ingrid_obj.get('circumference', ind='Min')+1
			if even(circumference_Max):
				ingrid_obj.set('circumference', ind='Max')
			if even(circumference_Min):
				ingrid_obj.set('circumference', ind='Min')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (chromaticNum_Max==chromaticNum_Min and (chromaticNum_Min==2.0)) and (nodes_Min>2.0):
			ingrid_obj.set('complete', False)
		return

