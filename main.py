# Isaac Francisco Marte
# Date: 11/15/2021
# Course: SDEV 300

"""Application provides several functionalities from formatting phone numbers and zipcodes,
to creating 3x3 matrices and performing math operations on them, and encrypting passwords to test
on algorithm  websites. """

import hashlib
import numpy as np


# Function Called when user enters #4 in main menu
def hash_password_generator():

    """The hash password function request user to enter 10 different passwords and uses the
    hash module to encrypt the password. The passwords can then be  tested in a password cracker
     to test if the algorithm can figure it out"""

    psw_array = np.array([])  # creates a numpy array which stores each password entered

    # prints welcome message to user
    print('________Welcome to the Python Matrix Hash Password Generator Application _________')
    print('')

    # for loop which loops with a range of 1-10 which acquires 10 passwords from user
    for psw in range(0, 10):

        # Message to user to  Enter passwords for each iteration
        print(f'Enter Password {psw + 1} To Encode')
        psw = str(input())  # variable name stores value entered for psw within each iteration

        # conditional statement which ensures input is not blank or to long or short
        if psw == '' or 4 < len(psw) > 18:
            print("Passwords entered must not contain, left blank and 4 to 18 characters long")
            hash_password_generator()

        # Appends input so long as the if conditions are not met
        else:
            psw_array = np.append(psw_array, psw)  # appends the psw to array list

    # Loop which iterates through array and displays the values
    for psw in psw_array:
        # prints the encrypted password using Hash Sha256 and Md5
        print(f'Password: {psw} ')
        print(f'Hash Sha256 Encoded Password: {hashlib.sha256(str.encode(psw)).hexdigest()}')
        print(f'Hash md5 Encoded: {hashlib.md5(str.encode(psw)).hexdigest()}\n')

    print(psw_array, '\n')  # prints the entire psw_array elements/passwords


# Function called when user enters #3 in the main menu function
def create_matrices():

    """Function which allows user to create 2, 3x3 matrices and perform operations
    between them such as +, -, * via its own selection menu within the function."""

    matrix = np.array([], dtype='int64')  # array for values of first matrix
    matrix2 = np.array([], dtype='int64')  # array for values of first matrix

    # while loop runs own selection menu within function
    while True:

        # try and except handle value error if input for matrices not a number
        try:

            # loop which iterates 9 times for input of each value of the 3 x 3 1st Matrix
            for i in range(0, 9):

                # print statement which request user to enter the password for each iteration
                print(f'Enter your {i + 1} element for First 3x3 Matrix')
                number = int(input())  # variable holds value in each iteration entered
                matrix = np.append(matrix, number)  # appends value to the matrix
            matrix = matrix.reshape(3, 3)  # Re-initiates matrix array to reshape it to a 3x3
            print('')

            # loop which iterates 9 times for input of each value of the 3 x 3 2nd Matrix
            for j in range(0, 9):
                print(f'Enter Your {j + 1} element for Second 3x3 Matrix')
                element = int(input())  # variable holds value in each iteration entered
                matrix2 = np.append(matrix2, element)  # appends values to matrix 2
            matrix2 = matrix2.reshape(3, 3)  # Re-initiates matrix 2 array to reshape it to a 3x3

        # prints if value for a matrices is not a number
        except ValueError:
            print('Values entered must all be numbers for each Matrix\n')
            create_matrices()

        # try and accept catch value error if value for selection menu is not a number
        try:

            # Selection menu for matrices operations
            print('_____________ Welcome to the Python Matrix Operations Application _____________')
            print('Make a selection on the operation you would like to perform on your matrices')
            print("1. Add ")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Element by Element Multiplication")
            print("5. Restart Matrix Operation Function")
            print("9. Return to Main Menu")
            selection = int(input())
            print('')

            if selection == 1:
                added_total = np.add(matrix, matrix2)  # adds matrix 1 and 2
                column_mean = added_total.mean(axis=0)  # calculates mean of column values
                row_mean = added_total.mean(axis=1)  # calculates mean of Row values

                # Final output to user once matrices operation is complete
                print(f'... Sum of Matrices ... \n{added_total}\n '
                      f''f'\n... Transpose of Matrix ... {added_total.T}\n '
                      f'\nMean values for the row and column'
                      f'\nRow:{added_total.mean(column_mean)} '
                      f'\nColumn: {row_mean} \n')
                main_menu()

            elif selection == 2:
                subtract_total = np.subtract(matrix, matrix2)  # Subtracts matrix 1 & 2
                column_mean = subtract_total.mean(axis=0)
                row_mean = subtract_total.mean(axis=1)

                print(f'... Subtraction of Matrices ... \n{subtract_total} '
                      f'\n... Transpose of Matrix ... {subtract_total.T} '
                      f'\nMean values for the row and column'
                      f'\nRow:{row_mean} '
                      f'\nColumn: {column_mean} \n')
                main_menu()

            elif selection == 3:
                multiply_total = np.matmul(matrix, matrix2)  # multiply matrix 1 & 2 together
                column_mean = multiply_total.mean(axis=0)
                row_mean = multiply_total.mean(axis=1)

                print(f'... Multiplication of Matrices ... \n{multiply_total} '
                      f'\n... Transpose of Matrix ... {multiply_total.T} '
                      f'\nMean values for the row and column'
                      f'\nRow:{row_mean} '
                      f'\nColumn: {column_mean} \n')
                main_menu()

            elif selection == 4:
                multiply_total = matrix * matrix2  # Multiplies matrix 1 & 2 element by element
                column_mean = multiply_total.mean(axis=0)
                row_mean = multiply_total.mean(axis=1)

                print(f'Multiplication of Matrices \n{multiply_total} '
                      f'\nTranspose of Matrix \n{multiply_total.T} '
                      f'\nMean values for the row and column'
                      f'\nRow:{row_mean} '
                      f'\nColumn: {column_mean} \n')
                main_menu()

            # if user enters #9 returns to main menu
            elif selection == 9:
                print('Thank you for visiting, come back soon to the Matrices Application')
                main_menu()

            else:
                print('Invalid Number Entered, \tTry Again!\n')

        # prints when user enters is not a number for the selection menu
        except ValueError:
            print('Input must be a digit of 1, 2, 3, 4 or 9\n')


# Function called when user enters #2 in main menu
def format_zipcode():

    """When function is initiated a welcome message to the user is displayed followed by a
    request for the user to enter the zipcode they want to format. Once the zipcode is entered to
    complete the format it request the user to enter the delivery route number that follows the
    zipcode. The conditional statement verifies the length of the values and to ensure they are
    numbers and displays the values should it meet the criteria. """

    # Welcome message to user
    print('____________ Welcome to Format Zip Code Application ____________\n')

    # request user to enter 5 digits of the zipcode
    print('Enter your 5 digit zipcode')
    zip_code = input()

    # request user to enter the delivery route 4 digit value
    print('Enter the 4 digit delivery route number of the your zipcode')
    delivery_route = input()

    # conditional statement checks zipcode and delivery route values meet criteria
    if zip_code.isdigit() \
            and delivery_route.isdigit() \
            and len(zip_code) == 5 \
            and len(delivery_route) == 4:
        print('Your Formatted Zipcode\n')
        print(f'{zip_code[0:6]}-{delivery_route[0:5]}')

    # if the length of numbers for zipcode or is contains a non numeric value message prints
    else:
        print('Your zipcode number is not in correct format. Please renter:\n')
        format_zipcode()  # recalls the function


# Function called when user enters #1 in main menu.
def format_phone_number():

    """ The format phone number application request user ot enter a 10 digit number
     and formats the values to standard phone number style (XXX)-XXX-XXXX.
     If user enters a value that is not a digit and composed of 10 digits a
     message will print to user to try again"""

    # Main message to user for phone number function
    print('_________ Format Phone Number Matrix Application Function _________')

    # Request user to enter a phone number and stores it under the phone_number variable
    print('Enter Phone Number')
    phone_number = str(input())

    # prints formatted phone number entered, if it is composed of 10 numbers
    if phone_number.isdigit and len(phone_number) == 10:
        print("Your Formatted Phone Number\n")
        print(f'({phone_number[0:3]})-{phone_number[3:6]}-{phone_number[6:]}\n')

    # condition runs if value entered did not meet criteria and recalls function
    else:
        print('Your phone number is not in correct format. Please renter:\n')
        format_phone_number()  # recalls function

    print('')  # next line space


# Main menu/ Interface to user
def main_menu():

    """The main menu function acts as the interface/ user selection menu which based
    on value entered will call upon the appropriate function to proceed with the
    program. Should the input be invalid the appropriate message is displayed to user
    and the function reiterates until an appropriate selection is made.
    The only way to terminate program within the application is to enter #9
    within this function"""

    # loop used to run interface to user
    while True:

        # try & except used to handle value error from non numeric input
        try:
            # print statements which show statements to user for them to make selection
            print('***************** Welcome to The Matrix Game Application *****************')
            print('Note: Enter the appropriate number, based on the function you wish to perform')
            print('1. Format Phone Number')
            print('2. Format Zip Code')
            print('3. Create two 3 x 3 Matrices & Perform Operations')
            print('4. Password Cracker')
            print('9. Exit Program')
            selection = int(input())  # Stores selection value
            print('')

            if selection == 1:
                format_phone_number()  # Calls format phone number function when #1 entered

            elif selection == 2:
                format_zipcode()  # Calls format zipcode function when #2 entered

            elif selection == 3:
                create_matrices()  # Calls create matrices function when #3 is entered

            elif selection == 4:
                hash_password_generator()  # calls hash password generator when #4 is entered

            # Terminates while loop/program when #9 is entered
            elif selection == 9:
                print('********** Thank You For Playing The Matrix Game Application **********')
                print('Please come back and play!')
                break

            # prints message to user when an incorrect number is entered
            else:
                print('Number entered is not Valid!\n')

        # prints when user enters a value that is not a number
        except ValueError:
            print('Input must be a digit of 1, 2, 3, 4 or 9\n')


# Initiates main menu function when program is first run
if __name__ == '__main__':
    main_menu()
