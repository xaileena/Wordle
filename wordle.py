#Name : Aileena Xie
#Student ID : 261050876

WORDLE_WORD_LENGTH = 5
MAX_NUM_OF_GUESSES = 6
CHAR_GREEN = '\x1b[6;30;42m'
CHAR_YELLOW = '\x1b[6;30;43m'
CHAR_GRAY = '\x1b[6;30;47m'
CHAR_END = '\x1b[0m'

import random
import wordle_utils

def is_valid_word(word, str_list):
    '''
    (str, list) -> bool
    Returns True if word contains 5 letters and is in str_list
    Returns False otherwise
    
    >>> is_valid_word('star', ['star', 'sand', 'snowflake'])
    False
    
    >>> is_valid_word('music', ['monster', 'magma', 'melancholy', 'music'])
    True
    
    >>> is_valid_word('sushi', ['sashimi', 'sorrow', 'sick', 'sequence'])
    False
    
    >>> is_valid_word('about', ['abounds', 'about', 'abouts', 'above', 'aboveboard'])
    True
    
    '''
    
    if word in str_list and len(word) == WORDLE_WORD_LENGTH:
        return True
    
    else:
        return False



def print_string_list (str_list):
    '''
    (list) -> NoneType
    Function prints each string in str_list on a new line
    
    >>> print_string_list(['star', 'sand', 'snowflake'])
    star
    sand
    snowflake
    
    >>> print_string_list(['monster', 'magma', 'melancholy', 'music'])
    monster
    magma
    melancholy
    music
    
    >>> print_string_list(['sashimi', 'sorrow', 'sick', 'sequence'])
    sashimi
    sorrow
    sick
    sequence
    
    >>> print_string_list(['abounds', 'about', 'abouts', 'aboveboard', 'abovedeck'])
    abounds
    about
    abouts
    aboveboard
    abovedeck
    
    '''
    
    for word in range(len(str_list)):
        print(str_list[word])
        


def color_string(word, color):
    '''
    (str, str) -> str
    Returns word concatenated in between color ANSI codes and CHAR_END
    If color is not 'green', 'yellow' or 'gray, function prints 'Invalid color'
    and returns word without color
    
    >>> color_string ('apple', 'green')
    \x1b[6;30;42mapple
    
    >>> color_string ('star', 'yellow')
    \x1b[6;30;43mstar
    
    >>> color_string ('spoon', 'gray')
    \x1b[6;30;47mspoon
    
    >>> color_string ('coral', 'pink')
    Invalid color.
    coral
    
    '''
    
    if color == 'green' or color == 'yellow' or color == 'gray':
        
        if color == 'green':
            return (str(CHAR_GREEN) + str(word) + str(CHAR_END))
        
        elif color == 'yellow':
            return (str(CHAR_YELLOW) + str(word) + str(CHAR_END))
        
        else:
            return (str(CHAR_GRAY) + str(word) + str(CHAR_END))
    
    else:
        print('Invalid color.')
        return word



def get_all_5_letter_words(str_list):
    '''
    (list) -> list
    Returns a new list of words that have the length of WORDLE_WORD_LENGTH
    
    >>> get_all_5_letter_words(['tabby', 'table', 'tar', 'tree', 'think'])
    ['tabby', 'table', 'think']
    
    >>> get_all_5_letter_words(['cat', 'clementine', 'cable', 'car'])
    ['cable']
    
    >>> get_all_5_letter_words(['ear', 'eager', 'earth', 'eagle'])
    ['eager', 'earth', 'eagle']
    
    >>> get_all_5_letter_words(['abs', 'about', 'abouts', 'above', 'aboveboard', 'aloft'])
    ['about', 'above', 'aloft']
    
    '''

    proper_list = []
    
    for word in str_list:
        if len(word) == WORDLE_WORD_LENGTH:
            proper_list.append(word)
        
    return proper_list




def generate_random_wordle(str_list):
    '''
    (list) -> str
    Returns random string from str_list
    
    >>> generate_random_wordle(['apple', 'annex', 'ankle', 'anvil'])
    apple
    
    >>> generate_random_wordle(['banjo', 'bumpy', 'black', 'blimp'])
    blimp
    
    >>> generate_random_wordle(['cable', 'cater', 'crane', 'carve', 'caper'])
    carve
    
    >>> generate_random_wordle(['about', 'above', 'aloft', 'aeons'])
    above
    
    '''
    
    #random_str is actually the index between 0 and the length of the string
    #so random.randint will give a random integer between those indices
    #which will return a random string from the list
    random_str = random.randint(0, len(str_list))
    return str_list[random_str]




def input_wordle (str_list):
    '''
    (list) -> str
    Asks user to input a word with the message "Input today's word: "
    Returns wordle from str_list
    Prints 'Not a valid word, please enter a new one.' if wordle is not in str_list
    
    '''
    
    todays_word = wordle_utils.input_and_hide("Input today's word: ")
    #We want the game to be played in lower case even if the input is in upper case
    todays_word = todays_word.lower()
    
    while todays_word not in str_list:
        print("Not a valid word, please enter a new one. ")
        todays_word = wordle_utils.input_and_hide("Input today's word: ")
    
    return todays_word





def choose_mode_and_wordle(str_list):
    '''
    (list) -> str
    Asks user to enter the number of players
    Returns random wordle from str_list if in player 1 mode
    Returns player 1's input of wordle from str_list if in 2 player mode
    
    >>> choose_mode_and_wordle(['apple', 'annex', 'ankle', 'anvil'])
    Enter the number of players: #1
    annex
    
    >>> choose_mode_and_wordle(['banjo', 'bumpy', 'black', 'blimp'])
    Enter the number of players: #2
    ***** Player 1's turn. *****
    
    ***** Player 2's turn. *****
    
    banjo
    
    >>> choose_mode_and_wordle(['apple', 'annex', 'ankle', 'anvil'])
    Enter the number of players: #2
    ***** Player 1's turn. *****
    
    ***** Player 2's turn. *****
    
    anvil
    
    >>> choose_mode_and_wordle(['banjo', 'bumpy', 'black', 'blimp'])
    Enter the number of players: #1
    bumpy
    
    '''
    
    ask_mode = input("Enter the number of players: ")
    
    while ask_mode != '1' and ask_mode != '2':
        print("Wordle can be played with 1 or 2 players. Please only enter 1 or 2.")
        ask_mode = input("Enter the number of players: ")
    
    
    if ask_mode == '1':
        random_str = generate_random_wordle(str_list)
        return random_str
    
    
    #I am calling the input_wordle function defined earlier, so that player 2
    #cannot see player 1's input. Please note that p1 stands for player 1
    else:
        print("\n***** Player 1's turn. *****\n")
        p1_wordle = input_wordle(str_list)
        
        print("\n***** Player 2's turn. *****\n")
        return p1_wordle




def compare_and_color_word(guess_word, soln_word):
    '''
    (str, str) -> str
    Function returns colored guess_word
    Letter from guess_word is colored green if the letter is the same
    and in the same position as soln_word
    Letter from guess_word is colored yellow if the letter is the same
    but at the wrong position as soln_word
    Letter from guess_word is colored gray otherwise
    
    >>> compare_and_color_word('axiom', 'axons')
    \x1b[6;30;42ma\x1b[6;30;42mx\x1b[6;30;47mi\x1b[6;30;43mo\x1b[6;30;47mm
    
    >>> compare_and_color_word('dozen', 'dozer')
    \x1b[6;30;42md\x1b[6;30;42mo\x1b[6;30;42mz\x1b[6;30;42me\x1b[6;30;47mn
    
    >>> compare_and_color_word('pizza', 'puppy')
    \x1b[6;30;42mp\x1b[6;30;47mi\x1b[6;30;47mz\x1b[6;30;47mz\x1b[6;30;47ma
    
    >>> compare_and_color_word('mount', 'about')
    \x1b[6;30;47mm\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;43mu\x1b[0m\x1b[6;30;47mn\x1b
    [0m\x1b[6;30;42mt\x1b[0m
    
    '''
    
    color_word = ''
    
    for letter in range(len(guess_word)):
        
        extra_letter = guess_word.count(guess_word[letter])
        #If guess_word has a letter in common with soln_word, but that letter appears more than in soln_word
        soln_word_count = soln_word.count(soln_word[letter])
        
        if guess_word[letter] == soln_word[letter]:
            color_word += color_string(guess_word[letter], 'green')
        
        elif guess_word[letter] in soln_word and extra_letter <= soln_word_count:
            color_word += color_string(guess_word[letter], 'yellow')
        
        else:
            color_word += color_string(guess_word[letter], 'gray')
    
    return color_word




def play_with_word(soln, word_list):
    '''
    (str, list) -> int
    Prints guess with appropriate color code
    Prints 'Not a valid word, please enter a new one' if soln is not in word_list
    Returns number of guesses the player made to guess soln from word_list
    Returns MAX_NUM_OF_GUESS + 1 if player exceed MAX_NUM_OF_GUESSES tries
    
    >>> play_with_word('bumpy',['banjo', 'bumpy', 'black', 'blimp'])
    \x1b[6;30;42mb\x1b[6;30;47ml\x1b[6;30;47ma'\x1b[6;30;47mc\x1b[6;30;47mk
    Not a valid word, please enter a new one.
    \x1b[6;30;42mb\x1b[6;30;47mn\x1b[6;30;47mj\x1b[6;30;47mo
    \x1b[6;30;42mb\x1b[6;30;42mu\x1b[6;30;42mm\x1b[6;30;42mp\x1b[6;30;42my
    
    2
    
    >>> play_with_word('apple', ['apple', 'annex', 'ankle', 'anvil'])
    \x1b[6;30;42ma\x1b[6;30;47mn\x1b[6;30;47mn\x1b[6;30;43me\x1b[6;30;47mx
    \x1b[6;30;42ma\x1b[6;30;47mn\x1b[6;30;47mk\x1b[6;30;42ml\x1b[6;30;42me
    \x1b[6;30;42ma\x1b[6;30;47m\x1b[6;30;47mv\x1b[6;30;47mi\x1b[6;30;47ml
    \x1b[6;30;42ma\x1b[6;30;42mp\x1b[6;30;42mp\x1b[6;30;42ml\x1b[6;30;42me
    
    3
    
    >>> play_with_word(('caper', ['cable', 'cater', 'crane', 'carve', 'caper', 'calls'])
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47ml\x1b[6;30;47ml\x1b[6;30;47ms
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47mb\x1b[6;30;47ml\x1b[6;30;42me
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47ml\x1b[6;30;47ml\x1b[6;30;47ms
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47mt\x1b[6;30;42me\x1b[6;30;42mr
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47mb\x1b[6;30;47ml\x1b[6;30;42me
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47ml\x1b[6;30;47ml\x1b[6;30;47ms
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;47mt\x1b[6;30;42me\x1b[6;30;42mr
    \x1b[6;30;42mc\x1b[6;30;42ma\x1b[6;30;42mp\x1b[6;30;42me\x1b[6;30;42mr
    
    7
    
    '''
    
    num_tries = 0
    guess_word = ''
    guess_list = []
    
    while guess_word != soln:
        
        guess_word = input("Enter a guess: ")
        guess_word = guess_word.lower()
        
        while guess_word not in word_list:
            print('Not a valid word, please enter a new one.')
            guess_word = input("Enter a guess: ")
        
        #Here I am making a call to the function compare_and_color_word
        colored_guess_word = compare_and_color_word(guess_word, soln)
        
        #I am appending every guess the user makes, so that we can print all the colored guesses made so far
        guess_list.append(colored_guess_word)
        
        #Here I am making a call to the function print_string_list
        print_string_list(guess_list)
                
        num_tries += 1
    
    #The user has at most MAX_NUM_OF_GUESSES, ie num_tries <= MAX_NUM_OF_GUESSES
    if num_tries > MAX_NUM_OF_GUESSES:
        return MAX_NUM_OF_GUESSES + 1
    
    else:
        return num_tries




def print_final_message(num_guess, soln):
    '''
    (int, str) -> NoneType
    Prints "You lost!" if the player lost and prints the wordle in green
    Prints "You won!" and prints how many guesses it took for the player to guess the wordle
    
    >>> print_final_message (5, 'apple')
    You won! It took you 5 guesses.
    
    >>> print_final_message (2, 'zebra')
    You won! It took you 2 guesses.
    
    >>> print_final_message (7, 'dream')
    You lost! The word was \x1b[6;30;42m dream
    
    >>> print_final_message(7, 'about')
    You lost! The word was \x1b[6;30;42m about
    
    '''
    
    if num_guess == 1:
        print("You won! It took you " + str(num_guess) + " guess.")
    
    elif num_guess <= MAX_NUM_OF_GUESSES:
        print("You won! It took you " + str(num_guess) + " guesses.")
    
    else:
        print("You lost! The word was " + color_string(soln, 'green'))





def play(str_list):
    '''
    (list) -> NoneType
    Prints what the function choose_mode_and_wordle prints by calling the function
    Prints what the function play_with_word prints by calling the function
    And prints what the function print_final_message prints by calling the function
    
    '''
    
    wordle = choose_mode_and_wordle(str_list)
    num_guess = play_with_word(wordle, str_list)
    
    print_final_message(num_guess, wordle)




def main():
    '''
    (None) -> NoneType
    Loads list of all words from load_words in wordle_utils module
    Filters load_words to get 5 letter words only
    by calling the helper function get_all_5_letter_words
    Prints what the function play prints by calling the function
    
    '''
    
    word_bank = wordle_utils.load_words()
    filtered_list = get_all_5_letter_words(word_bank)
    play(filtered_list)




