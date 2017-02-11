class Theorem21(Theorem):
	def __init__(self):
		super(Theorem21, self).__init__(21, "genus <= ((nodes-3)*(nodes-4)+11)/12;", "")
	def involves(self, str_invar):
		return str_invar in ["genus","nodes"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('genus', 8.33333333333333e-2*nodes**2.0-(0.583333333333333*nodes)+1.91666666666667, ind='Max')
			except:
				pass
		genus = ingrid_obj.get('genus', ind='Min')
		try:
			ingrid_obj.set('nodes', 0.5*(48.0*genus-(43.0))**(1/2)+3.5, ind='Min')
		except:
			pass
		return

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
		return

class Theorem24(Theorem):
	def __init__(self):
		super(Theorem24, self).__init__(24, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

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
		return

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
				ingrid_obj.set('edges', nodes*(0.5*domination*nodes-(1.5*domination)+1.0)/domination, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('domination', 1.0*nodes/(1.0*edges-(0.5*nodes**2.0)+1.5*nodes), ind='Min')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*(1.5*domination-(1.0))/domination+1.0*(2.0*edges*domination**2.0+2.25*domination**2.0-(3.0*domination)+1.0)**(1/2)/domination, ind='Min')
		except:
			pass
		return

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
				ingrid_obj.set('edgeCover', 1.0*maxdeg*nodes/(maxdeg+1.0), ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0*edgeCover/(edgeCover-(nodes))), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*edgeCover*(maxdeg+1.0)/maxdeg, ind='Min')
		except:
			pass
		return

class Theorem28(Theorem):
	def __init__(self):
		super(Theorem28, self).__init__(28, "if diameter <= 3 then { maxdeg <= nodes - diameter + 1 } else { maxdeg <= nodes - nodeConnec*(diameter - 4)-3 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		
		if (diameter_Max != 'undt' and (diameter_Max<=3.0)):
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(1.0*diameter)+1.0*nodes+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('diameter', -(1.0*maxdeg)+1.0*nodes+1.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg+1.0*diameter-(1.0), ind='Min')
			except:
				pass
		elif (True):
			diameter = ingrid_obj.get('diameter', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(1.0*diameter*nodeConnec)+4.0*nodeConnec+1.0*nodes-(3.0), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('diameter', (-(1.0*maxdeg)+4.0*nodeConnec+1.0*nodes-(3.0))/nodeConnec, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeConnec', (-(1.0*maxdeg)+1.0*nodes-(3.0))/(1.0*diameter-(4.0)), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg+1.0*diameter*nodeConnec-(4.0*nodeConnec)+3.0, ind='Min')
			except:
				pass
		return

class Theorem29(Theorem):
	def __init__(self):
		super(Theorem29, self).__init__(29, "edgeCliqueCover <= edges - (1/2)*maxClique(maxClique - 1)+1;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","edges","maxClique"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Max')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', -(0.5*maxClique(maxClique-(1.0)))+1.0*edges+1.0, ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		try:
			ingrid_obj.set('edges', 1.0*edgeCliqueCover+0.5*maxClique(maxClique-(1.0))-(1.0), ind='Min')
		except:
			pass
		return

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
					ingrid_obj.set('edges', 0.5*nodes*(nodes-(radius)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.5*radius+0.5*(8.0*edges+1.0*radius**2.0)**(1/2), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('radius', -(2.0*edges/nodes)+1.0*nodes, ind='Max')
				except:
					pass
		elif (connected == True) and (radius_Min>=3.0) and (radius_Max != 'undt' and (radius_Max<=nodes_Min/2.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if nodes != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('edges', 2.0*nodes*radius+2.5*nodes+0.5*nodes**2.0-(3.0*radius)+2.0*radius**2.0, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if nodes != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('edges', (1.0/2.0)*(-((6.0*radius))+4.0*radius**2.0+5.0*nodes+4.0*radius*nodes+nodes**2.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if nodes != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('edges', (1.0/2.0)*(-((6.0*radius))+4.0*radius**2.0+5.0*nodes+4.0*radius*nodes+nodes**2.0), ind='Max')
				except:
					pass
		return

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
				ingrid_obj.set('chromaticNum', 0.25*(nodes+1.0)**2.0/nodeCliqueCover, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', 0.25*(nodes+1.0)**2.0/chromaticNum, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 2.0*(chromaticNum*nodeCliqueCover)**0.5-(1.0), ind='Min')
		except:
			pass
		return

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
				ingrid_obj.set('chromaticNum', -(1.0*nodeCliqueCover)+2.0*nodes**0.5, ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', -(1.0*chromaticNum)+2.0*nodes**0.5, ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if chromaticNum != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', 0.25*(chromaticNum+nodeCliqueCover)**2.0, ind='Max')
			except:
				pass
		return

class Theorem33(Theorem):
	def __init__(self):
		super(Theorem33, self).__init__(33, "domination <= nodes + 1 - (1+2*edges)**(1/2);", "")
	def involves(self, str_invar):
		return str_invar in ["domination","edges","nodes"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('domination', 1.0*nodes-(1.0*(2.0*edges+1.0)**0.5)+1.0, ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*(-(domination)+nodes+1.0)**2.0-(0.5), ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		edges = ingrid_obj.get('edges', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*domination+1.0*(2.0*edges+1.0)**0.5-(1.0), ind='Min')
		except:
			pass
		return

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
				ingrid_obj.set('diameter', 0.5*girth-(0.5), ind='Min')
			except:
				pass
		return

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
					ingrid_obj.set('nodes', 3.0*nodeInd-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCover', 0.666666666666667*nodes-(0.333333333333333), ind='Max')
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
		return

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
		return

class Theorem37(Theorem):
	def __init__(self):
		super(Theorem37, self).__init__(37, "edges <= numOfComponents - 1 + (nodes+2-2*numOfComponents)*(nodes+1-2*numOfComponents)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if nodes != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*nodes**2.0-(2.0*nodes*numOfComponents)+1.5*nodes+2.0*numOfComponents**2.0-(2.0*numOfComponents), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if edges != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*numOfComponents+0.5*(8.0*edges-(8.0*numOfComponents)+9.0)**(1/2)-(1.5), ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('numOfComponents', 0.5*(nodes+1.0)+0.5*(2.0*edges-(1.0*nodes)+1.0)**(1/2), ind='Min')
		except:
			pass
		return

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
				ingrid_obj.set('domination', 1.0*nodes/(maxdeg+1.0), ind='Min')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if domination != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0)+1.0*nodes/domination, ind='Min')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if domination != 'undt' and maxdeg != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*domination*(maxdeg+1.0), ind='Max')
			except:
				pass
		return

class Theorem39(Theorem):
	def __init__(self):
		super(Theorem39, self).__init__(39, "if girth >= 4 or maxClique <= 2 then { maxClique <= 2, girth >= 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxClique"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (girth_Min>=4.0) or (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
			try:
				ingrid_obj.set('maxClique', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('girth', 4.0, ind='Min')
			except:
				pass
		return

class Theorem40(Theorem):
	def __init__(self):
		super(Theorem40, self).__init__(40, "if complete or mindeg == nodes - 1 or nodeInd == 1 or nodeCliqueCover == 1 or edgeCliqueCover == 1 or diameter == 1 then { complete, mindeg == nodes - 1, nodeInd == 1, nodeCliqueCover == 1, edgeCliqueCover == 1, diameter == 1};", "")
	def involves(self, str_invar):
		return str_invar in ["complete","diameter","edgeCliqueCover","mindeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		complete = ingrid_obj.get('complete')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		nodeCliqueCover_Min = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodeCliqueCover_Max = ingrid_obj.get('nodeCliqueCover', ind='Max')
		edgeCliqueCover_Min = ingrid_obj.get('edgeCliqueCover', ind='Min')
		edgeCliqueCover_Max = ingrid_obj.get('edgeCliqueCover', ind='Max')
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (complete == True) or (mindeg_Max != 'undt' and (mindeg_Max<=nodes_Min-(1.0))) and (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max-(1.0))) or (nodeInd_Max==nodeInd_Min and (nodeInd_Min==1.0)) or (nodeCliqueCover_Max==nodeCliqueCover_Min and (nodeCliqueCover_Min==1.0)) or (edgeCliqueCover_Max==edgeCliqueCover_Min and (edgeCliqueCover_Min==1.0)) or (diameter_Max==diameter_Min and (diameter_Min==1.0)):
			ingrid_obj.set('complete', True)
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*nodes-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 1.0*nodes-(1.0), ind='Min')
			except:
				pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*mindeg+1.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*mindeg+1.0, ind='Min')
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
		return

