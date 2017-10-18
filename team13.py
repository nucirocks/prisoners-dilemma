####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'This game is bull' # Only 10 chars displayed.
strategy_name = 'Tit-for-tat'
strategy_description = 'The strategy starts with picking collude and then copying the history of the opponent'
    
def move(my_history, their_history, my_score, their_score):
    class TitForTat(Player):
        
        def strategy(self, opponent):
            try:
                return opponent.history[-1]
            except IndexError:
               return 'C'
            else:
               return 'D'

    def __repr__(self):
        return 'Tit For Tat'
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

'''