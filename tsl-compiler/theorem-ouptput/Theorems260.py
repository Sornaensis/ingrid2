class Theorem241(Theorem):
	def __init__(self):
		super(Theorem241, self).__init__(241, "if maxClique == 2 then { chromaticNum <= 3*(nodes+12)/16 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 0.1875*nodes+2.25, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('nodes', 5.33333333333333*chromaticNum-(12.0), ind='Min')
			except:
				pass
		return

class Theorem242(Theorem):
	def __init__(self):
		super(Theorem242, self).__init__(242, "nodes >= nodeCliqueCover + chromaticNum - 1;", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*chromaticNum+1.0*nodeCliqueCover-(1.0), ind='Min')
		except:
			pass
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0*nodes-(1.0*nodeCliqueCover)+1.0, ind='Max')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0*nodes-(1.0*chromaticNum)+1.0, ind='Max')
			except:
				pass
		return

class Theorem243(Theorem):
	def __init__(self):
		super(Theorem243, self).__init__(243, "nodes >= maxdeg + domination;", "")
	def involves(self, str_invar):
		return str_invar in ["domination","maxdeg","nodes"]
	def run(self, ingrid_obj):
		domination = ingrid_obj.get('domination', ind='Min')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		try:
			ingrid_obj.set('nodes', domination+maxdeg, ind='Min')
		except:
			pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('domination', nodes-(maxdeg), ind='Max')
			except:
				pass
		domination = ingrid_obj.get('domination', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', nodes-(domination), ind='Max')
			except:
				pass
		return

class Theorem244(Theorem):
	def __init__(self):
		super(Theorem244, self).__init__(244, "if nodeInd == 2 then {nodeCliqueCover <= 3*(nodes + 12)/16};", "")
	def involves(self, str_invar):
		return str_invar in ["nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('nodeCliqueCover', 0.1875*nodes+2.25, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('nodes', 5.33333333333333*nodeCliqueCover-(12.0), ind='Min')
			except:
				pass
		return

class Theorem245(Theorem):
	def __init__(self):
		super(Theorem245, self).__init__(245, "if mindeg >= 2 then {edgeCliqueCover <= 2*(nodes - 2 + 2*genus) - 4*(numOfComponents - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","genus","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (mindeg_Min>=2.0):
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeCliqueCover', 4.0*genus+2.0*nodes-(4.0*numOfComponents), ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 0.25*edgeCliqueCover-(0.5*nodes)+1.0*numOfComponents, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*edgeCliqueCover-(2.0*genus)+2.0*numOfComponents, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', -(0.25*edgeCliqueCover)+1.0*genus+0.5*nodes, ind='Max')
				except:
					pass
		return

class Theorem246(Theorem):
	def __init__(self):
		super(Theorem246, self).__init__(246, "if nodes >= 3 then {edgeCliqueCover <= 2*(nodes - 2 + 2*genus) - (numOfComponents - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","genus","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodes_Min>=3.0):
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeCliqueCover', 4.0*genus+2.0*nodes-(1.0*numOfComponents)-(3.0), ind='Max')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 0.25*edgeCliqueCover-(0.5*nodes)+0.25*numOfComponents+0.75, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if genus != 'undt':
				try:
					ingrid_obj.set('nodes', 0.5*edgeCliqueCover-(2.0*genus)+0.5*numOfComponents+1.5, ind='Min')
				except:
					pass
			edgeCliqueCover = ingrid_obj.get('edgeCliqueCover', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', -(1.0*edgeCliqueCover)+4.0*genus+2.0*nodes-(3.0), ind='Max')
				except:
					pass
		return

class Theorem247(Theorem):
	def __init__(self):
		super(Theorem247, self).__init__(247, "nodeInd <= nodes /(1+mindeg/maxdeg);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if maxdeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeInd', 1.0*maxdeg*nodes/(maxdeg+mindeg), ind='Max')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if mindeg != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0*nodeInd*mindeg/(nodeInd-(nodes))), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeInd != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('mindeg', -(1.0*maxdeg*(nodeInd-(nodes))/nodeInd), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*nodeInd*(maxdeg+mindeg)/maxdeg, ind='Min')
		except:
			pass
		return

class Theorem248(Theorem):
	def __init__(self):
		super(Theorem248, self).__init__(248, "nodeCover >= nodes/(1+maxdeg/mindeg);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","mindeg","nodeCover","nodes"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*mindeg*nodes/(maxdeg+mindeg), ind='Min')
			except:
				pass
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if mindeg != 'undt':
			try:
				ingrid_obj.set('maxdeg', -(1.0*mindeg*(nodeCover-(nodes))/nodeCover), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('mindeg', -(1.0*nodeCover*maxdeg/(nodeCover-(nodes))), ind='Max')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Max')
		if maxdeg != 'undt' and mindeg != 'undt' and nodeCover != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*nodeCover*(maxdeg+mindeg)/mindeg, ind='Max')
			except:
				pass
		return

class Theorem249(Theorem):
	def __init__(self):
		super(Theorem249, self).__init__(249, "nodeInd >= nodes / (bandwidth + 1);", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodeInd","nodes"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if bandwidth != 'undt':
			try:
				ingrid_obj.set('nodeInd', 1.0*nodes/(bandwidth+1.0), ind='Min')
			except:
				pass
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('bandwidth', -(1.0)+1.0*nodes/nodeInd, ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if bandwidth != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*nodeInd*(bandwidth+1.0), ind='Max')
			except:
				pass
		return

class Theorem250(Theorem):
	def __init__(self):
		super(Theorem250, self).__init__(250, "nodeCover <= nodes/(1+1/bandwidth);", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","nodeCover","nodes"]
	def run(self, ingrid_obj):
		bandwidth = ingrid_obj.get('bandwidth', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if bandwidth != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', 1.0*bandwidth*nodes/(bandwidth+1.0), ind='Max')
			except:
				pass
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodeCover != 'undt':
			try:
				ingrid_obj.set('bandwidth', -(1.0*nodeCover/(nodeCover-(nodes))), ind='Min')
			except:
				pass
		bandwidth = ingrid_obj.get('bandwidth', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*nodeCover*(bandwidth+1.0)/bandwidth, ind='Min')
		except:
			pass
		return

class Theorem251(Theorem):
	def __init__(self):
		super(Theorem251, self).__init__(251, "if defined girth then {edge >= (girth - 1)*(arboricity - 1) ** 2 + (arboricity - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","edge","girth"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		if (girth_Max != 'undt'):
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('edge', arboricity+girth*(arboricity-(1.0))**2.0-(1.0*(arboricity-(1.0))**2.0)-(1.0), ind='Min')
			except:
				pass
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('edge', (-((1.0))+arboricity)+(-((1.0))+girth)*(-((1.0))+arboricity)**2.0, ind='Min')
			except:
				pass
			arboricity = ingrid_obj.get('arboricity', ind='Max')
			edge = ingrid_obj.get('edge', ind='Max')
			if arboricity != 'undt' and edge != 'undt':
				try:
					ingrid_obj.set('girth', (arboricity-(1.0))**(-(2.0))*(edge-(arboricity)+1.0*(arboricity-(1.0))**2.0+1.0), ind='Max')
				except:
					pass
		return

class Theorem252(Theorem):
	def __init__(self):
		super(Theorem252, self).__init__(252, "if nodeConnec >= 2 and girth >= 4 and istrue congruent(girth, 1, 4) then {edgeInd >= maxdeg*(girth-1)/4} else if nodeConnec >= 2 and girth >= 4 and (istrue congruent(girth, 2, 4) or (maxdeg == 2 and istrue congruent(girth, 3, 4))) then {edgeInd >= maxdeg*(girth-1)/4 + 1} else if nodeConnec>=2 and girth>=4 and (istrue congruent(g, 0, 4) or (maxdeg>=3 and istrue congruent(g,3,4))) then {edgeInd >= maxdeg*(girth-1)/4 + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","g","girth","maxdeg","nodeConnec"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind = 'Min')
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxdeg_Max = ingrid_obj.get('maxdeg', ind='Max')
		g_Min = ingrid_obj.get('g', ind = 'Min')
		g_Max = ingrid_obj.get('g', ind = 'Max')
		if (nodeConnec_Min>=2.0) and (girth_Min>=4.0) and (girth_Min == girth_Max):
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.25*maxdeg*(girth-(1.0)), ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('girth', 4.0*edgeInd/maxdeg+1.0, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', 4.0*edgeInd/(girth-(1.0)), ind='Max')
				except:
					pass
		elif (nodeConnec_Min>=2.0) and (girth_Min>=4.0) and (girth_Min == girth_Max) or (maxdeg_Max==maxdeg_Min and (maxdeg_Min==2.0)) and (girth_Min == girth_Max):
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.25*girth*maxdeg-(0.25*maxdeg)+1.0, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if edgeInd != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('girth', (4.0*edgeInd+1.0*maxdeg-(4.0))/maxdeg, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', 4.0*(edgeInd-(1.0))/(girth-(1.0)), ind='Max')
				except:
					pass
		elif (nodeConnec_Min>=2.0) and (girth_Min>=4.0) and (g_Min == g_Max) or (maxdeg_Min>=3.0) and (g_Min == g_Max):
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.25*girth*maxdeg-(0.25*maxdeg)+2.0, ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if edgeInd != 'undt' and maxdeg != 'undt':
				try:
					ingrid_obj.set('girth', (4.0*edgeInd+1.0*maxdeg-(8.0))/maxdeg, ind='Max')
				except:
					pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', 4.0*(1.0*edgeInd-(2.0))/(girth-(1.0)), ind='Max')
				except:
					pass
		return

class Theorem253(Theorem):
	def __init__(self):
		super(Theorem253, self).__init__(253, "if nodeConnec >= 1 then { maxdeg <= (nodes - 1)/((girth-1)/4 *(nodeConnec-1)+1) };", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (nodeConnec_Min>=1.0):
			girth = ingrid_obj.get('girth', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*(nodes-(1.0))/(0.25*girth*nodeConnec-(0.25*girth)-(0.25*nodeConnec)+1.25), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', (1.0*maxdeg*nodeConnec-(5.0*maxdeg)+4.0*nodes-(4.0))/(maxdeg*(nodeConnec-(1.0))), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeConnec', (1.0*maxdeg*girth-(5.0*maxdeg)+4.0*nodes-(4.0))/(maxdeg*(girth-(1.0))), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.25*maxdeg*girth*nodeConnec-(0.25*maxdeg*girth)-(0.25*maxdeg*nodeConnec)+1.25*maxdeg+1.0, ind='Min')
			except:
				pass
		return

class Theorem254(Theorem):
	def __init__(self):
		super(Theorem254, self).__init__(254, "if nodeInd == 2 and (mindeg == 1 or nodes <= 4) then {nodeCliqueCover <= 2} else if nodeInd == 2 and (nodes >= 5 and nodes <= 10) then {nodeInd <= 3} else if nodeInd == 2 then {nodeCliqueCover <= (mindeg + 11)/4};", "")
	def involves(self, str_invar):
		return str_invar in ["mindeg","nodeCliqueCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==1.0)) or (nodes_Max != 'undt' and (nodes_Max<=4.0)):
			try:
				ingrid_obj.set('nodeCliqueCover', 2.0, ind='Max')
			except:
				pass
		elif (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)) and (nodes_Min>=5.0) and (nodes_Max != 'undt' and (nodes_Max<=10.0)):
			try:
				ingrid_obj.set('nodeInd', 3.0, ind='Max')
			except:
				pass
		elif (nodeInd_Max==nodeInd_Min and (nodeInd_Min==2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('nodeCliqueCover', 0.25*mindeg+2.75, ind='Max')
				except:
					pass
			nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Min')
			try:
				ingrid_obj.set('mindeg', 4.0*nodeCliqueCover-(11.0), ind='Min')
			except:
				pass
		return

class Theorem255(Theorem):
	def __init__(self):
		super(Theorem255, self).__init__(255, "if connected then {edges >= nodes + 8*thickness - 13};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edges","nodes","thickness"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			nodes = ingrid_obj.get('nodes', ind='Min')
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('edges', 1.0*nodes+8.0*thickness-(13.0), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*edges-(8.0*thickness)+13.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('thickness', 0.125*edges-(0.125*nodes)+1.625, ind='Max')
				except:
					pass
		return

class Theorem256(Theorem):
	def __init__(self):
		super(Theorem256, self).__init__(256, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem257(Theorem):
	def __init__(self):
		super(Theorem257, self).__init__(257, "if diam >= 3 and (odd diam or nodeConnec == 1) then {edgeInd >= nodeConnec * (diam-1)/2} else if diam >= 3 and (even diam and nodeConnec >= 2) then {edgeInd >= nodeConnec *(diam-1)/2};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","edgeInd","nodeConnec"]
	def run(self, ingrid_obj):
		diam_Min = ingrid_obj.get('diam', ind='Min')
		diam_Max = ingrid_obj.get('diam', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (diam_Min>=3.0) and (odd(diam_Min) and odd(diam_Max)) or (nodeConnec_Max==nodeConnec_Min and (nodeConnec_Min==1.0)):
			diam = ingrid_obj.get('diam', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*nodeConnec*(diam-(1.0)), ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('diam', 2.0*edgeInd/nodeConnec+1.0, ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeConnec', 2.0*edgeInd/(diam-(1.0)), ind='Max')
				except:
					pass
		elif (diam_Min>=3.0) and (even(diam_Min) and even(diam_Max)) and (nodeConnec_Min>=2.0):
			diam = ingrid_obj.get('diam', ind='Min')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			try:
				ingrid_obj.set('edgeInd', 0.5*nodeConnec*(diam-(1.0)), ind='Min')
			except:
				pass
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('diam', 2.0*edgeInd/nodeConnec+1.0, ind='Max')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			edgeInd = ingrid_obj.get('edgeInd', ind='Max')
			if edgeInd != 'undt':
				try:
					ingrid_obj.set('nodeConnec', 2.0*edgeInd/(diam-(1.0)), ind='Max')
				except:
					pass
		return

class Theorem258(Theorem):
	def __init__(self):
		super(Theorem258, self).__init__(258, "if ((nodeConnec > 0 and nodes > 2) or mindeg > 1) and ((thickness > 3 or thickness < 3) and (nodes < 9 or nodes > 10)) then {genus >= thickness + (edges - 4*nodes - 1)/6};", "")
	def involves(self, str_invar):
		return str_invar in ["edges","genus","mindeg","nodeConnec","nodes","thickness"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		thickness_Min = ingrid_obj.get('thickness', ind='Min')
		thickness_Max = ingrid_obj.get('thickness', ind='Max')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodeConnec_Min>0.0) and (nodes_Min>2.0) or (mindeg_Min>1.0) and (thickness_Min>3.0) or (thickness_Max != 'undt' and (thickness_Max<3.0)) and (nodes_Max != 'undt' and (nodes_Max<9.0)) or (nodes_Min>10.0):
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('genus', 0.166666666666667*edges-(0.666666666666667*nodes)+1.0*thickness-(0.166666666666667), ind='Min')
				except:
					pass
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Min')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 6.0*genus+4.0*nodes-(6.0*thickness)+1.0, ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			thickness = ingrid_obj.get('thickness', ind='Min')
			if genus != 'undt':
				try:
					ingrid_obj.set('nodes', -(1.5*genus)+0.25*edges+1.5*thickness-(0.25), ind='Min')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('thickness', 1.0*genus-(0.166666666666667*edges)+0.666666666666667*nodes+0.166666666666667, ind='Max')
				except:
					pass
		return

class Theorem259(Theorem):
	def __init__(self):
		super(Theorem259, self).__init__(259, "if girth > 1 + 2 * (log(nodes)/log(2)) then {chromaticNum <= 3};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","girth","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (girth_Min>1.0+2.0*(log(nodes_Max)/log(2.0)))):
			try:
				ingrid_obj.set('chromaticNum', 3.0, ind='Max')
			except:
				pass
		return

class Theorem260(Theorem):
	def __init__(self):
		super(Theorem260, self).__init__(260, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

