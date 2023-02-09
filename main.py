from DFAClass import DFA
from NFAClass import NFA

accept01dfa = DFA(
    states={'a', 'b', 'c', 'd'},
    input_symbols={'0', '1'},
    transitions={
        'a': {'0': 'b', '1': 'd'},
        'b': {'0': 'd', '1': 'c'},
        'c': {'0': 'd', '1': 'd'},
	    'd': {'0': 'd', '1': 'd'}
    },
    initial_state='a',
    final_states={'c'}
)
accept10dfa = DFA(
    states={'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q1': {'0': 'q4', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q4'},
        'q3': {'0': 'q4', '1': 'q4'},
	    'q4': {'0': 'q4', '1': 'q4'}
    },
    initial_state='q1',
    final_states={'q3'}
)
nulldfa = DFA(
    states={'qa', 'qb', 'qc', 'qd', 'qe'},
    input_symbols={'a', 'b'},
    transitions={
        'qa': {'a': 'qb', 'b': 'qd'},
        'qb': {'a': 'qc', 'b': 'qb'},
        'qc': {'a': 'qb', 'b': 'qd'},
	    'qd': {'a': 'qc', 'b': 'qd'},
	    'qe': {'a': 'qa', 'b': 'qd'}
    },
    initial_state='qa',
    final_states={'qe'}
)
finitedfa = DFA(
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
infinitedfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
dfaforminify = DFA(
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
#Main Function
# print(accept01dfa.IsAccept('01'))
# print(nulldfa.IsNull())
# print(infinitedfa.IsFinite())
# uniondfa = DFA.Union(accept01dfa,accept10dfa)
# newuniondfa = uniondfa.MinimizeDFA()
# print(newuniondfa.IsAccept('10'))

