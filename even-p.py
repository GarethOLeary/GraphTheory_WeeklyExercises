class State:
    """A state in an automation."""
    def __init__(self, accept, arrows):
        #True if this is an accept state.
        self.accept = accept
        # Arrows (keys are labels) out of state.
        self.arrows = arrows

class DFA:
    """An automation"""
    def __init__(self, start):   
        # Start state of the automation
        self.start = start

    def match(self, s):
        """See if s is accepted by the automaton"""
        #current state
        current = self.start
        # loop through the characters in s.
        for c in s:
            # find the state in arrows with key c
            current = current.arrows[c]
        # return whether we're in an accept state
        return current.accept


def compile():
    """Create the automation."""

    # Create the start state.
    start = State(True, {})
    # Create the other state 
    other = State(False, {})

    # The states point to themselves on a 0
    start.arrows['0'] = start
    other.arrows['0'] = other

    # The states point to themselves on a 1
    start.arrows['1'] = other
    other.arrows['1'] = start

    # Create an automation.
    parity = DFA(start)

    # return automation
    return parity

# create automation instance
myautomaton = compile()
# a few small tests
for s in ['1100', '11111', '', '1', '0']:
    # check if s is accepted by the automaton
    result = myautomaton.match(s)
    # print the result
    print(f"{s} -> {result}")

for s in ['000', '001', '010', '011', '100', '101', '110', '111']:
    # check if s is accepted by the automaton
    result = myautomaton.match(s)
    # print the result
    print(f"{s} -> {result}")

