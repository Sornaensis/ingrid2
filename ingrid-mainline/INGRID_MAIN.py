import json
from INGRID_CLASSES import IngridObj
from thm_test import Theorem1
from tempfile import NamedTemporaryFile
from ntpath import basename
from os import remove
from string import replace


def test():
    ingrid = IngridObj()
    thm1 = Theorem1()
        
    # get the initialization json
    with open('init.json') as data_file:
        json_obj = json.load(data_file)

    # change the invariant values
    json_obj['Invariants']['nodes']['Value']['Max'] = '7'
    json_obj['Invariants']['nodes']['Changed'] = 'True'
    json_obj['Invariants']['edges']['Value']['Min'] = '30'
    json_obj['Invariants']['edges']['Changed'] = 'True'

    # Original input
    print 'Input' 
    print 'Nodes =', json_obj['Invariants']['nodes']['Value']
    print 'Nodes Trace =', json_obj['Invariants']['nodes']['Trace']  
    print 'Edges=', json_obj['Invariants']['edges']['Value']
    print 'Edges Trace =', json_obj['Invariants']['edges']['Trace']
    print json_obj['Theorems']
    print json_obj['Addenda']
    print json_obj['Error']

    # run ingrid
    ingrid.go(json_obj.copy(), [thm1])
    new_dict = ingrid.create_dict()

    # see results
    print 'Output' 
    print 'Nodes =', new_dict['Invariants']['nodes']['Value']
    print 'Nodes Trace =', new_dict['Invariants']['nodes']['Trace'] 
    print 'Edges=', new_dict['Invariants']['edges']['Value']
    print 'Edges Trace =', new_dict['Invariants']['edges']['Trace']  
    print new_dict['Theorems']
    print new_dict['Addenda']
    print new_dict['Error']


# TODO implement sending json to frontend
def send_json(json_dict):
    print 'TODO: Send json to server', json.dumps(json_dict)
    exit()
 
 
# TODO implement creating addenda
def create_addenda(thm_eqn):
    print 'TODO call addenda creator'
    error_msg, thm_code = '', 'import math\n\ndef $$THM$$():\n\ta = 49\n\tb = math.sqrt(a)\n\tprint b\n\treturn b\n'   
    return thm_code
 

# returns a list of all the theorem objects
def get_addenda_thms(addenda):
    tmp = NamedTemporaryFile(dir='./')
    module_name = basename(tmp.name)
    module = open(module_name+'.py', 'w')
    module.write('import math\n\n\n')
    
    thm_names = []
    for thm in addenda:
        error_msg, thm_code = create_addenda(addenda['Text'])
        # error occurred in parser
        if error_msg != '':
            module.close()
            remove('./' + module_name + '.py')
            remove('./' + module_name + '.pyc')
            tmp.close()
            return error_msg

        thm_name = 'AddTheorem' + str(len(thm_names)+1)
        thm_names.append(thm_name)
        thm_code_new = replace(thm_code, '$$THM$$', thm_name)
        module.write(thm_code_new + '\n\n')
        
    module.close()
    fileX = __import__(module_name)
    
    thms = []
    for class_name in thm_names:
        TheoremX = getattr(fileX, class_name)
        thms.append(TheoremX())
    
    remove('./' + module_name + '.py')
    remove('./' + module_name + '.pyc')
    tmp.close()
    
    return thms

    
# returns a list of all the base theorem objects
def get_base_thms():
    thm_module = __import__('theorems') # change this to file name
    thms = []
    while True:
        try:
            Thm = getattr(thm_module, 'Theorem'+str(len(thms)+1)) # Assumes thm names are # Theorem1, ..., TheoremN
            thms.append(Thm())
        except AttributeError:
            break
    
    return thms

    
# runs the mainline with a given json dictionary, returns a python dictionary
def run_mainline(json_obj):
    json_dict = json.loads(json_obj)
    # sends the initialization json to the server
    if json_dict == {}:
        with open('init.json') as data_file:
            json_dict = json.load(data_file)
            return json_dict
    # runs ingrid with given non-empty json dictionary
    else:
        # creates user defined theorems
        addenda_thms = get_addenda_thms(json_dict['Addenda'])
        if isinstance(addenda_thms, basestring):
            json_dict['Error'] = {'ErrorType': 'TheoremParser', 'ErrMsg': addenda_thms}
            print 'ERROR'
            return json_dict
        
        # gets base theorems
        base_thms = get_base_thms()
        
        all_thms = base_thms + addenda_thms
        
        # runs ingrid
        ingrid = IngridObj()
        ingrid.go(json_dict.copy(), all_thms)
        new_dict = ingrid.create_dict()
        return new_dict
        
        
#json_input = {}
#run_mainline(json_input)

#test()


