TypeError('unorderable types: float() <= complex()',)
class Theorem341(Theorem):
	def __init__(self):
		super(Theorem341, self).__init__(341, "if mindeg >= 2 and girth >= 7 then {domination >= maxdeg + 1};", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","maxdeg","mindeg"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Min>=2.0) and (girth_Min>=7.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('domination', 1.0*maxdeg+1.0, ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Max')
			if domination != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*domination-(1.0), ind='Max')
				except:
					pass
		return

class Theorem342(Theorem):
	def __init__(self):
		super(Theorem342, self).__init__(342, "if girth >= 5 and girth <= nodes/2 then {edges <= (nodes**2 - nodes*girth + 2*girth)/girth};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (girth_Min>=5.0) and (girth_Max != 'undt' and (girth_Max<=nodes_Min/2.0)):
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', -(nodes)+2.0+nodes**2.0/girth, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', nodes**2.0/(edges+nodes-(2.0)), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', (2.0*girth-((nodes*girth))+nodes**2.0)/girth, ind='Max')
				except:
					pass
		return

class Theorem343(Theorem):
	def __init__(self):
		super(Theorem343, self).__init__(343, "if girth >= 5 then {edges <= nodes*sqrt(nodes - 1)/2};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","girth","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (girth_Min>=5.0):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 0.5*nodes*(nodes-(1.0))**0.5, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', nodes*(nodes-((1.0)))**(1.0/2.0)/2.0, ind='Max')
				except:
					pass
		return

class Theorem344(Theorem):
	def __init__(self):
		super(Theorem344, self).__init__(344, "if not forest and nodes >= floor((3*girth-3)/2) then { edges <= nodes*(nodes-1)/((3*girth-5)/2) - numOfComponents + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","forest","girth","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (forest == False) and (girth_Max != 'undt' and (nodes_Min>=floor((3.0*girth_Max-(3.0))/2.0))):
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if girth != 'undt' and nodes != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('edges', (-(1.5*girth*numOfComponents)+1.5*girth+1.0*nodes**2.0-(1.0*nodes)+2.5*numOfComponents-(2.5))/(1.5*girth-(2.5)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('girth', (1.66666666666667*edges+0.666666666666667*nodes**2.0-(0.666666666666667*nodes)+1.66666666666667*numOfComponents-(1.66666666666667))/(edges+numOfComponents-(1.0)), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edges != 'undt' and girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', (-(1.5*edges*girth)+2.5*edges+1.5*girth+1.0*nodes**2.0-(1.0*nodes)-(2.5))/(1.5*girth-(2.5)), ind='Max')
				except:
					pass
		return

class Theorem345(Theorem):
	def __init__(self):
		super(Theorem345, self).__init__(345, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem346(Theorem):
	def __init__(self):
		super(Theorem346, self).__init__(346, "if not forest and (nodeConnec > 0 or mindeg > 1) then { genus >= (edges*(1-2/girth-2/mindeg)+2*numOfComponents)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","forest","genus","girth","mindeg","nodeConnec","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (forest == False) and (nodeConnec_Min>0.0) or (mindeg_Min>1.0):
			edges = ingrid_obj.get('edges', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('genus', 0.5*edges-(1.0*edges/mindeg)-(1.0*edges/girth)+1.0*numOfComponents, ind='Min')
			except:
				pass
			genus = ingrid_obj.get('genus', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt':
				try:
					ingrid_obj.set('edges', 1.0*girth*mindeg*(-(genus)+numOfComponents)/(-(0.5*girth*mindeg)+1.0*girth+1.0*mindeg), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			genus = ingrid_obj.get('genus', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('girth', -(1.0*edges*mindeg/(1.0*genus*mindeg-(0.5*edges*mindeg)+1.0*edges-(1.0*mindeg*numOfComponents))), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			genus = ingrid_obj.get('genus', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if numOfComponents != 'undt':
				try:
					ingrid_obj.set('mindeg', -(1.0*edges*girth/(1.0*genus*girth-(0.5*edges*girth)+1.0*edges-(1.0*girth*numOfComponents))), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			genus = ingrid_obj.get('genus', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			if edges != 'undt' and genus != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*genus-(0.5*edges)+1.0*edges/mindeg+1.0*edges/girth, ind='Max')
				except:
					pass
		return

class Theorem347(Theorem):
	def __init__(self):
		super(Theorem347, self).__init__(347, "if diameter == 2 then { nodes <= nodeConnec*maxdeg + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if maxdeg != 'undt' and nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*maxdeg*nodeConnec+1.0, ind='Max')
				except:
					pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*(nodes-(1.0))/nodeConnec, ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodeConnec', 1.0*(nodes-(1.0))/maxdeg, ind='Min')
				except:
					pass
		return

class Theorem348(Theorem):
	def __init__(self):
		super(Theorem348, self).__init__(348, "if not forest and edges >= nodes + 1 - numOfComponents then { nodes >= 3*girth/2 + 2*numOfComponents - 3 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","forest","girth","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
		if (forest == False) and (nodes_Max != 'undt' and numOfComponents_Max != 'undt' and (edges_Min>=nodes_Max+1.0-(numOfComponents_Max))):
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.5*girth+2.0*numOfComponents-(3.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.666666666666667*nodes-(1.33333333333333*numOfComponents)+2.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 0.5*nodes-(0.75*girth)+1.5, ind='Max')
				except:
					pass
		return

class Theorem349(Theorem):
	def __init__(self):
		super(Theorem349, self).__init__(349, "if not forest and edges >= nodes + 3 then { nodes >= 2*girth + 2*numOfComponents - 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","forest","girth","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (forest == False) and (nodes_Max != 'undt' and (edges_Min>=nodes_Max+3.0)):
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*girth+2.0*numOfComponents-(4.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.5*nodes-(1.0*numOfComponents)+2.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 0.5*nodes-(1.0*girth)+2.0, ind='Max')
				except:
					pass
		return

class Theorem350(Theorem):
	def __init__(self):
		super(Theorem350, self).__init__(350, "if not forest and edges >= nodes + 4 - numOfComponents then { nodes >= 9*girth/4 + 2*numOfComponents - 5 };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","forest","girth","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		numOfComponents_Max = ingrid_obj.get('numOfComponents', ind='Max')
		if (forest == False) and (nodes_Max != 'undt' and numOfComponents_Max != 'undt' and (edges_Min>=nodes_Max+4.0-(numOfComponents_Max))):
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.25*girth+2.0*numOfComponents-(5.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.444444444444444*nodes-(0.888888888888889*numOfComponents)+2.22222222222222, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 0.5*nodes-(1.125*girth)+2.5, ind='Max')
				except:
					pass
		return

class Theorem351(Theorem):
	def __init__(self):
		super(Theorem351, self).__init__(351, "if girth >= max((nodes+1)/2, 5) and edges >= nodes + 3 then { if girth <= 7 then { girth <= 6 } else { girth <= 8 }, nodes == 2*girth - 1, nodeConnec == 2, edgeConnec == 2, mindeg == 2, edges == nodes + 3, nonplanar };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","edges","girth","mindeg","nodeConnec","nodes","nonplanar"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		if (nodes_Max != 'undt' and (girth_Min>=max((nodes_Max+1.0)/2.0, 5.0))) and (nodes_Max != 'undt' and (edges_Min>=nodes_Max+3.0)):
			girth_Max = ingrid_obj.get('girth', ind='Max')
			
			if (girth_Max != 'undt' and (girth_Max<=7.0)):
				try:
					ingrid_obj.set('girth', 6.0, ind='Max')
				except:
					pass
			elif (True):
				try:
					ingrid_obj.set('girth', 8.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Max')
			if girth != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*girth-(1.0), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*girth-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', 0.5*nodes+0.5, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('girth', 0.5*nodes+0.5, ind='Min')
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
			try:
				ingrid_obj.set('edgeConnec', 2.0, ind='Max')
			except:
				pass
			try:
				ingrid_obj.set('edgeConnec', 2.0, ind='Min')
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
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edges', 1.0*nodes+3.0, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*nodes+3.0, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edges-(3.0), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*edges-(3.0), ind='Min')
			except:
				pass
			ingrid_obj.set('nonplanar', True)
		return

class Theorem352(Theorem):
	def __init__(self):
		super(Theorem352, self).__init__(352, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem353(Theorem):
	def __init__(self):
		super(Theorem353, self).__init__(353, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem354(Theorem):
	def __init__(self):
		super(Theorem354, self).__init__(354, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem355(Theorem):
	def __init__(self):
		super(Theorem355, self).__init__(355, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem356(Theorem):
	def __init__(self):
		super(Theorem356, self).__init__(356, "if regular and edgeInd < nodes/2 then { edgeChromatic == maxdeg + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeChromatic","edgeInd","maxdeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (regular == True) and (edgeInd_Max != 'undt' and (edgeInd_Max<nodes_Min/2.0)):
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

class Theorem357(Theorem):
	def __init__(self):
		super(Theorem357, self).__init__(357, "if regular then { edgeInd >= nodes*maxdeg/(2*(maxdeg + 1)) };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","maxdeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		if (regular == True):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*maxdeg*nodes/(maxdeg+1.0), ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', -(2.0*edgeInd/(2.0*edgeInd-(1.0*nodes))), ind='Min')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if edgeInd != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*edgeInd*(maxdeg+1.0)/maxdeg, ind='Max')
				except:
					pass
		return

class Theorem358(Theorem):
	def __init__(self):
		super(Theorem358, self).__init__(358, "if nodeConnec >= 2 and mindeg >= (nodes + nodeConnec)/3 then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeConnec_Min>=2.0) and (nodeConnec_Max != 'undt' and nodes_Max != 'undt' and (mindeg_Min>=(nodes_Max+nodeConnec_Max)/3.0)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem359(Theorem):
	def __init__(self):
		super(Theorem359, self).__init__(359, "if nodeConnec >= 3 then { circumference >= min(nodes, 3*mindeg - nodeConnec) };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (nodeConnec_Min>=3.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(nodes, 3.0*mindeg-(nodeConnec)), ind='Min')
			except:
				pass
		return

class Theorem360(Theorem):
	def __init__(self):
		super(Theorem360, self).__init__(360, "if regular and nodes == 2*maxdeg +  1 then { nodeConnec >= nodeInd };", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodeConnec","nodeInd","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		if (regular == True) and (nodes_Max != 'undt' and (nodes_Max<=2.0*maxdeg_Min+1.0)) and (maxdeg_Max != 'undt' and (nodes_Min>=2.0*maxdeg_Max+1.0)):
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', nodeInd, ind='Min')
			except:
				pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodeInd', nodeConnec, ind='Max')
				except:
					pass
		return

