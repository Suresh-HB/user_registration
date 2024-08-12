'''
@Author: Suresh
@Date: 2024-08-10
@Last Modified by: Suresh
@Last Modified: 2024-08-10
@Title : Has exactly 1 Special Character
'''
import re
import myloggingfile as mlf

logger = mlf.logger_init("user_registration.ipynb")

def valid_first_name(first_name):
    """
    Description: Function to validate user first name as per the pattern.
    Parameters:
        first_name : User first name to be validated.
    Returns:
        res : True if the first name matches the pattern, False otherwise.
    """
    logger.info("Inside valid_first_name function")
    first_name_pattern = r'[A-Z][a-z]{2,}'
    res = bool(re.match(first_name_pattern, first_name))
    logger.debug("Validating the user first name according to pattern matching")
    logger.info("Returning the bool value to main function")
    return res

def valid_last_name(last_name):
    """
    Description: Function to validate the user's last name according to the pattern.
    Parameters:
        last_name : User last name to be validated.
    Returns:
        result : True if the last name matches the pattern, False otherwise.
    """
    logger.info("Started valid_last_name function")
    last_name_pattern = r'[A-Z][a-z]{2,}'
    result = bool(re.match(last_name_pattern, last_name))
    logger.debug("Validating the user last name according to pattern matching")
    logger.info("Returning the bool value to main function")
    return result

def valid_email_id(email):
    """
    Description: Function to validate the user email id according to the pattern.
    Parameters:
        email : User email id to be validated.
    Returns:
        result : True if the email id matches the pattern, False otherwise.
    """
    logger.info("Started valid_email_id method")
    email_pattern = r'^[a-zA-Z.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    res = bool(re.match(email_pattern, email))
    logger.debug("Validating the user email id according to pattern matching")
    return res

def mob_num_valid(mob_num):
    """
    Description: Function to validate the user mobile number according to the pattern.
    Parameters:
        mob_num : User mobile number to be validated.
    Returns:
        result : True if the mobile number matches the pattern, False otherwise.
    """
    logger.info("Started mob_num_valid method")
    pattern = r'^\d{2} \d{10}$'
    mob_res = bool(re.match(pattern, mob_num))
    logger.debug("Validating the user mobile number according to pattern matching")
    return mob_res

def valid_password(password):
    """
    Description: Function to validate the user password according to the pattern.
    Parameters:
        password : User password to be validated.
    Returns:
        result : True if the password matches the pattern, False otherwise.
    """
    logger.info("Started valid_password method")
    # Rule1: Minimum 8 characters
    # Rule2: At least one uppercase letter
    # Rule3: At least one numeric digit
    # Rule4: Exactly one special character
    password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
    special_char_count_pattern = r'^[A-Za-z\d]*[@#$%^&+=][A-Za-z\d]*$'
    
    # Check the basic password rules
    pass_res = bool(re.match(password_pattern, password))
    
    # Check the special character count
    special_char_count = len(re.findall(r'[!@#$%^&*()_+={}\[\]|\\:;"\'<>,.?/~`-]', password))
    special_char_res = (special_char_count == 1)
    
    logger.debug("Validating the user password according to pattern matching")
    
    return pass_res and special_char_res

def main():
    logger.info("Started main function")

    first_name = input("Enter your first name: ")
    logger.debug(f"Taking first name as input from the user: {first_name}")

    last_name = input("Enter last name of the user: ")
    logger.debug(f"Taking last name as input from the user: {last_name}")

    email = input("Enter your email id: ")
    logger.debug(f"Taking email id as input from the user: {email}")

    mob_num = input("Enter your mobile number (format: XX XXXXXXXXXX): ")
    logger.debug(f"Taking mobile number as input from the user: {mob_num}")

    password = input("Enter your password: ")
    logger.debug(f"Taking password as input from the user")

    first_name_valid = valid_first_name(first_name)
    last_name_valid = valid_last_name(last_name)
    email_valid = valid_email_id(email)
    mob_num_valid_result = mob_num_valid(mob_num)
    password_valid = valid_password(password)

    if first_name_valid:
        logger.info(f"User Entered First name = '{first_name}' is valid")
    else:
        logger.info(f"User entered First name = '{first_name}' is invalid")

    if last_name_valid:
        logger.info(f"User Entered Last name = '{last_name}' is valid")
    else:
        logger.info(f"User entered Last name = '{last_name}' is invalid")

    if email_valid:
        logger.info(f"User Entered Email id = '{email}' is valid")
    else:
        logger.info(f"User entered Email id = '{email}' is invalid")

    if mob_num_valid_result:
        logger.info(f"User Entered Mobile number = '{mob_num}' is valid")
    else:
        logger.info(f"User entered Mobile number = '{mob_num}' is invalid")

    if password_valid:
        logger.info(f"User Entered Password is valid")
    else:
        logger.info(f"User entered Password is invalid")

    if not (first_name_valid and last_name_valid and email_valid and mob_num_valid_result and password_valid):
        logger.info("Pattern Matches Fails:")
        if not first_name_valid:
            logger.info(f"First name = '{first_name}' did not match pattern")
        if not last_name_valid:
            logger.info(f"Last name = '{last_name}' did not match pattern")
        if not email_valid:
            logger.info(f"Email id = '{email}' did not match pattern")
        if not mob_num_valid_result:
            logger.info(f"Mobile number = '{mob_num}' did not match pattern")
        if not password_valid:
            logger.info(f"Password did not match pattern")

    logger.info("Exit main function")

if __name__ == '__main__':
    main()
