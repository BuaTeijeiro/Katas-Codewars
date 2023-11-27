def bowling_score(frames):
    print(frames)
    throws = frames.split(' ')
    print(throws)
    points = 0
    double_2_turns = 0
    double_1_turn = 0
    for i, throw in enumerate(throws):
        for character in throw:
            mult = 1
            if double_1_turn > 0:
                mult += double_1_turn
                double_1_turn = 0
            if double_2_turns == 1:
                mult += 1
                double_2_turns = 0
                double_1_turn += 1
            if character.isdigit():
                new_score = int(character)
            elif character == '/':
                new_score = 10 - int(throw[0])
                if i != 9:
                    double_1_turn +=1
            elif character == 'X':
                new_score = 10
                if i != 9:
                    double_2_turns += 1
            points += mult * new_score
            print(character,mult,new_score,points)
    return points