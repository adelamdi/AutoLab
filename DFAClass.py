import networkx as nx
from collections import defaultdict, deque
class DFA:
    states = {}
    input_symbols={}
    transitions={}
    initial_state= ''
    final_states={}

    def __init__(self,states,input_symbols,transitions,initial_state,final_states) -> None:
        # Initialize DFA
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states
        #object.__setattr__(self, '_count_cache', [])
    
    def IsAccept(self,Text):
        # Return True if DFA was at final state when we finish reading text
        current = self.initial_state
        for c in Text:
            current = self.transitions.get(current).get(c)
        if current in self.final_states :
            print('Accept')
        else:
            print('Not Accept')

    def IsNull(self):
        #Return True if there is a final state in reachable states from initial state
        Reachables = []
        States = []
        Reachables.append(self.initial_state)
        States.append(self.initial_state)
        CheckNull = True
        while(len(States)>0):
            state = States.pop(0)
            for next_state in self.transitions[state].values():
                if not(next_state in Reachables):
                    if next_state in self.final_states:
                        CheckNull=False
                    Reachables.append(next_state)
                    States.append(next_state)
        return CheckNull

    def ToGraph(self):
        #Convert DFA to NetworkX Graph
        return nx.DiGraph([
            (start_state, end_state)
            for start_state, transition in self.transitions.items()
            for end_state in transition.values()
        ])

    def IsFinite(self):
        # Return True if There is a longest path available in converted graph
        # Return True (Finite) if DFA is Null
        if self.IsNull():
            return True

        graph = self.ToGraph()
        # Calculate all reachable nodes from initial state
        Reachables = nx.descendants(graph, self.initial_state) 

        # Calculate all nodes that have a path to 1 or more final states 
        NeededNodes = self.final_states.union(*(
            nx.ancestors(graph, state)
            for state in self.final_states
        ))
        GoodNodes = Reachables.intersection(NeededNodes)
        #Create Good SubGraph
        subgraph = graph.subgraph(GoodNodes)
        try:
            #Finite Language
            Longest =  nx.dag_longest_path_length(subgraph)
            return True
        except nx.exception.NetworkXUnfeasible:
            #Infinite Language
            return False
    def MaximumWordLength(self):
        #Return MaximumWordLength Accepted 
        # If DFA Language is Null, The Answer is 0
        if self.IsNull():
            return 0
        # if DFA is Infinite we cant calculate maximumwordlength
        if self.IsFinite():

            graph = self.ToGraph()

            Reachables = nx.descendants(graph, self.initial_state)

            NeededNodes = self.final_states.union(*(
                nx.ancestors(graph, state)
                for state in self.final_states
            ))

            GoodNodes = Reachables.intersection(NeededNodes)
            subgraph = graph.subgraph(GoodNodes)
            return nx.dag_longest_path_length(subgraph)
        else:
            return "Infinite Language"


    def MinimumWordLength(self):
        # Return MinimumWordLength Accepted, start from initial state and search with length 1, then increase length
        queue = deque()
        #Distances: Dictionary for storing states with them length
        distances = defaultdict(lambda: None)
        distances[self.initial_state] = 0
        queue.append(self.initial_state)
        while queue:
            state = queue.popleft()
            # Breaking Condition, We Reach final state and return length of path to reaching this state which is final
            if state in self.final_states:
                return distances[state]
            for next_state in self.transitions[state].values():
                if distances[next_state] is None:
                    distances[next_state] = distances[state] + 1
                    queue.append(next_state)
     
    def Complement(self):
        #Reverse Final and Normal States
        NewFinalStates = []
        for State in self.states:
            if not(State in self.final_states):
                NewFinalStates.append(State)
        
        newDFA = DFA(
            states=self.states,
            input_symbols=self.input_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            final_states=NewFinalStates
        )
        return newDFA
    def Union(self,OtherDFA):
        newStates = []
        newTransition = {}
        newFinalStates = []
        newInitialState = ''
        for fstate in self.states:
            for sstate in OtherDFA.states:
                #Create new state name
                newstate = fstate + sstate
                newStates.append(newstate)
                #New Final State
                if fstate in self.final_states or sstate in OtherDFA.final_states:
                    newFinalStates.append(fstate+sstate)
                #New Initial State
                if fstate == self.initial_state and sstate == OtherDFA.initial_state:
                    newInitialState = fstate+sstate
                #New Transition
                dest = {}
                for alpha in self.input_symbols:
                    #New Dictionary for Destinations
                    fgoesto = self.transitions.get(fstate).get(alpha)
                    sgoesto = OtherDFA.transitions.get(sstate).get(alpha)
                    dest.update({alpha:fstate+sstate})
                newTransition.update({fstate+sstate:dest})
        #Create new DFA and return it
        dfas = DFA(
        states=newStates,
        input_symbols=self.input_symbols,
        transitions=newTransition,
        initial_state=newInitialState,
        final_states=newFinalStates
        )
        return dfas

    def Intersection(self,OtherDFA):

        newStates = []
        newTransition = {}
        newFinalStates = []
        newInitialState = ''
        for fstate in self.states:
            for sstate in OtherDFA.states:
                #Create new state name
                newstate = fstate + sstate
                newStates.append(newstate)
                #New Final State
                if fstate in self.final_states and sstate in OtherDFA.final_states:
                    newFinalStates.append(fstate+sstate)
                #New Initial State
                if fstate == self.initial_state and sstate == OtherDFA.initial_state:
                    newInitialState = fstate+sstate
                #New Transition
                dest = {}
                for alpha in self.input_symbols:
                    #New Dictionary for Destinations
                    fgoesto = self.transitions.get(fstate).get(alpha)
                    sgoesto = OtherDFA.transitions.get(sstate).get(alpha)
                    dest.update({alpha:fstate+sstate})
                newTransition.update({fstate+sstate:dest})
        #Create new DFA and return it   
        dfas = DFA(
        states=newStates,
        input_symbols=self.input_symbols,
        transitions=newTransition,
        initial_state=newInitialState,
        final_states=newFinalStates
        )
        return dfas
