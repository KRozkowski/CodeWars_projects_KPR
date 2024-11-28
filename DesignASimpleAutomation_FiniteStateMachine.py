class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        Q = ["0","1"]
        Q1 = []
        for i in range(len(commands)):
            if commands[i] in Q:
                Q1.append(commands[i])
            else:
                continue
        q = "q1"
        for i in range(len(Q1)):
            if q == "q1" and Q1[i] == "1":
                q = "q2"
            elif q == "q2" and Q1[i] == "0":
                q = "q3"
            elif q == "q2" and Q1[i] == "1":
                q = "q2"
            elif q == "q3" and Q1[i] == "0":
                q = "q2"
            elif q == "q3" and Q1[i] == "1":
                q = "q3"


        if q == "q2":
            return True
        else:
            return False

my_automaton = Automaton()
