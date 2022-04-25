def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    new_hand = hand.copy()
    if word in wordList:
        for letter in word:
            try:
                if (letter not in new_hand) or (new_hand.get(letter) == 0):    
                    return False
                else:
                    new_hand[letter] = new_hand.get(letter) - 1
            except KeyError:
                return False
        return True
    else:
        return False 
