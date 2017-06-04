"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count_dict = {}

    word_list = phrase.split(' ')

    for word in word_list:
        word_count = word_list.count(word)
        word_count_dict[word] = word_count
    return word_count_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_dict = {
        'Watermelon': 2.95,
        'Cantaloupe': 2.50,
        'Musk': 3.25,
        'Christmas': 14.2
        }

    if melon_name in melon_dict:
        return melon_dict[melon_name]
    else:
        return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    result_list = []
    letter_count_dict = {}

    word_lengths = list(set([len(word) for word in words]))

    for word_length in word_lengths:
        # Using list comprehension
        letter_count_dict[word_length] = [word for word in words if len(word) == word_length]

        # Using nested loop instead of list comprehension:

        # letter_count_dict[word_length] = []
        # for word in words:
        #     if len(word) == word_length:
        #         letter_count_dict[word_length].append(word)

    for key in sorted(letter_count_dict.keys()):
        value = letter_count_dict[key]
        result_list.append((key, sorted(value)))

    return result_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'man': 'matey',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'restroom': 'head',
        'my': 'me',
        'is': 'be'
    }

    new_phrase = []
    word_list = phrase.split(' ')
    for word in word_list:
        if word not in english_to_pirate:
            new_phrase.append(word)
        elif word in english_to_pirate:
            new_phrase.append(english_to_pirate[word])
    return ' '.join(new_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # I couldn't figure out why we would use a dictionary here
    # seems more complicated because of the required order
    # my attempt at using dictioanry commented out below starting on line 252

    result_list = []

    current_word = names[0]
    result_list.append(names[0])
    while len(names) > 0:
        next_letter = current_word[-1]
        names.remove(current_word)
        for name in names:
            if name[0] == next_letter:
                result_list.append(name)
                current_word = name
                break
        if current_word not in names:
            break

    return result_list

    # result_dict = {}

    # current_word = names[0]
    # result_dict[current_word] = current_word
    # for name in names:
    #     next_letter = current_word[-1]
    #     for name in names:
    #         if name[0] == next_letter and name not in result_dict.values():
    #             result_dict[current_word] = name
    #             current_word = name
    #             print current_word
    #             break

#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
