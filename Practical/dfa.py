class DFA:
    def __init__(self):
        # Set of all states
        self.states = {'q0', 'q1'}

        # Set of alphabet symbols
        self.alphabet = {'a', 'b'}

        # Transition function
        self.transition = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q0', 'b': 'q1'}
        }

        # Initial state
        self.initial_state = 'q0'

        # Set of accept states
        self.final_states = {'q1'}

    # end of constructor
    
    def ends_with_b(self, state, input_string):
        # Base case: if the input string is empty
        if not input_string:
            return state in self.final_states
        
        # Get the current symbol
        symbol = input_string[0]
        
        # Check if the symbol is valid
        if symbol not in self.alphabet:
            raise ValueError("Symbol "+symbol+" not in the alphabet.")
        
        # Get the next state based on the current symbol
        next_state = self.transition[state][symbol]
        
        # Recursively process the rest of the string
        return self.ends_with_b(next_state, input_string[1:])
    
    # end of ends_with_b

    def process_string(self, input_string):
        if self.ends_with_b(self.initial_state, input_string):
            return "Accepted"
        else:
            return "Rejected"
    
    # end of process_string


# __main__
dfa = DFA()
test_strings = ["", "a", "b", "ab", "ba", "aab", "bba", "aaa"]

for s in test_strings:
    result = dfa.process_string(s)
    print("String "+s+" is "+result)

