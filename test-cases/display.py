import json


def disp_dict(inv_dict):
    keys = inv_dict.keys()
    str_len = len(max(keys, key=len))
    nums, bools = [], []
    for k in keys:
        s = k.ljust(str_len, ' ')
        if inv_dict[k]['Type'] != 'Bool':
            s += str(inv_dict[k]['Value']['Min'])[0:7].rjust(8, ' ')
            s += str(inv_dict[k]['Value']['Max'])[0:7].rjust(8, ' ')
            nums.append(s)
        else:
            s += str(inv_dict[k]['Value']).rjust(8, ' ')
            s += 8*' '
            bools.append(s)

    invs = nums+bools
    new_invs = []
    rows = 10
    for i in range(rows):
        new_invs.append('')
    for i in range(len(invs)):
        new_invs[i%rows] += invs[i] + ' | '

    for i in new_invs:
        print i
    print ''

'''
with open('init.json') as data_file:
    json_dict = json.load(data_file)

invariant_dict = json_dict['Invariants']

disp_dict(invariant_dict)
'''
