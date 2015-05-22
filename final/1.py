
class B:
    def __init__(self,s,x,y,dx,dy):
        self.state = s
        self.search = "UCS"
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def Next(self):
    def UniformCostSearch(self,problem):
        """Search the node of least total cost first."""
        "*** YOUR CODE HERE ***"
        from util import PriorityQueueWithFunction
        from util import PriorityQueue

        #import inspect
        #print inspect.getmembers(problem, predicate=inspect.ismethod)
        exp = {}
        # exp=1...added to queue, 2...poped from queue
        st = PriorityQueue()
        re = []


        state = problem.getStartState()
        st.push( (state,[]), 0 )
        exp[state] = 1
        
        while st.isEmpty()==False:
            tmp = st.pop()
            state = tmp[0]
            move = tmp[1]
            #print problem.getCostOfActions(move)
            
            exp[state] = 2

            if problem.isGoalState(state)==True:
                re = move
                break

            adj = problem.getSuccessors(state)
            for it in adj:
                Nstate = it[0]
                Nmove = it[1]
                Ncheck = it[2]
                if ( Nstate in exp ) == False:
                    tmpMove = list(move)
                    tmpMove.append(Nmove)
                    st.push( (Nstate,tmpMove), problem.getCostOfActions(tmpMove) )
                    exp[Nstate] = 1
                elif exp[Nstate]==1:
                    pass
                elif exp[Nstate]==2:
                    pass
        else:
            print "No route found"
            return []

        return re


class State:
    def __init__(self):
        self.e = [[0 for x in range(20)] for x in range(20)]
    

class A:
    "*state = State()*"
    def __init__(self,s):
        "*A.state = s*"
        self.i = 4
    def P(self):
        print self
    def Set(self,s):
        A.state = s
 

state = State()
m = A(state)
m2 = A(state)
m.Set(state)

state.e[0][2] = 3

print m2.state.e[0][2]
print m.state.e[0][2]
print state.e[0][2]















