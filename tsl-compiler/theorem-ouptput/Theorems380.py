class Theorem361(Theorem):
	def __init__(self):
		super(Theorem361, self).__init__(361, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem362(Theorem):
	def __init__(self):
		super(Theorem362, self).__init__(362, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem363(Theorem):
	def __init__(self):
		super(Theorem363, self).__init__(363, "if diameter == 2 and nodeConnec >= 3 then { edges >= (nodes-1)*(nodeConnec+1)/(2 - nodeConnec**2 + 2*nodeConnec) };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodeConnec_Min>=3.0):
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', (nodeConnec*nodes-(1.0*nodeConnec)+1.0*nodes-(1.0))/(2.0*nodeConnec-(nodeConnec**2.0)+2.0), ind='Min')
			except:
				pass
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', (-((1.0))+nodes)*(1.0+nodeConnec)/(2.0*nodeConnec-((nodeConnec**2.0))+2.0), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if edges != 'undt' and nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodes', (2.0*edges*nodeConnec-(edges*nodeConnec**2.0)+2.0*edges+1.0*nodeConnec+1.0)/(nodeConnec+1.0), ind='Max')
				except:
					pass
		return

class Theorem364(Theorem):
	def __init__(self):
		super(Theorem364, self).__init__(364, "if diameter == 2 and nodeConnec >= 3 and nodes >= 3*nodeConnec**2 + 6 then { edges > (nodes - 1)*(nodeConnec + 1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodeConnec_Min>=3.0) and (nodeConnec_Max != 'undt' and (nodes_Min>=3.0*nodeConnec_Max**2.0+6.0)):
			
			
			
		return

class Theorem365(Theorem):
	def __init__(self):
		super(Theorem365, self).__init__(365, "if bipartite then { if odd nodes then { crossing <= (nodes/4)**2*((nodes-2)/4)**2 } else { crossing <= ((nodes+1)/4)*((nodes-1)/4)**2*(nodes-3)/4 } };", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","crossing","nodes"]
	def run(self, ingrid_obj):
		bipartite = ingrid_obj.get('bipartite')
		if (bipartite == True):
			nodes_Min = ingrid_obj.get('nodes', ind='Min')
			nodes_Max = ingrid_obj.get('nodes', ind='Max')
			
			if (odd(nodes_Min) and odd(nodes_Max)):
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('crossing', 6.25e-2*nodes**2.0*(0.25*nodes-(0.5))**2.0, ind='Max')
					except:
						pass
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('crossing', (nodes/4.0)**2.0*((-((2.0))+nodes)/4.0)**2.0, ind='Max')
					except:
						pass
			elif (True):
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('crossing', (nodes-(1.0))**2.0*(3.90625e-3*nodes**2.0-(7.8125e-3*nodes)-(1.171875e-2)), ind='Max')
					except:
						pass
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('crossing', ((1.0+nodes)/4.0)*((-((1.0))+nodes)/4.0)**2.0*(-((3.0))+nodes)/4.0, ind='Max')
					except:
						pass
		return

class Theorem366(Theorem):
	def __init__(self):
		super(Theorem366, self).__init__(366, "if connected then { spectralRadius >= 2*cos(3.14159265358979/(nodes+1)) };", "")
	def involves(self, str_invar):
		return str_invar in ["connected"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		if (connected == True):
		return

class Theorem367(Theorem):
	def __init__(self):
		super(Theorem367, self).__init__(367, "if regular and mindeg >= 7 and odd mindeg and (mindeg > 9 or mindeg < 9) and not bipartite and girth  == 4 then { nodes >= 2*(5*mindeg/4) + 4 };", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","girth","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		bipartite = ingrid_obj.get('bipartite')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (regular == True) and (mindeg_Min>=7.0) and (odd(mindeg_Min) and odd(mindeg_Max)) and (mindeg_Min>9.0) or (mindeg_Max != 'undt' and (mindeg_Max<9.0)) and (bipartite == False) and (girth_Max==girth_Min and (girth_Min==4.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.5*mindeg+4.0, ind='Min')
			except:
				pass
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.4*nodes-(1.6), ind='Max')
				except:
					pass
		return

class Theorem368(Theorem):
	def __init__(self):
		super(Theorem368, self).__init__(368, "if bipartite then { thickness <= nodes/8 + 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["bipartite","nodes","thickness"]
	def run(self, ingrid_obj):
		bipartite = ingrid_obj.get('bipartite')
		if (bipartite == True):
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('thickness', 0.125*nodes+2.0, ind='Max')
				except:
					pass
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('nodes', 8.0*thickness-(16.0), ind='Min')
			except:
				pass
		return

class Theorem369(Theorem):
	def __init__(self):
		super(Theorem369, self).__init__(369, "if maxClique <= 2 then { thickness <= genus + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","maxClique","thickness"]
	def run(self, ingrid_obj):
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('thickness', 1.0*genus+1.0, ind='Max')
				except:
					pass
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*thickness-(1.0), ind='Min')
			except:
				pass
		return

class Theorem370(Theorem):
	def __init__(self):
		super(Theorem370, self).__init__(370, "if genus <= 1 then { thickness == genus + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","thickness"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		if (genus_Max != 'undt' and (genus_Max<=1.0)):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('thickness', 1.0*genus+1.0, ind='Max')
				except:
					pass
			genus = ingrid_obj.get('genus', ind='Min')
			try:
				ingrid_obj.set('thickness', 1.0*genus+1.0, ind='Min')
			except:
				pass
			thickness = ingrid_obj.get('thickness', ind='Max')
			if thickness != 'undt':
				try:
					ingrid_obj.set('genus', 1.0*thickness-(1.0), ind='Max')
				except:
					pass
			thickness = ingrid_obj.get('thickness', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*thickness-(1.0), ind='Min')
			except:
				pass
		return

class Theorem371(Theorem):
	def __init__(self):
		super(Theorem371, self).__init__(371, "arboricity <= edgeCover;", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","edgeCover"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('arboricity', edgeCover, ind='Max')
			except:
				pass
		arboricity = ingrid_obj.get('arboricity', ind='Min')
		try:
			ingrid_obj.set('edgeCover', arboricity, ind='Min')
		except:
			pass
		return

class Theorem372(Theorem):
	def __init__(self):
		super(Theorem372, self).__init__(372, "thickness <= edgeCover;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","thickness"]
	def run(self, ingrid_obj):
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('thickness', edgeCover, ind='Max')
			except:
				pass
		thickness = ingrid_obj.get('thickness', ind='Min')
		try:
			ingrid_obj.set('edgeCover', thickness, ind='Min')
		except:
			pass
		return

class Theorem373(Theorem):
	def __init__(self):
		super(Theorem373, self).__init__(373, "if genus >= 1 then { edgeCover <= 2 + sqrt(3*genus) };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","genus"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		if (genus_Min>=1.0):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('edgeCover', 1.73205080756888*genus**0.5+2.0, ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*(0.577350269189626*edgeCover-(1.15470053837925))**2.0, ind='Min')
			except:
				pass
		return

class Theorem374(Theorem):
	def __init__(self):
		super(Theorem374, self).__init__(374, "thickness <= 5 + sqrt(2*genus - 2);", "")
	def involves(self, str_invar):
		return str_invar in ["genus","thickness"]
	def run(self, ingrid_obj):
		genus = ingrid_obj.get('genus', ind='Max')
		if genus != 'undt':
			try:
				ingrid_obj.set('thickness', 1.4142135623731*(genus-(1.0))**0.5+5.0, ind='Max')
			except:
				pass
		thickness = ingrid_obj.get('thickness', ind='Max')
		if thickness != 'undt':
			try:
				ingrid_obj.set('genus', 0.5*(1.0*thickness-(5.0))**2.0+1.0, ind='Max')
			except:
				pass
		return

class Theorem375(Theorem):
	def __init__(self):
		super(Theorem375, self).__init__(375, "if connected and regular then { edgeCover <= 4 + (6*genus+2)/(nodes - 1) };", "")
	def involves(self, str_invar):
		return str_invar in ["connected","edgeCover","genus","nodes","regular"]
	def run(self, ingrid_obj):
		connected = ingrid_obj.get('connected')
		regular = ingrid_obj.get('regular')
		if (connected == True) and (regular == True):
			genus = ingrid_obj.get('genus', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if genus != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edgeCover', 1.0*(6.0*genus+4.0*nodes-(2.0))/(nodes-(1.0)), ind='Max')
				except:
					pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('genus', 0.166666666666667*edgeCover*nodes-(0.166666666666667*edgeCover)-(0.666666666666667*nodes)+0.333333333333333, ind='Min')
			except:
				pass
			edgeCover = ingrid_obj.get('edgeCover', ind='Min')
			genus = ingrid_obj.get('genus', ind='Min')
			try:
				ingrid_obj.set('nodes', (1.0*edgeCover+6.0*genus-(2.0))/(1.0*edgeCover-(4.0)), ind='Min')
			except:
				pass
		return

class Theorem376(Theorem):
	def __init__(self):
		super(Theorem376, self).__init__(376, "genus <= (thickness - 1)*(nodes - 1);", "")
	def involves(self, str_invar):
		return str_invar in ["genus","nodes","thickness"]
	def run(self, ingrid_obj):
		nodes = ingrid_obj.get('nodes', ind='Max')
		thickness = ingrid_obj.get('thickness', ind='Max')
		if nodes != 'undt' and thickness != 'undt':
			try:
				ingrid_obj.set('genus', 1.0*nodes*thickness-(1.0*nodes)-(1.0*thickness)+1.0, ind='Max')
			except:
				pass
		genus = ingrid_obj.get('genus', ind='Min')
		thickness = ingrid_obj.get('thickness', ind='Min')
		try:
			ingrid_obj.set('nodes', 1.0*(genus+thickness-(1.0))/(thickness-(1.0)), ind='Min')
		except:
			pass
		genus = ingrid_obj.get('genus', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		try:
			ingrid_obj.set('thickness', 1.0*(genus+nodes-(1.0))/(nodes-(1.0)), ind='Min')
		except:
			pass
		return

class Theorem377(Theorem):
	def __init__(self):
		super(Theorem377, self).__init__(377, "edgeCover <= (maxdeg + 2)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","maxdeg"]
	def run(self, ingrid_obj):
		maxdeg = ingrid_obj.get('maxdeg', ind='Max')
		if maxdeg != 'undt':
			try:
				ingrid_obj.set('edgeCover', 0.5*maxdeg+1.0, ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		try:
			ingrid_obj.set('maxdeg', 2.0*edgeCover-(2.0), ind='Min')
		except:
			pass
		return

class Theorem378(Theorem):
	def __init__(self):
		super(Theorem378, self).__init__(378, "edgeCover >= (mindeg+1)/2;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","mindeg"]
	def run(self, ingrid_obj):
		mindeg = ingrid_obj.get('mindeg', ind='Min')
		try:
			ingrid_obj.set('edgeCover', 0.5*mindeg+0.5, ind='Min')
		except:
			pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Max')
		if edgeCover != 'undt':
			try:
				ingrid_obj.set('mindeg', 2.0*edgeCover-(1.0), ind='Max')
			except:
				pass
		return

class Theorem379(Theorem):
	def __init__(self):
		super(Theorem379, self).__init__(379, "edgeCover >= edges/(nodes-numOfComponents);", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","edges","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		edges = ingrid_obj.get('edges', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edgeCover', edges/(nodes-(numOfComponents)), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Min')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if numOfComponents != 'undt':
			try:
				ingrid_obj.set('edges', edgeCover*(nodes-(numOfComponents)), ind='Min')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
		if edges != 'undt' and numOfComponents != 'undt':
			try:
				ingrid_obj.set('nodes', numOfComponents+edges/edgeCover, ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('numOfComponents', nodes-(edges/edgeCover), ind='Min')
			except:
				pass
		return

class Theorem380(Theorem):
	def __init__(self):
		super(Theorem380, self).__init__(380, "edgeCover <= 3*thickness;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCover","thickness"]
	def run(self, ingrid_obj):
		thickness = ingrid_obj.get('thickness', ind='Max')
		if thickness != 'undt':
			try:
				ingrid_obj.set('edgeCover', 3.0*thickness, ind='Max')
			except:
				pass
		edgeCover = ingrid_obj.get('edgeCover', ind='Min')
		try:
			ingrid_obj.set('thickness', 0.333333333333333*edgeCover, ind='Min')
		except:
			pass
		return

