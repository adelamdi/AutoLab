from DFAClass import *
class NFA:
    states = ()
    input_symbols={}
    transitions={}
    initial_state= ''
    final_states={}
    def __init__(self,states,input_symbols,transitions,initial_state,final_states) -> None:
        self.states = tuple(states)
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

            
    
    def ToDFA(self):
        #Convert NFA to DFA

        dfastates = []
        dfatransition = {}
        dfafinal = {}
        #dfatransition.update({self.initial_state:self.transitions[self.initial_state]})
        dfastates.append([self.initial_state])
        while True:
            shouldbreak=False
            isChanged = False
            for dfastate in dfastates:
                print('dfastate:' + str(dfastate))
                if shouldbreak:
                    break
                dfanamestr = ''
                for y in dfastate:
                    dfanamestr += y
                if not(dfanamestr in (dfatransition.keys())):
                    print('there is no transition for ' + str(dfastate))
                    #DFA State is a state that is in dfastates but dont have transition
                    #Lets Create Transition for dfastate based on nfa transition table
                    transitionline = {}
                    for alpha in self.input_symbols:
                        goeswiththisalpha = []
                        if len(dfastate)<3:
                            for eachstate in dfastate:
                                x = self.transitions.get(eachstate).get(alpha)
                                goeswiththisalpha.append(x)
                                if not(x in dfastates):
                                    print('new state: '+ str(x))
                                    dfastates.append(x)
                                    print('dfastates: '+ str(dfastates))
                            transitionline.update({alpha:x})
                        else:

                            x = self.transitions.get(dfastate).get(alpha)

                            goeswiththisalpha.append(x)
                            if not(x in dfastates):
                                print('new state: '+ str(x))
                                dfastates.append(x)
                                print('dfastates: '+ str(dfastates))
                            transitionline.update({alpha:x})

                    print('TransitionLine: ' + str(transitionline))
                    print('dfastates: ' + str(dfastates))
                    right = ''
                    for j in dfastate:
                        right+=j
                    print('right: '+right)
                    dfatransition.update({right:transitionline})
                    isChanged=True
                    shouldbreak=True
                    break
            print(dfatransition)
            if isChanged==False:
                break






                        