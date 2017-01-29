#!/usr/bin/env python2

import mystic.symbolic as ms
import sys
import json

## STDINa>
# <python style list of symbols>
# <symbol to solve for>
# equation to solve

#var = list('GPEN')
#
#equations = '''
#G <= P**2.0+4.0*(E/2.0-P)**(2.0)
#'''

inputstuff = json.loads(sys.stdin.readline())

var = inputstuff['invariants']
target = inputstuff['target_invariant']
equation = inputstuff['inequality']

ineqn = ms.simplify(equation, variables=var, target=target)

result = {}
result['solved_inequality'] = ineqn

# print (json.dumps(result))
print (ineqn + ";")
