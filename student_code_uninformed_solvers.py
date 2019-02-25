
from solver import *
import pdb

class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    '''def populate(self):
        # returns nothing, but populate the children of the current node; if no child, then do nothing
        movables = self.gm.getMovables()
        if movables:
            for movable in movables:
                self.gm.makeMove(movable)
                child_state = GameState(self.gm.getGameState(), self.currentState.depth + 1, movable)
                if not child_state in self.currentState.children:
                    self.currentState.children.append(child_state)
                    child_state.parent = self.currentState
                    self.gm.reverseMove(movable)


    def visit_child(self):
        # if the node has children
        if len(self.currentState.children) !=0:
            #if I have not visited all the child nodes
            if self.currentState.nextChildToVisit <len(self.currentState.children):
                child_to_visit = self.currentState.children[self.currentState.nextChildToVisit]
                self.currentState.nextChildToVisit += 1
                if child_to_visit.state == self.victoryCondition:
                    return True
                else:
                    self.currentState = child_to_visit
                    self.visited[child_to_visit] = True
            #when all of a node's children had been visited
            else:
                self.gm.reverseMove(self.currentState.requiredMovable)
                self.currentState = self.currentState.parent
        #if the node as no children
        else:
            if self.gm.getGameState()==self.victoryCondition:
                return True
            else:
                self.visited[self.currentState]=True
                self.gm.reverseMove(self.currentState.requiredMovable)
                self.currentState = self.currentState.parent'''






    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        #check if it satisfies the winning condtion at the beginning
        print(self.currentState.state)
        self.visited[self.currentState] = True
        if self.gm.getGameState() == self.victoryCondition:
            return True

        #populate the children nodes of the current node
        movables = self.gm.getMovables()
        if movables:
            for movable in movables:
                self.gm.makeMove(movable)
                child_state = GameState(self.gm.getGameState(), self.currentState.depth + 1, movable)
                if not child_state in self.currentState.children or self.visited[child_state] == False:
                    self.currentState.children.append(child_state)
                    child_state.parent = self.currentState
                    self.gm.reverseMove(movable)
        #visit each child
        if len(self.currentState.children) !=0:
            #if I have not visited all the child nodes
            if self.currentState.nextChildToVisit <len(self.currentState.children):
                child_to_visit = self.currentState.children[self.currentState.nextChildToVisit]
                self.currentState.nextChildToVisit += 1
                if child_to_visit.state == self.victoryCondition:
                    return True
                else:
                    self.visited[child_to_visit] = True
                    self.currentState = child_to_visit
            #when all of a node's children had been visited
            else:
                self.gm.reverseMove(self.currentState.requiredMovable)
                self.currentState = self.currentState.parent
        #if the node as no children
        else:
            if self.gm.getGameState()==self.victoryCondition:
                return True
            else:
                self.visited[self.currentState]=True
                self.gm.reverseMove(self.currentState.requiredMovable)
                self.currentState = self.currentState.parent

        return True






class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)



    def traverse(self):
        #recursive helper
        #if a node is running out of children, let the cursor go up, go to the siblings, go down,
        pass

    def populate(self):
        movables = self.gm.getMovables()
        if movables:
            for movable in movables:
                self.gm.makeMove(movable)
                child_state = GameState(self.gm.getGameState(), self.currentState.depth + 1, movable)
                self.gm.reverseMove(movable)
                self.currentState.children.append(child_state)
                child_state.parent = self.currentState

    def visit_child(self):

        pass

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here

        # check if it satisfies the winning condtion at the beginning
        if self.gm.getGameState() == self.victoryCondition:
            return True

        self.populate()






        return True
