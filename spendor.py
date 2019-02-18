def can_buy(cost_of_card, tokens_of_player):
    print(tokens_of_player['blue'])
    print(cost_of_card['blue'])
    blue_passes = tokens_of_player['blue'] >= cost_of_card['blue']
    green_passes = tokens_of_player['green'] >= cost_of_card['green']
    red_passes = tokens_of_player['red'] >= cost_of_card['red']
    if blue_passes and green_passes and red_passes:
        return True
    else:
        return False
    
def can_buy(cost_of_card, tokens_of_player):
    passes = []
    passes.append(tokens_of_player['blue'] >= cost_of_card['blue'])
    passes.append(tokens_of_player['green'] >= cost_of_card['green'])
    passes.append(tokens_of_player['red'] >= cost_of_card['red'])
    if all(passes):
        return True
    else:
        return False
    
def can_buy(cost_of_card, tokens_of_player):
    passes_all = True
    for color in cost_of_card.keys():
        passes = tokens_of_player[color] >= cost_of_card[color]
        passes_all = passes_all and passes
    return passes_all

def can_buy(cost_of_card, tokens_of_player):
    for color in cost_of_card.keys():
        passes = tokens_of_player[color] >= cost_of_card[color]
        if passes:
            pass
        else:
            return False
    return True
        
def can_buy(cost_of_card, tokens_of_player):
    for color in cost_of_card.keys():
        if tokens_of_player[color] >= cost_of_card[color]:
            pass
        else:
            return False
     return True

def can_buy(cost_of_card, tokens_of_player):
    for color, cost_count in cost_of_card.items():
        if tokens_of_player[color] >= cost_count
            pass
        else:
            return False
     return True

def can_buy(cost_of_card, tokens_of_player):
    def passes_for_color(color):
        return tokens_of_player[color] >= cost_of_card[color]
    return all(passes_for_color, cost_of_card.keys())

def can_buy(cost_of_card, tokens_of_player):
    return all(lambda color: tokens_of_player[color] >= cost_of_card[color], cost_of_card.keys())


def purchase(card_cost, tokens_of_player):
    pass

card_cost = {'blue': 1, 'green': 2, 'red': 1}
tokens_1 = {'blue': 1, 'green': 2, 'red': 1}

print(can_buy(card_cost, tokens_1))