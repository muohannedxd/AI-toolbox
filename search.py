
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Stack()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Queue()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    #((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                priority = prevCost + cost
                pQueue.push((nextNode, newAction, priority),priority)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    #((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                newCostToNode = prevCost + cost
                heuristicCost = newCostToNode + heuristic(nextNode,problem)
                pQueue.push((nextNode, newAction, newCostToNode),heuristicCost)

    util.raiseNotDefined()


def dls(problem, board, limit, verbose=False):
    #print("\n---------------------------------------\n")
    #print(f"Running DFS with\nState: {problem.state}\nGoal State: {problem.goal}\nLimit: {limit}...")
    
    start = time.perf_counter()
    
    frontier = [problem]
    frontier_size = len(frontier)
    gen_nodes = 0
    explored = set()
    mapp = {}
     
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        
        return Result(problem, "success", frontier_size, problem.depth, gen_nodes, end_prem - start)
    
    while frontier:
        node = frontier.pop()
        #print(len(frontier))
        #print(f"{node.state}")
        if node.depth <= limit:
            
            if node.str_state not in explored:
                explored.add(node.str_state)
                mapp[node.str_state] = node
                
                if node.str_state == node.goal_str:
                    end_final = time.perf_counter()
                    return Result(node, "success", frontier_size, node.depth, gen_nodes, end_final - start)
                
                children = reversed(make_child_node(node, node.goal, board))
                for child in children:
                    gen_nodes = gen_nodes + 1
                    frontier.append(child)
                if len(frontier) > frontier_size:
                    frontier_size = len(frontier)
            
            elif node.str_state in mapp and node.path_cost < mapp[node.str_state].path_cost:
                explored.remove(node.str_state)
                frontier.append(node)
                mapp[node.str_state] = node
                
    end_failed = time.perf_counter()    
    return Result(None, "failed", frontier_size, limit, gen_nodes, end_failed - start)

def bi_directional_search(self, start, goal):
        found, fringe1, visited1, came_from1 = False, deque([start]), set([start]), {start: None}
        meet, fringe2, visited2, came_from2 = None, deque([goal]), set([goal]), {goal: None}
        while not found and (len(fringe1) or len(fringe2)):
            print('FringeStart: {:30s} | FringeGoal: {}'.format(str(fringe1), str(fringe2)))
            if len(fringe1):
                current1 = fringe1.pop()
                if current1 in visited2: meet = current1; found = True; break
                for node in self.neighbors(current1):
                    if node not in visited1: visited1.add(node); fringe1.appendleft(node); came_from1[node] = current1
            if len(fringe2):
                current2 = fringe2.pop()
                if current2 in visited1: meet = current2; found = True; break
                for node in self.neighbors(current2):
                    if node not in visited2: visited2.add(node); fringe2.appendleft(node); came_from2[node] = current2
        if found: print(); return came_from1, came_from2, meet
        else: print('No path between {} and {}'.format(start, goal)); return None, None, Non

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch