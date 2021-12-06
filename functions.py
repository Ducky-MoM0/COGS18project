import webbrowser

def create_password():
    """ Use create_password to create a password that is atleast 8 characters long
    
    Parameters
    ----------
    no_input : 
        will ask user to create password in format of string when function is used
    
    Returns
    -------
    user_output : str
        user_input string to be returned
    """
    user_input = input('Create password:\t ')
    #checks that user input has length of 8 characters or more
    while len(user_input) < 8:
        rules = input('Password invalid. Would you like view password rules?')
        rules = rules.upper()
        if rules == 'YES':
            print('Password needs atleast 8 characters long.')
            user_input = input('Create password:\t ')
        else:
            user_input = input('Create password:\t ')
            
    return user_input

def secret_file():
    """ Use secret file to make user input into key and a file as value for dictionary
    
    Parameters
    ----------
    no_input:
    
    return
    ------
    lock_file : dictionary
        lock_file dictionary returned with user input as key and file as value
    """
    secret_file = 'https://youtu.be/dQw4w9WgXcQ'
    password = create_password()
    lock_file = {password : secret_file}
    
    return lock_file 

def access_file():
    """ User only needs access_file to access lock and unlock mystery file
    
    Parameters
    ----------
    no_input:
    
    return
    ------
    output : Boolean
        Output verifies that user input matches the key and gives acces to mystery file
    """
    locked_file = secret_file()
    # allows input for dictonary to be accessed as key, and value 
    # respecitively as a string
    key, value = next((str(k), str(v)) for k, v in locked_file.items())
    enter_password = input('Enter password: \t')
    
    #compare enter_password to key of dictionary to verify that they match
    while enter_password != key:
        enter_password = input('Incorrect. Try again: \t')
    output = webbrowser.open_new_tab(value)
    
    return output

                       