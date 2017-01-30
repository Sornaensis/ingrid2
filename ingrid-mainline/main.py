from INGRID_MAIN import run_mainline
import json

def main(json_dict, addenda_list):
    py_dict = run_mainline(json_dict, 'theorems', addenda_list) # change 'theorems' to the file name of the base theorems
    return json.dumps(py_dict)
    
    