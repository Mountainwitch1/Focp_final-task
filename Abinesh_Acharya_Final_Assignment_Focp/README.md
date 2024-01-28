**TASK 1**

  The BPP_Pizza_Calc function is a code for determining the entire cost of pizza orders at Beckett Plaza Pizza. 
  It starts by greeting users with a message and then goes through a sequence of input validations. Users are 
  requested to enter the number of pizzas they want to purchase, and a valid input.
  The function then asks whether delivery is necessary, if it's Tuesday, and if the consumer used the Beckett Plaza Pizza app, 
  requiring acceptable 'yes' or 'no' replies for each question.The pizza pricing is then computed using the user's input, 
  and a delivery fee is established, with free delivery available for purchases of five or more pizzas. Additional discounts
  are offered if it is Tuesday or if the client uses the app. The final total price is rounded to two decimal places and shown,
  resulting in a user-friendly and efficient method of computing pizza expenses at Beckett Plaza Pizza. The feature encompasses the
  full pizza ordering process, offering clients an integrated and efficient service.


**TASK 2**

  This python program , cat_visit_log, analyzes a cat visitation log file using command-line inputs. The script initially determines 
  whether a command line parameter with the location to the log file is provided. If not, it returns an error message. It then attempts
  to read the contents of the chosen log file, handling any possible file not found issues and terminating with an appropriate message 
  if one is detected.
  
  After successfully reading the log file, the script initializes many variables to track data about cat visits. It goes over each line in
  the log file, skipping empty lines and finishing when it sees the "END" keyword. 
  
  Each non-empty line is then divided into event type ("OURS" for visits from the user's own cat and others for invading cats), entry time,
  and exit time. The duration of each visit is computed, and information such as the number of visits by the user's cat, the number of invading 
  cats sprayed with water, the total time spent in the home, the user's cat's average visit length, and the longest and shortest visit durations
  are updated.
  
  The script tackles potential issues due to incorrect log file formats by producing an error notice for each issue. Finally, it calculates the total time
  spent in the house in hours and minutes, the average visit duration of the user's cat, and publishes a summary of the log file analysis findings. The output 
  contains the number of visits by the user's cat, the number of invading cats drenched with water, the total time spent in the home, the user's cat's average 
  visit length, and the longest and shortest visit duration.


**TASK 3**

Overall the code that we have written in Task implements basic user management system where you create an account, delete an account, update password of an account nad login
to the existing account.
There has been use of file handling,loops,conditions,modules,exception handling and functions to make it as required.
In Main.py
The code implements a basic user management system. The create_new_user function takes a username, full name, and password, encrypts the password using ROT13, and stores
the user information in a "password.txt" file.
The retrieve_user_data function checks if a username already exists and returns the corresponding full name and encrypted password. 
The read_user_data and write_user_data functions handle reading from and writing to the "password.txt" file, respectively. 
The password encryption is performed using a simple ROT13 substitution cipher. Note that for real-world applications, more robust encryption methods and error handling would be necessary.

In login.py
The provided Python script, login.py, facilitates user authentication by comparing inputted credentials with those stored in a password file using the check_password function from the password_util module.

In the login function, the script reads the password file, iterates through each line, and extracts stored username and encrypted password. If the provided username matches and the password is validated using check_password, access is granted; otherwise, access is denied.

In the main block, the script prompts the user for a username and password, leveraging the getpass module for secure password input. It then calls the login function with the entered credentials and the specified password file.

The script is a straightforward and effective means of user authentication, employing secure password entry practices. However, it lacks user feedback on whether the username was not found, potentially leading to confusion. Including a specific message for such scenarios would enhance user experience.

Overall, the script provides a functional and secure authentication mechanism for verifying user credentials.

In deluser.py
The provided Python script manages user creation, employing the encrypt_password function for secure password storage. The add_user function appends user details, including an encrypted password, to a specified file. In the main block, user input is solicited for a new username, real name, and password. Existing usernames are checked, and if the inputted username already exists, an error message is displayed. Otherwise, the script calls the add_user function, confirming successful user creation. The script showcases modular coding, input validation, and error handling, portraying a reliable tool for user account management. Enhancements could include bolstering security measures and addressing potential file-related issues. Overall, the script efficiently creates user accounts while adhering to good coding practices.

In adduser.py
The Python script facilitates new user creation, utilizing the encrypt_password function from password_util for password security. The add_user function appends user details, including an encrypted password, to a designated file. In the main block, user input is captured for username, real name, and password. The script checks existing usernames to ensure uniqueness, providing an error message if the username already exists. If not, it calls the add_user function, confirming successful user creation. The script demonstrates modular coding, input validation, and error handling. However, it could enhance security features and handle potential file-related issues. Overall, the script is a reliable tool for user account management in its current form.

In passwd.py
The provided Python script allows users to change their passwords securely by verifying the current password, updating it to a new one, and storing the changes in the specified password file.

The script imports functions encrypt_password and check_password from password_util for password encryption and validation. The change_password function reads the password file, searches for the user, and updates the password if the current password is validated. It ensures a valid password file structure and handles potential errors.

In the main block, the script prompts the user for their username, current password, and a new password. It uses the getpass module for secure password entry. The script checks if the new password matches the confirmation and then calls the change_password function. If successful, it confirms the password change; otherwise, it provides appropriate error messages.

The script follows secure password change practices, incorporating modular design and error handling. However, it could further benefit from explicit error messages for mismatched passwords and enhanced user feedback. Overall, it provides a reliable and secure mechanism for users to change their passwords.


