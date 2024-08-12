'''
@Author: Suresh
@Date: 2024-08-09
@Last Modified by: Suresh
@Last Modified: 2024-08-09 
@Title : As a User need to enter a valid email

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

def main():
    logger.info("Started main function")

    first_name = input("Enter your first name: ")
    logger.debug(f"Taking first name as input from the user: {first_name}")

    last_name = input("Enter last name of the user: ")
    logger.debug(f"Taking last name as input from the user: {last_name}")

    email = input("Enter your email id: ")
    logger.debug(f"Taking email id as input from the user: {email}")

    
    first_name_valid = valid_first_name(first_name)
    last_name_valid = valid_last_name(last_name)
    email_valid = valid_email_id(email)

 
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


    if not (first_name_valid and last_name_valid and email_valid):
        logger.info("Pattern Matches Fails:")
        if not first_name_valid:
            logger.info(f"First name = '{first_name}' did not match pattern")
        if not last_name_valid:
            logger.info(f"Last name = '{last_name}' did not match pattern")
        if not email_valid:
            logger.info(f"Email id = '{email}' did not match pattern")

    logger.info("Exit main function")

if __name__ == '__main__':
    main()
