import random

def main (): 

    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(1,"past")} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(1,"present")} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(2,"future")} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"past")} {get_prepositional_phrase(2)}')
    print(f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"present")} {get_prepositional_phrase(2)}')
    print(f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"future")} {get_prepositional_phrase(2)}')


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1: 
        noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else: 
        noun=  ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    nouns = random.choice(noun)
    return nouns


def get_verb(quantity, tense):

    if tense == "past": 
        verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense =="present" and quantity == 1: 
        verb=  ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1: 
        verb=  ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense =="future": 
        verb=  ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    verbs = random.choice(verb)
    return verbs

    """Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

def get_preposition(phrase):
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    if phrase >= 1:
        preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    prepositions = random.choice(preposition)
    return prepositions
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1: 
        prep_phrase = (f' {get_preposition(1)} {get_determiner(1)} {get_noun(1)}') 
    else: 
        prep_phrase = (f'{get_preposition(1)} {get_determiner(2)} {get_noun(2)}') 
    return prep_phrase


main() 