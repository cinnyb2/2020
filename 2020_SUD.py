import random
import sys
import time
import itertools as it

# constants, that do not change
FOE_VARIETY = ['crippling student debt', 'Murder Hornets', 'Australia bushfire', 'Dow Jones stock market crash',
               'your parents that you started living with since the pandemic', 'your sanity',
               'toilet paper shortage', 'avocado toast you can no longer afford',
               'anti-masker', 'Zoom university', 'online learning']  # variety of foes

RANDOM_TILE_DESCRIPTION = ['You see nothing, the emptiness fill you with hollowness.',
                           'You have entered a hallway full of monster statues, you are filled with fear.',
                           'You see a small light, which sparks hope in you.',
                           'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                           'You are surrounded by tall grass.']  # variety of tile descriptions

ROWS = 26
COLUMNS = 26

DEAD_ASCII = r"""

              _____
             /     \
            | () () |
             \  ^  /
              |||||
              |||||
     You have gone insane.
           """

VICTORY_ASCII = r"""
                                               .''.       
           .''.      .        *''*    :_\/_:     . 
          :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
      .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
     :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
     : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
      '..'  ':::'     * /\ *     .'/.\'.   '
          *            *..*         :
           *
            *
         Congratulations you have survived 2020!"""


def introduction() -> None:
    """
    Prints the introduction to 2020 Game.

    Teach the player how the game works and present them with objectives to complete the game.

    :precondition: this function should be executed as the first in the game.
    :postcondition: function will print helpful introductory text and instructions.
    :return: none, uses print statements
    """
    print(r"""
                 pd*"*b.  ,pP""Yq.   pd*"*b.  ,pP""Yq.  
                (O)   j8 6W'    `Wb (O)   j8 6W'    `Wb 
                    ,;j9 8M      M8     ,;j9 8M      M8 
                 ,-='    YA.    ,A9  ,-='    YA.    ,A9 
                Ammmmmmm  `Ybmmd9'  Ammmmmmm  `Ybmmd9'                       
    """)
    print(f'\nDecember 31st 2019 23:59: You were outside English Bay counting down the seconds until the new year.'
          f'\n2019 was a hard year for you, so you were so excited for the new year.\nIt is 2020 after all, and you are'
          f' here for the 20/20 vision.\nLittle did you know what 2020 has in store for you...\n')
    time.sleep(2)

    print(f'January 1st 2020 00:00: Something has gone horribly wrong the sky turned black'
          f' and you suddenly got \nteleported to an dark abyss. You have to escape abyss full of misfortunes in one'
          f' piece \nby defeating COVID-19 and everything that it throws at you without going insane.\n')
    time.sleep(2)

    print(f'Choose your fate wisely, each fate has different attributes and start at different positions.'
          f'\nThe more events (foes) you surviving through, the more you will generate antibodies (EXP) '
          f'\nby increasing your immunity (Level) and increase your HP which is your sanity meter. '
          f'\nYou need to defeat COVID-19 (final boss) by generating enough antibodies to withstand its attack and '
          f'survive 2020.\nYour location is marked by the P, and the final boss is the virus marked, there is a 20% '
          f'chance of an \nevent occurring which may inflict damage onto you before you attack it, or when you flee.'
          f'\nYou may choose to quit at any time by typing \'quit\' after you have selected your fate.')

    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    time.sleep(2)


def player_name() -> str:
    """
    Prompts user to enter their name, helper function for choose_character.

    :precondition: name cannot be changed once entered
    :postcondition: player name will be stored into the character dictionary
    :return: string
    """
    print(f'Please enter your name to start: ')
    name = input().title()  # Capitalize the first letter of the name entered
    return name


def generate_random_tile_description() -> str:
    """
    Returns a random tile description out of a list of random room descriptions.

    :precondition: the random tile description index has to be one of the 5 tile description in the list specified (0,4)
    :postcondition: correctly returns a random tile description out of a list of tile descriptions
    @return: a string describing the tile
    """
    # picks a random number from 0 to 4, and the number would be the index of the list of tiles chosen
    return RANDOM_TILE_DESCRIPTION[random.randint(0, 4)]


def make_board(rows: int, columns: int) -> dict:
    """
    Creates a game board dictionary the size of the rows and column argument.

    The dictionary format will be {(x, y): 'room description'}, where the x and y coordinates tuple will be the keys and
    the value will be a random room description.

    @param rows: positive non-zero integer
    @param columns: positive non-zero integer
    :precondition: both rows and columns must be positive non-zero integer
    :precondition: param must be >= 2
    :postcondition: correctly returns a dictionary
    @return: a dictionary
    """
    # create a dictionary with (x, y) as key and random tile description as the value
    dict_board = {(row, column): generate_random_tile_description() for row in range(rows) for column in range(columns)}
    return dict_board


def choose_character() -> dict:
    """
    Choose from a number list which character, the user would like to select.

     All character starts at a different position on the board and have different baseline stats
    :precondition: player must enter from the number option give, the game will otherwise break and exit
    :precondition: player must provide their name in order select their desired fate
    :postcondition: creates a character dictionary that contains their position on the game board and their current HP
    @return: dictionary with character information
    """
    name = player_name()
    all_character_options = {'vulnerable senior': {'X-coordinate': 20, 'Y-coordinate': 17, 'Current HP': 3, 'Level': 1,
                                                   'EXP': 0, 'Name': name, 'Attack': 10, 'Number of Attacks': 1,
                                                   'Attack description': 'You showed your hospital bill.',
                                                   'Description': 'You don\'t have a lot of life you but you '
                                                                  'keep hanging on!'},
                             'unemployed new grad': {'X-coordinate': 5, 'Y-coordinate': 2, 'Current HP': 8,
                                                     'Level': 1, 'EXP': 0, 'Name': name, 'Attack': 5,
                                                     'Number of Attacks': 1,
                                                     'Attack description': 'You Threw your overpriced textbook.',
                                                     'Description': 'You are hopeful but a bit jaded.'},
                             'furloughed worker': {'X-coordinate': 8, 'Y-coordinate': 7, 'Current HP': 15, 'Level': 1,
                                                   'Description': 'You are just done with life.', 'Name': name,
                                                   'Attack': 2, 'EXP': 0, 'Number of Attacks': 1,
                                                   'Attack description': 'You showed your receding hairline.'},
                             'angry teenager': {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Level': 1,
                                                'Description': 'You don\'t know why but you are angry at everything.',
                                                'Name': name, 'Attack': 8, 'EXP': 0, 'Number of Attacks': 1,
                                                'Attack description': 'You told the foe that you just don\'t want to '
                                                                      'talk about it.'}}

    print(f'\nWelcome {name}, please choose your fate (1, 2, 3, 4): \n'  # option list
          '1. Vulnerable senior \n'
          '2. Unemployed new graduate \n'
          '3. Furloughed worker \n'
          '4. Angry teenager \n')

    # edge case where user enter something other than the valid number (e.g. a number, a space, number outside index)
    acceptable_inputs = list(map(str, [i for i in range(1, 5)]))  # makes sure input is within [1, 2, 3, 4]
    player_input = input()  # prompt input
    while player_input not in acceptable_inputs:  # if it is not an acceptable input enter into while loop
        print(f"That is an invalid answer. Please choose again (1, 2, 3, 4): ")
        player_input = input()

    for index, character_type in enumerate(all_character_options.keys(), 1):  # enumerate all_character_option's keys
        if str(index) == player_input:  # check to see if character key is within input
            return all_character_options[character_type]


def describe_character(character: dict) -> None:
    """
    Describe the character description.

    @param character: a dictionary of a character's information
    :precondition: character's HP must > 0
    :postcondition: describe the room description and the current character coordinates of the character
    @return: none, print statement

    >>> player = {'Description': 'You are just done with life.', 'Attack': 2, 'Current HP': 15, 'Level': 1,\
    'Attack description': 'You showed your receding hairline.'}
    >>> describe_character(player)
    Attack: 2
    HP: 15
    Level: 1
    Special Attack: You showed your receding hairline.
    Description: You are just done with life.
    >>> player = {'Current HP': 8, 'Attack': 5, 'Level': 1, 'Attack description': 'You Threw your overpriced textbook',\
    'Description': 'You are hopeful but a bit jaded.'}
    >>> describe_character(player)
    Attack: 5
    HP: 8
    Level: 1
    Special Attack: You Threw your overpriced textbook
    Description: You are hopeful but a bit jaded.
    """
    print(f"Attack: {character['Attack']}"  # prints the character's stats
          f"\nHP: {character['Current HP']}"
          f"\nLevel: {character['Level']}"
          f"\nSpecial Attack: {character['Attack description']}"
          f"\nDescription: {character['Description']}")


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe the tile and the current board coordinates of the character.

    @param board: a dictionary
    @param character: a dictionary
    :precondition: character must be within the playing boundary of the board, and the exact coordinates of the
    character must be present in the board
    :precondition: character's HP must > 0
    :precondition: board must be unchanged
    :postcondition: describe the room description and the current board coordinates of the character
    @return: None

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> describe_current_location(board_map, player)
    <BLANKLINE>
    room 3 Your current coordinates are (1, 2).

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> describe_current_location(board_map, player)
    <BLANKLINE>
    room 1 Your current coordinates are (0, 0).
    """

    coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])  # combine the x and y values
    description = board[coordinates_tuple]

    print(f'\n{description} Your current coordinates are {coordinates_tuple}.')


def board_printer(width: int, height: int, character: dict) -> None:
    """
    Prints the board and character health.
    If the value for the key is true, the board displays the character's location.

    :param height: integer of height
    :param width: integer of width
    :param character: a dictionary
    :precondition: location must be a dictionary, character_health must be an int.
    :postcondition: print the map of the board with the location of the character and game boss
    :return: printed board displaying character's location and game boss location

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_printer(2, 4, player)
    #######
    # . P #
    # . . #
    # . . #
    # . . #
    #######
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])

    print("#" * (2 * width + 3))  # add the top border

    for row in range(height):
        print("#", end=" ")
        for column in range(width):
            if character_location == (column, row):
                print('P', end=" ")  # character location
            elif (column, row) == (20, 20):
                print('🦠', end="")  # game boss location
            else:
                print(".", end=" ")  # prints . for all tiles that are not the character nor game boss
        print("#")

    print("#" * (2 * width + 3))  # bottom border


def health_printer(character: dict) -> None:
    """
    Prints the character health.

    :param character: a dictionary
    :precondition: character HP must be > 0
    :postcondition: each key is printed and for the key that is assigned True as a value, it prints the character
    :return: printed board displaying character's current health
    """
    hearts = "♥ " * character['Current HP']
    empty_hearts = "♡ " * (20 - character['Current HP'])
    print(f"Health Points [{character['Current HP']} /20] {hearts}{empty_hearts}")  # represents your character HP
    # cannot be doctest since there was an additional space that evokes error


def user_direction_choice() -> str:
    """
    Prompt the user to enter which direction they wish to go.

    :precondition: user must input either the number, the starting letter or full direction corresponding to the
    direction they wish to go for input to register (e.g. '1', 'n', 'north', or 'North')
    :postcondition: user will enter the direction they wish to go
    @return: string stating direction 'North', 'East', 'South', 'West'
    """
    print('1. North \n'
          '2. East \n'
          '3. South \n'
          '4. West \n'
          'Please enter the number that corresponds to the direction you want to go (1, 2, 3, 4): ')
    user_direction_input = input()

    user_direction_input = user_direction_input.lower()

    direction_choice_dict = {('1', 'n', 'north'): 'North', ('2', 'e', 'east'): 'East',
                             ('3', 's', 'south'): 'South', ('4', 'w', 'west'): 'West'}

    while True:  # keeps looping until user enters a valid response from direction dictionary or enter quit
        for key, values in direction_choice_dict.items():
            if user_direction_input in key:
                return values  # return the string input
            if user_direction_input == 'quit':
                quit_game()  # calls quit function to exit the game

        print("That is an invalid answer. Please try again: ")  # If response is invalid, have user try again
        user_direction_input = input()


def quit_game() -> None:
    """
    Exit out of the game.

    :precondition: user must type 'quit' in order to quit
    :postcondition: successfully exit out of the game
    :return: None, exits out of the system
    """
    print(f'You have lost the will to go on...')  # message when user enter 'quit'
    sys.exit()  # exit out of the system and ends the game


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate whether the character is on the board and whether they can travel on to their desired direction on the map

    @param board: a dictionary
    @param character: a dictionary
    @param direction: a string from ['North', 'East', 'South', 'West']
    :precondition: the new position that the characcter moves to must be on the board
    :precondition: board must be unchanged
    :postcondition: validate correctly whether the character is on the board and whether they can travel on to their
    desired direction on the map
    @return: True or False

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'North'
    >>> validate_move(board_map, player, path)
    True

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'West'
    >>> validate_move(board_map, player, path)
    False
    """
    x_value = character['X-coordinate']
    y_value = character['Y-coordinate']  # stores your coordinates, so it is easier to work with

    if direction == 'North':
        y_value -= 1
    elif direction == 'East':
        x_value += 1
    elif direction == 'South':
        y_value += 1
    elif direction == 'West':
        x_value -= 1
    else:
        return False  # invalid direction

    return (x_value, y_value) in board.keys()  # return bool, whether (x or y) is in board.keys True else False


def move_character(board: dict, character: dict, direction: str) -> dict:
    """
    Move the character to the character to their new location given direction.

    @param board: dictionary of board coordinates with corresponding room description
    @param character: dictionary of character's coordinates and HP
    @param direction: a string from ['North', 'East', 'South', 'West']
    :precondition: direction must be one either North, East, South or West
    :precondition: board must be unchanged
    :precondition: the move must be validate (both the current position and the new position must be present on the
    board)
    :postcondition: move the character to the character to their new location given direction
    @return: dictionary of character's new coordinates

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'East'
    >>> move_character(board_map, player, path)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (0, 1): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'South'
    >>> move_character(board_map, player, path)
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    """

    if validate_move(board, character, direction):
        if direction == 'North':
            character['Y-coordinate'] -= 1
        elif direction == 'East':
            character['X-coordinate'] += 1
        elif direction == 'South':
            character['Y-coordinate'] += 1
        elif direction == 'West':
            character['X-coordinate'] -= 1
    return character  # return the modified character dictionary that has a new position


def foe_generator() -> dict:
    """
    Generate a random foe from a list of foes.

    :precondition: cannot generate a specific foe and the foe generated must be in the FOE_VARIETY list
    :postcondition: generate a random foe from a list of foes
    :return: dictionary with the foe's information
    """
    foes = {'Name': random.choice(FOE_VARIETY), 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50,
            'Number of Attacks': 1, 'Attack description': 'Its trying its best to make you miserable.'}
    return foes  # Choose a random foe from the FOE_VARIETY and give it all the same stats


def populate_foes_on_board(foe: dict) -> str:
    """
    Populate a random foe onto the game board

    :param foe: dictionary of the enemy's information
    :precondition: the character must encounter a foe first
    :postcondition: a random foe will be populated onto the board
    :return: dictionary of the enemy's information

    >>> enemy = {'Name': 'Australia bushfire', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50}
    >>> populate_foes_on_board(enemy)
    You have encountered a foe, Australia bushfire! It has 5 HP.
    'Australia bushfire'

    >>> enemy = {'Name': 'Murder Hornets', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50}
    >>> populate_foes_on_board(enemy)
    You have encountered a foe, Murder Hornets! It has 5 HP.
    'Murder Hornets'
    """
    type_of_foe = foe['Name']
    foe_hit_points = foe['Current HP']

    print(f'You have encountered a foe, {type_of_foe}! It has {foe_hit_points} HP.')  # Describe the foe to the player
    return type_of_foe


def check_for_foes() -> bool:
    """
    Returns True or False based on whether you have encountered a foe.

    :precondition: chance of encountering foe is always 20% and cannot be changed
    :postcondition: returns True or False based on whether you have encountered a foe
    @return: True or False
    """
    return random.randint(0, 4) < 1  # 20% chance of encountering foe


def user_combat_choice() -> str:
    """
    Prompt the user to enter which option they wish to do when they encounter a foe.

    :precondition: user must input either the number, the starting letter or full direction corresponding to the
    direction they wish to go for input to register (e.g. '0', 'a', 'attack', or 'Attack')
    :postcondition: the program will register their option and respond accordingly
    @return: string stating options
    """
    print('1. Attack \n'
          '2. Flee \n'
          'Please enter the number that correspond to the action you wish to take (1, 2): ')

    user_combat_input = input()

    user_combat_input = user_combat_input.lower()

    combat_choice_dict = {('1', 'a', 'attack'): 'Attack', ('2', 'f', 'flee'): 'Flee'}

    while True:
        for key, values in combat_choice_dict.items():
            if user_combat_input in key:  # see if user input option is a value of the key
                return values

            if user_combat_input == 'quit':
                quit_game()

        print("That is an invalid answer. Please try again (1, 2): ")
        user_combat_input = input()


def battle(character: dict, foe: dict) -> dict:
    """
    Initiates a battle between character and a foe

    The character/player will always go first.
    :param character: dictionary with character's information
    :param foe: dictionary of the foe's information
    :precondition: both the character and foe must have dictionaries that contain the same keys
    :precondition: both parties must have HP > 0 at the start of the battle
    :postcondition: battle will continue until either until the character choose to flee or quit, otherwise until
    one party dies
    :return: dictionary of character information
    """
    while is_alive(character) and is_alive(foe):  # keep looping if both character and foe are alive
        decision = user_combat_choice()

        if decision == 'Flee':
            flee(character)   # calls the flee function
            return character

        if decision == 'Attack':
            attack_foe(character, foe)  # character attacks first
            if not is_alive(foe):  # if the foe dies
                character['EXP'] += foe['EXP']    # gives character exp for killing foe
                print(f"\nYou have defeated {foe['Name']}. You have gained {character['EXP']} EXP!")
                return character
            attack_foe(foe, character)  # foe's turn to attack character


def attack_foe(character: dict, foe: dict) -> None:
    """
    Attack the opposing character.

    Attack damage is based on the character's own attack damage output.
    :param foe: dictionary of the enemy's information
    :param character: dictionary with character's information
    :precondition: both character must be alive at the start
    :postcondition: successfully inflict damage to the opposing character
    :return: None, print statements

    >>> player = {'Current HP': 10, 'Level': 1, 'Attack': 3, 'Attack description': 'You showed your receding hairline.'\
    ,'Number of Attacks': 1, 'Name': 'Cindy'}
    >>> enemy = {'name': 'anti-masker', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1, \
    'Name': 'Hannah'}
    >>> attack_foe(player, enemy)
    <BLANKLINE>
    Cindy You showed your receding hairline. It Inflicts 3 damage to Hannah.
    Hannah has 2 HP.
    >>> player = {'Current HP': 10, 'Level': 1, 'Attack': 3, 'Attack description': 'You glared menacingly', 'EXP': 50,\
'Number of Attacks': 1, 'Name': 'Cindy'}
    >>> enemy = {'Name': 'anti-masker', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,\
    'Attack description': 'refuse to wash its hands too!'}
    >>> attack_foe(enemy, player)
    <BLANKLINE>
    anti-masker refuse to wash its hands too! It Inflicts 1 damage to Cindy.
    Cindy has 9 HP.
    """
    for attack_damage in it.repeat(character['Attack'], character['Number of Attacks']):  # makes an iterable of the
        foe['Current HP'] -= attack_damage  # number of attack times, so some foes can attack twice in a turn
        print(f"\n{character['Name']} {character['Attack description']} It Inflicts {attack_damage} damage to "
              f"{foe['Name']}.")
        print(f"{foe['Name']} has {foe['Current HP']} HP.")


def flee(character: dict) -> dict:
    """
    Flee from the foe.

    There is a 20% chance of the foe dealing 1-2 damage.

    :param character: dictionary with character's information
    :precondition: the character's HP > 0
    :postcondition: the character will flee successfully with a change of
    :return: character dictionary
    """
    result = random.randint(0, 4) < 1  # 20% chance of getting attack when character flees
    if result == 1:
        damage = random.randint(1, 2)  # deal 1-2 damage
        print(f'\n The enemy attack you as you flee, you took {damage}.')
        character['Current HP'] -= damage
        return character
    else:
        print(f"\nYou got away safely!")
        return character


def make_boss() -> dict:
    """
    Create the boss of the game.

    :precondition: the boss cannot move, it's position on the map is stationary
    :postcondition: creates a game boss dictionary that contains their position on the game board and their current HP
    :return: dictionary with the boss's information

    >>> make_boss()
    {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 15, 'Attack': 2, 'EXP': 100000000, \
'Description': "Despite being a non-living object, it smirks at the thought of you fighting it, as it flash all \
its' crowns at you.", 'Name': 'SARS‐CoV‐2', 'Number of Attacks': 2, 'Attack description': 'is trying to mutate itself\
 to have your DNA.'}
    """
    game_boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 15, 'Attack': 2, 'EXP': 100000000,
                 'Description': 'Despite being a non-living object, it smirks at the thought of you fighting it, '
                                'as it flash all its\' crowns at you.', 'Name': 'SARS‐CoV‐2', 'Number of Attacks': 2,
                 'Attack description': 'is trying to mutate itself to have your DNA.'}
    return game_boss  # creates a boss object


def check_boss_location(character: dict, game_boss: dict) -> bool:
    """
    Check to see if the character has encounter the game boss.

    :precondition: the character and the game boss must both be in the same board coordinates
    :postcondition: correctly check to see if the character has encountered the game boss.
    If the character's coordinates is the same as the game boss, return True else False

    :param character: dictionary with character's information
    :param game_boss: dictionary of game boss information
    >>> player = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 5}
    >>> boss = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 20}
    >>> check_boss_location(player, boss)
    True
    >>> player = {'X-coordinate': 23, 'Y-coordinate': 18, 'Current HP': 5}
    >>> boss = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 20}
    >>> check_boss_location(player, boss)
    False
    """
    boss_coordinates_tuple = (game_boss['X-coordinate'], game_boss['Y-coordinate'])
    character_coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])

    # Check to see if the game boss has the same coordinates as you
    return True if boss_coordinates_tuple == character_coordinates_tuple else False


def describe_boss(game_boss: dict) -> None:
    """

    Describe the game boss information

    :param game_boss: dictionary of the game boss information
    :precondition: the player must be in the same board location as the game boss to interact with it
    :postcondition: describe the game boss's information
    :return: none, print statements

    >>> boss = {'Current HP': 15, 'Description': " It smirks at the thought of you fighting it."}
    >>> describe_boss(boss)
    You have encountered the source of this pandemic, SARS‐CoV‐2. I hope you have build up enough immunity to stand a \
fighting chance against it.
     It smirks at the thought of you fighting it. It has 15 HP.

    """
    print(f"You have encountered the source of this pandemic, SARS‐CoV‐2. I hope you have build up enough immunity "
          f"to stand a fighting chance against it.\n{game_boss['Description']} It has {game_boss['Current HP']} HP.")


def level_checker(character: dict) -> bool:
    """
    Check to see if character has enough EXP to level up.

    :param character: dictionary with character's information
    :precondition: the character must have the specified number of EXP that correlates to the level increase
    :postcondition: the function will return whether it is true that they have enough EXP to level up or not
    :return: True or False

    >>> player = {'EXP': 200}
    >>> level_checker(player)
    True
    >>> player = {'EXP': 150}
    >>> level_checker(player)
    False
    """
    return True if character['EXP'] == 100 or character['EXP'] == 200 else False


def level_up(character: dict) -> dict:
    """
    Level up the character and increase their attack and HP with each level up.

    :param character: dictionary with character's information
    :precondition: the character must have the specified number of EXP that correlates to the level increase
    :postcondition: level up the character and increase their attack and HP with each level up
    :return: dictionary of the character's information

    >>> player = {'Level': 1, 'EXP': 100, 'Current HP': 5, 'Attack': 2}
    >>> level_up(player)
    {'Level': 2, 'EXP': 100, 'Current HP': 7, 'Attack': 4}

    >>> player = {'Level': 2, 'EXP': 200, 'Current HP': 5, 'Attack': 2}
    >>> level_up(player)
    {'Level': 3, 'EXP': 200, 'Current HP': 8, 'Attack': 9}
    """
    if character['EXP'] == 100 and character['Level'] == 1:
        character['Level'] += 1
        character['Attack'] += 2
        character['Current HP'] += 2
    if character['EXP'] == 200 and character['Level'] == 2:
        character['Level'] += 1
        character['Attack'] += 7
        character['Current HP'] += 3

    return character


def level_describer(character: dict) -> None:
    """
    Describe the character's level.

    :param character: dictionary of the character
    :precondition: character must either level 2 or 3
    :postcondition: a description of the character level will be printed
    :return: None, print level message

    >>> player = {'X-coordinate': 23, 'Y-coordinate': 18, 'Current HP': 5, 'Level': 2, 'EXP': 100}
    >>> level_describer(player)
    Congratulations, you have leveled up to 2. You are now a partially vaccinated!

    >>> player = {'X-coordinate': 23, 'Y-coordinate': 18, 'Current HP': 5, 'Level': 3, 'EXP': 200}
    >>> level_describer(player)
    Congratulations, you have leveled up to 3. You are now fully vaccinated!
    """
    if character['EXP'] == 100:
        print(f"Congratulations, you have leveled up to {character['Level']}. You are now a partially vaccinated!")
    if character['EXP'] == 200:
        print(f"Congratulations, you have leveled up to {character['Level']}. You are now fully vaccinated!")
    if character['EXP'] > 100000000:
        print(f"Congratulations, you have unlocked hidden level. You are the hero the world needed!")


def check_if_goal_attained(board: dict, character: dict, game_boss: dict) -> bool:
    """
    Check to see if the character has reached the destination (20, 20) and defeated the monster

    True if character has reached destination and defeated the final boss else False.

    @param board: dictionary
    @param character: dictionary
    @param game_boss: dictionary of game boss information
    :precondition: character must be within the board boundary
    :precondition: board must be unchanged
    :postcondition: check to see if the character has reached the destination (20, 20)
    :return: True or False
    >>> player = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (20, 18): 'room 3'}
    >>> boss = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 0, 'Attack': 2}
    >>> check_if_goal_attained(board_map, player, boss)
    True

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (20, 18): 'room 7'}
    >>> boss = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 15, 'Attack': 2}
    >>> check_if_goal_attained(board_map, player, boss)
    False
    """
    coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])
    if coordinates_tuple == (20, 20) in board.keys() and not is_alive(game_boss):
        return True
    else:
        return False


def is_alive(character: dict) -> bool:
    """
    Return whether or not the character is still alive.

    @param character: dictionary with character's information (x, y coordinates, and current HP)
    :precondition: character cannot have < 0 HP
    :postcondition: Return whether or not the character is still alive
    @return: True or False

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> is_alive(player)
    True

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0}
    >>> is_alive(player)
    False
    """
    return False if character['Current HP'] <= 0 else True


def victory() -> None:
    """
    Return the ASCII art for when the character wins the game

    :precondition: character HP must be > 0 and must have defeated the game boss
    :postcondition: return the ASCII art for when the character wins
    :return: None, print statement
    """
    print(VICTORY_ASCII)


def dead_player() -> None:
    """
    Return the ASCII art for when the character dies.

    :precondition: character must be 0 HP
    :postcondition: return the ASCIII art for when the character dies
    :return: None, print statement
    >>> dead_player()
    """
    print(DEAD_ASCII)


def game() -> None:
    """
    Run the entire game

    Continuously loop the gameplay until the user wins or quits.
    :precondition: user must provide input
    :postcondition: the game will be over once this function terminates.
    :return: None, print statements
    """
    introduction()
    board = make_board(ROWS, COLUMNS)
    character = choose_character()
    describe_character(character)
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        board_printer(ROWS, COLUMNS, character)
        health_printer(character)
        describe_current_location(board, character)  # Tell the user where they are
        direction = user_direction_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(board, character, direction)
            final_boss = make_boss()
            boss_present = check_boss_location(character, final_boss)
            there_is_a_challenger = check_for_foes()
            if boss_present:
                describe_boss(final_boss)
                battle(character, final_boss)
                if level_checker:
                    level_up(character)
                    level_describer(character)
            elif there_is_a_challenger:
                foe = foe_generator()
                populate_foes_on_board(foe)
                battle(character, foe)
                if level_checker:
                    level_up(character)
                    level_describer(character)
            achieved_goal = check_if_goal_attained(board, character, final_boss)
        else:
            print(f"Oh no, you have reached the a dead end!")

    if achieved_goal:
        victory()
    if not is_alive(character):
        dead_player()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
