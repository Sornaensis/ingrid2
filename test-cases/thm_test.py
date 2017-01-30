import math
from INGRID_CLASSES import Theorem

# We must create a theorem which does not allow isolated nodes (i.e. edges >= nodes/2)

'''
given "edges <= (nodes*(nodes-1))/2"
- do parsing stuff
output should be the following

def run(self, ingrid_obj):
    nodes_max = ingrid_obj.get('nodes', ind='Max')
    # get all rhs values
    if nodes_max != 'undt':
        result = (nodes_max * (nodes_max - 1)) / 2
        ingrid_obj.set('edges', result, ind='Max', thm_id=self.id, thm_str=self.str, thm_name=self.name)

'''
'''
if cycle then not forest

def run(self, ingrid_obj):
    cycle = ingrid_obj.get('cycle')
    if cycle == True:
        ingrid_obj.set('forest', False, thm_id=self.id, thm_str=self.str, thm_name=self.name)

'''

'''
if kappa >= 2: then c >= min(p, 2*mindeg)

def run(self, ingrid_obj):
    kappa_min = ingrid_obj.get('kappa', ind='Min')
    if kappa_min >= 2:
        p_min = ingrid_obj.get('nodes', ind='Min')
        mindeg_min = ingrid_obj.get('mindeg', ind='Min')
        ingrid_obj.set('c', min(p_min, 2*mindeg_min), thm_id=self.id, thm_str=self.str, thm_name=self.name)
'''






class Theorem1(Theorem):
    def __init__(self):
        super(Theorem1, self).__init__(1, 'edges <= [nodes(nodes-1)]/2', 'Edge-Node Theorem')

    def involves(self, str_invar):
        return str_invar in ['nodes', 'edges']

    def run(self, ingrid_obj):
        nodes_max = ingrid_obj.get('nodes', ind='Max')
        if nodes_max != 'undt':
            new_edges_max = (nodes_max * (nodes_max - 1)) / 2
            ingrid_obj.set('edges', new_edges_max, ind='Max')

        edges_min = ingrid_obj.get('edges', ind='Min')
        new_nodes_min = (1 + math.sqrt(1 + 8 * edges_min)) / 2
        ingrid_obj.set('nodes', new_nodes_min, ind='Min')

        
class Theorem2(Theorem):
    def __init__(self):
        super(Theorem2, self).__init__(2, 'edges <= [nodes(nodes-1)]/2', 'Edge-Node Theorem COPY')

    def involves(self, str_invar):
        return str_invar in ['nodes', 'edges']

    def run(self, ingrid_obj):
        nodes_max = ingrid_obj.get('nodes', ind='Max')
        if nodes_max != 'undt':
            new_edges_max = (nodes_max * (nodes_max - 1)) / 2
            ingrid_obj.set('edges', new_edges_max, ind='Max')

        edges_min = ingrid_obj.get('edges', ind='Min')
        new_nodes_min = (1 + math.sqrt(1 + 8 * edges_min)) / 2
        ingrid_obj.set('nodes', new_nodes_min, ind='Min')
