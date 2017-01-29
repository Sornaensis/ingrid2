from display import disp_dict
import json
from INGRID_MAIN import run_mainline

'''

run : runs ingrid with the changed invariants
set invar [>=, <=, =] val : sets the invariant min, max, or eq to value
    invar val1 val2 : sets invariant min and max to val2 and val2 respectively
list [a] : lists all invariants and their bounds, [a] for alphabetical order
exit : exits the program

trace invar : gives the trace of an invariant

'''


class IngridUI():
    def __init__(self):
        with open('init.json') as data_file:
            self.json_dict = json.load(data_file)
        with open('init.json') as data_file:
            self.prev_dict = json.load(data_file)

    def print_trace(self, invar):
        if invar not in self.json_dict['Invariants'].keys():
            print invar + ' is not a valid invariant'
        
        trace = self.json_dict['Invariants'][invar]['Trace']
        theorems_used = self.json_dict['Theorems']
        
        for i in range(len(trace)):
            t = trace[i]
            print t['Message'], '| From Theorem #' + str(t['TheoremId'])   
            
    def process_input(self, input):
        command = input.split()
        if len(command) == 0:
            return

        if command[0] == 'exit':
            print 'Thank you for running Ingrid. Have a nice day!'
            exit()
        elif command[0] == 'run':
            self.prev_dict = self.json_dict
            self.json_dict = run_mainline(json.dumps(self.json_dict))
            if self.json_dict['Error']['ErrorType'] != '':
                print "ERROR OCCURED\n", self.json_dict['Error']
            else:    
                disp_dict(self.json_dict['Invariants'])
        elif command[0] == 'list':
            disp_dict(self.json_dict['Invariants'])
        elif command[0] == 'set':
            if len(command) < 4:
                print 'Not enough arguments for set command'
                return
            if command[1] not in self.json_dict['Invariants'].keys():
                print command[1], ' is not a valid invariant.'
                return

            if command[2] == '>=':
                self.set_invar(command[1], bound1=command[3])
            elif command[2] == '<=':
                self.set_invar(command[1], bound2=command[3])
            elif command[2] == '=':
                self.set_invar(command[1], bound1=command[3], bound2=command[3], val=command[3])
            else:
                self.set_invar(command[1], bound1=command[2], bound2=command[3])
        elif command[0] == 'help':
            print 'List of Commands:'
            print 'run : runs ingrid with the changed invariants'
            print 'set invariant >= val : sets the minimum bound to the given value for the given invariant'
            print '    invariant <= val : sets the maximum bound to the given value for the given invariant'
            print '    invariant = val : sets the minimum and maximum bounds to the given value for the given ' \
                  'invariant. Also used to set boolean invariants.'
            print '    invariant val1 val2 : sets the minimum and maximum bounds to val1 and val2 respectively for ' \
                  'the given invariant.'
            print 'list [a] : lists all invariants and their bounds, [a] for alphabetical order'
            print 'exit : exits the program'
        elif command[0] == 'trace':
            if len(command) == 1:
                print 'Need an invariant name'
                return
            self.print_trace(command[1])
        else:
            print 'Not a command'    
            
    def set_invar(self, invar, bound1=None, bound2=None, val=None):
        if self.json_dict['Invariants'][invar]['Type'] == 'Integer':
            if bound1 is not None:
                if not bound1.isdigit():
                    print bound1, 'is an invalid value for an integer invariant. Should be an integer.'
                    return
                if self.json_dict['Invariants'][invar]['Value']['Min'] != bound1:
                    self.json_dict['Invariants'][invar]['Value']['Min'] = bound1
                    self.json_dict['Invariants'][invar]['Changed'] = 'True'
            if bound2 is not None:
                if not bound2.isdigit() and val != 'undt':
                    print bound2, 'is an invalid value for an integer invariant. Should be an integer or undt'
                    return
                if self.json_dict['Invariants'][invar]['Value']['Max'] != bound2:
                    self.json_dict['Invariants'][invar]['Value']['Max'] = bound2
                    self.json_dict['Invariants'][invar]['Changed'] = 'True'
        elif self.json_dict['Invariants'][invar]['Type'] == 'Real':
            if bound1 is not None:
                if not (bound1.replace('.', '1').isdigit() and bound1.count('.') <= 1):
                    print bound1, 'is an invalid value for an real invariant. Should be an real.'
                    return
                if self.json_dict['Invariants'][invar]['Value']['Min'] != bound1:
                    self.json_dict['Invariants'][invar]['Value']['Min'] = bound1
                    self.json_dict['Invariants'][invar]['Changed'] = 'True'
            if bound2 is not None:
                if not (bound2.replace('.', '1').isdigit() and bound2.count('.') <= 1) and val != 'undt':
                    print bound2, 'is an invalid value for an real invariant. Should be an decimal number or undt'
                    return
                if self.json_dict['Invariants'][invar]['Value']['Max'] != bound2:
                    self.json_dict['Invariants'][invar]['Value']['Max'] = bound2
                    self.json_dict['Invariants'][invar]['Changed'] = 'True'
        else:
            if val is None and val != 'True' and val != 'False' and val != 'undt':
                print val, 'is an invalid value for a boolean invariant. Should be True, False, or undt'
                return
            if self.json_dict['Invariants'][invar]['Value'] != val:
                self.json_dict['Invariants'][invar]['Value'] = val
                self.json_dict['Invariants'][invar]['Changed'] = 'True'

    def run(self):
        print 'INGRID 2.0\n'
        disp_dict(self.json_dict['Invariants'])
        while True:
            self.process_input(raw_input())


ui = IngridUI()
ui.run()



