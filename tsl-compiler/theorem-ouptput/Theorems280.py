class Theorem261(Theorem):
	def __init__(self):
		super(Theorem261, self).__init__(261, "if genus <= 2 and girth >= 5 then {chromaticNum <= 4};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus","girth"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (genus_Max != 'undt' and (genus_Max<=2.0)) and (girth_Min>=5.0):
			try:
				ingrid_obj.set('chromaticNum', 4.0, ind='Max')
			except:
				pass
		return

class Theorem262(Theorem):
	def __init__(self):
		super(Theorem262, self).__init__(262, "if (genus == 0  and girth >= 4) or (genus <= 1 and girth >= 6) or (genus <= 2 and girth >= 7) or (girth >= 9) then {chromaticNum <= 3};", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus","girth"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		genus_Max = ingrid_obj.get('genus', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Min>=4.0) or (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Min>=6.0) or (genus_Max != 'undt' and (genus_Max<=2.0)) and (girth_Min>=7.0) or (girth_Min>=9.0):
			try:
				ingrid_obj.set('chromaticNum', 3.0, ind='Max')
			except:
				pass
		return

class Theorem263(Theorem):
	def __init__(self):
		super(Theorem263, self).__init__(263, "maxdeg >= (nodes - 1)^(1/radius);", "")
	def involves(self, str_invar):
		return str_invar in ["maxdeg","nodes","radius"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Min')
		radius = ingrid_obj.get('radius', ind='Max')
		if radius != 'undt':
			try:
				ingrid_obj.set('maxdeg', (nodes-(1.0))**(1.0/radius), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		radius = ingrid_obj.get('radius', ind='Max')
		if maxdeg != 'undt' and radius != 'undt':
			try:
				ingrid_obj.set('nodes', maxdeg**(1.0*radius)+1.0, ind='Max')
			except:
				pass
		nodes = ingrid_obj.get('nodes', ind='Min')
		radius = ingrid_obj.get('radius', ind='Max')
		if radius != 'undt':
			try:
				ingrid_obj.set('maxdeg', (-((1.0))+nodes)**(1.0/radius), ind='Min')
			except:
				pass
		return

class Theorem264(Theorem):
	def __init__(self):
		super(Theorem264, self).__init__(264, "if connected then { diameter <= 3*domination - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","domination"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			domination = ingrid_obj.get('domination', ind='Max')
			if domination != 'undt':
				try:
					ingrid_obj.set('diameter', 3.0*domination-(1.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('domination', 0.333333333333333*diameter+0.333333333333333, ind='Min')
			except:
				pass
		return

class Theorem265(Theorem):
	def __init__(self):
		super(Theorem265, self).__init__(265, "if connected and maxdeg >= 3 then {nodes <= 1 + mindeg*((maxdeg-1)^diameter - 1)/(maxdeg-2)};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","diameter","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (connected == True) and (maxdeg_Min>=3.0):
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', (1.0*maxdeg+mindeg*(maxdeg-(1.0))**diameter-(1.0*mindeg)-(2.0))/(maxdeg-(2.0)), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg*(-((1.0))+(-((1.0))+maxdeg)**diameter)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if diameter != 'undt' and maxdeg != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', mindeg*(-((1.0))+(-((1.0))+maxdeg)**diameter)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diameter != 'undt':
				try:
					ingrid_obj.set('mindeg', (nodes*maxdeg-(2.0*nodes)-(1.0*maxdeg)+2.0)/((maxdeg-(1.0))**diameter-(1.0)), ind='Min')
				except:
					pass
		return

class Theorem266(Theorem):
	def __init__(self):
		super(Theorem266, self).__init__(266, "if diameter >= 2 and maxdeg >= 3 then {maxdeg >= ceil((nodes-1)/mindeg)**(1/(diameter-1))};", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxdeg","mindeg","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (diameter_Min>=2.0) and (maxdeg_Min>=3.0):
			diameter = ingrid_obj.get('diameter', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diameter != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('maxdeg', ceil((nodes-(1.0))/mindeg)**(1.0/(diameter-(1.0))), ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('diameter', log((maxdeg*ceil((nodes-(1.0))/mindeg))**(1.0/log(maxdeg))), ind='Min')
				except:
					pass
		return

class Theorem267(Theorem):
	def __init__(self):
		super(Theorem267, self).__init__(267, "if diameter == radius and radius == 2 then {maxdeg >= 2};", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","maxdeg","radius"]
	def run(self, ingrid_obj):
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		radius_Min = ingrid_obj.get('radius', ind='Min')
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		radius_Max = ingrid_obj.get('radius', ind='Max')
		if (diameter_Max != 'undt' and (diameter_Max<=radius_Min)) and (radius_Max != 'undt' and (diameter_Min>=radius_Max)) and (radius_Max==radius_Min and (radius_Min==2.0)):
			try:
				ingrid_obj.set('maxdeg', 2.0, ind='Min')
			except:
				pass
		return

class Theorem268(Theorem):
	def __init__(self):
		super(Theorem268, self).__init__(268, "if not forest then {bandwidth >= (girth - 1)*(arboricity - 2) + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","bandwidth","forest","girth"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('bandwidth', 1.0*arboricity*girth-(1.0*arboricity)-(2.0*girth)+4.0, ind='Min')
			except:
				pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			if bandwidth != 'undt' and girth != 'undt':
				try:
					ingrid_obj.set('arboricity', 1.0*(1.0*bandwidth+2.0*girth-(4.0))/(girth-(1.0)), ind='Max')
				except:
					pass
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			try:
				ingrid_obj.set('girth', (1.0*bandwidth+1.0*arboricity-(4.0))/(1.0*arboricity-(2.0)), ind='Min')
			except:
				pass
		return

class Theorem269(Theorem):
	def __init__(self):
		super(Theorem269, self).__init__(269, "if not forest then {bandwidth >= (girth - 1)*nodes/(2*nodeInd) - girth + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","forest","girth","nodeInd","nodes"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			girth = ingrid_obj.get('girth', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('bandwidth', -(1.0*girth)+0.5*girth*nodes/nodeInd+2.0-(0.5*nodes/nodeInd), ind='Min')
			except:
				pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if bandwidth != 'undt':
				try:
					ingrid_obj.set('girth', (-(1.0*bandwidth*nodeInd)+2.0*nodeInd-(0.5*nodes))/(1.0*nodeInd-(0.5*nodes)), ind='Min')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if bandwidth != 'undt':
				try:
					ingrid_obj.set('nodeInd', 0.5*nodes*(girth-(1.0))/(1.0*bandwidth+1.0*girth-(2.0)), ind='Min')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if bandwidth != 'undt' and girth != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*nodeInd*(2.0*bandwidth+2.0*girth-(4.0))/(girth-(1.0)), ind='Max')
				except:
					pass
		return

class Theorem270(Theorem):
	def __init__(self):
		super(Theorem270, self).__init__(270, "if not forest then {domination <= nodes - floor(2*circumference/3)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","domination","forest","nodes"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			circumference = ingrid_obj.get('circumference', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(floor(2.0*circumference/3.0))+nodes, ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Min')
			domination = ingrid_obj.get('domination', ind='Min')
			try:
				ingrid_obj.set('nodes', domination+floor(2.0*circumference/3.0), ind='Min')
			except:
				pass
		return

class Theorem271(Theorem):
	def __init__(self):
		super(Theorem271, self).__init__(271, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem272(Theorem):
	def __init__(self):
		super(Theorem272, self).__init__(272, "if diameter == 2 then {domination <= nodeConnec};", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","domination","nodeConnec"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)):
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if nodeConnec != 'undt':
				try:
					ingrid_obj.set('domination', nodeConnec, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', domination, ind='Min')
			except:
				pass
		return

class Theorem273(Theorem):
	def __init__(self):
		super(Theorem273, self).__init__(273, "if tree then {radius == floor((diameter+1)/2)};", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","radius","tree"]
	def run(self, ingrid_obj):
		tree = ingrid_obj.get('tree')
		if (tree == True):
			diameter = ingrid_obj.get('diameter', ind='Max')
			if diameter != 'undt':
				try:
					ingrid_obj.set('radius', floor((diameter+1.0)/2.0), ind='Max')
				except:
					pass
			diameter = ingrid_obj.get('diameter', ind='Min')
			try:
				ingrid_obj.set('radius', floor((diameter+1.0)/2.0), ind='Min')
			except:
				pass
		return

class Theorem274(Theorem):
	def __init__(self):
		super(Theorem274, self).__init__(274, "if Hamiltonian then {nodes >= (maxdeg - 1)*(girth - 2) + 2};", "")
	def involves(self, str_invar):
		return str_invar in ["Hamiltonian","girth","maxdeg","nodes"]
	def run(self, ingrid_obj):
		Hamiltonian = ingrid_obj.get('Hamiltonian')
		if (Hamiltonian == True):
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*girth*maxdeg-(1.0*girth)-(2.0*maxdeg)+4.0, ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxdeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', 1.0*(1.0*nodes+2.0*maxdeg-(4.0))/(maxdeg-(1.0)), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('maxdeg', (1.0*nodes+1.0*girth-(4.0))/(1.0*girth-(2.0)), ind='Min')
			except:
				pass
		return

class Theorem275(Theorem):
	def __init__(self):
		super(Theorem275, self).__init__(275, "nodeInd >= maxdeg/(chromaticNum-1);", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxdeg","nodeInd"]
	def run(self, ingrid_obj):
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		if chromaticNum != 'undt':
			try:
				ingrid_obj.set('nodeInd', 1.0*maxdeg/(chromaticNum-(1.0)), ind='Min')
			except:
				pass
		maxdeg = ingrid_obj.get('maxdeg', ind='Min')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if nodeInd != 'undt':
			try:
				ingrid_obj.set('chromaticNum', 1.0+1.0*maxdeg/nodeInd, ind='Min')
			except:
				pass
		chromaticNum = ingrid_obj.get('chromaticNum', ind='Max')
		nodeInd = ingrid_obj.get('nodeInd', ind='Max')
		if chromaticNum != 'undt' and nodeInd != 'undt':
			try:
				ingrid_obj.set('maxdeg', 1.0*nodeInd*(chromaticNum-(1.0)), ind='Max')
			except:
				pass
		return

class Theorem276(Theorem):
	def __init__(self):
		super(Theorem276, self).__init__(276, "maxClique >= (nodes - mindeg - 1)/(nodeCliqueCover-1);", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","mindeg","nodeCliqueCover","nodes"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if mindeg != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('maxClique', 1.0*(-(mindeg)+nodes-(1.0))/(nodeCliqueCover-(1.0)), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('mindeg', -(1.0*maxClique*nodeCliqueCover)+1.0*maxClique+1.0*nodes-(1.0), ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Min')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if mindeg != 'undt':
			try:
				ingrid_obj.set('nodeCliqueCover', 1.0*(maxClique-(mindeg)+nodes-(1.0))/maxClique, ind='Min')
			except:
				pass
		maxClique = ingrid_obj.get('maxClique', ind='Max')
		mindeg = ingrid_obj.get('mindeg', ind='Max')
		nodeCliqueCover = ingrid_obj.get('nodeCliqueCover', ind='Max')
		if maxClique != 'undt' and mindeg != 'undt' and nodeCliqueCover != 'undt':
			try:
				ingrid_obj.set('nodes', 1.0*maxClique*nodeCliqueCover-(1.0*maxClique)+1.0*mindeg+1.0, ind='Max')
			except:
				pass
		return

class Theorem277(Theorem):
	def __init__(self):
		super(Theorem277, self).__init__(277, "if nodes >= 3 and nodeConnec <= 1 then {edgeConnec <= maxdeg/2};", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (nodes_Min>=3.0) and (nodeConnec_Max != 'undt' and (nodeConnec_Max<=1.0)):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('edgeConnec', 0.5*maxdeg, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			try:
				ingrid_obj.set('maxdeg', 2.0*edgeConnec, ind='Min')
			except:
				pass
		return

class Theorem278(Theorem):
	def __init__(self):
		super(Theorem278, self).__init__(278, "if connected and maxdeg >= 3 then {nodes <= 1 + maxdeg*((maxdeg-1)^radius - 1)/(maxdeg-2)};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","maxdeg","nodes","radius"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		if (connected == True) and (maxdeg_Min>=3.0):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if maxdeg != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('nodes', (maxdeg*(maxdeg-(1.0))**radius-(2.0))/(maxdeg-(2.0)), ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if maxdeg != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg*(-((1.0))+(-((1.0))+maxdeg)**radius)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			radius = ingrid_obj.get('radius', ind='Max')
			if maxdeg != 'undt' and radius != 'undt':
				try:
					ingrid_obj.set('nodes', maxdeg*(-((1.0))+(-((1.0))+maxdeg)**radius)/(-((2.0))+maxdeg)+1.0, ind='Max')
				except:
					pass
		return

class Theorem279(Theorem):
	def __init__(self):
		super(Theorem279, self).__init__(279, "if connected then {nodes >= maxdeg + 2*radius - 2};", "")
	def involves(self, str_invar):
		return str_invar in ["connected","maxdeg","nodes","radius"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			radius = ingrid_obj.get('radius', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*maxdeg+2.0*radius-(2.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			radius = ingrid_obj.get('radius', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(2.0*radius)+2.0, ind='Max')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('radius', 0.5*nodes-(0.5*maxdeg)+1.0, ind='Max')
				except:
					pass
		return

class Theorem280(Theorem):
	def __init__(self):
		super(Theorem280, self).__init__(280, "if forest then {nodes >= 2*(bandwidth + numOfComponents - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["bandwidth","forest","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == True):
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*bandwidth+2.0*numOfComponents-(2.0), ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('bandwidth', 0.5*nodes-(1.0*numOfComponents)+1.0, ind='Max')
				except:
					pass
			bandwidth = ingrid_obj.get('bandwidth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 0.5*nodes-(1.0*bandwidth)+1.0, ind='Max')
				except:
					pass
		return

