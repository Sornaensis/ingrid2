SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
SyntaxError('unexpected EOF while parsing', ('<string>', 0, 0, ''))
class Theorem381(Theorem):
	def __init__(self):
		super(Theorem381, self).__init__(381, "if planar and nodes >= 4 then { edges <= 3*nodes - 9 + min(3, edgeConnec) };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","edges","nodes","planar"]
	def run(self, ingrid_obj):
		planar = ingrid_obj.get('planar')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (planar == True) and (nodes_Min>=4.0):
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if edgeConnec != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 1.0*min(3.0, edgeConnec)+3.0*nodes-(9.0), ind='Max')
				except:
					pass
			edgeConnec = ingrid_obj.get('edgeConnec', ind='Min')
			edges = ingrid_obj.get('edges', ind='Min')
			try:
				ingrid_obj.set('nodes', 0.333333333333333*edges-(0.333333333333333*min(3.0, edgeConnec))+3.0, ind='Min')
			except:
				pass
		return

class Theorem382(Theorem):
	def __init__(self):
		super(Theorem382, self).__init__(382, "if planer and edgeConnec < mindeg and (nodes >= 5 or mindeg >= 2) then { if mindeg == edgeConnec + 1 and mindeg == 1 then { edges <= 3*nodes - 11 } else { edges <= 3*nodes - 12 + nodeConnec } };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeConnec","edges","mindeg","nodeConnec","nodes","planer"]
	def run(self, ingrid_obj):
		planer = ingrid_obj.get('planer')
		edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (planer == True) and (edgeConnec_Max != 'undt' and (edgeConnec_Max<mindeg_Min)) and (nodes_Min>=5.0) or (mindeg_Min>=2.0):
			mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
			edgeConnec_Min = ingrid_obj.get('edgeConnec', ind='Min')
			mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
			edgeConnec_Max = ingrid_obj.get('edgeConnec', ind='Max')
			
			if (mindeg_Max != 'undt' and (mindeg_Max<=edgeConnec_Min+1.0)) and (edgeConnec_Max != 'undt' and (mindeg_Min>=edgeConnec_Max+1.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==1.0)):
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('edges', 3.0*nodes-(11.0), ind='Max')
					except:
						pass
				edges = ingrid_obj.get('edges', ind='Min')
				try:
					ingrid_obj.set('nodes', 0.333333333333333*edges+3.66666666666667, ind='Min')
				except:
					pass
			elif (True):
				nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodeConnec != 'undt' and nodes != 'undt':
					try:
						ingrid_obj.set('edges', 1.0*nodeConnec+3.0*nodes-(12.0), ind='Max')
					except:
						pass
				edges = ingrid_obj.get('edges', ind='Min')
				nodes = ingrid_obj.get('nodes', ind='Max')
				if nodes != 'undt':
					try:
						ingrid_obj.set('nodeConnec', 1.0*edges-(3.0*nodes)+12.0, ind='Min')
					except:
						pass
				edges = ingrid_obj.get('edges', ind='Min')
				nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
				if nodeConnec != 'undt':
					try:
						ingrid_obj.set('nodes', 0.333333333333333*edges-(0.333333333333333*nodeConnec)+4.0, ind='Min')
					except:
						pass
		return

class Theorem383(Theorem):
	def __init__(self):
		super(Theorem383, self).__init__(383, "if not forest then { nodes >= maxdeg + numOfComponents - 2 + ((circumference*(girth-3)+2)/(girth/2)) };", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","forest","girth","maxdeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		forest = ingrid_obj.get('forest')
		if (forest == False):
			circumference = ingrid_obj.get('circumference', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*circumference-(6.0*circumference/girth)+1.0*maxdeg+1.0*numOfComponents-(2.0)+4.0/girth, ind='Min')
			except:
				pass
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Max')
			if maxdeg != 'undt' and numOfComponents != 'undt':
				try:
					ingrid_obj.set('circumference', (0.5*nodes*girth-(0.5*girth*maxdeg)-(0.5*girth*numOfComponents)+1.0*girth-(2.0))/(1.0*girth-(3.0)), ind='Min')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if circumference != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', (3.0*circumference-(2.0))/(-(0.5*nodes)+1.0*circumference+0.5*maxdeg+0.5*numOfComponents-(1.0)), ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if circumference != 'undt' and girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(2.0*circumference)+6.0*circumference/girth-(1.0*numOfComponents)+2.0-(4.0/girth), ind='Max')
				except:
					pass
			circumference = ingrid_obj.get('circumference', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if circumference != 'undt' and girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*nodes-(2.0*circumference)+6.0*circumference/girth-(1.0*maxdeg)+2.0-(4.0/girth), ind='Max')
				except:
					pass
		return

class Theorem384(Theorem):
	def __init__(self):
		super(Theorem384, self).__init__(384, "nodeCover <= (2*nodes + edges - edgeInd)/4;", "")
	def involves(self, str_invar):
		return str_invar in ["edgeInd","edges","nodeCover","nodes"]
	def run(self, ingrid_obj):
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edges != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('nodeCover', -(0.25*edgeInd)+0.25*edges+0.5*nodes, ind='Max')
			except:
				pass
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if edges != 'undt' and nodes != 'undt':
			try:
				ingrid_obj.set('edgeInd', -(4.0*nodeCover)+1.0*edges+2.0*nodes, ind='Max')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		nodes = ingrid_obj.get('nodes', ind='Max')
		if nodes != 'undt':
			try:
				ingrid_obj.set('edges', 4.0*nodeCover+1.0*edgeInd-(2.0*nodes), ind='Min')
			except:
				pass
		edgeInd = ingrid_obj.get('edgeInd', ind='Min')
		edges = ingrid_obj.get('edges', ind='Max')
		nodeCover = ingrid_obj.get('nodeCover', ind='Min')
		if edges != 'undt':
			try:
				ingrid_obj.set('nodes', 2.0*nodeCover+0.5*edgeInd-(0.5*edges), ind='Min')
			except:
				pass
		return

class Theorem385(Theorem):
	def __init__(self):
		super(Theorem385, self).__init__(385, "if genus <= nodes*(sqrt(2*nodes)-7)/12 + 1 then { edgeCliqueCover <= nodeCover*nodeInd };", "")
	def involves(self, str_invar):
		return str_invar in ["edgeCliqueCover","genus","nodeCover","nodeInd","nodes"]
	def run(self, ingrid_obj):
		genus_Max = ingrid_obj.get('genus', ind='Max')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (genus_Max != 'undt' and (genus_Max<=nodes_Min*((2.0*nodes_Min)**(1/2)-(7.0))/12.0+1.0)):
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

class Theorem386(Theorem):
	def __init__(self):
		super(Theorem386, self).__init__(386, "if mindeg >= 2 then { domination >= (girth+2)/3*numOfComponents };", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","mindeg","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (mindeg_Min>=2.0):
			girth = ingrid_obj.get('girth', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('domination', numOfComponents*(0.333333333333333*girth+0.666666666666667), ind='Min')
			except:
				pass
			domination = ingrid_obj.get('domination', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if domination != 'undt':
				try:
					ingrid_obj.set('girth', 3.0*domination/numOfComponents-(2.0), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			if domination != 'undt':
				try:
					ingrid_obj.set('numOfComponents', 1.0*domination/(0.333333333333333*girth+0.666666666666667), ind='Max')
				except:
					pass
		return

class Theorem387(Theorem):
	def __init__(self):
		super(Theorem387, self).__init__(387, "if mindeg >= 2 and girth >= 5 then { domination <= (nodes - girth/3 - (g - 4)*(mindeg - 2)*(mindeg - 3)/2 - 2*(mindeg - 2)+1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["domination","g","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Min>=2.0) and (girth_Min>=5.0):
			g = ingrid_obj.get('g', ind='Max')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if g != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.25*g*mindeg**2.0)+1.25*g*mindeg-(1.5*g)-(0.166666666666667*girth)+1.0*mindeg**2.0-(6.0*mindeg)+0.5*nodes+8.5, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('g', (-(4.0*domination)-(0.666666666666667*girth)+4.0*mindeg**2.0-(24.0*mindeg)+2.0*nodes+34.0)/(1.0*mindeg**2.0-(5.0*mindeg)+6.0), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			g = ingrid_obj.get('g', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if g != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', -(6.0*domination)-(1.5*g*mindeg**2.0)+7.5*g*mindeg-(9.0*g)+6.0*mindeg**2.0-(36.0*mindeg)+3.0*nodes+51.0, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Max')
			g = ingrid_obj.get('g', ind='Max')
			girth = ingrid_obj.get('girth', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if domination != 'undt' and g != 'undt' and girth != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('mindeg', (1.25*g+1.0*(-(1.0*domination*g)+4.0*domination+6.25e-2*g**2.0-(0.166666666666667*g*girth)+0.5*g*nodes-(0.5*g)+0.666666666666667*girth-(2.0*nodes)+2.0)**(1/2)-(6.0))/(0.5*g-(2.0)), ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			g = ingrid_obj.get('g', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*domination+0.5*g*mindeg**2.0-(2.5*g*mindeg)+3.0*g+0.333333333333333*girth-(2.0*mindeg**2.0)+12.0*mindeg-(17.0), ind='Min')
			except:
				pass
		return

class Theorem388(Theorem):
	def __init__(self):
		super(Theorem388, self).__init__(388, "if mindeg >= 2 and girth >= 9 then { domination <= (nodes-girth/3-(girth-4)*(mindeg-2)*(mindeg-3)/2+1)/2 };", "")
	def involves(self, str_invar):
		return str_invar in ["domination","girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		girth_Min = ingrid_obj.get('girth', ind='Min')
		if (mindeg_Min>=2.0) and (girth_Min>=9.0):
			girth = ingrid_obj.get('girth', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.25*girth*mindeg**2.0)+1.25*girth*mindeg-(1.66666666666667*girth)+1.0*mindeg**2.0-(5.0*mindeg)+0.5*nodes+6.5, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('girth', (-(1.0*domination)+1.0*mindeg**2.0-(5.0*mindeg)+0.5*nodes+6.5)/(0.25*mindeg**2.0-(1.25*mindeg)+1.66666666666667), ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Max')
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if girth != 'undt' and mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('domination', -(0.25*girth*mindeg**2.0)+1.25*girth*mindeg-(1.66666666666667*girth)+1.0*mindeg**2.0-(5.0*mindeg)+0.5*nodes+6.5, ind='Max')
				except:
					pass
			domination = ingrid_obj.get('domination', ind='Min')
			girth = ingrid_obj.get('girth', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 2.0*domination+0.5*girth*mindeg**2.0-(2.5*girth*mindeg)+3.33333333333333*girth-(2.0*mindeg**2.0)+10.0*mindeg-(13.0), ind='Min')
			except:
				pass
		return

class Theorem389(Theorem):
	def __init__(self):
		super(Theorem389, self).__init__(389, "if maxdeg >= 6 and maxClique <= maxdeg - 1 then { nodes <= maxdeg*nodeInd - 1 };", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique","maxdeg","nodeInd","nodes"]
	def run(self, ingrid_obj):
		maxdeg_Min = ingrid_obj.get('maxdeg', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxdeg_Min>=6.0) and (maxClique_Max != 'undt' and (maxClique_Max<=maxdeg_Min-(1.0))):
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			if maxdeg != 'undt' and nodeInd != 'undt':
				try:
					ingrid_obj.set('nodes', 1.0*maxdeg*nodeInd-(1.0), ind='Max')
				except:
					pass
			nodeInd = ingrid_obj.get('nodeInd', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if nodeInd != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*(nodes+1.0)/nodeInd, ind='Min')
				except:
					pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if maxdeg != 'undt':
				try:
					ingrid_obj.set('nodeInd', 1.0*(nodes+1.0)/maxdeg, ind='Min')
				except:
					pass
		return

class Theorem390(Theorem):
	def __init__(self):
		super(Theorem390, self).__init__(390, "if (nodes > 5 or nodes < 5) or (edges > 5 or edges < 5) or not cycle then { if maxClique > nodeInd then { maxClique >= (1/2)*log(2*nodes*sqrt(3.14159265359879),2) } else { nodeInd >= (1/2)*log(2*nodes*sqrt(3.14159265359879),2) } };", "")
	def involves(self, str_invar):
		return str_invar in ["cycle","edges","maxClique","nodeInd","nodes"]
	def run(self, ingrid_obj):
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		nodes_Max = ingrid_obj.get('nodes', ind='Max')
		edges_Min = ingrid_obj.get('edges', ind='Min')
		edges_Max = ingrid_obj.get('edges', ind='Max')
		cycle = ingrid_obj.get('cycle')
		if (nodes_Min>5.0) or (nodes_Max != 'undt' and (nodes_Max<5.0)) or (edges_Min>5.0) or (edges_Max != 'undt' and (edges_Max<5.0)) or (cycle == False):
			maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
			nodeInd_Max = ingrid_obj.get('nodeInd', ind='Max')
			
			if (nodeInd_Max != 'undt' and (maxClique_Min>nodeInd_Max)):
				nodes = ingrid_obj.get('nodes', ind='Min')
				try:
					ingrid_obj.set('maxClique', 0.721347520444482*log(nodes)+0.912874032369112, ind='Min')
				except:
					pass
				maxClique = ingrid_obj.get('maxClique', ind='Max')
				if maxClique != 'undt':
					try:
						ingrid_obj.set('nodes', 0.282094791773474*exp(1.38629436111989*maxClique), ind='Max')
					except:
						pass
			elif (True):
				nodes = ingrid_obj.get('nodes', ind='Min')
				try:
					ingrid_obj.set('nodeInd', 0.721347520444482*log(nodes)+0.912874032369112, ind='Min')
				except:
					pass
				nodeInd = ingrid_obj.get('nodeInd', ind='Max')
				if nodeInd != 'undt':
					try:
						ingrid_obj.set('nodes', 0.282094791773474*exp(1.38629436111989*nodeInd), ind='Max')
					except:
						pass
		return

class Theorem391(Theorem):
	def __init__(self):
		super(Theorem391, self).__init__(391, "if circumference <= nodes - mindeg then {edges <= nodes * (nodes - 1)/2 - mindeg *(nodes - mindeg - 1)};", "")
	def involves(self, str_invar):
		return str_invar in ["circumference","edges","mindeg","nodes"]
	def run(self, ingrid_obj):
		circumference_Max = ingrid_obj.get('circumference', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		nodes_Min = ingrid_obj.get('nodes', ind='Min')
		if (circumference_Max != 'undt' and (circumference_Max<=nodes_Min-(mindeg_Min))):
			mindeg = ingrid_obj.get('mindeg', ind='Max')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if mindeg != 'undt' and nodes != 'undt':
				try:
					ingrid_obj.set('edges', 1.0*mindeg**2.0-(1.0*mindeg*nodes)+1.0*mindeg+0.5*nodes**2.0-(0.5*nodes), ind='Max')
				except:
					pass
			edges = ingrid_obj.get('edges', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('mindeg', 0.5*(nodes-(1.0))+0.5*(4.0*edges-(1.0*nodes**2.0)+1.0)**(1/2), ind='Min')
			except:
				pass
			edges = ingrid_obj.get('edges', ind='Min')
			mindeg = ingrid_obj.get('mindeg', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*(1.0*mindeg+0.5)+1.0*(2.0*edges-(1.0*mindeg**2.0)-(1.0*mindeg)+0.25)**(1/2), ind='Min')
			except:
				pass
		return

class Theorem392(Theorem):
	def __init__(self):
		super(Theorem392, self).__init__(392, "if girth == 5 and mindeg >= 6 then {nodes >= 40} else if girth == 5 and mindeg == 5 then {nodes >= 5} else if girth == 5 and mindeg == 4 then {nodes >= 19};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","mindeg","nodes"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		mindeg_Max = ingrid_obj.get('mindeg', ind='Max')
		if (girth_Max==girth_Min and (girth_Min==5.0)) and (mindeg_Min>=6.0):
			try:
				ingrid_obj.set('nodes', 40.0, ind='Min')
			except:
				pass
		elif (girth_Max==girth_Min and (girth_Min==5.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==5.0)):
			try:
				ingrid_obj.set('nodes', 5.0, ind='Min')
			except:
				pass
		elif (girth_Max==girth_Min and (girth_Min==5.0)) and (mindeg_Max==mindeg_Min and (mindeg_Min==4.0)):
			try:
				ingrid_obj.set('nodes', 19.0, ind='Min')
			except:
				pass
		return

class Theorem393(Theorem):
	def __init__(self):
		super(Theorem393, self).__init__(393, "if girth == 6 and mindeg >= 7 and regular then {nodes >= 90} else if girth == 6 and mindeg >= 7 and not regular then {nodes >= 93};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","mindeg","nodes","regular"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		girth_Max = ingrid_obj.get('girth', ind='Max')
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		regular = ingrid_obj.get('regular')
		if (girth_Max==girth_Min and (girth_Min==6.0)) and (mindeg_Min>=7.0) and (regular == True):
			try:
				ingrid_obj.set('nodes', 90.0, ind='Min')
			except:
				pass
		elif (girth_Max==girth_Min and (girth_Min==6.0)) and (mindeg_Min>=7.0) and (regular == False):
			try:
				ingrid_obj.set('nodes', 93.0, ind='Min')
			except:
				pass
		return

class Theorem394(Theorem):
	def __init__(self):
		super(Theorem394, self).__init__(394, "if maxClique == 2 then {nodeInd >= nodes *(2*edges/nodes * ln(2*edges/nodes) - 2*edges/nodes +1)/((2*edges/nodes - 1)**2)};", "")
	def involves(self, str_invar):
		return str_invar in ["maxClique"]
	def run(self, ingrid_obj):
		maxClique_Min = ingrid_obj.get('maxClique', ind='Min')
		maxClique_Max = ingrid_obj.get('maxClique', ind='Max')
		if (maxClique_Max==maxClique_Min and (maxClique_Min==2.0)):
		return

class Theorem395(Theorem):
	def __init__(self):
		super(Theorem395, self).__init__(395, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem396(Theorem):
	def __init__(self):
		super(Theorem396, self).__init__(396, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

class Theorem397(Theorem):
	def __init__(self):
		super(Theorem397, self).__init__(397, "if girth >= 5+ log(max(1,genus),3) then {arboricity <= 2};", "")
	def involves(self, str_invar):
		return str_invar in ["arboricity","genus","girth"]
	def run(self, ingrid_obj):
		girth_Min = ingrid_obj.get('girth', ind='Min')
		genus_Max = ingrid_obj.get('genus', ind='Max')
		if (genus_Max != 'undt' and (girth_Min>=5.0+log(max(1.0, genus_Max), 3.0))):
			try:
				ingrid_obj.set('arboricity', 2.0, ind='Max')
			except:
				pass
		return

class Theorem398(Theorem):
	def __init__(self):
		super(Theorem398, self).__init__(398, "if mindeg >= 2 then {nodes >= girth * numOfComponents + maxdeg - 2};", "")
	def involves(self, str_invar):
		return str_invar in ["girth","maxdeg","mindeg","nodes","numOfComponents"]
	def run(self, ingrid_obj):
		mindeg_Min = ingrid_obj.get('mindeg', ind='Min')
		if (mindeg_Min>=2.0):
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			try:
				ingrid_obj.set('nodes', 1.0*girth*numOfComponents+1.0*maxdeg-(2.0), ind='Min')
			except:
				pass
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('girth', (1.0*nodes-(1.0*maxdeg)+2.0)/numOfComponents, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			numOfComponents = ingrid_obj.get('numOfComponents', ind='Min')
			if nodes != 'undt':
				try:
					ingrid_obj.set('maxdeg', 1.0*nodes-(1.0*girth*numOfComponents)+2.0, ind='Max')
				except:
					pass
			girth = ingrid_obj.get('girth', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Max')
			if nodes != 'undt':
				try:
					ingrid_obj.set('numOfComponents', (1.0*nodes-(1.0*maxdeg)+2.0)/girth, ind='Max')
				except:
					pass
		return

class Theorem399(Theorem):
	def __init__(self):
		super(Theorem399, self).__init__(399, "if nodeConnec > 0 then {nodeConnec >= (nodes *(maxdeg - 2))/((maxdeg-1)**diam + maxdeg - 3)};", "")
	def involves(self, str_invar):
		return str_invar in ["diam","maxdeg","nodeConnec","nodes"]
	def run(self, ingrid_obj):
		nodeConnec_Min = ingrid_obj.get('nodeConnec', ind='Min')
		if (nodeConnec_Min>0.0):
			diam = ingrid_obj.get('diam', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			if diam != 'undt':
				try:
					ingrid_obj.set('nodeConnec', nodes*(maxdeg-(2.0))/(maxdeg+(maxdeg-(1.0))**diam-(3.0)), ind='Min')
				except:
					pass
			diam = ingrid_obj.get('diam', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', (nodes*(-((2.0))+maxdeg))/(-((3.0))+maxdeg+(-((1.0))+maxdeg)**diam), ind='Min')
			except:
				pass
			diam = ingrid_obj.get('diam', ind='Min')
			maxdeg = ingrid_obj.get('maxdeg', ind='Min')
			nodes = ingrid_obj.get('nodes', ind='Min')
			try:
				ingrid_obj.set('nodeConnec', (nodes*(-((2.0))+maxdeg))/(-((3.0))+maxdeg+(-((1.0))+maxdeg)**diam), ind='Min')
			except:
				pass
			diam = ingrid_obj.get('diam', ind='Max')
			maxdeg = ingrid_obj.get('maxdeg', ind='Max')
			nodeConnec = ingrid_obj.get('nodeConnec', ind='Max')
			if diam != 'undt' and maxdeg != 'undt' and nodeConnec != 'undt':
				try:
					ingrid_obj.set('nodes', nodeConnec*(maxdeg+(maxdeg-(1.0))**diam-(3.0))/(maxdeg-(2.0)), ind='Max')
				except:
					pass
		return

class Theorem400(Theorem):
	def __init__(self):
		super(Theorem400, self).__init__(400, "null;", "")
	def involves(self, str_invar):
		return str_invar in []
	def run(self, ingrid_obj):
		return

