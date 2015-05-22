# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

# ---- import ----
from util import pause
from util import PriorityQueue
from util import Queue
# ---- end -------

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """
    


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        
        "Add more of your code here if you want to"

        #pause()
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """

        
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newGhostPos = successorGameState.getGhostPositions()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        ghostScoreMethod = 2
        if ghostScoreMethod==1:
            Dist = [ manhattanDistance(newPos, it ) for it in newGhostPos ]
            ghostScore = sum( [ dis-2 for dis in Dist if dis <= 2 ] )
            ghostScore = ghostScore * 100
        if ghostScoreMethod==2:
            Dist = [ manhattanDistance(newPos, it ) for it in newGhostPos ]
            ghostScore = sum( [ -100/dis if dis!=0 else -10000 for dis in Dist ] )
            ghostScore = ghostScore * 0.1


        foodScoreMethod = 1
        if foodScoreMethod==1:
            if currentGameState.getNumFood() > successorGameState.getNumFood():
                foodScore = 0
            else:
                foodScore = -self.searchDistanceToNearestFood(successorGameState)

        score = foodScore + ghostScore

            
##        print "----New state----"
##        print newPos
##        print self.distanceToNearestFood(successorGameState)
##        print self.searchDistanceToNearestFood(successorGameState)
##        print newGhostPos
##        print "score =",score
##        #print newScaredTimes
##        #return successorGameState.getScore()

        return score

    def listFoodPos(self, currentGameState):
        newFood = currentGameState.getFood()
        width = currentGameState.data.layout.width
        height = currentGameState.data.layout.height
        
        foodPos = [ (x,y) for x in range(0,width) for y in range(0,height) if newFood[x][y]==True ]
        #print foodPos
        
        return foodPos
    def distanceToNearestFood(self, currentGameState):
        PacmanPos = currentGameState.getPacmanPosition()
        foodPos = self.listFoodPos(currentGameState)
        foodDis = [ manhattanDistance(it,PacmanPos) for it in foodPos ]

        
        if len(foodDis)!=0:
            return min(foodDis)
        else:
            return None
    def searchDistanceToNearestFood(self, currentGameState):
        PacmanPos = currentGameState.getPacmanPosition()
        newFood = currentGameState.getFood()
        foodPos = self.listFoodPos(currentGameState)

        exp = {}
        st = Queue()

        st.push( (PacmanPos,0) )
        exp[PacmanPos] = 1

        while st.isEmpty()==False:
            tmp = st.pop()
            x = tmp[0][0]
            y = tmp[0][1]
            cost = tmp[1]
            if exp[(x,y)]==2:
                continue
            exp[(x,y)] = 2

            if newFood[x][y] == True:
                return cost

            fixadj = [(0,1),(0,-1),(1,0),(-1,0)]
            adj = [ (x+dx,y+dy) for (dx,dy) in fixadj if currentGameState.hasWall(x+dx,y+dy)==False ]
            for (x,y) in adj:
                if ((x,y) in exp)==False:
                    st.push( ((x,y),cost+1) )
                    exp[(x,y)]=1
                elif exp[(x,y)]==1:
                    pass
                elif exp[(x,y)]==2:
                    pass
        else:
            print "No route found"
            return 9999
        
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    def minimax_decision(self,state,agent,depth):
        if agent==state.getNumAgents():
            agent=0
        if state.isLose() or state.isWin():
            return self.evaluationFunction(state)
        if depth==self.depth*state.getNumAgents():
            return self.evaluationFunction(state)
        if agent==0:
            return self.maxV(state,agent,depth)
        elif agent < state.getNumAgents():
            return self.minV(state,agent,depth)
        else:
            print "Error in minimax_decision: agent index"
            return 0
    def maxV(self,state,agent,depth):
        #print state.getLegalActions(agent)
        posibleV = [ self.minimax_decision(state.generateSuccessor(agent,act),agent+1,depth+1) for act in state.getLegalActions(agent) ]
        return max( posibleV if len(posibleV)!=0 else [+9999] )
        
    def minV(self,state,agent,depth):
        #print state.getLegalActions(agent)
        posibleV = [ self.minimax_decision(state.generateSuccessor(agent,act),agent+1,depth+1) for act in state.getLegalActions(agent) ]
        return min( posibleV if len(posibleV)!=0 else [-9999] )
        
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        Dic = {self.minimax_decision(gameState.generateSuccessor(0,act),1,1):act for act in gameState.getLegalActions(0)}
        return Dic[max(Dic)]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    
    def minimax_decision(self,state,agent,depth,a,b):
        if agent==state.getNumAgents():
            agent=0
        if state.isLose() or state.isWin():
            return self.evaluationFunction(state)
        if depth==self.depth*state.getNumAgents():
            return self.evaluationFunction(state)
        if agent==0:
            return self.maxV(state,agent,depth,a,b)
        elif agent < state.getNumAgents():
            return self.minV(state,agent,depth,a,b)
        else:
            print "Error in minimax_decision: agent index"
            return 0
    def maxV(self,state,agent,depth,a,b):
        v = -9999
        for act in state.getLegalActions(agent):
            v = max( v, self.minimax_decision(state.generateSuccessor(agent,act),agent+1,depth+1,a,b ))
            if v>=b:
                return v
            a = max(a,v)
        return (v if len(state.getLegalActions(agent))!=0 else [+9999])

    def minV(self,state,agent,depth,a,b):
        v = +9999
        for act in state.getLegalActions(agent):
            v = min( v, self.minimax_decision(state.generateSuccessor(agent,act),agent+1,depth+1,a,b ))
            if v<=a:    # shouldn't use <=, but it's okay here since pruning is acceptable if score is the same
                return v
            b = min(b,v)
        return (v if len(state.getLegalActions(agent))!=0 else [-9999])
        
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        a = -9999
        b = +9999
        v = -9999
        av = None
        for act in gameState.getLegalActions(0):
            v = max( v, self.minimax_decision(gameState.generateSuccessor(0,act),1,1,a,b ) )
            if v>a:
                a=v
                av=act
        return av

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
