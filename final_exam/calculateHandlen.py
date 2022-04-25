def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    for letter in hand:
        if hand[letter] != 0:
            length += hand[letter]
    return length
