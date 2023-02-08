from DFAClass import DFA
#from NFAClass import NFA
# dfa = DFA(
#     states={'q0', 'q1', 'q2'},
#     input_symbols={'0', '1'},
#     transitions={
#         'q0': {'0': 'q0', '1': 'q1'},
#         'q1': {'0': 'q0', '1': 'q2'},
#         'q2': {'0': 'q2', '1': 'q1'}
#     },
#     initial_state='q0',
#     final_states={'q1'}
# )

# dfa = DFA(
#     states={'q0', 'q1', 'q2', 'q3', 'q4'},
#     input_symbols={'0', '1'},
#     transitions={
#         'q0': {'0': 'q1', '1': 'q2'},
#         'q1': {'0': 'q2', '1': 'q1'},
#         'q2': {'0': 'q3', '1': 'q2'},
# 	    'q3': {'0': 'q3', '1': 'q4'},
# 	    'q4': {'0': 'q2', '1': 'q1'},
#         'q5': {'0': 'q2', '1': 'q1'}
#     },
#     initial_state='q0',
#     final_states={'q4'}
# )

dfa3 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q3'},
        'q1': {'0': 'q2', '1': 'q4'},
        'q2': {'0': 'q1', '1': 'q4'},
	    'q3': {'0': 'q2', '1': 'q4'},
	    'q4': {'0': 'q4', '1': 'q4'}
    },
    initial_state='q0',
    final_states={'q4'}
)
dfa4 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q1'}
)
dfa = DFA(
    states={'qa', 'qb', 'qc', 'qd', 'qe'},
    input_symbols={'0', '1'},
    transitions={
        'qa': {'0': 'qb', '1': 'qd'},
        'qb': {'0': 'qc', '1': 'qe'},
        'qc': {'0': 'qb', '1': 'qe'},
	    'qd': {'0': 'qc', '1': 'qe'},
	    'qe': {'0': 'qe', '1': 'qe'}
    },
    initial_state='qa',
    final_states={'qe'}
)
