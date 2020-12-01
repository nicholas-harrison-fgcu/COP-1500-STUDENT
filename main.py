"""Simple Dungeons and Dragons 5th Edition Character Generator."""
__author__ = "Nicholas Harrison"

# COP 1500 project guidelines commented as "per guidelines."
# Below imports math and random for use later.
import math
import random


def continue_key_press():
    """Allows user to progress program and add a line break."""
    input("Press any key to continue: ")
    print(" ")


# Has range, if/else, for, operator, and in per guidelines.
# Formatted this function during conversation with Professor Vanselow.
def roll_six_side_die_four_times(roll):
    """Rolls a six-sided die four times after accepting input."""
    NUM_TIMES = 4
    dice_rolls = []
    if roll == 1:
        for a in range(NUM_TIMES):
            n = random.randint(1, 6)
            dice_rolls.append(n)
    else:
        print("Please use your own dice for this part.")
    return dice_rolls


# Program uses float instead of int to catch user input errors.
# Made my own solution rather than using the one on the course site.
# Multiline docstring formatted via PEP8 site per guidelines.
def get_input(output_string):
    """Sanitizes input with float and floor. Called repeatedly.
    Designed to push the user through the program while resolving errors.
    """
    try:
        answer = float(input(output_string))
        answer = math.floor(answer)
    except ValueError:
        answer = 0
    return answer


def main():
    """Core character creator styled as a conversation."""
    # Intro and user input test. Simple print functions.
    continue_key_press()
    print("Welcome!\nThis is a Dungeons & Dragons character sheet generator.")
    print("This is the second version.")
    continue_key_press()
    print("This program assumes basic knowledge of Dungeons & Dragons.")
    print("Your character creation process is interactive.")
    # Allows user to test keyboard functionality.
    answer_any = input("Try it out. Type anything here: ")
    # Adds lines without a function.
    print(" ")
    # Concatenate a string per guidelines.
    print("You said " + answer_any + "? " + "I'm sure that won't matter.")
    continue_key_press()
    # Uses function get_input to sanitize input. Used throughout.
    answer_start = get_input("Are you ready? 1 = Yes, 2 = No: ")
    # While loop to catch bad input per guidelines.
    # Operators for less/greater than per guidelines.
    # Boolean operator or per guidelines.
    while answer_start < 1 or answer_start > 2:
        answer_start = get_input("You have to answer with 1 or 2: ")
    # If-else statement for user input of 1 or 2(else) per guidelines.
    # Operator for equal per guidelines.
    if answer_start == 1:
        print(" ")
        print("You are in a dim tavern.\nA cloaked figure turns to you.")
    else:
        answer_start = get_input("You feel compelled to enter 1: ")
        # Operator for not equal per guidelines.
        while answer_start != 1:
            answer_start = get_input("You have to answer with 1: ")
        else:
            print(" ")
            print("You are in a dim tavern.\nA cloaked figure turns to you.")
    continue_key_press()
    # Naming process.
    print("The cloaked figure has a quill and parchment.\nIt asks...")
    name_player = input("'What should I call you?' Write your name here: ")
    print(" ")
    print("'Ah,", name_player, "- sounds like an adventurer to me.'")
    answer_name = get_input("Is this your name? 1 = Yes, Other = No: ")
    # Another version of the while loop from earlier.
    while answer_name != 1:
        name_player = input("'What should I call you?' Write your name: ")
        print(" ")
        print("'Ah,", name_player, "- sounds like an adventurer to me.'")
        answer_name = get_input("Happy? 1 = Yes, Other = No: ")
    else:
        print(" ")
        print("The cloaked figure says, 'Very well...'")
        continue_key_press()
    print("The cloaked figure takes a closer look at you.\n'What are you?'")
    print("The figure holds a mirror up and you see...")
    continue_key_press()
    print("Half-Orc? Strong.\nHumans, average skills.\nHalflings? Sneaky.")
    print(" ")
    print("Select a race.")
    race_select = get_input("1 = Half-Orc, 2 = Human, 3 = Halfling: ")
    # Another loop that catches input.
    while race_select < 1 or race_select > 3:
        print(" ")
        print("You didn't pick 1, 2, or 3.")
        race_select = get_input("1 = Half-Orc, 2 = Human, 3 = Halfling: ")
    # Nested if-elif-else with trailing else.
    else:
        if race_select == 1:
            print(" ")
            print("Half-Orc. Strength increases by 2, constitution by 1.")
        elif race_select == 2:
            print(" ")
            print("Human. All ability scores increase by 1.")
        else:
            print(" ")
            print("Halfling. Your dexterity increases by 2.")
    continue_key_press()
    if race_select == 1:
        print("'Aha, I know a half-orc when I see one.'")
    elif race_select == 2:
        print("'Oh, a human? How... interesting?'")
    else:
        print("'A halfling! I barely saw you down there...'")
    continue_key_press()
    print("'Now,' it says, 'I will chant my magic word to find your class.'")
    continue_key_press()
    # Multiply the input string by 10.
    # Should allow for some humor depending on user input.
    print(answer_any * 10)
    continue_key_press()
    # Class selection process.
    print("That makes sense. You are a...")
    print(" ")
    print("Fighters are good with weapons.\nRogues, sneaky.\nWizard? Magic.")
    print("NOTE: primary ability is what you're good at. Saves... save you.")
    print(" ")
    class_select = get_input("1 = Fighter, 2 = Rogue, 3 = Wizard: ")
    while class_select < 1 or class_select > 3:
        print(" ")
        print("Pick 1, 2, or 3.")
        class_select = get_input("1 = Fighter, 2 = Rogue, 3 = Wizard: ")
    # More nested loops per guidelines with operators.
    else:
        if class_select == 1:
            print(" ")
            print("Primary: strength. Save: strength, constitution.")
        elif class_select == 2:
            print(" ")
            print("Primary: dexterity. Save: dexterity, intelligence.")
        else:
            print(" ")
            print("Primary: intelligence. Save: intelligence, wisdom.")
    continue_key_press()
    # A summary for the player so far.
    print("The figure leans back in their chair.\nIt says, 'Let's see.'")
    # Has sep included per guidelines.
    summary_early = get_input("Like a summary? 1 = Yes, Other = No: ")
    if summary_early == 1:
        print("Your name's ", name_player, ", you're certain.", sep='')
        if race_select == 1:
            print("You are a Half-Orc. How scary.")
        elif race_select == 2:
            print("You are a Human. How tame.")
        else:
            print("You are a Halfling. How tiny.")
        if class_select == 1:
            print("Fighter: strength. Saves: strength, constitution.")
        elif class_select == 2:
            print("Rogue: dexterity. Saves: dexterity, intelligence.")
        else:
            print("Wizard: intelligence. Saves: intelligence, wisdom.")
    else:
        print("'Moving on then,' says the figure. 'We can ask again later.'")
    # Explanation of dice rolling.
    print(" ")
    print("The figure produces a bag.")
    print("'Let's decide your fate.'\n'How strong are you? How smart?'")
    continue_key_press()
    print("Out of the bag, the figure pulls four six-sided dice.")
    print("'You will roll these 6 times.'")
    continue_key_press()
    print("'We will add the total of the highest 3 dice six times.'")
    print("'Each sum can be used as one of your 6 ability scores.'")
    continue_key_press()
    # This is due to Dungeons and Dragons etiquette.
    print("NOTE: You are not allowed to re-roll. No cheating, please.")
    continue_key_press()
    # Wanted to give the player an option to use their own dice.
    print("Use your own dice? Hit any option other than 1.")
    print("If using your own dice, end results will be blanks.")
    question_roll = get_input("Roll the dice by pressing 1: ")
    # Calls the dice roll function and passes the user's request to roll.
    dice_roll = roll_six_side_die_four_times(question_roll)
    print(dice_roll)
    # Asks the user to do their own math in case they use their own dice.
    roll_one = get_input("Enter the sum of the three highest values: ")
    continue_key_press()
    print("The figure says, 'Easy, right?")
    print("If you are using your own dice, enter anything but 1.")
    # This is due to Dungeons and Dragons etiquette.
    print("REMINDER 1: You are not allowed to re-roll.")
    print("REMINDER 2: If using your own dice, end results will be blanks.")
    # Same as above process but now does it five times.
    # Still counts off the rolls if they are using their own dice.
    # This allows the user to keep track of their rolls regardless.
    question_roll_two = get_input("Roll five more times by pressing 1: ")
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_two = get_input("Enter the sum of the three highest values: ")
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_three = get_input("Enter the sum of the three highest values: ")
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_four = get_input("Enter the sum of the three highest values: ")
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_five = get_input("Enter the sum of the three highest values: ")
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_six = get_input("Enter the sum of the three highest values: ")
    continue_key_press()
    print("The figure scoops up the dice.\n'That was the last...'")
    continue_key_press()
    print("Your ability rolls are:")
    print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    # Makes sure the user keeps moving through the program regardless.
    print("NOTE: If you used your own dice, scores of 0 will display.")
    continue_key_press()
    print("NOTE: If you mistyped an answer, scroll up to see your rolls.")
    continue_key_press()
    print("The figure draws six cards.")
    print("And it says, 'You have six ability scores.'")
    print("Strength, dexterity, constitution...")
    print("... and intelligence, wisdom, & charisma.")
    print("'You will place each of your rolls into each category.'")
    continue_key_press()
    print("It is important to review your current character attributes.")
    summary_early = get_input("Like a summary? 1 = Yes, Other = No: ")
    # Summary for review.
    if summary_early == 1:
        print("Your name's ", name_player, ", you're certain.", sep='')
        if race_select == 1:
            print("You are a Half-Orc. How scary.")
        elif race_select == 2:
            print("You are a Human. How tame.")
        else:
            print("You are a Halfling. How tiny.")
        if class_select == 1:
            print("Fighter: strength. Saves: strength, constitution.")
        elif class_select == 2:
            print("Rogue: dexterity. Saves: dexterity, intelligence.")
        else:
            print("Wizard: intelligence. Saves: intelligence, wisdom.")
        print("Again, your ability rolls are:")
        print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    else:
        print("Moving on... Again, your ability rolls are:")
        print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    print(" ")
    print("'Enter the desired roll sum in each of the following statistics.'")
    player_str = get_input("Enter your strength: ")
    player_dex = get_input("Enter your dexterity: ")
    player_con = get_input("Enter your constitution: ")
    player_int = get_input("Enter your intelligence: ")
    player_wis = get_input("Enter your wisdom: ")
    player_cha = get_input("Enter your charisma: ")
    continue_key_press()
    # Prints the user's unique stats based on race selection.
    # Uses shortcuts and relational operators per guidelines.
    if race_select == 1:
        player_str += 2
        player_con += 1
        print(" ")
        print("'Such a strong Half-Orc, aren't we?'")
        # Contains end to put this all on one line per guidelines.
        print("Str:", player_str, "Dex:", player_dex, end=" ")
        print("Con:", player_con, "Int:", player_int, end=" ")
        print("Wis:", player_wis, "Cha:", player_cha)
    elif race_select == 2:
        player_str += 1
        player_dex += 1
        player_con += 1
        player_int += 1
        player_wis += 1
        player_cha += 1
        print(" ")
        print("'What a jack-of-all trades, eh, Human?'")
        print("Str:", player_str, "Dex:", player_dex, end=" ")
        print("Con:", player_con, "Int:", player_int, end=" ")
        print("Wis:", player_wis, "Cha:", player_cha)
    else:
        player_dex += 2
        print(" ")
        print("'I keep losing sight of you, little Halfling...'")
        print("Str:", player_str, "Dex:", player_dex, end=" ")
        print("Con:", player_con, "Int:", player_int, end=" ")
        print("Wis:", player_wis, "Cha:", player_cha)
    continue_key_press()
    print("The figure is pleased. It's cloak ruffles.")
    print("'Now, how much damage can you take?'")
    print("This is based on your class selection and your constitution.")
    continue_key_press()
    if class_select == 1:
        hit_die = 10
        # Greater than, less than, equal to, etc. per guidelines.
        # All below can be simplified, but must show *and* per guidelines.
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a beefy fighter.'")
        print("Your hit points are: ", hit_points)
    elif class_select == 2:
        hit_die = 8
        # All below can be simplified, but must show *and* per guidelines.
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a lithe rogue.'")
        print("Your hit points are: ", hit_points)
    else:
        hit_die = 6
        # All below can be simplified, but must show *and* per guidelines.
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a frail wizard.'")
        print("Your hit points are: ", hit_points)
    continue_key_press()
    print("The figure pauses for a moment.")
    # Not statement per guidelines.
    # Just a break for humor.
    x = hit_points
    if not x > 10:
        print("It says, 'You'll probably be fine...'")
        continue_key_press()
    else:
        print("It says, 'I'm a bit worried about you...'")
        continue_key_press()
    # Remaining operators used below per guidelines to assign equipment.
    print("The cloaked figure places the cards and dice back in the bag.")
    print("'You're about ready... but you need some equipment and... help.'")
    continue_key_press()
    print("The figure produces a crystal out of thin air.")
    print("'This is not all I can conjure... I need some information first.'")
    continue_key_press()
    print("The cloaked figure is going to ask you some questions.")
    print("Your answers will determine random boons you get for your quest.")
    continue_key_press()
    print("'Let us begin...'")
    print("'If you give me an incorrect answer, this will sway the results.'")
    continue_key_press()
    print("'But everything happens for a reason...'")
    continue_key_press()
    player_pet = get_input("Numeric value of your birth month?: ")
    player_tunic = get_input("What is your age?: ")
    player_henchman = get_input("How many siblings do you have?: ")
    player_deity = get_input("How tall are you? Nearest foot?: ")
    player_star = get_input("Numeric value of your birthdate?: ")
    continue_key_press()
    # Below can be simplified, but showing unsimplified per guidelines.
    # Exponential by 2 per guidelines.
    player_pet = player_pet ** 2
    if player_pet <= 10 and player_pet >= 60:
        player_pet = "Dog"
        print("You own a: ", player_pet)
    else:
        player_pet = "Cat"
        print("You own a: ", player_pet)
    # Below can be simplified, but showing unsimplified per guidelines.
    # Multiplies by 10 per guidelines.
    player_tunic = player_tunic * 10
    if player_tunic > 240 and player_tunic < 400:
        player_tunic = "Cold Resistant Tunic"
        print("You are wearing a: ", player_tunic)
    else:
        player_tunic = "Heat Resistant Tunic"
        print("You are wearing a: ", player_tunic)
    # Below can be simplified, but showing unsimplified per guidelines.
    # Divides by 10 per guidelines.
    player_henchman = player_henchman / 10
    if player_henchman > 0:
        player_henchman = "Demon"
        print("You are followed by a: ", player_henchman)
    else:
        player_henchman = "Spirit"
        print("You are followed by a: ", player_henchman)
    # Modulus per guidelines. Gives remainder.
    player_deity = player_deity * 666 % 10
    if player_deity < 5:
        player_deity = "Tyr"
        print("You worship: ", player_deity)
    else:
        player_deity = "Bane"
        print("You worship: ", player_deity)
    # Floor division per guidelines. Returns largest integer.
    player_star = player_star * 777 // 10
    if player_star > 500:
        player_star = "Northern Hemisphere"
        print("You were born under the: ", player_star)
    else:
        player_star = "Southern Hemisphere"
        print("You were born under the: ", player_star)
    # All the player's information has been entered by now.
    continue_key_press()
    print("The cloaked figure comes out of it's trance.")
    print("'Easy as that...'")
    print("It leans forward in the chair and grabs your hand.")
    continue_key_press()
    print("'I hope you are ready for your adventure...'")
    print("And with a shimmer in the air, the figure is gone.")
    print("You feel emboldened, like you know yourself better than before.")
    continue_key_press()
    # Generates the final character sheet.
    print("YOUR CHARACTER SHEET")
    print(" ")
    print("YOUR NAME:", name_player)
    if race_select == 1:
        print("RACE: HALF-ORC")
    elif race_select == 2:
        print("RACE: HUMAN")
    else:
        print("RACE: HALFLING")
    if class_select == 1:
        print("CLASS: FIGHTER")
    elif class_select == 2:
        print("CLASS: ROGUE")
    else:
        print("CLASS: WIZARD")
    print("STR: ", player_str, "DEX: ", player_dex, "CON: ", player_con)
    print("INT: ", player_int, "WIS: ", player_wis, "CHA: ", player_cha)
    print("HIT POINTS:", hit_points)
    print("PET:", player_pet)
    print("TUNIC:", player_tunic)
    print("HENCHMAN:", player_henchman)
    print("DEITY:", player_deity)
    print("BORN UNDER WHICH STARS:", player_star)
    continue_key_press()
    print("...")
    print("A familiar voice says, 'Good luck.'")
    print("And with that, thank you for generating your character with me.")
    print("This should be enough to get you started on D&D adventure.")
    # Final user input that closes the program on their own terms.
    input("Press any key to close the program, go back to the real world: ")


# CALL TO MAIN #
main()

# PyCharm used for debugging.
# Warnings are for simplification.
# Ignored warnings are a result of project guidelines.
