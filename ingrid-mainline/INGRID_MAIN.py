import json
from INGRID_CLASSES import IngridObj
from tempfile import NamedTemporaryFile
from ntpath import basename
from os import remove
from string import replace
import sys
 
# TODO implement creating addenda
def create_addenda(thm_eqn):
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
        error_msg, thm_code = create_addenda(thm['Text'])
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
        thm_code_new = replace(thm_code_new, '$$THM_NAME$$', thm['Name'])
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
def get_base_thms(thm_file_name):
    thm_module = __import__(thm_file_name) # change this to file name
    thms = []
    while True:
        try:
            Thm = getattr(thm_module, 'Theorem'+str(len(thms)+1)) # Assumes thm names are # Theorem1, ..., TheoremN
            thms.append(Thm())
        except AttributeError:
            break
    
    return thms

    
# runs the mainline with a given json dictionary, returns a python dictionary
def run_mainline_old(json_obj, thm_file_name):
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
            return json_dict
        
        # gets base theorems
        base_thms = get_base_thms(thm_file_name)
        
        all_thms = base_thms + addenda_thms
        
        # runs ingrid
        ingrid = IngridObj()
        ingrid.go(json_dict.copy(), all_thms)
        new_dict = ingrid.create_dict()
        return new_dict
    

def run_mainline(json_obj, thm_file_name, addenda_list):
    json_dict = json.loads(json_obj)
    # sends the initialization json to the server
    if json_dict == {}:
        with open('init.json') as data_file:
            json_dict = json.load(data_file)
            sys.stderr.write(str(json_dict.keys()) + '\n')
            return json.dumps(json_dict)
    # runs ingrid with given non-empty json dictionary
    else:
        base_thms = get_base_thms(thm_file_name)
        all_thms = base_thms + addenda_list
        # runs ingrid
        ingrid = IngridObj()
        ingrid.go(json_dict.copy(), all_thms)
        new_dict = ingrid.create_dict()
        sys.stderr.write(str(new_dict.keys()) + '\n')
        #sys.stderr.write(str(new_dict) + '\n')
        #sys.stderr.write('Right before main return!\n')
        deser = json.dumps(new_dict)
        #sys.stderr.write(str(deser) + '\n')
        return deser

