
def automaton(s):
    state = 0
    nbMatch = 0

    for c in s:
        if c == 'a':
            if state == 0 or state == 1:
                state += 1
            # if state == 2: state = 2
        else: # c == 'b'
            if state == 2:
                nbMatch += 1
            state = 0
        print(c, "  state=", state)
    print(nbMatch)
