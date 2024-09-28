
# Result
def result(p1_play, p2_play, results):
    if p1_play == p2_play:
        results["tie"] += 1

    elif (p1_play == "P" and p2_play == "R") or (
            p1_play == "R" and p2_play == "S") or (p1_play == "S" and p2_play == "P"):
        results["p1"] += 1

    elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
        results["p2"] += 1

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100
    results['win'] = win_rate

    return results


# quincy_test
def quincy_test(prev_play, counter_test=[0]):

    counter_test[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter_test[0] % len(choices)]

# kris_test
def kris_test(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]

# murgesh_test
def mrugesh_test(opponent_history):
  
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]

# abbey_test
def abbey_test(prev_opponent_play, opponent_history, play_order):
    
    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [prev_opponent_play + "R", prev_opponent_play + "P", prev_opponent_play + "S",]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}


    return ideal_response[prediction]
