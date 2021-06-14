def quit(user_input):
    '''Returns true when the user wants to quit.'''
    return user_input.upper() == 'X'

def get_number(which_number):
    '''
    Prompts the user to enter a number.  Returns the string input.
    which_number: specify 'first' or 'second'
     '''
    return input(f'Please enter the {which_number} number or X to exit: ')

def coprime(a, b):
    ''' Tests whether the numbers a and b are coprime. '''
    if a == 1 or b == 1:    # if either number is 1, they are coprime
        return True
    if a == b:              # if the numbers are equal, they are not coprime (factors are 1 and the number itself)
        return False
    if a % 2 == 0 and b % 2 == 0:   # both numbers are even, so 2 is a common factor
        return False
    
    #TODO: calculate the Greatest Common Divisor
    
    return True
    

def coprime_test_loop():
    '''Repeatedly prompts for two number inputs until told to quit'''

    

    user_quit = False

    while not user_quit:
        first_number = get_number('first')
        user_quit = quit(first_number)

        if user_quit:
            print('Thanks for playing!')
            continue

        second_number = get_number('second')
        
        user_quit = quit(second_number)
        if user_quit:
            print('Thanks for playing!')
            continue

        is_coprime = coprime(int(first_number), int(second_number))
        output_string = 'The numbers ' + str(first_number) + ' and ' + str(second_number) + ' are '
        if not is_coprime:
            output_string += 'not '
        output_string += 'coprimes.'
        print(output_string)

coprime_test_loop()