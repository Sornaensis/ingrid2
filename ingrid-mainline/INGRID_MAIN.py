import json
from INGRID_CLASSES import IngridObj

    
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
        
        

def run_mainline(json_obj, thm_file_name, addenda):
    json_dict = json.loads(json_obj)
    # sends the initialization json to the server
    if json_dict == {}:
        with open('init.json') as data_file:
            json_dict = json.load(data_file)
            return json_dict
    # runs ingrid with given non-empty json dictionary
    else:
        base_thms = get_base_thms(thm_file_name)
        all_thms = base_thms + addenda
        # runs ingrid
        ingrid = IngridObj()
        ingrid.go(json_dict.copy(), all_thms)
        new_dict = ingrid.create_dict()
        return new_dict

