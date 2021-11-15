import random
import time
import itertools as it


def introduction():
    """
    Prints the introduction to 2020 Game.
    """
    print('\n\nDecember 31st 2019 23:59: You were outside English Bay counting down the seconds until the new year.'
          '\n2019 was a hard year for you, so you were so excited for the new year.\nIt is 2020 after all, and you are '
          'here for the 20/20 vision.\nLittle did you know what 2020 has in store for you...\n')
    time.sleep(2)

    print('January 1st 2020 00:00: Something has gone horribly wrong the sky turned black'
          ' and you suddenly got \nteleported to an dark abyss. You have to escape abyss full of misfortunes in one'
          ' piece \nby defeating COVID-19 and everything that it throws at you without going insane.\n')
    time.sleep(2)

    print('Choose your character wisely, they will all have different attributes and start at different positions.')

    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def player_name():
    """
    Prompts user to enter their name, helper function for choose character.

    :return: string
    """
    print('Please enter your name to start: ')
    name = input().title()
    return name


def generate_random_room():
    """
    Returns a random room description out of a list of random room descriptions.

    :precondition: the random room description index has to be one of the 5 room description in the list specified (0,4)
    :postcondition: correctly returns a random room description out of a list of room descriptions
    @return: a string describing the room
    """
    random_room = ['You have discovered a magical room, the aura of magic fills you with wonder.',
                   'You have entered a room full of monster statues, you are filled with fear.',
                   'You have entered a room full of puppies, you are filled with happiness.',
                   'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                   'You have entered an empty room.']

    return random_room[random.randint(0, 4)]


def make_board(rows, columns):
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

    dict_board = {(row, column): generate_random_room() for row in range(rows) for column in range(columns)}
    return dict_board


def choose_character():
    """
    Creates a character dictionary that contains their position on the game board and their current HP.

    :precondition: each character starts at the x and y position (0, 0) and have 5 HP
    :postcondition: creates a character dictionary that contains their position on the game board and their current HP
    @return: dictionary with character information

    """
    name = player_name()
    all_character_options = {'vulnerable senior': {'X-coordinate': 20, 'Y-coordinate': 17, 'Current HP': 2, 'Level': 1,
                                                   'EXP': 0, 'Name': name, 'Attack': 10,
                                                   'Attack description': 'Showed your hospital bill.',
                                                   'Description': 'You don\'t have a lot of life you but you '
                                                                  'keep hanging on!'},
                             'unemployed new grad': {'X-coordinate': 5, 'Y-coordinate': 2, 'Current HP': 8,
                                                     'Level': 1, 'EXP': 0, 'Name': name, 'Attack': 5,
                                                     'Attack description': 'You Threw your overpriced textbook',
                                                     'Description': 'You are hopeful but a bit jaded.'},
                             'furloughed worker': {'X-coordinate': 8, 'Y-coordinate': 7, 'Current HP': 15, 'Level': 1,
                                                   'Description': 'You are just done with life.', 'Name': name, 'Attack'
                                                   : 2, 'Attack description': 'You showed your receding hairline'},
                             'angry teenager': {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Level': 1,
                                                'Description': 'You don\'t know why but you are angry at everything.',
                                                'Name': name, 'Attack': 10,
                                                'Attack description': 'You told the foe that you just don\'t want to '
                                                                      'talk about it.'}}

    print(f'\nWelcome {name}, please choose your fate (0, 1, 2, 3): \n'
          '0. Vulnerable senior \n'
          '1. Furloughed worker \n'
          '2. Unemployed new graduate \n'
          '3. Angry teenager \n')

    character_class_input = input().lower()

    for index, character_type in enumerate(all_character_options.keys()):
        if str(index) == character_class_input:
            return all_character_options[character_type]

    print("That is an invalid answer. Please choose again (0, 1, 2, 3): ")


def describe_character(character):
    """
    Describe the character description.

    @param character: a dictionary
    :precondition: character must be within the playing boundary of the board, and the exact coordinates of the
    character must be present in the board
    :precondition: character's HP must > 0
    :precondition: board must be unchanged
    :postcondition: describe the room description and the current board coordinates of the character
    @return: None

    >>> player = {'Description': 'You are just done with life.'}
    >>> describe_character(player)
    You are just done with life.
    >>> player = {'Description': 'You are hopeful but a bit jaded.'}
    >>> describe_character(player)
    You are hopeful but a bit jaded.
    """
    description = character['Description']

    print(f'{description}')


def describe_current_location(board, character):
    """
    Describe the room description and the current board coordinates of the character.

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
    room 3 Your current coordinates are (1, 2)

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> describe_current_location(board_map, player)
    room 1 Your current coordinates are (0, 0)
    """

    coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])
    description = board[coordinates_tuple]

    print(f'\n{description} Your current coordinates are {coordinates_tuple}')


def board_printer(width, height, character):
    """
    Prints the board and character health.
    If the value for the key is true, the board displays the character's location.

    :param height:
    :param width:
    :param character: a dictionary
    :precondition: location must be a dictionary, character_health must be an int.
    :postcondition: each key is printed and for the key that is assigned True as a value, it prints the character
    :return: printed board displaying character's location & current health

    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> player = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_printer(board_map, 2, 4, player)
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])

    print("#" * (2 * width + 3))

    for row in range(height):
        print("#", end=" ")
        for column in range(width):
            if character_location == (row, column):
                print('P', end=" ")
            elif (row, column) == (20, 18):
                print('🦠', end="")
            else:
                print(".", end=" ")
        print("#")

    print("#" * (2 * width + 3))


def health_printer(character):
    """
    Prints the board and character health.

    If the value for the key is true, the board displays the character's location.

    :param character: a dictionary
    :precondition: location must be a dictionary, character_health must be an int.
    :postcondition: each key is printed and for the key that is assigned True as a value, it prints the character
    :return: printed board displaying character's location & current health

    """
    hearts = "♥ " * character['Current HP']
    empty_hearts = "♡ " * (15 - character['Current HP'])
    print("Health Points [" + str(character['Current HP']) + "/15] " + hearts + empty_hearts)


def user_direction_choice():
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

    while True:
        for key, values in direction_choice_dict.items():
            if user_direction_input in key:
                return values

        print("That is an invalid answer. Please try again: ")
        user_direction_input = input()


def validate_move(board, character, direction):
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
    y_value = character['Y-coordinate']

    if direction == 'North':
        y_value += 1
    elif direction == 'East':
        x_value += 1
    elif direction == 'South':
        y_value -= 1
    elif direction == 'West':
        x_value -= 1
    else:
        return False  # invalid direction

    return (x_value, y_value) in board.keys()


def move_character(board, character, direction):
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
    """

    if validate_move(board, character, direction):
        if direction == 'North':
            character['Y-coordinate'] += 1
        elif direction == 'East':
            character['X-coordinate'] += 1
        elif direction == 'South':
            character['Y-coordinate'] -= 1
        elif direction == 'West':
            character['X-coordinate'] -= 1
    return character


def foe_generator():  # TODO
    """

    :return:

    >>> foe_generator()
    """
    foe_variety = ['crippling student debt', 'Murder Hornets', 'Australia bushfire', 'Dow Jones stock market crash',
                   'your parents that you started living with since the pandemic', 'your sanity', 'shortage in toilet '
                                                                                                  'paper'
                                                                                                  'avocado toast you can no longer afford',
                   'anti-masker', 'Zoom university', 'online learning']

    foes = {'name': random.choice(foe_variety), 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50}
    return foes


def populate_foes_on_board(foe):  # TODO
    """

    :param foe:
    :return:

    >>> enemy = {'name': 'Australia bushfire', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50}
    >>> populate_foes_on_board(enemy)
    You have encountered Australia bushfire!

    >>> enemy = {'name': 'Murder Hornets', 'Current HP': 5, 'Max HP': 5, 'Attack': 1, 'EXP': 50}
    >>> populate_foes_on_board(enemy)
    You have encountered Murder Hornets!
    """
    type_of_foe = foe['name']
    if check_for_foes():
        return type_of_foe
    print(f'You have encountered {type_of_foe}!')


def check_for_foes():
    """
    Returns True or False based on whether you have encountered a foe.

    :precondition: chance of encountering foe is always 20% and cannot be changed
    :postcondition: returns True or False based on whether you have encountered a foe
    @return: True or False
    """
    return random.randint(0, 4) < 1


def user_combat_choice():  # TODO
    """
    Prompt the user to enter which option they wish to do when they encounter a foe.

    :precondition: user must input either the number, the starting letter or full direction corresponding to the
    direction they wish to go for input to register (e.g. '0', 'a', 'attack', or 'Attack')
    :postcondition: the program will register their option and respond accordingly
    @return: string stating option
    """
    print('You have encountered an enemy!\n'
          '0. Attack \n'
          '1. Flee \n'
          '2. Quit \n'
          'Please enter the number that correspond to the action you wish to take (0, 1, 2, 3): ')

    user_combat_input = input()

    user_combat_input = user_combat_input.lower()

    combat_choice_dict = {('0', 'a', 'attack'): 'Attack', ('1', 'f', 'flee'): 'Flee', ('2', 'q', 'quit'): 'Quit'}

    while True:
        for key, values in combat_choice_dict.items():
            if user_combat_input in key:
                return values

        print("That is an invalid answer. Please try again: ")
        user_combat_input = input()


def guessing_game(character):
    """
    Prompt user to play a guessing game.

    Users have to input a number from 1 to 5, if they do not answer the correct number they will receive 1 HP of damage.

    :@param character: dictionary of character's coordinates and HP
    :precondition: character HP > 1 before starting the guessing game
    :precondition: the user must enter a number in range(1, 6), any other number will be wrong and damage will be
    inflicted on the character
    :postcondition: Users have to input a number from 1 to 5, if they do not answer the correct number they will receive
    1 HP of damage
    @return: None
    """
    user_guess = int(input('You have encountered an enemy! Pick a number from 1 to 5: '))
    secret_number = random.randint(1, 5)
    if user_guess == secret_number:
        print(f'You\'ve guessed right!, the number was {secret_number}.')
    else:
        character['Current HP'] -= 1
        hp = character['Current HP']
        print(f'Sorry, that was not the number. I am going to have to hurt you. Your HP is now {hp}.')


def battle(character, foe): # TODO
    pass


def attack(character, foe):  # TODO
    """

    :param foe:
    :param character:
    :param enemy:
    :return:
    """

    character['Current HP'] -= 1
    foe['Current HP'] -= 1


def quit_game():  # TODO
    """

    :return:
    """
    pass


def flee(character):  # TODO need to implement into main
    """
    Flees from the monster. There is a 20% chance of the monster dealing 1-3 damage.
    :return: The amount of damage dealt.


    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> flee(player)
    """
    result = random.randint(0, 4) < 1
    if result == 1:
        damage = random.randint(1, 2)
        print(f'\n The enemy attack you as you flee, you took {damage}.')
        character['Current HP'] -= damage
        return character
    else:
        print("\nYou got away safely!")
        return character


def make_boss():
    """
    Create the boss of the game.

    :precondition: the boss cannot move
    :postcondition: creates a game boss dictionary that contains their position on the game board and their current HP
    :return: dictionary with the boss's information

    >>> make_boss()
    {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 15, 'Attack': 2, 'Description': "Despite being a non-living \
object, it smirks at the thought of you fighting it, as it flash all its' crowns at you."}
    """
    COVID_GAME_BOSS = {'X-coordinate': 20, 'Y-coordinate': 18, 'Current HP': 15, 'Attack': 2,
                       'Description': 'Despite being a non-living object, it smirks at the thought of you fighting it, '
                                      'as it flash all its\' crowns at you.'}
    return COVID_GAME_BOSS


def check_if_goal_attained(board, character, game_boss):  # TODO
    """
    Check to see if the character has reached the destination (20, 18) and defeated the monster

    True if character has reached destination and defeated the final boss else False.

    @param board: dictionary
    @param character: dictionary
    :param game_boss: dictionary of boss stats
    :precondition: character must be within the board boundary
    :precondition: board must be unchanged
    :postcondition: check to see if the character has reached the destination (20, 18)
    @return: True or False
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
    if coordinates_tuple == (20, 18) in board.keys() and not is_alive(game_boss):
        return True
    else:
        return False


def is_alive(character):
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
    return False if character['Current HP'] == 0 else True


def game():
    """
    Drive the entire game.
    """
    introduction()
    ROWS = 26
    COLUMNS = 26
    board = make_board(ROWS, COLUMNS)
    character = choose_character()
    describe_character(character)
    final_boss = make_boss()
    foe = foe_generator()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        board_printer(ROWS, COLUMNS, character)
        health_printer(character)
        describe_current_location(board, character)  # Tell the user where they are
        direction = user_direction_choice()

        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(board, character, direction)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                combat = user_combat_choice()
                guessing_game(character)
            achieved_goal = check_if_goal_attained(board, character, final_boss)
        else:
            print("Oh no, you have reached the a dead end!")

    if achieved_goal:
        print("""
                                                   .''.       
               .''.      .        *''*    :_\/_:     . 
              :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
          .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
         :_\/_:'.:::.    ' *''*    * '.|'/.' _\(/_'.':'.'
         : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
          '..'  ':::'     * /\ *     .'/.|'.   '
              *            *..*         :
               *
                *
             Congratulations you have survived 2020!""")
    if not is_alive(character):
        print("""

                  _____
                 |     |
                | () () |
                 \  ^  /
                  |||||
                  |||||
              You have died.
               """)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
