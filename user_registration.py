'''

@Author: Suresh
@Date: 2024-08-08
@Last Modified by: Suresh
@Last Modified: 2024-08-08 
@Title : As a User need to enter a valid First Name
'''

import re
import myloggingfile as mlf
logger = mlf.logger_init("user_registration.ipynb")

def valid_frist_name(frist_name):

    """
    Description: Function to validating user frist name as per the pattern. 
    Parameters:
        frist_name : Function taking the user name as a parameter for match the pattern.
    Returns:
        res : returning the bool value to main function 
    """

    logger.info(" inside valid_frist_name function")

    frist_name_pattern = r'[A-Z][a-z]{2,}'
    res = bool(re.match(frist_name_pattern, frist_name))
    logger.debug(f" validating the user frist name according to pattern matching = '{frist_name_pattern}'")
    logger.info(" returning the bool value to main function")
    return res


def main():
    logger.info(" Started main function")

    frist_name = input(" Enter your frist name : ")
    logger.debug(f" Taking frist name as input from the user : {frist_name}")
    
    logger.info(" calling valid_frist_name function")
    res = valid_frist_name(frist_name)

    if res == True:
        logger.info(f" User entered frist name = '{frist_name}' is valid")
    else:
        logger.info(f" User entered frist name = '{frist_name}' invalid")

    logger.info(" exit main function")


if __name__=='__main__':
    main()