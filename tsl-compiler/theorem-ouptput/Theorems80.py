class Theorem61(Theorem):
	def __init__(self):
		super(Theorem61, self).__init__(61, "if genus <= 1 then { edgeCliqueCover <= nodeCover*nodeInd };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","genus","nodeCover","nodeInd"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		if (genus_Max != 'undt' and (genus_Max<=1.0)):
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeCover != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('edgeCliqueCover', nodeCover*nodeInd, ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('nodeCover', edgeCliqueCover/nodeInd, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodeCover = ingrid_obj.get('nodeCover', ind='Max')
			if nodeCover != 'undt':
				try:
					ingrid_obj.set('nodeInd', edgeCliqueCover/nodeCover, ind='Min')
				except:
					pass
		return

class Theorem62(Theorem):
	def __init__(self):
		super(Theorem62, self).__init__(62, "if mindeg >= nodes/2 then { nodeConnec >= nodeInd };", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeConnec","nodeInd","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max/2.0)):
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

class Theorem63(Theorem):
	def __init__(self):
		super(Theorem63, self).__init__(63, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem64(Theorem):
	def __init__(self):
		super(Theorem64, self).__init__(64, "if nodes >= 3 and nodeConnec >= nodeInd then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","nodeConnec","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodes_Min>=3.0) and (nodeInd_Max != 'undt' and (nodeConnec_Min>=nodeInd_Max)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem65(Theorem):
	def __init__(self):
		super(Theorem65, self).__init__(65, "if edges >= (nodes**2 - 3*nodes + 6) then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","hamiltonian","nodes"]
	def run(self, ingrid_obj):
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (edges_Min>=(nodes_Max**2.0-(3.0*nodes_Max)+6.0))):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem66(Theorem):
	def __init__(self):
		super(Theorem66, self).__init__(66, "if planar and nodeConnec >= 4 then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["hamiltonian","nodeConnec","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (planar == True) and (nodeConnec_Min>=4.0):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem67(Theorem):
	def __init__(self):
		super(Theorem67, self).__init__(67, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem68(Theorem):
	def __init__(self):
		super(Theorem68, self).__init__(68, "if complete then { regular }; if complete and even nodes then { edgeChromatic == nodes - 1 } else { edgeChromatic == nodes };", "")
	def involves(self, str_invar):
		return str_invar in ["complete","regular","edgeChromatic","nodes"]
	def run(self, ingrid_obj):
		complete = ingrid_obj.get('complete')
		if (complete == True):
			ingrid_obj.set('regular', True)
		complete = ingrid_obj.get('complete')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		
		if (complete == True) and (even(nodes_Min) and even(nodes_Max)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeChromatic', 1.0*nodes-(1.0), ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeChromatic', 1.0*nodes-(1.0), ind='Min')
			except:
				pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
			if edgeChromatic != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edgeChromatic+1.0, ind='Max')
				except:
					pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*edgeChromatic+1.0, ind='Min')
			except:
				pass
		elif (True):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('edgeChromatic', nodes, ind='Max')
				except:
					pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edgeChromatic', nodes, ind='Min')
			except:
				pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Max')
			if edgeChromatic != 'undt':
				try:
					ingrid_obj.set('nodes', edgeChromatic, ind='Max')
				except:
					pass
			edgeChromatic = ingrid_obj.get('edgeChromatic', ind='Min')
			try:
				ingrid_obj.set('nodes', edgeChromatic, ind='Min')
			except:
				pass
		return

class Theorem69(Theorem):
	def __init__(self):
		super(Theorem69, self).__init__(69, "chromaticNum >= 2*edges/(2*edges - spectralRadius**2);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","edges","spectralRadius"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('chromaticNum', 2.0*edges/(2.0*edges-(1.0*spectralRadius**2.0)), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		spectralRadius = ingrid_obj.get('spectralRadius', ind='Min')
		try:
			ingrid_obj.set('edges', 0.5*chromaticNum*spectralRadius**2.0/(chromaticNum-(1.0)), ind='Min')
		except:
			pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		edges = ingrid_obj.get('edges', ind='Max')
		if chromaticNum != 'undt' and edges != 'undt':
			try:
				ingrid_obj.set('spectralRadius', 1.4142135623731*(edges-(edges/chromaticNum))**0.5, ind='Max')
			except:
				pass
		return

class Theorem70(Theorem):
	def __init__(self):
		super(Theorem70, self).__init__(70, "if genus <= 1 and girth == 3 then { chromaticNum <= 7 } else if genus <= 1 and girth >= 4 then { chromaticNum <= 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus","girth"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
			try:
				ingrid_obj.set('chromaticNum', 7.0, ind='Max')
			except:
				pass
		elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Min>=4.0):
			try:
				ingrid_obj.set('chromaticNum', 4.0, ind='Max')
			except:
				pass
		return

class Theorem71(Theorem):
	def __init__(self):
		super(Theorem71, self).__init__(71, "if defined girth then { circumference <= nodes - (numOfComponents - 1)*(mindeg + 1), circumference <= edges - (numOfComponents - 1)*mindeg, maxdeg >= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edges","girth","maxdeg","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		if (girth_Max != 'undt'):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('circumference', -(1.0*mindeg*numOfComponents)+1.0*mindeg+1.0*nodes-(1.0*numOfComponents)+1.0, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*(-(circumference)+nodes-(numOfComponents)+1.0)/(numOfComponents-(1.0)), ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*circumference+1.0*mindeg*numOfComponents-(1.0*mindeg)+1.0*numOfComponents-(1.0), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*(-(circumference)+mindeg+nodes+1.0)/(mindeg+1.0), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if edges != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('circumference', 1.0*edges-(1.0*mindeg*numOfComponents)+1.0*mindeg, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*circumference+1.0*mindeg*numOfComponents-(1.0*mindeg), ind='Min')
			except:
				pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			edges = ingrid_obj.get('edges', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('mindeg', 1.0*(-(circumference)+edges)/(numOfComponents-(1.0)), ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			edges = ingrid_obj.get('edges', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if edges != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*(-(circumference)+edges+mindeg)/mindeg, ind='Max')
				except:
					pass
			try:
				ingrid_obj.set('maxdeg', 2.0, ind='Min')
			except:
				pass
		return

class Theorem72(Theorem):
	def __init__(self):
		super(Theorem72, self).__init__(72, "if hamiltonian or circumference == nodes then { hamiltonian, circumference == nodes };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","hamiltonian","nodes"]
	def run(self, ingrid_obj):
		hamiltonian = ingrid_obj.get('hamiltonian')
		circumference_Max = ingrid_obj.get('circumference', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		circumference_Min = ingrid_obj.get('circumference', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (hamiltonian == True) or (circumference_Max != 'undt' and (circumference_Max<=nodes_Min)) and (nodes_Max != 'undt' and (circumference_Min>=nodes_Max)):
			ingrid_obj.set('hamiltonian', True)
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
		return

class Theorem73(Theorem):
	def __init__(self):
		super(Theorem73, self).__init__(73, "if hamiltonian then { arboricity >= 2, nodeConnec >= 2, nodeInd <= nodes/2, edgeCover <= (nodes + 1)/2, nodeCliqueCover <= (nodes + 1)/2, nodeCover >= nodes/2, edgeInd >= (nodes - 1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","edgeCover","edgeInd","hamiltonian","nodeCliqueCover","nodeConnec","nodeCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		hamiltonian = ingrid_obj.get('hamiltonian')
		if (hamiltonian == True):
			try:
				ingrid_obj.set('arboricity', 2.0, ind='Min')
			except:
				pass
			try:
				ingrid_obj.set('nodeConnec', 2.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', 0.5*nodes, ind='Max')
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
					ingrid_obj.set('edgeCover', 0.5*nodes+0.5, ind='Max')
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
					ingrid_obj.set('nodeCliqueCover', 0.5*nodes+0.5, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*nodeCliqueCover-(1.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeCover', 0.5*nodes, ind='Min')
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
				ingrid_obj.set('edgeInd', 0.5*nodes-(0.5), ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*edgeInd+1.0, ind='Max')
				except:
					pass
		return

class Theorem74(Theorem):
	def __init__(self):
		super(Theorem74, self).__init__(74, "bandwidth <= nodes - nodeInd/2 - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('bandwidth', -(0.5*nodeInd)+1.0*nodes-(1.0), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', -(2.0*bandwidth)+2.0*nodes-(2.0), ind='Max')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*bandwidth+0.5*nodeInd+1.0, ind='Min')
		except:
			pass
		return

class Theorem75(Theorem):
	def __init__(self):
		super(Theorem75, self).__init__(75, "edges >= (nodes/nodeInd)*(nodes-nodeInd*(nodes/nodeInd+1)/2);", "")
	def involves(self, str_invar):
		return str_invar in ["edges","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('edges', 0.5*nodes*(-(nodeInd)+nodes)/nodeInd, ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodeInd', 0.5*nodes**2.0/(1.0*edges+0.5*nodes), ind='Min')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if edges != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 0.5*nodeInd+1.0*(nodeInd*(2.0*edges+0.25*nodeInd))**(1/2), ind='Max')
			except:
				pass
		return

class Theorem76(Theorem):
	def __init__(self):
		super(Theorem76, self).__init__(76, "edgeCliqueCover <= nodeCliqueCover + nodes*(nodeCliqueCover - 1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeCliqueCover != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edgeCliqueCover', 0.5*nodeCliqueCover*nodes+1.0*nodeCliqueCover-(0.5*nodes), ind='Max')
			except:
				pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('nodeCliqueCover', (1.0*edgeCliqueCover+0.5*nodes)/(0.5*nodes+1.0), ind='Min')
		except:
			pass
		edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*(edgeCliqueCover-(nodeCliqueCover))/(nodeCliqueCover-(1.0)), ind='Min')
			except:
				pass
		return

class Theorem77(Theorem):
	def __init__(self):
		super(Theorem77, self).__init__(77, "if nodes >= 6*mindeg and edges > (1/2)*(nodes-mindeg)*(nodes - mindeg - 1) + mindeg**2 then { hamiltonian };", "")
	def involves(self, str_invar):
		return str_invar in ["edges","hamiltonian","mindeg","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (mindeg_Max != 'undt' and (nodes_Min>=6.0*mindeg_Max)) and (mindeg_Max != 'undt' and nodes_Max != 'undt' and (edges_Min>(1.0/2.0)*(nodes_Max-(mindeg_Max))*(nodes_Max-(mindeg_Max)-(1.0))+mindeg_Max**2.0)):
			ingrid_obj.set('hamiltonian', True)
		return

class Theorem78(Theorem):
	def __init__(self):
		super(Theorem78, self).__init__(78, "if nodes >= 4 and edges >= 2*nodes - 3 then { girth <= (circumference + 2)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edges","girth","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Min>=4.0) and (nodes_Max != 'undt' and (edges_Min>=2.0*nodes_Max-(3.0))):
			circumference = ingrid_obj.get('circumference', ind='Max')
			if circumference != 'undt':
				try:
					ingrid_obj.set('girth', 0.5*circumference+1.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('circumference', 2.0*girth-(2.0), ind='Min')
			except:
				pass
		return

class Theorem79(Theorem):
	def __init__(self):
		super(Theorem79, self).__init__(79, "if not forest then { nodeInd >= girth/2, radius >= girth/2, edgeInd >= circumference/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edgeInd","forest","girth","nodeInd","radius"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('nodeInd', 0.5*girth, ind='Min')
			except:
				pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('girth', 2.0*nodeInd, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('radius', 0.5*girth, ind='Min')
			except:
				pass
			radius = ingrid_obj.get('radius', ind='Max')
			if radius != 'undt':
				try:
					ingrid_obj.set('girth', 2.0*radius, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*circumference, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('circumference', 2.0*edgeInd, ind='Max')
				except:
					pass
		return

class Theorem80(Theorem):
	def __init__(self):
		super(Theorem80, self).__init__(80, "if (defined girth and girth >= 4) or (undefined girth and nodes > 2) then { not complete };", "")
	def involves(self, str_invar):
		return str_invar in ["complete","girth","nodes"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (girth_Max != 'undt') and (girth_Min>=4.0) or (girth_Max == 'undt') and (nodes_Min>2.0):
			ingrid_obj.set('complete', False)
		return

