'''
@Author: Suresh
@Date: 2024-08-09
@Last Modified by: Suresh
@Last Modified: 2024-08-09 
@Title : As a user need to enter a valid First Name and Last Name 

'''

import re
import myloggingfile as mlf
logger = mlf.logger_init("user_registration.ipynb")

def valid_frist_name(frist_name):

    """
    Description: Function to validating user frist name as per the pattern. 
    Parameters:
        frist_name : User frist name to be validated.
    Returns:
        res : True if the frist name matches the pattern, False otherwise. 
    """

    logger.info(" inside valid_frist_name function")

    frist_name_pattern = r'[A-Z][a-z]{2,}'
    res = bool(re.match(frist_name_pattern, frist_name))
    logger.debug(f" validating the user frist name according to pattern matching ")
    logger.info(" returning the bool value to main function")
    return res


def valid_last_name(last_name):

    """
    Description: Function to validate the user's last name according to the pattern.
    Parameters:
        last_name : User last name to be validated.
    Returns:
        result : True if the last name matches the pattern, False otherwise.
    """

    logger.info(" Started valid_last_name function")
    last_name_pattern = r'[A-z][a-z]{2,}'
    result = bool(re.match(last_name_pattern,last_name))
    logger.debug(f" validating the user last name according to pattern matching")
    logger.info(" returning the bool value to main function")
    return result


def main():
    logger.info(" Started main function")

    frist_name = input(" Enter your frist name : ")
    logger.debug(f" Taking frist name as input from the user : {frist_name}")

    last_name = input("Enter last name of the user : ")
    logger.debug(f" Taking last name as input from the user : {last_name}")

    logger.info(" calling valid_frist_name method")
    res = valid_frist_name(frist_name)

    if res == True:
        
        logger.info(" calling valid_last_name method")
        result = valid_last_name(last_name)
        if result:
            logger.info(f" User Entered Frist name = '{frist_name}' is valid")
            logger.info(f" User Entered Last name = '{last_name}' is valid")
        else:
            logger.info(f" User Entered Last name = '{last_name}' is invalid")

    else:
        logger.info(f" User entered Frist name = '{frist_name}' invalid")

    logger.info(" exit main function")


if __name__=='__main__':
    main()