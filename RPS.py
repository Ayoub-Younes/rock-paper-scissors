
import copy
from Play import quincy_test, kris_test, mrugesh_test, abbey_test, result

#players Setup
r = {'o_history':[''], 'p_history':[''], 'results':{"p1": 0, "p2": 0, "tie": 0, 'win':0}}
play_order=[{"RR": 0,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0}]
quincy_record = copy.deepcopy(r)
kris_record = copy.deepcopy(r)
mrugesh_record = copy.deepcopy(r)
abbey_record = {**copy.deepcopy(r),**{'play_order':play_order}}
abbey_record['p_history'][0] = "R"
record = {'quincy':copy.deepcopy(r),'kris':copy.deepcopy(r),'abbey':copy.deepcopy(abbey_record),'mrugesh':copy.deepcopy(r)}

#Player Strategies
def player(prev_play, record = record, num_games = [0]):

    #Reset records
    if num_games[0] == 1000:
        record['quincy'] =  copy.deepcopy(r)
        record['abbey'] = copy.deepcopy(abbey_record)
        record['kris'] = copy.deepcopy(r)
        record['mrugesh'] = copy.deepcopy(r)
        num_games[0] = 0


    #ideal_response
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    #Players plays prediction
    quincy_play= quincy_test(record['quincy']['p_history'][-1])
    kris_play= kris_test(record['kris']['p_history'][-1])
    mrugesh_play = mrugesh_test(record['mrugesh']['p_history'])
    abbey_play = abbey_test(record['abbey']['p_history'][-1],record['abbey']['p_history'],record['abbey']['play_order'])


    #Counter players plays if winning rate is below 61% for each player to achieve final 60% win rate for all opponents

    guess = ideal_response[abbey_play]
    if record['quincy']['results']['win'] < 61:
        guess = ideal_response[quincy_play]

    if record['kris']['results']['win'] < 61:
        guess = ideal_response[kris_play]

    if record['mrugesh']['results']['win'] < 61:
        guess = ideal_response[mrugesh_play]


    #Update records fo each player
    record['abbey']['results'] = result(guess, abbey_play, record['abbey']['results'])
    record['abbey']['o_history'].append(abbey_play)
    record['abbey']['p_history'].append(guess)

    record['mrugesh']['results'] = result(guess, mrugesh_play, record['mrugesh']['results'])
    record['mrugesh']['o_history'].append(mrugesh_play)
    record['mrugesh']['p_history'].append(guess)

    record['quincy']['results'] = result(guess, quincy_play,record['quincy']['results'])
    record['quincy']['o_history'].append(quincy_play)
    record['quincy']['p_history'].append(guess)
    
    record['kris']['results'] = result(guess, kris_play,record['kris']['results'])
    record['kris']['o_history'].append(kris_play)
    record['kris']['p_history'].append(guess)


    num_games[0] +=1

    return guess

