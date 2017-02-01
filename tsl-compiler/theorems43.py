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
				ingrid_obj.set('edges', nodeConnec+0.5*nodes**2.0+-(1.5*nodes)+1.0, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeConnec', edges+-(0.5*nodes**2.0)+1.5*nodes+-(1.0), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodes', 0.5*(8.0*edges+-(8.0*nodeConnec)+1.0)**(1/2)+1.5, ind='Min')
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
				ingrid_obj.set('chromaticNum', 0.5*maxClique+0.5*nodeCover+0.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('maxClique', 2.0*chromaticNum+-(nodeCover)+-(1.0), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if maxClique != 'undt':
			try:
				ingrid_obj.set('nodeCover', 2.0*chromaticNum+-(maxClique)+-(1.0), ind='Min')
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

class Theorem4(Theorem):
	def __init__(self):
		super(Theorem4, self).__init__(4, "edges >= spectralRadius**2*(nodeCover+1)/(2*nodeCover);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodeCover","spectralRadius"]
	def run(self, ingrid_obj):
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*spectralRadius**2.0*(nodeCover+1.0)/nodeCover, ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		if spectralRadius != 'undt':
			try:
				ingrid_obj.set('nodeCover', spectralRadius**2.0/(2.0*edges+-(spectralRadius**2.0)), ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if edges != 'undt' and nodeCover != 'undt':
			try:
				ingrid_obj.set('spectralRadius', 1.4142135623731*(edges*nodeCover/(nodeCover+1.0))**(1/2), ind='Max')
			except:
				pass

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
				ingrid_obj.set('maxClique', -(nodes**2.0/(2.0*edges+-(nodes**2.0))), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		try:
			ingrid_obj.set('edges', 0.5*nodes**2.0*(maxClique+-(1.0))/maxClique, ind='Max')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('nodes', 1.4142135623731*(maxClique*edges/(maxClique+-(1.0)))**(1/2), ind='Min')
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
		
		if (nodeConnec_Max != 'undt' and (mindeg_Min>3.0*nodeConnec_Max+-(1.0))):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diameter*mindeg+0.333333333333333*diameter+mindeg+1.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', 3.0*(nodes+-(mindeg)+-(1.0))/(mindeg+1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (3.0*nodes+-(diameter)+-(3.0))/(diameter+3.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*diameter*mindeg+0.333333333333333*diameter+mindeg+1.0, ind='Min')
			except:
				pass
		elif (True):
			diameter = ingrid_obj.get('diameter', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', diameter*nodeConnec+2.0*mindeg+-(3.0*nodeConnec)+2.0, ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', (nodes+-(2.0*mindeg)+3.0*nodeConnec+-(2.0))/nodeConnec, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*nodes+-(0.5*diameter*nodeConnec)+1.5*nodeConnec+-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diameter != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodeConnec', (nodes+-(2.0*mindeg)+-(2.0))/(diameter+-(3.0)), ind='Min')
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
			ingrid_obj.set('nodes', maxdeg+mindeg*numOfComponents+-(mindeg)+numOfComponents, ind='Min')
		except:
			pass
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', nodes+-(mindeg*numOfComponents)+mindeg+-(numOfComponents), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if maxdeg != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('mindeg', (nodes+-(maxdeg)+-(numOfComponents))/(numOfComponents+-(1.0)), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('numOfComponents', (nodes+-(maxdeg)+mindeg)/(mindeg+1.0), ind='Max')
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
				ingrid_obj.set('edgeCliqueCover', 0.25*nodes**2.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*(edgeCliqueCover)**(1/2), ind='Min')
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
			ingrid_obj.set('radius', 0.5*diameter, ind='Min')
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
				ingrid_obj.set('edgeInd', 0.5*nodes, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*edgeInd, ind='Min')
		except:
			pass

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
				ingrid_obj.set('edgeInd', nodes/(maxdeg+1.0), ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', (-(edgeInd)+nodes)/edgeInd, ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if edgeInd != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', edgeInd*(maxdeg+1.0), ind='Max')
			except:
				pass

class Theorem13(Theorem):
	def __init__(self):
		super(Theorem13, self).__init__(13, "if g == 2*d + 1 then { regular };", "")
	def involves(self, str_invar):
		return str_invar in ["d","g","regular"]
	def run(self, ingrid_obj):
                return
		# g_Max = ingrid_obj.get('g', ind='Max')
		# d_Min = ingrid_obj.get('d', ind='Min')
		# g_Min = ingrid_obj.get('g', ind='Min')
		# d_Max = ingrid_obj.get('d', ind='Max')
		# if (g_Max != 'undt' and (g_Max<=2.0*d_Min+1.0)) and (d_Max != 'undt' and (g_Min>=2.0*d_Max+1.0)):
		# 	ingrid_obj.set('regular', True)

class Theorem14(Theorem):
	def __init__(self):
		super(Theorem14, self).__init__(14, "theta1 <= p**2/4;", "chromaticNum >= nodes / (nodes - spectralRadius);")
	def involves(self, str_invar):
		return str_invar in ["p","theta1"]
	def run(self, ingrid_obj):
                return
		# p = ingrid_obj.get('p', ind='Max')
		# if p != 'undt':
		# 	try:
		# 		ingrid_obj.set('theta1', 0.25*p**2.0, ind='Max')
		# 	except:
		# 		pass
		# theta1 = ingrid_obj.get('theta1', ind='Min')
		# try:
		# 	ingrid_obj.set('p', 2.0*(theta1)**(1/2), ind='Min')
		# except:
		# 	pass

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
					ingrid_obj.set('edges', 2.0**(girth/2.0)+nodes+-(numOfComponents), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edges != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('girth', 2.88539008177793*log(edges+-(nodes)+numOfComponents), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if edges != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('nodes', -(2.0**(girth/2.0))+edges+numOfComponents, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 2.0**(girth/2.0)+-(edges)+nodes, ind='Min')
				except:
					pass

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
				ingrid_obj.set('edges', 0.5*edgeCliqueCover*maxClique*(maxClique+-(1.0)), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if edges != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 2.0*edges/(maxClique*(maxClique+-(1.0))), ind='Min')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('maxClique', 0.5+0.5*(edgeCliqueCover*(8.0*edges+edgeCliqueCover))**(1/2)/edgeCliqueCover, ind='Min')
		except:
			pass

class Theorem18(Theorem):
	def __init__(self):
		super(Theorem18, self).__init__(18, "chromaticNum <= (1/2)*(7+(1+48*genus)**(1/2));", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus"]
	def run(self, ingrid_obj):
		genus = ingrid_obj.get('genus', ind='Max')
		if genus != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 0.5*(48.0*genus+1.0)**(1/2)+3.5, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('genus', 2.08333333333333e-2*(2.0*chromaticNum+-(7.0))**2.0+-(2.08333333333333e-2), ind='Min')
			except:
				pass

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

class Theorem20(Theorem):
	def __init__(self):
		super(Theorem20, self).__init__(20, "if chromaticNum == 2 then { edgeInd == nodeCover, nodeInd == nodeCliqueCover, edgeChromatic == maxDeg, even girth, even circumference }; if chromaticNum == 2 and nodes > 2 then { not complete };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","circumference","edgeChromatic","edgeInd","girth","maxDeg","nodeCliqueCover","nodeCover","nodeInd","complete","nodes"]
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
			maxDeg = ingrid_obj.get('maxDeg', ind='Max')
			if maxDeg != 'undt':
				try:
					ingrid_obj.set('edgeChromatic', maxDeg, ind='Max')
				except:
					pass
			maxDeg = ingrid_obj.get('maxDeg', ind='Min')
			try:
				ingrid_obj.set('edgeChromatic', maxDeg, ind='Min')
			except:
				pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
			if edgeChromatic != 'undt':
				try:
					ingrid_obj.set('maxDeg', edgeChromatic, ind='Max')
				except:
					pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
			try:
				ingrid_obj.set('maxDeg', edgeChromatic, ind='Min')
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

class Theorem21(Theorem):
	def __init__(self):
		super(Theorem21, self).__init__(21, "genus <= ((nodes-3)*(nodes-4)+11)/12;", "")
	def involves(self, str_invar):
		return str_invar in ["genus","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('genus', 8.33333333333333e-2*nodes**2.0+-(0.583333333333333*nodes)+1.91666666666667, ind='Max')
			except:
				pass
		genus = ingrid_obj.get('genus', ind='Min')
		if genus != 'undt':
			try:
				ingrid_obj.set('nodes', 0.5*(48.0*genus+-(43.0))**(1/2)+3.5, ind='Min')
			except:
				pass

class Theorem22(Theorem):
	def __init__(self):
		super(Theorem22, self).__init__(22, "if edges  > maxdeg*edgeInd then { edgeChromatic == maxdeg + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edgeInd","edges","maxdeg"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (edgeInd_Max != 'undt' and maxdeg_Max != 'undt' and (edges_Min>maxdeg_Max*edgeInd_Max)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('edgeChromatic', maxdeg+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('edgeChromatic', maxdeg+1.0, ind='Min')
			except:
				pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
			if edgeChromatic != 'undt':
				try:
					ingrid_obj.set('maxdeg', edgeChromatic+-(1.0), ind='Max')
				except:
					pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
			try:
				ingrid_obj.set('maxdeg', edgeChromatic+-(1.0), ind='Min')
			except:
				pass

class Theorem23(Theorem):
	def __init__(self):
		super(Theorem23, self).__init__(23, "edgeCliqueCover <= edgeCover * edgeInd;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","edgeCover","edgeInd"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeCover != 'undt' and edgeInd != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', edgeCover*edgeInd, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edgeInd = ingrid_obj.get('edgeInd', ind='Max')
		if edgeInd != 'undt':
			try:
				ingrid_obj.set('edgeCover', edgeCliqueCover/edgeInd, ind='Min')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('edgeInd', edgeCliqueCover/edgeCover, ind='Min')
			except:
				pass

class Theorem24(Theorem):
	def __init__(self):
		super(Theorem24, self).__init__(24, "if mindeg >= 3 and odd girth then { nodes >= (mindeg*(mindeg - 1)**((girth - 1)/2) - 2)/(mindeg - 2) } else { nodes >= (2*(mindeg - 1)**(girth/3) - 2)/(mindeg - 2) } ;", "")
	def involves(self, str_invar):
		return str_invar in ["girth","mindeg","nodes"]
	def run(self, ingrid_obj):
                return
		# mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		# girth_Min = ingrid_obj.get('girth', ind='Min')
		# girth_Max = ingrid_obj.get('girth', ind='Max')
		
		# if (mindeg_Min>=3.0) and (odd(girth_Min)):
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', (mindeg*(mindeg+-(1.0))**(girth/2.0)+-(2.0*(mindeg+-(1.0))**(1/2)))/((mindeg+-(2.0))*(mindeg+-(1.0))**(1/2)), ind='Min')
		# 	except:
		# 		pass
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', (-((2.0))+mindeg*(-((1.0))+mindeg)**((-((1.0))+girth)/2.0))/(-((2.0))+mindeg), ind='Min')
		# 	except:
		# 		pass
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', (-((2.0))+mindeg*(-((1.0))+mindeg)**((-((1.0))+girth)/2.0))/(-((2.0))+mindeg), ind='Min')
		# 	except:
		# 		pass
		# elif (True):
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', 2.0*((mindeg+-(1.0))**(girth/3.0)+-(1.0))/(mindeg+-(2.0)), ind='Min')
		# 	except:
		# 		pass
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', (-((2.0))+2.0*(-((1.0))+mindeg)**(girth/3.0))/(-((2.0))+mindeg), ind='Min')
		# 	except:
		# 		pass
		# 	girth = ingrid_obj.get('girth', ind='Min')
		# 	mindeg = ingrid_obj.get('mindeg', ind='Min')
		# 	try:
		# 		ingrid_obj.set('nodes', (-((2.0))+2.0*(-((1.0))+mindeg)**(girth/3.0))/(-((2.0))+mindeg), ind='Min')
		# 	except:
		# 		pass

class Theorem25(Theorem):
	def __init__(self):
		super(Theorem25, self).__init__(25, "edgeCover >= (1/2)*nodes;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('edgeCover', 0.5*nodes, ind='Min')
		except:
			pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*edgeCover, ind='Max')
			except:
				pass

class Theorem26(Theorem):
	def __init__(self):
		super(Theorem26, self).__init__(26, "edges <= (1/2)*(nodes - 1)*(nodes-2)+nodes/domination - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edges","nodes"]
	def run(self, ingrid_obj):
		domination = ingrid_obj.get('domination', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if domination != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*nodes*(domination*nodes+-(3.0*domination)+2.0)/domination, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('domination', 2.0*nodes/(2.0*edges+-(nodes**2.0)+3.0*nodes), ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('nodes', 0.5*(3.0*domination+-(2.0))/domination+0.5*(8.0*edges*domination**2.0+9.0*domination**2.0+-(12.0*domination)+4.0)**(1/2)/domination, ind='Min')
		except:
			pass

class Theorem27(Theorem):
	def __init__(self):
		super(Theorem27, self).__init__(27, "edgeCover <= nodes*maxdeg/(1 + maxdeg);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edgeCover', maxdeg*nodes/(maxdeg+1.0), ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(edgeCover/(edgeCover+-(nodes))), ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', edgeCover+edgeCover/maxdeg, ind='Min')
			except:
				pass

class Theorem28(Theorem):
	def __init__(self):
		super(Theorem28, self).__init__(28, "if diameter <= 3 then { maxdeg <= nodes - diamaeter + 1 } else { maxdeg <= nodes - nodeConnec*(diameter - 4)-3 };", "")
	def involves(self, str_invar):
		return str_invar in ["diamaeter","diameter","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		
		if (diameter_Max != 'undt' and (diameter_Max<=3.0)):
			diamaeter = ingrid_obj.get('diamaeter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(diamaeter)+nodes+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diamaeter', -(maxdeg)+nodes+1.0, ind='Max')
				except:
					pass
			diamaeter = ingrid_obj.get('diamaeter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', maxdeg+diamaeter+-(1.0), ind='Min')
			except:
				pass
		elif (True):
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(diameter*nodeConnec)+4.0*nodeConnec+nodes+-(3.0), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', (-(maxdeg)+4.0*nodeConnec+nodes+-(3.0))/nodeConnec, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodeConnec', (-(maxdeg)+nodes+-(3.0))/(diameter+-(4.0)), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', maxdeg+diameter*nodeConnec+-(4.0*nodeConnec)+3.0, ind='Min')
			except:
				pass

class Theorem29(Theorem):
	def __init__(self):
		super(Theorem29, self).__init__(29, "edgeCliqueCover <= edges - (1/2)*maxClique(maxClique - 1)+1;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","edges","maxClique"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		if edges != 'undt' and maxClique != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', -(0.5*maxClique(maxClique+-(1.0)))+edges+1.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('edges', edgeCliqueCover+0.5*maxClique(maxClique+-(1.0))+-(1.0), ind='Min')
		except:
			pass

class Theorem30(Theorem):
	def __init__(self):
		super(Theorem30, self).__init__(30, "if connected and radius <= min(2,nodes/2) then { edges <= (1/2)*nodes*(nodes-radius) } else if connected and radius >= 3 and radius <= nodes/2 then { edges <= (1/2)*(nodes**2+4*radius*nodes+5*nodes+4*radius**2-6*radius) };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edges","nodes","radius"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		radius_Min = ingrid_obj.get('radius', ind='Min')
		if (connected == True) and (radius_Max != 'undt' and (radius_Max<=min(2.0, nodes_Min/2.0))):
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*nodes*(nodes+-(radius)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.5*radius+0.5*(8.0*edges+radius**2.0)**(1/2), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('radius', -(2.0*edges/nodes)+nodes, ind='Max')
				except:
					pass
		elif (connected == True) and (radius_Min>=3.0) and (radius_Max != 'undt' and (radius_Max<=nodes_Min/2.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if nodes != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*nodes**2.0+2.0*nodes*radius+2.5*nodes+2.0*radius**2.0+-(3.0*radius), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('nodes', -(2.0*radius)+0.5*(8.0*edges+64.0*radius+25.0)**(1/2)+-(2.5), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('radius', -(0.5*nodes)+0.25*(8.0*edges+-(32.0*nodes)+9.0)**(1/2)+0.75, ind='Max')
				except:
					pass

class Theorem31(Theorem):
	def __init__(self):
		super(Theorem31, self).__init__(31, "chromaticNum <= (nodes + 1 )**2/(4*nodeCliqueCover);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 0.25*(nodes**2.0+2.0*nodes+1.0)/nodeCliqueCover, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', 0.25*(nodes**2.0+2.0*nodes+1.0)/chromaticNum, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*(chromaticNum*nodeCliqueCover)**(1/2)+-(1.0), ind='Min')
		except:
			pass

class Theorem32(Theorem):
	def __init__(self):
		super(Theorem32, self).__init__(32, "chromaticNum >= 2*nodes**(1/2)-nodeCliqueCover;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('chromaticNum', -(nodeCliqueCover)+2.0*(nodes)**(1/2), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', -(chromaticNum)+2.0*(nodes)**(1/2), ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if chromaticNum != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', 0.25*(chromaticNum+nodeCliqueCover)**2.0, ind='Max')
			except:
				pass

class Theorem33(Theorem):
	def __init__(self):
		super(Theorem33, self).__init__(33, "domination <= nodes + 1 - (1+2*edges)**(1/2);", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edges","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edges != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('domination', nodes+-((2.0*edges+1.0)**(1/2))+1.0, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*(-(domination)+nodes+1.0)**2.0+-(0.5), ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('nodes', domination+(2.0*edges+1.0)**(1/2)+-(1.0), ind='Min')
		except:
			pass

class Theorem34(Theorem):
	def __init__(self):
		super(Theorem34, self).__init__(34, "if nodeConnec > 0 and not tree then { girth <= 2*diameter+1 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","girth","nodeConnec","tree"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		tree = ingrid_obj.get('tree')
		if (nodeConnec_Min>0.0) and (tree == False):
			diameter = ingrid_obj.get('diameter', ind='Max')
			if diameter != 'undt':
				try:
					ingrid_obj.set('girth', 2.0*diameter+1.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('diameter', 0.5*girth+-(0.5), ind='Min')
			except:
				pass

class Theorem35(Theorem):
	def __init__(self):
		super(Theorem35, self).__init__(35, "if planar and maxClique < 3 then { nodeInd >= (1/3)*(nodes+1), nodeCover <= (2*nodes-1)/3 } else if planar then { maxClique >= 3 }; ", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","nodeCover","nodeInd","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (planar == True) and (maxClique_Max != 'undt' and (maxClique_Max<3.0)):
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.333333333333333*nodes+0.333333333333333, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 3.0*nodeInd+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.666666666666667*nodes+-(0.333333333333333), ind='Max')
				except:
					pass
			nodeCover = ingrid_obj.get('nodeCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.5*nodeCover+0.5, ind='Min')
			except:
				pass
		elif (planar == True):
			try:
				ingrid_obj.set('maxClique', 3.0, ind='Min')
			except:
				pass

class Theorem36(Theorem):
	def __init__(self):
		super(Theorem36, self).__init__(36, "if not planar then { maxdeg >= 3, nodes >= 5, edges >= 9, edgeInd >= 2, nodeCover >= 3, edgeCover >= 3, bandwidth >= 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","edgeCover","edgeInd","edges","maxdeg","nodeCover","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		if (planar == False):
			try:
				ingrid_obj.set('maxdeg', 3.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodes', 5.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edges', 9.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeInd', 2.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCover', 3.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCover', 3.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('bandwidth', 4.0, ind='Min')
			except:
				pass

class Theorem37(Theorem):
	def __init__(self):
		super(Theorem37, self).__init__(37, "edges <= numOfComponents - 1 + (1/2)*(nodes+2-2*numOfComponents)*(nodes+1-2*numOfComponents);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if nodes != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*nodes**2.0+-(2.0*nodes*numOfComponents)+1.5*nodes+2.0*numOfComponents**2.0+-(2.0*numOfComponents), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*numOfComponents+0.5*(8.0*edges+-(8.0*numOfComponents)+9.0)**(1/2)+-(1.5), ind='Min')
		except:
			pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		try:
			ingrid_obj.set('numOfComponents', 0.5*nodes+0.5*(2.0*edges+-(nodes)+1.0)**(1/2)+0.5, ind='Max')
		except:
			pass

class Theorem38(Theorem):
	def __init__(self):
		super(Theorem38, self).__init__(38, "domination >= nodes / (maxdeg + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["domination","maxdeg","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('domination', nodes/(maxdeg+1.0), ind='Min')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if domination != 'undt':
			try:
				ingrid_obj.set('maxdeg', (-(domination)+nodes)/domination, ind='Min')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if domination != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', domination*(maxdeg+1.0), ind='Max')
			except:
				pass

class Theorem39(Theorem):
	def __init__(self):
		super(Theorem39, self).__init__(39, "if girth >= 4 then { maxClique <= 2 }; if maxClique <= 2 then { girth >= 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxClique"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=4.0):
			try:
				ingrid_obj.set('maxClique', 2.0, ind='Max')
			except:
				pass
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
			try:
				ingrid_obj.set('girth', 4.0, ind='Min')
			except:
				pass

class Theorem40(Theorem):
	def __init__(self):
		super(Theorem40, self).__init__(40, "if complete then { mindeg == nodes - 1, nodeInd == 1, nodeCliqueCover == 1, edgeCliqueCover == 1, diameter == 1}; if mindeg == nodes - 1 then { complete, nodeInd == 1, nodeCliqueCover == 1, edgeCliqueCover == 1, diameter == 1}; if nodeInd == 1 then { complete, mindeg == nodes - 1, nodeCliqueCover == 1, edgeCliqueCover == 1, diameter == 1}; if nodeCliqueCover == 1 then { complete, mindeg == nodes - 1, nodeInd == 1, edgeCliqueCover == 1, diameter == 1 }; if edgeCliqueCover == 1 then { complete, mindeg == nodes - 1, nodeInd == 1, nodeCliqueCover == 1, diameter == 1 }; if diameter == 1 then { complete, mindeg == nodes - 1, nodeInd == 1, nodeCliqueCover == 1, edgeCliqueCover == 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["complete","diameter","edgeCliqueCover","mindeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		complete = ingrid_obj.get('complete')
		if (complete == True):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodes+-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Min')
			except:
				pass
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (mindeg_Max != 'undt' and (mindeg_Max<=nodes_Min+-(1.0))) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max+-(1.0))):
			ingrid_obj.set('complete', True)
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Min')
			except:
				pass
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==1.0)):
			ingrid_obj.set('complete', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodes+-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Min')
			except:
				pass
		nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if (nodeCliqueCover_Max==nodeCliqueCover_Min and (nodeCliqueCover_Min==1.0)):
			ingrid_obj.set('complete', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodes+-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Min')
			except:
				pass
		edgeCliqueCover_Min = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edgeCliqueCover_Max = ingrid_obj.get('edgeCliqueCover', ind='Max')
		if (edgeCliqueCover_Max==edgeCliqueCover_Min and (edgeCliqueCover_Min==1.0)):
			ingrid_obj.set('complete', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodes+-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('diameter', 1.0, ind='Min')
			except:
				pass
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==1.0)):
			ingrid_obj.set('complete', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', nodes+-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', mindeg+1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeInd', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeCliqueCover', 1.0, ind='Min')
			except:
				pass

class Theorem41(Theorem):
	def __init__(self):
		super(Theorem41, self).__init__(41, "if chromaticNum <= 2 then { bipartite }; if bipartite then { chromaticNum <= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","chromaticNum"]
	def run(self, ingrid_obj):
		chromaticNum_Max = ingrid_obj.get('chromaticNum', ind='Max')
		if (chromaticNum_Max != 'undt' and (chromaticNum_Max<=2.0)):
			ingrid_obj.set('bipartite', True)
		bipartite = ingrid_obj.get('bipartite')
		if (bipartite == True):
			try:
				ingrid_obj.set('chromaticNum', 2.0, ind='Max')
			except:
				pass

class Theorem42(Theorem):
	def __init__(self):
		super(Theorem42, self).__init__(42, "if radius == 1 then { maxdeg == nodes - 1 }; if maxdeg == nodes - 1 then { radius == 1};", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodes","radius"]
	def run(self, ingrid_obj):
		radius_Min = ingrid_obj.get('radius', ind='Min')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		if (radius_Max==radius_Min and (radius_Min==1.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', nodes+-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', nodes+-(1.0), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', maxdeg+1.0, ind='Min')
			except:
				pass
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (maxdeg_Max != 'undt' and (maxdeg_Max<=nodes_Min+-(1.0))) and (nodes_Max != 'undt' and (maxdeg_Min>=nodes_Max+-(1.0))):
			try:
				ingrid_obj.set('radius', 1.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('radius', 1.0, ind='Min')
			except:
				pass

class Theorem43(Theorem):
	def __init__(self):
		super(Theorem43, self).__init__(43, "if forest and connected then { tree }; if tree then { forest and connected };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","forest","tree"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		connected = ingrid_obj.get('connected')
		if (forest == True) and (connected == True):
			ingrid_obj.set('tree', True)
		tree = ingrid_obj.get('tree')
		if (tree == True):
			ingrid_obj.set('forest', True)
			ingrid_obj.set('connected', True)

