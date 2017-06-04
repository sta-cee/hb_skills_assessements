"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_hometown(hometown_name):
    """ Returns True if town_name is 'Newport Beach'."""

    return hometown_name == 'Newport Beach'


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def combine_first_last_name(first_name, last_name):
    """ Takes first and last name and returns the concatenation of the two names. """

    return '%s %s' % (first_name, last_name)

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def print_greeting_check_hometown(hometown, first_name, last_name):
    """ Takes three strings as parameters. Uses is_hometown()
    helper function to determine which custom message to print,
    full_name supplied by combine_first_last_name(). """

    full_name = combine_first_last_name(first_name, last_name)

    if is_hometown(hometown):
        print 'Hi, %s here. We\'re from the same place!' % (full_name)
    else:
        print 'Hi %s here. I\'d like to visit %s' % (full_name, hometown)


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    # if fruit == 'strawberry' or fruit == 'raspberry' or fruit == 'blackberry':
    #     return True
    # else:
    #     return False

    return fruit in ['strawberry', 'raspberry', 'blackberry']


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit):
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    new_list = lst[:]
    new_list.append(num)
    return new_list


def calculate_price(item_base_price, state, tax=.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    tax_total = item_base_price * tax
    total_cost = item_base_price + tax_total

    if state == 'CA':
        ca_tax = total_cost * .03
        total_cost = total_cost + ca_tax
    elif state == 'PA':
        total_cost = total_cost + 2
    elif state == 'MA':
        if total_cost < 100:
            total_cost = total_cost + 1
        elif total_cost >= 100:
            total_cost = total_cost + 3
    return total_cost


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

def add_args_to_list(lst, *args):
    """ Takes list and any number of additional args, adds arg(s) to list, returns entire list. """

    for arg in args:
        lst.append(arg)
    return lst


#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def output_word_tuple(word):
    def multiply_word(single_word):
        return single_word * 3
    return (word, multiply_word(word))

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
