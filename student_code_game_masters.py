from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### student code goes here
        peg_1_bindings = self.kb.kb_ask(parse_input('fact: (on ?disk peg1)'))
        peg_1_list = []
        if peg_1_bindings:
            for binding in peg_1_bindings:
                peg_1_list.append(binding.bindings_dict['?disk'])
        for i in range(0,len(peg_1_list)):
            peg_1_list[i] = peg_1_list[i][4]
        for i in range(0, len(peg_1_list)):
            peg_1_list[i] = int(peg_1_list[i])
        peg_1_list.sort()
        peg_1 = tuple(peg_1_list)

        peg_2_bindings = self.kb.kb_ask(parse_input('fact: (on ?disk peg2)'))
        peg_2_list = []
        if peg_2_bindings:
            for binding in peg_2_bindings:
                peg_2_list.append(binding.bindings_dict['?disk'])
        for i in range(0, len(peg_2_list)):
            peg_2_list[i] = peg_2_list[i][4]
        for i in range(0, len(peg_2_list)):
            peg_2_list[i] = int(peg_2_list[i])
        peg_2_list.sort()
        peg_2 = tuple(peg_2_list)

        peg_3_bindings = self.kb.kb_ask(parse_input('fact: (on ?disk peg3)'))
        peg_3_list = []
        if peg_3_bindings:
            for binding in peg_3_bindings:
                peg_3_list.append(binding.bindings_dict['?disk'])
        for i in range(0,len(peg_3_list)):
            peg_3_list[i] = peg_3_list[i][4]
        for i in range(0, len(peg_3_list)):
            peg_3_list[i] = int(peg_3_list[i])
        peg_3_list.sort()
        peg_3 = tuple(peg_3_list)

        game_state = (peg_1, peg_2, peg_3)
        return game_state
        pass


    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        movable_terms = movable_statement.terms
        disk = movable_terms[0]
        origin = movable_terms[1]
        target = movable_terms[2]


        new_on_fact_to_add = parse_input(str('fact: (on ' + str(disk) + ' ' + str(target) + ')'))
        new_top_fact_to_add = parse_input(str('fact: (ontop ' + str(disk) + ' ' + str(target) + ')'))
        old_on_fact_to_retract = parse_input(str('fact: (on ' + str(disk) + ' ' + str(origin) + ')'))
        old_top_fact_to_retract = parse_input(str('fact: (ontop ' + str(disk) + ' ' + str(origin) + ')'))

        self.kb.kb_retract(old_on_fact_to_retract)
        self.kb.kb_retract(old_top_fact_to_retract)
        self.kb.kb_assert(new_on_fact_to_add)
        self.kb.kb_assert(new_top_fact_to_add)

        old_empty_bindings = self.kb.kb_ask(parse_input('fact: (on ?disk ' + str(target) + ')'))
        if old_empty_bindings:
            old_empty_fact_to_retract = parse_input(str('fact: (empty ' + str(target) + ')'))
            self.kb.kb_retract(old_empty_fact_to_retract)

        origin_bindings =self.kb.kb_ask(parse_input('fact: (on ?disk ' + str(origin) + ')'))
        if not origin_bindings:
            new_empty_fact_to_add = parse_input(str('fact: (empty ' + str(origin) + ')'))
            self.kb.kb_assert(new_empty_fact_to_add)
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here


        Y_1_bindings = self.kb.kb_ask(parse_input('fact: (Ypos ?tile pos1)'))
        Y_2_bindings = self.kb.kb_ask(parse_input('fact: (Ypos ?tile pos2)'))
        Y_3_bindings = self.kb.kb_ask(parse_input('fact: (Ypos ?tile pos3)'))
        X_1_bindings = self.kb.kb_ask(parse_input('fact: (Xpos ?tile pos1)'))
        X_2_bindings = self.kb.kb_ask(parse_input('fact: (Xpos ?tile pos2)'))
        X_3_bindings = self.kb.kb_ask(parse_input('fact: (Xpos ?tile pos3)'))

        Y_1_list = [0,0,0]
        Y_2_list = [0,0,0]
        Y_3_list = [0,0,0]

        Y_1_bindings_list = []
        Y_2_bindings_list = []
        Y_3_bindings_list = []
        X_1_bindings_list = []
        X_2_bindings_list = []
        X_3_bindings_list = []
        for y_1_binding in Y_1_bindings:
            Y_1_bindings_list.append(y_1_binding.bindings_dict['?tile'])
        for y_2_binding in Y_2_bindings:
            Y_2_bindings_list.append(y_2_binding.bindings_dict['?tile'])
        for y_3_binding in Y_3_bindings:
            Y_3_bindings_list.append(y_3_binding.bindings_dict['?tile'])
        for x_1_binding in X_1_bindings:
            X_1_bindings_list.append(x_1_binding.bindings_dict['?tile'])
        for x_2_binding in X_2_bindings:
            X_2_bindings_list.append(x_2_binding.bindings_dict['?tile'])
        for x_3_binding in X_3_bindings:
            X_3_bindings_list.append(x_3_binding.bindings_dict['?tile'])
        for y in Y_1_bindings_list:
            if y in X_1_bindings_list:
                Y_1_list[0] = y
            if y in X_2_bindings_list:
                Y_1_list[1] = y
            if y in X_3_bindings_list:
                Y_1_list[2] = y

        for y_1_binding in Y_1_bindings:
            Y_1_bindings_list.append(y_1_binding.bindings_dict['?tile'])
        for y_2_binding in Y_2_bindings:
            Y_2_bindings_list.append(y_2_binding.bindings_dict['?tile'])
        for y_3_binding in Y_3_bindings:
            Y_3_bindings_list.append(y_3_binding.bindings_dict['?tile'])
        for x_1_binding in X_1_bindings:
            X_1_bindings_list.append(x_1_binding.bindings_dict['?tile'])
        for x_2_binding in X_2_bindings:
            X_2_bindings_list.append(x_2_binding.bindings_dict['?tile'])
        for x_3_binding in X_3_bindings:
            X_3_bindings_list.append(x_3_binding.bindings_dict['?tile'])

        for y in Y_1_bindings_list:
            if y in X_1_bindings_list:
                Y_1_list[0] = y
            if y in X_2_bindings_list:
                Y_1_list[1] = y
            if y in X_3_bindings_list:
                Y_1_list[2] = y
        for i in range(0,len(Y_1_list)):
            if Y_1_list[i][-1] != 'y':
                Y_1_list[i] = Y_1_list[i][-1]
            else:
                Y_1_list[i] = '-1'
        for i in range(0, len(Y_1_list)):
            Y_1_list[i] = int(Y_1_list[i])
        Y_1 = tuple(Y_1_list)

        for y in Y_2_bindings_list:
            if y in X_1_bindings_list:
                Y_2_list[0] = y
            if y in X_2_bindings_list:
                Y_2_list[1] = y
            if y in X_3_bindings_list:
                Y_2_list[2] = y
        for i in range(0, len(Y_2_list)):
            if Y_2_list[i][-1] != 'y':
                Y_2_list[i] = Y_2_list[i][-1]
            else:
                Y_2_list[i] = '-1'
        for i in range(0, len(Y_2_list)):
            Y_2_list[i] = int(Y_2_list[i])
        Y_2 = tuple(Y_2_list)

        for y in Y_3_bindings_list:
            if y in X_1_bindings_list:
                Y_3_list[0] = y
            if y in X_2_bindings_list:
                Y_3_list[1] = y
            if y in X_3_bindings_list:
                Y_3_list[2] = y
        for i in range(0, len(Y_3_list)):
            if Y_3_list[i][-1] != 'y':
                Y_3_list[i] = Y_3_list[i][-1]
            else:
                Y_3_list[i] = '-1'
        for i in range(0, len(Y_3_list)):
            Y_3_list[i] = int(Y_3_list[i])
        Y_3 = tuple(Y_3_list)

        game_state = (Y_1, Y_2, Y_3)


        return game_state
        pass

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        movable_terms = movable_statement.terms
        tile = movable_terms[0]
        sourcex = movable_terms[1]
        sourcey = movable_terms[2]
        targetx = movable_terms[3]
        targety = movable_terms[4]
        new_xpos_fact_statement = str('fact: (Xpos '+ str(tile)+ ' '+ str(targetx) +')')
        new_ypos_fact_statement = str('fact: (Ypos '+ str(tile)+ ' '+ str(targety) +')')
        new_empty_xpos_statement = str('fact: (Xpos empty '+ str(sourcex) +')')
        new_empty_ypos_statement = str('fact: (Ypos empty '+ str(sourcey) +')')
        old_xpos_fact_statement = str('fact: (Xpos '+ str(tile)+ ' '+ str(sourcex) +')')
        old_ypos_fact_statement = str('fact: (Ypos '+ str(tile)+ ' '+ str(sourcey) +')')
        old_empty_xpos_statement = str('fact: (Xpos empty '+ str(targetx) +')')
        old_empty_ypos_statement = str('fact: (Ypos empty '+ str(targety) +')')


        new_xpos_fact_to_add = parse_input(new_xpos_fact_statement)
        new_ypos_fact_to_add = parse_input(new_ypos_fact_statement)
        new_empty_xpos_to_add = parse_input(new_empty_xpos_statement)
        new_empty_ypos_to_add = parse_input(new_empty_ypos_statement)
        old_xpos_fact_to_retract = parse_input(old_xpos_fact_statement)
        old_ypos_fact_to_retract = parse_input(old_ypos_fact_statement)
        old_empty_xpos_to_retract = parse_input(old_empty_xpos_statement)
        old_empty_ypos_to_retract = parse_input(old_empty_ypos_statement)

        self.kb.kb_retract(old_xpos_fact_to_retract)
        self.kb.kb_retract(old_ypos_fact_to_retract)
        self.kb.kb_retract(old_empty_xpos_to_retract)
        self.kb.kb_retract(old_empty_ypos_to_retract)
        self.kb.kb_assert(new_xpos_fact_to_add)
        self.kb.kb_assert(new_ypos_fact_to_add)
        self.kb.kb_assert(new_empty_xpos_to_add)
        self.kb.kb_assert(new_empty_ypos_to_add)


        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
