class Theorem81(Theorem):
	def __init__(self):
		super(Theorem81, self).__init__(81, "if regular then { nodeInd <= nodes/2 + (maxClique**2 + 3*maxClique - 2)/2*mindeg };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","mindeg","nodeInd","nodes","regular"]
	def run(self, ingrid_obj):
		regular = ingrid_obj.get('regular')
		if (regular == True):
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', 1.5*maxClique*mindeg+0.5*maxClique**2.0*mindeg-(1.0*mindeg)+0.5*nodes, ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('nodeInd', (-((2.0))+3.0*maxClique+maxClique**2.0)/2.0*mindeg+nodes/2.0, ind='Max')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if maxClique != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (nodeInd-(0.5*nodes))/(1.5*maxClique+0.5*maxClique**2.0-(1.0)), ind='Min')
				except:
					pass
			maxClique = ingrid_obj.get('maxClique', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodeInd = ingrid_obj.get('nodeInd', ind='Min')
			if maxClique != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*nodeInd-(3.0*maxClique*mindeg)-(1.0*maxClique**2.0*mindeg)+2.0*mindeg, ind='Min')
				except:
					pass
		return

class Theorem82(Theorem):
	def __init__(self):
		super(Theorem82, self).__init__(82, "if mindeg >= nodes/2 then { edgeConnec == mindeg };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (nodes_Max != 'undt' and (mindeg_Min>=nodes_Max/2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('edgeConnec', mindeg, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', mindeg, ind='Min')
			except:
				pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			if edgeConnec != 'undt':
				try:
					ingrid_obj.set('mindeg', edgeConnec, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			try:
				ingrid_obj.set('mindeg', edgeConnec, ind='Min')
			except:
				pass
		return

class Theorem83(Theorem):
	def __init__(self):
		super(Theorem83, self).__init__(83, "if genus > 0 then { arboricity <= 9 + (1+48*genus)**(1/2)/4 };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","genus"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		if (genus_Min>0.0):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('arboricity', 0.25*(48.0*genus+1.0)**0.5+9.0, ind='Max')
				except:
					pass
			arboricity = ingrid_obj.get('arboricity', ind='Max')
			if arboricity != 'undt':
				try:
					ingrid_obj.set('genus', 0.333333333333333*(1.0*arboricity-(9.0))**2.0-(2.08333333333333e-2), ind='Max')
				except:
					pass
		return

class Theorem84(Theorem):
	def __init__(self):
		super(Theorem84, self).__init__(84, "if maxClique == 2 then { arboricity <= 2 + genus**(1/2) };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","genus","maxClique"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('arboricity', 1.0*genus**0.5+2.0, ind='Max')
				except:
					pass
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*(1.0*arboricity-(2.0))**2.0, ind='Min')
			except:
				pass
		return

class Theorem85(Theorem):
	def __init__(self):
		super(Theorem85, self).__init__(85, "if maxClique == 2 then { chromaticNum <= 3 + 2*genus**(1/2) };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","genus","maxClique"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('chromaticNum', 2.0*genus**0.5+3.0, ind='Max')
				except:
					pass
			chromaticNum = ingrid_obj.get('chromaticNum', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*(0.5*chromaticNum-(1.5))**2.0, ind='Min')
			except:
				pass
		return

class Theorem86(Theorem):
	def __init__(self):
		super(Theorem86, self).__init__(86, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem87(Theorem):
	def __init__(self):
		super(Theorem87, self).__init__(87, "if genus > 0 then { mindeg <= 5 + (1 + 48*genus)**(1/2)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["genus","mindeg"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		if (genus_Min>0.0):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('mindeg', 0.5*(48.0*genus+1.0)**0.5+5.0, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('genus', 8.33333333333333e-2*(1.0*mindeg-(5.0))**2.0-(2.08333333333333e-2), ind='Max')
				except:
					pass
		return

class Theorem88(Theorem):
	def __init__(self):
		super(Theorem88, self).__init__(88, "if genus > 0 and maxClique <= 2 then { edgeConnec <= 2 + 2*genus**(1/2) };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","genus","maxClique"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (genus_Min>0.0) and (maxClique_Max != 'undt' and (maxClique_Max<=2.0)):
			genus = ingrid_obj.get('genus', ind='Max')
			if genus != 'undt':
				try:
					ingrid_obj.set('edgeConnec', 2.0*genus**0.5+2.0, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			try:
				ingrid_obj.set('genus', 1.0*(0.5*edgeConnec-(1.0))**2.0, ind='Min')
			except:
				pass
		return

class Theorem89(Theorem):
	def __init__(self):
		super(Theorem89, self).__init__(89, "if genus == 0 and girth == 3 then { edgeConnec <= 5 } else if genus == 0 and (girth == 4 or girth == 5) then { edgeConnec <= 3 } else if genus == 0 and girth >= 6 then { edgeConnec <= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","genus","girth"]
	def run(self, ingrid_obj):
		genus_Min = ingrid_obj.get('genus', ind='Min')
		genus_Max = ingrid_obj.get('genus', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
			try:
				ingrid_obj.set('edgeConnec', 5.0, ind='Max')
			except:
				pass
		elif (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Max==girth_Min and (girth_Min==4.0)) or (girth_Max==girth_Min and (girth_Min==5.0)):
			try:
				ingrid_obj.set('edgeConnec', 3.0, ind='Max')
			except:
				pass
		elif (genus_Max==genus_Min and (genus_Min==0.0)) and (girth_Min>=6.0):
			try:
				ingrid_obj.set('edgeConnec', 2.0, ind='Max')
			except:
				pass
		return

class Theorem90(Theorem):
	def __init__(self):
		super(Theorem90, self).__init__(90, "if genus <= 1 and girth == 3 then { edgeConnec <= 6 } else if genus <= 1 and girth == 4 then { edgeConnec <= 4 } else if genus <= 1 and (girth == 5 or girth == 6) then { edgeConnec <= 3 } else if genus <= 1 and girth >= 7 then { edgeConnec <= 2 };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","genus","girth"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==3.0)):
			try:
				ingrid_obj.set('edgeConnec', 6.0, ind='Max')
			except:
				pass
		elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==4.0)):
			try:
				ingrid_obj.set('edgeConnec', 4.0, ind='Max')
			except:
				pass
		elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Max==girth_Min and (girth_Min==5.0)) or (girth_Max==girth_Min and (girth_Min==6.0)):
			try:
				ingrid_obj.set('edgeConnec', 3.0, ind='Max')
			except:
				pass
		elif (genus_Max != 'undt' and (genus_Max<=1.0)) and (girth_Min>=7.0):
			try:
				ingrid_obj.set('edgeConnec', 2.0, ind='Max')
			except:
				pass
		return

class Theorem91(Theorem):
	def __init__(self):
		super(Theorem91, self).__init__(91, "if mindeg >= 3 and domination >= 1 and domination == (girth - 1)/4 then { nodes >= girth*(mindeg - 1)**domination };", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		domination_Min = ingrid_obj.get('domination', ind='Min')
		domination_Max = ingrid_obj.get('domination', ind='Max')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		if (mindeg_Min>=3.0) and (domination_Min>=1.0) and (domination_Max != 'undt' and (domination_Max<=(girth_Min-(1.0))/4.0)) and (girth_Max != 'undt' and (domination_Min>=(girth_Max-(1.0))/4.0)):
			domination = ingrid_obj.get('domination', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', girth*(mindeg-(1.0))**domination, ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', girth*(-((1.0))+mindeg)**domination, ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', nodes*(mindeg-(1.0))**(-(domination)), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (nodes/girth)**(1.0/domination)+1.0, ind='Max')
				except:
					pass
		return

class Theorem92(Theorem):
	def __init__(self):
		super(Theorem92, self).__init__(92, "if nodeConnec >= 2 then { circumference >= min(nodes, 2*mindeg) };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","mindeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (nodeConnec_Min>=2.0):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('circumference', min(nodes, 2.0*mindeg), ind='Min')
			except:
				pass
		return

class Theorem93(Theorem):
	def __init__(self):
		super(Theorem93, self).__init__(93, "if diameter == 2 and ((even nodes and even mindeg and nodes >= mindeg**3 + mindeg + 1) or ((odd nodes or odd mindeg) and nodes > mindeg**3 + 1)) then { edges >= ((nodes-1)*(mindeg+1)+1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edges","mindeg","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (even(nodes_Min) and even(nodes_Max)) and (even(mindeg_Min) and even(mindeg_Max)) and (mindeg_Max != 'undt' and (nodes_Min>=mindeg_Max**3.0+mindeg_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(mindeg_Min) and odd(mindeg_Max)) and (mindeg_Max != 'undt' and (nodes_Min>mindeg_Max**3.0+1.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 0.5*mindeg*nodes-(0.5*mindeg)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('mindeg', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if edges != 'undt' and mindeg != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*mindeg)/(mindeg+1.0), ind='Max')
				except:
					pass
		return

class Theorem94(Theorem):
	def __init__(self):
		super(Theorem94, self).__init__(94, "if diameter == 2 and (nodeConnec > 2 or nodeConnec < 2) and ((even nodes and even nodeConnec and nodes >= nodeConnec**3 + nodeConnec + 1) or ((odd nodes or odd nodeConnec) and nodes > nodeConnec**3 + 1)) then { edges >= ((nodes-1)*(nodeConnec+1)+1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edges","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		nodeConnec_Max = ingrid_obj.get('nodeConnec', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (nodeConnec_Min>2.0) or (nodeConnec_Max != 'undt' and (nodeConnec_Max<2.0)) and (even(nodes_Min) and even(nodes_Max)) and (even(nodeConnec_Min) and even(nodeConnec_Max)) and (nodeConnec_Max != 'undt' and (nodes_Min>=nodeConnec_Max**3.0+nodeConnec_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(nodeConnec_Min) and odd(nodeConnec_Max)) and (nodeConnec_Max != 'undt' and (nodes_Min>nodeConnec_Max**3.0+1.0)):
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 0.5*nodeConnec*nodes-(0.5*nodeConnec)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('nodeConnec', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if edges != 'undt' and nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*nodeConnec)/(nodeConnec+1.0), ind='Max')
				except:
					pass
		return

class Theorem95(Theorem):
	def __init__(self):
		super(Theorem95, self).__init__(95, "if diameter == 2 and ((even nodes and even edgeConnec and nodes >= edgeConnec**3 + edgeConnec + 1) or ((odd nodes or odd edgeConnec) and nodes > edgeConnec**3 + 1)) then { edges >= ((nodes-1)*(edgeConnec+1)+1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edgeConnec","edges","nodes"]
	def run(self, ingrid_obj):
		diameter_Min = ingrid_obj.get('diameter', ind='Min')
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
		edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
		if (diameter_Max==diameter_Min and (diameter_Min==2.0)) and (even(nodes_Min) and even(nodes_Max)) and (even(edgeConnec_Min) and even(edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (nodes_Min>=edgeConnec_Max**3.0+edgeConnec_Max+1.0)) or (odd(nodes_Min) and odd(nodes_Max)) or (odd(edgeConnec_Min) and odd(edgeConnec_Max)) and (edgeConnec_Max != 'undt' and (nodes_Min>edgeConnec_Max**3.0+1.0)):
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('edges', 0.5*edgeConnec*nodes-(0.5*edgeConnec)+0.5*nodes, ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if edges != 'undt':
				try:
					ingrid_obj.set('edgeConnec', 2.0*(1.0*edges-(0.5*nodes))/(nodes-(1.0)), ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			edges = ingrid_obj.get('edges', ind='Max')
			if edgeConnec != 'undt' and edges != 'undt':
				try:
					ingrid_obj.set('nodes', 2.0*(1.0*edges+0.5*edgeConnec)/(edgeConnec+1.0), ind='Max')
				except:
					pass
		return

class Theorem96(Theorem):
	def __init__(self):
		super(Theorem96, self).__init__(96, "if defined girth then { nodes >= (girth - 1)*(arboricity - 1) + 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","girth","nodes"]
	def run(self, ingrid_obj):
		girth_Max = ingrid_obj.get('girth', ind = 'Max')
		if (girth_Max != 'undt'):
			arboricity = ingrid_obj.get('arboricity', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*arboricity*girth-(1.0*arboricity)-(1.0*girth)+2.0, ind='Min')
			except:
				pass
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('arboricity', 1.0*(1.0*nodes+1.0*girth-(2.0))/(girth-(1.0)), ind='Max')
				except:
					pass
			arboricity = ingrid_obj.get('arboricity', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if arboricity != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', 1.0*(1.0*nodes+1.0*arboricity-(2.0))/(arboricity-(1.0)), ind='Max')
				except:
					pass
		return

class Theorem97(Theorem):
	def __init__(self):
		super(Theorem97, self).__init__(97, "if maxClique == 2 and chromaticNum >= 4 then { nodes >= 11 };", "")
	def involves(self, str_invar):
		return str_invar in ["chromaticNum","maxClique","nodes"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		chromaticNum_Min = ingrid_obj.get('chromaticNum', ind='Min')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)) and (chromaticNum_Min>=4.0):
			try:
				ingrid_obj.set('nodes', 11.0, ind='Min')
			except:
				pass
		return

class Theorem98(Theorem):
	def __init__(self):
		super(Theorem98, self).__init__(98, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem99(Theorem):
	def __init__(self):
		super(Theorem99, self).__init__(99, "if diameter <= 2 then { edgeConnec == mindeg };", "")
	def involves(self, str_invar):
		return str_invar in ["diameter","edgeConnec","mindeg"]
	def run(self, ingrid_obj):
		diameter_Max = ingrid_obj.get('diameter', ind='Max')
		if (diameter_Max != 'undt' and (diameter_Max<=2.0)):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			if mindeg != 'undt':
				try:
					ingrid_obj.set('edgeConnec', mindeg, ind='Max')
				except:
					pass
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('edgeConnec', mindeg, ind='Min')
			except:
				pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			if edgeConnec != 'undt':
				try:
					ingrid_obj.set('mindeg', edgeConnec, ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			try:
				ingrid_obj.set('mindeg', edgeConnec, ind='Min')
			except:
				pass
		return

class Theorem100(Theorem):
	def __init__(self):
		super(Theorem100, self).__init__(100, "if nodeInd >= edgeInd then { edgeCliqueCover <= nodeCover * nodeInd } ;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","edgeInd","nodeCover","nodeInd"]
	def run(self, ingrid_obj):
		nodeInd_Min = ingrid_obj.get('nodeInd', ind='Min')
		edgeInd_Max = ingrid_obj.get('edgeInd', ind='Max')
		if (edgeInd_Max != 'undt' and (nodeInd_Min>=edgeInd_Max)):
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

