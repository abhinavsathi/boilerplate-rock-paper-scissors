# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)
        if len(my_history) > 0:
            my_history.append(my_history[-1])

    if len(opponent_history) < 20:
        return "R"

    #Kris Strategy
    if len(my_history) > 0 and prev_play == counter(my_history[-1]):
        return counter(counter(my_history[-1]))

    #Rest of Bots Strategy
    patterns = {}
    n = 4  
    if len(opponent_history) > n:
        for i in range(len(opponent_history) - n):
            key = tuple(opponent_history[i:i+n])
            if key not in patterns:
                patterns[key] = []
            patterns[key].append(opponent_history[i+n])

        last_moves = tuple(opponent_history[-n:])
        if last_moves in patterns:
            predicted_move = max(set(patterns[last_moves]), key=patterns[last_moves].count)
            return counter(predicted_move)

    return "P"

def counter(move):
    if move == "R":
        return "P"
    if move == "P":
        return "S"
    if move == "S":
        return "R"