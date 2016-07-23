# 1. In the very first section the user can chose the difficulty level#
easiest_level = '''A ___1___ is a programmable machine designed to automatically carry out a ___2___ of arithmetic or logical operations.
                The first use of the word "___1___" was recorded in 1613, referring to a person who carried out calculations, or ___3___,
                and the word continued with the same meaning until the middle of the 20th century.
                From the end of the 19th century the word began to take on its more familiar meaning, a machine that carries out ___3___.
                Later ___4___s created new applications to help users perform many things from word processing to image editing.'''
easiest_answers = ['computer', 'sequence', 'computations', 'developer']

easy_level = '''___1___ and Juliet fall in love at a party. But they come from families Capulet and ___2___ which hate each other.
            They are sure they will not be allowed to ___3___, so they ___3___ in secret instead.
            Before their wedding night ___1___ kills Juliet's cousin and he is forced to leave her.
            Juliet's parents told her she must ___3___ Paris. She refuses in the beginning, but later agrees because she plans to fake her ___4___
            and escape to be with ___1___ forever. Frair Laurence gives Juliet a ___5___ potion, She appears to be ___4___,
            but ___1___ had no idea it's fake, so he killed himself.
            When Juliet finally wakes up, she discovers that ___1___ is ___4___ and then kills herself.'''
easy_answers = ['Romeo', 'Montague', 'marry', 'dead', 'sleeping']

moderate_level = '''Mr. ___1___ is a series of fourteen 25-minute episodes written by and starring Rowan ___2___.
            This British situation comedy television program is based on a character originally developed by ___2___.
            while he was studying for his master's degree at Oxford University. The series features ___3___ situations occurring
            in the life of Mr. ___1___. The latter was described by ___2___ as "a ___4___ in a grown man's body".
            Mr. ___1___ tries to solve various ___5___ presented by everyday tasks and often causes disruption in the process.
            ___1___ rarely speaks, and the largely physical humor of the series is derived from his inter___6___ with other people
            and his un___7___ solutions to situations.'''
moderate_answers = ['Bean', 'Atkinson', 'funny', 'child', 'problems', 'actions', 'usual']

hard_level = ''' ___1___s are often regarded as one of Earth's most intelligent animals. They are social creatures,
            living in ___2___ of up to a dozen individuals. In places with a high abundance of food, ___2___ can merge temporarily,
            forming a superpod; such groupings may exceed 1,000 ___1___s. They ___3___ using a variety of clicks,
            whistle-like sounds and other vocalizations. Membership in ___2___ is not rigid; interchange is common. ___1___s can, however,
            establish strong social bonds; they will stay with injured or ill individuals, even ___4___ them to breathe by bringing them
            to the surface if needed. This altruism does not appear to be limited to their own ___5___.
            The ___1___ Moko in New ___6___ has been observed guiding a female Pygmy Sperm Whale together with her calf out of shallow water
            where they had stranded several times. They have also been seen ___7___ swimmers from sharks by ___8___ circles around the swimmers
            or charging the sharks to make them go away.'''
hard_answers = ['Dolphin', 'pods', 'communicate', 'helping', 'species', 'Zealand', 'protecting', 'swimming',]

hardest_level = '''The modern ___1___ was originally invented in Naples, Italy but the word ___1___ is ___2___ in origin,
            derived from the ___2___ word pektos meaning solid or clotted. The ancient ___2___s covered their bread with oils, herbs and cheese.
            The first major innovation that led to flat bread ___1___ was the use of ___3___ as a topping.
            It was common for the ___4___ of the area around Naples to add ___3___ to their yeast-based flat bread, and so the ___1___ began.
            While it is difficult to say for sure who invented the ___1___, it is however believed that modern ___1___ was first made
            by baker Raffaele Esposito of Naples. In fact, a popular urban legend holds that the archetypal ___1___, ___1___ ___5___,
            was invented in 1889, when the Royal Palace of Capodimonte commissioned the Neapolitan ___1___iolo Raffaele Esposito
            to create a ___1___ in honor of the visiting Queen ___5___.
            Of the three different ___1___s he created, the Queen strongly preferred a pie swathed in the colors of the Italian ___6___:
            red (___3___), green (___7___), and white (mozzarella). Supposedly, this kind of ___1___ was then named after the Queen as ___1___ ___5___.
            Later, the dish has become ___8___ in many parts of the world:
            The first ___9___, Antica ___9___ Port'Alba, was opened in 1830 in Naples.
            In North America, The first ___9___ was opened in 1905 by Gennaro Lombardi at 53 1/3 Spring Street in New York City.
            The first ___1___ Hut, the ___10___ of ___1___ restaurants appeared in the United States during the 1930s.
            Nowadays, many varieties of ___1___ exist worldwide, along with several dish variants based upon ___1___.'''
hardest_answers = ['pizza', 'Greek', 'tomato', 'poor', 'Margherita', 'flag', 'basil', 'popular', 'pizzeria', 'chain']

blanks = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___', '___7___', '___8___', '___9___', '___10___']


def select_level(easiest_level, easiest_answers, easy_level, easy_answers, moderate_level, moderate_answers, hard_level, hard_answers, hardest_level, hardest_answers):
    """User is required to select level

    Function select_level takes arguments which are all refering to strings, the actual text of the game will be played:
    easiest_level, easy_level, etc. and others containing lists of the correct answers for each level: easiest_answers, easy_answers, etc.
    The user required to provide input level_selection in order to select the difficulty level of the game will be played.
    Once it's done, it returnes the the selected level along with the particular text(level) and particular answers of the game."""
    while True:
        level_selection = raw_input('Please type in your chosen difficulty level from easiest / easy / moderate / hard / hardest:')
        print ''
        print "You are on level:", level_selection
        print ''
        if level_selection == "easiest":
            return easiest_level, easiest_answers, level_selection
        elif level_selection == "easy":
            return easy_level, easy_answers, level_selection
        elif level_selection == "moderate":
            return moderate_level, moderate_answers, level_selection
        elif level_selection == "hard":
            return hard_level, hard_answers, level_selection
        elif level_selection == "hardest":
            return hardest_level, hardest_answers, level_selection
        else:
            print 'Chose from the existing difficulty levels:'
            continue

def your_level():
    """ Assigns varriables to others and displays the text.

    Assigns the particul level, answers and level selection to variavles(level, answers, level_selection)
    and make the text appear so it is ready for the user to start the game."""
    level, answers, level_selection = select_level(easiest_level, easiest_answers, easy_level, easy_answers, moderate_level, moderate_answers, hard_level, hard_answers, hardest_level, hardest_answers)
    print level
    return level, answers, level_selection

# 2. Play the game #

def introduction ():
    """ This funtion greets the user and displays the version."""
    print'  '
    print 'Welcome to my Fill-in-the-blanks style quiz!'
    print 'version 1, 2016'
    print'  '

def guess_check(count, level, answers, level_selection):
    ''' Requires guesses from the user, check them and replaced the blanks.

    Guess check function takes inputs: count, level(text of the selected level),
    answers(a list which contains all the correct answers for the particular text), level_selection(selected level)
    and requires an additional, the guess from the user.
    If the guess is not correct, the user has to pass in another guess and it prints Try again!
    If it is correct it replaces the word with the correct answer as the output and prints correct along with the selected level.'''
    guess = None
    while guess != answers[count]:
        guess = raw_input('Please fill the blank with your guess:')
        if guess != answers[count]:
            print "Try again!"
        else:
            level = level.replace(blanks[count], answers[count])
            print guess, "is correct!"
            print "You are on level:", level_selection
            print ''
            print level
            return level

def fill_in_the_blanks():
    ''' Based on user's choices fill the blank spaces with and gives back the completeted text.

    It automatically greats the user(introduction).
    Fill_in_the_blanks function expect the user to select a level(your_level & select_level) of the game at first place
    and a function(guess_check) expect another input, guess from the user and the same function examines this guess
    whether it's correct. If it is, it replaces the blank with the correct answer and returns the text(level) with it's replaced blanks
    as the output. In other case the player have to guess again. It does not stop until all the blanks replaces with right answers'''
    introduction ()
    level, answers, level_selection = your_level()
    count = 0
    print '         '
    answers_number = len(answers)
    while count < answers_number:
        print ''
        print 'blank: ', blanks[count]
        level = guess_check(count, level, answers, level_selection)
        count += 1
        if count == answers_number:
            print ''
            print "Congratulations, you've filled out all the blanks!"
fill_in_the_blanks()
